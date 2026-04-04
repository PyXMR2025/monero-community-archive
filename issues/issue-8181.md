---
title: '[Discussion] Proposal to make mining pools impossible, by requiring pools
  to trust their miners.'
source_url: https://github.com/monero-project/monero/issues/8181
author: ghost
assignees: []
labels: []
created_at: '2022-02-15T15:26:52+00:00'
updated_at: '2022-02-16T12:41:01+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Monero is currently under a 51% attack. A pool called MineXMR has the majority of the network hashrate. This is most certainly not a single entity that has caused this particular pool to gain the majority. The pool was for a very long time the largest pool, it was only just recently that it hit the 50.00% mark.

The reason for this attack is the existence of pools and the miners who choose to mine for large pools for comfort reasons - more frequent payouts, higher uptime, better connection and low fees to name a few, instead of mining for a smaller pool or solo to help decentralize the network.

For this reason, i think that the best way to prevent this from happening, is to make pools not possible at all, resulting in miners having to mine solo, and being incentivised to run their own nodes.

My proposal is to instead of requiring the (RX)hash of a block to match the threshold, require the hash of the signature of the (RX)hash of the block to match the threshold instead. This would require the signature to be generated for every nonce, which would not be very effective for the pool operator to do with their own private key, and the miners could not be trusted to share their reward with other miners.

Formulas:
- Current: H(B)
- Proposed: h(S(H(B)))

H - RandomX hash
h - Regular hash
S - Signature
B - Block with nonce applied

The blocks wouldbe produced either by miners' nodes, or centralized block producers working similarily to pools. but without the payout sharing. This choice would be made by the miner, depending if they want to download the whole blockchain.

I believe this solution would work, but I'm still not sure if enough miners would switch over to solo mining if the change was made. It's a very radical way, but i believe it could work well. Be free to propose your adjustments.

# Discussion History
## selsta | 2022-02-15T17:44:10+00:00
> Monero is currently under a 51% attack. A pool called MineXMR has the majority of the network hashrate.

No. MineXMR has 40% of the network hashrate and even if they had more than 50% of the hashrate it wouldn't automatically be an attack.

## jeffro256 | 2022-02-15T19:52:31+00:00
I second what @selsta said; the Monero network is not currently undergoing a 51% attack.  I assume that what you're suggesting is that each block be signed by a pool operator. If that's the case, then  what's keeping the large pool operator from changing their signature each block?

## ghost | 2022-02-15T19:58:31+00:00
> I second what @selsta said; the Monero network is not currently undergoing a 51% attack. I assume that what you're suggesting is that each block be signed by a pool operator. If that's the case, then what's keeping the large pool operator from changing their signature each block?

No, what I'm suggesting is that every **nonce** would have to be signed by the pool operator, what wouldn't happen at all because it's very ineffective.

## jeffro256 | 2022-02-15T20:02:24+00:00
With the coinbase output private key or some other key?

## ghost | 2022-02-15T20:08:51+00:00
> With the coinbase output private key or some other key?

Yes, the coinbase output private key, I don't know what other private key could you have on mind.

## jeffro256 | 2022-02-15T20:24:31+00:00
It would certainly discourage pool mining, but then you would have to have your spend key on every computer you mine on, each connected to the internet. I don't know if that's a risk that most miners want to worry about. 

## ghost | 2022-02-15T20:31:51+00:00
> It would certainly discourage pool mining, but then you would have to have your spend key on every computer you mine on, each connected to the internet. I don't know if that's a risk that most miners want to worry about.

You can, and even should use a separate buffer wallet to receive mining rewards. This is not a major issue.

## ImaginaryOlive | 2022-02-16T12:40:47+00:00
> > It would certainly discourage pool mining, but then you would have to have your spend key on every computer you mine on, each connected to the internet. I don't know if that's a risk that most miners want to worry about.
> 
> You can, and even should use a separate buffer wallet to receive mining rewards. This is not a major issue.

https://www.timeanddate.com/countdown/generic?p0=1440&iso=20220216T17
https://app.element.io/#/room/#monero-research-lab:matrix.org
This meeting is the best place to discuss any solution to remove mining pools.

# Action History
- Created by: ghost | 2022-02-15T15:26:52+00:00
