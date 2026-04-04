---
title: Move away from using indices
source_url: https://github.com/monero-project/monero/issues/4828
author: Gingeropolous
assignees: []
labels: []
created_at: '2018-11-09T04:36:51+00:00'
updated_at: '2018-11-11T04:08:05+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
This has been talked about forever, and I wanted to post this to get the ball rolling. The recent attack on wownero really brings to light how fragile these networks can be. Right now monero can't gracefully handle a deep reorg - transactions get dumped into the ether as opposed to getting back into the majority chain. As I understand it, this is because monero references other outputs using the index of the output as opposed to a position-independent identifier, so therefore when you create a transaction, the ringpartners are reference using an index for a place in the blockchain, not the output itself.

I know there's some fancy databasing term for what I'm talking about.

Anyway, because of this, if your transaction is on a forked chain that needs to get reabsorbed into the main chain, and your transaction references outputs on the fork chain, those indices no longer exist on the new merged chain, so that transaction dies. 

I believe this indexing was done to save space by the original cryptonote developers. Someone mentioned during some IRC in some room that the weight of using an identifier is negligible in comparison to the other things we've done to make txs heavier (RingCT, I'm looking at you!). In addition, most transactions use less inputs ( no denominations, etc) so there are less things to reference. 

Ultimately, move away from using an index so the monero network can become more resilient and secure. 

Hopefully now that its filed as an issue something will happen. 

# Discussion History
## hyc | 2018-11-09T13:35:38+00:00
Yes, an index is only a 64 bit integer, a full hash is 256 bits. That tells you how much space we're talking about. For a 1-input ring of size 11 that means your transaction would be 264 bytes larger.

## vtnerd | 2018-11-11T04:08:05+00:00
The size difference is usually a little bit more - 264 bytes is the upper limit. The wire/stored format sorts the indexes of the ring, then changes the indexes to be the difference from the prior index, then serializes the value in a varint format. 

# Action History
- Created by: Gingeropolous | 2018-11-09T04:36:51+00:00
