---
title: QR-code on Receive page doesn't seem to work
source_url: https://github.com/monero-project/monero-gui/issues/201
author: peanutsformonkeys
assignees: []
labels: []
created_at: '2016-11-24T21:41:56+00:00'
updated_at: '2016-12-22T21:45:53+00:00'
type: issue
status: closed
closed_at: '2016-12-22T21:45:53+00:00'
---

# Original Description
Trying the [pre-beta](https://github.com/Jaqueeee/monero-core/releases/tag/pre-beta) build. Created a new wallet. The QR-code shown on the "Receive" page doesn't scan with the QR-code [app](http://itunes.apple.com/us/app/scan/id411206394) from [scan.me](https://scan.me) on my smartphone. E.g.:

![gui-qr](https://cloud.githubusercontent.com/assets/21346321/20610244/1e476a62-b297-11e6-96b8-2d205117d19a.png)

For reference, the QR-codes that are generated on [MoneroAddress.org](https://moneroaddress.org), do scan immediately with the same app. Another reddit user encountered the [same issue](https://www.reddit.com/r/Monero/comments/5emgio/unofficial_gui_builds/dae9qzk/). Needs to be looked at.

# Discussion History
## SamsungGalaxyPlayer | 2016-11-24T22:02:09+00:00
I can confirm the same issue. I'm using Barcode scanner (https://play.google.com/store/apps/details?id=com.google.zxing.client.android). This scanner works perfectly with MyMonero.

## moneromooo-monero | 2016-11-24T23:33:05+00:00
https://github.com/monero-project/monero-core/pull/203

## Jaqueeee | 2016-12-19T19:37:00+00:00
@SamsungGalaxyPlayer @peanutsformonkeys can you confirm if #203 (merged to master) fixes this issue? 

## peanutsformonkeys | 2016-12-20T15:49:13+00:00
@Jaqueeee I am now able to scan a (newly) generated QR-code with the [scan.be](https://scan.me/) app on my smartphone:

<img width="250" alt="qr-20161220" src="https://cloud.githubusercontent.com/assets/21346321/21357037/1276a1a2-c6d4-11e6-96e9-7e2194bd6f0d.png">

## peanutsformonkeys | 2016-12-22T21:45:53+00:00
Checked again with the [macOS beta](https://downloads.getmonero.org/gui/monero.gui.mac.x64.beta.tar.bz2).

# Action History
- Created by: peanutsformonkeys | 2016-11-24T21:41:56+00:00
- Closed at: 2016-12-22T21:45:53+00:00
