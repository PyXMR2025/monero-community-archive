---
title: Trouble with Windows 10 GUI Wallet and CLI monerod
source_url: https://github.com/monero-project/monero/issues/2136
author: DavidJNowak
assignees: []
labels:
- invalid
created_at: '2017-06-30T23:30:06+00:00'
updated_at: '2017-08-09T20:18:13+00:00'
type: issue
status: closed
closed_at: '2017-08-09T20:18:13+00:00'
---

# Original Description
Help!
I would like to run a monero full node on the blockchain.

I downloaded both the "Windows, 64-bit (GUI Beta 2)" and the "Windows, 64-bit (Command-Line Tools Only)" from https://getmonero.org/downloads/.

When I started the GUI version, it askes for my wallet and password.  Then the program goes and looks for the server.  When I can not find the server, it puts up a dialog box wht the message: "Daemon failed to start.  Please check your wallet and daemon log for errors. You can also try to start monerod.exe manually.".

Then I opend a cmd window, changed directories to the directory I unzipped the CLI programs into.  I received a warning and failures message.

I have include screen dumps of each.

My next step would be to recompile the monerod from scratch, but I am not a programmer.  I did install msys2, but am unfamiliar with how to download and compile the code from github.

Please help me.
![monero daemon start message](https://user-images.githubusercontent.com/13257104/27756970-349b4ea8-5db1-11e7-8362-09d4323f7ce4.PNG)
![mymonerowallet not connect window](https://user-images.githubusercontent.com/13257104/27756972-38e71d8e-5db1-11e7-87f4-3669edf7a9af.PNG)
![monerd windows startup failure](https://user-images.githubusercontent.com/13257104/27756988-58b509b4-5db1-11e7-9930-6379e95cfdc6.PNG)
![monerd windows startup and import failures](https://user-images.githubusercontent.com/13257104/27756990-5d51d97a-5db1-11e7-99c8-1a198eba1fc7.PNG)





# Discussion History
## Jaqueeee | 2017-07-01T07:41:40+00:00
Looks like your database is corrupt. Did you have a crash prior to this?
Remove the lmdb folder` C:\ProgramData\Bitmonero\lmdb`, restart monerod.exe and it should start syncing. 

## moneromooo-monero | 2017-08-09T10:07:50+00:00
Corrupt DB, so not a bug.

+invalid

## moneromooo-monero | 2017-08-09T20:16:05+00:00
+resolved

# Action History
- Created by: DavidJNowak | 2017-06-30T23:30:06+00:00
- Closed at: 2017-08-09T20:18:13+00:00
