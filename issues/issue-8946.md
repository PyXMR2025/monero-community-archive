---
title: Consider pulling in the "unfriendly peers PR suite", perhaps with a flag
source_url: https://github.com/monero-project/monero/issues/8946
author: Gingeropolous
assignees: []
labels:
- feature
- proposal
created_at: '2023-07-13T04:18:08+00:00'
updated_at: '2025-12-28T23:35:10+00:00'
type: issue
status: closed
closed_at: '2025-12-28T23:35:10+00:00'
---

# Original Description
About 3 years or so ago, the network had some unfriendly participants and @moneromooo-monero made a bunch of PRs with potential mechanisms to keep a node connected even in that kind of environment. 

I think the effort stopped, so these PRs have just been sitting there.

7297, 
7255
7135
5955
6935
6940
6946
7081

edited to add

6944


edited to add clickable links added by @SChernykh 

https://github.com/monero-project/monero/pull/7297 https://github.com/monero-project/monero/pull/7255 https://github.com/monero-project/monero/pull/7135 https://github.com/monero-project/monero/pull/5955 https://github.com/monero-project/monero/pull/6935 https://github.com/monero-project/monero/pull/6940 https://github.com/monero-project/monero/pull/6946 https://github.com/monero-project/monero/pull/7081 https://github.com/monero-project/monero/pull/6944

To me, the logic of the PRs seemed sound, and they even received reviews. Thus, my conclusion regarding their unmerged status is that no one really tested them.

In lieu of testing (though I guess that could be done), these could be integrated with a flag that disables them. Thus, a node will run with them on as default. But if there happens to be an unexpected behavior, folks could disable the features. 

though i guess it could be argued that the daemon should ship with them off by default, and folks could switch it on. 

but defaults. 

( in addition, merging them would also make it easier to test, because ppl could just flip flags instead of compiling fancy PRs). 

ooooh, or maybe the flags could have varying levels of these measures. Because, the counterpoint to the above point is that by leaving them as PRs, we could test them 1 at a time....

well thanks for reading. 

--friendly-peers [0-4]         set network friendliness level. 0 = least friendly (all countermeasures active), 4 = most friendly (no countermeasures active). 

.... or this has already been done and i just missed it. 

# Discussion History
## SChernykh | 2023-07-13T09:34:11+00:00
Clickable links: #7297 #7255 #7135 #5955 #6935 #6940 #6946 #7081
IIRC the most important fixes were merged and a new release was made back then. These ones in the list don't look properly reviewed/tested, and some concerns were raised in the comments.

## Gingeropolous | 2023-07-13T12:40:29+00:00
thanks @SChernykh . I think I may have missed some, and some weren't included because they were duplicates for release and master. 

i missed https://github.com/monero-project/monero/pull/6944 . 

I'm trying to see which PR included m_score

## selsta | 2025-12-28T23:35:06+00:00
Without reviews and testing, these can't be merged.

# Action History
- Created by: Gingeropolous | 2023-07-13T04:18:08+00:00
- Closed at: 2025-12-28T23:35:10+00:00
