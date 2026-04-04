---
title: Thread 8 "QSGRenderThread" received signal SIGSEGV, Segmentation fault.
source_url: https://github.com/monero-project/monero-gui/issues/893
author: kolorafa
assignees: []
labels:
- bug
- resolved
created_at: '2017-09-27T19:11:53+00:00'
updated_at: '2018-07-17T15:36:29+00:00'
type: issue
status: closed
closed_at: '2018-07-17T15:36:29+00:00'
---

# Original Description
OS: Arch (Antergos)
Compiled using: monero-wallet-qt (AUR)

Crash right after start.
How can i debug it more?

[kolorafa@kolorafa-newarch ~]$ gdb monero-wallet-qt
GNU gdb (GDB) 8.0.1
Copyright (C) 2017 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-pc-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from monero-wallet-qt...(no debugging symbols found)...done.
(gdb) run
Starting program: /usr/bin/monero-wallet-qt 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/usr/lib/libthread_db.so.1".
[New Thread 0x7fffe89ba700 (LWP 19381)]
[New Thread 0x7fffdaefc700 (LWP 19382)]
app startd
[New Thread 0x7fffda6fb700 (LWP 19383)]
WARNING: Cannot find style "org.kde.desktop" - fallback: "/usr/lib/qt/qml/QtQuick/Controls/Styles/Desktop"
[New Thread 0x7fffcbfff700 (LWP 19384)]
qml: check next false
qml: Checking seed
file:///usr/lib/qt/qml/QtQuick/Dialogs/DefaultFileDialog.qml:210:25: QML ListView: Binding loop detected for property "model"
qml: check next false
file:///usr/lib/qt/qml/QtQuick/Dialogs/DefaultFileDialog.qml:210:25: QML ListView: Binding loop detected for property "model"
file:///usr/lib/qt/qml/QtQuick/Dialogs/DefaultFileDialog.qml:210:25: QML ListView: Binding loop detected for property "model"
qml: check next false
file:///usr/lib/qt/qml/QtQuick/Dialogs/DefaultFileDialog.qml:210:25: QML ListView: Binding loop detected for property "model"
file:///usr/lib/qt/qml/QtQuick/Dialogs/DefaultFileDialog.qml:210:25: QML ListView: Binding loop detected for property "model"
file:///usr/lib/qt/qml/QtQuick/Dialogs/DefaultFileDialog.qml:210:25: QML ListView: Binding loop detected for property "model"
file:///usr/lib/qt/qml/QtQuick/Dialogs/DefaultFileDialog.qml:210:25: QML ListView: Binding loop detected for property "model"
file:///usr/lib/qt/qml/QtQuick/Dialogs/DefaultFileDialog.qml:210:25: QML ListView: Binding loop detected for property "model"
qml: log level changed:  0
file:///usr/lib/qt/qml/QtQuick/Dialogs/DefaultFileDialog.qml:210:25: QML ListView: Binding loop detected for property "model"
file:///usr/lib/qt/qml/QtQuick/Dialogs/DefaultFileDialog.qml:210:25: QML ListView: Binding loop detected for property "model"
[New Thread 0x7fffc8905700 (LWP 19391)]
qml: transfer page loaded
qml: PrivacyLevel changed:0
qml: mixin count: 4
qml: qrScannerEnabled disabled
[New Thread 0x7fffc355f700 (LWP 19392)]
Checking for updates
[New Thread 0x7fffc2520700 (LWP 19393)]
qml: languages availible:  16

