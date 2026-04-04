---
title: Monerod can't connect and breaks internet connection
source_url: https://github.com/monero-project/monero/issues/5710
author: rating89us
assignees: []
labels: []
created_at: '2019-06-30T19:16:09+00:00'
updated_at: '2022-02-22T23:39:27+00:00'
type: issue
status: closed
closed_at: '2022-02-22T23:39:27+00:00'
---

# Original Description
I'm using v0.14.1.0 on win7 64 bits with VPN. Internet connection stops working when monerod is started.

Some logs:

**monerod --log-level 4**
```
2019-06-30 18:51:40.433 I Monero 'Boron Butterfly' (v0.14.1.0-29a505d1c)
2019-06-30 18:51:40.433 I Moving from main() into the daemonize now.
2019-06-30 18:51:40.434 I Initializing cryptonote protocol...
2019-06-30 18:51:40.434 I Cryptonote protocol initialized OK
2019-06-30 18:51:40.435 T Blockchain::Blockchain
2019-06-30 18:51:40.435 I Initializing p2p server...
2019-06-30 18:51:40.589 I Setting LIMIT: 2048 kbps
2019-06-30 18:51:40.590 I Set limit-up to 2048 kB/s
2019-06-30 18:51:40.590 I Setting LIMIT: 8192 kbps
2019-06-30 18:51:40.591 I Setting LIMIT: 8192 kbps
2019-06-30 18:51:40.591 I Set limit-down to 8192 kB/s
2019-06-30 18:51:40.591 I Setting LIMIT: 2048 kbps
2019-06-30 18:51:40.592 I Set limit-up to 2048 kB/s
2019-06-30 18:51:40.592 I Setting LIMIT: 8192 kbps
2019-06-30 18:51:40.593 I Setting LIMIT: 8192 kbps
2019-06-30 18:51:40.593 I Set limit-down to 8192 kB/s
2019-06-30 18:51:40.593 D dns_threads[0] created for: seeds.moneroseeds.se
2019-06-30 18:51:40.594 D dns_threads[1] created for: seeds.moneroseeds.ae.org
2019-06-30 18:51:40.594 D dns_threads created, now waiting for completion or timeout of 20000ms
2019-06-30 18:51:40.595 D dns_threads[2] created for: seeds.moneroseeds.ch
2019-06-30 18:51:40.595 D dns_threads[3] created for: seeds.moneroseeds.li
2019-06-30 18:51:40.622 I adding trust anchor: . IN DS 19036 8 2 49AAC11D7B6F644 6702E54A1607371607A1A41855200FD2CE1CDDE32F24E8FB5
2019-06-30 18:51:40.623 I adding trust anchor: . IN DS 20326 8 2 E06D44B80B8F1D3
9A95C0B0D7C65D08458E880409BBC683457104237C7F8EC8D
2019-06-30 18:52:00.595 W dns_threads[0] timed out, sending interrupt
2019-06-30 18:52:00.596 W dns_threads[1] timed out, sending interrupt
2019-06-30 18:52:00.596 W dns_threads[2] timed out, sending interrupt
2019-06-30 18:52:00.597 W dns_threads[3] timed out, sending interrupt
2019-06-30 18:52:00.597 D DNS lookup for seeds.moneroseeds.se: 0 results
2019-06-30 18:52:00.597 D DNS lookup for seeds.moneroseeds.ae.org: 0 results
2019-06-30 18:52:00.598 D DNS lookup for seeds.moneroseeds.ch: 0 results
2019-06-30 18:52:00.598 D DNS lookup for seeds.moneroseeds.li: 0 results
2019-06-30 18:52:00.599 I DNS seed node lookup either timed out or failed, falli
ng back to defaults
2019-06-30 18:52:00.599 D Seed node: 107.152.130.98:18080
2019-06-30 18:52:00.599 I Resolving node address: host=107.152.130.98, port=18080
2019-06-30 18:52:00.600 I Added node: 107.152.130.98:18080
2019-06-30 18:52:00.600 D Seed node: 161.67.132.39:18080
2019-06-30 18:52:00.601 I Resolving node address: host=161.67.132.39, port=18080
2019-06-30 18:52:00.601 I Added node: 161.67.132.39:18080
2019-06-30 18:52:00.601 D Seed node: 163.172.182.165:18080
2019-06-30 18:52:00.602 I Resolving node address: host=163.172.182.165, port=18080
2019-06-30 18:52:00.602 I Added node: 163.172.182.165:18080
2019-06-30 18:52:00.603 D Seed node: 195.154.123.123:18080
2019-06-30 18:52:00.603 I Resolving node address: host=195.154.123.123, port=18080
2019-06-30 18:52:00.603 I Added node: 195.154.123.123:18080
2019-06-30 18:52:00.604 D Seed node: 198.74.231.92:18080
2019-06-30 18:52:00.604 I Resolving node address: host=198.74.231.92, port=18080
2019-06-30 18:52:00.605 I Added node: 198.74.231.92:18080
2019-06-30 18:52:00.605 D Seed node: 212.83.172.165:18080
2019-06-30 18:52:00.605 I Resolving node address: host=212.83.172.165, port=18080
2019-06-30 18:52:00.606 I Added node: 212.83.172.165:18080
2019-06-30 18:52:00.606 D Seed node: 212.83.175.67:18080
2019-06-30 18:52:00.606 I Resolving node address: host=212.83.175.67, port=18080
2019-06-30 18:52:00.607 I Added node: 212.83.175.67:18080
2019-06-30 18:52:00.607 D Seed node: 5.9.100.248:18080
2019-06-30 18:52:00.607 I Resolving node address: host=5.9.100.248, port=18080
2019-06-30 18:52:00.608 I Added node: 5.9.100.248:18080
2019-06-30 18:52:00.608 D Number of seed nodes: 8
2019-06-30 18:52:00.610 I Set server type to: 2 from name: P2P, prefix_name = P2P
2019-06-30 18:52:00.610 I Binding on 0.0.0.0:18080
2019-06-30 18:52:00.615 D start accept
2019-06-30 18:52:00.617 D Spawned connection #0 to 0.0.0.0 currently we have sockets count:1
2019-06-30 18:52:00.617 D test, connection constructor set m_connection_type=2
2019-06-30 18:52:00.618 I ←[1;32mNet service bound to 0.0.0.0:18080←[0m
2019-06-30 18:52:00.618 D Attempting to add IGD port mapping.
2019-06-30 18:52:04.626 I No IGD was found.
2019-06-30 18:52:04.626 I p2p server initialized OK
2019-06-30 18:52:04.627 I Initializing core RPC server...
2019-06-30 18:52:04.628 I Set server type to: 1 from name: RPC, prefix_name = RPC
2019-06-30 18:52:04.630 I Binding on 127.0.0.1:18081
2019-06-30 18:52:04.630 I Generating SSL certificate
2019-06-30 18:52:07.471 D start accept
2019-06-30 18:52:07.471 D Spawned connection #0 to 0.0.0.0 currently we have sockets count:1
2019-06-30 18:52:07.472 D test, connection constructor set m_connection_type=1
2019-06-30 18:52:07.472 I core RPC server initialized OK on port: 18081
2019-06-30 18:52:07.473 I Initializing core...
2019-06-30 18:52:07.474 T BlockchainLMDB::BlockchainLMDB
2019-06-30 18:52:07.474 T BlockchainLMDB::get_db_name
2019-06-30 18:52:07.474 I Loading blockchain from folder C:\ProgramData\bitmonero\lmdb ...
2019-06-30 18:52:07.475 D option: fast
2019-06-30 18:52:07.476 D option: async
2019-06-30 18:52:07.476 D option: 250000000bytes
2019-06-30 18:52:07.476 T BlockchainLMDB::open
2019-06-30 18:52:07.493 T BlockchainLMDB::need_resize
2019-06-30 18:52:07.494 D DB map size:     1073741824
2019-06-30 18:52:07.494 D Space used:      86016
2019-06-30 18:52:07.494 D Space remaining: 1073655808
2019-06-30 18:52:07.495 D Size threshold:  0
2019-06-30 18:52:07.495 D Percent used: 0.0001  Percent threshold: 0.9000
2019-06-30 18:52:07.496 D Setting m_height to: 1
2019-06-30 18:52:07.496 T mdb_txn_safe: destructor
2019-06-30 18:52:07.496 T Blockchain::init
2019-06-30 18:52:07.498 T BlockchainLMDB::height
2019-06-30 18:52:07.498 T BlockchainLMDB::block_rtxn_start
2019-06-30 18:52:07.498 T mdb_txn_safe: destructor
2019-06-30 18:52:07.499 T BlockchainLMDB::block_rtxn_start
2019-06-30 18:52:07.499 T BlockchainLMDB::height
2019-06-30 18:52:07.499 T BlockchainLMDB::height
2019-06-30 18:52:07.500 T BlockchainLMDB::get_block_blob_from_height
2019-06-30 18:52:07.500 T BlockchainLMDB::height
2019-06-30 18:52:07.500 T BlockchainLMDB::height
2019-06-30 18:52:07.501 T BlockchainLMDB::get_hard_fork_version
2019-06-30 18:52:07.501 T BlockchainLMDB::height
2019-06-30 18:52:07.502 T BlockchainLMDB::block_rtxn_stop
2019-06-30 18:52:07.503 D init done
2019-06-30 18:52:07.503 T BlockchainLMDB::height
2019-06-30 18:52:07.504 T BlockchainLMDB::block_rtxn_start
2019-06-30 18:52:07.504 T mdb_txn_safe: destructor
2019-06-30 18:52:07.504 T BlockchainLMDB::fixup
2019-06-30 18:52:07.505 T BlockchainLMDB::set_batch_transactions
2019-06-30 18:52:07.505 I batch transaction mode already enabled, but asked to enable batch mode
2019-06-30 18:52:07.506 I batch transactions enabled
2019-06-30 18:52:07.506 T BlockchainLMDB::batch_start
2019-06-30 18:52:07.506 T BlockchainLMDB::check_and_resize_for_batch
2019-06-30 18:52:07.507 T [check_and_resize_for_batch] checking DB size
2019-06-30 18:52:07.507 T BlockchainLMDB::need_resize
2019-06-30 18:52:07.507 D DB map size:     1073741824
2019-06-30 18:52:07.508 D Space used:      86016
2019-06-30 18:52:07.508 D Space remaining: 1073655808
2019-06-30 18:52:07.508 D Size threshold:  0
2019-06-30 18:52:07.509 D Percent used: 0.0001  Percent threshold: 0.9000
2019-06-30 18:52:07.509 T batch transaction: begin
2019-06-30 18:52:07.509 T BlockchainLMDB::get_block_hash_from_height
2019-06-30 18:52:07.510 T BlockchainLMDB::height
2019-06-30 18:52:07.510 T BlockchainLMDB::height
2019-06-30 18:52:07.510 T BlockchainLMDB::batch_stop
2019-06-30 18:52:07.511 T batch transaction: committing...
2019-06-30 18:52:07.511 T mdb_txn_safe: destructor
2019-06-30 18:52:07.511 T batch transaction: end
2019-06-30 18:52:07.512 T BlockchainLMDB::block_rtxn_start
2019-06-30 18:52:07.512 T BlockchainLMDB::get_top_block_timestamp
2019-06-30 18:52:07.512 T BlockchainLMDB::height
2019-06-30 18:52:07.513 T BlockchainLMDB::get_block_timestamp
2019-06-30 18:52:07.513 I Loading precomputed blocks (232004 bytes)
2019-06-30 18:52:07.517 I precomputed blocks hash: <cfca50ea0c87718ac92a14654c60
d7ee8f6453e2765b329b40d10da4ed85a4f2>, expected cfca50ea0c87718ac92a14654c60d7ee
8f6453e2765b329b40d10da4ed85a4f2
2019-06-30 18:52:07.518 T BlockchainLMDB::height
2019-06-30 18:52:07.537 I 7250 block hashes loaded
2019-06-30 18:52:07.537 T BlockchainLMDB::get_txpool_tx_count
2019-06-30 18:52:07.538 T BlockchainLMDB::for_all_txpool_txes
2019-06-30 18:52:07.538 T BlockchainLMDB::height
2019-06-30 18:52:07.538 T Blockchain initialized. last block: 0, d1899.h8.m3.s14
 time ago, current difficulty: Blockchain::get_difficulty_for_next_block
2019-06-30 18:52:07.538 T Blockchain::get_tail_id
2019-06-30 18:52:07.538 T BlockchainLMDB::top_block_hash
2019-06-30 18:52:07.539 T BlockchainLMDB::height
2019-06-30 18:52:07.539 T BlockchainLMDB::get_block_hash_from_height
2019-06-30 18:52:07.539 T Blockchain::get_tail_id
2019-06-30 18:52:07.539 T BlockchainLMDB::top_block_hash
2019-06-30 18:52:07.539 T BlockchainLMDB::height
2019-06-30 18:52:07.539 T BlockchainLMDB::get_block_hash_from_height
2019-06-30 18:52:07.539 I 1
2019-06-30 18:52:07.540 T BlockchainLMDB::block_rtxn_stop
2019-06-30 18:52:07.540 T BlockchainLMDB::top_block_hash
2019-06-30 18:52:07.540 T BlockchainLMDB::height
2019-06-30 18:52:07.540 T BlockchainLMDB::block_rtxn_start
2019-06-30 18:52:07.540 T mdb_txn_safe: destructor
2019-06-30 18:52:07.540 T BlockchainLMDB::get_block_hash_from_height
2019-06-30 18:52:07.540 T BlockchainLMDB::block_rtxn_start
2019-06-30 18:52:07.540 T mdb_txn_safe: destructor
2019-06-30 18:52:07.541 T BlockchainLMDB::get_top_block
2019-06-30 18:52:07.541 T BlockchainLMDB::height
2019-06-30 18:52:07.541 T BlockchainLMDB::block_rtxn_start
2019-06-30 18:52:07.541 T mdb_txn_safe: destructor
2019-06-30 18:52:07.541 T BlockchainLMDB::get_block_blob_from_height
2019-06-30 18:52:07.541 T BlockchainLMDB::block_rtxn_start
2019-06-30 18:52:07.541 T mdb_txn_safe: destructor
2019-06-30 18:52:07.541 T BlockchainLMDB::block_wtxn_start
2019-06-30 18:52:07.542 T Blockchain::update_next_cumulative_weight_limit
2019-06-30 18:52:07.542 T BlockchainLMDB::height
2019-06-30 18:52:07.543 T Blockchain::get_last_n_blocks_weights
2019-06-30 18:52:07.543 T BlockchainLMDB::height
2019-06-30 18:52:07.543 T BlockchainLMDB::get_block_info_64bit_fields
2019-06-30 18:52:07.543 T BlockchainLMDB::height
2019-06-30 18:52:07.543 T BlockchainLMDB::add_max_block_size
2019-06-30 18:52:07.543 T BlockchainLMDB::block_wtxn_stop
2019-06-30 18:52:07.543 T mdb_txn_safe: destructor
2019-06-30 18:52:07.544 T BlockchainLMDB::for_all_txpool_txes
2019-06-30 18:52:07.544 T BlockchainLMDB::block_rtxn_start
2019-06-30 18:52:07.544 T mdb_txn_safe: destructor
2019-06-30 18:52:07.544 T BlockchainLMDB::for_all_txpool_txes
2019-06-30 18:52:07.544 T BlockchainLMDB::block_rtxn_start
2019-06-30 18:52:07.544 T mdb_txn_safe: destructor
2019-06-30 18:52:07.545 T BlockchainLMDB::for_all_txpool_txes
2019-06-30 18:52:07.545 T BlockchainLMDB::block_rtxn_start
2019-06-30 18:52:07.545 T mdb_txn_safe: destructor
2019-06-30 18:52:07.545 I Loading checkpoints
2019-06-30 18:52:07.545 I Blockchain checkpoints file not found
```
**monerod --rpc-bind-port 18089 --log-level 1**
```
2019-06-30 18:56:34.878 I Monero 'Boron Butterfly' (v0.14.1.0-29a505d1c)
2019-06-30 18:56:34.879 I Moving from main() into the daemonize now.
2019-06-30 18:56:34.879 I Initializing cryptonote protocol...
2019-06-30 18:56:34.880 I Cryptonote protocol initialized OK
2019-06-30 18:56:34.881 I Initializing p2p server...
2019-06-30 18:56:35.033 I Setting LIMIT: 2048 kbps
2019-06-30 18:56:35.034 I Set limit-up to 2048 kB/s
2019-06-30 18:56:35.034 I Setting LIMIT: 8192 kbps
2019-06-30 18:56:35.035 I Setting LIMIT: 8192 kbps
2019-06-30 18:56:35.035 I Set limit-down to 8192 kB/s
2019-06-30 18:56:35.036 I Setting LIMIT: 2048 kbps
2019-06-30 18:56:35.036 I Set limit-up to 2048 kB/s
2019-06-30 18:56:35.036 I Setting LIMIT: 8192 kbps
2019-06-30 18:56:35.037 I Setting LIMIT: 8192 kbps
2019-06-30 18:56:35.037 I Set limit-down to 8192 kB/s
2019-06-30 18:56:35.064 I adding trust anchor: . IN DS 19036 8 2 49AAC11D7B6F644
6702E54A1607371607A1A41855200FD2CE1CDDE32F24E8FB5
2019-06-30 18:56:35.064 I adding trust anchor: . IN DS 20326 8 2 E06D44B80B8F1D3
9A95C0B0D7C65D08458E880409BBC683457104237C7F8EC8D
2019-06-30 18:56:55.043 W dns_threads[0] timed out, sending interrupt
2019-06-30 18:56:55.044 W dns_threads[1] timed out, sending interrupt
2019-06-30 18:56:55.045 W dns_threads[2] timed out, sending interrupt
2019-06-30 18:56:55.046 W dns_threads[3] timed out, sending interrupt
2019-06-30 18:56:55.048 I DNS seed node lookup either timed out or failed, falli
ng back to defaults
2019-06-30 18:56:55.049 I Resolving node address: host=107.152.130.98, port=18080
2019-06-30 18:56:55.050 I Added node: 107.152.130.98:18080
2019-06-30 18:56:55.051 I Resolving node address: host=161.67.132.39, port=18080
2019-06-30 18:56:55.053 I Added node: 161.67.132.39:18080
2019-06-30 18:56:55.054 I Resolving node address: host=163.172.182.165, port=18080
2019-06-30 18:56:55.055 I Added node: 163.172.182.165:18080
2019-06-30 18:56:55.056 I Resolving node address: host=195.154.123.123, port=18080
2019-06-30 18:56:55.058 I Added node: 195.154.123.123:18080
2019-06-30 18:56:55.059 I Resolving node address: host=198.74.231.92, port=18080
2019-06-30 18:56:55.061 I Added node: 198.74.231.92:18080
2019-06-30 18:56:55.062 I Resolving node address: host=212.83.172.165, port=18080
2019-06-30 18:56:55.063 I Added node: 212.83.172.165:18080
2019-06-30 18:56:55.064 I Resolving node address: host=212.83.175.67, port=18080
2019-06-30 18:56:55.066 I Added node: 212.83.175.67:18080
2019-06-30 18:56:55.067 I Resolving node address: host=5.9.100.248, port=18080
2019-06-30 18:56:55.069 I Added node: 5.9.100.248:18080
2019-06-30 18:56:55.071 I Set server type to: 2 from name: P2P, prefix_name = P2P
2019-06-30 18:56:55.072 I Binding on 0.0.0.0:18080
2019-06-30 18:56:55.078 I ←[1;32mNet service bound to 0.0.0.0:18080←[0m
2019-06-30 18:56:59.085 I No IGD was found.
2019-06-30 18:56:59.085 I p2p server initialized OK
2019-06-30 18:56:59.088 I Initializing core RPC server...
2019-06-30 18:56:59.088 I Set server type to: 1 from name: RPC, prefix_name = RPC
2019-06-30 18:56:59.091 I Binding on 127.0.0.1:18089
2019-06-30 18:56:59.092 I Generating SSL certificate
2019-06-30 18:57:02.740 I core RPC server initialized OK on port: 18089
2019-06-30 18:57:02.740 I Initializing core...
2019-06-30 18:57:02.741 I Loading blockchain from folder C:\ProgramData\bitmonero\lmdb ...
2019-06-30 18:57:02.756 I batch transaction mode already enabled, but asked to enable batch mode
2019-06-30 18:57:02.756 I batch transactions enabled
2019-06-30 18:57:02.757 I Loading precomputed blocks (232004 bytes)
2019-06-30 18:57:02.761 I precomputed blocks hash: <cfca50ea0c87718ac92a14654c60
d7ee8f6453e2765b329b40d10da4ed85a4f2>, expected cfca50ea0c87718ac92a14654c60d7ee
8f6453e2765b329b40d10da4ed85a4f2
2019-06-30 18:57:02.787 I 7250 block hashes loaded
2019-06-30 18:57:02.788 I Blockchain initialized. last block: 0, d1899.h8.m8.s9
time ago, current difficulty: 1
2019-06-30 18:57:02.789 I Loading checkpoints
2019-06-30 18:57:02.789 I Blockchain checkpoints file not found
```

