---
title: 'Monero Tech Meeting #120 - Monday, 2025-05-12, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1202
author: rbrunner7
assignees: []
labels: []
created_at: '2025-05-09T17:37:08+00:00'
updated_at: '2025-05-12T18:33:41+00:00'
type: issue
status: closed
closed_at: '2025-05-12T18:33:40+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1198).

# Discussion History
## rbrunner7 | 2025-05-12T18:33:40+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1202
<s​needlewoods> hello
<j​berman> *waves*
<uncle_rae> hello
<r​brunner7> So, what is there to report from last week?
<r​brunner7> I finished coding the improved peer selection code. Rucknium is currently testing it.
<sneedlewoods> +1
<rucknium> +1
<jberman> +1
<jeffro256> +1
<syntheticbird> +1
<s​needlewoods> working on replacing wallet2 with Wallet API in simplewallet
<jberman> +1
<jeffro256> +1
<syntheticbird> +1
<r​brunner7> Oh, good. That will become a nice milestone.
<s​needlewoods> I noticed I missed some functions for the API that are in wallet.h but not in wallet.cpp for #9664
<r​brunner7> Nothing beats actual use of an API to check it :)
<sneedlewoods> +1
<j​berman> me: mostly worked on FCMP++ input limit-related work last week. I bumped input limits to 128, tested it out, and shared in MRL some preliminary thoughts on using groups of max 8-input proofs in single FCMP++ txs rather than individually large input proofs
<j​effro256> Howdy sorry I'm late
<j​effro256> Thanks for taking the initiative there !
<r​brunner7> By the way, I tried to find some clear info about the size in bytes of FCMP++ transactions, depending on the number of inputs and outputs. I am pretty sure that exists already, and that I saw that once somewhere, but couldn't find it. Does somebody have a link?
<r​brunner7> jeffro256: Yeah, I surpised myself to find such a nice piece of Monero coding work within my reach.
<j​effro256> I can post a template for that today assuming default carrot tx extra size
<rbrunner7> +1
<j​effro256> *table not template
<r​brunner7> It might get more interesting still because somebody might have found yet more "spy nodes" ...
<r​brunner7> (talk over in /dev)
<j​berman> here's a table that shows membership proof byte size by n inputs and n layers: https://github.com/j-berman/monero/blob/84daa22a878544fe2e7536f4b047e872ff8c21cb/src/fcmp_pp/proof_len.h#L43-L173
<j​berman> doesn't include other tx components
<j​berman> the tree currently would have 6 layers, and bumps to 7 layers around 300mn outputs in the chain total (we're currently at ~150mn, probably a bit higher now)
<j​effro256> SA/L proofs are an additional 384 bytes per input
<r​brunner7> jberman: At first sight, that table looks pretty strange What is such a table needed for?
<j​berman> We determine how large the FCMP++ proof should be from a tx's n inputs and n layers in the tree when de-serializing the tx. That calculation is slow/expensive. To avoid making de-serialization slow, we include a table with all pre-calculated values for fast lookups
<j​berman> note if we were to stick with max 8-input proofs in single FCMP++ txs, that table would be way way smaller (only the first 8 rows)
<r​brunner7> Ah, ok. I just hope that won't be brittle somehow.
<j​berman> fwiw I also included a unit test that re-does the calculation for every table value and checks against the table
<j​berman> Although that doesn't address all brittle-prone concerns
<r​brunner7> Oh, that's nice
<r​brunner7> Good idea
<r​brunner7> And now to my weekly curiousity question: Anything new regarding the contest? How many entries does the leaderboard have already :)
<j​berman> No valid submissions yet :( We got a couple that both look like AI unfortunately, neither work (one doesn't compile the other doesn't pass tests)
<j​effro256> I've seen several private repo invite links but honestly haven't looked at any submissions
<r​brunner7> So at least there is some movement, somewhere
<j​berman> xmrack is reaching out to zprize contestants from here https://www.zprize.io/blog/announcing-the-2023-zprize-winners
<j​berman> it should help that the fiat value of prizes has gone up too
<r​brunner7> Certainly. XMR in USD has a remarkable run lately. One can only wonder.
<r​brunner7> Alright. Anything more to discuss today beyond the reports?
<s​yntheticbird> *Luke if you see this message please submit the best code imaginable anonymously pretty please*
<r​brunner7> Doesn't look like it. I think we can close the meeting already. Thanks everybody for attending, read you again next week!
<jberman> +1
<syntheticbird> +1
<s​needlewoods> thanks everyone
````


# Action History
- Created by: rbrunner7 | 2025-05-09T17:37:08+00:00
- Closed at: 2025-05-12T18:33:40+00:00
