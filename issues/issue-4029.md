---
title: Sent XMR to GUI WALLET, balance shows 0
source_url: https://github.com/monero-project/monero-gui/issues/4029
author: gregus79
assignees: []
labels: []
created_at: '2022-09-13T21:39:53+00:00'
updated_at: '2022-09-14T17:37:30+00:00'
type: issue
status: closed
closed_at: '2022-09-14T17:37:30+00:00'
---

# Original Description
I ve sent XMR from Kraken to Gui wallet primary account address.
My balance shows 0.
My network status is disconnected.
Can someone help? am new on the monero blockchain

# Discussion History
## selsta | 2022-09-13T21:40:54+00:00
Please go to Settings -> Info and post

- Version
- Wallet mode
- Wallet restore height

## gregus79 | 2022-09-13T21:44:09+00:00
Version 0.18.1.0 release
wallet mode   advanced mode
wallet restore height 2690998

## selsta | 2022-09-13T21:45:07+00:00
Does it say Advanced mode (Local node) or (Remote node)?

## gregus79 | 2022-09-13T21:45:24+00:00
local node


## selsta | 2022-09-13T21:45:48+00:00
Did you sync up a local node?

## gregus79 | 2022-09-13T21:45:59+00:00
nope

## selsta | 2022-09-13T21:46:38+00:00
You either have to sync a local node or connect to a remote node, see for example nodes.monero.com

## gregus79 | 2022-09-13T21:51:39+00:00
any reliable node to connect to?

## selsta | 2022-09-13T21:52:55+00:00
Look on https://nodes.monero.com for example. I don't have any specific recommendations.

## gregus79 | 2022-09-13T21:57:46+00:00
ok I am now synchronised to remote node
balance still showing 0

## selsta | 2022-09-13T22:19:29+00:00
Do you have a transaction id?

What does it say in the bottom left corner? Is the wallet synchronized? It can take a bit with a remote node.

## gregus79 | 2022-09-14T06:41:15+00:00
432cca45b16540d33fb89ee328e55ed5434abec0a6532158b2f81d1bbd5fc21b

It says wallet is synchronised, Daemon is synchronised, artwork status is remote node

## gregus79 | 2022-09-14T06:56:42+00:00
OK its now showing balance
I had to scan transaction in settings

## selsta | 2022-09-14T17:37:30+00:00
Ok, if you are connected to a proper node this should not happen again.

# Action History
- Created by: gregus79 | 2022-09-13T21:39:53+00:00
- Closed at: 2022-09-14T17:37:30+00:00
