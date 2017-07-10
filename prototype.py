#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Notify', '0.7')
from gi.repository import Gtk, Notify
import subprocess, os, fnmatch

Notify.init("Game Launcher")

def find(path, file):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, file):
                result.append(os.path.join(root, name))
    return result

def read_config(config_path="./config"):
	configFile=open(config_path,"r")
	config=configFile.readlines()
	configFile.close()
	
	gogIndex=0
	for index,path in enumerate(config) :
		if "GOG folder" in path :
			gogIndex=index
	gogPath=config[gogIndex].split(":")[1]
	if gogPath[-1]=="\n":
		gogPath=gogPath[:-1]
	return(gogPath)

def on_appButton_clicked(widget):
	FlowBoxChild,FlowBoxParent = widget.props.parent, widget.props.parent.props.parent
	index=FlowBoxChild.get_index()
	FlowBoxParent.select_child(widget.props.parent)
	# Updating description
	gameinfoFile=open(gamePaths[index]+"/gameinfo","r")
	gameinfo=gameinfoFile.read()
	gameinfoFile.close()
	description.set_text(gameinfo)

def create_lib(flowbox):
	gogPath=read_config()
	proc=subprocess.Popen(['ls',gogPath],stdout=subprocess.PIPE)
	liste=str(proc.stdout.read())[2:-1].split("\\n")[:-1] # "b'day-mode.sh\nnight-mode.sh\nprototype.py\n'" -> ['day-mode.sh', 'night-mode.sh', 'prototype.py']
	global gamePaths
	gamePaths={}
	for index,pathname in enumerate(liste) :
		path=gogPath+pathname
		gamePaths[index]=path
		
		#Generate the application button
		button=Gtk.Button(label=pathname)
		button.connect("clicked",on_appButton_clicked)
		button.set_image(Gtk.Image.new_from_file(path+"/game/icon.png"))
		button.set_image_position(Gtk.PositionType.TOP)
		flowbox.add(button) # ... and adds it to the flowbox

class Handler:
	def onDeleteWindow(self, *args):
		Gtk.main_quit(*args)

	def on_launch_click(self, button):
		selectedChild=flowbox.get_selected_children()[0]
		requestedPath=gamePaths[selectedChild.get_index()]
		
		subprocess.Popen([requestedPath+"/start.sh"]) #The starting script always has the same name, it seems
		
		GameName=requestedPath.split("/")[-1]
		iconPath=find(requestedPath,"*icon*")[0]
		launched_notif=Notify.Notification.new("Game launched :", GameName, iconPath)
		launched_notif.show()
	
	def on_uninstall_click(self, button):
		# First run the confirmation dialog
		confirmDialog = Gtk.MessageDialog(window, 0, Gtk.MessageType.QUESTION,
			Gtk.ButtonsType.YES_NO, "Confirmation")
		confirmDialog.format_secondary_text("Do you want to uninstall this game ?")
		response = confirmDialog.run()
		if response == Gtk.ResponseType.YES:
			# Then run the uninstallation script
			selectedChildIndex=flowbox.get_selected_children()[0] # Only one child is selectable, as set on the .glade structure
			requestedPath=gamePaths[selectedChildIndex.get_index()]
			requestedFile=find(requestedPath,"uninstall*")[0] #Assuming there is only one "uninstall"-like file. The "find" function is necessary because there can be different names for this file.
			subprocess.Popen([requestedFile])

		confirmDialog.destroy()

	def on_open_gog_click(self, *args):
		subprocess.Popen(["exo-open", "https://www.gog.com"])
	
	def on_install_click(self, *args):
		loadDialog = Gtk.FileChooserDialog("Select the installer :", window,
		Gtk.FileChooserAction.OPEN,
		(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
		Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

		response = loadDialog.run()
		if response == Gtk.ResponseType.OK:
			try :
				subprocess.Popen([loadDialog.get_filename()])
			except OSError :
				errorDialog = Gtk.MessageDialog(window, 0, Gtk.MessageType.ERROR,
				Gtk.ButtonsType.CANCEL, "Erreur :")
				errorDialog.format_secondary_text(
					"Le script d'installation n'a pas pu être executé.\nL'installateur possède-t-il un header correct (#!/bin/bash par exemple) ?")
				errorDialog.run()
				errorDialog.destroy()
		loadDialog.destroy()

builder=Gtk.Builder()
builder.add_from_file("layout.glade")
builder.connect_signals(Handler())

window=builder.get_object("window")
flowbox=builder.get_object("flowbox")
description=builder.get_object("description")
create_lib(flowbox)

window.show_all()
Gtk.main()