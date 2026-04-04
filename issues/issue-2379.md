---
title: Decrease default confirmation/unlock times in GUI
source_url: https://github.com/monero-project/monero-gui/issues/2379
author: 1blockologist
assignees: []
labels:
- invalid
created_at: '2019-09-07T02:36:22+00:00'
updated_at: '2019-09-09T19:45:38+00:00'
type: issue
status: closed
closed_at: '2019-09-09T19:40:43+00:00'
---

# Original Description
Can we decrease the unlock time from ~20 minutes to 5 or less? This is tied to estimated block time, and therefore how many blocks are necessary

What is the current rationale for so many blocks?

# Discussion History
## xiphon | 2019-09-07T02:47:23+00:00
We can't. While 10 blocks confirmation is just a wallet requirement, it will be enforced on the consensus level soon.
See https://github.com/monero-project/monero/issues/5712


## 1blockologist | 2019-09-07T02:49:54+00:00
@xiphon I see, before I contribute there, couldn't we drop it to 5 confirmations just because the anonymity set is larger now than before?

## ghost | 2019-09-07T07:37:51+00:00
> couldn't we drop it to 5 confirmations just because the anonymity set is larger now than before?

The lock time has nothing to do with the anonymity set. It's about reverting blocks and related problems.

If you want to reduce the block time you should present strong arguments, possibly based on your research, why a lock time of 5 blocks is as secure as 10 blocks.

Can we close this issue?

## xiphon | 2019-09-07T10:28:16+00:00
> couldn't we drop it to 5 confirmations just because the anonymity set is larger now than before?

no sure about that, i think anonymity set size is not the main factor here.

Edit: didn't see @Realchacal's answer, basically said the same

## selsta | 2019-09-09T19:39:58+00:00
Not something we can decide on GUI side.

+invalid

# Action History
- Created by: 1blockologist | 2019-09-07T02:36:22+00:00
- Closed at: 2019-09-09T19:40:43+00:00
