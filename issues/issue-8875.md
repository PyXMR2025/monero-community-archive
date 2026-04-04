---
title: stuck when synchronizing - corrupt DB ?
source_url: https://github.com/monero-project/monero/issues/8875
author: Gingeropolous
assignees: []
labels: []
created_at: '2023-05-24T17:13:02+00:00'
updated_at: '2023-12-10T05:26:08+00:00'
type: issue
status: closed
closed_at: '2023-06-17T13:34:32+00:00'
---

# Original Description
I've been trying to compare sync times between --fast-sync 0 and fast-sync 1, but can't seem to sync in a continuous run. 

I'm currently stuck at 

Height: 2199748/2199748 (100.0%) on mainnet, not mining, net hash 1.47 GH/s, v12 (next fork in 14.2 days), 12(out)+0(in) connections, uptime 1d 16h 39m 14s



```
user@login-node:~/.bitmonero$ grep ERROR * | head
bitmonero.log:2023-05-24 14:52:10.278	[P2P1]	WARNING	net.p2p	src/p2p/net_node.inl:1163	[72.204.109.84:20022 OUT] COMMAND_HANDSHAKE invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
bitmonero.log:2023-05-24 14:56:13.213	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: cryptonote::DB_ERROR
bitmonero.log:2023-05-24 14:56:13.214	[P2P9]	ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:1115	Exception at [core::handle_incoming_txs()], what=DB error attempting to fetch transaction index from hash 707b4aace81915876e5d0316217c91c6552cff1a8ff310d49d9dca0d08c0b2bf: MDB_CORRUPTED: Located page was wrong type
bitmonero.log:2023-05-24 14:56:13.214	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: cryptonote::DB_ERROR
bitmonero.log:2023-05-24 14:56:13.215	[P2P9]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:4726	Exception at [add_new_block], what=DB error attempting to fetch block index from hashMDB_BAD_TXN: Transaction must abort, has a child, or is invalid
bitmonero.log:2023-05-24 14:56:13.221	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1603	[115.70.236.197:18080 OUT] span connection id not found
bitmonero.log:2023-05-24 14:56:13.221	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: cryptonote::DB_ERROR
bitmonero.log:2023-05-24 14:56:13.221	[P2P9]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:4857	Exception in cleanup_handle_incoming_blocks: Failed to commit a transaction to the db: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
bitmonero.log:2023-05-24 14:56:16.556	[P2P9]	WARNING	net.p2p	src/p2p/net_node.inl:1163	[176.9.0.187:18080 OUT] COMMAND_HANDSHAKE invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
bitmonero.log:2023-05-24 14:56:16.737	[P2P2]	WARNING	net.p2p	src/p2p/net_node.inl:1163	[66.85.74.134:18080 OUT] COMMAND_HANDSHAKE invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
```

error logs mention DB_ERROR. Ima try and restart the daemon.

now i get this

Height: 2199748/2893016 (76.0%) on mainnet, not mining, net hash 1.47 GH/s, v12, 11(out)+0(in) connections, uptime 0d 0h 0m 24s

```
2023-05-24 17:12:20.454	[P2P1]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: cryptonote::DB_ERROR
2023-05-24 17:12:20.454	[P2P1]	ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:1115	Exception at [core::handle_incoming_txs()], what=DB error attempting to fetch transaction index from hash 707b4aace81915876e5d0316217c91c6552cff1a8ff310d49d9dca0d08c0b2bf: MDB_CORRUPTED: Located page was wrong type
2023-05-24 17:12:20.454	[P2P1]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: cryptonote::DB_ERROR
2023-05-24 17:12:20.454	[P2P1]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:4726	Exception at [add_new_block], what=DB error attempting to fetch block index from hashMDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-05-24 17:12:20.455	[P2P1]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1603	[95.111.233.106:18080 OUT] span connection id not found
2023-05-24 17:12:20.455	[P2P1]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: cryptonote::DB_ERROR
2023-05-24 17:12:20.455	[P2P1]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:4857	Exception in cleanup_handle_incoming_blocks: Failed to commit a transaction to the db: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
```

# Discussion History
## Gingeropolous | 2023-05-25T00:04:44+00:00
so as suggested by @selsta i tried syncing with --fast-sync=1 (the default) using the release binaries.

the daemon decided to stall out at 

```
Height: 2645004/2645004 (100.0%) on mainnet, not mining, net hash 2.93 GH/s, v14, 12(out)+0(in) connections, uptime 0d 5h 20m 1s
```

this showed up. I think its from this run

```
2023-05-24 23:32:45.993	[P2P4]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:4476	Error adding block with hash: <445f8cab5510b498afb0f78f8d5d6968a34d9d8d2107f432187d121a2a01d4af> to blockchain, what = Error adding spent key image to db transaction: MDB_PAGE_FULL: Internal error - page has no more space

```
@hyc , from my googling of MDB_PAGE_FULL , i should report this upstream. ?

i did a thread apply all bt as well for the lulz

https://termbin.com/dagw

## Gingeropolous | 2023-05-25T10:33:03+00:00
ok, definitely happened on the release binaries as well

