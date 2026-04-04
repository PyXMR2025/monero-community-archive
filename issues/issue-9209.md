---
title: '`prune_blockchain` cause entire node to hang on'
source_url: https://github.com/monero-project/monero/issues/9209
author: SyntheticBird45
assignees: []
labels:
- not reproducible
created_at: '2024-02-28T21:15:01+00:00'
updated_at: '2024-02-28T21:41:29+00:00'
type: issue
status: closed
closed_at: '2024-02-28T21:41:29+00:00'
---

# Original Description
**Monero v0.18.3.1 syncing 99%, Linux 6.7 x86_64**

`prune_blockchain` rpc methods cause node to hang on and don't react to SIGTERM. Killing process is the only solution.
The bug is consistent

# Discussion History
## SyntheticBird45 | 2024-02-28T21:15:44+00:00
command used for rpc:
```
curl http://127.0.0.1:18081/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"prune_blockchain","params":{"check":true}}' -H 'Content-Type: application/json'
```

## selsta | 2024-02-28T21:16:53+00:00
How long did you wait? The prune process can take multiple hours.

## SyntheticBird45 | 2024-02-28T21:18:39+00:00
I waited 30 minute. node is already pruned and since i set `check: true` It shouldn't even trigger the pruning process

## SyntheticBird45 | 2024-02-28T21:22:42+00:00
Issue is still happening when node is fully synced

## selsta | 2024-02-28T21:24:23+00:00
does entering `check_blockchain_pruning` in monerod also not work?

## SyntheticBird45 | 2024-02-28T21:25:51+00:00
Yes

## SyntheticBird45 | 2024-02-28T21:27:22+00:00
Just tested if it wasn't alacritty or terminal emulator causing issue but it is consistent across 3 other terminals.

## SyntheticBird45 | 2024-02-28T21:30:24+00:00
Disk read I/O is increasing while hanging so it might be stuck at interacting with the database. I maybe stupid but is the `prune_blockchain` rpc command check the pruning state over all the database ?

## selsta | 2024-02-28T21:32:29+00:00
Do you have an SSD or HDD? Running `check_blockchain_pruning` took about 5 minutes on my system with SSD.

moneromooo said it reads all tx data so it can be lengthy

## SyntheticBird45 | 2024-02-28T21:34:31+00:00
I've an SSD, however the filesystem is almost at capacity.

## SyntheticBird45 | 2024-02-28T21:37:29+00:00
Looking at my I/O Read rate monerod will have finish to check in 1 hour. I believed that monerod didn't checked the all database for pruning state. If the hanging of monerod is something known during the check of the prune worker, I believe we can close this issue.

# Action History
- Created by: SyntheticBird45 | 2024-02-28T21:15:01+00:00
- Closed at: 2024-02-28T21:41:29+00:00
