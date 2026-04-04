---
title: Block verification failing on RPi2
source_url: https://github.com/monero-project/monero/issues/624
author: osensei
assignees: []
labels: []
created_at: '2016-01-26T23:46:54+00:00'
updated_at: '2016-01-29T20:20:22+00:00'
type: issue
status: closed
closed_at: '2016-01-29T20:20:22+00:00'
---

# Original Description
Block verification is failing on my RPi2, which is running latest HEAD (f4e99d6957b06b8d73e9465ab3b8e4af63acfab3) on Ubuntu Mate 15.04 with GCC 4.8.4

This is the output with log level 1:

```
2016-Jan-26 19:53:54.493197 [P2P9][x.x.x.x:18080 OUT]Got NEW BLOCKS inside of handle_response_get_objects: size: 200
2016-Jan-26 19:53:54.494413 [P2P9]block_batches: 50
2016-Jan-26 19:54:18.807073 [P2P9]Attempting to get an output index by amount and amount index, but amount not found
2016-Jan-26 19:54:18.807728 [P2P9]EXCEPTION: Attempting to get an output index by amount and amount index, but amount not found
2016-Jan-26 19:54:19.105040 [P2P9]Index: 246722 Elems: 246718 partial results found for get_output_tx_and_index
2016-Jan-26 19:54:19.174390 [P2P9]Index: 203238 Elems: 203236 partial results found for get_output_tx_and_index
2016-Jan-26 19:54:19.205906 [P2P9]Index: 188465 Elems: 188464 partial results found for get_output_tx_and_index
2016-Jan-26 19:54:19.237742 [P2P9]Index: 182430 Elems: 182428 partial results found for get_output_tx_and_index
2016-Jan-26 19:54:19.281039 [P2P9]Index: 184317 Elems: 184317 partial results found for get_output_tx_and_index
2016-Jan-26 19:54:19.320161 [P2P9]Index: 213051 Elems: 213049 partial results found for get_output_tx_and_index
2016-Jan-26 19:54:19.626515 [P2P9]Index: 1065772 Elems: 1065765 partial results found for get_output_tx_and_index
2016-Jan-26 19:54:19.768316 [P2P9]Index: 771858 Elems: 771810 partial results found for get_output_tx_and_index
2016-Jan-26 19:54:19.864902 [P2P9]Index: 550916 Elems: 550913 partial results found for get_output_tx_and_index
2016-Jan-26 19:54:20.011234 [P2P9]Index: 938920 Elems: 938866 partial results found for get_output_tx_and_index
2016-Jan-26 19:54:20.097275 [P2P9]Index: 543900 Elems: 543895 partial results found for get_output_tx_and_index
2016-Jan-26 19:54:20.273923 [P2P9]Index: 330929 Elems: 330927 partial results found for get_output_tx_and_index
2016-Jan-26 19:54:20.380739 [P2P9]Index: 675135 Elems: 675133 partial results found for get_output_tx_and_index
2016-Jan-26 19:54:20.434498 [P2P9]Index: 317331 Elems: 317324 partial results found for get_output_tx_and_index
2016-Jan-26 19:54:20.471895 [P2P9]Index: 226175 Elems: 226166 partial results found for get_output_tx_and_index
2016-Jan-26 19:54:20.535065 [P2P9]Index: 198521 Elems: 198510 partial results found for get_output_tx_and_index
2016-Jan-26 19:54:20.557875 [P2P9]Index: 128770 Elems: 128765 partial results found for get_output_tx_and_index
2016-Jan-26 19:54:20.590105 [P2P9]Index: 200603 Elems: 200603 partial results found for get_output_tx_and_index
2016-Jan-26 19:54:20.808185 [P2P9]Index: 11550 Elems: 11549 partial results found for get_output_tx_and_index
2016-Jan-26 19:54:20.810976 [P2P9]Index: 11173 Elems: 11170 partial results found for get_output_tx_and_index
2016-Jan-26 19:54:20.819209 [P2P9]Index: 27082 Elems: 27078 partial results found for get_output_tx_and_index
2016-Jan-26 19:54:20.830856 [P2P9]Index: 486 Elems: 485 partial results found for get_output_tx_and_index
2016-Jan-26 19:54:21.018257 [P2P9]Block with id: <63a843b2626c28d0b6118cbb3bb58020e15f4fc13a8d048340abf335ae5a306d>
does not have enough proof of work: <7093bf6fb20f5f60a1dada4f636d3aa4fabfeed5d10df3fb13d38c59677c38f2>
unexpected difficulty: 939289168
2016-Jan-26 19:54:21.018791 [P2P9][x.x.x.x:18080 OUT]Block verification failed, dropping connection
```

Reverting commit 8ce12a978e710ca31d076e9be4c4f4ca846b0e3b fixes the problem.


# Discussion History
## hyc | 2016-01-27T01:33:10+00:00
What compiler flags are you using?


## osensei | 2016-01-27T01:53:09+00:00
The ones set by "make release-arm7"


## osensei | 2016-01-28T05:03:17+00:00
Well... I've recompiled it with GCC 4.9.2, which is the default on Ubuntu 15.04, and it's working now!

I had previously changed to GCC 4.8.4 because I was having a similar problem long ago ([check here](https://forum.getmonero.org/5/support/2375/can-t-sync-further-than-block-600000-on-rpi2)), and it was solved by downgrading GCC from 4.9 to 4.8.


## hyc | 2016-01-28T05:26:43+00:00
Glad to hear it. This version of the asm code is faster than the previous anyway.


## osensei | 2016-01-29T20:20:22+00:00
I'm closing this issue then. 

@fluffypony maybe there should be some mention of it in the README.md to avoid others running into the same problem.


# Action History
- Created by: osensei | 2016-01-26T23:46:54+00:00
- Closed at: 2016-01-29T20:20:22+00:00
