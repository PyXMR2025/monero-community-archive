---
title: tx is not possible
source_url: https://github.com/monero-project/monero/issues/3898
author: axeoman
assignees: []
labels: []
created_at: '2018-06-01T07:45:48+00:00'
updated_at: '2018-06-07T12:57:08+00:00'
type: issue
status: closed
closed_at: '2018-06-07T12:57:08+00:00'
---

# Original Description
Hi there! 
I need to automate sending funds, so I am using monero-wallet-rpc JSON-RPC API call "transfer" for that. But unfortunately after about 5 sending, API start returning error with text "tx not possible". Usually it disapears after half an our.
Anyone have a clue why is it happening?
Thank you.

# Discussion History
## moneromooo-monero | 2018-06-01T08:15:42+00:00
You'll get more info if you run "set_log 1" in monerod.
If you use transfer, it's likely that the tx is too big. You should be using transfer_split instead.
In any case, 0.12.2.0 is out soon (tomorrow probably) and fixes a few issues with sending.

## dEBRUYNE-1 | 2018-06-01T09:15:15+00:00
Posted this on reddit:

>By default, outputs are locked for 10 blocks. Note that this includes change outputs which are sent back to your own wallet. Thus, if you're sending transactions in rapid succession, eventually all your outputs will be locked. A quick workaround is splitting up your outputs into smaller outputs and sending them to yourself. For instance, let's say you have an output of 1 XMR and want to split it up into 10 0.1 outputs. You'd have to execute the following command.

    transfer <own-address> 0.1 <own-address> 0.1 <own-address> 0.1 <own-address> 0.1 <own-address> 0.1 <own-address> 0.1 <own-address> 0.1 <own-address> 0.1 <own-address> 0.1 <own-address> 0.1

>Hopefully this clears up some confusion. 

## axeoman | 2018-06-07T12:57:08+00:00
Thank you very much for the information, I think I got it. 

# Action History
- Created by: axeoman | 2018-06-01T07:45:48+00:00
- Closed at: 2018-06-07T12:57:08+00:00
