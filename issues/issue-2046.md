---
title: Automatic mining
source_url: https://github.com/monero-project/monero-gui/issues/2046
author: sanderfoobar
assignees: []
labels: []
created_at: '2019-03-30T21:14:30+00:00'
updated_at: '2019-04-26T16:55:52+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
If https://github.com/monero-project/monero/pull/5374 makes it, GUI should follow. 

We'll have to replicate some code that's in `simplewallet.cpp` to check for mining status.

https://github.com/monero-project/monero/blob/cf3bc50e070ab4b3095f9dac0cdd7b1679f77cad/src/simplewallet/simplewallet.cpp#L4457-L4496

# Discussion History
## SamsungGalaxyPlayer | 2019-03-30T21:24:37+00:00
The less intrusive, the better.

## trasherdk | 2019-04-01T16:48:28+00:00
The ***less intrusive*** option would be ***Don't start mining until told to***.


## sanderfoobar | 2019-04-01T17:30:55+00:00
I think comments regarding automatic mining are better suited in monero-project/monero#5374

## jonathancross | 2019-04-15T11:57:20+00:00
FYI: https://github.com/monero-project/monero/pull/5374 has been merged.

## sanderfoobar | 2019-04-26T16:55:52+00:00
Thanks for the headsup @jonathancross. Currently working on this. Will not make next release, but the one after that.

# Action History
- Created by: sanderfoobar | 2019-03-30T21:14:30+00:00
