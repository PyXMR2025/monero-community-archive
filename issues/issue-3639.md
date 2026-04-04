---
title: Grab QR code button doesn't work if QR code is below Monero GUI window
source_url: https://github.com/monero-project/monero-gui/issues/3639
author: rating89us
assignees: []
labels: []
created_at: '2021-07-23T05:00:14+00:00'
updated_at: '2021-07-26T18:10:44+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
v0.17.2.2. Seen on Ubuntu and Windows (my grab QR code button isn't working on Mac)

# Discussion History
## selsta | 2021-07-24T19:10:55+00:00
Can you try master? I'm quite sure this was fixed in #3598

## rating89us | 2021-07-25T03:16:10+00:00
This issue also occurs with master and was not fixed in #3598. 

It seems to be related with the C++ code of grab QR code button. It minimizes Monero GUI window for less than a second, and then takes a screenshot. It seems to be taking this screenshot before the window is fully minimized, so adding a delay/waiting for the window to minimize will probably solve the problem.

## selsta | 2021-07-25T13:40:15+00:00
Does it only happen on Ubuntu?

## rating89us | 2021-07-25T16:10:07+00:00
No, this issue also happens on Windows. 
I tested on Mac, but the grab QR code button isn't working at all.

## selsta | 2021-07-25T16:11:16+00:00
It's working for me on Mac. You have to give the application screen recording permission.

## selsta | 2021-07-25T16:12:06+00:00
Maybe I need better steps to reproduce, e.g. the exact QR code used.

## rating89us | 2021-07-25T16:54:12+00:00
This is on Ubuntu, using QR code from https://grapheneos.org/donate:
![grabQRUbuntu](https://user-images.githubusercontent.com/45968869/126906996-6c7ffa9b-608a-4762-8443-257a051863bb.gif)


## selsta | 2021-07-25T17:00:30+00:00
Hmm, unable to reproduce on Mac. Works fine here. No matter where the GUI window is.

## rating89us | 2021-07-25T17:05:44+00:00
On Ubuntu, if I click outside the Monero GUI window while it's being minimized, it works.
![doubleclickqrcode](https://user-images.githubusercontent.com/45968869/126907299-0611d28a-f5d6-47ea-9963-ab3f84e8f3ab.gif)


## rating89us | 2021-07-25T17:07:31+00:00
I have this problem on Windows 7 and Ubuntu 21.04
Maybe we could keep Monero GUI window minimized for 1 second and only then take the screenshot?

## selsta | 2021-07-25T17:21:09+00:00
Do you have multiple monitors?

## rating89us | 2021-07-25T17:43:54+00:00
> Do you have multiple monitors?

No.

I don't think it's related, but i'm using low graphics mode on Ubuntu and OpenGL on Windows.

## selsta | 2021-07-26T18:10:44+00:00
Can you reproduce on Mac if:

System Preferences -> Security & Privacy -> Privacy -> Screen Recording -> Allow `monero-wallet-gui` and `Terminal`?

# Action History
- Created by: rating89us | 2021-07-23T05:00:14+00:00
