---
title: Text cursor always on focus
source_url: https://github.com/monero-project/monero-gui/issues/2924
author: pijcab
assignees: []
labels: []
created_at: '2020-05-26T02:13:40+00:00'
updated_at: '2020-07-08T18:53:54+00:00'
type: issue
status: closed
closed_at: '2020-07-08T18:53:54+00:00'
---

# Original Description
The text cursor for the wallet password text field is always blinking like the GUI is in focus even when it's not on Widows.
This has led me to type multiple times my password on a Discord chat which was in focus instead of the wallet...
I don't know if I'm the only one having this issue or not but this is infuriating, I've changed my password like 5 times this month.

# Discussion History
## selsta | 2020-05-26T02:15:40+00:00
What OS are you using? I can’t reproduce this on my system (macOS), the cursor only blinks when in focus.

## rating89us | 2020-05-26T07:14:55+00:00
Can't reproduce on Windows and Discord chat.

## pijcab | 2020-05-26T20:06:32+00:00
Hi,
It doesn't happen all the time but here is an exemple : https://i.imgur.com/FEm8hUX.png
As you can see Discord is in focus, but the Monero GUI cursor is still blinking (just like Discord's).
I'm on W10, as you can see I have a 2 monitor setup, which could be causing this issue

Update : and now after I've posted this comment, the issue is gone (for now). I don't know how to replicate it either to be honest.

Update 2 : I managed to replicate it, steps to follow : 

- Have the Monero GUI app open and **not minimized**

- Have the `lock wallet on inactivity after x mins` option **on** (after 1 min for this instance)

- Switch focus to another app window (Discord, Web browser, File Explorer etc...)

- Wait for wallet to auto lock itself

Another result exemple : (file explorer is in focus) https://i.imgur.com/BD1GjGM.png

## sanderfoobar | 2020-07-07T13:34:58+00:00
I was able to reproduce the bug and PR a fix.

## pijcab | 2020-07-08T15:26:25+00:00
Damn, I was looking at that specific line in the .qml file but I didn't know how to fix it... 😅 

Thank you for the fix !

# Action History
- Created by: pijcab | 2020-05-26T02:13:40+00:00
- Closed at: 2020-07-08T18:53:54+00:00
