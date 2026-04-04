---
title: Lmdb error after disconnecting HDD
source_url: https://github.com/monero-project/monero/issues/1939
author: mrosseel
assignees: []
labels:
- invalid
created_at: '2017-03-28T20:12:35+00:00'
updated_at: '2017-09-20T21:24:27+00:00'
type: issue
status: closed
closed_at: '2017-09-20T21:24:27+00:00'
---

# Original Description
Hi,

I was doing my initial sync on a raspberry pi 3 with USB HDD (1Tb). Monero 0.10.3.0 was installed on this drive (/mnt) and started with '--data-dir /mnt/monero_chain'. Everything worked fine, but after 20k blocks the HDD disconnected (not sure why). 

The next run I get this:
https://gist.github.com/mrosseel/541647833bd3983ea61c4b3155e06845

Let me know if more info is needed. Is there any way to recover this? Restarting is painful on the pi!

# Discussion History
## hyc | 2017-03-28T20:28:07+00:00
Unfortunately we don't really have a mechanism for recovering from hardware failures. It's possible that we can salvage this DB still. Find me on IRC and we can try to walk through it. You will need mdb_stat built from the monero source tree, and a binary file editor.

## iamsmooth | 2017-04-16T08:47:59+00:00
This is not an issue with the code. Please close.

## moneromooo-monero | 2017-09-20T21:04:50+00:00
There is a new --db-salvage option now, which might help in case of bad sector or something in the last tx writes. Otherwise, a resync from scratch on good media seems necessary.

+invalid

# Action History
- Created by: mrosseel | 2017-03-28T20:12:35+00:00
- Closed at: 2017-09-20T21:24:27+00:00
