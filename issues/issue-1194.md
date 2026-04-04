---
title: Undefined error; could not load wallet (will show zero balance)
source_url: https://github.com/monero-project/monero-gui/issues/1194
author: sanderfoobar
assignees: []
labels:
- bug
- resolved
created_at: '2018-03-21T02:16:46+00:00'
updated_at: '2019-11-12T00:10:36+00:00'
type: issue
status: closed
closed_at: '2019-11-11T23:36:37+00:00'
---

# Original Description
From reading Reddit, some users sometimes report not seeing their balance. This can happen in multiple ways, of which I've found one. To reproduce:

1. Open the GUI, load up a wallet that has a balance
2. Settings -> close wallet
3. Create a new wallet, move through the wizards, continue into the GUI
4. Settings -> close wallet
5. Open the wallet from step 1

At this point, it will fail [on this line](https://github.com/monero-project/monero-gui/blob/e39ea7119f8acc03556df83b867659449e97ab49/main.qml#L260) with `undefined does not have attribute 'path'` which leaves the GUI in limbo, not able to update the balance text due the javascript attribute error.

I've coded this solution in the meantime: [link](https://github.com/monero-project/monero-gui/pull/952/commits/81330da44f5609cb67915012c671922e23d6962f). It shows a message and closes the GUI so you can restart it.

A real solution would be to figure out why the `wallet` variable is `undefined`.

# Discussion History
## Jaqueeee | 2018-03-21T06:02:24+00:00
This is only reproducible on master right? So not related to the zero balance issue users are reporting on Reddit who are using the official binaries. Needs to be fixed until next release nevertheless!

## sanderfoobar | 2018-03-21T13:30:07+00:00
Yep, current master. Not sure about the official bins.

## sanderfoobar | 2018-03-29T21:19:31+00:00
+bug

## selsta | 2019-11-11T22:50:42+00:00
I think this got fixed in the meantime? I can’t reproduce this.

+resolved

## sanderfoobar | 2019-11-12T00:06:07+00:00
@selsta bug was "fixed" by closing the GUI.

https://github.com/monero-project/monero-gui/blob/5df14abed26f415984bdfe306e4a073d289665d2/main.qml#L327-L335

Actual bug is not resolved. I'd say keep this open.

## selsta | 2019-11-12T00:10:36+00:00
Can you reproduce it using the 5 steps you described above?

-resolve

# Action History
- Created by: sanderfoobar | 2018-03-21T02:16:46+00:00
- Closed at: 2019-11-11T23:36:37+00:00
