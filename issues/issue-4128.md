---
title: Lost and not receiving funds
source_url: https://github.com/monero-project/monero-gui/issues/4128
author: mlpotesak
assignees: []
labels: []
created_at: '2023-03-11T21:35:30+00:00'
updated_at: '2023-03-17T15:41:10+00:00'
type: issue
status: closed
closed_at: '2023-03-17T15:41:09+00:00'
---

# Original Description
I’m having a problem with my wallet. I tried to receive funds from my miner group to my wallet..I had some problems and after I tried to fix the transfer issue all the funds from my wallet were gone. My wallet is empty. Can you advise?

# Discussion History
## selsta | 2023-03-11T22:27:37+00:00
Please open your wallet and go to Settings -> Info and post

- Version
- Wallet mode
- Wallet restore height

## mlpotesak | 2023-03-12T19:48:19+00:00
Version o.18.1.2-unknown 
Advanced mode (Remote node)
Wallet reset height 3

## plowsof | 2023-03-12T21:27:41+00:00
is your wallet fully synchronised? 
valid remote node? try selsta2.featherwallet.net:18081 or node2.monerodevs.org:18089

## mlpotesak | 2023-03-13T17:27:46+00:00
Thank you it looks like it’s connected.
It’s still showing zero funds.
I’m not sure how to fix that.
Thank you so much for your time.

## selsta | 2023-03-13T17:28:32+00:00
@mlpotesak Can you post the exact text it says in the bottom left corner? Is you wallet synchronized?

## mlpotesak | 2023-03-14T17:51:25+00:00
Wallet is synchronized
Daememon is synchronized(2841979)
Network status remote node
I hope this is what you need

## selsta | 2023-03-14T18:39:57+00:00
When was the first time you received a transaction into this wallet approximately? Which months / year?

## mlpotesak | 2023-03-15T18:06:57+00:00
2022-07-10 

## selsta | 2023-03-15T18:57:15+00:00
Did you try rescanning from that height?

Go to Settings -> Info, click on (Change) next to wallet restore height and enter `2022-07-10`. Wait for the wallet to sync and check if your funds show up. Syncing can take a while.

## mlpotesak | 2023-03-16T17:29:36+00:00
Is it important how to enter the date because my full amount is not being showed.
Thanks to everyone For your help.

## selsta | 2023-03-16T17:30:38+00:00
Yes, you have to enter it the same way I wrote in my previous comment.

What is the current value of Wallet Restore height?

## mlpotesak | 2023-03-17T15:40:32+00:00
Thank you everyone for your help:)
it looks like everything is working now:)

## selsta | 2023-03-17T15:41:09+00:00
Glad to hear :)

# Action History
- Created by: mlpotesak | 2023-03-11T21:35:30+00:00
- Closed at: 2023-03-17T15:41:09+00:00
