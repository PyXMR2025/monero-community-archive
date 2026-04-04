---
title: Fix the default size of the wallet's window on high DPI screens
source_url: https://github.com/monero-project/monero-gui/issues/1273
author: bitlamas
assignees: []
labels:
- duplicate
- enhancement
- easy
- Hacktoberfest
created_at: '2018-04-05T12:19:52+00:00'
updated_at: '2020-01-16T03:27:49+00:00'
type: issue
status: closed
closed_at: '2020-01-16T03:27:49+00:00'
---

# Original Description
In a computer running an updated version of Windows 10, with a resolution of 2256 x 1504, when opening the GUI wallet it takes the default size of 971 x 839 (including the title bar). This leads to hiding some information from the bottom part of the screen, as you can see in the image below:

![01-send](https://user-images.githubusercontent.com/34245203/38365241-8e8aef1c-38a9-11e8-97d4-2cab7e77eb86.png)

Ideally, there would be an increase in 18% of the height size. The following image shows a 971 x 995 version (including the title bar):

![01-sendv2](https://user-images.githubusercontent.com/34245203/38365316-d0182242-38a9-11e8-9556-5dd9124fcbb7.png)

I'm unsure if this reproduces in every high DPI screen. Let me know if you need extra info.



# Discussion History
## bitlamas | 2018-04-05T13:11:32+00:00
I've noticed in another computer that this only happens if you have the Advanced options section opened, which is stored somewhere in the wallet. When you re-open the wallet the advanced options keeps open, thus giving the impression that something is mixing.

This is very minor.

## sanderfoobar | 2018-04-09T08:24:32+00:00
+enhancement

## sanderfoobar | 2018-04-09T08:24:35+00:00
+easy

## erciccione | 2018-10-06T15:47:30+00:00
+hacktoberfest

## lorvent | 2018-12-04T13:23:30+00:00
http://doc.qt.io/qt-5/highdpi.html

might be a simple(?) fix

## selsta | 2020-01-16T02:18:10+00:00
#1309 

+duplicate

# Action History
- Created by: bitlamas | 2018-04-05T12:19:52+00:00
- Closed at: 2020-01-16T03:27:49+00:00
