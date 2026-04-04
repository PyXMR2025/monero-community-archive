---
title: Wayland support
source_url: https://github.com/monero-project/monero-gui/issues/1308
author: GarethH96
assignees: []
labels:
- resolved
created_at: '2018-04-11T21:51:15+00:00'
updated_at: '2025-11-29T08:16:23+00:00'
type: issue
status: closed
closed_at: '2018-04-28T17:18:19+00:00'
---

# Original Description
I get this error when trying to run `./start.sh`:
```
This application failed to start because it could not find or load the Qt platform plugin "wayland"
in "".

Available platform plugins are: xcb.

Reinstalling the application may fix this problem.
./start-gui.sh: line 7:  3165 Aborted                 (core dumped) "$SCRIPT_DIR"/monero-wallet-gui
```

# Discussion History
## sanderfoobar | 2018-04-11T22:56:20+00:00
Probably does not support wayland yet.

Could you try running this command: `export QT_QPA_PLATFORM=xcb`

Afterwards `./start.sh`



## pazos | 2018-04-11T23:42:29+00:00
@GarethH96: qt bundled in official binaries only support xcb platform plugin for linux ATM.

if you build monero-wallet-gui from source you'll get more plugins. In my system (Ubuntu 16.04 | x64 | official qt 5.10.1)
```
Available platform plugins are: eglfs, linuxfb, minimal, minimalegl, offscreen, vnc, xcb.
```
official qt binaries don't distribute wayland, but I'm sure new distros build qt with support  for wayland.

So, you can build from source following the readme an give us some feedback :)



## GarethH96 | 2018-04-12T14:44:21+00:00
@skftn That actually works, but really would prefer to have Wayland support.

@pazos I use Antergos KDE which is Arch Linux based, so I have the latest software. Tried cloning and compiling the source of v0.12. At first, it appears to work fine, but when I deleted the .bitmonero folder that was made from the pre-compiled version I get a window that only displays the text 'Weclome to Monero! Please choose a language and regional format' and the rest of the window is completely empty, no matter weather it is on Wayland or X11.

## pazos | 2018-04-21T19:54:51+00:00
> At first, it appears to work fine, but when I deleted the .bitmonero folder that was made from the pre-compiled version I get a window that only displays the text 'Weclome to Monero! Please choose a language and regional format' and the rest of the window is completely empty, no matter weather it is on Wayland or X11.

That is weeeeird

> That actually works, but really would prefer to have Wayland support.

It doesn't matter for the near future. Wayland does support X11 applications via [XWayland ](https://wayland.freedesktop.org/xserver.html) and [qt doesn't bundle wayland](https://wiki.qt.io/QtWayland).

X11 has almost 40 years now, so I think it will be supported at least other 20 years :grinning: 


## sanderfoobar | 2018-04-28T17:01:10+00:00
Closing, #1357 forces xcb which fixes the issue. Wayland will not be supported. PRs always welcome though.

+resolved

## cirosantilli | 2025-11-29T08:09:57+00:00
Sad I still get the issue on Ubuntu 25.10 wayland, it was working on 25.04 previously:

```
~/bin/monero-gui-v0.18.4.4
2025-11-29_08-09-21@ciro@ciro-p14s$ QT_QPA_PLATFORM=xcb ./monero-wallet-gui
Warning: Ignoring XDG_SESSION_TYPE=wayland on Gnome. Use QT_QPA_PLATFORM=wayland to run on Wayland anyway.
Authorization required, but no authorization protocol specified

qt.qpa.xcb: could not connect to display :0
qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.
This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.

Available platform plugins are: xcb, xcb, minimal, offscreen, vnc.

Aborted
~/bin/monero-gui-v0.18.4.4
2025-11-29_08-09-27@ciro@ciro-p14s$ QT_QPA_PLATFORM=wayland ./monero-wallet-gui
Warning: Ignoring XDG_SESSION_TYPE=wayland on Gnome. Use QT_QPA_PLATFORM=wayland to run on Wayland anyway.
qt.qpa.plugin: Could not find the Qt platform plugin "wayland" in ""
This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.

Available platform plugins are: xcb, xcb, minimal, offscreen, vnc.

Aborted
```

Edit: I have the crazy impression that:

```
sudo apt install monero
```

fixed it, despit me still using the manually downloaded prebuilt. Maybe a system dependency was missing?

# Action History
- Created by: GarethH96 | 2018-04-11T21:51:15+00:00
- Closed at: 2018-04-28T17:18:19+00:00
