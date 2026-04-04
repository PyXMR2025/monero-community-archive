---
title: '[Discussion] Stress Testing monerod'
source_url: https://github.com/monero-project/monero/issues/9348
author: spackle-xmr
assignees: []
labels:
- important
- proposal
- discussion
created_at: '2024-05-29T23:20:18+00:00'
updated_at: '2025-03-23T14:24:18+00:00'
type: issue
status: closed
closed_at: '2025-03-23T14:24:18+00:00'
---

# Original Description
I have seen multiple people express the need for extensive stress testing of monerod. Per the recent MRL meeting (https://github.com/monero-project/meta/issues/1015), this might be done either with simulation tools or via a dedicated/abusable testnet. The intention is to address any daemon performance issues which present a roadblock. It is important to note that the current set of issues do not appear to be readily reproduced in isolated environments.

My personal belief is that the present situation calls for the creation of a new/disposable testnet, though that would admittedly require significant participation for the testing to work as desired. I imagine an additional testnet could be integrated into the project as a recurring temporary network that runs for a limited time frame each year. Perhaps, as was suggested to me, an even more fully featured approach might be taken by adding the ability for monerod to spin up custom public testnets using command line parameters.

I do not have the background needed to discuss creating appropriate simulation tools, and I hope others will speak to that.

In any case, I believe an additional testing tool would be helpful and I hope this issue can guide collaboration on creating it.

# Discussion History
## hyc | 2024-05-29T23:25:15+00:00
> Perhaps, as was suggested to me, an even more fully featured approach might be taken by adding the ability for monerod to spin up custom public testnets using command line parameters.

That ability has always existed. But starting on ad hoc basis like this requires all participants to communicate with each other to tell each other their specific node addresses, so it takes some coordination.

## spackle-xmr | 2024-05-29T23:38:53+00:00
Perhaps I am exaggerating the issues, but my thought was that using --add-exclusive-node to create an extra testnet is not a quality solution due to the difficulty of coordination, as well as the possibility that someone might connect with a copy of the existing testnet. That would destroy/overwrite the alternative chain that people are attempting to create.

## spackle-xmr | 2024-05-30T00:19:10+00:00
In the interest of trying to get something set up quickly, I would like to share my hasty attempt at a disposable testnet/stressnet (https://github.com/spackle-xmr/monero). It is a simple testnet replacement, making no other changes. My node p2p port is stressnet.net:28080 if anyone wishes to use it.

## 0xFFFC0000 | 2024-05-31T16:11:54+00:00
For the time being, in my ugly solution, what I am doing is to use `—add-exclusive-node` list and pass it as argument which is quite ugly [1], until we can decide on some custom approach. 



1. https://github.com/0xFFFC0000/benchmark-project/blob/7d5aef21a6778ea8ac62fdc8637efb5e2df942ca/benchmark_project.cpp#L672


Maybe having `—exclusive-node-list-file` which would require a simple txt file containing list of nodes for that testnet is not such a bad idea. 

## spackle-xmr | 2024-05-31T21:11:50+00:00
Another option might be to publish a copy of the testnet after running --pop-blocks to the most recent fork and mining/churning to a single address for a while. Publishing that chain and miner seed phrase would offer an end product that: 
1. runs the same version as mainnet
2. is far enough behind the actual testnet that there is no real danger of overwriting the actual testnet
3. has many thousands of available key images for a user to spend immediately

I expect that having this available will make independent stress testing more attractive. 

## Boog900 | 2024-06-15T20:10:46+00:00
I made some tools to stress test monerod: https://github.com/Boog900/Monero-stress-test-tools

My idea was to pob blocks back to when we know txpool was huge and push the transactions from the blocks after that to the nodes pool, doing this at height `3139920` I was able to get the txpool to around 90 MBs. 

Then I also created a tool to make and maintain a certain number of "fake" connections to a node, these connections do just enough to stay connected and nothing else. Monerod  will still fluff txs to these connections.

Using these tools I am able to reliably get a node killed.

The first thing to note is that even with no connections and spamming txs monerod still likes to use a lot of RAM, however using `pmap` this seems to come from Linux caching more of the LMDB database, therefore I couldn't actually get a node killed with no connections.

My node got killed in a VM with 10GB of RAM with ~150 connections I can't remember how long it took and I have killed a node 3 times in a VM with 5GB of RAM with 100 connections within 20 minutes each.

I wouldn't recommend setting the `connection-maker` to maintain over 100 connections as I found it starts getting pretty unstable.  

## spackle-xmr | 2024-06-17T00:56:22+00:00
I want to confirm that the testnet fork / 'stressnet' set up [here](https://github.com/spackle-xmr/monero) at  is now running with community support. There are over 35 nodes on the network, with flooding set to begin at 15:00 UTC on June 19th.

## hinto-janai | 2024-06-26T15:03:04+00:00
`185.198.234.30:28080` should be online, can someone confirm?

## spackle-xmr | 2024-06-26T16:39:16+00:00
> `185.198.234.30:28080` should be online, can someone confirm?

I see you on one of my nodes via 'print_cn'. Should be good to go. 

# Action History
- Created by: spackle-xmr | 2024-05-29T23:20:18+00:00
- Closed at: 2025-03-23T14:24:18+00:00
