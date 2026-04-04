---
title: Fees show up as Max Amount
source_url: https://github.com/monero-project/monero/issues/1280
author: medusadigital
assignees: []
labels: []
created_at: '2016-10-30T19:32:06+00:00'
updated_at: '2016-11-05T09:22:29+00:00'
type: issue
status: closed
closed_at: '2016-11-05T09:22:29+00:00'
---

# Original Description
Fees can show up as Max Amount. Affects GUI as well as CLI wallet.

![maxfeemoo](https://cloud.githubusercontent.com/assets/17108301/19839316/d9743c1e-9edf-11e6-9ef7-30ebf1360c2c.png)


# Discussion History
## moneromooo-monero | 2016-10-31T20:31:58+00:00
For CLI only:

Are you running with commit 1dd5b0b7dff60d45aa3d5d33f8be304f3e222c7a in monero ?

If yes, does the bug appear for transactions _sent_ with this commit, or only for transactions sent before it ?

Is the bug showing up for in, out, pending, failed, pool, txes ?


## medusadigital | 2016-11-02T09:04:30+00:00
bug only seems to affect outgoing transactions which get restored. probably rebuildig cache is the issue 


## moneromooo-monero | 2016-11-02T12:53:46+00:00
https://github.com/monero-project/monero/pull/1288

That's a GUI fix though, so that doesn't fix the bug on restore, that'd be a second bug.


## medusadigital | 2016-11-05T09:22:29+00:00
fixed --> closed


# Action History
- Created by: medusadigital | 2016-10-30T19:32:06+00:00
- Closed at: 2016-11-05T09:22:29+00:00
