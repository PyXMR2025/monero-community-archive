---
title: GUI sets refresh-from-block-height to a distant future block
source_url: https://github.com/monero-project/monero/issues/2802
author: stevesbrain
assignees: []
labels: []
created_at: '2017-11-14T03:56:31+00:00'
updated_at: '2017-11-14T12:04:51+00:00'
type: issue
status: closed
closed_at: '2017-11-14T07:08:23+00:00'
---

# Original Description
Hi all,

Just been playing around with testnet, and noticed that the GUI version 0.11.1 for Linux x64 (and Monerujo) both set the wallets `refresh-from-block-height` to a block far in the future (in my testing, approximately 27850 blocks further down the line). I am making the assumption this is not by design, as it has the effect that a transaction sent to the wallet will show as pending, but once assigned a block + confirmed it will disappear. 

Manually setting the refresh-from-block-height to a lower value and then rescanning the blockchain allows the balance to appear.

_In case this is a GUI-code-specific issue (as I suspect it may be) I've cross posted to https://github.com/monero-project/monero-core/issues/955_

# Discussion History
## binaryFate | 2017-11-14T06:32:09+00:00
Fixed in https://github.com/monero-project/monero/pull/2342

## Jaqueeee | 2017-11-14T07:05:40+00:00
+resolved

## stevesbrain | 2017-11-14T12:04:44+00:00
Thanks @binaryFate @Jaqueeee :)

# Action History
- Created by: stevesbrain | 2017-11-14T03:56:31+00:00
- Closed at: 2017-11-14T07:08:23+00:00
