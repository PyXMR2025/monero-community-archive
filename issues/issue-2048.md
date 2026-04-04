---
title: OSX GUI seems to be stuck on block 1288616 during sync
source_url: https://github.com/monero-project/monero/issues/2048
author: pinheadmz
assignees: []
labels: []
created_at: '2017-05-25T15:59:11+00:00'
updated_at: '2017-05-26T01:42:44+00:00'
type: issue
status: closed
closed_at: '2017-05-26T01:42:44+00:00'
---

# Original Description
GUI sync progress bar says "1288616/1317967". Log is below. I had gotten stuck on (I'm pretty sure) the exact same block yesterday, so I tried using the `pop-blocks` command [I found here](https://monero.stackexchange.com/questions/3977/monerod-cant-synchronize), but now I appear to be stuck in the same place again (numbers aren't progressing, no new lines in log file, etc.)

```
2017-May-25 07:29:43.935982 Monero 'Wolfram Warptangent' (v0.10.1.0-dd580d7b)
2017-May-25 07:29:43.937238 Initializing cryptonote protocol...
2017-May-25 07:29:43.937285 Cryptonote protocol initialized OK
2017-May-25 07:29:43.937395 Initializing p2p server...
2017-May-25 07:29:44.386809 DNS seed node lookup either timed out or failed, falling back to defaults
2017-May-25 07:29:44.388474 Set limit-up to 2048 kB/s
2017-May-25 07:29:44.388533 Set limit-down to 8192 kB/s
2017-May-25 07:29:44.388567 Set limit-up to 2048 kB/s
2017-May-25 07:29:44.388609 Set limit-down to 8192 kB/s
2017-May-25 07:29:44.394543 Binding on 0.0.0.0:18080
2017-May-25 07:29:44.394765 Net service bound to 0.0.0.0:18080
2017-May-25 07:29:44.394791 Attempting to add IGD port mapping.
2017-May-25 07:29:49.479949 UPnP device was found but not recognized as IGD.
2017-May-25 07:29:49.480000 P2p server initialized OK
2017-May-25 07:29:49.480037 Initializing core rpc server...
2017-May-25 07:29:49.480088 Binding on 127.0.0.1:18081
2017-May-25 07:29:49.480285 Core rpc server initialized OK on port: 18081
2017-May-25 07:29:49.480319 Initializing core...
2017-May-25 07:29:49.553319 Loading blockchain from folder /Users/pinhead/.bitmonero/lmdb ...
2017-May-25 07:29:49.553385 option: fast
2017-May-25 07:29:49.553402 option: async
2017-May-25 07:29:49.553416 option: 1000
2017-May-25 07:29:49.682412 Blockchain initialized. last block: 1288615, d40.h20.m50.s4 time ago, current difficulty: 9718310133
2017-May-25 07:29:50.214254 WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-May-25 07:29:50.231413 Core initialized OK
2017-May-25 07:29:50.231466 Starting core rpc server...
2017-May-25 07:29:50.231484 Run net_service loop( 2 threads)...
2017-May-25 07:29:50.231812 [SRV_MAIN]Core rpc server started ok
2017-May-25 07:29:50.231990 [SRV_MAIN]Starting p2p net loop...
2017-May-25 07:29:50.232067 [SRV_MAIN]Run net_service loop( 10 threads)...
2017-May-25 07:29:51.235708 [P2P1]
**********************************************************************
The daemon will start synchronizing with the network. It may take up to several hours.

You can set the level of process detailization* through "set_log <level>" command*, where <level> is between 0 (no details) and 4 (very verbose).

Use "help" command to see the list of available commands.

Note: in case you need to interrupt the process, use "exit" command. Otherwise, the current progress won't be saved.
**********************************************************************
2017-May-25 07:30:08.024333 [P2P3]
**********************************************************************
You are now synchronized with the network. You may now start monero-wallet-cli.

Please note, that the blockchain will be saved only after you quit the daemon with "exit" command or if you use "save" command.
Otherwise, you will possibly need to synchronize the blockchain again.

Use "help" command to see the list of available commands.
**********************************************************************
2017-May-25 07:30:19.222634 [P2P4][181.41.201.170:18080 OUT]Sync data returned a new top block candidate: 1288616 -> 1317955 [Your node is 29339 blocks (40 days) behind] 
SYNCHRONIZATION started
2017-May-25 07:30:26.110062 [P2P8][124.170.124.167:18080 OUT]Sync data returned a new top block candidate: 1288616 -> 1317955 [Your node is 29339 blocks (40 days) behind] 
SYNCHRONIZATION started
2017-May-25 07:30:27.053964 [P2P2][223.18.70.235:18080 OUT]Sync data returned a new top block candidate: 1288616 -> 1317955 [Your node is 29339 blocks (40 days) behind] 
SYNCHRONIZATION started
2017-May-25 07:30:27.833984 [P2P7][194.96.181.126:18080 OUT]Sync data returned a new top block candidate: 1288616 -> 1317955 [Your node is 29339 blocks (40 days) behind] 
SYNCHRONIZATION started
2017-May-25 07:30:29.386700 [P2P7][70.24.212.190:18080 OUT]Sync data returned a new top block candidate: 1288616 -> 1317955 [Your node is 29339 blocks (40 days) behind] 
SYNCHRONIZATION started
2017-May-25 07:30:45.470450 [P2P2][24.222.163.146:18080 OUT]Sync data returned a new top block candidate: 1288616 -> 1316216 [Your node is 27600 blocks (38 days) behind] 
SYNCHRONIZATION started
2017-May-25 07:31:02.041971 [P2P8][210.6.175.44:18080 OUT]Sync data returned a new top block candidate: 1288616 -> 1317955 [Your node is 29339 blocks (40 days) behind] 
SYNCHRONIZATION started
2017-May-25 07:31:38.701189 [P2P1][89.177.38.60:18080 OUT]Sync data returned a new top block candidate: 1288616 -> 1317955 [Your node is 29339 blocks (40 days) behind] 
SYNCHRONIZATION started
2017-May-25 07:32:01.823908 [P2P0][104.218.50.245:18080 OUT]Sync data returned a new top block candidate: 1288616 -> 1317956 [Your node is 29340 blocks (40 days) behind] 
SYNCHRONIZATION started
2017-May-25 07:32:02.601208 [P2P8][217.182.73.97:18080 OUT]Sync data returned a new top block candidate: 1288616 -> 1317956 [Your node is 29340 blocks (40 days) behind] 
SYNCHRONIZATION started
2017-May-25 07:32:42.899625 [P2P2][160.202.163.118:18080 OUT]Sync data returned a new top block candidate: 1288616 -> 1317956 [Your node is 29340 blocks (40 days) behind] 
SYNCHRONIZATION started
2017-May-25 07:33:19.629020 [P2P1][218.90.115.84:18080 OUT]Sync data returned a new top block candidate: 1288616 -> 1317956 [Your node is 29340 blocks (40 days) behind] 
SYNCHRONIZATION started
2017-May-25 07:33:28.617554 [P2P0][112.64.117.224:18080 OUT]Sync data returned a new top block candidate: 1288616 -> 1317956 [Your node is 29340 blocks (40 days) behind] 
SYNCHRONIZATION started
2017-May-25 07:33:55.528178 [P2P2][82.221.111.100:18080 OUT]Sync data returned a new top block candidate: 1288616 -> 1317957 [Your node is 29341 blocks (40 days) behind] 
SYNCHRONIZATION started
2017-May-25 07:34:31.255139 [P2P8][14.207.87.226:18080 OUT]Sync data returned a new top block candidate: 1288616 -> 1317616 [Your node is 29000 blocks (40 days) behind] 
SYNCHRONIZATION started
2017-May-25 07:35:33.624936 [P2P2][198.255.38.244:18080 OUT]Sync data returned a new top block candidate: 1288616 -> 1317824 [Your node is 29208 blocks (40 days) behind] 
SYNCHRONIZATION started
2017-May-25 07:35:48.881061 [P2P5][69.85.99.149:18080 OUT]Sync data returned a new top block candidate: 1288616 -> 1317958 [Your node is 29342 blocks (40 days) behind] 
SYNCHRONIZATION started
2017-May-25 07:36:01.231322 [P2P0][73.226.35.69:18080 OUT]Sync data returned a new top block candidate: 1288616 -> 1317958 [Your node is 29342 blocks (40 days) behind] 
SYNCHRONIZATION started
2017-May-25 07:36:07.453882 [P2P2][73.203.12.111:18080 OUT]Sync data returned a new top block candidate: 1288616 -> 1317958 [Your node is 29342 blocks (40 days) behind] 
SYNCHRONIZATION started
2017-May-25 07:36:42.586559 [P2P9][75.162.113.78:18080 OUT]Sync data returned a new top block candidate: 1288616 -> 1317958 [Your node is 29342 blocks (40 days) behind] 
SYNCHRONIZATION started
2017-May-25 07:37:03.284964 [P2P7][171.224.18.75:18080 OUT]Sync data returned a new top block candidate: 1288616 -> 1317958 [Your node is 29342 blocks (40 days) behind] 
SYNCHRONIZATION started
2017-May-25 07:37:39.673171 [P2P0][98.28.121.231:18080 OUT]Sync data returned a new top block candidate: 1288616 -> 1317959 [Your node is 29343 blocks (40 days) behind] 
SYNCHRONIZATION started
2017-May-25 07:37:40.272450 [P2P8][95.172.167.228:18080 OUT]Sync data returned a new top block candidate: 1288616 -> 1317959 [Your node is 29343 blocks (40 days) behind] 
SYNCHRONIZATION started
2017-May-25 07:38:05.408928 [P2P5][78.132.85.218:18080 OUT]Sync data returned a new top block candidate: 1288616 -> 1317415 [Your node is 28799 blocks (39 days) behind] 
SYNCHRONIZATION started
2017-May-25 07:40:18.977007 [P2P5][5.9.99.230:18080 OUT]Sync data returned a new top block candidate: 1288616 -> 1317959 [Your node is 29343 blocks (40 days) behind] 
SYNCHRONIZATION started
2017-May-25 07:40:19.616548 [P2P9][173.25.137.165:18080 OUT]Sync data returned a new top block candidate: 1288616 -> 1317959 [Your node is 29343 blocks (40 days) behind] 
SYNCHRONIZATION started
2017-May-25 07:41:07.207099 [P2P3][54.223.133.248:18080 OUT]Sync data returned a new top block candidate: 1288616 -> 1317959 [Your node is 29343 blocks (40 days) behind] 
SYNCHRONIZATION started
2017-May-25 07:41:07.449437 [P2P3][46.183.145.69:18080 OUT]Sync data returned a new top block candidate: 1288616 -> 1317959 [Your node is 29343 blocks (40 days) behind] 
SYNCHRONIZATION started
2017-May-25 07:42:31.939550 [P2P7][62.176.6.94:18080 OUT]Sync data returned a new top block candidate: 1288616 -> 1317959 [Your node is 29343 blocks (40 days) behind] 
SYNCHRONIZATION started
2017-May-25 07:43:06.776331 [P2P5][2.7.132.146:18080 OUT]Sync data returned a new top block candidate: 1288616 -> 1317960 [Your node is 29344 blocks (40 days) behind] 
SYNCHRONIZATION started
2017-May-25 07:43:18.083027 [P2P3][82.181.28.205:18080 OUT]Sync data returned a new top block candidate: 1288616 -> 1317960 [Your node is 29344 blocks (40 days) behind] 
SYNCHRONIZATION started
2017-May-25 07:43:54.467189 [P2P7][85.5.27.78:18080 OUT]Sync data returned a new top block candidate: 1288616 -> 1317960 [Your node is 29344 blocks (40 days) behind] 
SYNCHRONIZATION started
2017-May-25 07:44:57.269489 [P2P7][94.46.164.183:18080 OUT]Sync data returned a new top block candidate: 1288616 -> 1317960 [Your node is 29344 blocks (40 days) behind] 
SYNCHRONIZATION started
2017-May-25 07:46:47.584346 [P2P8][198.100.144.155:18080 OUT]Sync data returned a new top block candidate: 1288616 -> 1317964 [Your node is 29348 blocks (40 days) behind] 
SYNCHRONIZATION started
2017-May-25 07:49:25.841486 [P2P1][71.82.221.0:18080 OUT]Sync data returned a new top block candidate: 1288616 -> 1317967 [Your node is 29351 blocks (40 days) behind] 
SYNCHRONIZATION started
2017-May-25 07:51:18.584774 [P2P5][121.42.157.248:18080 OUT]Sync data returned a new top block candidate: 1288616 -> 1317968 [Your node is 29352 blocks (40 days) behind] 
SYNCHRONIZATION started
```

