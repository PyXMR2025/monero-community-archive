---
title: 'Failed to create a transaction for the db: Permission denied'
source_url: https://github.com/monero-project/monero/issues/5438
author: moneroexamples
assignees: []
labels: []
created_at: '2019-04-14T06:19:23+00:00'
updated_at: '2019-04-16T22:17:33+00:00'
type: issue
status: closed
closed_at: '2019-04-16T22:17:33+00:00'
---

# Original Description
Just found this issue in my projects, but now I see it also affects monero's blockchain utilities. 

For example, running `./monero-blockchain-export` produces the following error:

```
mdb/db_lmdb.cpp:75	Failed to create a transaction for the db: Permission denied
2019-04-14 06:12:07.065	    7fe3e4f38bc0	ERROR	bcutil	src/blockchain_utilities/blockchain_export.cpp:204	Exception at [Export error], what=Failed to create a transaction for the db: Permission denied
```

I think it has something to do that the blockchain is being opened in read only mode (DBF_RDONLY). 

# Discussion History
## moneromooo-monero | 2019-04-14T08:36:35+00:00
I merged the fix in https://github.com/monero-project/monero/pull/5400

## moneroexamples | 2019-04-14T08:58:45+00:00
Thanks! Its working. I will leave the issue open till the PR gets merged. 

## moneromooo-monero | 2019-04-16T22:12:01+00:00
+resolved

# Action History
- Created by: moneroexamples | 2019-04-14T06:19:23+00:00
- Closed at: 2019-04-16T22:17:33+00:00
