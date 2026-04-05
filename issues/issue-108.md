---
title: Binary with kDonateLevel = 0 compiled do not start with donate-level command
  line parameter
source_url: https://github.com/xmrig/xmrig/issues/108
author: therealseeku
assignees: []
labels:
- bug
created_at: '2017-09-13T00:24:01+00:00'
updated_at: '2017-09-17T13:58:47+00:00'
type: issue
status: closed
closed_at: '2017-09-17T13:58:47+00:00'
---

# Original Description
Hi!

Just wan to report a small issue, maybe...
Compiled binary with kDonateLevel = 0 does not start when the command line parameter donate-level=0 is used.



# Discussion History
## krash867 | 2017-09-13T14:43:27+00:00
That would be because there is some other code elsewhere preventing the binary from starting with that command line option. If you try `donate-level=0` without changing `kDonateLevel` it won't start either. 

I am new to this repo and have not dug around too much yet, if I come across it I will let you know. 

You should at least consider a small donation or even dropping the donate level to 1. Someone here is doing all of this work for free, and even small contributions keep projects alive. 

## xmrig | 2017-09-13T15:03:49+00:00
I fixed it in dev branch.
Anyway you don't need specify `--donate-level=0` in command line if you already change `kDonateLevel` in code.

## therealseeku | 2017-09-13T20:09:25+00:00
I have my miner on donation=1 running :) Thanks your your work

# Action History
- Created by: therealseeku | 2017-09-13T00:24:01+00:00
- Closed at: 2017-09-17T13:58:47+00:00
