---
title: 'I used the monero gui, my balance is not displayed and my transaction history
  is missing. '
source_url: https://github.com/monero-project/monero-gui/issues/4016
author: web26082022
assignees: []
labels: []
created_at: '2022-08-25T20:36:14+00:00'
updated_at: '2025-01-06T13:31:42+00:00'
type: issue
status: closed
closed_at: '2022-08-26T15:59:42+00:00'
---

# Original Description
I used the monero gui, my balance is not displayed and my transaction history is missing. The balance is positive and today there is an incoming transaction, I have its hash and the balance was not zero even before this transaction. Nothing was deleted. Help please. Thanks.

# Discussion History
## selsta | 2022-08-25T20:37:32+00:00
Please go to Settings -> Info and post

- Version
- Wallet mode
- Wallet restore height

## web26082022 | 2022-08-25T20:42:41+00:00
GUI version: 0.18.1.0-release (Qt 5.12.8)
Embedded Monero version: 0.18.1.0-release
Wallet restore height: 2598683
Wallet mode: Advanced mode (Local node)
Graphics mode: OpenGL

## selsta | 2022-08-25T20:44:14+00:00
When was the first time you received a transaction into this wallet? Approximately?

## web26082022 | 2022-08-25T20:48:22+00:00
A few months ago. There were several transactions. Here, for example, is the hash of today's transaction:
f3d35982d23c9a3879c4eb8a60be840030cdcfcc770140dc0b03457849620fd6

## selsta | 2022-08-25T20:49:34+00:00
So if you go to Transactions tab it shows not a single transaction? It's not clear from your description.

## web26082022 | 2022-08-25T20:51:27+00:00
That's right, all transactions have disappeared and the balance is zero.

## selsta | 2022-08-25T20:53:06+00:00
Can you go to Settings -> Log, type "status" into the textbox and post the output here?

Afterwards go to Settings -> Info, click on "(Change)" next to wallet restore height and then ok twice. Wait for it to resync, this might take a while.

## web26082022 | 2022-08-25T20:57:16+00:00
[26.08.2022 4:41] 2022-08-25 20:41:18.521 I Monero 'Fluorine Fermi' (v0.18.1.0-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[26.08.2022 4:41] 2022-08-25 20:41:33.127 I Monero 'Fluorine Fermi' (v0.18.1.0-release)
Height: 1178299, target: 1178299 (100%)
Downloading at 0 kB/s
Next needed pruning seed: 8
1 peers
Remote Host Peer_ID State Prune_Seed Height DL kB/s, Queued Blocks / MB
212.33.255.208:18080 0000000000000000 before_handshake 0 0 0 kB/s, 0 blocks / 0 MB queued
0 spans, 0 MB
[]

## selsta | 2022-08-25T20:58:22+00:00
Your node isn't synced.

## web26082022 | 2022-08-25T21:01:01+00:00
"Info, click on "(Change)" next to wallet restore height and then ok twice. Wait for it to resync, this might take a while"
-- I do not see such a button and opportunity, I only display the information that I have already sent to you


## selsta | 2022-08-25T21:03:24+00:00
Your local node isn't synced. You either have to get it synced with the network first or you have to use a remote node.

## web26082022 | 2022-08-25T21:04:48+00:00
Yes, I found it, it's done  "(Change)" .

## selsta | 2022-08-25T21:06:38+00:00
You need a synced node first before you can rescan your wallet.

Go to Settings -> Node, select Remote node and then add one from this list: https://nodes.monero.com

Or alternatively you can wait for your local node to sync.

## web26082022 | 2022-08-25T21:07:12+00:00
How to use a remote node? Since it's been more than 12 hours such a trial?

## web26082022 | 2022-08-25T21:12:55+00:00
I will try to log into another node. Thanks for the help.

## web26082022 | 2022-08-25T21:14:51+00:00
This is how the login and password of the node are requested, but I did not find such information

## selsta | 2022-08-25T21:15:55+00:00
you don't have to enter login / password

just address and port (the number)

for example address: xmr.fail port: 18081


## web26082022 | 2022-08-25T21:18:37+00:00
Synchronization is going on a new node, I will wait for the result. Thanks again for your help. 

## web26082022 | 2022-08-25T21:26:20+00:00
[26.08.2022 4:41] 2022-08-25 20:41:18.521 I Monero 'Fluorine Fermi' (v0.18.1.0-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[26.08.2022 4:41] 2022-08-25 20:41:33.127 I Monero 'Fluorine Fermi' (v0.18.1.0-release)
Height: 1178299, target: 1178299 (100%)
Downloading at 0 kB/s
Next needed pruning seed: 8
1 peers
Remote Host Peer_ID State Prune_Seed Height DL kB/s, Queued Blocks / MB
212.33.255.208:18080 0000000000000000 before_handshake 0 0 0 kB/s, 0 blocks / 0 MB queued
0 spans, 0 MB
[]
[26.08.2022 5:11] 2022-08-25 21:11:26.621 I Monero 'Fluorine Fermi' (v0.18.1.0-release)
Stop signal sent
[26.08.2022 5:11] 2022-08-25 21:11:31.301 I Monero 'Fluorine Fermi' (v0.18.1.0-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081

## web26082022 | 2022-08-25T21:27:16+00:00
There is no speed change


## selsta | 2022-08-25T21:27:17+00:00
Settings -> Log is not relevant if you have a remote node set.

## web26082022 | 2022-08-25T21:29:31+00:00
I'll have to wait until he downloads all the blocks, as I understand? Tell me approximately the weight and how long will it take?

## selsta | 2022-08-25T22:27:41+00:00
What does it say in the bottom left corner? How many blocks remaining?

## web26082022 | 2022-08-26T06:59:43+00:00
Problem has been solved, the data has been updated, the balance is in place and the transaction history has been restored. Thanks for the help.

# Action History
- Created by: web26082022 | 2022-08-25T20:36:14+00:00
- Closed at: 2022-08-26T15:59:42+00:00
