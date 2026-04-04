---
title: bitmonerod crashes with "too many open files" message (+core dump)
source_url: https://github.com/monero-project/monero/issues/278
author: antanst
assignees: []
labels: []
created_at: '2015-05-05T11:46:44+00:00'
updated_at: '2016-07-07T20:02:35+00:00'
type: issue
status: closed
closed_at: '2016-07-07T20:02:35+00:00'
---

# Original Description
After a few days running in my Linux machine, bitmonerod consistently crashes. 

I compiled it at commit 41f0a8fe4d87a0c58dcc60917eedaa6315fb30b8 with [this](https://github.com/monero-project/bitmonero/pull/277/files) additional patch (unrelated but I thought I should mention it).

```
# uname -a
Linux snf-627174 3.13.0-43-generic #72-Ubuntu SMP Mon Dec 8 19:35:06 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux
```

bitmonerod startup parameters:

`--limit-rate=2048 --limit-rate-up=2048 --limit-rate-down=2048`

Last few relevant lines of output of bitmonerod before crash:

```
2015-May-05 00:18:36.058752 [P2P9][46.148.140.72:44054 INC] SYNCHRONIZED OK
[warn] epoll_create: Too many open files
[err] evsig_init: socketpair: Too many open files
[warn] epoll_create: Too many open files
[err] evsig_init: socketpair: Too many open files
*** Error in './bitmonerod': double free or corruption (fasttop): 0x0000000002835a90 ***
Aborted (core dumped)
```

Core dump is [here](http://83.212.102.247/core).


# Discussion History
## moneromooo-monero | 2016-02-06T13:37:16+00:00
That's fixed a while back. Can you check if it happens again with current master ?


## fluffypony | 2016-07-07T20:02:35+00:00
Fixed


# Action History
- Created by: antanst | 2015-05-05T11:46:44+00:00
- Closed at: 2016-07-07T20:02:35+00:00
