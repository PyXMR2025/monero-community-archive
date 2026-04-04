---
title: monerod just quits at start
source_url: https://github.com/monero-project/monero/issues/9255
author: l29ah
assignees: []
labels:
- database
- reproduction needed
- more info needed
created_at: '2024-03-17T14:59:24+00:00'
updated_at: '2025-12-19T14:52:38+00:00'
type: issue
status: closed
closed_at: '2025-12-19T14:52:38+00:00'
---

# Original Description
The log output doesn't look interesting, nothing in dmesg too:
```
2024-03-17 14:57:00.532	    7ff3503222c0	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2024-03-17 14:57:00.532	    7ff3503222c0	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:INFO,global:INFO,stacktrace:INFO,logging:INFO,msgwriter:INFO,perf.*:DEBUG
2024-03-17 14:57:00.532	    7ff3503222c0	INFO	global	src/daemon/main.cpp:309	Monero 'Fluorine Fermi' (v0.18.3.3-unknown)
2024-03-17 14:57:00.532	    7ff3503222c0	INFO	daemon	src/daemon/main.cpp:371	Moving from main() into the daemonize now.
2024-03-17 14:57:00.532	    7ff3503222c0	INFO	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2024-03-17 14:57:00.532	    7ff3503222c0	INFO	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2024-03-17 14:57:00.533	    7ff3503222c0	INFO	global	src/daemon/core.h:64	Initializing core...
2024-03-17 14:57:00.533	    7ff3503222c0	INFO	global	src/cryptonote_core/cryptonote_core.cpp:523	Loading blockchain from folder /var/lib/monero/lmdb ...
2024-03-17 14:57:00.557	    7ff3503222c0	INFO	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:3876	batch transaction mode already enabled, but asked to enable batch mode
2024-03-17 14:57:00.557	    7ff3503222c0	INFO	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:3879	batch transactions enabled
2024-03-17 14:57:00.560	    7ff3503222c0	INFO	blockchain	src/cryptonote_core/blockchain.cpp:5565	Loading precomputed blocks (387844 bytes)
2024-03-17 14:57:00.562	    7ff3503222c0	INFO	blockchain	src/cryptonote_core/blockchain.cpp:5575	precomputed blocks hash: <0046a0019beb6e697e27d834d6127851425f7ee09bfb8e9f8df7b1420131aca8>, expected 0046a0019beb6e697e27d834d6127851425f7ee09bfb8e9f8df7b1420131aca8
2024-03-17 14:57:00.609	    7ff3503222c0	INFO	blockchain	src/cryptonote_core/blockchain.cpp:5619	6060 block hashes loaded
```

Tried `log-level=3`, the tail of the log looks like this:
```
2024-03-17 14:55:13.630	    7f3eb9b1f2c0	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:3831	batch transaction: committing...
2024-03-17 14:55:13.630	    7f3eb9b1f2c0	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:382	mdb_txn_safe: destructor
2024-03-17 14:55:13.630	    7f3eb9b1f2c0	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:3845	batch transaction: end
2024-03-17 14:55:13.630	    7f3eb9b1f2c0	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:3916	BlockchainLMDB::block_rtxn_start
2024-03-17 14:55:13.630	    7f3eb9b1f2c0	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:382	mdb_txn_safe: destructor
2024-03-17 14:55:13.630	    7f3eb9b1f2c0	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2557	BlockchainLMDB::get_top_block_timestamp
2024-03-17 14:55:13.630	    7f3eb9b1f2c0	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2918	BlockchainLMDB::height
2024-03-17 14:55:13.630	    7f3eb9b1f2c0	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2472	BlockchainLMDB::get_block_timestamp
2024-03-17 14:55:13.630	    7f3eb9b1f2c0	INFO	blockchain	src/cryptonote_core/blockchain.cpp:5565	Loading precomputed blocks (387844 bytes)
2024-03-17 14:55:13.632	    7f3eb9b1f2c0	INFO	blockchain	src/cryptonote_core/blockchain.cpp:5575	precomputed blocks hash: <0046a0019beb6e697e27d834d6127851425f7ee09bfb8e9f8df7b1420131aca8>, expected 0046a0019beb6e697e27d834d6127851425f7ee09bfb8e9f8df7b1420131aca8
2024-03-17 14:55:13.632	    7f3eb9b1f2c0	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2918	BlockchainLMDB::height
2024-03-17 14:55:13.679	    7f3eb9b1f2c0	INFO	blockchain	src/cryptonote_core/blockchain.cpp:5619	6060 block hashes loaded
2024-03-17 14:55:13.679	    7f3eb9b1f2c0	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1786	BlockchainLMDB::get_txpool_tx_count
2024-03-17 14:55:13.679	    7f3eb9b1f2c0	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2286	BlockchainLMDB::for_all_txpool_txes
```
I have no idea what's going on. Used to work fine.

