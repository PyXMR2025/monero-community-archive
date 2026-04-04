---
title: P2Pool keeps stopping after loading peers from seeds.p2pool.io
source_url: https://github.com/monero-project/monero-gui/issues/4239
author: colageneral
assignees: []
labels: []
created_at: '2023-11-06T18:24:45+00:00'
updated_at: '2023-11-07T12:31:33+00:00'
type: issue
status: closed
closed_at: '2023-11-07T12:22:09+00:00'
---

# Original Description
Hi all. Installed monero gui, p2pool and xmrig. Got everything set up but p2pool keeps stopping at this point 

2023-11-06 18:22:38.0034 RandomX_Hasher new seed 80d3caffd42a570354bbbac207fba4790a7f2fa7fffc4207e5c765ba0772204c
2023-11-06 18:22:38.0035 SideChain get_shares: 1 unique wallets in PPLNS window
2023-11-06 18:22:38.0036 BlockTemplate 4085 transactions can be taken with current block size limit
2023-11-06 18:22:38.0036 BlockTemplate mempool has 25 transactions, taking 3 transactions from it
2023-11-06 18:22:38.0036 BlockTemplate base  reward = 0.600000000000 XMR, 3 transactions, fees = 0.063064000000 XMR, weight = 6662
2023-11-06 18:22:38.0040 BlockTemplate blob size = 421
2023-11-06 18:22:38.0040 BlockTemplate final reward = 0.663064000000 XMR, weight = 6789, outputs = 1, 3 of 3 transactions included
2023-11-06 18:22:38.0040 P2Pool 127.0.0.1:18081:ZMQ:18083 ping is 0.179 ms
2023-11-06 18:22:38.0055 P2Pool parsed block header for height 3008512
2023-11-06 18:22:38.0055 RandomX_Hasher old seed c98ef43b341b287776473db80e4dbe9c9aa1c376104f5e53d7c96226d926f784
2023-11-06 18:22:38.3009 RandomX_Hasher cache updated
2023-11-06 18:22:38.3010 RandomX_Hasher running 32 threads to update dataset
2023-11-06 18:22:38.5866 RandomX_Hasher old cache updated
2023-11-06 18:22:38.5866 P2Pool parsed block header for height 3010560
2023-11-06 18:22:38.5912 P2Pool parsed 720 block headers for heights 3011643 - 3012362
2023-11-06 18:22:38.5914 P2Pool median timestamp updated to 1699292730
2023-11-06 18:22:38.5924 TCPServer listening on [::]:3333
2023-11-06 18:22:38.5928 TCPServer listening on 0.0.0.0:3333
2023-11-06 18:22:38.5930 StratumServer event loop started
2023-11-06 18:22:38.5935 BlockCache loading cached blocks
2023-11-06 18:22:38.6003 BlockCache loaded 0 cached blocks
2023-11-06 18:22:38.6004 P2PServer loading peers from seeds.p2pool.io
2023-11-06 18:22:38.6036 P2PServer added [2a01:4f8:160:91ef::2]:37889,[2a01:4f9:6a:1a0d::2]:37889,65.21.227.114:37889,5.9.17.234:37889 from seeds.p2pool.io

Can anyone assist? There are no errors in the p2pool log. I am using windows 11 CLI

# Discussion History
## SChernykh | 2023-11-06T19:18:55+00:00
What's the p2pool version that you use? The one that comes with GUI wallet by default?

## colageneral | 2023-11-06T20:41:23+00:00
> What's the p2pool version that you use? The one that comes with GUI wallet by default?

Hi, I am using this version:
P2Pool v3.8 (built with MSVC/1929 on Oct 31 2023)

I ran into this problem from the beginning when I was using the GUI, so I decided to reinstall windows and do everything again but through the command line. Same problem. In the GUI, it kept saying Starting P2Pool, but never showed a hash rate. I was using GUPAX then, and P2Pool always stopped saying failed. However, there were never any errors.


## SChernykh | 2023-11-06T21:13:04+00:00
What's the exact command line you use to start p2pool? You can edit out the wallet address. Can you try to add `--light-mode` to the command line? If it still crashes, also add `--loglevel 6`, maybe it will show some more stuff at the highest log level.

