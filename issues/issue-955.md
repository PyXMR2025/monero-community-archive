---
title: GUI sets refresh-from-block-height to a distant future block
source_url: https://github.com/monero-project/monero-gui/issues/955
author: stevesbrain
assignees: []
labels:
- resolved
created_at: '2017-11-14T04:14:49+00:00'
updated_at: '2017-11-14T12:05:15+00:00'
type: issue
status: closed
closed_at: '2017-11-14T06:27:10+00:00'
---

# Original Description
_I had posted this at https://github.com/monero-project/monero/issues/2802 but I realised it may be a GUI-project-specific issue, so I've cross-posted it here_

Hi all,

Just been playing around with testnet, and noticed that the GUI (and Monerujo) both set the wallets `refresh-from-block-height` to a block far in the future (in my testing, approximately 27850 blocks further down the line). I am making the assumption this is not by design, as it has the effect that a transaction sent to the wallet will show as pending, but once assigned a block + confirmed it will disappear. 

Manually setting the refresh-from-block-height to a lower value and then rescanning the blockchain allows the balance to appear.

# Discussion History
## Jaqueeee | 2017-11-14T05:08:05+00:00
Please provide some more information. Which version of GUI? Official bins or custom built? On mainnet or testnet?



## stevesbrain | 2017-11-14T05:55:01+00:00
@Jaqueeee Official binaries (the release version ones), version 0.11.1 for Linux x64 (though this has happened to me since version 10 - when I started using monero - I'd never sat down to troubleshoot until now). No custom build, and testnet as mentioned in OP :)

## Jaqueeee | 2017-11-14T06:18:41+00:00
Thanks. Known issue on testnet. Fixed in https://github.com/monero-project/monero/pull/2342, merged in master. 
+resolved

## Jaqueeee | 2017-11-14T06:20:24+00:00
Same as https://github.com/monero-project/monero/issues/2775

## stevesbrain | 2017-11-14T12:05:14+00:00
My apologies for not seeing that beforehand - thanks for pointing me in the right direction, and being willing to assist :) 

# Action History
- Created by: stevesbrain | 2017-11-14T04:14:49+00:00
- Closed at: 2017-11-14T06:27:10+00:00
