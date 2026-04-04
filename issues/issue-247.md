---
title: Crash on windows when wallet is created/wallet path in config is changed
source_url: https://github.com/monero-project/monero-gui/issues/247
author: medusadigital
assignees: []
labels: []
created_at: '2016-12-07T10:55:22+00:00'
updated_at: '2016-12-09T17:52:19+00:00'
type: issue
status: closed
closed_at: '2016-12-09T17:52:19+00:00'
---

# Original Description
monero-core crashes in the moment a wallet is created or the wallet path in the config gets altered. seems only to affect windows. 

The same issue an also cause a **crash on startup**, if a config registry allready exists in : Computer\HKEY_CURRENT_USER\Software\The Monero Project\monero-core.

last working build i had: https://github.com/Jaqueeee/monero-core/releases

System: win 7 x64 non AVX together with Quick2dRenderer


# Discussion History
## medusadigital | 2016-12-08T12:34:34+00:00
This binary was built by Equation Solution <http://www.Equation.com>.
GNU gdb (GDB) 7.12
Copyright (C) 2016 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-w64-mingw32".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word".
(gdb) target exec C:\Users\ququ\Downloads\monero-core-win32-debug-jaquee\bin\monero-core.exe
(gdb) run
Starting program: C:\Users\ququ\Downloads\monero-core-win32-debug-jaquee\bin\monero-core.exe
[New Thread 3528.0xac8]
warning: Can not parse XML library list; XML support was disabled at compile time
warning: app startd
[New Thread 3528.0x1378]
[New Thread 3528.0x580]
[New Thread 3528.0xf04]
[New Thread 3528.0xd8c]
warning: qrc:///MiddlePanel.qml:259:9: QML StackView: Das Ziel eines Anker muss ein Elternelement oder Element der gleichen Ebene sein.
[New Thread 3528.0x640]
[New Thread 3528.0x99c]
[New Thread 3528.0xf9c]
[New Thread 3528.0x13a0]
[New Thread 3528.0x109c]
[New Thread 3528.0x1384]
[New Thread 3528.0xf0c]
[New Thread 3528.0x1078]
warning: qml: languages availible:  1
warning: qml: Skipping language page until more languages are availible
warning: qml: Language chosen:  US English
warning: qml: switchpage: currentPage:  0
warning: qml: show create wallet page
[New Thread 3528.0x159c]
 
Thread 1 received signal SIGILL, Illegal instruction.
0x0000002b in ?? ()
(gdb) bt
#0  0x0000002b in ?? ()
Backtrace stopped: Cannot access memory at address 0x0
(gdb) kill
Kill the program being debugged? (y or n) y
(gdb)

## medusadigital | 2016-12-08T12:36:12+00:00
seems there are several options that could cause this:

- change of Organisation Name
- Build Env moved to different Hardware 


## Jaqueeee | 2016-12-08T14:38:39+00:00
Fixed in https://github.com/monero-project/monero-core/pull/239

## medusadigital | 2016-12-09T17:52:19+00:00
works-->closed

# Action History
- Created by: medusadigital | 2016-12-07T10:55:22+00:00
- Closed at: 2016-12-09T17:52:19+00:00
