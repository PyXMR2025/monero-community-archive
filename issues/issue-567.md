---
title: 'blockchain export: Failed to create a transaction for the db: Permission denied'
source_url: https://github.com/monero-project/monero/issues/567
author: Gingeropolous
assignees: []
labels: []
created_at: '2015-12-26T20:45:00+00:00'
updated_at: '2016-10-04T02:41:07+00:00'
type: issue
status: closed
closed_at: '2016-10-04T02:41:07+00:00'
---

# Original Description
My current blockchain_utilities.h

//define SOURCE_DB DB_MEMORY
# define SOURCE_DB DB_LMDB

// to use global compile-time setting (DB_MEMORY or DB_LMDB):
// #define SOURCE_DB BLOCKCHAIN_DB

I got this:

e5405@e5405-G31M-ES2L:~/bitmonero_20151226/bitmonero/build/release/bin$  ./blockchain_export --output-file 20151226_blockchain.raw  
2015-Dec-26 15:40:21.116600 Starting...  
2015-Dec-26 15:40:21.116702 Setting log level = 0  
2015-Dec-26 15:40:21.116783 Export output file: 20151226_blockchain.raw  
2015-Dec-26 15:40:21.116855 Initializing source blockchain (BlockchainDB)  
2015-Dec-26 15:40:21.116953 Loading blockchain from folder /home/e5405/.bitmonero/lmdb ...  
2015-Dec-26 15:40:21.177531 Failed to create a transaction for the db: Permission denied  
terminate called after throwing an instance of 'cryptonote::DB_ERROR'  
  what():  Failed to create a transaction for the db: Permission denied  
Aborted (core dumped)  
e5405@e5405-G31M-ES2L:~/bitmonero_20151226/bitmonero/build/release/bin$

troubleshooting attempts:

tried without flags, tried stopping the daemon and then performing. All fail. 


# Discussion History
## moneroexamples | 2016-01-05T08:54:14+00:00
Seems to be working now.


## ghost | 2016-09-18T21:49:32+00:00
Hi @Gingeropolous and @moneroexamples - is this still an active issue or can it be closed?


## Gingeropolous | 2016-10-04T02:41:07+00:00
I'm assuming fixed considering all the work done with the DB. 


# Action History
- Created by: Gingeropolous | 2015-12-26T20:45:00+00:00
- Closed at: 2016-10-04T02:41:07+00:00
