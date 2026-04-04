---
title: Monero GUI v0.12 behaves as "always on top" window in Xubuntu 16.04.4 in VirtualBox
source_url: https://github.com/monero-project/monero-gui/issues/1431
author: bananajamma
assignees: []
labels:
- resolved
created_at: '2018-05-26T01:45:41+00:00'
updated_at: '2019-07-13T06:36:35+00:00'
type: issue
status: closed
closed_at: '2019-07-13T06:36:35+00:00'
---

# Original Description
## Information and Steps to Reproduce

On Xubuntu 16.04.4, when first opening the GUI v0.12 [build 201](https://build.getmonero.org/builders/monero-gui-ubuntu-amd64/builds/201), the file dialog is behind the Monero GUI, which behaves as "always on top", over any other GTK dialog, action menu, or application.

![monero-always-on-top](https://user-images.githubusercontent.com/37884555/40571187-6fdf7c46-6062-11e8-8b0b-7fdb9ca3c178.png)

The Monero GUI appears to be "frozen".

A work-around is to right-click the application on the xfce4-panel, and select "move" to gain access to the file dialog:

![monero-xubuntu-move-workaround](https://user-images.githubusercontent.com/37884555/40571186-6fd62db2-6062-11e8-84c6-acb3e0f4a08d.png)

## System Information

Running inside of VirtualBox 5.2.12:

```
bj@xubuntu$ cat /etc/lsb-release 
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=16.04
DISTRIB_CODENAME=xenial
DISTRIB_DESCRIPTION="Ubuntu 16.04.4 LTS"
```
```
bj@xubuntu$ dpkg -l "*ubuntu-desktop" |grep ii
ii  xubuntu-desktop 2.206        amd64        Xubuntu desktop system
```
```
bj@xubuntu$ xfce4-about --version
xfce4-about 4.12.1 (Xfce 4.12)

Copyright (c) 2008-2015
	The Xfce development team. All rights reserved.

Please report bugs to <http://bugzilla.xfce.org/>.
Translators list from 2015-03-15 16:44:46.
```

```
bj@xubuntu$ uname -a
Linux xubuntu 4.13.0-43-generic #48~16.04.1-Ubuntu SMP Thu May 17 12:56:46 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux
```

# Discussion History
## dEBRUYNE-1 | 2018-05-26T09:58:29+00:00
Similar to #1096 and #1097 it seems. 

## bananajamma | 2018-05-26T15:23:56+00:00
**edit:** this comment was based on the incorrect assumption that monero-gui uses electron

~Thanks for those two related issues.  They were labeled `won't fix` with blame placed on the Window Manager.  However, if you compare Monero with another Electron application, such as [boostnote](https://github.com/BoostIO/Boostnote), the "z-index" problem doesn't exist.~

![boostnote](https://user-images.githubusercontent.com/37884555/40577623-b0931350-60d6-11e8-9da8-498f284b5c55.png)

~This leads me to believe this is perhaps a configuration, or dependency issue within this specific Electron application (monero-gui).~

I was unable to find anything related in ~[electron's issue tracker](https://github.com/electron/electron/issues), or~ [xfce's bugtracker](https://bugzilla.xfce.org/buglist.cgi?quicksearch=monero).

## sanderfoobar | 2018-05-26T15:46:23+00:00
Thanks for reporting. Please note monero-gui uses QT and not Electron, so you wont find it there ^^

Will look into this at a later stage, unless someone else does. 

## bananajamma | 2018-05-26T16:02:12+00:00
@skftn egg on my face.  I made an assumption based on the UI, I should have looked closer at the source code.  Thanks for pointing out the error in my assessment.  I'll look into some QT bugs and see if I come with anything similar as well.

## bananajamma | 2018-05-26T22:14:20+00:00
Ubuntu 18.04 has a similar issue in GNOME.  However, the work-around doesn't work, the file open dialog appears to move with the application itself, so it's never able to retrieve focus.

![ubuntu-18 04-monero-bug](https://user-images.githubusercontent.com/37884555/40580637-86964fa6-6110-11e8-8016-af438dc40fce.png)

I also tried other qt applications in XFCE on 16.04.4, keepassx (qt4) and phototonic (qt5.5).  These did not have the z-order issue.

Please let me know if there are any test cases you'd like me to try.  Thanks.

## sanderfoobar | 2018-05-26T22:29:03+00:00
Could you try a more recent build? [441](https://build.getmonero.org/builders/monero-gui-ubuntu-amd64/builds/441) for example. Just to make sure.

## bananajamma | 2018-05-26T23:10:42+00:00
I was able to resolve the issue in both 16.04.4 and 18.04 by disabling "3d acceleration" in my VirtualBox VM settings.

Edited the issue title to specify VirtualBox now, as I'm not sure if this is strictly related to the other bugs, or not.  It could be OpenGL related/video driver issues.

![ubuntu-18 04-monero-works-no-3d](https://user-images.githubusercontent.com/37884555/40580925-9f57db92-6118-11e8-91c6-81b16fca8719.png)

The bug is still reproducible with build 441 in VirtualBox on either version of [X]ubuntu when "3d acceleration" is enabled.  Guest Additions is installed via the "CD version" that ships with VirtualBox, not from the [older] ubuntu repositories.

I'd like to add that I've noticed focus can still given to the application behind the Monero GUI if I tried to bring it in front.  Also, I could click through to the "browse", or "cancel" buttons on the file open dialog, if I knew where they were behind the splash screen where you select a wallet file to open.

edit: I believe this bug is related, as I can reproduce with blender when 3d acceleration is on https://www.virtualbox.org/ticket/12738

## pazos | 2018-05-27T04:47:22+00:00
@bananajamma : mmmm interesting bug. Can you reproduce this without custom decorations?

Vbox->3daccel->start_gui->settings->disable custom decorations. I wouldn't expect the window on top.

## bananajamma | 2018-05-27T14:19:58+00:00
Sorry @pazos, I don't see that option anywhere in VirtualBox, or the OS Settings.  Can you clarify?

edit: I figured out what you meant.  Enable 3d acceleration in VirtualBox; then in the Monero GUI, go to Settings, and uncheck "custom decorations"

This did not fix the window priority, but I was able to move the Monero GUI using the title bar, where I cannot always with the cusom decorations

![custom-decorations-off](https://user-images.githubusercontent.com/37884555/40589448-5c47c88c-61bb-11e8-856e-8434066c769c.png)



## pazos | 2018-06-09T20:10:50+00:00
@bananajamma: thanks for the feedback.

If you are still interested in running the gui without disabling experimental HW accel on VBox you can force software render for the gui with `QT_OPENGL=software ./monero-wallet-gui` from an open terminal. This should fix your problem, since it forces the same behaviour for monero-wallet-gui as running it without HW accel.

## dEBRUYNE-1 | 2019-07-04T06:34:26+00:00
@bananajamma - Can you check if this still happens with GUI v0.14.1.0?

## dEBRUYNE-1 | 2019-07-12T16:09:58+00:00
@bananajamma - ping. 

## SamsungGalaxyPlayer | 2019-07-12T18:24:46+00:00
No updates from the user since July 2018, please close.

## dEBRUYNE-1 | 2019-07-13T06:24:24+00:00
+resolved

# Action History
- Created by: bananajamma | 2018-05-26T01:45:41+00:00
- Closed at: 2019-07-13T06:36:35+00:00
