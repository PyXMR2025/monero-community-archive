---
title: QR-code on black background is difficult to scan
source_url: https://github.com/monero-project/monero-gui/issues/1262
author: Starmute
assignees: []
labels:
- bug
created_at: '2018-04-04T15:38:34+00:00'
updated_at: '2019-05-03T19:02:01+00:00'
type: issue
status: closed
closed_at: '2018-05-07T20:48:52+00:00'
---

# Original Description
GUI version: v0.12.0.0

OS: macOS 10.13.1

Reproducibility: Always

Steps:

1. Open GUI to 'receive' section.

2. Scan QR code.

Issue: The QR code cannot be scanned by most QR code scanning software because it is on a black background without border. To mitigate, add a white border around the QR code.

Expected result: QR code scans and produces proper address.

# Discussion History
## SamsungGalaxyPlayer | 2018-04-04T16:43:39+00:00
Reproduced using the Windows GUI and Monerujo. Does not scan the QR code.

## sanderfoobar | 2018-04-04T17:09:00+00:00
+bug

## LesterCovax | 2018-04-04T22:58:44+00:00
I think I found the issue.  I haven't looked through the code yet to see where it's happening though.  It wouldn't read the code in Monerujo for me either, but it worked fine in a QR code scanner (after a while).

Black background shouldn't matter.  QR codes are very resilient to things like that.  They'll work with the colors inverted and even with a large portion of the QR code missing (depending on the QR version).  

I [decoded it into a raw value](http://www.onlinebarcodereader.com/) and compared it to a generated QR code online and the GUI QR code seems to be missing some data.

### Text Content (for both)
`monero:83yiuYLUk1kdPyPLeNx9S73nFYqjKYtGG8dqEUonmaghMUFjE931BNBNgBggXhGBqxeL99BmXuo6yJwL1SAL8cbEB698TEp`

### GUI hex values
`6d 6f 6e 65 72 6f 3a 38 33 79 69 75 59 4c 55 6b 31 6b 64 50 79 50 4c 65 4e 78 39 53 37 33 6e 46 59 71 6a 4b 59 74 47 47 38 64 71 45 55 6f 6e 6d 61 67 68 4d 55 46 6a 45 39 33 31 42 4e 42 4e 67 42 67 67 58 68 47 42 71 78 65 4c 39 39 42 6d 58 75 6f 36 79 4a 77 4c 31 53 41 4c 38 63 62 45 42 36 39 38 54 45 70`
![screenshot from 2018-04-04 17-45-50](https://user-images.githubusercontent.com/34850610/38338922-a156bc90-3839-11e8-8226-e91a57bfd6a2.png)

### Generated QR hex values
`6d 6f 6e 65 72 6f 3a 38 33 79 69 75 59 4c 55 6b 31 6b 64 50 79 50 4c 65 4e 78 39 53 37 33 6e 46 59 71 6a 4b 59 74 47 47 38 64 71 45 55 6f 6e 6d 61 67 68 4d 55 46 6a 45 39 33 31 42 4e 42 4e 67 42 67 67 58 68 47 42 71 78 65 4c 39 39 42 6d 58 75 6f 36 79 4a 77 4c 31 53 41 4c 38 63 62 45 42 36 39 38 54 45 70 0a `
![screenshot from 2018-04-04 18-08-30](https://user-images.githubusercontent.com/34850610/38338901-8b727784-3839-11e8-9989-7f4560bf2735.png)

### Diff
`0a`, which appears to be a LF / Line Feed in Hex.  I compared this to some other generators and it's the same result.  It's not the QR version/format as I originally thought.

## sanderfoobar | 2018-04-05T10:06:49+00:00
Looking at `pages/Receive.qml` we find a `qrCode` image component.

https://github.com/monero-project/monero-gui/blob/76a105261e4ce60555931b4b2dfe1c6a25971825/pages/Receive.qml#L378

It uses `makeQRCodeString()` to generate a valid qr code string. I debugged this, in my case the output of that javascript function was: `monero:A1eTt937UiPG2YznHoejJkLtJbUK21gUML3JHF6K3R8K7hY6Qfwow62brQFnYc2QQeZ6gn1srwtwPAKfxzPMMw7fHDUP1c8`, which does not seem to include line feeds (`s.indexOf('\x0a') === -1`). 

I'm guessing the error is somewhere in the C++ code that handles the `image://qrcode/...` part.




## sanderfoobar | 2018-04-05T10:45:20+00:00
Are both QR codes for primary address and sub addresses broken?

## Starmute | 2018-04-05T17:43:29+00:00
@skftn Yes. Cake refuses to scan subaddress QR codes.

## pazos | 2018-04-23T00:12:18+00:00
Using white color [here](https://github.com/monero-project/monero-gui/blob/master/pages/Receive.qml#L46) solves the problem for me, so adding white margins (about 4px) to the qrcode will do the job.

If @skftn doesn't have time I'll try to implement this before the next release

## jakeqr2019 | 2019-05-03T19:02:01+00:00
Same problem in https://www.qrcode-monkey.com with: Black Background+logo_Image+Color_ Gradient+Custom_Eye_Color
Even with a good contrast using only black & white and without an image logo: QR can not be readed

# Action History
- Created by: Starmute | 2018-04-04T15:38:34+00:00
- Closed at: 2018-05-07T20:48:52+00:00
