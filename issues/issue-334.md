---
title: Win64 Wallet Crashes Not Usable
source_url: https://github.com/monero-project/monero-gui/issues/334
author: allegro101
assignees: []
labels: []
created_at: '2016-12-22T17:03:42+00:00'
updated_at: '2016-12-23T17:33:03+00:00'
type: issue
status: closed
closed_at: '2016-12-23T17:33:03+00:00'
---

# Original Description
GUI Wizard crashes when asked to open a wallet from file. Never given the chance to specify the file. 

If using the wizard to create a new wallet the wallet is created but program crashes when the Use Monero button is clicked.

# Discussion History
## relics219 | 2016-12-22T17:48:55+00:00
I'm using the x64 wallet and it's not crashing for me at that point. Maybe check another computer?

## Jaqueeee | 2016-12-22T18:48:11+00:00
@allegro101 
Can you start cmd.exe and run the wallet in there? 
```
cd <your gui location>
monero-wallet-gui.exe > log.txt 
```
Hopefully it will give us some debug info in log.txt

## allegro101 | 2016-12-22T19:53:58+00:00
Jaqueeee I can run the wallet from the command window but when I use the 'open wallet from file' option GUI quits with error msg that GUI has stopped working. For some reason I cannot get any debug information saved to a log file. Wish I could provide more help. 

## Jaqueeee | 2016-12-22T20:02:16+00:00
ok. It would help a lot if you could download [GDB](https://sourceforge.net/projects/mingw-w64/files/External%20binary%20packages%20(Win64%20hosted)/gdb/) debugger and start gui with that. 
from cmd:
```
gdb monero-wallet-gui.exe
(gdb) run
```
after crash you can type `thread apply all bt full` to get the stack trace. Copy that info to https://paste.fedoraproject.org and link here. 

## allegro101 | 2016-12-22T21:38:37+00:00
Sorry have not been able to decipher using gdb perhaps someone else with the same problem can contribute.

## medusadigital | 2016-12-23T06:30:33+00:00
@allegro101 you can use like this:

- open gdb
- "target exec C:\path\to\bins\monero-wallet-gui.exe"
-  "run"

## Jaqueeee | 2016-12-23T11:42:32+00:00
@allegro101  Please also try using the software renderer described here:
http://monero.stackexchange.com/questions/2928/how-to-change-the-monero-core-rendering-mode-for-older-computers/2929#2929

## allegro101 | 2016-12-23T17:24:41+00:00
Problem solved. deBRUYNE posted a fix at /r/Monero that is directed at older computers but solved the problem on my new one details at [this link](https://www.reddit.com/r/Monero/comments/5jwteb/psa_if_the_beta_gui_is_not_working_on_your/) 

# Action History
- Created by: allegro101 | 2016-12-22T17:03:42+00:00
- Closed at: 2016-12-23T17:33:03+00:00
