---
title: Miner power supply
source_url: https://github.com/monero-project/monero/issues/2143
author: mehtaphysical
assignees: []
labels: []
created_at: '2017-07-02T23:29:20+00:00'
updated_at: '2017-08-07T15:48:53+00:00'
type: issue
status: closed
closed_at: '2017-08-07T12:48:34+00:00'
---

# Original Description
I'm getting an error when attempting to mine on linux:
```
uname -a
Linux fichte 4.11.6-3-ARCH #1 SMP PREEMPT Thu Jun 22 12:21:46 CEST 2017 x86_64 GNU/Linux
```

Error:

```
2017-07-02 16:27:15.516	    7f45517fa700	ERROR	miner	src/cryptonote_basic/miner.cpp:829	Couldn't find battery/power status file, can't determine if plugged in!
```
Seems like the issue comes from here: https://github.com/monero-project/monero/blob/421a6d0340527fe23c1b10cfd20769555afffb1b/src/cryptonote_basic/miner.cpp#L849. The paths to check battery status are hard coded.

Also, others appear to be having this issue: https://forum.getmonero.org/5/support/87704/mining-issue-on-linux and https://www.reddit.com/r/Monero/comments/61yy9s/essential_update_monero_01031_wolfram_warptangent/dfkczl0/

I can submit a PR to fix this if it is welcome.

# Discussion History
## moneromooo-monero | 2017-07-03T09:34:09+00:00
A good patch for this would be welcome, yes. Thanks.

## mehtaphysical | 2017-07-04T02:28:12+00:00
Cool. added #2144 

# Action History
- Created by: mehtaphysical | 2017-07-02T23:29:20+00:00
- Closed at: 2017-08-07T12:48:34+00:00
