---
title: Starting monero-core accesses the webcam for a split second
source_url: https://github.com/monero-project/monero-gui/issues/611
author: ddyzhang
assignees: []
labels: []
created_at: '2017-03-26T08:33:56+00:00'
updated_at: '2017-03-28T23:50:19+00:00'
type: issue
status: closed
closed_at: '2017-03-28T23:50:19+00:00'
---

# Original Description
Starting the latest build of monero-core on win64, I can see my webcam activity light come on for a second or two before turning off. This only happens when launching monero-core. Quite concerning.

Platform is Windows 10 x64, webcam is a Logitech C920.

# Discussion History
## SamsungGalaxyPlayer | 2017-03-26T10:28:38+00:00
I can confirm this too with [build #677](https://build.getmonero.org/builders/monero-core-win64/builds/677). 

Windows 10 x64, built-in HP TrueVision HD on an HP Pavillion dv6.

## dternyak | 2017-03-26T16:43:01+00:00
Can confirm occurs on macOs 10.11 as well. 

## MoroccanMalinois | 2017-03-26T17:01:41+00:00
Sorry guys, this one is on me !
To add a QR Code scanner, i had to add a dependency to QtMultimedia (to access the camera).
I was not expecting it to do anything when the flag `WITH_SCANNER` is not activated. 
Looks like https://github.com/monero-project/monero-core/blob/master/main.qml#L35 is already too much.
It is a little painful to do conditional includes in QML, and it will make the code a little more complex. 
But now, i have a good reason for it :) 

## Jaqueeee | 2017-03-28T16:49:10+00:00
@SamsungGalaxyPlayer @dternyak @ddyzhang Can you confirm that this is fixed?

## ddyzhang | 2017-03-28T16:56:10+00:00
@Jaqueeee Haven't had a chance to test the latest build yet, will test when I get home.

From skimming the PR, it seems like we are simply moving the decision to include QR scanning to compile time. Is there any way to preserve QR code scanning in all builds, but only attempt to access the webcam when we are actually scanning? I'm assuming no, since it appears that qt is populating the available webcam list at start up.

## MoroccanMalinois | 2017-03-28T17:34:30+00:00
@ddyzhang dunno, I think it might be doable, but not necessarily a good thing. 

First, it relies on 2 new dependencies : libzbar and QtMultimedia. Libzbar has been reported to work on all majors platforms, yet i am not sure that it works with the 13 (11 in build bots, + android and ios) builds environnements. It was already skipped at compil time. I think that's the reason we did not see people complaining about it. 
Also, QtMultimedia is quite a heavy lib, with multiple dependencies (like gstreamer). So, this complexifies the build (we already saw multiple people complaining about  erros due to QtMultimedia) and produces a significantly bigger binary. 

Second, for now, i don't see any use case to scan a qrcode in a laptop or desktop camera.
Eventually, it might be interesting to use it as an RPC between a non networked computer (acting as a cold storage) and a networked computer (acting as a view only wallet), for example, to forward a cold signed transaction or get the key images. But these would be marginal use cases. 


## ddyzhang | 2017-03-28T17:37:08+00:00
@MoroccanMalinois Fair enough, thanks for your input! I've never used Qt much myself, so I'll trust your judgement on this one. Again, will test the new build when I get home.

## ddyzhang | 2017-03-28T23:50:19+00:00
Confirmed, issue fixed by PR #616, monero-core also starts a lot quicker now too!

# Action History
- Created by: ddyzhang | 2017-03-26T08:33:56+00:00
- Closed at: 2017-03-28T23:50:19+00:00