Thread 8 "QSGRenderThread" received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0x7fffc2520700 (LWP 19393)]
0x00007fffebca0e30 in ?? () from /usr/lib/libQt5XcbQpa.so.5
(gdb) bt
#0  0x00007fffebca0e30 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#1  0x00007fffebca1387 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#2  0x00007fffebca3529 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#3  0x00007fffebc9ae22 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#4  0x00007fffebca39d3 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#5  0x00007ffff4ddb187 in QFontEngine::alphaMapForGlyph(unsigned int, QTransform const&) () from /usr/lib/libQt5Gui.so.5
#6  0x00007ffff4ddba21 in QFontEngine::alphaMapForGlyph(unsigned int, QFixed, QTransform const&) () from /usr/lib/libQt5Gui.so.5
#7  0x00007fffebca3657 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#8  0x00007fffebc9ae22 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#9  0x00007fffebca39d3 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#10 0x00007ffff4ddb187 in QFontEngine::alphaMapForGlyph(unsigned int, QTransform const&) () from /usr/lib/libQt5Gui.so.5
#11 0x00007ffff4ddba21 in QFontEngine::alphaMapForGlyph(unsigned int, QFixed, QTransform const&) () from /usr/lib/libQt5Gui.so.5
#12 0x00007fffebca3657 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#13 0x00007fffebc9ae22 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#14 0x00007fffebca39d3 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#15 0x00007ffff4ddb187 in QFontEngine::alphaMapForGlyph(unsigned int, QTransform const&) () from /usr/lib/libQt5Gui.so.5
#16 0x00007ffff4ddba21 in QFontEngine::alphaMapForGlyph(unsigned int, QFixed, QTransform const&) () from /usr/lib/libQt5Gui.so.5
#17 0x00007fffebca3657 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#18 0x00007fffebc9ae22 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#19 0x00007fffebca39d3 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#20 0x00007ffff4ddb187 in QFontEngine::alphaMapForGlyph(unsigned int, QTransform const&) () from /usr/lib/libQt5Gui.so.5
#21 0x00007ffff4ddba21 in QFontEngine::alphaMapForGlyph(unsigned int, QFixed, QTransform const&) () from /usr/lib/libQt5Gui.so.5
#22 0x00007fffebca3657 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#23 0x00007fffebc9ae22 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#24 0x00007fffebca39d3 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#25 0x00007ffff4ddb187 in QFontEngine::alphaMapForGlyph(unsigned int, QTransform const&) () from /usr/lib/libQt5Gui.so.5
#26 0x00007ffff4ddba21 in QFontEngine::alphaMapForGlyph(unsigned int, QFixed, QTransform const&) () from /usr/lib/libQt5Gui.so.5
#27 0x00007fffebca3657 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#28 0x00007fffebc9ae22 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#29 0x00007fffebca39d3 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#30 0x00007ffff4ddb187 in QFontEngine::alphaMapForGlyph(unsigned int, QTransform const&) () from /usr/lib/libQt5Gui.so.5
#31 0x00007ffff4ddba21 in QFontEngine::alphaMapForGlyph(unsigned int, QFixed, QTransform const&) () from /usr/lib/libQt5Gui.so.5
#32 0x00007fffebca3657 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#33 0x00007fffebc9ae22 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#34 0x00007fffebca39d3 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#35 0x00007ffff4ddb187 in QFontEngine::alphaMapForGlyph(unsigned int, QTransform const&) () from /usr/lib/libQt5Gui.so.5
#36 0x00007ffff4ddba21 in QFontEngine::alphaMapForGlyph(unsigned int, QFixed, QTransform const&) () from /usr/lib/libQt5Gui.so.5
#37 0x00007fffebca3657 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#38 0x00007fffebc9ae22 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#39 0x00007fffebca39d3 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#40 0x00007ffff4ddb187 in QFontEngine::alphaMapForGlyph(unsigned int, QTransform const&) () from /usr/lib/libQt5Gui.so.5
#41 0x00007ffff4ddba21 in QFontEngine::alphaMapForGlyph(unsigned int, QFixed, QTransform const&) () from /usr/lib/libQt5Gui.so.5
#42 0x00007fffebca3657 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#43 0x00007fffebc9ae22 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#44 0x00007fffebca39d3 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#45 0x00007ffff4ddb187 in QFontEngine::alphaMapForGlyph(unsigned int, QTransform const&) () from /usr/lib/libQt5Gui.so.5
---Type <return> to continue, or q <return> to quit---
#46 0x00007ffff4ddba21 in QFontEngine::alphaMapForGlyph(unsigned int, QFixed, QTransform const&) () from /usr/lib/libQt5Gui.so.5
#47 0x00007fffebca3657 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#48 0x00007fffebc9ae22 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#49 0x00007fffebca39d3 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#50 0x00007ffff4ddb187 in QFontEngine::alphaMapForGlyph(unsigned int, QTransform const&) () from /usr/lib/libQt5Gui.so.5
#51 0x00007ffff4ddba21 in QFontEngine::alphaMapForGlyph(unsigned int, QFixed, QTransform const&) () from /usr/lib/libQt5Gui.so.5
#52 0x00007fffebca3657 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#53 0x00007fffebc9ae22 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#54 0x00007fffebca39d3 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#55 0x00007ffff4ddb187 in QFontEngine::alphaMapForGlyph(unsigned int, QTransform const&) () from /usr/lib/libQt5Gui.so.5
#56 0x00007ffff4ddba21 in QFontEngine::alphaMapForGlyph(unsigned int, QFixed, QTransform const&) () from /usr/lib/libQt5Gui.so.5
#57 0x00007fffebca3657 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#58 0x00007fffebc9ae22 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#59 0x00007fffebca39d3 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#60 0x00007ffff4ddb187 in QFontEngine::alphaMapForGlyph(unsigned int, QTransform const&) () from /usr/lib/libQt5Gui.so.5
#61 0x00007ffff4ddba21 in QFontEngine::alphaMapForGlyph(unsigned int, QFixed, QTransform const&) () from /usr/lib/libQt5Gui.so.5
#62 0x00007fffebca3657 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#63 0x00007fffebc9ae22 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#64 0x00007fffebca39d3 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#65 0x00007ffff4ddb187 in QFontEngine::alphaMapForGlyph(unsigned int, QTransform const&) () from /usr/lib/libQt5Gui.so.5
#66 0x00007ffff4ddba21 in QFontEngine::alphaMapForGlyph(unsigned int, QFixed, QTransform const&) () from /usr/lib/libQt5Gui.so.5
#67 0x00007fffebca3657 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#68 0x00007fffebc9ae22 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#69 0x00007fffebca39d3 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#70 0x00007ffff4ddb187 in QFontEngine::alphaMapForGlyph(unsigned int, QTransform const&) () from /usr/lib/libQt5Gui.so.5
#71 0x00007ffff4ddba21 in QFontEngine::alphaMapForGlyph(unsigned int, QFixed, QTransform const&) () from /usr/lib/libQt5Gui.so.5
#72 0x00007fffebca3657 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#73 0x00007fffebc9ae22 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#74 0x00007fffebca39d3 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#75 0x00007ffff4ddb187 in QFontEngine::alphaMapForGlyph(unsigned int, QTransform const&) () from /usr/lib/libQt5Gui.so.5
#76 0x00007ffff4ddba21 in QFontEngine::alphaMapForGlyph(unsigned int, QFixed, QTransform const&) () from /usr/lib/libQt5Gui.so.5
#77 0x00007fffebca3657 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#78 0x00007fffebc9ae22 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#79 0x00007fffebca39d3 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#80 0x00007ffff4ddb187 in QFontEngine::alphaMapForGlyph(unsigned int, QTransform const&) () from /usr/lib/libQt5Gui.so.5
#81 0x00007ffff4ddba21 in QFontEngine::alphaMapForGlyph(unsigned int, QFixed, QTransform const&) () from /usr/lib/libQt5Gui.so.5
#82 0x00007fffebca3657 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#83 0x00007fffebc9ae22 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#84 0x00007fffebca39d3 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#85 0x00007ffff4ddb187 in QFontEngine::alphaMapForGlyph(unsigned int, QTransform const&) () from /usr/lib/libQt5Gui.so.5
#86 0x00007ffff4ddba21 in QFontEngine::alphaMapForGlyph(unsigned int, QFixed, QTransform const&) () from /usr/lib/libQt5Gui.so.5
#87 0x00007fffebca3657 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#88 0x00007fffebc9ae22 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#89 0x00007fffebca39d3 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#90 0x00007ffff4ddb187 in QFontEngine::alphaMapForGlyph(unsigned int, QTransform const&) () from /usr/lib/libQt5Gui.so.5
#91 0x00007ffff4ddba21 in QFontEngine::alphaMapForGlyph(unsigned int, QFixed, QTransform const&) () from /usr/lib/libQt5Gui.so.5
---Type <return> to continue, or q <return> to quit---
#92 0x00007fffebca3657 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#93 0x00007fffebc9ae22 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#94 0x00007fffebca39d3 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#95 0x00007ffff4ddb187 in QFontEngine::alphaMapForGlyph(unsigned int, QTransform const&) () from /usr/lib/libQt5Gui.so.5
#96 0x00007ffff4ddba21 in QFontEngine::alphaMapForGlyph(unsigned int, QFixed, QTransform const&) () from /usr/lib/libQt5Gui.so.5
#97 0x00007fffebca3657 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#98 0x00007fffebc9ae22 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#99 0x00007fffebca39d3 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#100 0x00007ffff4ddb187 in QFontEngine::alphaMapForGlyph(unsigned int, QTransform const&) () from /usr/lib/libQt5Gui.so.5
#101 0x00007ffff4ddba21 in QFontEngine::alphaMapForGlyph(unsigned int, QFixed, QTransform const&) () from /usr/lib/libQt5Gui.so.5
#102 0x00007fffebca3657 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#103 0x00007fffebc9ae22 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#104 0x00007fffebca39d3 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#105 0x00007ffff4ddb187 in QFontEngine::alphaMapForGlyph(unsigned int, QTransform const&) () from /usr/lib/libQt5Gui.so.5
#106 0x00007ffff4ddba21 in QFontEngine::alphaMapForGlyph(unsigned int, QFixed, QTransform const&) () from /usr/lib/libQt5Gui.so.5
#107 0x00007fffebca3657 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#108 0x00007fffebc9ae22 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#109 0x00007fffebca39d3 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#110 0x00007ffff4ddb187 in QFontEngine::alphaMapForGlyph(unsigned int, QTransform const&) () from /usr/lib/libQt5Gui.so.5
#111 0x00007ffff4ddba21 in QFontEngine::alphaMapForGlyph(unsigned int, QFixed, QTransform const&) () from /usr/lib/libQt5Gui.so.5
#112 0x00007fffebca3657 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#113 0x00007fffebc9ae22 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#114 0x00007fffebca39d3 in ?? () from /usr/lib/libQt5XcbQpa.so.5
#115 0x00007ffff4ddb187 in QFontEngine::alphaMapForGlyph(unsigned int, QTransform const&) () from /usr/lib/libQt5Gui.so.5
#116 0x00007ffff4ddba21 in QFontEngine::alphaMapForGlyph(unsigned int, QFixed, QTransform const&) () from /usr/lib/libQt5Gui.so.5
#117 0x00007fffebca3657 in ?? () from /usr/lib/libQt5XcbQpa.so.5


# Discussion History
## dEBRUYNE-1 | 2017-10-16T19:05:46+00:00
+bug

## dEBRUYNE-1 | 2017-10-27T13:45:03+00:00
Can you try v0.11.1.0?

## sanderfoobar | 2018-07-17T15:23:15+00:00
I'm resolving this issue due the many updates the GUI has received in the meantime. If problem remains on 0.12.2 or 0.12.3, re-open.

+resolved

# Action History
- Created by: kolorafa | 2017-09-27T19:11:53+00:00
- Closed at: 2018-07-17T15:36:29+00:00
