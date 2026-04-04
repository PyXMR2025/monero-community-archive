---
title: Support 4K displays
source_url: https://github.com/monero-project/monero-gui/issues/1309
author: Warchant
assignees: []
labels:
- enhancement
created_at: '2018-04-12T07:26:22+00:00'
updated_at: '2021-01-08T05:05:35+00:00'
type: issue
status: closed
closed_at: '2021-01-08T05:05:35+00:00'
---

# Original Description
This is how `monero-gui` (`v0.12.0.0`, Windows 10) looks like on my laptop's 4K display (Dell XPS 15 9560):

![image](https://user-images.githubusercontent.com/1867551/38661994-7b73c1fa-3e3b-11e8-8d5a-a026bebca1df.png)

![image](https://user-images.githubusercontent.com/1867551/38662013-8eae9c22-3e3b-11e8-9128-721c19618883.png)

Please, add scaling. 

# Discussion History
## medusadigital | 2018-04-12T09:23:14+00:00
Hei @Warchant, you need to enter application Zoom yourself. 

right click on monero-wallet-gui.exe, select properties --> compatibility.

then there is a high DPI option, change value there from "Application" to "System" or vice versa 

## SamsungGalaxyPlayer | 2018-04-12T21:42:46+00:00
Yes, follow the instructions as @medusadigital said, selecting "System" or "System (Advanced)".

## pazos | 2018-04-13T01:56:54+00:00
[HiDPI support for windows](https://vicrucann.github.io/tutorials/osg-qt-high-dpi/) seems [portable to X11/android](http://blog.qt.io/blog/2016/01/26/high-dpi-support-in-qt-5-6/).  a little different for [osx](http://blog.qt.io/blog/2013/04/25/retina-display-support-for-mac-os-ios-and-x11/)

please leave this issue open as an enhancement,
thanks!

## sanderfoobar | 2018-04-18T13:19:51+00:00
+enhancement

## pazos | 2018-05-08T17:35:08+00:00
@Warchant : I think I found a way to fix that in Windows. Since I don't have any hiDPI screens I cannot test. Would you want to test that for me? In that case I will submit a PR :taco: 

## valiant1x | 2018-05-16T20:10:25+00:00
@pazos we would also appreciate your test [here](https://github.com/valiant1x/intensecoinwallet) - feel free to submit a PR 😄 

## pazos | 2018-05-17T01:10:54+00:00
Sorry, I have no incentive to do stuff for your forked coin. But if you have a windows machine and a hidpi screen and want to test stuff please ping me :slightly_smiling_face: 

## valiant1x | 2018-05-17T02:03:06+00:00
We contribute upstream as well when able. Open source doesn't have to be a one way street! In any case, I am on a 1440p monitor and am happy to test.

## QuickBASIC | 2019-08-03T15:16:53+00:00
I just got a high density screen and there's a way we could work around this on Windows without mucking with QT DPI scaling.

@medusadigital is on the right track, but it might be confusing to new users to have to do this on first run. (4k screens are becoming more and more common, my cheap $1300 laptop has one, so it's not just enthusiasts, programmers, and artists that might end up having one.)
 
We could have the GUI provide an option to write the compatibility options to the registry directly w/ a command line switch and/or a checkbox in the GUI.

For an individual user: 
`HKEY_CURRENT_USER\Software\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Layers`

For all users: 
`HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Layers`

The value is `~ DPIUNAWARE` for the setting that was suggested.

Or include a batch (like the we already do for 'start-low-graphics-mode.bat') that sets the key. Example:
```
@ECHO OFF
::Sets compatibility settings for high DPI screens for the Monero Wallet GUI (only need to run once).
::This makes changes to your Registry.
::To set for all users, change 'HKCU' to 'HKLM' (run as administrator)
REG ADD "HKCU\Software\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Layers" /V %cd%\monero-wallet-gui.exe /T REG_SZ /D "~ DPIUNAWARE" /F
```

## selsta | 2019-08-12T17:19:20+00:00
Thanks @QuickBASIC,

I’m currently trying to get it working in Qt, if I don’t figure it out we can look into a `.bat`.

## selsta | 2020-01-16T02:18:31+00:00
#2670 

Will leave this open until release binaries ship with Qt 5.14

## selsta | 2021-01-08T05:05:35+00:00
With v0.17.1.9 all our binaries support high DPI.

# Action History
- Created by: Warchant | 2018-04-12T07:26:22+00:00
- Closed at: 2021-01-08T05:05:35+00:00
