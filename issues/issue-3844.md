---
title: I cannot start the GUI via X11 forwarding
source_url: https://github.com/monero-project/monero-gui/issues/3844
author: kaizushi
assignees: []
labels: []
created_at: '2022-02-23T05:22:24+00:00'
updated_at: '2023-01-18T06:02:05+00:00'
type: issue
status: closed
closed_at: '2023-01-18T06:02:05+00:00'
---

# Original Description
I am trying to run the Monero GUI for the latest version via X11 forwarding and it does not work. I am used to such issues and for example to run the Chromium web browser this way I would launch it with `chromium --disable-gpu` for that to work. I am trying to run the Monero GUI from a Debian bullseye guest on a Fedora host. I like to compartmentalize software I use with libvirt virtual machines and use them with X11 forwarding on SSH.

This is what Monero does when I try to run it via X11 forwarding...

```
2022-02-23 05:21:04.151 W Qt:5.15.2 GUI:- | screen: XXXXxXXXX - available: QSize(3840, 2160) - dpi: 120 - ratio:1.24201
libGL error: No matching fbConfigs or visuals found
libGL error: failed to load driver: swrast
2022-02-23 05:21:04.467 W QGLXContext: Failed to create dummy context
2022-02-23 05:21:06.289 W qrc:/qt-project.org/imports/QtQuick/Controls/ApplicationWindow.qml:259:9: QML ContentItem: Binding loop detected for property "implicitWidth"
2022-02-23 05:21:06.318 E Failed to create OpenGL context for format QSurfaceFormat(version 2.0, options QFlags<QSurfaceFormat::FormatOption>(), depthBufferSize 24, redBufferSize -1, greenBufferSize -1, blueBufferSize -1, alphaBufferSize -1, stencilBufferSize 8, samples -1, swapBehavior QSurfaceFormat::DoubleBuffer, swapInterval 1, colorSpace QSurfaceFormat::DefaultColorSpace, profile  QSurfaceFormat::NoProfile) 
Aborted
```
 
I redacted my screen resolution in the above console output from `monero-wallet-gui`

# Discussion History
## selsta | 2022-02-23T19:45:44+00:00
Try to start with `QMLSCENE_DEVICE=softwarecontext` env var.

## oliverlj | 2022-08-15T07:44:35+00:00
Having this issue in local on lubuntu 22.04 on latest release 0.18.1.0

the ```QMLSCENE_DEVICE=softwarecontext``` works good

## oliverlj | 2022-08-15T07:53:14+00:00
Working good after a reboot because of an nvidia driver update

## nosfirlabs | 2022-08-15T17:57:55+00:00
@oliverlj did the same, still does not work. any fixes?

## selsta | 2022-08-15T17:59:01+00:00
@nosfirlabs please stay in a single issue. Can you post more information:

- Which OS
- Which hardware
- How did you install monero-gui

## selsta | 2023-01-18T06:02:05+00:00
Closing due to inactivity and no reply from issue creator.

# Action History
- Created by: kaizushi | 2022-02-23T05:22:24+00:00
- Closed at: 2023-01-18T06:02:05+00:00
