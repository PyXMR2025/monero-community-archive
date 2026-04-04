---
title: RandomX 2 year anniversary, evaluating the landscape of PoW, etc.
source_url: https://github.com/monero-project/meta/issues/636
author: Gingeropolous
assignees: []
labels: []
created_at: '2021-12-01T14:32:01+00:00'
updated_at: '2023-12-18T04:23:52+00:00'
type: issue
status: closed
closed_at: '2023-12-18T04:23:52+00:00'
---

# Original Description
If you don't recall the fun leading up to the RandomX fork 2 years ago, I made a [super rushed write up yesterday](https://moneroworld.com/randomx_2yr.html) . Long story short, we did it, and it seems that we're still doing it. However, when reading through our history I came across some notions that we were going to "check in" on RandomX and see how its fairing.

One particularly "fun" issue is the question of whether we should "tune" RandomX to adjust to the hardware landscape. 

Off the cuff, and from brief discussions in #monero-pow, there doesn't seem to be anything in the current space or on the horizon that could challenge the goals and purpose of RandomX. It seems the major chip manufacturers are bringing things to market that are... well, not really game changing. 

Intel's bigLITTLE is more of the same. Of potential interest is the move of Apple to bring RAM onto the CPU die. Similarly, AMD is growing monstrous caches on their processors, and will probably move RAM onto the die at some point probably. 

So yeah. The point of this issue is to discuss and explore.

Any thoughts?

# Discussion History
## hyc | 2021-12-01T14:57:46+00:00
Thanks for writing up, the summary sounds right to me.

Another hardware development to mention is wafer scale computing, but that is unlikely to be useful for anything besides AI/ML projects.

## Gingeropolous | 2021-12-01T15:34:58+00:00
Dumping articles on next gen CPU tech could be useful. 

AMD
https://www.digitaltrends.com/computing/amd-ryzen-6000-news-rumors-specs-release-date/

So, if the general move is to continue loading up CPU die with more memory (in any sense), does RandomX continue to do its thing? I mean, presumably the major advantage to closer memory is to reduce the latency, and RandomX is sensitive to RAM latency. So if we keep the 2gb scratchpad or whatever, and that all moves on-die, then those CPUs are just better at RandomX because they are just faster CPUs? 

At that point I guess the actual computation may become the bottleneck.

Should there be a consideration to increase the 2gb thing to force use of distant RAM?

I guess I'm trying to figure out *what* sort of change we'd be looking for to warrant any tuning. 

## carrington1859 | 2021-12-03T13:21:53+00:00
RISC-V is something to keep an eye on in general. Seems like it is taking off in a big way, and maybe will lead to more diverse hardware. Not sure how that impacts Random-X though.

## Gingeropolous | 2023-09-14T11:08:19+00:00
https://web.archive.org/web/20230914110625/https://m.bitmain.com/product/detail?pid=00020230828105038795jYr5J0WO0689

The Bitmain X5 claims to be a "professional miner" for Monero. Note it doesn't say its an ASIC. It also directly states its RISC-V

## selsta | 2023-12-18T04:23:52+00:00
Closing this since a lot of time has passed and we are working on tweaking RandomX.

# Action History
- Created by: Gingeropolous | 2021-12-01T14:32:01+00:00
- Closed at: 2023-12-18T04:23:52+00:00
