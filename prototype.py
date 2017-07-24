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

def on_appButton_clicked(button):
	FlowBoxChild,FlowBoxParent = button.props.parent, button.props.parent.props.parent
	index=FlowBoxChild.get_index()
	FlowBoxParent.select_child(FlowBoxChild)

def create_lib(flowbox,gameFolderRoot):
	try :
		gameListe=os.listdir(gameFolderRoot)
	except FileNotFoundError :
		return(None)
	global gamePaths
	gamePaths={}
	for index,gameName in enumerate(gameListe) :
		path=gameFolderRoot+gameName
		gamePaths[index]=path
		
		#Generate the application "button"
		box=Gtk.Box(orientation=1)
		icon=Gtk.Image.new_from_file(find(path, "icon*")[0])
		title=Gtk.Label(gameName)
		box.add(icon)
		box.add(title)
		flowbox.add(box)

class Handler:
	def onDeleteMainWindow(self, *args):
		Gtk.main_quit(*args)
	
	def onDeletenewShortcutWindow(self, *args):
		newShortcutWindow.hide()
		newShortcutWindow.unrealize()
		return True

	def on_launch_click(self, button):
		# Get the launch script
		selectedChild=flowbox.get_selected_children()[0]
		requestedPath=gamePaths[selectedChild.get_index()]
		# Creates the environment
		gameEnv=os.environ.copy()
		if GALLIUM_fps.get_active() and GALLIUM_cpu.get_active():
			gameEnv["GALLIUM_HUD"]="fps,cpu"
		else:
			if GALLIUM_cpu.get_active():
				gameEnv["GALLIUM_HUD"]="cpu"
			if GALLIUM_fps.get_active():
				gameEnv["GALLIUM_HUD"]="fps"
			# That part is not really clever, but it works since there's only 2 elements ; maybe i'll rework that if i want to add more arguments
		if disable_compositor.get_active():
			subprocess.Popen(["killall","compton"]) # There is no way to automatically detect the compositor ; replace this command with your own to disable it !
		if WINEDEBUG_Entry.get_text()!="":
			gameEnv["WINEDEBUG"]=WINEDEBUG_Entry.get_text()
		# Creates the processus
		subprocess.Popen([requestedPath+"/start.sh"],env=gameEnv)
		# Creates the notifiation
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
			selectedChildIndex=flowbox.get_selected_children()[0]
			requestedPath=gamePaths[selectedChildIndex.get_index()]
			requestedFile=find(requestedPath,"uninstall*")[0]
			subprocess.Popen([requestedFile])
		confirmDialog.destroy()

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

	def on_new_shortcut_click(self, *args):
		newShortcutWindow.show()
	
	def on_runner_combo_changed(self, runnersCombo):
		NativeLinuxBox.hide()
		Wine_Frame.hide()
		DolphinBox.hide()
		if runnersCombo.get_active_text()=="Linux Natif":
			NativeLinuxBox.show()
		if runnersCombo.get_active_text()=="Wine":
			Wine_Frame.show()
		if runnersCombo.get_active_text()=="Dolphin":
			DolphinBox.show()
	
	def on_new_shortcut_done_click(self,button):
		if runnersCombo.get_active_text()=="Linux Natif":
			NativeLinuxBox.show()
		if runnersCombo.get_active_text()=="Wine":
			Wine_Frame.show()
		if runnersCombo.get_active_text()=="Dolphin":
			DolphinBox.show()
		self.onDeletenewShortcutWindow()

	def WINEDIR_Entry_folder_select(self, entry, icon, eventButton):
		print("WINEDIR Entry selected")
		#return(folder)

	def WINEPREFIX_Entry_folder_select(self, entry, icon, eventButton):
		print("WINEPREFIX Entry selected")
		#return(folder)

builder=Gtk.Builder()
builder.add_from_file("layout.glade")
builder.connect_signals(Handler())

# Main window
window=builder.get_object("window")
flowbox=builder.get_object("flowbox")
GALLIUM_cpu=builder.get_object("GALLIUM_cpu")
GALLIUM_fps=builder.get_object("GALLIUM_fps")
WINEDEBUG_Entry=builder.get_object("WINEDEBUG_Entry")
disable_compositor=builder.get_object("disable_compositor")

# Installation Window
nameEntry=builder.get_object("nameEntry")
newShortcutWindow=builder.get_object("newShortcutWindow")
newShortcutBox=builder.get_object("newShortcutBox")
runnersCombo=builder.get_object("runnersCombo")
Wine_Frame=builder.get_object("Wine_Frame")
NativeLinuxBox=builder.get_object("NativeLinuxBox")
NativeLinuxInstallScriptChooser=builder.get_object("NativeLinuxInstallScriptChooser")
DolphinBox=builder.get_object("DolphinBox")
DolphinIsoChooser=builder.get_object("DolphinIsoChooser")
iconFileChooser=builder.get_object("iconFileChooser")

create_lib(flowbox,os.environ["HOME"]+"/GOG Games/")
create_lib(flowbox,os.environ["HOME"]+"/.games/")

window.show_all()
Gtk.main()