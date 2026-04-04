---
title: Wallet gui crashes on Pop OS
source_url: https://github.com/monero-project/monero-gui/issues/3366
author: jonatino
assignees: []
labels: []
created_at: '2021-03-23T22:27:58+00:00'
updated_at: '2024-02-28T02:23:33+00:00'
type: issue
status: closed
closed_at: '2021-03-31T22:04:04+00:00'
---

# Original Description
GPU Driver: nvidia-driver-460 v460.56
OS: Pop OS 20.10
Monero version: 0.17.1.9

The gui fails to start, the following is the crash log.

```
user@pop-os:~/Desktop/monero-gui-v0.17.1.9$ ./monero-wallet-gui
2021-03-23 22:26:06.236	W Qt:5.15.2 GUI:0.17.1.9-3ca5f10 | screen: 2560x1440 - dpi: 96 - ratio:86.5187
2021-03-23 22:26:06.419	W QGLXContext: Failed to create dummy context
2021-03-23 22:26:07.307	W qrc:/qt-project.org/imports/QtQuick/Controls/ApplicationWindow.qml:259:9: QML ContentItem: Binding loop detected for property "implicitWidth"
2021-03-23 22:26:07.316	E Failed to create OpenGL context for format QSurfaceFormat(version 2.0, options QFlags<QSurfaceFormat::FormatOption>(), depthBufferSize 24, redBufferSize -1, greenBufferSize -1, blueBufferSize -1, alphaBufferSize -1, stencilBufferSize 8, samples -1, swapBehavior QSurfaceFormat::DoubleBuffer, swapInterval 1, colorSpace QSurfaceFormat::DefaultColorSpace, profile  QSurfaceFormat::NoProfile) 
Aborted (core dumped)
```

# Discussion History
## jonatino | 2021-03-23T22:28:42+00:00
Launching in software mode works.

`QMLSCENE_DEVICE=softwarecontext ./monero-wallet-gui`

## selsta | 2021-03-23T22:29:30+00:00
Can you try updating / reinstalling GPU drivers?

## jonatino | 2021-03-31T22:04:04+00:00
After running once with software mode, hardware mode works correctly now.

## technout | 2021-06-13T20:06:43+00:00
I got the same kind of error at starting up the gui on Ubuntu 20.04.2 with kernel 5.4.0-72-generic
Monero version: 0.17.2.1-8444a95
NVidia driver: 460.73.01 with dual monitor setup!

2021-06-13 19:52:37.693	W Qt:5.15.2 GUI:0.17.2.1-8444a95 | screen: 1680x1050 - dpi: 96 - ratio:0.70362
2021-06-13 19:52:38.062	W QGLXContext: Failed to create dummy context
2021-06-13 19:52:41.461	W qrc:/qt-project.org/imports/QtQuick/Controls/ApplicationWindow.qml:259:9: QML ContentItem: Binding loop detected for property "implicitWidth"
2021-06-13 19:52:41.487	E Failed to create OpenGL context for format QSurfaceFormat(version 2.0, options QFlags<QSurfaceFormat::FormatOption>(), depthBufferSize 24, redBufferSize -1, greenBufferSize -1, blueBufferSize -1, alphaBufferSize -1, stencilBufferSize 8, samples -1, swapBehavior QSurfaceFormat::DoubleBuffer, swapInterval 1, colorSpace QSurfaceFormat::DefaultColorSpace, profile  QSurfaceFormat::NoProfile) 
Aborted (core dumped)

How to execute this line?
QMLSCENE_DEVICE=softwarecontext ./monero-wallet-gui
I got: bash: ./monero-wallet-gui: No such file or directory
Edit: Fixed it with the correct path to monero-wallet-gui

After the first time running monero-wallet-gui with QMLSCENE_DEVICE=softwarecontext, then the next times monero-wallet-gui will run correctly without errors!

## nosfirlabs | 2022-08-15T17:56:17+00:00
i have the same problem

## selsta | 2022-08-15T17:57:45+00:00
@nosfirlabs can you follow the steps in the previous comments?

## nosfirlabs | 2022-08-15T17:59:41+00:00
i updated gpu drivers
i set the env variable
i rebooted

![image](https://user-images.githubusercontent.com/80362772/184689862-61ee7ba0-61b5-42b7-9c29-7ca595917063.png)


## nosfirlabs | 2022-08-15T18:02:50+00:00
Ubuntu 20.04.4 LTS
X11
monero-gui-v0.18.1.0


## selsta | 2022-08-15T18:03:15+00:00
I don't see any crash in your screenshot.

## nosfirlabs | 2022-08-15T18:04:57+00:00
@selsta the proccess seems to be running but the window is popping up for a second and then its gone. i have 4 monitors, its visible in taskbar and i can also see it and select it by pressing SUPER + TAB
but i can not focus or get it to show

## selsta | 2022-08-15T18:05:48+00:00
what happens when you only connect 1 monitor for testing purposes?

## nosfirlabs | 2022-08-15T18:09:25+00:00
@selsta that works. but thats not a accetable status quo

## selsta | 2022-08-15T18:10:09+00:00
I did not claim that this is acceptable, I was just trying to find out what the issue is...

## nosfirlabs | 2022-08-15T18:11:00+00:00
@selsta didn't mean to sound like a asshole. But im pretty sure im not the only one having more than one monitor. are there best practices or anything to follow?


## selsta | 2022-08-15T18:12:13+00:00
Can you test how many monitors it takes until the issue starts showing up?

## nosfirlabs | 2022-08-15T18:17:21+00:00
Only seems to be working with one monitor

## selsta | 2022-08-15T18:33:23+00:00
Which window manager are you using? Is there a move window to current display shortcut or something similar?

## nosfirlabs | 2022-08-30T17:57:20+00:00
> Which window manager are you using? Is there a move window to current display shortcut or something similar?

I am using gdm3. It still does not work, i have tried logging monero output and  journalctl   also doesnt show anything

## selsta | 2022-08-31T01:08:44+00:00
@nosfirlabs Can you post the complete Terminal output? The previous screenshot is missing the beginning.

## oneEyedCharlie | 2024-02-28T02:22:52+00:00
For anyone encountering this for the first time on Ubuntu in 2024 after an NVidia driver update, jonatino's response in the second post above works.

# Action History
- Created by: jonatino | 2021-03-23T22:27:58+00:00
- Closed at: 2021-03-31T22:04:04+00:00