# Discussion History
## selsta | 2024-03-17T15:01:24+00:00
Can you share the full logs of starting with log level 2? What you shared seems incomplete.

Please also try to start without any config or startup options.

## l29ah | 2024-03-17T15:03:46+00:00
> Can you share the full logs of starting with log level 2? What you shared seems incomplete.
> 
> Please also try to start without any config.

The output with only the following config contents:
```
data-dir=/var/lib/monero
log-file=/var/log/monero/monero.log
log-level=2
```

```
2024-03-17 15:02:22.942	    7fe8298892c0	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2024-03-17 15:02:22.942	    7fe8298892c0	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:DEBUG
2024-03-17 15:02:22.943	    7fe8298892c0	INFO	global	src/daemon/main.cpp:309	Monero 'Fluorine Fermi' (v0.18.3.3-unknown)
2024-03-17 15:02:22.943	    7fe8298892c0	INFO	daemon	src/daemon/main.cpp:371	Moving from main() into the daemonize now.
2024-03-17 15:02:22.943	    7fe8298892c0	INFO	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2024-03-17 15:02:22.943	    7fe8298892c0	INFO	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2024-03-17 15:02:22.944	    7fe8298892c0	INFO	global	src/daemon/core.h:64	Initializing core...
2024-03-17 15:02:22.944	    7fe8298892c0	INFO	global	src/cryptonote_core/cryptonote_core.cpp:523	Loading blockchain from folder /var/lib/monero/lmdb ...
2024-03-17 15:02:22.944	    7fe8298892c0	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:551	option: fast
2024-03-17 15:02:22.944	    7fe8298892c0	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:551	option: async
2024-03-17 15:02:22.944	    7fe8298892c0	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:551	option: 250000000bytes
2024-03-17 15:02:22.944	    7fe8298892c0	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:636	DB map size:     212837601280
2024-03-17 15:02:22.944	    7fe8298892c0	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:637	Space used:      190785708032
2024-03-17 15:02:22.944	    7fe8298892c0	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:638	Space remaining: 22051893248
2024-03-17 15:02:22.945	    7fe8298892c0	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:639	Size threshold:  0
2024-03-17 15:02:22.945	    7fe8298892c0	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:641	Percent used: 89.6391  Percent threshold: 90.0000
2024-03-17 15:02:22.945	    7fe8298892c0	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1482	Setting m_height to: 3091705
2024-03-17 15:02:22.968	    7fe8298892c0	DEBUG	hardfork	src/cryptonote_basic/hardfork.cpp:189init done
2024-03-17 15:02:22.968	    7fe8298892c0	INFO	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:3876	batch transaction mode already enabled, but asked to enable batch mode
2024-03-17 15:02:22.968	    7fe8298892c0	INFO	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:3879	batch transactions enabled
2024-03-17 15:02:22.969	    7fe8298892c0	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:636	DB map size:     212837601280
2024-03-17 15:02:22.969	    7fe8298892c0	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:637	Space used:      190785708032
2024-03-17 15:02:22.969	    7fe8298892c0	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:638	Space remaining: 22051893248
2024-03-17 15:02:22.969	    7fe8298892c0	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:639	Size threshold:  0
2024-03-17 15:02:22.969	    7fe8298892c0	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:641	Percent used: 89.6391  Percent threshold: 90.0000
2024-03-17 15:02:22.972	    7fe8298892c0	INFO	blockchain	src/cryptonote_core/blockchain.cpp:5565	Loading precomputed blocks (387844 bytes)
2024-03-17 15:02:22.974	    7fe8298892c0	INFO	blockchain	src/cryptonote_core/blockchain.cpp:5575	precomputed blocks hash: <0046a0019beb6e697e27d834d6127851425f7ee09bfb8e9f8df7b1420131aca8>, expected 0046a0019beb6e697e27d834d6127851425f7ee09bfb8e9f8df7b1420131aca8
2024-03-17 15:02:23.021	    7fe8298892c0	INFO	blockchain	src/cryptonote_core/blockchain.cpp:5619	6060 block hashes loaded
```

