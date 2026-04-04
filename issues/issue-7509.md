---
title: All Hosts Blocked
source_url: https://github.com/monero-project/monero/issues/7509
author: dremil
assignees: []
labels: []
created_at: '2021-03-11T13:31:54+00:00'
updated_at: '2021-08-13T03:57:38+00:00'
type: issue
status: closed
closed_at: '2021-08-13T03:57:37+00:00'
---

# Original Description
Hey,

I was syncing with monerod and since my internet connection cut for 1 hour i only get the message that all the hosts are blocked when trying to sync. Any body now a fix for it?
i m Starting it from a different disk with this command:
/media/USER/DISK/monero-x86_64-linux-gnu-v0.17.1.9/monerod --data-dir /media/USERl/DISK/SYNC --enable-dns-blocklist

This is what i get in the terminal

2021-03-11 13:24:27.790	I Host 105.226.221.175 blocked.
2021-03-11 13:24:43.793	I Host 95.84.1.206 blocked.
2021-03-11 13:25:15.798	I Host 194.75.9.127 blocked.
2021-03-11 13:25:46.512	I [185.189.125.19:18080 OUT] Sync data returned a new top block candidate: 1332412 -> 2314646 [Your node is 982234 blocks (3.7 years) behind] 
2021-03-11 13:25:46.513	I SYNCHRONIZATION started
2021-03-11 13:26:59.813	I Host 34.241.206.202 blocked.
2021-03-11 13:27:07.815	I Host 96.55.129.45 blocked.
..... and so on forever!

EDIT:
If i start a completely new sync of the blockchain in a different directory it starts to sync normally again. I m in a remote area with bad connection, downloading everything again would take days.
EDIT EDIT: now starting a fresh sync also doesnt work anymore!



# Discussion History
## mrx23dot | 2021-03-11T16:14:34+00:00
Reported @analyticname857 to admins for spamming

## selsta | 2021-03-11T16:15:28+00:00
@mrx23dot Github usually deletes the spam after a couple hours.

## selsta | 2021-03-11T16:16:10+00:00
> If i start a completely new sync of the blockchain in a different directory it starts to sync normally again. I m in a remote area with bad connection, downloading everything again would take days.

Having your connections cut out should not result in peers getting banned. Please report back if you see the same behaviour again.

## dremil | 2021-03-11T16:17:44+00:00
> > If i start a completely new sync of the blockchain in a different directory it starts to sync normally again. I m in a remote area with bad connection, downloading everything again would take days.
> 
> Having your connections cut out should not result in peers getting banned. Please report back if you see the same behaviour again.

Its always happening since then, restart doesn't help.

## selsta | 2021-03-11T16:19:38+00:00
Does your node continue to sync even if peers getting banned?

## selsta | 2021-03-11T16:19:50+00:00
Also can you try starting monerod with --enable-dns-blocklist and try again?

## dremil | 2021-03-11T16:41:31+00:00
> Does your node continue to sync even if peers getting banned?
> Also can you try starting monerod with --enable-dns-blocklist and try again?

No nothing gets synced anymore, every IP just gets blocked.

as described in the first post i did already start it with --enable-dns-blocklist


## moneromooo-monero | 2021-03-11T18:32:15+00:00
This probably means your blockchain is corrupted, and it thinks all the data everyone sends is wrong, since it doens't agree with its local state. Did you have a power cut or OS crash shortly before ?

## dremil | 2021-03-11T19:25:06+00:00
EDIT:
i thought its solved, internet is a bit faster now and it worked one time to sync for 30 minutes, now its blocking everything again since 2 hours. Regardless if i use -enable-dns-blocklist or not.

## moneromooo-monero | 2021-03-12T13:07:58+00:00
I guess it could happen if your internet is very, very slow (ie, you request some data, but peers take a very long time to reply).

