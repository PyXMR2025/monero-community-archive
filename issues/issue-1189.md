---
title: Monero-Gui default screen, and Items order...
source_url: https://github.com/monero-project/monero-gui/issues/1189
author: juanpc2018
assignees: []
labels:
- wontfix
created_at: '2018-03-19T17:39:43+00:00'
updated_at: '2018-04-04T17:18:19+00:00'
type: issue
status: closed
closed_at: '2018-04-04T17:18:19+00:00'
---

# Original Description
seems to me that the Top Left Menu in the GUI, should be History...
inside History: Send, Receive & Address.

Send 1st does not make sense.
Address Hidden also strange... at least should be outside, like Send & Receive.

# Discussion History
## sanderfoobar | 2018-03-29T21:49:46+00:00
pinging @GBKS

## GBKS | 2018-03-30T20:32:32+00:00
Considering Send and Receive are the primary functions of a wallet, don't you think they should be immediately visible? 

## juanpc2018 | 2018-03-31T04:17:55+00:00
seems to me that the Top Left Menu should be History...
after 
History:
Receive,
Send,
Address,
Config.

Send 1st does not make sense, to me..
Address Hidden also strange... at least should be outside, like Send & Receive.
Or in both ? Or All 3 H,S&R.

Play/Stop Daemon should be a global button... that can be seen from any menu.
Give the user the ability to Pin Windows.
Move up or down, top or bottom.
Not everybody thinks like me.,

When syncing the Daemon most of the times the GUI gives a false positive "Connected Progrees Bar",
The true way to know if it's truly synced is:
A) press start mining.......
or
B) task manager hard drive activity....

A way to detect HardDrive activity like task manager should combined to give a proper reading.
NOT + AND Gate Logic.
also detecting the true last block independently from another source + Comparator....

## sanderfoobar | 2018-04-04T06:20:31+00:00
On the subject of the menu, even though I agree with your reasoning I don't believe the menu should be reordered at this point.

As for the other suggestions, they ought to be in separate issues. Please note you can always submit a PR for changes, regardless of what I or anyone thinks :)

## sanderfoobar | 2018-04-04T17:13:16+00:00
+wontfix

# Action History
- Created by: juanpc2018 | 2018-03-19T17:39:43+00:00
- Closed at: 2018-04-04T17:18:19+00:00
