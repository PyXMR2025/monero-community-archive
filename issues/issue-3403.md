---
title: XMR balance not showing. Where did it go?
source_url: https://github.com/monero-project/monero-gui/issues/3403
author: KeineWeissEs
assignees: []
labels: []
created_at: '2021-04-15T14:29:03+00:00'
updated_at: '2021-04-19T16:40:05+00:00'
type: issue
status: closed
closed_at: '2021-04-19T16:40:05+00:00'
---

# Original Description
I've withdrawn XMR from Binance to my wallet I've got from getmonero.org, the transaction has been confirmed but the balance still shows 0. I've tried resyncing it and I've confirmed that the transaction was sent to my wallet but still I haven't figured out why my balance won't update. 
Please help.



# Discussion History
## selsta | 2021-04-15T14:30:21+00:00
Which "wallet mode" are you using? You can check inside Settings -> Info.

## KeineWeissEs | 2021-04-15T15:19:09+00:00
> Which "wallet mode" are you using? You can check inside Settings -> Info.

Advanced Mode (Remote node)

## selsta | 2021-04-15T15:21:14+00:00
Can you also tell me the "Wallet restore height" inside Settings -> Info?

Also which remote node are you using? Try one of the following:

- node.xmr.to:18081
- node.supportxmr.com:18081
- 88.198.199.23:18081
- 78.47.80.55:18081

## KeineWeissEs | 2021-04-15T16:23:16+00:00
I changed my wallet restore height to 1940000 because I read that this could help but it didn't change anything.
I'll try node.xmr.to:18081, I'll report if it changed anyting or stayed the same.

## selsta | 2021-04-15T16:24:03+00:00
Which node did you use previously?

## KeineWeissEs | 2021-04-15T16:25:24+00:00
node.moneroworld.com:18089

## selsta | 2021-04-19T16:40:05+00:00
Closing as this seems to be a user support issue. If you still have issues comment here our reach out to http://reddit.com/r/monerosupport

# Action History
- Created by: KeineWeissEs | 2021-04-15T14:29:03+00:00
- Closed at: 2021-04-19T16:40:05+00:00