## sumariva | 2021-08-10T01:40:10+00:00
Today I got the same issue. I stopped my node using the pkill monerod.
The log file says it has stopped the node successfully.
Now restarted the node with --out-peers 4 --block-sync-size 100 and max-concurrency 4.
I let the node run for more than 8 hours and got several blocked hosts and none block synced.
I using the version from
git checkout tags/v0.17.2.0
Internet connection is DSL 500Kbits ~50KiB/s.
Log file contains the following advertise messages

> 2021-08-10 01:23:28.494 [P2P2]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:410     SYNCHRONIZATION started
2021-08-10 01:24:27.471 [P2P3]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:410     [45.63.106.192:42802 INC] Sync data returned a new top block candidate: 1306188 -> 2423690 [Your node is 1117502 blocks (4.2 years) behind]
2021-08-10 01:24:27.471 [P2P3]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:410     SYNCHRONIZATION started
2021-08-10 01:25:09.409 [P2P8]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:410     [88.198.32.34:57888 INC] Sync data returned a new top block candidate: 1306188 -> 2423691 [Your node is 1117503 blocks (4.2 years) behind]
2021-08-10 01:25:09.409 [P2P8]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:410     SYNCHRONIZATION started
2021-08-10 01:25:22.747     7faee41f3700        INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: boost::thread_interrupted
2021-08-10 01:25:22.747     7faee41f3700        INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:
2021-08-10 01:25:22.748     7faee41f3700        INFO    stacktrace      src/common/stack_trace.cpp:172      [1]  0x113) [0x55b3fa0cd73b]:__cxa_throw+0x113) [0x55b3fa0cd73b]
2021-08-10 01:25:22.749     7faee41f3700        INFO    stacktrace      src/common/stack_trace.cpp:172      [2]  0xf1dd) [0x7fb331a071dd]:_64-linux-gnu/libboost_thread.so.1.71.0(+0xf1dd) [0x7fb331a071dd]
2021-08-10 01:25:22.749     7faee41f3700        INFO    stacktrace      src/common/stack_trace.cpp:172      [3]  0x33e) [0x55b3fa44e8be]:_ZZN8nodetool11node_serverIN10cryptonote29t_cryptonote_protocol_handlerINS1_4coreEEEE18get_dns_seed_nodesB5cxx11EvENKUlvE_clEv+0x33e) [0x55b3fa44e8be]
2021-08-10 01:25:22.749     7faee41f3700        INFO    stacktrace      src/common/stack_trace.cpp:172      [4]  0x1143b) [0x7fb331a0943b]:_64-linux-gnu/libboost_thread.so.1.71.0(+0x1143b) [0x7fb331a0943b]
2021-08-10 01:25:22.749     7faee41f3700        INFO    stacktrace      src/common/stack_trace.cpp:172      [5]  0x9609) [0x7fb331639609]:_64-linux-gnu/libpthread.so.0(+0x9609) [0x7fb331639609]
2021-08-10 01:25:22.749     7faee41f3700        INFO    stacktrace      src/common/stack_trace.cpp:172      [6]  0x43) [0x7fb33155a293]:_64-linux-gnu/libc.so.6(clone+0x43) [0x7fb33155a293]
2021-08-10 01:25:22.749     7faee41f3700        INFO    stacktrace      src/common/stack_trace.cpp:172
2021-08-10 01:25:24.957 [P2P3]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:410     [84.19.86.162:55258 INC] Sync data returned a new top block candidate: 1306188 -> 2423691 [Your node is 1117503 blocks (4.2 years) behind]
2021-08-10 01:36:22.956 [P2P8]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:410     SYNCHRONIZATION started
2021-08-10 01:37:14.149 [P2P1]  INFO    global  src/p2p/net_node.inl:283        Host 52.73.168.104 blocked.

I have about 53% of all blocks synced. Could not figure whats is the problem.
I see some error messages related to libboost on logs but monerod keeps running.
The same internet connection synced 53% using --out-peers 16, so should not be slow speed problem.

