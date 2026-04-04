---
title: monerod started to crash
source_url: https://github.com/monero-project/monero/issues/3551
author: Keksov
assignees: []
labels: []
created_at: '2018-04-04T11:40:40+00:00'
updated_at: '2018-08-26T17:07:28+00:00'
type: issue
status: closed
closed_at: '2018-04-09T12:17:28+00:00'
---

# Original Description
After upgrading to 0.12 (official binaries, Win Server 2008 R2 x64) monerod was able to sync and worked for several days without issues. But two of three days ago it was terminated with a error and now it can't be started at all - it crashes right after start. I've resurrected one month old lmdb database from backup and monerod is able to sync until it reaches some height and crashes. Here is log-level 4 output from monerod:
[bitmonero.zip](https://github.com/monero-project/monero/files/1875508/bitmonero.zip)
Here is the error message from windows log:
```
- <Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
- <System>
  <Provider Name="Application Error" /> 
  <EventID Qualifiers="0">1000</EventID> 
  <Level>2</Level> 
  <Task>100</Task> 
  <Keywords>0x80000000000000</Keywords> 
  <TimeCreated SystemTime="2018-04-04T11:36:44.000000000Z" /> 
  <EventRecordID>82579724</EventRecordID> 
  <Channel>Application</Channel> 
  <Computer>FOOBOO</Computer> 
  <Security /> 
  </System>
- <EventData>
  <Data>monerod.exe</Data> 
  <Data>0.0.0.0</Data> 
  <Data>5aba638b</Data> 
  <Data>msvcrt.dll</Data> 
  <Data>7.0.7601.17744</Data> 
  <Data>4eeb033f</Data> 
  <Data>c0000005</Data> 
  <Data>0000000000015a01</Data> 
  <Data>6bc</Data> 
  <Data>01d3cc091eb6d28e</Data> 
  <Data>c:\bin\monero-v0.12.0.0\monerod.exe</Data> 
  <Data>C:\Windows\system32\msvcrt.dll</Data> 
  <Data>7334ce4f-37fc-11e8-a9da-000c2947840f</Data> 
  </EventData>
  </Event>
```

# Discussion History
## moneromooo-monero | 2018-04-04T12:11:08+00:00
Can you get a stack trace for the crash ? I don't know offhand how to do this on windows though. The log does not seem to have clues.

## Keksov | 2018-04-04T13:07:09+00:00
Do you have debug symbol file? Below is an output from windbg,
```
(5b4.4fc): Access violation - code c0000005 (first chance)
First chance exceptions are reported before any exception handling.
This exception may be expected and handled.
*** ERROR: Symbol file could not be found.  Defaulted to export symbols for monerod.exe - 
msvcrt!strlen+0x31:
000007fe`ff035a01 488b10          mov     rdx,qword ptr [rax] ds:00000000`00000000=????????????????
```
And output from monerod is
```
2018-04-04 13:12:20.355 [P2P5]  INFO    global  src/cryptonote_protocol/cryptono
te_protocol_handler.inl:310     [24.193.54.34:18080 OUT] Sync data returned a ne
w top block candidate: 1543366 -> 1544643 [Your node is 1277 blocks (1 days) beh
ind]
SYNCHRONIZATION started
```

## Keksov | 2018-04-04T13:11:12+00:00
Can you please provide monerod.exe with enabled debug info?

## moneromooo-monero | 2018-04-04T13:15:31+00:00
Thanks, that's starting to be helpful. Can you get a stack trace ? Maybe try "help" in windbg, and look for such a command.

## Keksov | 2018-04-04T13:24:09+00:00
Without debug info it looks cryptic 
```
 # Child-SP          RetAddr           : Args to Child                                                           : Call Site
00 00000000`109fd678 00000000`00787a5e : 00000000`0000002f 005203db`17982769 00000000`109fd6f0 00000000`109fd7a0 : msvcrt!strlen+0x31
01 00000000`109fd680 00000000`00073c00 : 00000000`109fd6ec 00000000`090750d0 00000000`109fd700 00000000`0000000f : monerod!ZNK5boost7archive6detail11oserializerINS0_24portable_binary_oarchiveEN8nodetool26anchor_peerlist_entry_baseIN4epee9net_utils15network_addressEEEE16save_object_dataERNS1_14basic_oarchiveEPKv+0xf976e
02 00000000`109fd6c0 00000000`000d4996 : 01d3cc18`d1f62ab6 00000000`00000000 00000000`00000000 00000000`00000000 : monerod+0x63c00
03 00000000`109fd860 00000000`000c1218 : 00000000`109fdb20 00000000`77961910 00000000`128eec80 00000000`00003303 : monerod+0xc4996
04 00000000`109fdb00 00000000`000c190f : 00000000`00000000 00000000`00000000 00000000`00000000 00000000`00000000 : monerod+0xb1218
05 00000000`109fdc30 00000000`004cea31 : 00000000`01960000 00000000`77c23771 00000000`01960000 00000000`12853f01 : monerod+0xb190f
06 00000000`109fde40 00000000`004d7335 : 00000000`090c9b70 00000000`77bc797c 00000000`01960000 7fffffff`fffffffe : monerod+0x4bea31
07 00000000`109fe400 00000000`005a9378 : 00000000`00000001 00000000`00000027 00000000`40000062 00000000`01960000 : monerod+0x4c7335
08 00000000`109fe810 00000000`004cd99a : 00000000`77c703c8 00000000`000007d4 00000000`00000000 00000000`01960000 : monerod+0x599378
09 00000000`109fea50 00000000`0065ec38 : 00000000`109fedc0 00000000`006a27ce 00000000`00000020 00000000`00000000 : monerod+0x4bd99a
0a 00000000`109fec40 00000000`0066a722 : 00000000`109fef30 00000000`00000af3 00000000`109ff0f0 00000000`004535d9 : monerod!ZN5boost7archive6detail11oserializerINS0_24portable_binary_oarchiveEN8nodetool26anchor_peerlist_entry_baseIN4epee9net_utils15network_addressEEEEC2Ev+0x18eb8
0b 00000000`109fee20 00000000`0054392d : 00000000`00000000 00000000`00000000 00000000`00000000 00000000`109fefb0 : monerod!ZN5boost7archive6detail11oserializerINS0_24portable_binary_oarchiveEN8nodetool26anchor_peerlist_entry_baseIN4epee9net_utils15network_addressEEEEC2Ev+0x249a2
0c 00000000`109feed0 00000000`005656be : 01d3cc18`d012f35f 00000000`50000163 00000000`00000af3 00000000`00000000 : monerod+0x53392d
0d 00000000`109ff060 00000000`00620df9 : 00000000`00000000 00000000`0046c076 00000000`00000af3 005203db`17982769 : monerod+0x5556be
0e 00000000`109ff210 00000000`00623c86 : 00000000`000493e0 000007fe`fdb3a256 00000000`00000000 00000000`002144d8 : monerod!ZN5boost13serialization9singletonISt8multisetIPKNS0_18extended_type_infoENS0_6detail11key_compareESaIS5_EEE20get_mutable_instanceEv+0x39529
0f 00000000`109ff2d0 00000000`006208bd : 00000000`77955170 00000000`091cee60 00000000`109ff570 00000000`005654a0 : monerod!ZN5boost13serialization9singletonISt8multisetIPKNS0_18extended_type_infoENS0_6detail11key_compareESaIS5_EEE20get_mutable_instanceEv+0x3c3b6
10 00000000`109ff3f0 00000000`00628428 : 00000000`005b8b00 00000000`00000000 00000000`090fd970 00000000`090fda10 : monerod!ZN5boost13serialization9singletonISt8multisetIPKNS0_18extended_type_infoENS0_6detail11key_compareESaIS5_EEE20get_mutable_instanceEv+0x38fed
11 00000000`109ff4d0 00000000`00626161 : 00000000`01852ad0 00000000`004f6754 00000000`090fe820 00000000`00000000 : monerod!ZN5boost13serialization9singletonISt8multisetIPKNS0_18extended_type_infoENS0_6detail11key_compareESaIS5_EEE20get_mutable_instanceEv+0x40b58
12 00000000`109ff610 00000000`005b7ad7 : 00000000`01934920 00000000`00a2e4c0 00000000`00000000 00000000`00000000 : monerod!ZN5boost13serialization9singletonISt8multisetIPKNS0_18extended_type_infoENS0_6detail11key_compareESaIS5_EEE20get_mutable_instanceEv+0x3e891
13 00000000`109ff6e0 00000000`0045e38d : 00000000`017771d0 000007fe`ff021407 00000000`090fe820 00000000`00000001 : monerod+0x5a7ad7
14 00000000`109ff9e0 000007fe`ff02415f : 00000000`017771d0 00000000`00000000 00000000`00000000 00000000`00000000 : monerod+0x44e38d
15 00000000`109ffa20 000007fe`ff026ebd : 000007fe`ff0b1ea0 00000000`090fe820 00000000`00000000 00000000`00000000 : msvcrt!endthreadex+0x47
16 00000000`109ffa50 00000000`779559cd : 00000000`00000000 00000000`00000000 00000000`00000000 00000000`00000000 : msvcrt!endthreadex+0xe0
17 00000000`109ffa80 00000000`77b8a561 : 00000000`00000000 00000000`00000000 00000000`00000000 00000000`00000000 : kernel32!BaseThreadInitThunk+0xd
18 00000000`109ffab0 00000000`00000000 : 00000000`00000000 00000000`00000000 00000000`00000000 00000000`00000000 : ntdll!RtlUserThreadStart+0x1d

```

## mmortal03 | 2018-04-04T15:48:38+00:00
I'm also getting crashing with 0.12 on Windows over on this other issue thread, working on getting better debug info: https://github.com/monero-project/monero/issues/3540

## Keksov | 2018-04-07T08:00:29+00:00
Well... three days later, running debug version (thanx to #3523 `git clone --recursive https://github.com/monero-project/monero` and #3490 [patch](https://github.com/monero-project/monero/pull/3490/commits/3fb42230697098655fccfc0716fb2a97d20d3041)) and got some meaningful output (no crash, but errors).

The message `The requested operation can not be completed due to the limitation of the file system` came from OS. Applying a [hotfix KB967351 from MS](https://support.microsoft.com/en-us/help/967351/a-heavily-fragmented-file-in-an-ntfs-volume-may-not-grow-beyond-a-cert) didn't help (after reboot) Size of data.mdb is 48461512704 bytes, looks like it unable to grow anymore.

```
2018-04-07 07:22:42.529	616	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-04-07 07:22:42.529	616	INFO 	global	src/daemon/main.cpp:280	Monero 'Lithium Luna' (v0.12.0.0-master-8361d60a)
2018-04-07 07:22:42.544	616	INFO 	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2018-04-07 07:22:42.544	616	INFO 	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2018-04-07 07:22:42.544	616	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2018-04-07 07:22:46.803	616	INFO 	global	src/daemon/p2p.h:68	p2p server initialized OK
2018-04-07 07:22:47.302	616	INFO 	global	src/daemon/rpc.h:63	Initializing core RPC server...
2018-04-07 07:22:47.302	616	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:76	Binding on 127.0.0.1:18081
2018-04-07 07:22:47.302	616	INFO 	global	src/daemon/rpc.h:69	core RPC server initialized OK on port: 18081
2018-04-07 07:22:47.302	616	INFO 	global	src/daemon/core.h:86	Initializing core...
2018-04-07 07:22:47.302	616	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:427	Loading blockchain from folder C:\ProgramData\bitmonero\lmdb ...
2018-04-07 07:23:30.748	616	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:4396	Block hash data does not match expected hash
2018-04-07 07:23:30.998	616	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:525	Loading checkpoints
2018-04-07 07:23:32.433	616	INFO 	global	src/daemon/core.h:92	Core initialized OK
2018-04-07 07:23:32.433	616	INFO 	global	src/daemon/rpc.h:74	Starting core RPC server...
2018-04-07 07:23:32.433	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:79	core RPC server started ok
2018-04-07 07:23:32.464	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:78	Starting p2p net loop...
2018-04-07 07:23:33.478	[P2P7]	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:1386	[1;33m
**********************************************************************
The daemon will start synchronizing with the network. This may take a long time to complete.

You can set the level of process detailization through "set_log <level|categories>" command,
where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).

Use the "help" command to see the list of available commands.
Use "help <command>" to see a command's documentation.
**********************************************************************
[0m
2018-04-07 07:23:33.993	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[67.218.193.131:18080 OUT] Sync data returned a new top block candidate: 1543378 -> 1546086 [Your node is 2708 blocks (3 days) behind] 
SYNCHRONIZATION started
2018-04-07 07:24:34.240	[P2P4]	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:295	internal error: transaction already exists at inserting in memory pool: Error adding txpool tx blob to db transaction: The requested operation can not be completed due to the limitation of the file system


2018-04-07 07:24:34.240	[P2P4]	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:75	Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2018-04-07 07:24:34.240	[P2P4]	ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:781	Exception at [core::handle_incoming_txs()], what=Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2018-04-07 07:24:34.240	[P2P4]	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:75	Failed to commit a transaction to the db: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2018-04-07 07:24:34.240	[P2P4]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:3733	Exception in cleanup_handle_incoming_blocks: Failed to commit a transaction to the db: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2018-04-07 07:24:41.323	[P2P6]	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:295	internal error: transaction already exists at inserting in memory pool: Error adding txpool tx blob to db transaction: The requested operation can not be completed due to the limitation of the file system


2018-04-07 07:24:41.323	[P2P6]	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:75	Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2018-04-07 07:24:41.323	[P2P6]	ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:781	Exception at [core::handle_incoming_txs()], what=Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2018-04-07 07:24:41.323	[P2P6]	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:75	Failed to commit a transaction to the db: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2018-04-07 07:24:41.323	[P2P6]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:3733	Exception in cleanup_handle_incoming_blocks: Failed to commit a transaction to the db: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2018-04-07 07:25:02.336	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:80	p2p net loop stopped
2018-04-07 07:25:02.710	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:84	Stopping core RPC server...
2018-04-07 07:25:02.710	[SRV_MAIN]	INFO 	global	src/daemon/daemon.cpp:189	Node stopped.
2018-04-07 07:25:02.710	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:96	Deinitializing core RPC server...
2018-04-07 07:25:02.710	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:90	Deinitializing p2p...
2018-04-07 07:25:06.766	[SRV_MAIN]	INFO 	global	src/daemon/core.h:103	Deinitializing core...
2018-04-07 07:25:06.798	[SRV_MAIN]	INFO 	global	src/daemon/protocol.h:75	Stopping cryptonote protocol...
2018-04-07 07:25:06.798	[SRV_MAIN]	INFO 	global	src/daemon/protocol.h:79	Cryptonote protocol stopped successfully 
```

## moneromooo-monero | 2018-04-07T08:13:25+00:00
What filesystem, out of curiosity ?

## Keksov | 2018-04-07T09:05:03+00:00
NTFS 

## Keksov | 2018-04-09T12:17:28+00:00
I was able to fix the problem by (re)formatting the partition using 16K cluster size. 
1. Copy bitmonero directory to backup location
2. Format the partition
3. Restore bitmonero directory from backup

## mmortal03 | 2018-04-10T00:36:51+00:00
This still sounds like a bug that needs to be fixed. Monero shouldn't be dependent on a particular hard drive cluster size. @Keksov , what was your drive at before, 512 bytes per sector, and 4096 bytes per cluster? That's what mine is at.

## Keksov | 2018-04-10T09:07:16+00:00
Mine was 4096 bytes per cluster. The only viable solution, to my mind, would be partitioning of blockchain DB on say monthly basis so it would span several files (one file per month). I wish Monero exponential grow, so we need a solution anyway...

## mmortal03 | 2018-04-11T09:00:33+00:00
I will test this workaround to see if this also solves the crashing problem that I've been experiencing.

## Marcus-Vittek-Haakan | 2018-04-12T10:51:29+00:00
I can confirm I'm getting a crash on monerod as well. However, I was using a larger DB as I just was like 1000 blocks behind yet it didn't update anymore so I used a backup database and now I can't go beyond block 1500518 before it crashes. 



## Keksov | 2018-04-12T10:56:43+00:00
@Marcus-Vittek-Haakan did you try to fix the problem by formatting partition with 16K cluster size? (see my comment above)

## Marcus-Vittek-Haakan | 2018-04-12T18:30:41+00:00
Indeed, I did. Although I have the database in a different partition than the OS, I'd prefer to explore other solutions. 

## mmortal03 | 2018-04-19T13:45:08+00:00
@Keksov , I'm preparing to test this, but where did you come up with the idea to try a 16k cluster size in the first place?

## Keksov | 2018-04-19T14:10:02+00:00
@mmortal03 Just a wild guess. According to [MS article](https://technet.microsoft.com/en-us/library/cc750355.aspx) maximum file size for 4K cluster is 16TB. It's way larger that current data.mdb, so I don't think that was a reason of the problem. Probably the volume on my server had some strange problems due to it's 5+ years history and (re)formatting solved it. May be (re)formatting with 4K cluster size would be also a solution, I don't know, would be nice if you may try to verify it.

## Keksov | 2018-04-19T14:12:23+00:00
@mmortal03 actually from performance point of view formatting with 64K cluster size would be even better. [NTFS optimization](http://www.ntfs.com/ntfs_optimization.htm)

## Marcus-Vittek-Haakan | 2018-04-19T18:57:44+00:00
Ok, granted. But one shouldn't be needing to reformat a partition in order to download a blockchain and run a daemon I guess... I think we can consider this a workaround while the devs figure it out. A smart move nonetheless. 

-----Mensaje original-----
De: Keksov [mailto:notifications@github.com] 
Enviado el: jueves, 19 de abril de 2018 10:13
Para: monero-project/monero
CC: Marcus Vittek Haakan; Mention
Asunto: Re: [monero-project/monero] monerod started to crash (#3551)

@mmortal03 actually from performance point of view formatting with 64K cluster size would be even better. [NTFS optimization](http://www.ntfs.com/ntfs_optimization.htm)

-- 
You are receiving this because you were mentioned.
Reply to this email directly or view it on GitHub:
https://github.com/monero-project/monero/issues/3551#issuecomment-382751642



## mmortal03 | 2018-04-20T11:21:19+00:00
As a temporary workaround, I started running the Linux version of monerod on the same computer, accessing the same NTFS file system, but by way of Windows Subsystem for Linux (Ubuntu). This might be speaking the obvious, but whatever virtualization that WSL makes use of, or the difference in the Linux version itself, gets around any potential filesystem issue. Not a solution, though, just a workaround.

Anyway, this past evening, I decided to try the Windows version of monerod again, and got the same crashing issue, so this wasn't something transient -- it's still happening at the current block height.

So, first step, I'm going to set the monerod data directory to an external NTFS drive with the same 4096 cluster size to see what happens there. If it still crashes doing that, I'll try some more exotic settings, like larger cluster size, or even exFAT.

## mmortal03 | 2018-04-20T15:35:08+00:00
Yep, just crashed even with the external NTFS drive at 4096. Time to try some other parameters.

## mmortal03 | 2018-04-21T09:14:02+00:00
Ok, back from testing. Looks like my issue may be different. Tried exFAT, still crashes. Tried 16k cluster size with NTFS, still crashes. Every time it crashes, I get the following:

Assertion failed: Connection reset by peer (../zeromq-4.2.3/src/signaler.cpp:357)
Assertion failed: Connection reset by peer (../zeromq-4.2.3/src/signaler.cpp:357)
Assertion failed: Connection reset by peer (../zeromq-4.2.3/src/signaler.cpp:357)

## Keksov | 2018-04-21T12:29:38+00:00
Which binary did you try? I tested it with debug version (see my comment above)

## mmortal03 | 2018-04-24T00:50:04+00:00
I'm referring to the regular binaries. I'll build the binaries for debugging. I overlooked that necessity earlier; it would be the obvious next step if I was applying more brain power to this. 😄 

## mmortal03 | 2018-04-24T14:14:32+00:00
OK, I've compiled the debug build up through commit 3fb4223 (as was mentioned above).
Testing it now to see if it crashes. Once I can reproduce with the debug build, I'll see what the logs show and I presume I'll need to break out windbg.
@Keksov , what level of log verbosity were you using to produce the above log, in the following comment? Was it the default?: https://github.com/monero-project/monero/issues/3551#issuecomment-379447360

## mmortal03 | 2018-04-24T19:42:08+00:00
Yep, I was able to reproduce the crashing with the debug build. The following is at log level 1. I'll run it from the debugger next time to catch debug info.

[level_1.txt](https://github.com/monero-project/monero/files/1944314/level_1.txt)




## mmortal03 | 2018-04-25T16:57:49+00:00
I did some research, and windbg isn't what we need to use to debug this, as these debug builds don't contain the symbols that windbg expects; debugging needs to happen with gdb on msys2 so that the expected symbols format can be read. I got msys2 and gdb installed on the relevant machine and ran monerod through gdb. I've currently got it paused at the fault point where it crashes, but I haven't used gdb before, so hopefully someone (@moneromooo-monero ?) can walk me through exporting the information that would be needed to diagnose the crashing. If need be, I can also figure out how to get the source code onto the machine working with an IDE so that we can more easily find the point in the source where it crashes.

## mmortal03 | 2018-04-25T20:16:34+00:00
Using gdb, it looks like the issue starts at line 46 of daemon/main.cpp, which is the include for "blockchain_db/db_types.h". I don't know how helpful that is.

I tried to do a backtrace, but it says:
```
#0  0x00007ffc37984008 in RaiseException ()
   from C:\WINDOWS\System32\KernelBase.dll
#1  0x0000000000f3ed64 in ?? ()
Backtrace stopped: previous frame inner to this frame (corrupt stack?)
```

## kenken64 | 2018-08-26T00:23:29+00:00
Uncaught exception! Error adding hard fork version to db transaction: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid

## mmortal03 | 2018-08-26T17:07:28+00:00
I must have written this elsewhere, @Keksov , but my issue was NetWorx causing zeromq to crash. Did you find the solution to your issue?

# Action History
- Created by: Keksov | 2018-04-04T11:40:40+00:00
- Closed at: 2018-04-09T12:17:28+00:00
