---
title: ~BlockchainLMDB() throws if is opened in readonly mode (DBF_RDONLY)
source_url: https://github.com/monero-project/monero/issues/4144
author: moneroexamples
assignees: []
labels: []
created_at: '2018-07-17T03:47:10+00:00'
updated_at: '2018-07-17T05:11:22+00:00'
type: issue
status: closed
closed_at: '2018-07-17T05:11:22+00:00'
---

# Original Description
I just wonder if this is expected or I misunderstand how it all works?

The `BlockchainLMDB::~BlockchainLMDB()` calls `BlockchainLMDB::close()` which in turn calls `BlockchainLMDB::sync()`. Subsequently `BlockchainLMDB::sync()` throws exception `throw0(DB_ERROR(lmdb_error("Failed to sync database: ", result).c_str()));` as lmdb is open in read only mode.

This is problematic, because you can't delete BlockchainLMDB() instances open in DBF_RDONLY mode, which leads to application crash as exception is thrown from its destructor or memory leaks. 

For instance,  `blockchain_export` utility  which opens lmdb in DBF_RDONLY mode. It uses `new` to create `BlockchainLMDB`, but never tries to `delete` it. In this case there is memory leak, because you cant `delete` the object.





# Discussion History
## stoffu | 2018-07-17T05:05:32+00:00
This should be fixed in #4129.

## moneroexamples | 2018-07-17T05:11:22+00:00
Cool. So no just waiting till it gets merged. Closing the issue.



# Action History
- Created by: moneroexamples | 2018-07-17T03:47:10+00:00
- Closed at: 2018-07-17T05:11:22+00:00
