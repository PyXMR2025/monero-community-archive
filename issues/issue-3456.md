---
title: '[SOLVED] Stagenet  all shares rejected as low difficulty shares'
source_url: https://github.com/monero-project/monero/issues/3456
author: Admiral-Noisy-Bottom
assignees: []
labels:
- invalid
created_at: '2018-03-21T00:36:02+00:00'
updated_at: '2018-03-21T11:32:52+00:00'
type: issue
status: closed
closed_at: '2018-03-21T11:32:52+00:00'
---

# Original Description
I've been testing and developing a pool for the past week without any issues with mining. All of a sudden, yesterday (20th of March in Australia) all shares submitted by test miners are rejected - every one of them.

I ran my miner on another site and go the same problem, so I did some research. Found something about an upgrade taking place on the 28th of March and also found that XMRIG had been update to work with the new monero upgrade.

I ran the miner on a normal monero pool with out issue. But on my stagenet pool, every share is rejected.

Any ideas?

# Discussion History
## Admiral-Noisy-Bottom | 2018-03-21T02:50:49+00:00
Turns out the issue was cause by my own stupidity!

The version of node.js had changed. Once it was back to the recommended version, using the Node Version Manager, the problem went away.

You're dismissed, carry on.

## moneromooo-monero | 2018-03-21T11:24:34+00:00
Good to see all is well :)

+invalid


# Action History
- Created by: Admiral-Noisy-Bottom | 2018-03-21T00:36:02+00:00
- Closed at: 2018-03-21T11:32:52+00:00
