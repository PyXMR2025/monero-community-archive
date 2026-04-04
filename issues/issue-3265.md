---
title: New Blockchain Sync E Block verification failed, is it a blocker?
source_url: https://github.com/monero-project/monero-gui/issues/3265
author: gab81
assignees: []
labels: []
created_at: '2020-12-10T08:40:50+00:00'
updated_at: '2020-12-13T13:29:19+00:00'
type: issue
status: closed
closed_at: '2020-12-13T13:29:19+00:00'
---

# Original Description
hi,

I had to re-sync all the blockchain. I've used the raw downloaded file... during database import process, at the very end i had:

**E Block verification failed, id** = e8404e3fda0393dfXXXXXXXXXXXXXXXXXXXXXXXXd5bd1ea6eb ? it happened twice as i wanted to be double sure.

however it completed afterwards 

Number of blocks imported: 2237438
Finished at block: 2237439  total blocks: 2237440

and now i am running monerod and is catching up latest blocks. is that an issue?

thanks

# Discussion History
## gab81 | 2020-12-10T10:04:46+00:00
oh and also now that it's synced the new database / blockchain size is 100 GB is that right?

## selsta | 2020-12-13T13:29:19+00:00
Yes, 100GB sounds correct. ~30GB when pruned.

Closing as the issue seems resolved.

# Action History
- Created by: gab81 | 2020-12-10T08:40:50+00:00
- Closed at: 2020-12-13T13:29:19+00:00
