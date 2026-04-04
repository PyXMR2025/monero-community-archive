---
title: A bug about monero-blockchain-import.
source_url: https://github.com/monero-project/monero/issues/2566
author: p1gd0g
assignees: []
labels: []
created_at: '2017-10-03T07:03:05+00:00'
updated_at: '2017-10-03T09:32:36+00:00'
type: issue
status: closed
closed_at: '2017-10-03T09:32:36+00:00'
---

# Original Description
The option "--data-dir" in monero-blockchain-import had been removed, but you still see it in "--help".

https://github.com/monero-project/monero/blob/a2041c98742154df4360831c99cfd9200a5620c2/src/blockchain_utilities/blockchain_import.cpp#L588

Someone is confused at this.
https://monero.stackexchange.com/questions/6219/bootstrap-import-data-dir-command-not-working/6228#6228

# Discussion History
## moneromooo-monero | 2017-10-03T08:15:21+00:00
These lines are obsolete, I'll remove them. The data dir and a couple others are now set by the core. Anyway, it works for me:

$ ./build/debug/bin/monero-blockchain-import --data-dir /home/user/FOO-dd --input-file blockchain.raw

2017-10-03 08:12:01.140	    7ce5648bd880	INFO 	bcutil	src/blockchain_utilities/blockchain_import.cpp:719	database path:       /home/user/FOO-dd

$ ls ~/FOO-dd/lmdb/
data.mdb  lock.mdb


# Action History
- Created by: p1gd0g | 2017-10-03T07:03:05+00:00
- Closed at: 2017-10-03T09:32:36+00:00
