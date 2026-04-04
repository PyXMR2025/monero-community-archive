---
title: newbie brainstorm question?
source_url: https://github.com/monero-project/monero/issues/9781
author: dbee01
assignees: []
labels: []
created_at: '2025-02-07T17:07:45+00:00'
updated_at: '2025-02-07T17:13:34+00:00'
type: issue
status: closed
closed_at: '2025-02-07T17:13:34+00:00'
---

# Original Description
Hi everyone,

I’m a blockchain noob but i’m picking it up as i go along. To help me learn i’m playing devil’s advocate and trying to picture attack vectors to the Monero network.

I’m especially interested, given the current political climate, as to how an operational agency might attack the Monero network and how it could be hardened against such an attack…

The most likely attack from the 3 letter army would surely be the addition of Sybil nodes to the network i think followed by a possible Eclipse attack. Given that an army of Monero nodes could be created in VM’s behind a single (or multiple)  ip's and unleashed on the network if i understand correctly? 

I’m positing a possible network defence for this attack. I’m calling it the Phalanx Defence. Really,  i'm just learning though,  so feel free to pick holes. Here goes:

At the moment the block template consists of the block header (the proof-of-work, timestamp and hash of previous node) along with the Transaction Layer (ring signatures, ring confidential transaction and stealth address).

What if the verified nodes were able to form a phalanx to protect themselves against Sybil nodes? Every time the Concensus Protocol rejected a transaction from a node, that node loses a small degree of credibility in the blockchain network.

We could call this the Node Trust score and it could be stored and relayed from one node to another by adding the node trust score to the blockchain transaction layer ie. Ring signature, ring confidential transaction, stealth address AND the node trust score.

The idea would be, existing verified nodes would have a very high node trust score but newer Sybil nodes would be outcast quickly since they don’t have node trust. This node trust algorithm would be weighted to reflect the most recent transactions first. Kinda like a decentralised Page Rank system Google used for SEO. An Amazon Product Review comparison may be more apt.

Where can i go to learn more about Monero? Where does my idea go wrong?

# Discussion History
## dbee01 | 2025-02-07T17:13:15+00:00
Duplicate

# Action History
- Created by: dbee01 | 2025-02-07T17:07:45+00:00
- Closed at: 2025-02-07T17:13:34+00:00
