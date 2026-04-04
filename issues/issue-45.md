---
title: Investigate network bootstrapping problem
source_url: https://github.com/monero-project/research-lab/issues/45
author: b-g-goodell
assignees: []
labels: []
created_at: '2018-12-18T16:53:35+00:00'
updated_at: '2018-12-18T18:48:56+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
> @gingeropolous: so the seed node thing always bums me out. Its like "in order to create a decentralized network, you need a centralized seeding system".....

A recent publication (see [here](https://www.cs.umd.edu/projects/coinscope/coinscope.pdf)) utilizes properties of the Bitcoin protocol to develop a way to probe the Bitcoin network topology, to determine whether two nodes are connected to each other. Under the assumptions that the network is sufficiently well connected and no more than 50% of nodes are behaving non-honestly (including semi-honest nodes), the method reveals the ground truth network topology of all honest nodes and provides estimates for the network topology of the remainder of the network as well.

Utilizing a similar approach, perhaps in Kovri, it may be possible to bootstrap a decentralized network without relying upon trusted network views.

# Discussion History
## b-g-goodell | 2018-12-18T18:48:56+00:00
Keep in mind the difference between honest, semi-honest, and dishonest behavior. Semi-honest parties may do things outside the protocol in between steps, but will always faithfully execute the protocol in the correct order. Honest parties follow the protocol to the letter and do nothing else. Dishonest parties do whatever they want. By "non-honest" I mean semi- and dishonest actors above. I'm not sure about the semi-honest model.

# Action History
- Created by: b-g-goodell | 2018-12-18T16:53:35+00:00
