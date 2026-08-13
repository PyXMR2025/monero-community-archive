---
title: Don't ban peers that send invalid blocks that pass the PoW checks.
source_url: https://github.com/seraphis-migration/monero/issues/454
author: Boog900
assignees: []
labels: []
created_at: '2026-08-11T17:13:06+00:00'
updated_at: '2026-08-11T17:53:09+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
If monerod did not ban peers that send invalid blocks, which still pass the PoW check, then we would be able to relay blocks immediately after the PoW checks but before the other expensive checks, speeding up block relay. Bitcoin does this.

P2pool was updated to relay all blocks that pass PoW checks over its network to nodes, but you need to run a p2pool node for that. I think with FCMP we should change monerod here to allow the node to do this itself. This is something I want to do in Cuprate.

# Discussion History
## j-berman | 2026-08-11T17:53:09+00:00
@Boog900 also raised this strong point:

> Having all nodes check FCMP proofs in parallel is much better than going 1 node then to its peers then to their peers etc

I think we definitely want to stop banning in the monerod version released containing the FCMP++/Carrot fork. And I think we'll want to relay blocks after the PoW check and before expensive checks at some point, potentially before the fork if there's time. Doing the former with the fork version enables implementing the latter at a later time.

# Action History
- Created by: Boog900 | 2026-08-11T17:13:06+00:00
