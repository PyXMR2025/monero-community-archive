---
title: problem with receiving XMR on GUI wallet
source_url: https://github.com/monero-project/monero-gui/issues/4074
author: TTwallet
assignees: []
labels: []
created_at: '2022-11-29T08:57:43+00:00'
updated_at: '2023-01-18T05:59:52+00:00'
type: issue
status: closed
closed_at: '2023-01-18T05:59:52+00:00'
---

# Original Description
Hi there, 
3 weeks ago I withdraw some XMR from Binance to GUI wallet.  And it never received, I thought maybe it had to do something with the update that is required on Ledger live app but I did the update yesterday and I logged into my GUI wallet and still not received my XMR. I contacted Binance support service and from their end everything is correct, transaction was completed. Can someone maybe help me with this matter? I have the tixd link and transaction information. thanks in advance. 

# Discussion History
## selsta | 2022-11-29T10:12:01+00:00
Please go to Settings -> Info and post

- Version
- Wallet restore height
- Wallet mode

## TTwallet | 2022-11-29T12:05:50+00:00
thanks for the reply, what should the version, wallet height and wallet mode be? 

## selsta | 2022-11-29T12:06:58+00:00
Post them here and I will tell you if they are ok, the other way around makes everything more complicated.

## TTwallet | 2022-11-29T12:36:29+00:00
thanks alot I will check it when I am home.


## TTwallet | 2022-11-30T20:23:53+00:00
Hi there, 

I looked it up, here are is the info:

version: 0.18.1.2-unknown (Qt 5.15.6)
wallet height: 2581447
mode:  Advanced mode (Local node)

## plowsof | 2022-11-30T21:55:17+00:00
you're using the latest version. perhaps the problem is with your local node. have you tried re-syncing from a remote node e.g. selsta2.featherwallet.net:18081?
- Settings 
- Node -> click Remote node
- (+) Add remote node
- Address = selsta2.featherwallet.net
- Port = 18081
- OK. now make sure the node is clicked / highlighted grey in the list under 'Add remote node' 
- it should say connected eventually
- To resync your wallet go to Settings -> Info -> click change next to restore height -> dont change anything , just click ok -> ok

## TTwallet | 2022-12-01T08:47:48+00:00
Did not changed my node yet, I changed the height of the wallet to the height of the frist receiving transaction. after I did that, it showed only less balance.. Do you think that changing the node will be the solution? thank you for your help so far.

## selsta | 2022-12-01T11:21:30+00:00
@TTwallet please go to Settings -> Log, enter "status" into the textbox and post the output here. Then we can see if your node is properly synced.

## TTwallet | 2022-12-03T20:02:35+00:00
[3-12-2022 20:17] 2022-12-03 19:17:52.209 I Monero 'Fluorine Fermi' (v0.18.1.2-release) 
Height: 1481118, target: 2769435 (53.4809%) 
Downloading at 31 kB/s 
Next needed pruning seed: 3 
4 peers 
Remote Host Peer_ID State Prune_Seed Height DL kB/s, Queued Blocks / MB 
92.205.62.235:18080 f88d8eb9646e0206 synchronizing 0 2769435 11 kB/s, 0 blocks / 0 MB queued 
141.98.11.121:18080 dc4dc31afcc3eb97 synchronizing 181 2769435 8 kB/s, 0 blocks / 0 MB queued 
136.33.130.147:18080 8e02306afbe91337 synchronizing 0 2769435 11 kB/s, 0 blocks / 0 MB queued 
47.157.248.110:18080 2f208bbf8bc7c4bb normal 0 1 1 kB/s, 0 blocks / 0 MB queued 
0 spans, 0 MB 
[]

## TTwallet | 2022-12-03T20:04:34+00:00
I changed the block height again, but it is still not showing the last transaction. 

## TTwallet | 2022-12-03T20:05:09+00:00
sorry for the late reply, it was a verry busy week for me


## selsta | 2022-12-03T20:26:09+00:00
Your node is only 53% synced. You either have to wait for it to fully sync up to 100%, or use a remote node.

## selsta | 2023-01-18T05:59:52+00:00
Closing as this is a support ticket and there's no update from issue creator.

# Action History
- Created by: TTwallet | 2022-11-29T08:57:43+00:00
- Closed at: 2023-01-18T05:59:52+00:00
