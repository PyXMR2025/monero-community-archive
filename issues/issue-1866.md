---
title: Testnet won't start with daemon unless --testnet-data-dir is specified
source_url: https://github.com/monero-project/monero/issues/1866
author: ghost
assignees: []
labels: []
created_at: '2017-03-13T17:33:35+00:00'
updated_at: '2017-03-13T17:39:33+00:00'
type: issue
status: closed
closed_at: '2017-03-13T17:39:33+00:00'
---

# Original Description
Ubuntu 16.04 VPS

If I run a detached daemon command with the `--testnet` flag, it will say it's initializing, but what it really is initializing is mainnet. If I instead run it with both the `--testnet` and `--testnet-data-dir` flags then it initializes fine.

Also, if I start it not detached, it will work fine as well.

https://paste.fedoraproject.org/paste/~-cgIr0LKXtblCaalMdFtV5M1UNdIGYhyRLivL9gydE=

# Discussion History
## ghost | 2017-03-13T17:39:33+00:00
Nevermind, I think I figured out the issue.

# Action History
- Created by: ghost | 2017-03-13T17:33:35+00:00
- Closed at: 2017-03-13T17:39:33+00:00