## selsta | 2024-03-17T15:07:29+00:00
Can you start it from command line like this to see if it segfaults? Please share the logs from the command line output and not the log file.

`./monerod --data-dir /path/to --log-level 2`

## l29ah | 2024-03-17T15:15:43+00:00
> Can you start it from command line like this to see if it segfaults? Please share the logs from the command line output and not the log file.
> 
> `./monerod --data-dir /path/to --log-level 2`

It says `Bus error` at the end. Tried to run it with gdb, but it doesn't look nice without symbols, tell me if you need them:
```
(gdb) bt
#0  0x0000555555912a53 in ?? ()
#1  0x000055555591fc17 in ?? ()
#2  0x0000555555c4830e in ?? ()
#3  0x0000555555a91105 in ?? ()
#4  0x0000555555bae6ec in ?? ()
#5  0x0000555555a1af25 in ?? ()
#6  0x0000555555a90f70 in ?? ()
#7  0x0000555555a3a3bb in ?? ()
#8  0x0000555555a50f8d in ?? ()
#9  0x0000555555a6bd68 in ?? ()
#10 0x000055555569eefa in ?? ()
#11 0x00005555556fc310 in ?? ()
#12 0x000055555567432f in ?? ()
#13 0x00005555556fd758 in ?? ()
#14 0x000055555563b61d in ?? ()
#15 0x00007ffff7049090 in __libc_start_call_main () from /lib64/libc.so.6
#16 0x00007ffff7049149 in __libc_start_main_impl () from /lib64/libc.so.6
#17 0x00005555556445c5 in ?? ()
```

## selsta | 2024-03-17T15:17:57+00:00
I would guess it's a corrupt database. Do you remember what happened the last time it worked? Did you have a power outage? Did you force shutdown monerod during sync?

## l29ah | 2024-03-17T15:19:29+00:00
I had a couple of power outages, yes. Not sure if monerod stopped working after one of these, since i don't monitor it.

## selsta | 2024-03-17T15:20:37+00:00
If you have regular power outages I would recommend to keep a backup of the blockchain.

## ChecksumDev | 2024-04-08T21:33:01+00:00
I am having segmentation faults with the application, I've tried resyncing the database three times now but I'm still having this issue, it might be related. Using Arch Linux on Kernel 6.8.4-zen1-1-zen

It's never gotten to the point of being online and the system should absolutely have enough RAM.
I've tried the DB Salvage parameters as well, no power outages.

```
2024-04-08 21:27:52.015 I Monero 'Fluorine Fermi' (v0.18.3.3-release)
2024-04-08 21:27:52.015 I Moving from main() into the daemonize now.
2024-04-08 21:27:52.015 I Initializing cryptonote protocol...
2024-04-08 21:27:52.015 I Cryptonote protocol initialized OK
2024-04-08 21:27:52.015 I Initializing core...
2024-04-08 21:27:52.015 I Loading blockchain from folder /home/checksum/.bitmonero/lmdb ...
2024-04-08 21:27:52.015 D option: fast
2024-04-08 21:27:52.015 D option: async
2024-04-08 21:27:52.015 D option: 250000000bytes
2024-04-08 21:27:52.016 D DB map size:     164775038976
2024-04-08 21:27:52.016 D Space used:      148520964096
2024-04-08 21:27:52.016 D Space remaining: 16254074880
2024-04-08 21:27:52.016 D Size threshold:  0
2024-04-08 21:27:52.016 D Percent used: 90.1356  Percent threshold: 90.0000
2024-04-08 21:27:52.016 I Threshold met (percent-based)
2024-04-08 21:27:52.016 W LMDB memory map needs to be resized, doing that now.
2024-04-08 21:27:52.016 I LMDB Mapsize increased.  Old: 157141MiB, New: 158165MiB
2024-04-08 21:27:52.016 D Setting m_height to: 2695748
[1]    5906 segmentation fault (core dumped)  monerod --log-level 2
(base) ➜  ~
```

