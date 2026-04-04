---
title: I am missing (not seeing) some transactions to (in) the CLI
source_url: https://github.com/monero-project/monero-gui/issues/3479
author: GongSuiLi
assignees: []
labels: []
created_at: '2021-05-13T03:43:28+00:00'
updated_at: '2021-05-17T20:03:05+00:00'
type: issue
status: closed
closed_at: '2021-05-17T20:03:05+00:00'
---

# Original Description
I encountered a more urgent problem. Use monero-wallet-rpc --configfile to query all transactions in my own wallet, use monero-wallet-cli to create a hot wallet, and use show_transfer txid to return that the transaction does not exist, and only some transactions exist in rpc results. This problem means that the balance of monero-wallet-rpc is greater than the balance of monero-wallet-cli, and there are more transactions. I don't know the reason. I always have the same problem when I try to use the latest version of v0.17.2.0. I would like to ask you to help me. 
I am very worried about the loss of assets. I can check these transactions using rpc, but there is no such transaction created by using cli. I have tried several times

# Discussion History
## selsta | 2021-05-13T05:16:19+00:00
Which restore height did you set? Do you use subaddresses?

## GongSuiLi | 2021-05-13T06:17:11+00:00
> Which restore height did you set? Do you use subaddresses?

I deleted the viewWallet file and recreated it. Use monero-wallet-cli --daemon-address --generate-from-view-key, The command line height defaults to 0. I used  subaddress, but most of the subaddress transactions exist. Only some transactions do not exist in the cli. These transactions can be queried by rpc. You can also find it in the browser. There has never been such a problem before. The incoming transactions queried by rpc are consistent with the cli, and now there is a problem.
In addition, rpc,cli,monerod version is v0.17.1.3, I tried update cli version to v0.17.2.0, always no those transactions

## selsta | 2021-05-13T17:23:41+00:00
One thing you can try is to add --subaddress-lookahead 200:1000, in case the issue is related to subaddress lookahead.

Also if you generate a wallet only from view key you won't see outgoing transactions, only incoming and change transactions. Are the missing transactions outgoing transactions?

## moneromooo-monero | 2021-05-13T17:28:26+00:00
Did you properly export/import outputs and key images on that hot wallet ? The hot wallet will otherwise not know the key images of your outputs, and will not see any tx spending them without change (ie, sweep txes).

## GongSuiLi | 2021-05-14T02:58:07+00:00
> One thing you can try is to add --subaddress-lookahead 200:1000, in case the issue is related to subaddress lookahead.
> 
> Also if you generate a wallet only from view key you won't see outgoing transactions, only incoming and change transactions. Are the missing transactions outgoing transactions?

The transactions I mentioned are incoming transactions, I want to enter #monero-dev to communicate with you directly, how to open the chat room permissions

## GongSuiLi | 2021-05-14T03:00:15+00:00
> Did you properly export/import outputs and key images on that hot wallet ? The hot wallet will otherwise not know the key images of your outputs, and will not see any tx spending them without change (ie, sweep txes).

Because the transactions I'm talking about are incoming transactions, I think it has nothing to do with exports/import outputs and keyImages

## selsta | 2021-05-14T03:00:21+00:00
@GongSuiLi What is your matrix username?

## selsta | 2021-05-17T20:03:05+00:00
Closing as the issue was resolved.

# Action History
- Created by: GongSuiLi | 2021-05-13T03:43:28+00:00
- Closed at: 2021-05-17T20:03:05+00:00