# Discussion History
## hyc | 2017-05-25T16:02:36+00:00
Your daemon is out of date. Current version is 0.10.3.1. There's no bug here.

## pinheadmz | 2017-05-25T16:04:24+00:00
Oh thanks! I just downloaded the GUI yesterday from https://getmonero.org/2017/03/29/monero-gui-beta-2-released.html but I have used the command line daemon and simple-wallet before. Is there a way to update the daemon and still run the GUI? 

edit: looks like, is it possible that the OSX GUI release did not get the updated daemon for the most recent hard fork? The file I downloaded has the correct version number, but see my log above:

https://downloads.getmonero.org/gui/monero-gui-mac-x64-v0.10.3.1.tar.bz2

## Jaqueeee | 2017-05-25T20:58:46+00:00
@pinheadmz  When i run the daemon included in that download you linked i'm getting the correct version number. Are you sure you're not running an old version of monerod?

```
$ cd monero-gui-0.10.3.1-beta2/monero-wallet-gui.app/Contents/MacOS/
$ ./monerod 
2017-05-25 22:56:51.718		INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
2017-05-25 22:56:51.727		INFO 	global	src/daemon/main.cpp:282	Monero 'Wolfram Warptangent' (v0.10.3.1-release)
2017-05-25 22:56:51.728		INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2017-05-25 22:56:51.728		INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
2017-05-25 22:56:51.728		INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
```

## pinheadmz | 2017-05-25T21:12:16+00:00
Well I just double-clicked the app after downloading from that link. However, I do have older versions of monerod on the same computer. Could the app be running that instead of the daemon included in the package? My log says version 0.10.1, which looks like it was released Dec 2016, but I actually don't think I've downloaded new monero software since then, so I'm not sure why 0.10.1 would even be installed. Maybe that's the last version I ran. I'll try deleting it and restarting the app.

## pinheadmz | 2017-05-26T01:42:44+00:00
My fault, I downloaded GUI beta 1 by accident. Thanks!

# Action History
- Created by: pinheadmz | 2017-05-25T15:59:11+00:00
- Closed at: 2017-05-26T01:42:44+00:00