Log:

```
cat .bitmonero/bitmonero.log
2024-04-08 21:30:19.846     74a821a3fc00        INFO    logging contrib/epee/src/mlog.cpp:273   New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2024-04-08 21:30:19.846     74a821a3fc00        INFO    logging contrib/epee/src/mlog.cpp:273   New log categories: *:DEBUG
2024-04-08 21:30:19.846     74a821a3fc00        INFO    global  src/daemon/main.cpp:309 Monero 'Fluorine Fermi' (v0.18.3.3-release)
2024-04-08 21:30:19.846     74a821a3fc00        INFO    daemon  src/daemon/main.cpp:371 Moving from main() into the daemonize now.
2024-04-08 21:30:19.846     74a821a3fc00        INFO    global  src/daemon/protocol.h:53        Initializing cryptonote protocol...
2024-04-08 21:30:19.846     74a821a3fc00        INFO    global  src/daemon/protocol.h:58        Cryptonote protocol initialized OK
2024-04-08 21:30:19.847     74a821a3fc00        INFO    global  src/daemon/core.h:64    Initializing core...
2024-04-08 21:30:19.847     74a821a3fc00        INFO    global  src/cryptonote_core/cryptonote_core.cpp:523     Loading blockchain from folder /home/checksum/.bitmonero/lmdb ...
2024-04-08 21:30:19.847     74a821a3fc00        DEBUG   cn      src/cryptonote_core/cryptonote_core.cpp:551     option: fast
2024-04-08 21:30:19.847     74a821a3fc00        DEBUG   cn      src/cryptonote_core/cryptonote_core.cpp:551     option: async
2024-04-08 21:30:19.847     74a821a3fc00        DEBUG   cn      src/cryptonote_core/cryptonote_core.cpp:551     option: 250000000bytes
2024-04-08 21:30:19.847     74a821a3fc00        DEBUG   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:636  DB map size:     164775038976
2024-04-08 21:30:19.847     74a821a3fc00        DEBUG   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:637  Space used:      148520964096
2024-04-08 21:30:19.847     74a821a3fc00        DEBUG   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:638  Space remaining: 16254074880
2024-04-08 21:30:19.847     74a821a3fc00        DEBUG   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:639  Size threshold:  0
2024-04-08 21:30:19.847     74a821a3fc00        DEBUG   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:641  Percent used: 90.1356  Percent threshold: 90.0000
2024-04-08 21:30:19.847     74a821a3fc00        INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:656  Threshold met (percent-based)
2024-04-08 21:30:19.847     74a821a3fc00        WARNING blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1405 LMDB memory map needs to be resized, doing that now.
2024-04-08 21:30:19.847     74a821a3fc00        INFO    global  src/blockchain_db/lmdb/db_lmdb.cpp:612  LMDB Mapsize increased.  Old: 157141MiB, New: 158165MiB
2024-04-08 21:30:19.847     74a821a3fc00        DEBUG   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1482 Setting m_height to: 2695748
```

If I'm missing anything I can provide it ^^

## selsta | 2024-04-09T13:22:16+00:00
@ChecksumDev what kind of hardware do you have?

## ChecksumDev | 2024-04-09T13:42:10+00:00
> @ChecksumDev what kind of hardware do you have?

I'm running:
**CPU**: AMD Ryzen 7 5800X3D
**GPU**: NVIDIA GeForce RTX 3070
**RAM**: 96 GB
**Storage**: Samsung SSD 970 EVO Plus 2TB

## selsta | 2024-04-09T13:46:05+00:00
@ChecksumDev can you also your config file? also how did you install monero? from package manager or getmonero website?

## ChecksumDev | 2024-04-09T13:50:04+00:00
I assume you mean this file:
```
# Configuration for monerod
# Syntax: any command line option may be specified as 'clioptionname=value'.
#         Boolean options such as 'no-igd' are specified as 'no-igd=1'.
# See 'monerod --help' for all available options.

data-dir=/var/lib/monero
log-file=/var/log/monero/monero.log
log-level=2
```

