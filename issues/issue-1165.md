---
title: 'Monero Tech Meeting #110 - Monday, 2025-03-03, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1165
author: rbrunner7
assignees: []
labels: []
created_at: '2025-03-01T16:48:00+00:00'
updated_at: '2025-03-03T18:19:22+00:00'
type: issue
status: closed
closed_at: '2025-03-03T18:19:21+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1160).

# Discussion History
## rbrunner7 | 2025-03-03T18:19:21+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1165
<j​effro256> Howdy
<s​needlewoods> hey
<j​berman> *waves*
<r​brunner7> So, what was up last week?
<s​needlewoods> Unfortunately not much, been busy with other stuff
<r​brunner7> I intended to finish part 2 of my little post series about Carrot, but couldn't either
<j​effro256> Making FCMP++ crypto unit tests on our transaction format
<sneedlewoods> +1
<j​berman> me: I've merged my latest FCMP++ work into the fcmp++-stage branch in the seraphis-migration repo, and am working on top of it in my local right now. At the moment I'm working on tx helper functions to construct FCMP++ txs. I'm working with the CLI / wallet2 for now, and the helper functions should be re-usable alongside the Carrot integration (e.g. setting the path, setting tx source)
<sneedlewoods> +1
<r​brunner7> Is the tx format fixed already? Do you know what gets new versions, and how, and what not?
<j​effro256> Yes mainly
<r​brunner7> Good to hear
<j​effro256> We're bumping the RingCT version, and changing adding a Carrot variant to `cryptonote::tx_out`
<j​effro256> There's also the FCMP++ details in the RingCT prunable data, like block index, tree depth, and proof buffers.
<r​brunner7> Many new things to learn for people doing low-level work, I guess
<j​berman> also I've kept the current cryptonote::txxin_to_key, but made key_offsets empty and amount 0
<j​effro256> There's discussions to be had about typing the format in the C++ code and saving a few bytes, but I'm not super focused on that atm
<r​brunner7> Well, "saving a few bytes" with those much larger tx sizes is a bit ironic :)
<jeffro256> +1
<j​berman> in theory we could exclude those exclude-able fields when serializing for writing to disk / sending over the wire at any point in the future
<r​brunner7> Anyway, I think parties like the Cuprate team with be glad to see things stabilize soon
<r​brunner7> Maybe also the kind soul that modifies the block exporer code
<r​brunner7> *block explorer
<r​brunner7> Alright, everything progressing smoothly. Do we have to discuss something today beyond these reports?
<r​brunner7> Doesn't seem to be the case. So thanks for attending this pretty short meeting nevertheless, and read you again next week!
<j​effro256> Thanks!
<s​needlewoods> Thanks, cu
<j​berman> thanks :)
````


# Action History
- Created by: rbrunner7 | 2025-03-01T16:48:00+00:00
- Closed at: 2025-03-03T18:19:21+00:00