## selsta | 2021-08-10T01:42:15+00:00
> Now restarted the node with --out-peers 4 --block-sync-size 100 and max-concurrency 4.

Which config did you initially use?

Do you have enough disk space?


## sumariva | 2021-08-10T01:45:23+00:00
This is the bash command used to start daemon:
`monerod --restricted-rpc --max-log-files 8 --max-log-file-size 33554432 --log-file monerod.log --max-concurrency 4 --public-node --prune-blockchain --no-igd --out-peers 4 --block-sync-size 100 --limit-rate-up 400 --detach`

The df tool reported

> /dev/sda4       212G  112G   96G  54% /home

Server is up and other coin nodes are working properly.

## selsta | 2021-08-10T01:46:50+00:00
Please try to restart with just ./monerod, no settings


## sumariva | 2021-08-10T02:03:21+00:00
OK, now has passed about 10 minutes since restart.
These are all the blocks that were synced but got more blocked hosts.

> 2021-08-10 01:48:12.237 I Monero 'Oxygen Orion' (v0.17.2.0-release)
2021-08-10 01:48:12.237 I Initializing cryptonote protocol...
2021-08-10 01:48:12.237 I Cryptonote protocol initialized OK
2021-08-10 01:48:12.238 I Initializing core...
2021-08-10 01:48:12.239 I Loading blockchain from folder /home/monero/.bitmonero/lmdb ...
2021-08-10 01:48:12.401 I Loading checkpoints
2021-08-10 01:48:12.402 I Core initialized OK
2021-08-10 01:48:12.402 I Initializing p2p server...
2021-08-10 01:48:12.411 I p2p server initialized OK
2021-08-10 01:48:12.418 I Initializing core RPC server...
2021-08-10 01:48:12.418 I Binding on 127.0.0.1 (IPv4):18081
2021-08-10 01:48:13.375 I core RPC server initialized OK on port: 18081
2021-08-10 01:48:13.376 I Starting core RPC server...
2021-08-10 01:48:13.382 I core RPC server started ok
2021-08-10 01:48:13.383 I Starting p2p net loop...
2021-08-10 01:48:14.384 I
2021-08-10 01:48:14.384 I **********************************************************************
2021-08-10 01:48:14.384 I The daemon will start synchronizing with the network. This may take a long time to complete.
2021-08-10 01:48:14.384 I
2021-08-10 01:48:14.384 I You can set the level of process detailization through "set_log <level|categories>" command,
2021-08-10 01:48:14.384 I where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).
2021-08-10 01:48:14.384 I
2021-08-10 01:48:14.384 I Use the "help" command to see the list of available commands.
2021-08-10 01:48:14.384 I Use "help <command>" to see a command's documentation.
2021-08-10 01:48:14.384 I **********************************************************************
2021-08-10 01:48:16.681 I [184.66.235.123:18080 OUT] Sync data returned a new top block candidate: 1306188 -> 2423703 [Your node is 1117515 blocks (4.2 years) behind]
2021-08-10 01:48:16.681 I SYNCHRONIZATION started
2021-08-10 01:48:51.098 I [185.7.77.60:58412 INC] Sync data returned a new top block candidate: 1306188 -> 2423705 [Your node is 1117517 blocks (4.2 years) behind]
2021-08-10 01:48:51.098 I SYNCHRONIZATION started
2021-08-10 01:52:35.208 I [65.128.60.76:18080 OUT] Sync data returned a new top block candidate: 1306188 -> 2423706 [Your node is 1117518 blocks (4.2 years) behind]
2021-08-10 01:52:35.209 I SYNCHRONIZATION started
2021-08-10 01:53:34.092 I Host 65.128.60.76 blocked.
2021-08-10 01:53:51.668 I [135.181.75.19:44948 INC] Sync data returned a new top block candidate: 1306188 -> 2423707 [Your node is 1117519 blocks (4.2 years) behind]
2021-08-10 01:53:51.668 I SYNCHRONIZATION started
2021-08-10 01:54:59.621 I [139.162.225.228:18080 OUT] Sync data returned a new top block candidate: 1306188 -> 2423707 [Your node is 1117519 blocks (4.2 years) behind]
2021-08-10 01:54:59.621 I SYNCHRONIZATION started
2021-08-10 01:55:31.545 I [139.162.225.228:18080 OUT] Sync data returned a new top block candidate: 1306188 -> 2423708 [Your node is 1117520 blocks (4.2 years) behind]
2021-08-10 01:55:31.545 I SYNCHRONIZATION started
2021-08-10 01:55:53.213 I [75.186.47.240:58819 INC] Sync data returned a new top block candidate: 1306188 -> 2423709 [Your node is 1117521 blocks (4.2 years) behind]
2021-08-10 01:55:53.213 I SYNCHRONIZATION started
2021-08-10 01:57:01.774 I [192.110.160.146:39334 INC] Sync data returned a new top block candidate: 1306188 -> 2423710 [Your node is 1117522 blocks (4.2 years) behind]
2021-08-10 01:57:01.774 I SYNCHRONIZATION started
2021-08-10 01:57:17.442 I [batch] DB resize needed
2021-08-10 01:57:17.457 I LMDB Mapsize increased.  Old: 17306MiB, New: 24131MiB
2021-08-10 01:57:52.952 I Synced 1306208/2423710 (53%, 1117502 left)
2021-08-10 01:57:55.536 I [45.78.183.59:10235 INC] Sync data returned a new top block candidate: 1306208 -> 2423711 [Your node is 1117503 blocks (4.2 years) behind]
2021-08-10 01:57:55.536 I SYNCHRONIZATION started
2021-08-10 01:58:14.080 I Synced 1306228/2423711 (53%, 1117483 left)
2021-08-10 01:58:33.579 I Host 117.20.65.179 blocked.
2021-08-10 01:59:14.529 I [139.162.225.228:18080 OUT] Sync data returned a new top block candidate: 1306228 -> 2423711 [Your node is 1117483 blocks (4.2 years) behind]
2021-08-10 01:59:14.530 I SYNCHRONIZATION started

