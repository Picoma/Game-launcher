#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import subprocess, os, fnmatch

gladeLayout="""<?xml version="1.0" encoding="UTF-8"?>
<!-- Generated with glade 3.20.0 -->
<interface>
  <requires lib="gtk+" version="3.20"/>
  <object class="GtkWindow" id="window">
    <property name="width_request">1000</property>
    <property name="height_request">618</property>
    <property name="can_focus">False</property>
    <property name="halign">start</property>
    <property name="valign">start</property>
    <property name="window_position">center</property>
    <property name="gravity">center</property>
    <property name="has_resize_grip">True</property>
    <signal name="delete-event" handler="onDeleteWindow" swapped="no"/>
    <child>
      <object class="GtkAlignment">
        <property name="visible">True</property>
        <property name="can_focus">False</property>
        <property name="top_padding">10</property>
        <property name="bottom_padding">10</property>
        <property name="left_padding">10</property>
        <property name="right_padding">10</property>
        <child>
          <object class="GtkBox">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <property name="spacing">10</property>
            <child>
              <object class="GtkFlowBox" id="flowbox">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="halign">start</property>
                <property name="valign">start</property>
                <property name="homogeneous">True</property>
                <property name="max_children_per_line">4</property>
                <property name="activate_on_single_click">False</property>
              </object>
              <packing>
                <property name="expand">True</property>
                <property name="fill">True</property>
                <property name="position">0</property>
              </packing>
            </child>
            <child>
              <object class="GtkBox">
                <property name="width_request">400</property>
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="orientation">vertical</property>
                <child>
                  <object class="GtkFrame">
                    <property name="visible">True</property>
                    <property name="can_focus">False</property>
                    <property name="label_xalign">0</property>
                    <property name="shadow_type">out</property>
                    <child>
                      <object class="GtkAlignment">
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="left_padding">12</property>
                        <child>
                          <object class="GtkLabel" id="description">
                            <property name="visible">True</property>
                            <property name="can_focus">False</property>
                            <property name="label" translatable="yes">Select a
game</property>
                            <property name="justify">center</property>
                          </object>
                        </child>
                      </object>
                    </child>
                    <child type="label">
                      <object class="GtkLabel">
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="label" translatable="yes"> Description :</property>
                      </object>
                    </child>
                  </object>
                  <packing>
                    <property name="expand">True</property>
                    <property name="fill">True</property>
                    <property name="position">0</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkAlignment">
                    <property name="visible">True</property>
                    <property name="can_focus">False</property>
                    <property name="top_padding">10</property>
                    <property name="bottom_padding">10</property>
                    <property name="left_padding">10</property>
                    <property name="right_padding">10</property>
                    <child>
                      <object class="GtkGrid">
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="halign">center</property>
                        <property name="valign">center</property>
                        <property name="row_spacing">10</property>
                        <property name="column_spacing">10</property>
                        <property name="row_homogeneous">True</property>
                        <property name="column_homogeneous">True</property>
                        <child>
                          <object class="GtkButton">
                            <property name="label" translatable="yes">Launch</property>
                            <property name="visible">True</property>
                            <property name="can_focus">True</property>
                            <property name="receives_default">True</property>
                            <signal name="clicked" handler="on_launch_click" swapped="no"/>
                          </object>
                          <packing>
                            <property name="left_attach">0</property>
                            <property name="top_attach">0</property>
                          </packing>
                        </child>
                        <child>
                          <object class="GtkButton">
                            <property name="label" translatable="yes">Uninstall</property>
                            <property name="visible">True</property>
                            <property name="can_focus">True</property>
                            <property name="receives_default">True</property>
                            <signal name="clicked" handler="on_uninstall_click" swapped="no"/>
                          </object>
                          <packing>
                            <property name="left_attach">1</property>
                            <property name="top_attach">0</property>
                          </packing>
                        </child>
                        <child>
                          <object class="GtkButton">
                            <property name="label" translatable="yes">Open Gog.com</property>
                            <property name="visible">True</property>
                            <property name="can_focus">True</property>
                            <property name="receives_default">True</property>
                            <signal name="clicked" handler="on_open_gog_click" swapped="no"/>
                          </object>
                          <packing>
                            <property name="left_attach">0</property>
                            <property name="top_attach">1</property>
                          </packing>
                        </child>
                        <child>
                          <object class="GtkButton">
                            <property name="label" translatable="yes">Install a game</property>
                            <property name="visible">True</property>
                            <property name="can_focus">True</property>
                            <property name="receives_default">True</property>
                            <signal name="clicked" handler="on_install_click" swapped="no"/>
                          </object>
                          <packing>
                            <property name="left_attach">1</property>
                            <property name="top_attach">1</property>
                          </packing>
                        </child>
                      </object>
                    </child>
                  </object>
                  <packing>
                    <property name="expand">False</property>
                    <property name="fill">False</property>
                    <property name="position">1</property>
                  </packing>
                </child>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">True</property>
                <property name="position">1</property>
              </packing>
            </child>
          </object>
        </child>
      </object>
    </child>
  </object>
</interface>
"""

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
	gogPath=config[gogIndex].split(":")[1][:-1]
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
		selectedChildrenIndex=flowbox.get_selected_children()
		requestedPath=gamePaths[selectedChildrenIndex[0].get_index()]
		subprocess.Popen(["bash", requestedPath+"/start.sh"]) #The starting script always has the same name, it seems
	
	def on_uninstall_click(self, button):
		# First run the confirmation dialog
		confirmDialog = Gtk.MessageDialog(window, 0, Gtk.MessageType.QUESTION,
			Gtk.ButtonsType.YES_NO, "Confirmation")
		confirmDialog.format_secondary_text("Voulez-vouz désinstaller ce jeu de votre ordinateur ?")
		response = confirmDialog.run()
		if response == Gtk.ResponseType.YES:
			# Then run the uninstallation script
			selectedChildIndex=flowbox.get_selected_children()[0] # Only one child is selectable, as set on the .glade structure
			requestedPath=gamePaths[selectedChildIndex.get_index()]
			requestedFile=find(requestedPath,"uninstall*")[0] #Assuming there is only one "uninstall"-like file. The "find" function is necessary because there can be different names for this file.
			subprocess.Popen(["bash", requestedFile])

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
builder.add_from_string(gladeLayout)
builder.connect_signals(Handler())

window=builder.get_object("window")
flowbox=builder.get_object("flowbox")
description=builder.get_object("description")
create_lib(flowbox)

window.show_all()
Gtk.main()