2023-05-25 10:21:58.946	[P2P1]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:4476	Error adding block with hash: <445f8cab5510b498afb0f78f8d5d6968a34d9d8d2107f432187d121a2a01d4af> to blockchain, what = Error adding spent key image to db transaction: MDB_PAGE_FULL: Internal error - page has no more space


and it got stuck at the same height as before

Height: 2645004/2645004 (100.0%) on mainnet, not mining, net hash 2.93 GH/s, v14, 12(out)+0(in) connections, uptime 0d 15h 32m 47s

This box is a 5900x.

i tried on another box (a 3900x) , and it could sync fully with no errors.

## Gingeropolous | 2023-05-25T13:42:35+00:00
on the 5900x box, did memtest, got

``` 
 Bit Flip            : testing 473FAILURE: 0x800000000000000 != 0x804000000000000 at offset 0x332030e0.
```

im gonna keep running tests. While there might be a memory error, is it possible to make the software robust enough to account for the fact that users won't have 100% perfect hardware?

## selsta | 2023-05-25T13:45:17+00:00
> is it possible to make the software robust enough to account for the fact that users won't have 100% perfect hardware?

this isn't possible

## Gingeropolous | 2023-05-25T13:53:24+00:00
so monerod can only be run on ECC memory?

## selsta | 2023-05-25T14:05:51+00:00
Obviously you can do things like error correction and checksums, but hardware can be broken in various ways so I don't think it's possible to make it fully "robust" against broken hardware.

But in your case having issues 3 out of 3 syncs likely means it's more than just a single random bit flip.

## hyc | 2023-05-25T15:14:44+00:00
Yeah, MDB_PAGE_FULL would usually mean an LMDB bug but if the machine is flaky I'm a bit skeptical. I'll try doing a full sync on my LAN here, have a new SSD I wanted to test anyway.


## Gingeropolous | 2023-05-25T17:58:13+00:00
so I tried max-concurrency=1 to see if keeping things less threaded would help, and it did not. Same type of error.

I'm now attempting "db-sync-mode=safe:sync:250000000bytes"

but it seems to still be erroring out


```
2023-05-25 17:55:02.918	[P2P0]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:4476	Error adding block with hash: <0d49638c14d875f2b2eb3aa44364b8573662bc2386caaac428d448f5a21857bd> to blockchain, what = Error adding spent key image to db transaction: MDB_PAGE_NOTFOUND: Requested page not found
2023-05-25 17:55:02.918	[P2P0]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:4726	Exception at [add_new_block], what=Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-05-25 17:55:02.918	[P2P0]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1603	[65.108.195.227:18080 OUT] span connection id not found
```

I don't have another zen3 box to test it on. 

## DeeDeeRanged | 2023-05-25T18:16:02+00:00
Sounds like you have a bad RAM stick.
Try different RAM or if you have 2 or more RAM sticks remove them all but one and run memtest if it doesn't report errors add another RAM stick to find the actual culprit. It doen't matter if you use ECC RAM or not unless you have an actual need for it. For norma PC use you don't need ECC RAM. It's all basic fault finding how tedious it may seem.

## Gingeropolous | 2023-05-25T21:22:21+00:00
first some drive tests.

```
SMART Self-test log structure revision number 1
Num  Test_Description    Status                  Remaining  LifeTime(hours)  LBA_of_first_error
# 1  Extended offline    Completed without error       00%     12922         -
# 2  Short offline       Completed without error       00%     12896         -
```



## Gingeropolous | 2023-05-26T01:02:25+00:00
memtest. only show 1, but all 10 loops OK. Currently redoing it at 40GB

```
user@login-node:~$ sudo memtester 16G 10
memtester version 4.3.0 (64-bit)
Copyright (C) 2001-2012 Charles Cazabon.
Licensed under the GNU General Public License version 2 (only).

pagesize is 4096
pagesizemask is 0xfffffffffffff000
want 16384MB (17179869184 bytes)
got  16384MB (17179869184 bytes), trying mlock ...locked.
Loop 1/10:
  Stuck Address       : ok
  Random Value        : /ok
  Compare XOR         : ok
  Compare SUB         : ok
  Compare MUL         : ok
  Compare DIV         : ok
  Compare OR          : ok
  Compare AND         : ok
  Sequential Increment: ok
  Solid Bits          : ok
  Block Sequential    : ok
  Checkerboard        : ok
  Bit Spread          : ok
  Bit Flip            : ok
  Walking Ones        : ok
  Walking Zeroes      : ok
  8-bit Writes        : ok
  16-bit Writes       : ok

```

## Gingeropolous | 2023-06-17T13:34:32+00:00
OK, well I managed to sync using the same MOBO and CPU. Chalking it up to either RAM or the SSD. 

also fast=sync was 0, so thats good. 

Another glitch....... glitchin out. 

## chayleaf | 2023-12-10T05:25:06+00:00
I'm getting `MDB_PAGE_NOTFOUND` on two separate machines (aarch64 and x86_64), but in my case it seems like the issue is caused by bcachefs, as there's not much else that seems like it could cause the issue

# Action History
- Created by: Gingeropolous | 2023-05-24T17:13:02+00:00
- Closed at: 2023-06-17T13:34:32+00:00
