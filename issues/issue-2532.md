---
title: Monero GUI Windows 10 64bit - crashed during wallet sync
source_url: https://github.com/monero-project/monero/issues/2532
author: TrojanZA
assignees: []
labels: []
created_at: '2017-09-26T09:30:41+00:00'
updated_at: '2018-03-13T08:21:13+00:00'
type: issue
status: closed
closed_at: '2017-10-15T18:30:20+00:00'
---

# Original Description
Hi

Not sure if this is the right place to log this, please redirect if I should be going elsewhere.

I ran monero-wallet-gui this morning. All going well, wallet opened and was doing the refresh, where it started hanging at around 30k blocks left. Have opened the CLI and sync completed without a hitch. 

# Discussion History
## moneromooo-monero | 2017-09-26T10:24:39+00:00
Can you get a stack trace of the crash ?
If the wallet hanged and something crashed, it's monerod that crashed. I can't give instructions for windows though, so if you don't know how, ignore it. If it was a moneord crash, it's most likely fixed on master though.

## moneromooo-monero | 2017-10-02T19:15:46+00:00
Please test with new master, where 2492 is merged, and a likely fix for your crash.

## moneromooo-monero | 2017-10-10T11:47:55+00:00
2492 is now merged, so testing current master will use the patch.

## moneromooo-monero | 2017-10-15T18:25:23+00:00
No more info, and the crash is likely 2492, closing.

+resolved

## BernhardSchlegel | 2018-03-13T08:21:13+00:00
I can confirm, that the issue still exists, I'm on `monero-gui-v0.11.1.0`. Last logentry in "monero-wallet-gui.log" is `2018-03-13 08:16:53.915	13872	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:2505	Loaded wallet keys file, with public address: XXX`. How can I provide further details ? Windows 10 Pro, Version 1709, Build 16299.248. 

Thanks & Cheers

# Action History
- Created by: TrojanZA | 2017-09-26T09:30:41+00:00
- Closed at: 2017-10-15T18:30:20+00:00
