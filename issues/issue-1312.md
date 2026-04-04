---
title: Linux doesn't show Monero icon on Show Applications
source_url: https://github.com/monero-project/monero-gui/issues/1312
author: cialu
assignees: []
labels: []
created_at: '2018-04-13T07:01:41+00:00'
updated_at: '2018-04-17T16:13:30+00:00'
type: issue
status: closed
closed_at: '2018-04-17T16:13:30+00:00'
---

# Original Description
Hi,
I have downloaded source of **monero-wallet-gui** (v0.12.0.0 - Lithium Luna) from here and installed it on **Linux Ubuntu 18.04** system with communitheme(the next Ubuntu theme in development). I compiled the code and moved the executable to `/opt` folder, then I made a `monero-gui.desktop` file in `/home/user/.local/share/applications/`.

This is the `monero-gui.desktop` file:

```
[Desktop Entry]
Name=Monero GUI wallet
Comment=Monero: the secure, private, untraceable cryptocurrency
Exec=/opt/monero/monero-wallet-gui
Icon=monero
Terminal=false
Type=Application
StartupNotify=true
```
                 
Everything went fine and all is working. The node connect itself to the network and the GUI wallet works like a charm. Just, one minor graphical issue.

The **monero-wallet-gui** application shows the correct icon on the dock when it's opened, but in 'Show Application' there's no Monero icon. I know that I specified `Icon=monero` and the default theme doesn't provide a Monero icon, so I also look into Monero folder to make a link to the right icon, but I found no icon file.

Here the monero-wallet-gui icon on the dock:
![monero-dock](https://user-images.githubusercontent.com/1382127/38720624-3f820afa-3ef7-11e8-98dd-0ecc438dd49f.png)

Here the wrong icon on 'Show Applications':
![screenshot from 2018-04-13 08-34-04](https://user-images.githubusercontent.com/1382127/38720639-4eb4e8d0-3ef7-11e8-8fb2-adc818c88554.png)

Is there a way to provide a Monero icon to link to?

~~Also I'm wondering, should I open an issue upstream to insert Monero (and crypto in general) icon in the default Ubuntu theme?~~ I also opened this [How about to insert Monero and Crypto icons in the theme?](https://github.com/snwh/suru-icon-theme/issues/41) on the next Ubuntu icons theme repository.

# Discussion History
## pazos | 2018-04-13T16:39:15+00:00
duplicate of #1165.

You'll need to copy the icon you want to /usr/share/pixmaps/monero.png

The monero icon on the taskbar is qt stuff. Linux binaries (elf files) don't have an icon embedded, so instead we follow the freedesktop way of doing things :)

## cialu | 2018-04-14T10:02:14+00:00
@pazos thanks. I have already placed an icon in the theme folder and it worked as your proposed solution. I also opened an issue upstream to insert the Monero icon directly in the standard Ubuntu icons theme.

The #1165 is a different issue, it's regarding the Ubuntu Software application, instead I was talking about the 'Show Application' function in the GNOME desktop environment. 

## pazos | 2018-04-17T16:00:59+00:00
@cialu: I'm glad it worked.

This issue is indeed related to #1165. This isn't about linux distros, because every linux distro out there is based on freedesktop and its [desktop entry specification](https://specifications.freedesktop.org/desktop-entry-spec/desktop-entry-spec-1.1.html).

So please close this issue, thanks :)

## cialu | 2018-04-17T16:13:30+00:00
Ok, sure.

# Action History
- Created by: cialu | 2018-04-13T07:01:41+00:00
- Closed at: 2018-04-17T16:13:30+00:00