**monerod --log-level 1,net.p2p:DEBUG**
```
2019-06-30 18:59:43.136 I Monero 'Boron Butterfly' (v0.14.1.0-29a505d1c)
2019-06-30 18:59:43.137 I Moving from main() into the daemonize now.
2019-06-30 18:59:43.137 I Initializing cryptonote protocol...
2019-06-30 18:59:43.138 I Cryptonote protocol initialized OK
2019-06-30 18:59:43.139 I Initializing p2p server...
2019-06-30 18:59:43.294 I Setting LIMIT: 2048 kbps
2019-06-30 18:59:43.296 I Set limit-up to 2048 kB/s
2019-06-30 18:59:43.296 I Setting LIMIT: 8192 kbps
2019-06-30 18:59:43.297 I Setting LIMIT: 8192 kbps
2019-06-30 18:59:43.297 I Set limit-down to 8192 kB/s
2019-06-30 18:59:43.298 I Setting LIMIT: 2048 kbps
2019-06-30 18:59:43.298 I Set limit-up to 2048 kB/s
2019-06-30 18:59:43.298 I Setting LIMIT: 8192 kbps
2019-06-30 18:59:43.299 I Setting LIMIT: 8192 kbps
2019-06-30 18:59:43.299 I Set limit-down to 8192 kB/s
2019-06-30 18:59:43.300 D dns_threads[0] created for: seeds.moneroseeds.se
2019-06-30 18:59:43.300 D dns_threads[1] created for: seeds.moneroseeds.ae.org
2019-06-30 18:59:43.300 D dns_threads[2] created for: seeds.moneroseeds.ch
2019-06-30 18:59:43.301 D dns_threads created, now waiting for completion or timeout of 20000ms
2019-06-30 18:59:43.301 D dns_threads[3] created for: seeds.moneroseeds.li
2019-06-30 18:59:43.325 I adding trust anchor: . IN DS 19036 8 2 49AAC11D7B6F644
6702E54A1607371607A1A41855200FD2CE1CDDE32F24E8FB5
2019-06-30 18:59:43.326 I adding trust anchor: . IN DS 20326 8 2 E06D44B80B8F1D3
9A95C0B0D7C65D08458E880409BBC683457104237C7F8EC8D
2019-06-30 19:00:03.301 W dns_threads[0] timed out, sending interrupt
2019-06-30 19:00:03.302 W dns_threads[1] timed out, sending interrupt
2019-06-30 19:00:03.302 W dns_threads[2] timed out, sending interrupt
2019-06-30 19:00:03.303 W dns_threads[3] timed out, sending interrupt
2019-06-30 19:00:03.303 D DNS lookup for seeds.moneroseeds.se: 0 results
2019-06-30 19:00:03.304 D DNS lookup for seeds.moneroseeds.ae.org: 0 results
2019-06-30 19:00:03.306 D DNS lookup for seeds.moneroseeds.ch: 0 results
2019-06-30 19:00:03.307 D DNS lookup for seeds.moneroseeds.li: 0 results
2019-06-30 19:00:03.308 I DNS seed node lookup either timed out or failed, falli
ng back to defaults
2019-06-30 19:00:03.309 D Seed node: 107.152.130.98:18080
2019-06-30 19:00:03.310 I Resolving node address: host=107.152.130.98, port=18080
2019-06-30 19:00:03.311 I Added node: 107.152.130.98:18080
2019-06-30 19:00:03.312 D Seed node: 161.67.132.39:18080
2019-06-30 19:00:03.313 I Resolving node address: host=161.67.132.39, port=18080
2019-06-30 19:00:03.314 I Added node: 161.67.132.39:18080
2019-06-30 19:00:03.315 D Seed node: 163.172.182.165:18080
2019-06-30 19:00:03.316 I Resolving node address: host=163.172.182.165, port=18080
2019-06-30 19:00:03.318 I Added node: 163.172.182.165:18080
2019-06-30 19:00:03.319 D Seed node: 195.154.123.123:18080
2019-06-30 19:00:03.320 I Resolving node address: host=195.154.123.123, port=18080
2019-06-30 19:00:03.321 I Added node: 195.154.123.123:18080
2019-06-30 19:00:03.322 D Seed node: 198.74.231.92:18080
2019-06-30 19:00:03.323 I Resolving node address: host=198.74.231.92, port=18080
2019-06-30 19:00:03.324 I Added node: 198.74.231.92:18080
2019-06-30 19:00:03.326 D Seed node: 212.83.172.165:18080
2019-06-30 19:00:03.327 I Resolving node address: host=212.83.172.165, port=18080
2019-06-30 19:00:03.328 I Added node: 212.83.172.165:18080
2019-06-30 19:00:03.329 D Seed node: 212.83.175.67:18080
2019-06-30 19:00:03.330 I Resolving node address: host=212.83.175.67, port=18080
2019-06-30 19:00:03.332 I Added node: 212.83.175.67:18080
2019-06-30 19:00:03.333 D Seed node: 5.9.100.248:18080
2019-06-30 19:00:03.334 I Resolving node address: host=5.9.100.248, port=18080
2019-06-30 19:00:03.335 I Added node: 5.9.100.248:18080
2019-06-30 19:00:03.336 D Number of seed nodes: 8
2019-06-30 19:00:03.339 I Set server type to: 2 from name: P2P, prefix_name = P2P
2019-06-30 19:00:03.340 I Binding on 0.0.0.0:18080
2019-06-30 19:00:03.346 I ←[1;32mNet service bound to 0.0.0.0:18080←[0m
2019-06-30 19:00:03.346 D Attempting to add IGD port mapping.
2019-06-30 19:00:07.354 I No IGD was found.
2019-06-30 19:00:07.354 I p2p server initialized OK
2019-06-30 19:00:07.357 I Initializing core RPC server...
2019-06-30 19:00:07.357 I Set server type to: 1 from name: RPC, prefix_name = RPC
2019-06-30 19:00:07.360 I Binding on 127.0.0.1:18081
2019-06-30 19:00:07.361 I Generating SSL certificate
2019-06-30 19:00:08.875 I core RPC server initialized OK on port: 18081
2019-06-30 19:00:08.875 I Initializing core...
2019-06-30 19:00:08.876 I Loading blockchain from folder C:\ProgramData\bitmonero\lmdb ...
2019-06-30 19:00:08.885 I batch transaction mode already enabled, but asked to enable batch mode
2019-06-30 19:00:08.886 I batch transactions enabled
2019-06-30 19:00:08.886 I Loading precomputed blocks (232004 bytes)
2019-06-30 19:00:08.888 I precomputed blocks hash: <cfca50ea0c87718ac92a14654c60
d7ee8f6453e2765b329b40d10da4ed85a4f2>, expected cfca50ea0c87718ac92a14654c60d7ee
8f6453e2765b329b40d10da4ed85a4f2
2019-06-30 19:00:08.904 I 7250 block hashes loaded
2019-06-30 19:00:08.904 I Blockchain initialized. last block: 0, d1899.h8.m11.s1
5 time ago, current difficulty: 1
2019-06-30 19:00:08.905 I Loading checkpoints
2019-06-30 19:00:08.906 I Blockchain checkpoints file not found
```

# Discussion History
## MoneroChan | 2019-07-04T14:23:52+00:00
If your "Internet connection stops working " ,As in, it affects "all your other programs connecting to the internet", then i suspect it's a firewall / antivirus failsafe or VPN Level P2P restriction. 
There's not much other reason why Monerod would break the connection for other programs.

Possible solution: I recommend connecting to a VPN server that permits P2P.

## selsta | 2022-02-22T21:28:37+00:00
@rating89us is this still relevant or can it be closed?

## rating89us | 2022-02-22T23:39:27+00:00
This bug is not present in last GUI version.

# Action History
- Created by: rating89us | 2019-06-30T19:16:09+00:00
- Closed at: 2022-02-22T23:39:27+00:00
