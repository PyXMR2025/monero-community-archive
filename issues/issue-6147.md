---
title: v0.15.0.0, systemd, lmdb corruption
source_url: https://github.com/monero-project/monero/issues/6147
author: HashVault
assignees: []
labels: []
created_at: '2019-11-16T11:42:17+00:00'
updated_at: '2019-11-18T19:25:21+00:00'
type: issue
status: closed
closed_at: '2019-11-18T19:25:21+00:00'
---

# Original Description
**OS**: Ubuntu 18.04.3 LTS, 4.15.0-58-generic

**Monerod**: 
```
linux-vdso.so.1 (0x00007ffddcf95000)
librt.so.1 => /lib/x86_64-linux-gnu/librt.so.1 (0x00007f202a4a7000)
libboost_chrono.so.1.70.0 => /usr/local/src/boost_1_70_0/stage/lib/libboost_chrono.so.1.70.0 (0x00007f202a29c000)
libboost_filesystem.so.1.70.0 => /usr/local/src/boost_1_70_0/stage/lib/libboost_filesystem.so.1.70.0 (0x00007f202a080000)
libboost_program_options.so.1.70.0 => /usr/local/src/boost_1_70_0/stage/lib/libboost_program_options.so.1.70.0 (0x00007f2029dfa000)
libboost_regex.so.1.70.0 => /usr/local/src/boost_1_70_0/stage/lib/libboost_regex.so.1.70.0 (0x00007f2029b1e000)
libzmq.so.5 => /usr/lib/x86_64-linux-gnu/libzmq.so.5 (0x00007f2029884000)
libsodium.so.23 => /usr/lib/x86_64-linux-gnu/libsodium.so.23 (0x00007f2029633000)
libreadline.so.7 => /lib/x86_64-linux-gnu/libreadline.so.7 (0x00007f20293ea000)
libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007f20291e6000)
libunbound.so.2 => /usr/lib/x86_64-linux-gnu/libunbound.so.2 (0x00007f2028f3c000)
libssl.so.1.1 => /usr/lib/x86_64-linux-gnu/libssl.so.1.1 (0x00007f2028caf000)
libcrypto.so.1.1 => /usr/lib/x86_64-linux-gnu/libcrypto.so.1.1 (0x00007f20287e4000)
libboost_serialization.so.1.70.0 => /usr/local/src/boost_1_70_0/stage/lib/libboost_serialization.so.1.70.0 (0x00007f20285a2000)
libboost_thread.so.1.70.0 => /usr/local/src/boost_1_70_0/stage/lib/libboost_thread.so.1.70.0 (0x00007f202837c000)
libstdc++.so.6 => /usr/lib/x86_64-linux-gnu/libstdc++.so.6 (0x00007f2027ff3000)
libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007f2027c55000)
libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007f2027a3d000)
libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007f202781e000)
libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f202742d000)
/lib64/ld-linux-x86-64.so.2 (0x00007f202b4d7000)
libicui18n.so.60 => /usr/lib/x86_64-linux-gnu/libicui18n.so.60 (0x00007f2026f8c000)
libicuuc.so.60 => /usr/lib/x86_64-linux-gnu/libicuuc.so.60 (0x00007f2026bd5000)
libpgm-5.2.so.0 => /usr/lib/x86_64-linux-gnu/libpgm-5.2.so.0 (0x00007f2026989000)
libnorm.so.1 => /usr/lib/x86_64-linux-gnu/libnorm.so.1 (0x00007f2026659000)
libtinfo.so.5 => /lib/x86_64-linux-gnu/libtinfo.so.5 (0x00007f202642f000)
libevent-2.1.so.6 => /usr/lib/x86_64-linux-gnu/libevent-2.1.so.6 (0x00007f20261de000)
libhogweed.so.4 => /usr/lib/x86_64-linux-gnu/libhogweed.so.4 (0x00007f2025faa000)
libnettle.so.6 => /usr/lib/x86_64-linux-gnu/libnettle.so.6 (0x00007f2025d74000)
libgmp.so.10 => /usr/lib/x86_64-linux-gnu/libgmp.so.10 (0x00007f2025af3000)
libicudata.so.60 => /usr/lib/x86_64-linux-gnu/libicudata.so.60 (0x00007f2023f4a000)
```
**Systemd unit**:
```
[Unit]
Description=Monero Daemon
After=network.target

[Service]
Type=forking
GuessMainPID=no
ExecStart=/usr/local/src/monero/build/Linux/_HEAD_detached_at_v0.15.0.0_/release/bin/monerod --detach --config-file /etc/monero/monero.conf
Restart=always
User=monero

[Install]
WantedBy=multi-user.target
```
**Config file**:
```
block-notify=/usr/bin/curl http://127.0.0.1:19091/newblock/monero/%s
rpc-bind-ip=0.0.0.0
restricted-rpc=1
confirm-external-bind=1
log-file=/var/log/monero/monero.log
```

