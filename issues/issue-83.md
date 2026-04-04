---
title: 'Save the network: Disincentivize megapools'
source_url: https://github.com/monero-project/research-lab/issues/83
author: t-anon
assignees: []
labels: []
created_at: '2021-04-17T21:42:52+00:00'
updated_at: '2021-05-25T16:53:36+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
We are all aware of the current problem facing Monero: today, **only two people (pool operators) need to be compromised in order to 51% attack the network.** The health and freedom of the currency of tomorrow is entirely dependent on the opsec and goodwill of _two people_ today.

I propose that we reduce block rewards to make it less profitable for people to join megapools. We could do something like this for new block rewards:

- If the same address was awarded the last block, a 0.001% block reward
- If it was awarded within the last 1-10 blocks - a 0.01% reward
- Within the last 10-100 blocks - a 0.1% reward
- Within the last 100-1000 blocks - a 1% reward
- etc.

Someone more skilled at math than me can figure out the optimal curve or mathematical construction to incentivize miners to join smaller pools

---

**Edit:** Upon further thought, megapools will just simply start providing various addresses for people to mine to, and this would be easy to automate. Perhaps the solution is developing some sort of feeless P2P mining application?

# Discussion History
## busyboredom | 2021-05-25T16:20:29+00:00
Bitcoin has P2Pool, which is a decentralized mining pool we might take some inspiration from.

It operates using a "Share Chain", which has a block rate 20x faster than the main bitcoin chain so that a consensus on miner work can be reached on time. There's no law of physics saying we couldn't do the same, although you'd need a pretty stable internet connection to participate when share chain blocks are flying at you every 6 seconds (2 minutes / 20). 

Edit: I just remembered -- we have self-select now! Doesn't self-select solve this issue by allowing miners to hash a block template of their own choosing? 

# Action History
- Created by: t-anon | 2021-04-17T21:42:52+00:00
