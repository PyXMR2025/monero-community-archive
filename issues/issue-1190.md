---
title: NOT AN ISSUE , JUST WANT TO CLARIFY  ABOUT OCTOBER HARDFORK!!!
source_url: https://github.com/xmrig/xmrig/issues/1190
author: Gill1000
assignees: []
labels:
- question
created_at: '2019-09-23T04:38:16+00:00'
updated_at: '2019-09-28T17:44:10+00:00'
type: issue
status: closed
closed_at: '2019-09-28T17:44:10+00:00'
---

# Original Description
1)Will the 4.0.1 beta will automatically start randomX  in october 2019?
2)There is notification on monerocean claiming the current xmr wallet become obsolute after october 2019.
3)Is there really hardfork coming next month or these are rumours only bcoz there is no article  on web I found useful or clarifying enough  about this hardfork ?

And xmrig its feel good to come back here..always admire your work. keep up brother

# Discussion History
## xmrig | 2019-09-23T05:40:57+00:00
I start from end:
3) https://www.reddit.com/r/Monero/comments/d7twle/tentative_monero_015_release_schedule/ so 2+ months before algorithm change and 1 month for final decisions about RandomX variant.
2) address with integrated payment id (106 characters long) and with payment id (with dot) become obsolete, usual wallet addresses (95 character long) and sub-addresses will be fine, if use own address (not provided by exchange) all will be fine.
1) there will be another release, at least should rename `rx/test` to final name. Until Monero code freeze I can't guarantee current RandomX variant will works after the fork. About automatic switch, if pool support algorithm negotiation all will be fine (in this case you no need specify algorithm at all) for another pools I will add option `coin`.
Thank you.

## xmrig | 2019-09-28T17:44:10+00:00
RandomX migration guide #1204

# Action History
- Created by: Gill1000 | 2019-09-23T04:38:16+00:00
- Closed at: 2019-09-28T17:44:10+00:00
