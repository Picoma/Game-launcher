# Game-launcher

## Description

A small GUI gog game launcher I did as a personnal Python exercise. It retrieves the games installed in the default installation folder (set in the config file) and then creates the interface accordingly, to enable launch and uninstallation.
It was designed primarily for Linux machines, since Windows and macOS can use the GOG Galaxy client.

## Installation

Note that, as said before, it was designed primarily for use on a Linux machine, on which it should work out-of-the-box (assuming it can use the GTK libraries).
Formally, the required libs are :
- `gi`
- `subprocess`,`os` (should be already installed, which is convenient)
- `fnmatch` (might be a default lib too, although I'm not sure)

## Usage
Two notes about the usage :
- It needs the config file on the same folder than the python script. This config file is just the path to the "GOG Games" folder (by default, ~/[your_username]/Gog Games, see the file) *followed by another line.* The content of this line doesn't matter, but there needs to be a second line after the "Gog folder" one.
- The game folder structure has to look like this :
```
GOG Games/
	[GameName]/
		start.sh
		*uninstall*.sh
		gameinfo
```
Where \* is the wildcard character.

## TO DO
0) Enhance the UI if I really want to do all of this...

1) Add notifications (ez)
2) Add an icon rescaling utility
3) Add Wine prefix support 
4) Add an overlay (yes, the one like steam or gog. Got an idea for that, so why not ? =D )
5) Add a game addition utility (bunch of code to edit then)
