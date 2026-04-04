---
title: data.mdb doesn't transfer between systems
source_url: https://github.com/monero-project/monero/issues/1186
author: Gingeropolous
assignees: []
labels:
- invalid
created_at: '2016-10-06T02:07:48+00:00'
updated_at: '2017-08-12T20:12:12+00:00'
type: issue
status: closed
closed_at: '2017-08-12T20:12:12+00:00'
---

# Original Description
system 1, downloaded release binaries, ran monerod to sync. Then transferred same binaries and the data.mdb to system 2, and this happens

2016-Oct-05 22:02:55.767695 Monero 'Wolfram Warptangent' (v0.10.0.0-release)
2016-Oct-05 22:02:55.767895 Forking to background...
2016-Oct-05 22:02:55.771955 Monero 'Wolfram Warptangent' (v0.10.0.0-release
2016-Oct-05 22:02:55.772078 Initializing cryptonote protocol...
2016-Oct-05 22:02:55.772107 Cryptonote protocol initialized OK
2016-Oct-05 22:02:55.772143 Blockchain::Blockchain
2016-Oct-05 22:02:55.772489 Initializing p2p server...
2016-Oct-05 22:02:56.120265 Seed node: 107.5.178.229:18080
2016-Oct-05 22:02:56.120433 Seed node: 119.114.77.217:18080
2016-Oct-05 22:02:56.120495 Seed node: 138.201.137.226:18080
2016-Oct-05 22:02:56.120529 Seed node: 173.208.164.226:18080
2016-Oct-05 22:02:56.120565 Seed node: 188.142.218.19:18080
2016-Oct-05 22:02:56.120609 Seed node: 192.111.57.160:18080
2016-Oct-05 22:02:56.120639 Seed node: 40.84.148.217:18080
2016-Oct-05 22:02:56.120668 Seed node: 71.224.11.214:18080
2016-Oct-05 22:02:56.120697 Seed node: 78.46.94.35:18080
2016-Oct-05 22:02:56.120726 Seed node: 82.95.208.173:18080
2016-Oct-05 22:02:56.120755 Seed node: 83.212.99.89:18080
2016-Oct-05 22:02:56.120784 Seed node: 85.17.15.137:18080
2016-Oct-05 22:02:56.120813 Seed node: 85.194.238.202:18080
2016-Oct-05 22:02:56.120841 Seed node: 95.67.228.50:18080
2016-Oct-05 22:02:56.120870 Number of seed nodes: 14
2016-Oct-05 22:02:56.121744 Set limit-up to 2048 kB/s
2016-Oct-05 22:02:56.121878 Set limit-down to 8192 kB/s
2016-Oct-05 22:02:56.121921 Set limit-up to 2048 kB/s
2016-Oct-05 22:02:56.121978 Set limit-down to 8192 kB/s
2016-Oct-05 22:02:56.126136 Binding on 0.0.0.0:18080
2016-Oct-05 22:02:56.126263 Net service bound to 0.0.0.0:18080
2016-Oct-05 22:02:56.126295 Attempting to add IGD port mapping.
2016-Oct-05 22:03:00.130341 No IGD was found.
2016-Oct-05 22:03:00.130448 P2p server initialized OK
2016-Oct-05 22:03:00.130565 Initializing core rpc server...
2016-Oct-05 22:03:00.130643 Binding on 127.0.0.1:18081
2016-Oct-05 22:03:00.130749 Core rpc server initialized OK on port: 18081
2016-Oct-05 22:03:00.130777 Initializing core...
2016-Oct-05 22:03:00.131180 Locking //.bitmonero/.daemon_lock
2016-Oct-05 22:03:00.131211 BlockchainLMDB::BlockchainLMDB
2016-Oct-05 22:03:00.131229 BlockchainLMDB::get_db_name
2016-Oct-05 22:03:00.131243 Loading blockchain from folder //.bitmonero/lmdb ...
2016-Oct-05 22:03:00.131266 option: fast
2016-Oct-05 22:03:00.131281 option: async
2016-Oct-05 22:03:00.131294 option: 1000
2016-Oct-05 22:03:00.131314 BlockchainLMDB::open
2016-Oct-05 22:03:00.131413 BlockchainLMDB::need_resize
2016-Oct-05 22:03:00.131433 DB map size:     13958643712
2016-Oct-05 22:03:00.131447 Space used:      8274526208
2016-Oct-05 22:03:00.131461 Space remaining: 5684117504
2016-Oct-05 22:03:00.131475 Size threshold:  0
2016-Oct-05 22:03:00.131510 Percent used: 0.5928  Percent threshold: 0.8000
2016-Oct-05 22:03:00.131580 Setting m_height to: 1151170
2016-Oct-05 22:03:00.341577 Monero 'Wolfram Warptangent' (v0.10.0.0-release)
2016-Oct-05 22:03:00.342566 Forking to background...
2016-Oct-05 22:03:00.345766 Monero 'Wolfram Warptangent' (v0.10.0.0-release
2016-Oct-05 22:03:00.345879 Initializing cryptonote protocol...
2016-Oct-05 22:03:00.345908 Cryptonote protocol initialized OK
2016-Oct-05 22:03:00.345943 Blockchain::Blockchain
2016-Oct-05 22:03:00.346273 Initializing p2p server...
2016-Oct-05 22:03:00.575280 Seed node: 107.5.178.229:18080
2016-Oct-05 22:03:00.575460 Seed node: 119.114.77.217:18080
2016-Oct-05 22:03:00.575520 Seed node: 138.201.137.226:18080
2016-Oct-05 22:03:00.575554 Seed node: 173.208.164.226:18080
2016-Oct-05 22:03:00.575583 Seed node: 188.142.218.19:18080
2016-Oct-05 22:03:00.575612 Seed node: 192.111.57.160:18080
2016-Oct-05 22:03:00.575641 Seed node: 40.84.148.217:18080
2016-Oct-05 22:03:00.575670 Seed node: 71.224.11.214:18080
2016-Oct-05 22:03:00.575699 Seed node: 78.46.94.35:18080
2016-Oct-05 22:03:00.575727 Seed node: 82.95.208.173:18080
2016-Oct-05 22:03:00.575756 Seed node: 83.212.99.89:18080
2016-Oct-05 22:03:00.575785 Seed node: 85.17.15.137:18080
2016-Oct-05 22:03:00.575813 Seed node: 85.194.238.202:18080
2016-Oct-05 22:03:00.575841 Seed node: 95.67.228.50:18080
2016-Oct-05 22:03:00.575870 Number of seed nodes: 14
2016-Oct-05 22:03:00.576729 Set limit-up to 2048 kB/s
2016-Oct-05 22:03:00.576865 Set limit-down to 8192 kB/s
2016-Oct-05 22:03:00.576908 Set limit-up to 2048 kB/s
2016-Oct-05 22:03:00.576966 Set limit-down to 8192 kB/s
2016-Oct-05 22:03:00.581093 Binding on 0.0.0.0:18080
2016-Oct-05 22:03:00.581221 Net service bound to 0.0.0.0:18080
2016-Oct-05 22:03:00.581253 Attempting to add IGD port mapping.
2016-Oct-05 22:03:04.589337 No IGD was found.
2016-Oct-05 22:03:04.589433 P2p server initialized OK
2016-Oct-05 22:03:04.589551 Initializing core rpc server...
2016-Oct-05 22:03:04.589627 Binding on 127.0.0.1:18081
2016-Oct-05 22:03:04.589737 Core rpc server initialized OK on port: 18081
2016-Oct-05 22:03:04.589765 Initializing core...
2016-Oct-05 22:03:04.590165 Locking //.bitmonero/.daemon_lock
2016-Oct-05 22:03:04.590198 BlockchainLMDB::BlockchainLMDB
2016-Oct-05 22:03:04.590215 BlockchainLMDB::get_db_name
2016-Oct-05 22:03:04.590230 Loading blockchain from folder //.bitmonero/lmdb ...
2016-Oct-05 22:03:04.590253 option: fast
2016-Oct-05 22:03:04.590267 option: async
2016-Oct-05 22:03:04.590280 option: 1000
2016-Oct-05 22:03:04.590300 BlockchainLMDB::open
2016-Oct-05 22:03:04.590399 BlockchainLMDB::need_resize
2016-Oct-05 22:03:04.590419 DB map size:     13958643712
2016-Oct-05 22:03:04.590434 Space used:      8274526208
2016-Oct-05 22:03:04.590447 Space remaining: 5684117504
2016-Oct-05 22:03:04.590461 Size threshold:  0
2016-Oct-05 22:03:04.590496 Percent used: 0.5928  Percent threshold: 0.8000
2016-Oct-05 22:03:04.590569 Setting m_height to: 1151170
2016-Oct-05 22:03:05.206098 Monero 'Wolfram Warptangent' (v0.10.0.0-release)
2016-Oct-05 22:03:05.206267 Forking to background...
2016-Oct-05 22:03:05.211147 Monero 'Wolfram Warptangent' (v0.10.0.0-release
2016-Oct-05 22:03:05.211260 Initializing cryptonote protocol...
2016-Oct-05 22:03:05.211290 Cryptonote protocol initialized OK
2016-Oct-05 22:03:05.211352 Blockchain::Blockchain
2016-Oct-05 22:03:05.211680 Initializing p2p server...
2016-Oct-05 22:03:05.690566 Seed node: 107.5.178.229:18080
2016-Oct-05 22:03:05.690727 Seed node: 119.114.77.217:18080
2016-Oct-05 22:03:05.690788 Seed node: 138.201.137.226:18080
2016-Oct-05 22:03:05.690821 Seed node: 173.208.164.226:18080
2016-Oct-05 22:03:05.690852 Seed node: 188.142.218.19:18080
2016-Oct-05 22:03:05.690881 Seed node: 192.111.57.160:18080
2016-Oct-05 22:03:05.690911 Seed node: 40.84.148.217:18080
2016-Oct-05 22:03:05.690940 Seed node: 71.224.11.214:18080
2016-Oct-05 22:03:05.690968 Seed node: 78.46.94.35:18080
2016-Oct-05 22:03:05.690997 Seed node: 82.95.208.173:18080
2016-Oct-05 22:03:05.691027 Seed node: 83.212.99.89:18080
2016-Oct-05 22:03:05.691056 Seed node: 85.17.15.137:18080
2016-Oct-05 22:03:05.691085 Seed node: 85.194.238.202:18080
2016-Oct-05 22:03:05.691114 Seed node: 95.67.228.50:18080
2016-Oct-05 22:03:05.691142 Number of seed nodes: 14
2016-Oct-05 22:03:05.691998 Set limit-up to 2048 kB/s
2016-Oct-05 22:03:05.692135 Set limit-down to 8192 kB/s
2016-Oct-05 22:03:05.692178 Set limit-up to 2048 kB/s
2016-Oct-05 22:03:05.692236 Set limit-down to 8192 kB/s
2016-Oct-05 22:03:05.696255 Binding on 0.0.0.0:18080
2016-Oct-05 22:03:05.696504 Net service bound to 0.0.0.0:18080
2016-Oct-05 22:03:05.696540 Attempting to add IGD port mapping.
2016-Oct-05 22:03:09.700294 No IGD was found.
2016-Oct-05 22:03:09.700333 P2p server initialized OK
2016-Oct-05 22:03:09.700439 Initializing core rpc server...
2016-Oct-05 22:03:09.700505 Binding on 127.0.0.1:18081
2016-Oct-05 22:03:09.700606 Core rpc server initialized OK on port: 18081
2016-Oct-05 22:03:09.700625 Initializing core...
2016-Oct-05 22:03:09.701015 Locking //.bitmonero/.daemon_lock
2016-Oct-05 22:03:09.701035 BlockchainLMDB::BlockchainLMDB
2016-Oct-05 22:03:09.701044 BlockchainLMDB::get_db_name
2016-Oct-05 22:03:09.701051 Loading blockchain from folder //.bitmonero/lmdb ...
2016-Oct-05 22:03:09.701067 option: fast
2016-Oct-05 22:03:09.701074 option: async
2016-Oct-05 22:03:09.701081 option: 1000
2016-Oct-05 22:03:09.701094 BlockchainLMDB::open
2016-Oct-05 22:03:09.701178 BlockchainLMDB::need_resize
2016-Oct-05 22:03:09.701188 DB map size:     13958643712
2016-Oct-05 22:03:09.701195 Space used:      8274526208
2016-Oct-05 22:03:09.701202 Space remaining: 5684117504
2016-Oct-05 22:03:09.701210 Size threshold:  0
2016-Oct-05 22:03:09.701238 Percent used: 0.5928  Percent threshold: 0.8000
2016-Oct-05 22:03:09.701304 Setting m_height to: 1151170
2016-Oct-05 22:03:10.436678 Monero 'Wolfram Warptangent' (v0.10.0.0-release)
2016-Oct-05 22:03:10.436791 Forking to background...
2016-Oct-05 22:03:10.439692 Monero 'Wolfram Warptangent' (v0.10.0.0-release
2016-Oct-05 22:03:10.439782 Initializing cryptonote protocol...
2016-Oct-05 22:03:10.439792 Cryptonote protocol initialized OK
2016-Oct-05 22:03:10.439811 Blockchain::Blockchain
2016-Oct-05 22:03:10.440116 Initializing p2p server...
2016-Oct-05 22:03:10.952004 Seed node: 107.5.178.229:18080
2016-Oct-05 22:03:10.952098 Seed node: 119.114.77.217:18080
2016-Oct-05 22:03:10.952146 Seed node: 138.201.137.226:18080
2016-Oct-05 22:03:10.952169 Seed node: 173.208.164.226:18080
2016-Oct-05 22:03:10.952190 Seed node: 188.142.218.19:18080
2016-Oct-05 22:03:10.952211 Seed node: 192.111.57.160:18080
2016-Oct-05 22:03:10.952231 Seed node: 40.84.148.217:18080
2016-Oct-05 22:03:10.952251 Seed node: 71.224.11.214:18080
2016-Oct-05 22:03:10.952279 Seed node: 78.46.94.35:18080
2016-Oct-05 22:03:10.952302 Seed node: 82.95.208.173:18080
2016-Oct-05 22:03:10.952323 Seed node: 83.212.99.89:18080
2016-Oct-05 22:03:10.952343 Seed node: 85.17.15.137:18080
2016-Oct-05 22:03:10.952363 Seed node: 85.194.238.202:18080
2016-Oct-05 22:03:10.952383 Seed node: 95.67.228.50:18080
2016-Oct-05 22:03:10.952402 Number of seed nodes: 14
2016-Oct-05 22:03:10.953258 Set limit-up to 2048 kB/s
2016-Oct-05 22:03:10.953383 Set limit-down to 8192 kB/s
2016-Oct-05 22:03:10.953415 Set limit-up to 2048 kB/s
2016-Oct-05 22:03:10.953464 Set limit-down to 8192 kB/s
2016-Oct-05 22:03:10.957541 Binding on 0.0.0.0:18080
2016-Oct-05 22:03:10.957634 Net service bound to 0.0.0.0:18080
2016-Oct-05 22:03:10.957643 Attempting to add IGD port mapping.


# Discussion History
## radfish | 2016-11-18T23:56:28+00:00
So, the process is crashing? segfault? And, what is restarting the process? systemd?


## moneromooo-monero | 2017-03-18T10:56:01+00:00
I see no indication whatsoever that this has anything to do with data.mdb...

## moneromooo-monero | 2017-08-09T09:44:32+00:00
Reopen if there's any more information.

+invalid

## moneromooo-monero | 2017-08-12T20:03:31+00:00
+resolved

# Action History
- Created by: Gingeropolous | 2016-10-06T02:07:48+00:00
- Closed at: 2017-08-12T20:12:12+00:00
