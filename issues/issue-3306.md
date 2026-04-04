---
title: Free disk space displayed incorrectly
source_url: https://github.com/monero-project/monero/issues/3306
author: brad-richards
assignees: []
labels: []
created_at: '2018-02-23T07:07:44+00:00'
updated_at: '2018-03-05T22:40:37+00:00'
type: issue
status: closed
closed_at: '2018-03-05T22:40:37+00:00'
---

# Original Description
When there is too little disk space to expand the blockchain db, monerod executes the code (monero/src/blockchain_db/lmdb/db_lmdb.cpp line 454)
```
boost::filesystem::space_info si = boost::filesystem::space(path);
    if(si.available < add_size)
    {
      MERROR("!! WARNING: Insufficient free space to extend database !!: " << si.available / 1LL << 20L);
      return;
    }
```
The calculation in the error message is incorrect: it divides the available disk space by 1, then multiplies it by 2^20, giving an unreasonably large number. If the goal is to display it in MB, then something like `si.available >> 20` would be better. The message should then also display the unit (i.e. "MB").

# Discussion History
## moneromooo-monero | 2018-02-23T09:07:17+00:00
Thanks, https://github.com/monero-project/monero/pull/3307

## moneromooo-monero | 2018-03-05T22:33:39+00:00
+resolved

# Action History
- Created by: brad-richards | 2018-02-23T07:07:44+00:00
- Closed at: 2018-03-05T22:40:37+00:00
