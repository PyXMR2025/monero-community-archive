---
title: Icon missing causing small taskbar area
source_url: https://github.com/monero-project/monero-gui/issues/4006
author: f2ph7z02sdb
assignees: []
labels: []
created_at: '2022-08-16T14:01:33+00:00'
updated_at: '2024-11-07T22:56:52+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
LMDE 5  Elsie (Debian Bullseye)
Cinnamon Version 5.4.10
monero-gui-v0.18.1.0

Icon missing causing small taskbar area

![noicon](https://user-images.githubusercontent.com/111281626/184898731-7700d16d-5e8f-4f6c-81e4-fd2e35199d07.png)


Also no icon in the start menu entry therefor also no icon when creating a desktop shortcut


# Discussion History
## selsta | 2022-08-16T17:27:43+00:00
On first start it asks you if you want to create a desktop entry. What did you press? And how did you install monero-gui?

## f2ph7z02sdb | 2022-08-17T18:15:59+00:00
yes but it has also no icon

![yes2](https://user-images.githubusercontent.com/111281626/185212925-5630bea9-5968-4ef9-96f1-4a6c88d5c1c0.png)

> And how did you install monero-gui?

Download from official website extract and run


## nahuhh | 2022-08-30T17:05:03+00:00
I can confirm the **menu** not having an icon assigned.
I installed v18.0.0 for a friend a couple weeks back, clicked the button to add to menus and although the taskbar _did_,  the menu entry had no icon.

Was using Linux Mint 21



## selsta | 2022-10-02T20:44:14+00:00
The GUI follows this spec: https://wiki.archlinux.org/title/desktop_entries

So far this issue seems to be limited to Linux Mint.

## plowsof | 2022-12-19T01:53:15+00:00
as per selstas comment^ icons are searched for in 3 locations:

- $HOME/.icons (for backwards compatibility)
- $XDG_DATA_DIRS/icons
- /usr/share/pixmaps (requires root)

Simply placing `monero.png` inside `$HOME/.icons` solves the issue. The only problem is Linux Mint DE (what i tested) does not have an `.icons` folder by default so you must create it first if not exists and place the image there:

```bash
if [[ ! -d "$HOME/.icons" ]]
then
    mkdir "$HOME/.icons"
fi
wget -O "$HOME/.icons/monero.png" "https://raw.githubusercontent.com/monero-project/monero-gui/master/images/appicons/64x64.png
```
<details>
  <summary>short clip</summary>

  [mint-screen0.webm](https://user-images.githubusercontent.com/77655812/208332570-bfae7850-2f75-469a-b8b9-ec40003cc3cd.webm)

</details>

perhaps related to #2291 (TIL about XDG dirs and the above is just a hack fix^ )

## nahuhh | 2022-12-19T04:50:05+00:00
Ubuntu 22.04 doesn't have that folder either (also no icon)

## Botspot | 2023-05-17T14:18:01+00:00
If the goal is to keep monero-gui as portable as possible with minimal changes to the outside system, then the desktop file can specify the full path to an icon png file.
In `~/.local/share/applications/monero-gui.desktop`, change this line from:
```
Icon=monero
```
To:
```
Icon=/home/pi/monero-gui/images/appicon.ico
```
Your home directory will be different, so please change it accordingly.

I tested this to work on the LXDE desktop. Full paths to icons in .desktop files is uncommon and may not be supported on other desktop environments.

## S5NC | 2024-04-02T09:35:53+00:00
From the `monero-gui-v0.18.3.3` path, run `./monero-wallet-gui`. Does the icon show up then? For me the icon doesn't show up when using the desktop entry, but shows up when running that command.

## taltamir | 2024-11-07T22:40:01+00:00
On Mint 22, restarting the computer made the wallet show the icon in the taskbar while running. Before the restart it was showing a blank square with `...`

# Action History
- Created by: f2ph7z02sdb | 2022-08-16T14:01:33+00:00
