---
title: 'Unable to sync after pruning: E internal error: passed start_height not <  m_db->height()
  -- 3343083 >= 3343083'
source_url: https://github.com/monero-project/monero/issues/9789
author: tendermonster
assignees: []
labels: []
created_at: '2025-02-08T23:25:23+00:00'
updated_at: '2025-02-09T22:16:29+00:00'
type: issue
status: closed
closed_at: '2025-02-09T22:16:28+00:00'
---

# Original Description
Hi there,

today I finished pruning the bc successfully. After which monerod just freezes and does not sync anymore.

When syncing I get following log:
2025-02-08 23:20:28.861	E internal error: passed start_height not <  m_db->height() -- 3343083 >= 3343083
2025-02-08 23:20:28.917	I ###### REORGANIZE on height: 3343084 of 3343082 with cum_difficulty 421245755676214153
2025-02-08 23:20:28.917	I  alternative blockchain size: 1 with cum_difficulty 421246732671934804

The monerod process do seem to do something but generally it seems frozen as killing using ctrl+c does not work. Either not implemented or the code is in some infinite loop. 

Killing process using kill command works. 

What could be the cause to this ? 

# Discussion History
## selsta | 2025-02-08T23:31:56+00:00
What command did you use to prune?

## tendermonster | 2025-02-08T23:36:52+00:00
> What command did you use to prune?

as simple as --prune-blockchain. The operation was completed successfully.  By now i've tried older versions of monerod but still same problem persist. monerod --no-sync works fine. With that i can cancel the process using ctrl+c.

While running the monerod does seem to read and write periodically in about 2mb/s to disk 

## selsta | 2025-02-09T09:57:59+00:00
Just so that I understand it correctly, you used `--prune-blockchain` on an existing synced node? If yes, how long did you wait for it to run? As far as I know it can take multiple hours.

Also can you share what it prints with `--log-level 2`?

## tendermonster | 2025-02-09T10:46:56+00:00
The log is composed of errors like this:
```
2025-02-09 10:44:55.111	I Transaction added to pool: txid <8ba117c63ffdf4a96e34c6c07059e56fc889928a4b5efce455deb410e9e0c0c9> weight: 5665 fee/byte: 20017.7, count: 242206
2025-02-09 10:44:55.111	D Mixin: 15-15
2025-02-09 10:44:55.111	D RCT cache: tx <7442387f91c49114d4953243a1b05c55243065e8041671745512abb8284e66eb> missed
2025-02-09 10:44:55.116	I Transaction added to pool: txid <7442387f91c49114d4953243a1b05c55243065e8041671745512abb8284e66eb> weight: 2893 fee/byte: 20020.7, count: 242207
2025-02-09 10:44:55.116	D Mixin: 15-15
2025-02-09 10:44:55.116	D RCT cache: tx <892ed56f59f1feacc38857576bd398d78e3f3723a7285b0de3c8ff1b553f9027> missed
2025-02-09 10:44:55.121	I Transaction added to pool: txid <892ed56f59f1feacc38857576bd398d78e3f3723a7285b0de3c8ff1b553f9027> weight: 1533 fee/byte: 20691.5, count: 242208
2025-02-09 10:44:55.121	D Mixin: 15-15
```

Followed by:
```
2025-02-09 10:49:10.017	I Transaction added to pool: txid <486723a29048f1a938cc4cfae0c1da43e5e197291d5c1132c383163d11d81b02> weight: 1539 fee/byte: 320000, count: 265350
2025-02-09 10:49:10.376	I Pool weight after pruning is larger than limit: 648974571/648000000
2025-02-09 10:49:10.376	D Mixin: 15-15
2025-02-09 10:49:10.385	D RCT cache: tx <5e3bd35e39e3ce4498d4b371198d3b1621433fd2362ccf8f6b67f303f2e93e15> missed
```


## tendermonster | 2025-02-09T22:16:28+00:00
even though i did not manage to resolve this particular issue, resyncing the bc with --prune-blockchain --sync-pruned-blocks did make monerod work properly

# Action History
- Created by: tendermonster | 2025-02-08T23:25:23+00:00
- Closed at: 2025-02-09T22:16:28+00:00