I guess just 40 blocks were synced. Should I switch to the 20 block standard again?


## selsta | 2021-08-10T02:04:58+00:00
> I guess just 40 blocks were synced. Should I switch to the 20 block standard again?

what do you mean here?

## sumariva | 2021-08-10T02:07:07+00:00
My normal configuration is 100 for the block sync size. Could be this causing hosts to be blocked? I trying to speed up the sync.

## selsta | 2021-08-10T02:07:51+00:00
Yes, this could be the reason, that's why I suggested without any settings.

## selsta | 2021-08-10T02:08:37+00:00
At some point you are requesting too much data from a node at once and so it fails.

## sumariva | 2021-08-10T02:09:49+00:00
OK, will try to increase to 50 blocks and 16 nodes again. If I found many more blocked hosts will report. Thanks.

## selsta | 2021-08-10T02:11:10+00:00
Honestly, I would just sync without changing --block-sync-size and without --limit-up/down

There won't be much speed difference anyway.

## sumariva | 2021-08-10T02:17:18+00:00
I imagined that if monerod found a good peer, with a larger block size it could maximize speed reusing this same available peer. I do not know how the peer's pool handles the reconnect after a block is synced.

## selsta | 2021-08-10T02:19:30+00:00
Most time is spent on verification, not network.

## sumariva | 2021-08-10T02:32:40+00:00
With a block size of 50 got some more hosts blocked.
Switched back to 20 and blocks are syncing again.
Using max --out-peers 16.

## selsta | 2021-08-13T03:57:37+00:00
Closing as the issue seems resolved by using a smaller block size.

# Action History
- Created by: dremil | 2021-03-11T13:31:54+00:00
- Closed at: 2021-08-13T03:57:37+00:00