## colageneral | 2023-11-06T21:18:58+00:00
I tried quite a few. This would be the most loaded I guess...

 ./p2pool.exe --rpc-port 18081 --zmq-port 18083 --wallet My_Wallet --stratum 127.0.0.1:3333 --p2p 0.0.0.0:37889 --loglevel 6

Trying with your suggestion now.

## colageneral | 2023-11-06T21:25:40+00:00
> What's the exact command line you use to start p2pool? You can edit out the wallet address. Can you try to add `--light-mode` to the command line? If it still crashes, also add `--loglevel 6`, maybe it will show some more stuff at the highest log level.

Unfortunately --light-mode didn't make a difference. Anything else you can think of?

## SChernykh | 2023-11-06T21:27:31+00:00
I will prepare a debug build for you tomorrow, it will print a call stack when it crashes. I have no clue why it crashes there.

## colageneral | 2023-11-06T21:28:04+00:00
Thanks, really appreciate the assist.

## SChernykh | 2023-11-07T09:42:32+00:00
[p2pool_debug.zip](https://github.com/monero-project/monero-gui/files/13278315/p2pool_debug.zip)
Can you try to run this p2pool build? When it crashes, it should print the call stack of the crash - copy-paste it here.

## colageneral | 2023-11-07T11:17:38+00:00
> [p2pool_debug.zip](https://github.com/monero-project/monero-gui/files/13278315/p2pool_debug.zip) Can you try to run this p2pool build? When it crashes, it should print the call stack of the crash - copy-paste it here.

This is what I got. 

2023-11-07 09:16:12.6681 RandomX_Hasher new seed fdd3828a3d9f7a88418b733ba274741d2d3bc867767ea2036ffff89efc5a55f2
2023-11-07 09:16:12.6682 SideChain get_shares: 1 unique wallets in PPLNS window
2023-11-07 09:16:12.6682 BlockTemplate 4085 transactions can be taken with current block size limit
2023-11-07 09:16:12.6682 BlockTemplate mempool has 5 transactions, taking 0 transactions from it
2023-11-07 09:16:12.6682 BlockTemplate base  reward = 0.600000000000 XMR, 0 transactions, fees = 0.000000000000 XMR, weight = 0
2023-11-07 09:16:12.6684 BlockTemplate blob size = 325
2023-11-07 09:16:12.6684 BlockTemplate final reward = 0.600000000000 XMR, weight = 127, outputs = 1, 0 of 0 transactions included
2023-11-07 09:16:12.6685 P2Pool 127.0.0.1:18081:ZMQ:18083 ping is 0.171 ms
2023-11-07 09:16:12.7829 P2Pool parsed block header for height 3012608
2023-11-07 09:16:12.7829 P2Pool parsed block header for height 3010560
2023-11-07 09:16:12.7829 RandomX_Hasher old seed 80d3caffd42a570354bbbac207fba4790a7f2fa7fffc4207e5c765ba0772204c
2023-11-07 09:16:12.9797 RandomX_Hasher cache updated
2023-11-07 09:16:12.9797 RandomX_Hasher running 32 threads to update dataset
2023-11-07 09:16:13.2814 RandomX_Hasher old cache updated
2023-11-07 09:16:13.3503 P2Pool parsed 720 block headers for heights 3012119 - 3012838
2023-11-07 09:16:13.3503 P2Pool median timestamp updated to 1699351696
2023-11-07 09:16:13.3518 TCPServer listening on 127.0.0.1:3333
2023-11-07 09:16:13.3520 StratumServer event loop started
2023-11-07 09:16:13.3531 BlockCache loading cached blocks
2023-11-07 09:16:13.4225 BlockCache loaded 0 cached blocks
2023-11-07 09:16:13.4226 P2PServer loading peers from seeds.p2pool.io
2023-11-07 09:16:13.7562 P2PServer added [2a01:4f8:160:91ef::2]:37889,[2a01:4f9:6a:1a0d::2]:37889,65.21.227.114:37889,5.9.17.234:37889 from seeds.p2pool.io


Unhandled exception at:
C:\Users\user\Documents\GitHub\p2pool\src\util.cpp (p2pool::get_dns_txt_records_base, line 519)
C:\Users\user\Documents\GitHub\p2pool\src\p2p_server.cpp (<lambda_d41c4bdc6b9c00d336f2282e4c91d125>::operator(), line 508)
C:\Users\user\Documents\GitHub\p2pool\src\p2p_server.cpp (p2pool::P2PServer::load_peer_list, line 581)
C:\Users\user\Documents\GitHub\p2pool\src\p2p_server.cpp (p2pool::P2PServer::P2PServer, line 139)
C:\Users\user\Documents\GitHub\p2pool\src\p2pool.cpp (<lambda_26f49fded713a8eba48ce4fdcf7d15aa>::operator(), line 787)
C:\Users\user\Documents\GitHub\p2pool\src\json_rpc_request.cpp (p2pool::JSONRPCRequest::CurlContext::~CurlContext, line 238)
C:\Users\user\Documents\GitHub\p2pool\src\json_rpc_request.cpp (p2pool::JSONRPCRequest::CurlContext::on_close, line 459)
C:\Users\user\Documents\GitHub\p2pool\external\src\libuv\src\win\async.c (uv__async_endgame, line 37)
C:\Users\user\Documents\GitHub\p2pool\external\src\libuv\src\win\core.c (uv_run, line 668)
C:\Users\user\Documents\GitHub\p2pool\src\p2pool.cpp (p2pool::p2pool::run, line 1685)
C:\Users\user\Documents\GitHub\p2pool\src\main.cpp (main, line 197)
D:\a\_work\1\s\src\vctools\crt\vcstartup\src\startup\exe_common.inl (__scrt_common_main_seh, line 288)


2023-11-07 09:16:13.8386 Log Unhandled exception at:
2023-11-07 09:16:13.8386 Log C:\Users\user\Documents\GitHub\p2pool\src\util.cpp (p2pool::get_dns_txt_records_base, line 519)
2023-11-07 09:16:13.8386 Log C:\Users\user\Documents\GitHub\p2pool\src\p2p_server.cpp (<lambda_d41c4bdc6b9c00d336f2282e4c91d125>::operator(), line 508)
2023-11-07 09:16:13.8387 Log C:\Users\user\Documents\GitHub\p2pool\src\p2p_server.cpp (p2pool::P2PServer::load_peer_list, line 581)
2023-11-07 09:16:13.8387 Log C:\Users\user\Documents\GitHub\p2pool\src\p2p_server.cpp (p2pool::P2PServer::P2PServer, line 139)
2023-11-07 09:16:13.8387 Log C:\Users\user\Documents\GitHub\p2pool\src\p2pool.cpp (<lambda_26f49fded713a8eba48ce4fdcf7d15aa>::operator(), line 787)
2023-11-07 09:16:13.8387 Log C:\Users\user\Documents\GitHub\p2pool\src\json_rpc_request.cpp (p2pool::JSONRPCRequest::CurlContext::~CurlContext, line 238)
2023-11-07 09:16:13.8387 Log C:\Users\user\Documents\GitHub\p2pool\src\json_rpc_request.cpp (p2pool::JSONRPCRequest::CurlContext::on_close, line 459)
2023-11-07 09:16:13.8388 Log C:\Users\user\Documents\GitHub\p2pool\external\src\libuv\src\win\async.c (uv__async_endgame, line 37)
2023-11-07 09:16:13.8388 Log C:\Users\user\Documents\GitHub\p2pool\external\src\libuv\src\win\core.c (uv_run, line 668)
2023-11-07 09:16:13.8388 Log C:\Users\user\Documents\GitHub\p2pool\src\p2pool.cpp (p2pool::p2pool::run, line 1685)
2023-11-07 09:16:13.8388 Log C:\Users\user\Documents\GitHub\p2pool\src\main.cpp (main, line 197)
2023-11-07 09:16:13.8388 Log D:\a\_work\1\s\src\vctools\crt\vcstartup\src\startup\exe_common.inl (__scrt_common_main_seh, line 288)
2023-11-07 09:16:14.2356 Util UPnP: Finished scanning for UPnP IGD devices
2023-11-07 09:16:14.5960 RandomX_Hasher dataset updated

## SChernykh | 2023-11-07T11:30:33+00:00
Hmm, it shouldn't crash at that specific place - there's nothing in Microsoft's documentation about the possibility of null pointers in the returned list of strings. But I'll add a check there.

## SChernykh | 2023-11-07T11:35:46+00:00
You can try this build now
[p2pool.zip](https://github.com/monero-project/monero-gui/files/13279359/p2pool.zip)


## colageneral | 2023-11-07T11:36:03+00:00
Ok. Thanks so much. Would have loved to mine on windows on this system because I use the linux install on the same system for running models. I got the gui to mine there with p2pool though. Would you advice using GUPAX or stand alone p2pool and xmrig? I am getting 12000h/s just on the gui. 

## SChernykh | 2023-11-07T11:40:15+00:00
Standalone p2pool + xmrig is better, because nothing else is slowing them down.

## colageneral | 2023-11-07T11:41:25+00:00
ok thanks. No luck with the new p2pool build you sent. crashes at the same place it seems. 

## SChernykh | 2023-11-07T11:46:45+00:00
This is weird. Can you try this build then?
[p2pool_debug.zip](https://github.com/monero-project/monero-gui/files/13279456/p2pool_debug.zip)


## colageneral | 2023-11-07T11:50:13+00:00
2023-11-07 09:49:07.8294 RandomX_Hasher new seed fdd3828a3d9f7a88418b733ba274741d2d3bc867767ea2036ffff89efc5a55f2
2023-11-07 09:49:07.8295 SideChain get_shares: 1 unique wallets in PPLNS window
2023-11-07 09:49:07.8295 BlockTemplate 4085 transactions can be taken with current block size limit
2023-11-07 09:49:07.8295 BlockTemplate mempool has 41 transactions, taking 0 transactions from it
2023-11-07 09:49:07.8295 BlockTemplate base  reward = 0.600000000000 XMR, 0 transactions, fees = 0.000000000000 XMR, weight = 0
2023-11-07 09:49:07.8297 BlockTemplate blob size = 325
2023-11-07 09:49:07.8297 BlockTemplate final reward = 0.600000000000 XMR, weight = 127, outputs = 1, 0 of 0 transactions included
2023-11-07 09:49:07.8298 P2Pool 127.0.0.1:18081:ZMQ:18083 ping is 0.187 ms
2023-11-07 09:49:07.8308 P2Pool parsed block header for height 3010560
2023-11-07 09:49:07.8308 RandomX_Hasher old seed 80d3caffd42a570354bbbac207fba4790a7f2fa7fffc4207e5c765ba0772204c
2023-11-07 09:49:08.1182 RandomX_Hasher cache updated
2023-11-07 09:49:08.1183 RandomX_Hasher running 32 threads to update dataset
2023-11-07 09:49:08.3947 RandomX_Hasher old cache updated
2023-11-07 09:49:08.4000 P2Pool parsed 720 block headers for heights 3012133 - 3012852
2023-11-07 09:49:08.4000 P2Pool median timestamp updated to 1699353798
2023-11-07 09:49:08.4009 TCPServer listening o

Unhandled exception C0000005 at:
n 127.0.0.1:3333
2023-11-07 09:49:08.4011 StratumServer event loop started
2023-11-07 09:49:08.4015 BlockCache loading cached blocks
2023-11-07 09:49:08.4084 BlockCache loaded 0 cached blocks
2023-11-07 09:49:08.4084 P2PServer loading peers from seeds.p2pool.io
2023-11-07 09:49:08.4090 P2PServer added [2a01:4f8:160:91ef::2]:37889,[2a01:4f9:6a:1a0d::2]:37889,65.21.227.114:37889,5.9.17.234:37889 from seeds.p2pool.io
C:\Users\user\Documents\GitHub\p2pool\src\util.cpp (p2pool::get_dns_txt_records_base, line 521)
C:\Users\user\Documents\GitHub\p2pool\src\p2p_server.cpp (<lambda_d41c4bdc6b9c00d336f2282e4c91d125>::operator(), line 508)
C:\Users\user\Documents\GitHub\p2pool\src\p2p_server.cpp (p2pool::P2PServer::load_peer_list, line 581)
C:\Users\user\Documents\GitHub\p2pool\src\p2p_server.cpp (p2pool::P2PServer::P2PServer, line 139)
C:\Users\user\Documents\GitHub\p2pool\src\p2pool.cpp (<lambda_26f49fded713a8eba48ce4fdcf7d15aa>::operator(), line 787)
C:\Users\user\Documents\GitHub\p2pool\src\json_rpc_request.cpp (p2pool::JSONRPCRequest::CurlContext::~CurlContext, line 238)
C:\Users\user\Documents\GitHub\p2pool\src\json_rpc_request.cpp (p2pool::JSONRPCRequest::CurlContext::on_close, line 459)
C:\Users\user\Documents\GitHub\p2pool\external\src\libuv\src\win\async.c (uv__async_endgame, line 37)
C:\Users\user\Documents\GitHub\p2pool\external\src\libuv\src\win\core.c (uv_run, line 668)
C:\Users\user\Documents\GitHub\p2pool\src\p2pool.cpp (p2pool::p2pool::run, line 1685)
C:\Users\user\Documents\GitHub\p2pool\src\main.cpp (main, line 197)
D:\a\_work\1\s\src\vctools\crt\vcstartup\src\startup\exe_common.inl (__scrt_common_main_seh, line 288)


2023-11-07 09:49:08.4821 Log Unhandled exception c0000005 at:
2023-11-07 09:49:08.4821 Log C:\Users\user\Documents\GitHub\p2pool\src\util.cpp (p2pool::get_dns_txt_records_base, line 521)
2023-11-07 09:49:08.4822 Log C:\Users\user\Documents\GitHub\p2pool\src\p2p_server.cpp (<lambda_d41c4bdc6b9c00d336f2282e4c91d125>::operator(), line 508)
2023-11-07 09:49:08.4822 Log C:\Users\user\Documents\GitHub\p2pool\src\p2p_server.cpp (p2pool::P2PServer::load_peer_list, line 581)
2023-11-07 09:49:08.4822 Log C:\Users\user\Documents\GitHub\p2pool\src\p2p_server.cpp (p2pool::P2PServer::P2PServer, line 139)
2023-11-07 09:49:08.4822 Log C:\Users\user\Documents\GitHub\p2pool\src\p2pool.cpp (<lambda_26f49fded713a8eba48ce4fdcf7d15aa>::operator(), line 787)
2023-11-07 09:49:08.4822 Log C:\Users\user\Documents\GitHub\p2pool\src\json_rpc_request.cpp (p2pool::JSONRPCRequest::CurlContext::~CurlContext, line 238)
2023-11-07 09:49:08.4822 Log C:\Users\user\Documents\GitHub\p2pool\src\json_rpc_request.cpp (p2pool::JSONRPCRequest::CurlContext::on_close, line 459)
2023-11-07 09:49:08.4823 Log C:\Users\user\Documents\GitHub\p2pool\external\src\libuv\src\win\async.c (uv__async_endgame, line 37)
2023-11-07 09:49:08.4823 Log C:\Users\user\Documents\GitHub\p2pool\external\src\libuv\src\win\core.c (uv_run, line 668)
2023-11-07 09:49:08.4823 Log C:\Users\user\Documents\GitHub\p2pool\src\p2pool.cpp (p2pool::p2pool::run, line 1685)
2023-11-07 09:49:08.4823 Log C:\Users\user\Documents\GitHub\p2pool\src\main.cpp (main, line 197)
2023-11-07 09:49:08.4823 Log D:\a\_work\1\s\src\vctools\crt\vcstartup\src\startup\exe_common.inl (__scrt_common_main_seh, line 288)
2023-11-07 09:49:08.8788 Util UPnP: Finished scanning for UPnP IGD devices

## colageneral | 2023-11-07T11:54:09+00:00
The time on the log is incorrect. It is 13:53 here. Could this be the issue?

## SChernykh | 2023-11-07T11:57:32+00:00
P2Pool shows UTC time in the log, so people don't leak their timezone when posting logs. And it's easier to compare different logs when they all have the same time.

## colageneral | 2023-11-07T11:58:15+00:00
Got you. Thanks.

## SChernykh | 2023-11-07T12:08:47+00:00
This build should work
[p2pool_debug.zip](https://github.com/monero-project/monero-gui/files/13279645/p2pool_debug.zip)


## colageneral | 2023-11-07T12:12:18+00:00
It works :) 

## colageneral | 2023-11-07T12:19:20+00:00
Thank you! much appreciated. you can close the issue if there is nothing further from yourside. 

## SChernykh | 2023-11-07T12:21:40+00:00
I can't close it, you should find "close" button somewhere on this page and click it.

## colageneral | 2023-11-07T12:31:32+00:00
Thanks!

# Action History
- Created by: colageneral | 2023-11-06T18:24:45+00:00
- Closed at: 2023-11-07T12:22:09+00:00
