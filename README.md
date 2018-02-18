# Game-launcher

## Description

A small GUI GOG game launcher I did as a personnal Python exercise. It retrieves the games installed in the default installation folder (`$HOME/GOG Games/`) and then creates the interface accordingly, to enable launch and uninstallation.
It was designed primarily for Linux machines, since Windows and macOS can use the GOG Galaxy client.

## Installation

Note that, as said before, it was designed primarily for use on a Linux machine, on which it should work out-of-the-box (assuming it can use the GTK libraries).
Formally, the required libs are :
- `gi`
- `subprocess`,`os` (should be already installed, which is convenient)
- `fnmatch` (might be a default lib too, although I'm not sure)

## Usage
Make sure that the games are installed in `$HOME/GOG Games/` ; if not, just change the occurences in the python file.
Every game folder structure has to look like this :
```
GOG Games/
	[GameName]/
		start.sh
		*uninstall*.sh
		gameinfo
```
Where \* is the wildcard character.

## TO DO
1) Finish the game addition utility
2) Add Wine prefix support
3) Add an overlay ? (yes, the one like steam or gog. Got an idea for that, so why not ? =D )