* **Step 1**: Running v15 with existing v14 database
Result: *"src/blockchain_db/lmdb/db_lmdb.cpp:459	LMDB map resize detected."* for half an hour with two cores at full load. Stopping service. Running again. *"Error opening database: Failed to open lmdb environment: MDB_INVALID: File is not an LMDB file"*
Logfile: https://share.hashvault.pro/monero/v14tov15.log.gz

* **Step 2**: Recovering db from the backup, setting --debug-level 4.
Result: Visually normal operation 
Logfile: https://share.hashvault.pro/monero/v14tov15-debug.log.gz

* **Step 3**: Stopping service, removing --debug-level 4.
Result: *"Error opening database: Failed to open lmdb environment: MDB_INVALID: File is not an LMDB file"*
Logfile: https://share.hashvault.pro/monero/v15-after-debug.log.gz

* **Step 4**: Recovering db from the backup, running v15 directly in console without systemd under the monero user (``/usr/local/src/monero/build/Linux/_HEAD_detached_at_v0.15.0.0_/release/bin/monerod --rpc-bind-ip 0.0.0.0 --restricted-rpc --confirm-external-bind --log-file /var/log/monero/monero.log``)
Result: Normal operation
Logfile: https://share.hashvault.pro/monero/v15-console.log.gz

* **Step 5**: Running under systemd with database from step 4
Result: Normal operation
* **Step 5.1**: Restart service
Result: *"Error opening database: Failed to open lmdb environment: MDB_INVALID: File is not an LMDB file, Error attempting to retrieve a cumulative difficulty from the db"*
Logfile: https://share.hashvault.pro/monero/v15-service.log.gz

* **Step 6.1**: Running monero from scratch
Result: *"Error attempting to retrieve a block hash from the db: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid"*
Logfile: https://share.hashvault.pro/monero/v15-blank.log.gz

* **Step 6.2**: Running monero from scratch with debug
Result: *"MDB_CORRUPTED: Located page was wrong type"*
Logfile: https://share.hashvault.pro/monero/v15-blank-debug.log.gz

* **Step 7.1**: Running monero testnet from scratch with debug
Result: *"Error adding block with hash: <5a1125384b088dbeaaa6f61c39db0318e53732ffc927978a52e3b16553203138> to blockchain, what = Error checking if tx index exists for tx hash 5c877a194499c31dd5819a1d9f9ea85120b3ab5987dd4459de03794fe535bbe9: MDB_CORRUPTED: Located page was wrong type"*, but after starts syncing
* **Step 7.2**: Restart service
Result: *"Error adding block with hash: <5a1125384b088dbeaaa6f61c39db0318e53732ffc927978a52e3b16553203138> to blockchain, what = Error checking if tx index exists for tx hash 5c877a194499c31dd5819a1d9f9ea85120b3ab5987dd4459de03794fe535bbe9: MDB_CORRUPTED: Located page was wrong type"*, but after starts syncing
Logfile: https://share.hashvault.pro/monero/v15-blank-testnet.log.gz

* **Step 8**: Running monero testnet with database from step 6.2 without debug
Result: *"Error adding block with hash: <5a1125384b088dbeaaa6f61c39db0318e53732ffc927978a52e3b16553203138> to blockchain, what = Error checking if tx index exists for tx hash 5c877a194499c31dd5819a1d9f9ea85120b3ab5987dd4459de03794fe535bbe9: MDB_CORRUPTED: Located page was wrong type"*, loops and doesn't sync after
Logfile: https://share.hashvault.pro/monero/v15-testnet.log.gz

**Side notes**: Also reproducible with clean 18.04 install, monero v0.15 release binaries, wownero v0.7.0

# Discussion History
## hyc | 2019-11-17T11:35:50+00:00
We've shown conclusively that the corruption is caused by errant writes to file descriptor 2, which would ordinarily be stderr, but when monerod is daemonized, is instead pointed to the blockchain's data.mdb. These writes aren't happening in the monerod process itself, but are caused when monerod spawns some other process (such as for a block-notify invocation) since the child process inherits monerod's fds [012]. 

The obvious fix is in daemonizer/posix_fork.cpp; we should open /dev/null for [012] instead of simply leaving [12] closed.

# Action History
- Created by: HashVault | 2019-11-16T11:42:17+00:00
- Closed at: 2019-11-18T19:25:21+00:00
