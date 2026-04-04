---
title: Monero GUI doesn't show up in Ubuntu's list of installed apps
source_url: https://github.com/monero-project/monero-gui/issues/1165
author: Bomper
assignees: []
labels:
- feature
created_at: '2018-03-06T11:43:00+00:00'
updated_at: '2021-05-24T23:47:43+00:00'
type: issue
status: closed
closed_at: '2021-05-24T23:47:43+00:00'
---

# Original Description
![image](https://user-images.githubusercontent.com/34669048/37030622-713fb788-20f0-11e8-9115-d918037f69bb.png)


# Discussion History
## pazos | 2018-03-06T12:07:24+00:00
@Bomper : you don't really install the application. You download it and execute it from its own directory. A proper installation would require place different bits in some specific PATH.

For Debian/Ubuntu/Mint:

binaries  in /usr/bin
libraries (if any) in /usr/lib
app icon in /usr/share/pixmaps
a desktop file in /usr/share/applications

## sanderfoobar | 2018-03-29T23:37:10+00:00
I can see the GUI having a 'create desktop icon' feature on the platforms @pazos mentioned.

## sanderfoobar | 2018-03-29T23:37:18+00:00
+feature

## ITwrx | 2018-04-01T22:27:01+00:00
Here's the icon and desktop file i use for distros/installs using gnome (i'm using it with Arch Linux). 

copy the text below and create a file as /usr/share/applications/monero-gui.desktop (for all users to access)
or ~/.local/share/applications/monero-gui.desktop (for just your user). make sure the path and monero filename match your location and monero version.

[Desktop Entry]
Comment=Monero Client
Exec=/home/username/Downloads/monero-gui-v0.11.1.0/start-gui.sh
GenericName[en_US]=Monero Wallet
GenericName=Monero Wallet
Icon=monero-gui
Name[en_US]=Monero Wallet
Name=Monero Wallet
Categories=Finance;Network;
StartupNotify=false
Terminal=true
Type=Application

download this: https://imgur.com/a/NpuCc

and copy it to /usr/share/pixmaps. 
maybe check to make sure your .desktop file and icon match the permissions of the other files in the two respective locations. 

## scottAnselmo | 2020-04-20T00:29:51+00:00
For what it's worth, this issue concerning a Monero GUI .desktop file, even now that it's included in the Arch community repo is still happening:

https://old.reddit.com/r/Monero/comments/fcabhs/running_monero_client_on_arch_linux/

Running `monero-wallet-gui` in terminal will obviously launch it, but not having a proper .desktop does hinder adoption/ease of use.

## selsta | 2021-05-24T23:47:43+00:00
The GUI offers you to install a .desktop file on first start.

# Action History
- Created by: Bomper | 2018-03-06T11:43:00+00:00
- Closed at: 2021-05-24T23:47:43+00:00
