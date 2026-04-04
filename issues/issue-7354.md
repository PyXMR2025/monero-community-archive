---
title: 'Feature request: Only store statewise information on nodes'
source_url: https://github.com/monero-project/monero/issues/7354
author: fullmetal1
assignees: []
labels: []
created_at: '2021-01-29T01:51:48+00:00'
updated_at: '2022-02-19T00:41:24+00:00'
type: issue
status: closed
closed_at: '2022-02-19T00:39:45+00:00'
---

# Original Description
Currently, data.mdb is massive (I'm about a third of the way through syncing and I'm at 30GB already), and I can't help but think that there has to be a better way.

Would it not be possible to have nodes only store the last X amount of blocks and the current state of the blockchain, and after that any new nodes just assume that the state sent p2p is valid?



# Discussion History
## JustFranz | 2021-01-29T19:27:35+00:00
the current state of the blockchain is all of the blocks, you can not determine whether an output has been spent by looking at the blockchain alone

If you have just joined the network and just assume that the state you are given is correct then how can you tell if a node is lying? By definition you don't, you believe everything. In a trustless network you have to verify everything yourself. 

## selsta | 2021-01-29T19:29:48+00:00
You can use --prune-blockchain to only store 1/3rd of the normal blockchain size (30GB)

## fullmetal1 | 2021-01-29T20:58:46+00:00
Thanks, I'll add that to my bitmonero.conf.

You could snapshot the state every X blocks and use consensus to trust it (sign the state. check the signature with other nodes, or something to that effect). Since consensus is required to trust that nodes are not lying (for example, about which wallet to give monero to from mining)

I'm not worried about this from a personal perspective (at least not yet. I just want to test out mining for fun), but more in thinking long term. Eventually blockchains will be in the terabytes of size, and I worry that that will make mining unfeasible for anyone but large institutions. I suppose my feature request is an engineering challenge much too large for slapping onto an existing blockchain.



## selsta | 2021-01-29T21:00:36+00:00
> Thanks, I'll add that to my bitmonero.conf.

Note that this will not shrink existing blockchains. If you want to end up with a 30GB .mdb file I would recommend to sync from scratch with --prune-blockchain.

## selsta | 2022-02-19T00:41:23+00:00
Such major changes are currently not planned. If you don't want to run a node, or don't have the necessary hardware then I would recommend to use a public remote node.

# Action History
- Created by: fullmetal1 | 2021-01-29T01:51:48+00:00
- Closed at: 2022-02-19T00:39:45+00:00
