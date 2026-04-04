---
title: '[Idea] Storing encrypted tx details to tx_extra?'
source_url: https://github.com/monero-project/monero/issues/1518
author: kenshi84
assignees: []
labels: []
created_at: '2016-12-31T05:04:05+00:00'
updated_at: '2022-07-20T20:50:30+00:00'
type: issue
status: closed
closed_at: '2022-07-20T20:50:30+00:00'
---

# Original Description
One can restore his funds using the mnemonic seed, but the detailed information about the past outgoing transfers (i.e., destination addresses and amounts, tx private keys) are only stored in the wallet cache file and cannot by recovered from the seed. I find it nice to be able to recover that information also from the seed only.

When scanning the blockchain, one knows if his funds were spent by finding his key images on the input side of each transaction. In such a situation, what if the transaction's detailed information was stored with encryption using the private spend key to the tx_extra field? This way, the fully detailed information of the wallet's past transfers can be recovered from the seed only.

Adding data to the tx_extra increases the fee, of course, but I'd be personally happy to have an option to pay the additional cost for the benefit of being able to recover the full history of my wallet.

# Discussion History
## moneromooo-monero | 2017-01-01T16:30:56+00:00
It seems wasteful, compared to saving them in the wallet cache, which doesn't have to be replicated by every node.

## kenshi84 | 2017-01-02T02:24:00+00:00
Personally I find it not wasteful, as long as the increase in fee is reasonable. I'd be willing to pay more fees if such an option was available.

One problem with saving data to the cache file is that you can't easily use multiple wallet files of the same address. If you spend money from a wallet file A of a certain address, that tx info won't appear in the `show_transfers` command in another wallet file B of the same address.

Another solution would be to implement import/export of the past transfer details.

## moneromooo-monero | 2017-01-02T10:27:53+00:00
We may have to implement transient communication on the chain anyway (encrypt stuff with the recipient's address, it gets propagated to the txpool, but never mined). This could be used for this. You'd pay for the txpool space, but it would not get into the blockchain. You'd have to refresh your second wallet within N days though.

## kenshi84 | 2017-01-02T11:22:41+00:00
Aren't data on txpool supposed to stay only for 2 minutes on average?

I feel quite positive about storing transaction history permanently and privately on the blockchain, but maybe the majority of the community are against such an idea... but isn't it always good to provide users with a choice, if there's a demand?

## moneromooo-monero | 2017-01-02T11:55:28+00:00
If they're mined, they'll stay for 2 minutes.
And if you want to make the claim a majority of the community wants a change, you first have to give some kind of evidence that (1) there is, and (2) they thought things through.

## kenshi84 | 2017-01-02T12:04:13+00:00
I thought this idea to be useful since I've seen people being unable to open their old wallet file with a new release binary, hence losing their past transaction details. But maybe the recent PRs on portable wallet cache will solve this issue and make the proposed idea less useful.

## moneromooo-monero | 2017-01-02T14:52:05+00:00
It is useful. It also has problems. So it is not an obvious thing to add.

## kenshi84 | 2017-01-05T00:35:59+00:00
> We may have to implement transient communication on the chain anyway (encrypt stuff with the recipient's address, it gets propagated to the txpool, but never mined).

Btw this sounds new to me. Is this part of the development roadmap?

## kenshi84 | 2017-01-16T02:44:00+00:00
Considering the impact of the increase in transaction sizes after RingCT due to range proofs, the increase in tx size caused by this proposal would be relatively minor (i.e. one tx privkey, two pubkeys for each recipient address, ... what else?). So I'll leave this post open just in case we might want to implement it in the future.

## Cactii1 | 2022-07-20T20:00:55+00:00
This issue seems to have been decided against as the community aims to keep all txs looking similar on the blockchain.

Propose to close.

## selsta | 2022-07-20T20:50:30+00:00
It has been 5-6 years and there is not much support for this. Closing. This issue can still be referenced in future proposals.

# Action History
- Created by: kenshi84 | 2016-12-31T05:04:05+00:00
- Closed at: 2022-07-20T20:50:30+00:00