I installed monerod from the pacman extra repository.
![image](https://github.com/monero-project/monero/assets/24845326/5268cf3e-dc50-4d31-b42d-d85051f4a7e6)


## selsta | 2024-04-09T13:55:18+00:00
Can you try the monerod binary from https://www.getmonero.org/downloads/ to rule out it's related to how the package manager built monerod?

Also can you rule out unstable hardware, e.g. overclocking?

## ChecksumDev | 2024-04-09T14:02:16+00:00
No unstable hardware, relatively new. I don't think any components in the system are more than three years old, not overclocking.

I honestly expected the binary to work so now I'm a little more puzzled.

## ChecksumDev | 2024-04-09T14:02:24+00:00
![image](https://github.com/monero-project/monero/assets/24845326/73093bca-5da3-469f-ae2c-c4a9622acbc2)
Sorry that sent early for some reason

## ChecksumDev | 2024-04-09T14:04:29+00:00
dmesg output in case that's helpful:
```
[16817.046876] monerod[4894]: segfault at 56fe0d3d7860 ip 00007703a257548c sp 00007fffdcb81c88 error 4 in libc.so.6[7703a2442000+15b000] likely on CPU 0 (core 0, socket 0)
[16817.046890] Code: c5 7e 7f 02 c5 fe 7f 01 c5 f8 77 c3 66 90 48 85 c9 74 f5 c5 fe 6f 6e 20 c5 fe 6f 76 40 48 8d 8c 17 7f ff ff ff c5 fe 6f 7e 60 <c5> 7e 6f 44 16 e0 48 29 fe 48 83 e1 e0 48 01 ce 0f 1f 40 00 c5 fe
[16831.143693] monerod[4910]: segfault at 55ecc1cb5520 ip 00007875fe37548c sp 00007ffff3f29478 error 4 in libc.so.6[7875fe242000+15b000] likely on CPU 15 (core 7, socket 0)
[16831.143702] Code: c5 7e 7f 02 c5 fe 7f 01 c5 f8 77 c3 66 90 48 85 c9 74 f5 c5 fe 6f 6e 20 c5 fe 6f 76 40 48 8d 8c 17 7f ff ff ff c5 fe 6f 7e 60 <c5> 7e 6f 44 16 e0 48 29 fe 48 83 e1 e0 48 01 ce 0f 1f 40 00 c5 fe
[16832.360437] monerod[4924]: segfault at 633da043af00 ip 000079bd27f7548c sp 00007fff9e611fa8 error 4 in libc.so.6[79bd27e42000+15b000] likely on CPU 8 (core 0, socket 0)
[16832.360450] Code: c5 7e 7f 02 c5 fe 7f 01 c5 f8 77 c3 66 90 48 85 c9 74 f5 c5 fe 6f 6e 20 c5 fe 6f 76 40 48 8d 8c 17 7f ff ff ff c5 fe 6f 7e 60 <c5> 7e 6f 44 16 e0 48 29 fe 48 83 e1 e0 48 01 ce 0f 1f 40 00 c5 fe
[16833.607700] monerod[4938]: segfault at 5c42465d4520 ip 00007751f957548c sp 00007ffc5b1920c8 error 4 in libc.so.6[7751f9442000+15b000] likely on CPU 0 (core 0, socket 0)
[16833.607712] Code: c5 7e 7f 02 c5 fe 7f 01 c5 f8 77 c3 66 90 48 85 c9 74 f5 c5 fe 6f 6e 20 c5 fe 6f 76 40 48 8d 8c 17 7f ff ff ff c5 fe 6f 7e 60 <c5> 7e 6f 44 16 e0 48 29 fe 48 83 e1 e0 48 01 ce 0f 1f 40 00 c5 fe
[16835.360952] monerod[4951]: segfault at 5b46d0ec4910 ip 000077ba6b57548c sp 00007fffbc229b28 error 4 in libc.so.6[77ba6b442000+15b000] likely on CPU 15 (core 7, socket 0)
[16835.360963] Code: c5 7e 7f 02 c5 fe 7f 01 c5 f8 77 c3 66 90 48 85 c9 74 f5 c5 fe 6f 6e 20 c5 fe 6f 76 40 48 8d 8c 17 7f ff ff ff c5 fe 6f 7e 60 <c5> 7e 6f 44 16 e0 48 29 fe 48 83 e1 e0 48 01 ce 0f 1f 40 00 c5 fe
[16837.912389] monerod[4963]: segfault at 59b82d5f5860 ip 000078b07bb7548c sp 00007fff5425ffa8 error 4 in libc.so.6[78b07ba42000+15b000] likely on CPU 0 (core 0, socket 0)
[16837.912401] Code: c5 7e 7f 02 c5 fe 7f 01 c5 f8 77 c3 66 90 48 85 c9 74 f5 c5 fe 6f 6e 20 c5 fe 6f 76 40 48 8d 8c 17 7f ff ff ff c5 fe 6f 7e 60 <c5> 7e 6f 44 16 e0 48 29 fe 48 83 e1 e0 48 01 ce 0f 1f 40 00 c5 fe
[16889.907710] systemd-fstab-generator[5141]: Mount point  is not a valid path, ignoring.
[17094.139389] monerod[5747]: segfault at 5fbe14836860 ip 000074fe3957548c sp 00007ffc6643d288 error 4 in libc.so.6[74fe39442000+15b000] likely on CPU 0 (core 0, socket 0)
[17094.139398] Code: c5 7e 7f 02 c5 fe 7f 01 c5 f8 77 c3 66 90 48 85 c9 74 f5 c5 fe 6f 6e 20 c5 fe 6f 76 40 48 8d 8c 17 7f ff ff ff c5 fe 6f 7e 60 <c5> 7e 6f 44 16 e0 48 29 fe 48 83 e1 e0 48 01 ce 0f 1f 40 00 c5 fe
[17146.780436] monerod[5777]: segfault at 5bf97f12a860 ip 00007de29cd7548c sp 00007ffd291d9bb8 error 4 in libc.so.6[7de29cc42000+15b000] likely on CPU 7 (core 7, socket 0)
[17146.780446] Code: c5 7e 7f 02 c5 fe 7f 01 c5 f8 77 c3 66 90 48 85 c9 74 f5 c5 fe 6f 6e 20 c5 fe 6f 76 40 48 8d 8c 17 7f ff ff ff c5 fe 6f 7e 60 <c5> 7e 6f 44 16 e0 48 29 fe 48 83 e1 e0 48 01 ce 0f 1f 40 00 c5 fe
[17152.053986] monerod[5789]: segfault at 56899d3c5480 ip 000074f41897548c sp 00007ffd22de97a8 error 4 in libc.so.6[74f418842000+15b000] likely on CPU 15 (core 7, socket 0)
[17152.053999] Code: c5 7e 7f 02 c5 fe 7f 01 c5 f8 77 c3 66 90 48 85 c9 74 f5 c5 fe 6f 6e 20 c5 fe 6f 76 40 48 8d 8c 17 7f ff ff ff c5 fe 6f 7e 60 <c5> 7e 6f 44 16 e0 48 29 fe 48 83 e1 e0 48 01 ce 0f 1f 40 00 c5 fe
[17153.964614] monerod[5801]: segfault at 610629025860 ip 00007bcdca17548c sp 00007ffc5e9152a8 error 4 in libc.so.6[7bcdca042000+15b000] likely on CPU 0 (core 0, socket 0)
[17153.964624] Code: c5 7e 7f 02 c5 fe 7f 01 c5 f8 77 c3 66 90 48 85 c9 74 f5 c5 fe 6f 6e 20 c5 fe 6f 76 40 48 8d 8c 17 7f ff ff ff c5 fe 6f 7e 60 <c5> 7e 6f 44 16 e0 48 29 fe 48 83 e1 e0 48 01 ce 0f 1f 40 00 c5 fe
[17314.006277] monerod[5906]: segfault at 5e985fc73860 ip 00007863e0d7548c sp 00007fffc7c1fd08 error 4 in libc.so.6[7863e0c42000+15b000] likely on CPU 0 (core 0, socket 0)
[17314.006286] Code: c5 7e 7f 02 c5 fe 7f 01 c5 f8 77 c3 66 90 48 85 c9 74 f5 c5 fe 6f 6e 20 c5 fe 6f 76 40 48 8d 8c 17 7f ff ff ff c5 fe 6f 7e 60 <c5> 7e 6f 44 16 e0 48 29 fe 48 83 e1 e0 48 01 ce 0f 1f 40 00 c5 fe
[17461.840388] monerod[5974]: segfault at 5d543715e860 ip 000074a82237548c sp 00007ffe8a7e0ab8 error 4 in libc.so.6[74a822242000+15b000] likely on CPU 0 (core 0, socket 0)
[17461.840399] Code: c5 7e 7f 02 c5 fe 7f 01 c5 f8 77 c3 66 90 48 85 c9 74 f5 c5 fe 6f 6e 20 c5 fe 6f 76 40 48 8d 8c 17 7f ff ff ff c5 fe 6f 7e 60 <c5> 7e 6f 44 16 e0 48 29 fe 48 83 e1 e0 48 01 ce 0f 1f 40 00 c5 fe
[76107.522481] monerod[11811]: segfault at 5b9c209c4480 ip 0000723acbf7548c sp 00007ffc414a7c08 error 4 in libc.so.6[723acbe42000+15b000] likely on CPU 2 (core 2, socket 0)
[76107.522492] Code: c5 7e 7f 02 c5 fe 7f 01 c5 f8 77 c3 66 90 48 85 c9 74 f5 c5 fe 6f 6e 20 c5 fe 6f 76 40 48 8d 8c 17 7f ff ff ff c5 fe 6f 7e 60 <c5> 7e 6f 44 16 e0 48 29 fe 48 83 e1 e0 48 01 ce 0f 1f 40 00 c5 fe
[76855.236763] monerod[11977]: segfault at 0 ip 00005b2248d6a29c sp 00007ffe2b9713a0 error 4 in monerod[5b2248600000+11bd000] likely on CPU 0 (core 0, socket 0)
[76855.236775] Code: 4c 89 ea e8 16 b0 ff ff 85 c0 41 89 c6 75 a2 49 8b 44 24 18 41 8b 74 24 20 41 0f b7 5c 24 42 48 8b 40 68 48 8d 4b 08 48 89 da <48> 8b 04 f0 49 8b 7c cc 08 48 85 c0 0f 84 07 fc ff ff 41 f6 44 24
[77046.755068] monerod[12040]: segfault at 59ff3af10480 ip 00007b74a457548c sp 00007ffcc8f8cef8 error 4 in libc.so.6[7b74a4442000+15b000] likely on CPU 0 (core 0, socket 0)
[77046.755078] Code: c5 7e 7f 02 c5 fe 7f 01 c5 f8 77 c3 66 90 48 85 c9 74 f5 c5 fe 6f 6e 20 c5 fe 6f 76 40 48 8d 8c 17 7f ff ff ff c5 fe 6f 7e 60 <c5> 7e 6f 44 16 e0 48 29 fe 48 83 e1 e0 48 01 ce 0f 1f 40 00 c5 fe
[77054.307107] monerod[12058]: segfault at 634ff17c8480 ip 0000726070d7548c sp 00007ffd82c7c528 error 4 in libc.so.6[726070c42000+15b000] likely on CPU 0 (core 0, socket 0)
[77054.307116] Code: c5 7e 7f 02 c5 fe 7f 01 c5 f8 77 c3 66 90 48 85 c9 74 f5 c5 fe 6f 6e 20 c5 fe 6f 76 40 48 8d 8c 17 7f ff ff ff c5 fe 6f 7e 60 <c5> 7e 6f 44 16 e0 48 29 fe 48 83 e1 e0 48 01 ce 0f 1f 40 00 c5 fe

```

## selsta | 2024-04-09T14:47:44+00:00
> I honestly expected the binary to work so now I'm a little more puzzled.

I don't know how they are compiling monero, that's why it would be good to try the getmonero.org binary in an attempt to isolate the issue.

Also where is your blockchain stored? Local ssd? Local hdd? Network drive?

## ChecksumDev | 2024-04-09T18:32:36+00:00
Local NVME, I did try it from getmonero too. see IMG.

## selsta | 2024-04-09T22:48:29+00:00
> I've tried resyncing the database three times now but I'm still having this issue, it might be related

Does it always happen around the same block height when you delete the blockchain and resync? If yes, which block?

## ChecksumDev | 2024-04-10T00:27:11+00:00
It seems like the same block every time if I estimated the time it took to crash, though I couldn't find logs going back that to the previous sync, another resync would take a while.

```
2024-04-08 16:20:52.811 [P2P2]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1696    Synced 2695188/3122962 (86%, 427774 left)
2024-04-08 16:20:53.128 [P2P2]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1696    Synced 2695208/3122962 (86%, 427754 left)
2024-04-08 16:20:53.568 [P2P2]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1696    Synced 2695228/3122962 (86%, 427734 left)
2024-04-08 16:20:54.229 [P2P2]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1696    Synced 2695248/3122962 (86%, 427714 left)
2024-04-08 16:20:54.667 [P2P2]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1696    Synced 2695268/3122962 (86%, 427694 left)
2024-04-08 16:20:55.174 [P2P2]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1696    Synced 2695288/3122962 (86%, 427674 left)
2024-04-08 16:21:25.813     77b204cdec00        INFO    logging contrib/epee/src/mlog.cpp:273   New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2024-04-08 16:21:25.813     77b204cdec00        INFO    global  src/daemon/main.cpp:309 Monero 'Fluorine Fermi' (v0.18.3.3-release)
2024-04-08 16:21:25.814     77b204cdec00        INFO    global  src/daemon/protocol.h:53        Initializing cryptonote protocol...
2024-04-08 16:21:25.814     77b204cdec00        INFO    global  src/daemon/protocol.h:58        Cryptonote protocol initialized OK
2024-04-08 16:21:25.815     77b204cdec00        INFO    global  src/daemon/core.h:64    Initializing core...
2024-04-08 16:21:25.815     77b204cdec00        INFO    global  src/cryptonote_core/cryptonote_core.cpp:523     Loading blockchain from folder /home/checksum/.bitmonero/lmdb ...
2024-04-08 16:21:25.816     77b204cdec00        WARNING blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1405 LMDB memory map needs to be resized, doing that now.
2024-04-08 16:21:25.816     77b204cdec00        INFO    global  src/blockchain_db/lmdb/db_lmdb.cpp:612  LMDB Mapsize increased.  Old: 157141MiB, New: 158165MiB
2024-04-08 16:21:27.111     7fedebec1c00        INFO    logging contrib/epee/src/mlog.cpp:273   New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2024-04-08 16:21:27.112     7fedebec1c00        INFO    global  src/daemon/main.cpp:309 Monero 'Fluorine Fermi' (v0.18.3.3-release)
2024-04-08 16:21:27.112     7fedebec1c00        INFO    global  src/daemon/protocol.h:53        Initializing cryptonote protocol...
2024-04-08 16:21:27.112     7fedebec1c00        INFO    global  src/daemon/protocol.h:58        Cryptonote protocol initialized OK
2024-04-08 16:21:27.112     7fedebec1c00        INFO    global  src/daemon/core.h:64    Initializing core...
```

## pe-yahniukov | 2024-05-09T11:08:09+00:00
Had the same issue after power outage. Unfortunately, daemon started working only after removing of data.lmdb database. Synchronization started from the beginning (sadly). Seems LMDB is not protected from power outage. But even so, monerod doesn't properly handle corrupted database data and that's bad. Maybe it could try to reverse or just remove some last entries.

Below is a OpenLDAP discussion about LMDB behavior during power outage.
https://lists.openldap.org/hyperkitty/list/openldap-technical@openldap.org/thread/GEQ3B3QBSLIWXNWMTJROULWUYVLRHGKH/

But at the same time I saw plenty of sources that claim LMDB engine is protected from this.

Important information: I observed this on the computer with HDD, not SSD.

**UPDATE**
Just for curiosity I've tried to unplug the computer from the power source 3 times during monerod synchronization. After boot-up monerod fails to start every time with the following possible observed errors:

- Segmentation fault (kernel error)
- Bus error (kernel error)
- The current version is not compatible with database (monerod error)

## ross-rosario | 2024-10-04T13:27:04+00:00
Same issue here, corrupted db due to power outage. Can't Monerod handle this a little more gracefully? Re-syncing from the beginning is a huge pain in the rear.

## selsta | 2024-12-13T23:48:41+00:00
If `monerod` is fully synced, the database should not corrupt on power outage. If it is during the initial sync phase, it can corrupt because we use a faster sync mode. That can be manually overriden with `--db-sync-mode safe`.

# Action History
- Created by: l29ah | 2024-03-17T14:59:24+00:00
- Closed at: 2025-12-19T14:52:38+00:00
