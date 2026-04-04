---
title: Synchronization failed
source_url: https://github.com/monero-project/monero/issues/8074
author: rexbutz
assignees: []
labels: []
created_at: '2021-11-20T18:13:47+00:00'
updated_at: '2023-08-09T00:13:42+00:00'
type: issue
status: closed
closed_at: '2023-08-09T00:13:42+00:00'
---

# Original Description
I'm trying to setup a Monero node on ubuntu 20.  I am getting the following error:

> candidate: 2403424 -> 2497555 [Your node is 94131 blocks (4.3 months) behind] 
2021-11-20 18:10:17.054 I SYNCHRONIZATION started
monerod: malloc.c:2379: sysmalloc: Assertion `(old_top == initial_top (av) && old_size == 0) || ((unsigned long) (old_size) >= MINSIZE && prev_inuse (old_top) && ((unsigned long) old_end & (pagesize - 1)) == 0)' failed.
Aborted

Does anyone have any idea what is wrong and how to fix?

# Discussion History
## antonegorov | 2021-12-22T20:07:11+00:00
Hi.

First it makes sense to try running monerod with `--log-level 4`

If, alas, there is no answers in the logs, then try re-sync blocks. Read about `--db-sync-mode` and maybe this option is a solution to your problem.

## selsta | 2022-02-18T23:30:52+00:00
Which version are you using?

# Action History
- Created by: rexbutz | 2021-11-20T18:13:47+00:00
- Closed at: 2023-08-09T00:13:42+00:00
