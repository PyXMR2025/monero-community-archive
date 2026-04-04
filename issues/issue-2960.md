---
title: QR code overlaps GUI on Trezor T display
source_url: https://github.com/monero-project/monero-gui/issues/2960
author: bosomt
assignees: []
labels: []
created_at: '2020-06-17T06:53:24+00:00'
updated_at: '2020-07-01T20:25:17+00:00'
type: issue
status: closed
closed_at: '2020-07-01T20:25:17+00:00'
---

# Original Description
software: Monero GUI 0.16.0.0
hardware: Trezor model T fw version 2.3.1
OS: windows 10 , latest version

How to reproduce:
1) go to receive tam
2) press Show on device
3) device freezes, application freezes

![image](https://user-images.githubusercontent.com/31506317/84864784-7a705380-b077-11ea-89b8-74cb9ab0dc11.png)


# Discussion History
## xiphon | 2020-06-17T11:42:15+00:00
@ph4r05

## rating89us | 2020-06-17T12:53:21+00:00
I'm using Trezor FW 2.3.0 in Monero GUI 0.16.0.0 and I can tap on the buttons below the QR code, but it is really difficult because they are covered.
If I remember correctly, in previous Trezor FW versions you could tap on the QR code to make it disappear.

## ph4r05 | 2020-06-17T13:08:26+00:00
@rating89us I've just tested it and had similar results. Due to the limited space, it is more problematic to hit the button but I succeeded. So I hope it is not a blocker issue, but it is not good for UX for sure. 

I don't think we can scale down the QR code much because it could become unreadable. QR codes for monero addresses are bigger compared to the currencies the QR code was deployed for (e.g., BTC). 

So the question is how it should be handled properly...

## rating89us | 2020-06-17T14:35:49+00:00
It would be better if the QR code were moved down and the bottom buttons hidden while QR code is shown. This would give enough space for the path on top to be displayed.

Tapping or swipping the QR code should make it disappear.

Like this: 
![image](https://user-images.githubusercontent.com/45968869/84911394-5e40d680-b0b8-11ea-96ed-42c3a8d60bcd.png)


## ph4r05 | 2020-06-17T15:13:48+00:00
@rating89us hmm I like the idea that swipe/tap removes the QR code!

## rating89us | 2020-06-17T16:04:15+00:00
I also noticed that the screen of @bosomt's device is a little larger than the screen of my Trezor Model T. Maybe older versions of Model T had a different screen with lower touch sensitivity on the borders.

## tsusanka | 2020-06-27T15:58:30+00:00
@rating89us @ph4r05 have you ever used this feature? I mean the fact that Trezor is capable of showing the QR code. Because I have not and it seems to me as a feature for 0.01% users. So I am actually wondering if we should not remove the QR code completely. What is your take on that?

## tsusanka | 2020-07-01T17:32:08+00:00
Fixed on our side in firmware, https://github.com/trezor/trezor-firmware/commit/0f9a2459d3179da0625c69c9bf601c6692abb7f6. The fix will be most likely included in the next firmware 2.3.2 to be released on August 5th.

Feel free to close this issue.

## selsta | 2020-07-01T20:25:17+00:00
@tsusanka Thank you for the update, closing.

# Action History
- Created by: bosomt | 2020-06-17T06:53:24+00:00
- Closed at: 2020-07-01T20:25:17+00:00
