---
title: Enforce unique ring members in multi-input transactions (consensus level)
source_url: https://github.com/monero-project/monero/issues/5433
author: Mitchellpkt
assignees: []
labels: []
created_at: '2019-04-12T20:15:40+00:00'
updated_at: '2019-04-13T16:09:00+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
## Issue
Transactions with many inputs that reuse ring members (recent [example](https://xmrchain.net/tx/469838bce3be05335784eafd4d071fcd7dbfaadc2e13cb5c3f8024aab4c3fc87)) heuristically reveal when outputs switched spend state, often with relatively high statistical confidence. This practice is detrimental to:
-  The sender's privacy (they fell victim to an incorrectly-designed wallet that circumvents ring signature obfuscation, effectively disabling one of our main privacy features).
-  Privacy of any general user whose wallet has *previously* selected those outputs for decoys
-  Privacy of any general user whose wallet selects those outputs as decoys *in the future*

## Solution
This can be trivially prevented at the consensus level by the following requirement: Any transaction with `N` inputs and `R` ring size (currently 11) must reference `N*R` unique ring members. For example the cringe-worthy transaction [linked above](https://xmrchain.net/tx/469838bce3be05335784eafd4d071fcd7dbfaadc2e13cb5c3f8024aab4c3fc87) has 133 key images containing 1463 ring members, but only references 143 unique outputs.

Equivalently, could be implemented by looking at ring intersections, etc. Will leave method choice to the devs. :- )

## Contraindications?
Is there any plausible use case that **strictly** requires the construction of these privacy-damaging transactions? (i.e. use case cannot be accomplished any other way). I cannot think of any cases where this is even useful, much less required.

Thoughts?

Thanks,
-:- Isthmus

# Discussion History
## SamsungGalaxyPlayer | 2019-04-13T16:09:00+00:00
Is it worth adding one exception? A small part of me is worried about legitimate transactions that use an input twice.

# Action History
- Created by: Mitchellpkt | 2019-04-12T20:15:40+00:00
