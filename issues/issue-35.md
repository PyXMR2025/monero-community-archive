---
title: Technical note on log-sized but linearly timed authentication
source_url: https://github.com/monero-project/research-lab/issues/35
author: b-g-goodell
assignees: []
labels: []
created_at: '2018-10-02T03:02:43+00:00'
updated_at: '2018-10-02T03:29:00+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Sublinear ring signatures have been proposed before in multiple contexts and settings, including bilinear pairings and LWE approaches, and so on. For implementation, we must look at the _total time to download and verify_ the blockchain, assuming that these two processes (downloading and verifying) must occur in disjoint intervals of time. For a sublinearly sized blockchain, download time is sublinear, but ring signatures always require at least a linear amount of time for verification for the first time they are verified; batching and other optimizations may bring this to be sublinear after the first verification. SNARKs and STARKs avoid this, essentially, by verifying only once (although this is a mischaracterization, it isn't relevant to our desired tech note).

If the ring sigs are logarithmically sized, this introduces an exponential space-time tradeoff: worsening verification time by a small percentage can only be "made up" by making total space very very much smaller. Or, to think of it another way: saving a tiny bit of space in exchange for a tiny bit of verification time is not a good trade.

We would like a technical note that details this trade-off and establishes _some_ standard or rule by which future Monero contributors can judge whether to trade-off between space and time. For example, with the improvements made by bulletproofs, transactions have been made both smaller and faster to verify, allowing us some extra room in spacetime for increased ring sizes.

# Discussion History
## b-g-goodell | 2018-10-02T03:07:26+00:00
If we have some standards or rules as described, then we can put hard numbers on things like ring sizes for future reference. 

# Action History
- Created by: b-g-goodell | 2018-10-02T03:02:43+00:00
