---
title: '"Daemon failed to start" '
source_url: https://github.com/monero-project/monero-gui/issues/890
author: gitmehubscotty
assignees: []
labels:
- invalid
created_at: '2017-09-22T18:36:24+00:00'
updated_at: '2022-05-21T23:15:37+00:00'
type: issue
status: closed
closed_at: '2019-04-27T01:00:37+00:00'
---

# Original Description
Hi guys, 
Monero keeps giving me this message when I try to setup localhost:18081
"Daemon failed to start.
Please check your wallet and daemon log for errors. You can also try to start monerod.exe manually."
![unbenannt](https://user-images.githubusercontent.com/32205357/30758744-e2891180-9fd3-11e7-87cb-0fe3573fcc1a.PNG)
![unbenannt2](https://user-images.githubusercontent.com/32205357/30759116-42f3fb2e-9fd5-11e7-8ae7-4f0f73fd6ed5.PNG)

- I am running Windows 10 64 bit
- I installed from https://getmonero.org/downloads/ -> Windows, 64-bit -> Version: 0.11.0.0 Helium Hydra
- I use "localhost" and "18081" as daemon adress
- My folder contains no spaces: "G:\MoneroGui2"
- It used to be "MoneroGUI", I tried renaming it to "MoneroGui2", does not help
- I just moved to a SSD drive, maybe that helps
- The data.mdb currently has ~25GB. 
- Sometimes it does connect, sometimes it doesn't
- When it does work, I have been waiting for days to synchronize and it never seemed to synchronize 100%
- Starting monerod.exe leads to "Synchronization started" and shortly after to a windows fail message and I have to close the program
- I'm just an average joe, I have no programming knowledge
- Sadly I am not convinced that Monero is ready yet for mass adoption like this, but I see great potential and I thank everyone who developed it

Sincerely


# Discussion History
## gitmehubscotty | 2017-09-22T19:00:04+00:00
2017-09-22 18:41:50.954	1060	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-09-22 18:41:51.960	1060	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081

## dEBRUYNE-1 | 2017-09-23T20:10:50+00:00
Could you paste the last 100 lines or so of `bitmonero.log` (on Windows it's located in `C:\ProgramData\bitmonero`) to https://paste.fedoraproject.org? Note that this folder, by default, is hidden. Therefore, you have to manually enter aforementioned path into the explorer.

## gitmehubscotty | 2017-09-24T09:20:08+00:00
Thank you. 
https://paste.fedoraproject.org/paste/EMXdnKZT7h6LrrobRbW-Lg


## dEBRUYNE-1 | 2017-09-24T15:52:13+00:00
Could you try the following steps:

1. Close the GUI and make sure to close the daemon as well.

2. Reboot to ensure no Monero related processes are running anymore.

3. Delete `p2pstate.bin` (it's in `C:\ProgramData\bitmonero`). 

4. Browse to the directory `monero-wallet-gui.exe` is located.

5. Open `monerod.exe` (from that directory) manually by double clicking on it.

6. Periodically check the status of the sync with the `status` command. The block height should be equal to the block height displayed on, for instance, this [block explorer](https://xmrchain.net/). 

7. When it's fully synced, open `monero-wallet-gui.exe`.

-------------------------

If `monerod.exe` crashes at step 5, start it with the `--log-level 1` flag from the command line. This is done as follows. Go to the folder `monerod.exe` is located and make sure your cursor isn't located on any of the files. Subsequently do SHIFT + right click and it will give you an option to "Open command window here". Lastly, type the following command:

`monerod.exe --log-level 1`

Lastly, again paste the laste 100 lines or so from `bitmonero.log`.

## gitmehubscotty | 2017-09-24T19:46:51+00:00
I did steps 1 to 5. No crash so far. Sync in process. I'll let it run and report again tomorrow.

Thanks!!!

## gitmehubscotty | 2017-09-25T06:14:27+00:00
Unfortunately no success. Monerod.exe works now and I am fully synced, but I get the same error message in the GUI.
LOG:
https://paste.fedoraproject.org/paste/KCxuQDMevc4wiBTcIUVDcQ

## dEBRUYNE-1 | 2017-09-25T23:23:35+00:00
That's the log from `bitmonero.log` right? Could you also paste the last 100 lines or so of  `monero-wallet-gui.log`? It's in the same directory as `monero-wallet-gui.exe`. 

## medusadigital | 2017-09-26T13:58:44+00:00
hei @gitmehubscotty 

-start monerod.exe
-start GUI
-edit setting to localhost and Port 18081
-hit connect

what happens ? 
if that doesnt work, pls post monero-wallet-gui.log

## gitmehubscotty | 2017-09-28T20:38:28+00:00
So I did this: 
"-start monerod.exe
-start GUI
-edit setting to localhost and Port 18081
-hit connect"
and it seems daemon was already running (due to monerod.exe being open?) and therefore there was no connection error :-)
Now it's synchronizing and daemon seems to be running, because "Start daemon" is now an inactive button.

I copied the monero-wallet-gui.log anyway here:
https://paste.fedoraproject.org/paste/EuWYcChUk1DA7HEBkASczA

So is the idea to keep monerod.exe and the GUI running in parallel?

## SA-chron | 2017-10-16T01:56:15+00:00
Having the same issue after a crash. Any way of recovering the data or would I have to download the blockchain again?

## dEBRUYNE-1 | 2017-10-17T14:38:00+00:00
>So is the idea to keep monerod.exe and the GUI running in parallel?

@gitmehubscotty: If that works properly for you, just run it that way. 

------

>Having the same issue after a crash. Any way of recovering the data or would I have to download the blockchain again?

@jb241: If you incurred a system crash, your blockchain is most likely corrupt. You can trigger a resync from scratch by deleting C:\ProgramData\bitmonero (Windows) or ~/.bitmonero (Mac OS X & Linux). 

## dEBRUYNE-1 | 2017-10-27T13:46:28+00:00
Could you guys try v0.11.1.0 if you still have issues?

## gitmehubscotty | 2017-11-02T19:37:16+00:00
Downloaded GUI version: v0.11.1.0
Unfortunately still the same issue: Daemon failed to start. This happesn when monerod.exe is not running in parallel.
It still works fine if run monerod.exe in parallel.

## Spartan-Hex-Shadow | 2017-11-13T04:35:32+00:00
I am having the same issue. Here is my error log with the first 100 lines:
2017-11-12 06:30:49.853	3100	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 06:30:50.932	3100	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-12 06:30:56.933	12328	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 06:30:56.934	12328	INFO 	global	src/daemon/main.cpp:279	Monero 'Helium Hydra' (v0.11.1.0-release)
2017-11-12 06:30:56.934	12328	INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2017-11-12 06:30:56.934	12328	INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
2017-11-12 06:30:56.936	12328	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2017-11-12 06:30:58.727	12328	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2017-11-12 06:30:58.727	12328	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
2017-11-12 06:30:58.728	12328	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:70	Binding on 127.0.0.1:18081
2017-11-12 06:30:58.729	12328	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2017-11-12 06:30:58.729	12328	INFO 	global	src/daemon/core.h:73	Initializing core...
2017-11-12 06:30:58.730	12328	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:323	Loading blockchain from folder C:\ProgramData\bitmonero\lmdb ...
2017-11-12 06:30:58.759	12328	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1155	LMDB memory map needs to be resized, doing that now.
2017-11-12 06:30:58.759	12328	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:494	LMDB Mapsize increased.  Old: 36263MiB, New: 37287MiB
2017-11-12 06:30:58.940	1472	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 06:31:12.738	1472	ERROR	net.http	contrib/epee/include/net/http_client.h:444	Unexpected recv fail
2017-11-12 06:31:12.738	1472	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-12 06:31:14.806	7672	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 06:31:15.811	7672	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-12 06:31:17.878	10732	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 06:31:18.884	10732	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-12 06:31:20.956	11452	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 06:31:22.044	11452	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-12 06:31:24.121	3360	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 06:31:25.126	3360	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-12 06:31:27.199	10060	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 06:31:28.206	10060	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-12 06:31:53.318	10580	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 06:31:54.466	10580	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-12 06:31:59.218	2376	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 06:31:59.218	2376	INFO 	global	src/daemon/main.cpp:279	Monero 'Helium Hydra' (v0.11.1.0-release)
2017-11-12 06:31:59.219	2376	INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2017-11-12 06:31:59.219	2376	INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
2017-11-12 06:31:59.220	2376	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2017-11-12 06:32:00.832	2376	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2017-11-12 06:32:00.832	2376	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
2017-11-12 06:32:00.832	2376	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:70	Binding on 127.0.0.1:18081
2017-11-12 06:32:00.833	2376	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2017-11-12 06:32:00.833	2376	INFO 	global	src/daemon/core.h:73	Initializing core...
2017-11-12 06:32:00.833	2376	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:323	Loading blockchain from folder C:\ProgramData\bitmonero\lmdb ...
2017-11-12 06:32:00.845	2376	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1155	LMDB memory map needs to be resized, doing that now.
2017-11-12 06:32:00.848	2376	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:494	LMDB Mapsize increased.  Old: 36263MiB, New: 37287MiB
2017-11-12 06:32:01.226	8420	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 06:32:13.282	8420	ERROR	net.http	contrib/epee/include/net/http_client.h:444	Unexpected recv fail
2017-11-12 06:32:13.282	8420	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-12 06:32:15.349	11492	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 06:32:16.365	11492	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-12 06:32:18.433	11444	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 06:32:19.437	11444	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-12 06:32:21.506	10952	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 06:32:22.511	10952	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-12 06:32:24.581	3816	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 06:32:25.588	3816	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-12 06:32:27.658	1888	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 06:32:28.728	1888	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-12 06:32:30.800	3208	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 06:32:31.805	3208	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-12 06:32:42.334	11696	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 06:32:43.337	11696	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-12 06:33:00.782	10108	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 06:33:00.782	10108	INFO 	global	src/daemon/main.cpp:279	Monero 'Helium Hydra' (v0.11.1.0-release)
2017-11-12 07:14:01.939	9572	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 07:14:02.940	9572	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-12 07:14:08.799	13984	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 07:14:08.800	13984	INFO 	global	src/daemon/main.cpp:279	Monero 'Helium Hydra' (v0.11.1.0-release)
2017-11-12 07:14:08.800	13984	INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2017-11-12 07:14:08.800	13984	INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
2017-11-12 07:14:08.802	13984	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2017-11-12 07:14:10.804	9372	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 07:14:11.807	9372	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-12 07:14:13.842	9812	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 07:14:14.845	9812	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-12 07:14:15.647	13984	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2017-11-12 07:14:15.648	13984	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
2017-11-12 07:14:15.648	13984	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:70	Binding on 127.0.0.1:18081
2017-11-12 07:14:15.649	13984	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2017-11-12 07:14:15.649	13984	INFO 	global	src/daemon/core.h:73	Initializing core...
2017-11-12 07:14:15.649	13984	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:323	Loading blockchain from folder C:\ProgramData\bitmonero\lmdb ...
2017-11-12 07:14:15.669	13984	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1155	LMDB memory map needs to be resized, doing that now.
2017-11-12 07:14:15.669	13984	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:494	LMDB Mapsize increased.  Old: 36263MiB, New: 37287MiB
2017-11-12 07:14:16.876	2188	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 07:14:28.035	2188	ERROR	net.http	contrib/epee/include/net/http_client.h:444	Unexpected recv fail
2017-11-12 07:14:28.035	2188	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-12 07:14:30.067	13516	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 07:14:31.073	13516	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-12 07:14:33.105	13828	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 07:14:34.109	13828	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-12 07:14:36.142	1132	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 07:14:37.146	1132	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-12 07:14:39.175	1424	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 07:14:40.177	1424	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-12 14:05:24.828	12376	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 14:05:24.829	12376	INFO 	global	src/daemon/main.cpp:279	Monero 'Helium Hydra' (v0.11.1.0-release)
2017-11-12 14:05:24.829	12376	INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2017-11-12 14:05:24.829	12376	INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
2017-11-12 14:05:24.830	12376	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2017-11-12 14:05:26.757	12376	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2017-11-12 14:05:26.757	12376	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
2017-11-12 14:05:26.758	12376	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:70	Binding on 127.0.0.1:18081
2017-11-12 14:05:26.758	12376	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2017-11-12 14:05:26.759	12376	INFO 	global	src/daemon/core.h:73	Initializing core...
2017-11-12 14:05:26.759	12376	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:323	Loading blockchain from folder C:\ProgramData\bitmonero\lmdb ...
2017-11-12 14:05:26.767	12376	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1155	LMDB memory map needs to be resized, doing that now.
2017-11-12 14:05:26.767	12376	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:494	LMDB Mapsize increased.  Old: 36263MiB, New: 37287MiB
2017-11-12 14:05:26.831	12780	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 14:05:39.390	12780	ERROR	net.http	contrib/epee/include/net/http_client.h:444	Unexpected recv fail
2017-11-12 14:05:39.390	12780	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-12 14:05:41.590	3432	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 14:05:42.593	3432	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-12 14:05:44.745	5868	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 14:05:45.941	5868	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-12 14:05:47.997	11924	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 14:05:49.019	11924	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-12 14:05:51.071	11872	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 14:05:52.074	11872	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-12 14:05:54.151	1680	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 14:05:55.153	1680	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-12 14:08:19.786	8276	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 14:08:20.789	8276	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-12 14:10:37.056	8296	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 14:10:38.062	8296	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-12 20:20:21.518	3800	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 20:20:22.522	3800	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-12 20:20:28.392	13004	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 20:20:28.392	13004	INFO 	global	src/daemon/main.cpp:279	Monero 'Helium Hydra' (v0.11.1.0-release)
2017-11-12 20:20:28.393	13004	INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2017-11-12 20:20:28.393	13004	INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
2017-11-12 20:20:28.394	13004	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2017-11-12 20:20:30.210	13004	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2017-11-12 20:20:30.210	13004	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
2017-11-12 20:20:30.211	13004	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:70	Binding on 127.0.0.1:18081
2017-11-12 20:20:30.211	13004	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2017-11-12 20:20:30.212	13004	INFO 	global	src/daemon/core.h:73	Initializing core...
2017-11-12 20:20:30.212	13004	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:323	Loading blockchain from folder C:\ProgramData\bitmonero\lmdb ...
2017-11-12 20:20:30.230	13004	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1155	LMDB memory map needs to be resized, doing that now.
2017-11-12 20:20:30.230	13004	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:494	LMDB Mapsize increased.  Old: 36263MiB, New: 37287MiB
2017-11-12 20:20:30.395	8344	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 20:20:42.382	8344	ERROR	net.http	contrib/epee/include/net/http_client.h:444	Unexpected recv fail
2017-11-12 20:20:42.382	8344	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-12 20:20:44.417	9296	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 20:20:45.420	9296	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-12 20:20:47.450	9352	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 20:20:48.452	9352	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-12 20:20:50.482	8580	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 20:20:51.484	8580	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-12 20:20:53.515	8188	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 20:20:54.516	8188	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-12 20:20:56.546	4408	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 20:20:57.548	4408	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-12 20:20:59.580	10116	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 20:21:00.581	10116	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-12 20:38:29.089	8320	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 20:38:30.092	8320	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-12 20:41:01.030	15116	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 20:41:02.032	15116	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-12 20:41:07.901	2072	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 20:41:07.902	2072	INFO 	global	src/daemon/main.cpp:279	Monero 'Helium Hydra' (v0.11.1.0-release)
2017-11-12 20:41:07.902	2072	INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2017-11-12 20:41:07.902	2072	INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
2017-11-12 20:41:07.904	2072	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2017-11-12 20:41:09.906	4624	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 20:41:10.909	4624	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-12 20:41:12.940	8760	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 20:41:13.941	8760	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-12 20:41:14.631	2072	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2017-11-12 20:41:14.631	2072	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
2017-11-12 20:41:14.632	2072	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:70	Binding on 127.0.0.1:18081
2017-11-12 20:41:14.632	2072	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2017-11-12 20:41:14.632	2072	INFO 	global	src/daemon/core.h:73	Initializing core...
2017-11-12 20:41:14.633	2072	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:323	Loading blockchain from folder C:\ProgramData\bitmonero\lmdb ...
2017-11-12 20:41:14.654	2072	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1155	LMDB memory map needs to be resized, doing that now.
2017-11-12 20:41:14.654	2072	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:494	LMDB Mapsize increased.  Old: 36263MiB, New: 37287MiB
2017-11-12 20:41:15.971	1552	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 20:41:28.345	1552	ERROR	net.http	contrib/epee/include/net/http_client.h:444	Unexpected recv fail
2017-11-12 20:41:28.346	1552	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-12 20:41:30.408	15104	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 20:41:31.412	15104	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-12 20:41:33.475	1020	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 20:41:34.478	1020	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-12 20:41:36.547	13544	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 20:41:37.564	13544	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-12 20:41:39.627	13504	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 20:41:40.854	13504	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-12 20:53:42.200	9180	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 20:53:43.218	9180	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-12 20:53:49.126	13064	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 20:53:49.128	13064	INFO 	global	src/daemon/main.cpp:279	Monero 'Helium Hydra' (v0.11.1.0-release)
2017-11-12 20:53:49.130	13064	INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2017-11-12 20:53:49.130	13064	INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
2017-11-12 20:53:49.133	13064	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2017-11-12 20:53:51.132	13500	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 20:53:52.136	13500	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-12 20:53:53.865	13064	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2017-11-12 20:53:53.871	13064	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
2017-11-12 20:53:53.873	13064	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:70	Binding on 127.0.0.1:18081
2017-11-12 20:53:53.874	13064	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2017-11-12 20:53:53.874	13064	INFO 	global	src/daemon/core.h:73	Initializing core...
2017-11-12 20:53:53.875	13064	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:323	Loading blockchain from folder C:\ProgramData\bitmonero\lmdb ...
2017-11-12 20:53:53.901	13064	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1155	LMDB memory map needs to be resized, doing that now.
2017-11-12 20:53:53.901	13064	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:494	LMDB Mapsize increased.  Old: 36263MiB, New: 37287MiB
2017-11-12 20:53:54.189	9176	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 20:54:17.097	9176	ERROR	net.http	contrib/epee/include/net/http_client.h:444	Unexpected recv fail
2017-11-12 20:54:17.098	9176	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-12 20:54:19.157	3716	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 20:54:20.161	3716	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-12 22:11:52.762	812	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-12 22:11:53.768	812	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-13 04:23:46.465	2740	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-13 04:23:46.465	2740	INFO 	global	src/daemon/main.cpp:279	Monero 'Helium Hydra' (v0.11.1.0-release)
2017-11-13 04:23:46.465	2740	INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2017-11-13 04:23:46.465	2740	INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
2017-11-13 04:23:46.465	2740	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2017-11-13 04:23:48.262	2740	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2017-11-13 04:23:48.262	2740	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
2017-11-13 04:23:48.262	2740	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:70	Binding on 127.0.0.1:18081
2017-11-13 04:23:48.262	2740	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2017-11-13 04:23:48.262	2740	INFO 	global	src/daemon/core.h:73	Initializing core...
2017-11-13 04:23:48.262	2740	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:323	Loading blockchain from folder C:\ProgramData\bitmonero\lmdb ...
2017-11-13 04:23:48.278	2740	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1155	LMDB memory map needs to be resized, doing that now.
2017-11-13 04:23:48.278	2740	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:494	LMDB Mapsize increased.  Old: 36263MiB, New: 37287MiB
2017-11-13 04:24:06.227	12280	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-13 04:24:06.227	12280	INFO 	global	src/daemon/main.cpp:279	Monero 'Helium Hydra' (v0.11.1.0-release)
2017-11-13 04:24:06.227	12280	INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2017-11-13 04:24:06.227	12280	INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
2017-11-13 04:24:06.227	12280	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2017-11-13 04:24:07.680	12280	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2017-11-13 04:24:07.680	12280	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
2017-11-13 04:24:07.680	12280	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:70	Binding on 127.0.0.1:18081
2017-11-13 04:24:07.680	12280	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2017-11-13 04:24:07.680	12280	INFO 	global	src/daemon/core.h:73	Initializing core...
2017-11-13 04:24:07.680	12280	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:323	Loading blockchain from folder C:\ProgramData\bitmonero\lmdb ...
2017-11-13 04:24:07.680	12280	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1155	LMDB memory map needs to be resized, doing that now.
2017-11-13 04:24:07.680	12280	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:494	LMDB Mapsize increased.  Old: 36263MiB, New: 37287MiB
2017-11-13 04:24:32.776	9832	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-13 04:24:33.778	9832	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-13 04:24:36.049	13884	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-13 04:24:36.049	13884	INFO 	global	src/daemon/main.cpp:279	Monero 'Helium Hydra' (v0.11.1.0-release)
2017-11-13 04:24:36.057	13884	INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2017-11-13 04:24:36.057	13884	INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
2017-11-13 04:24:36.059	13884	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2017-11-13 04:24:37.508	13884	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2017-11-13 04:24:37.508	13884	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
2017-11-13 04:24:37.508	13884	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:70	Binding on 127.0.0.1:18081
2017-11-13 04:24:37.509	13884	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2017-11-13 04:24:37.509	13884	INFO 	global	src/daemon/core.h:73	Initializing core...
2017-11-13 04:24:37.509	13884	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:323	Loading blockchain from folder C:\ProgramData\bitmonero\lmdb ...
2017-11-13 04:24:37.511	13884	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1155	LMDB memory map needs to be resized, doing that now.
2017-11-13 04:24:37.512	13884	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:494	LMDB Mapsize increased.  Old: 36263MiB, New: 37287MiB
2017-11-13 04:24:39.653	10740	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-13 04:24:39.653	10740	INFO 	global	src/daemon/main.cpp:279	Monero 'Helium Hydra' (v0.11.1.0-release)
2017-11-13 04:24:39.654	10740	INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2017-11-13 04:24:39.654	10740	INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
2017-11-13 04:24:39.655	10740	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2017-11-13 04:24:41.154	10740	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2017-11-13 04:24:41.154	10740	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
2017-11-13 04:24:41.155	10740	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:70	Binding on 127.0.0.1:18081
2017-11-13 04:24:41.155	10740	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2017-11-13 04:24:41.155	10740	INFO 	global	src/daemon/core.h:73	Initializing core...
2017-11-13 04:24:41.155	10740	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:323	Loading blockchain from folder C:\ProgramData\bitmonero\lmdb ...
2017-11-13 04:24:41.156	10740	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1155	LMDB memory map needs to be resized, doing that now.
2017-11-13 04:24:41.157	10740	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:494	LMDB Mapsize increased.  Old: 36263MiB, New: 37287MiB
2017-11-13 04:24:41.656	2556	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-13 04:24:50.933	2556	ERROR	net.http	contrib/epee/include/net/http_client.h:444	Unexpected recv fail
2017-11-13 04:24:50.933	2556	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-13 04:24:52.966	11400	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-13 04:25:03.368	11400	ERROR	net.http	contrib/epee/include/net/http_client.h:444	Unexpected recv fail
2017-11-13 04:25:03.368	11400	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-13 04:25:05.424	8812	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-13 04:25:06.428	8812	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-13 04:25:08.466	9068	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-13 04:25:09.469	9068	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-13 04:25:11.508	11948	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-13 04:25:12.511	11948	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-13 04:25:27.280	11820	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-13 04:25:28.284	11820	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2017-11-13 04:26:40.970	1684	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-13 04:26:40.970	1684	INFO 	global	src/daemon/main.cpp:279	Monero 'Helium Hydra' (v0.11.1.0-release)
2017-11-13 04:26:40.971	1684	INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2017-11-13 04:26:40.971	1684	INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
2017-11-13 04:26:40.973	1684	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2017-11-13 04:26:42.467	1684	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2017-11-13 04:26:42.467	1684	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
2017-11-13 04:26:42.467	1684	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:70	Binding on 127.0.0.1:18081
2017-11-13 04:26:42.467	1684	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2017-11-13 04:26:42.467	1684	INFO 	global	src/daemon/core.h:73	Initializing core...
2017-11-13 04:26:42.482	1684	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:323	Loading blockchain from folder C:\ProgramData\bitmonero\lmdb ...
2017-11-13 04:26:42.482	1684	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1155	LMDB memory map needs to be resized, doing that now.
2017-11-13 04:26:42.482	1684	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:494	LMDB Mapsize increased.  Old: 36263MiB, New: 37287MiB
2017-11-13 04:30:42.583	14132	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-13 04:30:42.583	14132	INFO 	logging	contrib/epee/src/mlog.cpp:156	New log categories: *:WARNING,global:INFO,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-13 04:30:42.583	14132	INFO 	global	src/daemon/main.cpp:279	Monero 'Helium Hydra' (v0.11.1.0-release)
2017-11-13 04:30:42.583	14132	INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2017-11-13 04:30:42.583	14132	INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
2017-11-13 04:30:42.583	14132	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2017-11-13 04:30:44.052	14132	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2017-11-13 04:30:44.052	14132	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
2017-11-13 04:30:44.052	14132	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:70	Binding on 127.0.0.1:18081
2017-11-13 04:30:44.052	14132	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2017-11-13 04:30:44.052	14132	INFO 	global	src/daemon/core.h:73	Initializing core...
2017-11-13 04:30:44.052	14132	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:323	Loading blockchain from folder C:\ProgramData\bitmonero\lmdb ...
2017-11-13 04:30:44.068	14132	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1155	LMDB memory map needs to be resized, doing that now.
2017-11-13 04:30:44.068	14132	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:494	LMDB Mapsize increased.  Old: 36263MiB, New: 37287MiB

## nobrand | 2017-11-14T19:31:26+00:00
I got the COMMAND_HANDSHAKE Failed, what should I do?

## nobrand | 2017-11-14T22:21:07+00:00
stuck at 1442119

## nobrand | 2017-11-15T11:30:45+00:00
Is this because the monero network is compromised?

## Jaqueeee | 2017-11-15T20:50:35+00:00
@nobrand the Monero network is not compromised. =)
Can you paste your daemon log please?

## BBooch | 2017-11-18T07:44:43+00:00
having the same problem here.  

## nobrand | 2017-11-19T08:03:58+00:00
@Jaqueeee , I already found out that the problem is that- i didn't exit the monerod.exe properly i just click the "x" button. I higly recommend to the Monero team that they must have the blockchain fixer program or something related so that I will not resync again.  But here is the log:
2017-11-18 03:50:38.246	4660	INFO 	logging	contrib/epee/src/mlog.cpp:156	New log categories: *:WARNING,global:INFO,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-18 03:50:38.247	4660	INFO 	global	src/daemon/main.cpp:279	Monero 'Helium Hydra' (v0.11.1.0-release)
2017-11-18 03:50:38.248	4660	INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2017-11-18 03:50:38.249	4660	INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
2017-11-18 03:50:38.250	4660	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2017-11-18 03:50:41.716	4660	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2017-11-18 03:50:41.717	4660	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
2017-11-18 03:50:41.737	4660	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:70	Binding on 127.0.0.1:18081
2017-11-18 03:50:41.739	4660	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2017-11-18 03:50:41.740	4660	INFO 	global	src/daemon/core.h:73	Initializing core...
2017-11-18 03:50:41.741	4660	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:323	Loading blockchain from folder D:\ProgramData\bitmonero\lmdb ...
2017-11-18 03:51:23.255	4660	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:421	Loading checkpoints
2017-11-18 03:51:24.990	4660	WARN 	net.dns	src/common/dns_utils.cpp:487	WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-11-18 03:51:25.904	4660	INFO 	global	src/daemon/core.h:78	Core initialized OK
2017-11-18 03:51:25.906	4660	INFO 	global	src/daemon/rpc.h:68	Starting core rpc server...
2017-11-18 03:51:25.909	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:73	Core rpc server started ok
2017-11-18 03:51:25.911	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:78	Starting p2p net loop...
2017-11-18 03:51:26.912	[P2P7]	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:1258	[1;33m
**********************************************************************
The daemon will start synchronizing with the network. This may take a long time to complete.

You can set the level of process detailization* through "set_log <level|categories>" command*,
where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING)

Use the "help" command to see the list of available commands.
**********************************************************************
[0m
2017-11-18 03:51:32.235	[P2P6]	WARN 	net.p2p	src/p2p/net_node.inl:759	[163.172.182.165:18080 OUT] COMMAND_HANDSHAKE invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2017-11-18 03:51:32.237	[P2P8]	WARN 	net.p2p	src/p2p/net_node.inl:808	[163.172.182.165:18080 OUT] COMMAND_HANDSHAKE Failed
2017-11-18 03:51:37.532	5712	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Height: 1442127/1442127 (100.0%) on mainnet, not mining, net hash 273.45 MH/s, v6, up to date, 1(out)+0(in) connections, uptime 0d 0h 0m 56s
2017-11-18 03:51:47.862	[P2P6]	WARN 	net.p2p	src/p2p/net_node.inl:759	[212.83.172.165:28080 OUT] COMMAND_HANDSHAKE invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2017-11-18 03:51:47.864	[P2P8]	WARN 	net.p2p	src/p2p/net_node.inl:808	[212.83.172.165:28080 OUT] COMMAND_HANDSHAKE Failed
2017-11-18 03:51:48.914	[P2P7]	WARN 	net.dns	src/common/dns_utils.cpp:487	WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-11-18 03:51:49.254	[P2P7]	WARN 	net.p2p	src/p2p/net_node.inl:1629	[212.83.175.67:18080 OUT] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
2017-11-18 03:51:49.299	5712	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Height: 1442127, target: 1442127 (100%)
2017-11-18 03:51:49.300	5712	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Downloading at 3 kB/s
2017-11-18 03:51:49.301	5712	INFO 	msgwriter	src/common/scoped_message_writer.h:102	3 peers
2017-11-18 03:51:49.302	5712	INFO 	msgwriter	src/common/scoped_message_writer.h:102	212.83.175.67:18080       0000000000000000  0  3 kB/s, 0 blocks / 0 MB queued
2017-11-18 03:51:49.303	5712	INFO 	msgwriter	src/common/scoped_message_writer.h:102	212.83.172.165:28080      0000000000000000  0  0 kB/s, 0 blocks / 0 MB queued
2017-11-18 03:51:49.304	5712	INFO 	msgwriter	src/common/scoped_message_writer.h:102	163.172.182.165:18080     0000000000000000  0  0 kB/s, 0 blocks / 0 MB queued
2017-11-18 03:51:49.304	5712	INFO 	msgwriter	src/common/scoped_message_writer.h:102	0 spans, 0 MB
2017-11-18 03:52:01.608	[P2P9]	WARN 	net.p2p	src/p2p/net_node.inl:759	[212.83.172.165:28080 OUT] COMMAND_HANDSHAKE invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2017-11-18 03:52:01.610	[P2P7]	WARN 	net.p2p	src/p2p/net_node.inl:808	[212.83.172.165:28080 OUT] COMMAND_HANDSHAKE Failed
2017-11-18 03:52:03.109	[P2P5]	WARN 	net.p2p	src/p2p/net_node.inl:1629	[212.83.175.67:18080 OUT] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
2017-11-18 03:52:15.611	[P2P5]	WARN 	net.p2p	src/p2p/net_node.inl:759	[163.172.182.165:18080 OUT] COMMAND_HANDSHAKE invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2017-11-18 03:52:15.613	[P2P7]	WARN 	net.p2p	src/p2p/net_node.inl:808	[163.172.182.165:18080 OUT] COMMAND_HANDSHAKE Failed
2017-11-18 03:52:31.362	[P2P5]	WARN 	net.p2p	src/p2p/net_node.inl:759	[212.83.172.165:28080 OUT] COMMAND_HANDSHAKE invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2017-11-18 03:52:31.363	[P2P7]	WARN 	net.p2p	src/p2p/net_node.inl:808	[212.83.172.165:28080 OUT] COMMAND_HANDSHAKE Failed
2017-11-18 03:52:32.732	[P2P7]	WARN 	net.p2p	src/p2p/net_node.inl:1629	[212.83.175.67:18080 OUT] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
2017-11-18 03:52:38.047	[P2P5]	WARN 	net.p2p	src/p2p/net_node.inl:759	[5.9.100.248:18080 OUT] COMMAND_HANDSHAKE invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2017-11-18 03:52:38.050	[P2P7]	WARN 	net.p2p	src/p2p/net_node.inl:808	[5.9.100.248:18080 OUT] COMMAND_HANDSHAKE Failed
2017-11-18 03:52:39.135	[P2P7]	WARN 	net.p2p	src/p2p/net_node.inl:1629	[107.152.130.98:18080 OUT] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
2017-11-18 03:52:41.906	[P2P8]	ERROR	net	contrib/epee/include/net/levin_protocol_handler_async.h:289	[107.152.130.98:18080 OUT] [levin_protocol] -->> start_outer_call failed
2017-11-18 03:52:51.617	[P2P5]	WARN 	net.p2p	src/p2p/net_node.inl:759	[212.83.172.165:28080 OUT] COMMAND_HANDSHAKE invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2017-11-18 03:52:57.086	[P2P9]	WARN 	net.p2p	src/p2p/net_node.inl:808	[212.83.172.165:28080 OUT] COMMAND_HANDSHAKE Failed
2017-11-18 03:52:58.578	[P2P8]	WARN 	net.p2p	src/p2p/net_node.inl:1629	[212.83.175.67:18080 OUT] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
2017-11-18 03:53:00.317	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:305	[106.68.200.20:18080 OUT] Sync data returned a new top block candidate: 1442127 -> 1445340 [Your node is 3213 blocks (4 days) behind] 
SYNCHRONIZATION started
2017-11-18 03:53:03.367	[P2P9]	WARN 	net.p2p	src/p2p/net_node.inl:1629	[116.251.27.111:18080 OUT] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
2017-11-18 03:53:05.697	[P2P7]	ERROR	net	contrib/epee/include/net/levin_protocol_handler_async.h:289	[116.251.27.111:18080 OUT] [levin_protocol] -->> start_outer_call failed
2017-11-18 03:53:06.367	[P2P7]	WARN 	net.p2p	src/p2p/net_node.inl:1195	Failed to connect to any of seed peers, trying fallback seeds
2017-11-18 03:53:06.369	[P2P7]	WARN 	net.p2p	src/p2p/net_node.inl:1206	Failed to connect to any of seed peers, continuing without seeds
2017-11-18 03:53:29.348	[P2P5]	WARN 	net.p2p	src/p2p/net_node.inl:759	[5.69.79.206:18080 OUT] COMMAND_HANDSHAKE invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2017-11-18 03:53:29.350	[P2P7]	WARN 	net.p2p	src/p2p/net_node.inl:808	[5.69.79.206:18080 OUT] COMMAND_HANDSHAKE Failed
2017-11-18 03:53:32.326	5712	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Blockchain saved
2017-11-18 03:53:34.633	[P2P9]	WARN 	net.p2p	src/p2p/net_node.inl:759	[24.3.243.32:18080 OUT] COMMAND_HANDSHAKE invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2017-11-18 03:53:34.634	[P2P7]	WARN 	net.p2p	src/p2p/net_node.inl:808	[24.3.243.32:18080 OUT] COMMAND_HANDSHAKE Failed
2017-11-18 03:53:37.497	5712	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Height: 1442127/1445340 (99.8%) on mainnet, not mining, net hash 273.45 MH/s, v6, up to date, 6(out)+0(in) connections, uptime 0d 0h 2m 56s

P.S.
Our power grid is only compromised =)

## apostnik76 | 2017-11-23T17:35:41+00:00
I just developed seemingly the same problem. Any help will be greatly appreciated. 

here is my log after I deleted p2pstate.bin and started monerod with level 1:

The monerod displayed to following:
`2017-11-23 17:30:11.662	  0x7fff7b2be000	INFO 	global	src/daemon/main.cpp:279	Monero 'Helium Hydra' (v0.11.0.0-release)
2017-11-23 17:30:11.663	  0x7fff7b2be000	INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2017-11-23 17:30:11.663	  0x7fff7b2be000	INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
2017-11-23 17:30:11.663	  0x7fff7b2be000	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2017-11-23 17:30:13.252	  0x7fff7b2be000	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2017-11-23 17:30:13.253	  0x7fff7b2be000	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
2017-11-23 17:30:13.253	  0x7fff7b2be000	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:70	Binding on 127.0.0.1:18081
2017-11-23 17:30:13.253	  0x7fff7b2be000	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2017-11-23 17:30:13.253	  0x7fff7b2be000	INFO 	global	src/daemon/core.h:73	Initializing core...
2017-11-23 17:30:13.253	  0x7fff7b2be000	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:323	Loading blockchain from folder /Users/tramp/.bitmonero/lmdb ...`
Bus error: 10

bitmonero.log has this:
`2017-11-23 17:30:11.662   0x7fff7b2be000        INFO    logging contrib/epee/src/mlog.cpp:148   New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-23 17:30:11.662   0x7fff7b2be000        INFO    logging contrib/epee/src/mlog.cpp:156   New log categories: *:WARNING,global:INFO,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-11-23 17:30:11.662   0x7fff7b2be000        INFO    global  src/daemon/main.cpp:279 Monero 'Helium Hydra' (v0.11.0.0-release)
2017-11-23 17:30:11.663   0x7fff7b2be000        INFO    global  src/daemon/protocol.h:55        Initializing cryptonote protocol...
2017-11-23 17:30:11.663   0x7fff7b2be000        INFO    global  src/daemon/protocol.h:60        Cryptonote protocol initialized OK
2017-11-23 17:30:11.663   0x7fff7b2be000        INFO    global  src/daemon/p2p.h:63     Initializing p2p server...
2017-11-23 17:30:13.252   0x7fff7b2be000        INFO    global  src/daemon/p2p.h:68     P2p server initialized OK
2017-11-23 17:30:13.253   0x7fff7b2be000        INFO    global  src/daemon/rpc.h:58     Initializing core rpc server...
2017-11-23 17:30:13.253   0x7fff7b2be000        INFO    global  contrib/epee/include/net/http_server_impl_base.h:70     Binding on 127.0.0.1:18081
2017-11-23 17:30:13.253   0x7fff7b2be000        INFO    global  src/daemon/rpc.h:63     Core rpc server initialized OK on port: 18081
2017-11-23 17:30:13.253   0x7fff7b2be000        INFO    global  src/daemon/core.h:73    Initializing core...
2017-11-23 17:30:13.253   0x7fff7b2be000        INFO    global  src/cryptonote_core/cryptonote_core.cpp:323     Loading blockchain from folder /Users/tramp/.bitmonero/lmdb ...`

## Spartan-Hex-Shadow | 2017-11-24T05:07:36+00:00
Any resolution to the stacktrace i posted above team?

## dEBRUYNE-1 | 2017-11-24T15:30:02+00:00
@Spartan-Hex-Shadow Would you be able to compile monero master and use the daemon from the build?

----------------

@apostnik76 Can you first upgrade to v0.11.1.0 and then try `./monerod --max-concurrency 1` ?

https://monero.stackexchange.com/questions/6390/how-do-i-upgrade-my-software-to-v0-11-1-0

--------------

@nobrand Did you try restarting the daemon? 


## Spartan-Hex-Shadow | 2017-11-27T04:24:57+00:00
@dEBRUYNE-1 what do you mean when you say compile monero master? As in download the code, compile it, and then run? Sorry, new to the mining arena

## dEBRUYNE-1 | 2017-11-27T12:19:16+00:00
@Spartan-Hex-Shadow Yes, you can use `git clone` to download the code. See:

https://github.com/monero-project/monero#build-instructions

## MattDHill | 2017-12-01T16:08:39+00:00
Successfully synced the blockchain yesterday and was connected all day. Restarted my machine this morning. Launched the GUI and Daemon and got this error: "Error: Couldn't connect to daemon: 127.0.0.1:18081". I deleted p2pstate.bin, restarted my machine, and am still getting the error. Any idea what might have caused this and how to resolve?

## dEBRUYNE-1 | 2017-12-01T17:04:06+00:00
@MattDHill Can you paste the content of `bitmonero.log` (C:\ProgramData\bitmonero on Windows | ~/.bitmonero on Linux and Mac OS X) to https://paste.fedoraproject.org?

## living-legend | 2017-12-01T19:22:16+00:00
@gitmehubscotty I noticed you have "G:\MoneroGui2" under Blockchain Location in the GUI.  Try removing this and see if the GUI will then start the daemon.  I was having the same issue i.e. "Daemon failed to start" but was able to start the daemon manually.  After trying multiple things, even wiped EVERYTHING and started over, it turns out the GUI apparently couldn't find or launch the daemon when I had an entry under 'Blockchain Location'. 

## davidjoyce-okta | 2017-12-10T07:18:35+00:00
So a temporary solution to this problem is to do the following:

1. In regedit, navigate to `HKEY_CURRENT_USER\Software\monero-project\monero-core`
2. Set `blockchainDataDir` to nothing (currently there is no way to do this through the GUI itself)

Back in the GUI, set `Daemon startup flags` to `--data-dir=F:\CryptoCurrencyData\Monero` (change the directory to yours).

The daemon should now launch properly from the GUI. Hope this helps.

## Volaviand | 2017-12-12T18:35:07+00:00
Got mine to start syncing again. Ran as Admin!
*Update*
Starting my monerod.exe with admin settings on alone. I got this error it fixed. Not too much of a coder, learning, but seems like it had to be allowed to reset the mapsize, cant bind socket, or no two valid dns checkpoints recieved.  Someone with more exp? lol


 after putting my WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:xxxxLMDB memory map needs to be resized, doing that now.
2017-12-12 1xxx:x.x6x 4700    INFO    global  src/blockchain_db/lmdb/db_lmdb.cpp:494  LMDB Mapsize increased.  Old: 35087MiB, New: 36111MiB

2017-12-12 x:xx:xxxx.xxx 4700    INFO    global  src/cryptonote_core/cryptonote_core.cpp:421     Loading checkpoints
[1513105107] libunbound[18596:0] error: can't bind socket: Permission denied. for 0.0.0.0
2017-12-12 xx:xx:xx.xxx 4700    WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received


## gitmehubscotty | 2017-12-13T17:11:11+00:00
Could anyone write an update for the GUI that fixes this problem permanently? Monero is great, keep up the good work.

## glitch182 | 2017-12-15T03:16:36+00:00
I had the same issue, until I ran the wallet in administrator mode (Right click -> Run as administrator)

## orsonwinston | 2017-12-17T16:14:50+00:00
I have the same problem, but I'm on a Mac. Is there a Mac fix? 'Please check your wallet and daemon log for errors. You can also try to start monerod manually.'

## dEBRUYNE-1 | 2017-12-17T20:15:13+00:00
@orsonwinston Did you try to start monerod manually? You can simply double click on it and it's located in ` ~/Applications/monero-wallet-gui.app/Contents/MacOS`

## jordangunderson | 2017-12-20T11:31:44+00:00
I think I'm seeing this same error running GUI version 0.11.1.0 on Ubuntu 16.04.3 LTS.

When starting the app (or clicking "Start daemon" inside the GUI), I see the following "Daemon failed to start" message: "Please check your wallet and daemon log for errors. You can also try to start monerod manually."

When I click "Show status", I see the following log info:

```
Error: Couldn't connect to daemon: 127.0.0.1:18081

[31m2017-12-20 11:12:55.571	    7f9ea7a79740	ERROR	net.http	contrib/epee/include/net/http_client.h:444	Unexpected recv fail
[0mError: Couldn't connect to daemon: 127.0.0.1:18081
```

In the console itself, I see the following:

```
"starting monerod /opt/monero-gui-v0.11.1.0/monerod"
With command line arguments  ("--detach", "--check-updates", "disabled")
2017-12-20 11:18:54.239	    7efc9a0a4740	INFO 	global	src/daemon/main.cpp:279	Monero 'Helium Hydra' (v0.11.1.0-release)
Forking to background...
sending external cmd:  ("status")
"\u001B[31m2017-12-20 11:18:56.285\t    7f3a75671740\tERROR\tnet.http\tcontrib/epee/include/net/http_client.h:444\tUnexpected recv fail\n\u001B[0mError: Couldn't connect to daemon: 127.0.0.1:18081\n"
daemon not running. checking again in 2 seconds.
sending external cmd:  ("status")
"Error: Couldn't connect to daemon: 127.0.0.1:18081\n"
```

If I close the app and try manually start the daemon via the command line, I see the following:

```
2017-12-20 11:20:03.524	    7fd0c26c3740	INFO 	global	src/daemon/main.cpp:279	Monero 'Helium Hydra' (v0.11.1.0-release)
2017-12-20 11:20:03.524	    7fd0c26c3740	INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2017-12-20 11:20:03.524	    7fd0c26c3740	INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
2017-12-20 11:20:03.525	    7fd0c26c3740	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2017-12-20 11:20:05.541	    7fd0c26c3740	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2017-12-20 11:20:05.542	    7fd0c26c3740	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
2017-12-20 11:20:05.542	    7fd0c26c3740	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:70	Binding on 127.0.0.1:18081
2017-12-20 11:20:05.542	    7fd0c26c3740	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2017-12-20 11:20:05.542	    7fd0c26c3740	INFO 	global	src/daemon/core.h:73	Initializing core...
2017-12-20 11:20:05.542	    7fd0c26c3740	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:323	Loading blockchain from folder /home/myname/.bitmonero/lmdb ...
Bus error (core dumped)
```

Any recommendations?

## dEBRUYNE-1 | 2017-12-20T12:20:22+00:00
@jordangunderson Are you sure your chain isn't corrupt?

## jordangunderson | 2017-12-20T13:28:47+00:00
@dEBRUYNE-1 
I'm not sure, but I wouldn't be surprised. (There's a good chance I've killed the app using CTRL-C in the terminal. I'll be sure to click the "X" from now on.)

I just tried following your (excellent) [guide on Stack Overflow](https://monero.stackexchange.com/questions/6825/i-am-using-the-gui-and-my-daemon-doesnt-start-anymore) and got to step 10, which addresses determining whether the blockchain is currupted:

> [10] If your log contains this line or something similar, the blockchain is corrupted:
>     Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid

I ran `cat bitmonero.log | grep "MDB_BAD_TXN"` with no results. (Same with grepping for "Failed" and "abort".) I don't know if there's anything else I should be searching for that would indicate a corrupted chain.

That's the point in the guide at which I stopped.

Anything else I should try?

## jordangunderson | 2017-12-20T13:45:47+00:00
Tailing that log file, I see the following benign-looking pattern:
```
2017-12-20 11:18:54.239	    7efc9a0a4740	INFO 	global	src/daemon/main.cpp:279	Monero 'Helium Hydra' (v0.11.1.0-release)
2017-12-20 11:18:54.239	    7efc9a0a4740	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Forking to background...
2017-12-20 11:18:54.240	    7efc9a0a4740	WARN 	daemon	src/daemon/executor.cpp:62	Monero 'Helium Hydra' (v0.11.1.0-release) Daemonised
2017-12-20 11:18:54.240	    7efc9a0a4740	INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2017-12-20 11:18:54.240	    7efc9a0a4740	INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
2017-12-20 11:18:54.241	    7efc9a0a4740	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2017-12-20 11:18:55.940	    7efc9a0a4740	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2017-12-20 11:18:55.940	    7efc9a0a4740	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
2017-12-20 11:18:55.940	    7efc9a0a4740	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:70	Binding on 127.0.0.1:18081
2017-12-20 11:18:55.940	    7efc9a0a4740	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2017-12-20 11:18:55.940	    7efc9a0a4740	INFO 	global	src/daemon/core.h:73	Initializing core...
2017-12-20 11:18:55.940	    7efc9a0a4740	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:323	Loading blockchain from folder /home/myname/.bitmonero/lmdb ...
```

...followed by these repeating errors:
```
2017-12-20 11:18:56.245	    7f3a75671740	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-12-20 11:18:56.285	    7f3a75671740	ERROR	net.http	contrib/epee/include/net/http_client.h:444	Unexpected recv fail
2017-12-20 11:18:56.286	    7f3a75671740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
```


## peternemser | 2017-12-21T16:48:04+00:00
Had the problem in Windows 10 - was running in normal mode and needed to allow for exceptions in the windows default security and to run in admin mode - then everything worked great. In windows go to your wallet folder and right click on the monero.exe and  "run as administrator" - that how I got mine to work.

## dEBRUYNE-1 | 2017-12-22T21:12:34+00:00
@jordangunderson Could you paste the full content of bitmonero.log to https://paste.fedoraproject.org? 

## jordangunderson | 2017-12-23T14:46:54+00:00
dEBRUYNE-1 - Here you go: https://paste.fedoraproject.org/paste/kFPg~xTHfvM45Jdvv9SeJw

You should know I've since deleted `data.mdb` and restarted the app, and the data /seems/ to have resynced just fine.

## jordangunderson | 2017-12-23T14:53:32+00:00
dEBRUYNE-1 - I had also tried `./monerod --db-salvage` to no effect. (It failed very quickly, ending with that same `Bus error (core dumped)` output to the terminal.)

## dEBRUYNE-1 | 2017-12-23T16:28:03+00:00
@jordangunderson Your chain was likely corrupted, but, according to moneromooo, it's not apparent from your log. You'd have to rerun it with `--log-level 1`, but I presume you don't have the old chain anymore?

## Poppy2 | 2018-01-04T21:39:11+00:00
I am having the same issue when trying to syncronise my Monero wallet after a power failure
"Daemon failed to start.
Please check your wallet and daemon log for errors. You can also try to start monerod.exe manually."
I have tried some of the suggestions in this post but non seem to have worked. Could someone please help?

## BBooch | 2018-01-05T07:34:37+00:00
over a long period of time, I have tried many of the suggestions in the
thread.  Finally, all I did was leave it on for a full day at the main
screen..... it somehow synchronized fully!?!? I have no idea.....

On Thu, Jan 4, 2018 at 2:39 PM, Poppy2 <notifications@github.com> wrote:

> I am having the same issue when trying to syncronise my Monero wallet
> after a power failure
> "Daemon failed to start.
> Please check your wallet and daemon log for errors. You can also try to
> start monerod.exe manually."
> I have tried some of the suggestions in this post but non seem to have
> worked. Could someone please help?
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero-gui/issues/890#issuecomment-355406222>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AK48TWzYScqd72AhjWClcWB8kFs9dSuCks5tHUUBgaJpZM4PhFQ2>
> .
>


## jordangunderson | 2018-01-05T20:45:52+00:00
dEBRUYNE-1 - Sorry it's taken me so long to respond. I'm not sure what you mean by the `chain`, but I'm assuming that means `data.mdb`. I deleted that file, but kept the log. (I presume it just keeps tacking stuff on.) Incidentally, I actually had run manually the daemon briefly with `--log-level 1` a few times to see if I noticed anything peculiar --so I'm assuming that stuff would still be in the log file (including the stuff that I posted in Paste. LMK if you'd like me to paste it again.) Lastly, if I run into this problem again, I'll just move my .mdb file instead of deleting it to allow for further troubleshooting; but I agree with the synopsis that there must have been some kind of corruption, since deleting and resyncing the database seemed to do the trick.

## cc45 | 2018-01-24T20:23:52+00:00
I am having the issue as well. Same error as gitmehubscotty. Running Windows 10 and installed it just today as of 1/24/2018. Is there a fix? I tried the easy stuff like opening in Admin and trying different nodes but no joy.

## BBooch | 2018-01-24T23:58:07+00:00
have you tried to just leave it open for a really long time, like couple
days?  I have done many of the suggestions around the web, then finally
just let it stay open for a long time and it somehow started working
again.  I deleted some monero folder that was tucked far away in the C
drive also

On Wed, Jan 24, 2018 at 1:23 PM, cc45 <notifications@github.com> wrote:

> I am having the issue as well. Same error as gitmehubscotty. Running
> Windows 10 and installed it just today as of 1/24/2018. Is there a fix? I
> tried the easy stuff like opening in Admin and trying different nodes but
> no joy.
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero-gui/issues/890#issuecomment-360261788>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AK48Tf3XEkmjFUUfuh4fL3SEL2_YDZCEks5tN5FagaJpZM4PhFQ2>
> .
>


## cc45 | 2018-01-25T00:01:53+00:00

I hadn't, I Just started mining I want to see some progress lol!
Chris

      From: BBooch <notifications@github.com>
 To: monero-project/monero-gui <monero-gui@noreply.github.com> 
Cc: cc45 <chris.corino@yahoo.com>; Comment <comment@noreply.github.com>
 Sent: Wednesday, January 24, 2018 4:58 PM
 Subject: Re: [monero-project/monero-gui] "Daemon failed to start" (#890)
   
have you tried to just leave it open for a really long time, like couple
days? I have done many of the suggestions around the web, then finally
just let it stay open for a long time and it somehow started working
again. I deleted some monero folder that was tucked far away in the C
drive also

On Wed, Jan 24, 2018 at 1:23 PM, cc45 <notifications@github.com> wrote:

> I am having the issue as well. Same error as gitmehubscotty. Running
> Windows 10 and installed it just today as of 1/24/2018. Is there a fix? I
> tried the easy stuff like opening in Admin and trying different nodes but
> no joy.
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero-gui/issues/890#issuecomment-360261788>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AK48Tf3XEkmjFUUfuh4fL3SEL2_YDZCEks5tN5FagaJpZM4PhFQ2>
> .
>
—
You are receiving this because you commented.
Reply to this email directly, view it on GitHub, or mute the thread.  

   

## emminer | 2018-01-27T06:39:37+00:00
I have the same issue.
macOS Sierra 10.12.6
The wallet and daemon worked well days ago, today when I open wallet, it says Daemon failed to start. Please check your wallet and daemon log for errors. You can also try to start monerod manually.

GUI version: v0.11.1.0
Embedded Monero version: v0.11.1.0-2-gc328163

/Users/me/.bitmonero/bitmonero.log:

2018-01-27 06:35:15.616   0x7fffd28003c0        INFO    logging contrib/epee/src/mlog.cpp:148   New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-01-27 06:35:15.618   0x7fffd28003c0        ERROR   msgwriter       src/common/scoped_message_writer.h:102  Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-01-27 06:35:17.643   0x7fffd28003c0        INFO    logging contrib/epee/src/mlog.cpp:148   New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-01-27 06:35:17.645   0x7fffd28003c0        ERROR   msgwriter       src/common/scoped_message_writer.h:102  Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-01-27 06:35:19.671   0x7fffd28003c0        INFO    logging contrib/epee/src/mlog.cpp:148   New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-01-27 06:35:19.672   0x7fffd28003c0        ERROR   msgwriter       src/common/scoped_message_writer.h:102  Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-01-27 06:35:21.694   0x7fffd28003c0        INFO    logging contrib/epee/src/mlog.cpp:148   New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-01-27 06:35:21.696   0x7fffd28003c0        ERROR   msgwriter       src/common/scoped_message_writer.h:102  Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-01-27 06:35:23.722   0x7fffd28003c0        INFO    logging contrib/epee/src/mlog.cpp:148   New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-01-27 06:35:23.723   0x7fffd28003c0        ERROR   msgwriter       src/common/scoped_message_writer.h:102  Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-01-27 06:35:25.747   0x7fffd28003c0        INFO    logging contrib/epee/src/mlog.cpp:148   New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-01-27 06:35:25.748   0x7fffd28003c0        ERROR   msgwriter       src/common/scoped_message_writer.h:102  Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-01-27 06:35:27.771   0x7fffd28003c0        INFO    logging contrib/epee/src/mlog.cpp:148   New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-01-27 06:35:27.772   0x7fffd28003c0        ERROR   msgwriter       src/common/scoped_message_writer.h:102  Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-01-27 06:35:29.793   0x7fffd28003c0        INFO    logging contrib/epee/src/mlog.cpp:148   New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-01-27 06:35:29.795   0x7fffd28003c0        ERROR   msgwriter       src/common/scoped_message_writer.h:102  Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-01-27 06:35:31.820   0x7fffd28003c0        INFO    logging contrib/epee/src/mlog.cpp:148   New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-01-27 06:35:31.821   0x7fffd28003c0        ERROR   msgwriter       src/common/scoped_message_writer.h:102  Error: Couldn't connect to daemon: 127.0.0.1:18081



Don't know how to troubleshoot it.

## leonklingele | 2018-01-27T07:14:54+00:00
@emminer what's the output of `lsof -i | grep 18081` (while the daemon is running)? Do you start the daemon manually (via CLI?) or automatically via GUI?

## cc45 | 2018-01-27T14:47:06+00:00
Well I left it on since I posted and it still does not work. Have we tried uninstalling and reinstalling the wallet? Can we mine directly to a wallet for Monero? I really wanted to be part of this but I have to be honest in that if the wallet is this much of an issue I am going to move on.  Or can I mine to my light wallet? (Yes I know its not recommended however we are not talking about a mining farm either).

## emminer | 2018-01-28T00:14:57+00:00
lsof -i | grep 18081 outputs nothing.
I started daemon automatically via GUI, I clicked the start daemon button in GUI, both of them didn't work.
Not sure how to start the daemon via CLI.

## cc45 | 2018-01-28T00:17:41+00:00
I have tried it every which way, nothing. Which is why I was wondering if you can mine directly to the light wallet which opens no problem.


## leonklingele | 2018-01-28T00:28:45+00:00
@emminer please try this:

1. Close the Monero GUI (and monerod CLI in case you've started it)
2. Rename (or delete) the `bitmonero.log` log file
3. Start the GUI
4. Post the output of the full log file (preferably to https://paste.ubuntu.com/ so it doesn't clutter this conversation here)

## emminer | 2018-01-28T00:43:57+00:00
thanks leoniingele, result is:
https://paste.ubuntu.com/26474099/


## cc45 | 2018-01-28T00:55:02+00:00
Here is what I deleted and just like that it connected - no errors. 
C:\ProgramData\bitmonero\lmdb  -  I am running windows 10. Hope this helps someone else.

## olmie75 | 2018-01-28T00:58:13+00:00
I'm using Windows 7 Pro, installed Monero wallet GUI v0.11.1.0 today, and it worked and synced up. After computer crash, I can't get the daemon to start, tried the various suggestions above with no luck. Last several lines of log info below. Please advise.
2018-01-27 23:09:39.285	13056	ERROR	net.http	contrib/epee/include/net/http_client.h:444	Unexpected recv fail
2018-01-27 23:09:39.285	13056	ERROR	WalletAPI	src/wallet/api/wallet.cpp:738	daemonBlockChainTargetHeight: possibly lost connection to daemon
2018-01-27 23:11:22.536	13056	ERROR	net.http	contrib/epee/include/net/http_client.h:444	Unexpected recv fail
2018-01-27 23:11:22.536	13056	ERROR	WalletAPI	src/wallet/api/wallet.cpp:738	daemonBlockChainTargetHeight: possibly lost connection to daemon
2018-01-27 23:12:15.228	6420	ERROR	net.http	contrib/epee/include/net/http_client.h:444	Unexpected recv fail
2018-01-27 23:12:15.228	6420	ERROR	WalletAPI	src/wallet/api/wallet.cpp:738	daemonBlockChainTargetHeight: possibly lost connection to daemon
2018-01-27 23:17:02.285	13056	ERROR	net.http	contrib/epee/include/net/http_client.h:444	Unexpected recv fail
2018-01-27 23:17:02.285	13056	ERROR	WalletAPI	src/wallet/api/wallet.cpp:738	daemonBlockChainTargetHeight: possibly lost connection to daemon
2018-01-27 23:17:35.785	13056	ERROR	net.http	contrib/epee/include/net/http_client.h:444	Unexpected recv fail
2018-01-27 23:17:35.785	13056	ERROR	WalletAPI	src/wallet/api/wallet.cpp:738	daemonBlockChainTargetHeight: possibly lost connection to daemon
2018-01-27 23:18:55.786	13056	ERROR	net.http	contrib/epee/include/net/http_client.h:444	Unexpected recv fail
2018-01-27 23:18:55.786	13056	ERROR	WalletAPI	src/wallet/api/wallet.cpp:738	daemonBlockChainTargetHeight: possibly lost connection to daemon
2018-01-27 23:53:23.292	4544	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-01-27 23:53:25.106	4544	INFO 	logging	contrib/epee/src/mlog.cpp:156	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-01-27 23:53:26.215	4544	INFO 	logging	contrib/epee/src/mlog.cpp:156	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-01-27 23:53:26.244	3252	ERROR	net.http	contrib/epee/include/storages/portable_storage.h:161	portable_storage: wrong binary format - signature mismatch
2018-01-27 23:53:26.244	3252	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:2128	!r. THROW EXCEPTION: error::invalid_password
2018-01-27 23:53:26.244	3252	WARN 	net.http	src/wallet/wallet_errors.h:707	C:/msys64/home/vagrant/slave/monero-core-win64/build/monero/src/wallet/wallet2.cpp:2128:N5tools5error16invalid_passwordE: invalid password
2018-01-27 23:53:26.244	3252	ERROR	WalletAPI	src/wallet/api/wallet.cpp:504	Error opening wallet: invalid password
2018-01-27 23:53:26.488	3252	ERROR	WalletAPI	src/wallet/api/wallet.cpp:553	Status_Critical - not storing wallet
2018-01-27 23:53:54.912	4544	INFO 	logging	contrib/epee/src/mlog.cpp:156	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-01-27 23:53:54.942	3252	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:2505	Loaded wallet keys file, with public address: 4APiNrDxSwCUnje57cDdiu7qNYLmpD2Aq5jCy9GuZMxr2G4SRGrCWsbWtwEV1pDVYTGJ22P9Lm1dR96rA1Z8gjReELic1zE
2018-01-27 23:55:23.725	5348	WARN 	net.dns	src/common/dns_utils.cpp:487	WARNING: no two valid MoneroPulse DNS checkpoint records were received
2018-01-28 00:14:16.980	6084	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-01-28 00:14:18.966	6084	INFO 	logging	contrib/epee/src/mlog.cpp:156	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-01-28 00:14:19.772	6084	INFO 	logging	contrib/epee/src/mlog.cpp:156	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-01-28 00:14:19.802	1676	ERROR	net.http	contrib/epee/include/storages/portable_storage.h:161	portable_storage: wrong binary format - signature mismatch
2018-01-28 00:14:19.803	1676	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:2128	!r. THROW EXCEPTION: error::invalid_password
2018-01-28 00:14:19.804	1676	WARN 	net.http	src/wallet/wallet_errors.h:707	C:/msys64/home/vagrant/slave/monero-core-win64/build/monero/src/wallet/wallet2.cpp:2128:N5tools5error16invalid_passwordE: invalid password
2018-01-28 00:14:19.804	1676	ERROR	WalletAPI	src/wallet/api/wallet.cpp:504	Error opening wallet: invalid password
2018-01-28 00:14:20.003	1676	ERROR	WalletAPI	src/wallet/api/wallet.cpp:553	Status_Critical - not storing wallet
2018-01-28 00:14:31.255	6084	INFO 	logging	contrib/epee/src/mlog.cpp:156	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-01-28 00:14:31.274	1676	ERROR	net.http	contrib/epee/include/storages/portable_storage.h:161	portable_storage: wrong binary format - signature mismatch
2018-01-28 00:14:31.274	1676	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:2128	!r. THROW EXCEPTION: error::invalid_password
2018-01-28 00:14:31.274	1676	WARN 	net.http	src/wallet/wallet_errors.h:707	C:/msys64/home/vagrant/slave/monero-core-win64/build/monero/src/wallet/wallet2.cpp:2128:N5tools5error16invalid_passwordE: invalid password
2018-01-28 00:14:31.274	1676	ERROR	WalletAPI	src/wallet/api/wallet.cpp:504	Error opening wallet: invalid password
2018-01-28 00:14:31.285	1676	ERROR	WalletAPI	src/wallet/api/wallet.cpp:553	Status_Critical - not storing wallet
2018-01-28 00:14:43.700	6084	INFO 	logging	contrib/epee/src/mlog.cpp:156	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-01-28 00:14:43.722	1676	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:2505	Loaded wallet keys file, with public address: 4APiNrDxSwCUnje57cDdiu7qNYLmpD2Aq5jCy9GuZMxr2G4SRGrCWsbWtwEV1pDVYTGJ22P9Lm1dR96rA1Z8gjReELic1zE
2018-01-28 00:16:11.467	1752	WARN 	net.dns	src/common/dns_utils.cpp:487	WARNING: no two valid MoneroPulse DNS checkpoint records were received


## leonklingele | 2018-01-28T01:13:44+00:00
@emminer are you sure that's all? Do you still get the `Daemon failed to start` error message when starting the GUI?

Close the GUI and start `monerod` via CLI. This can be done as follows:

1. Open the `Terminal` app
2. Paste the following line (you might need to adjust the path): `/Applications/monero-wallet-gui.app/Contents/MacOS/monerod --log-level 3`
3. Press Enter & wait for a few seconds / until error messages appear
4. Paste the whole output, make sure to redact sensitive information

## emminer | 2018-01-28T01:15:28+00:00
I renamed lmdb, the daemon started.
But I have to re sync and download 35G file :(

## leonklingele | 2018-01-28T01:19:23+00:00
@emminer sure, that'll work. Most likely your old blockchain is corrupted. Let's try to find the root cause. Please stop your daemon and undo the lmdb rename, then follow the instructions from my previous comment. Maybe there's an easier way than to resync the whole blockchain.

## emminer | 2018-01-28T01:37:13+00:00
https://paste.ubuntu.com/26474319/

## leonklingele | 2018-01-28T02:13:26+00:00
@emminer oops, try it again with `--log-level 1` or `--log-level 2` please.

## emminer | 2018-01-28T02:53:15+00:00
level 2:
https://paste.ubuntu.com/26474587/


## emminer | 2018-01-28T02:54:36+00:00
level 1:
https://paste.ubuntu.com/26474593/


## leonklingele | 2018-01-28T03:14:42+00:00
@emminer looks like this has already been reported in https://github.com/monero-project/monero/issues/2669 and fixed&merged in https://github.com/monero-project/monero/pull/3019. Try [building](https://github.com/monero-project/monero#on-linux-and-os-x) latest master and check if it works for you.

## emminer | 2018-01-28T10:47:14+00:00
Got a ton of errors during build, tried to fix them but no luck. I've downloaded the 35G blockchain file.

## drogongod | 2018-02-18T17:50:02+00:00
Had the same issue deleted C:\ProgramData\bitmonero  issue fixed... painful to redownload but nothing else for it.So stop playing with it. The blockchain we downloaded corrupted delete restart problem solved..  Then have a good cry over the 35 gig sync you got redo.. We Really should have a torrent for first 35 (Tared) of C:\ProgramData\bitmonero ...then we just verify force check the torrent and untar it then slip it in and sync... Save us all a lot of pain


## gaga9999 | 2018-04-15T16:09:41+00:00
I am on Ubuntu and monerod synced everything (v.0.12.0.0):
`2018-04-15 16:02:13.432 [P2P5]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1557    SYNCHRONIZED OK`

monero-cli works fine:
`Refreshed 1551837/1551837, synced, daemon RPC v1.19
[wallet 43o5JF]: 
`


Running monero-gui does not work (while monerod is running):
1."network status disconnected"
2.show status: "
Height: 1551837/1551837 (100.0%) on mainnet, not mining, net hash 481.44 MH/s, v7, up to date, 8(out)+0(in) connections, uptime 0d 0h 7m 18s"

nothing moves

When runnin monero-gui without monerod running and pressing "start daemon" it show: "cant connect do daemon".


in bitmonero.log I have this line repeating from monero-gui:
"logging contrib/epee/src/mlog.cpp:185   New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global::INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
"
then:
":INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO"
and
":INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
"
and
"src/common/stack_trace.cpp:163      [1] ./monerod:__wrap___cxa_throw+0x10a [0x559c487c81ba]"
etc etc

when the gui runs and not the daemon and i press "start daemon" i also get
"WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,g..."

## oblique99 | 2018-05-30T00:28:19+00:00
Hi everyone.

Running 0.12.0.0 in Win10x64 and getting the following error when manually starting monerod (GUI runs ok but always daemon failed to start message)


2018-05-30 00:20:29.190 5268    INFO    global  src/daemon/main.cpp:280 Monero 'Lithium Luna' (v0.12.0.0-master-release)
2018-05-30 00:20:29.190 5268    INFO    global  src/daemon/protocol.h:53        Initializing cryptonote protocol...
2018-05-30 00:20:29.190 5268    INFO    global  src/daemon/protocol.h:58        Cryptonote protocol initialized OK
2018-05-30 00:20:29.190 5268    INFO    global  src/daemon/p2p.h:63     Initializing p2p server...
2018-05-30 00:20:30.553 5268    INFO    global  src/daemon/p2p.h:68     p2p server initialized OK
2018-05-30 00:20:30.740 5268    INFO    global  src/daemon/rpc.h:63     Initializing core RPC server...
2018-05-30 00:20:30.740 5268    INFO    global  contrib/epee/include/net/http_server_impl_base.h:76  Binding on 127.0.0.1:18081
2018-05-30 00:20:30.740 5268    INFO    global  src/daemon/rpc.h:69     core RPC server initialized OK on port: 18081
2018-05-30 00:20:30.740 5268    INFO    global  src/daemon/core.h:86    Initializing core...
2018-05-30 00:20:30.740 5268    INFO    global  src/cryptonote_core/cryptonote_core.cpp:427     Loading blockchain from folder C:\ProgramData\bitmonero\lmdb ...
2018-05-30 00:20:30.740 5268    WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:75   Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2018-05-30 00:20:30.740 5268    ERROR   cn      src/cryptonote_core/cryptonote_core.cpp:503     Error opening database: Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2018-05-30 00:20:30.740 5268    INFO    global  src/daemon/rpc.h:96     Deinitializing core RPC server...
2018-05-30 00:20:30.740 5268    INFO    global  src/daemon/p2p.h:90     Deinitializing p2p...
2018-05-30 00:20:31.963 5268    INFO    global  src/daemon/core.h:103   Deinitializing core...
2018-05-30 00:20:31.963 5268    ERROR   daemon  src/daemon/core.h:108   Failed to deinitialize core...
2018-05-30 00:20:31.963 5268    INFO    global  src/daemon/protocol.h:75        Stopping cryptonote protocol...
2018-05-30 00:20:31.963 5268    INFO    global  src/daemon/protocol.h:79        Cryptonote protocol stopped successfully

## stoffu | 2018-05-30T02:25:22+00:00
@oblique99 

The error MDB_BAD_TXN is likely due to the DB being corrupt:

- https://github.com/monero-project/monero/issues/3551
- https://github.com/monero-project/monero/issues/3240

Please try `monerod --db-salvage`. If it doesn't work, then try redoing the full syncing. If the problem persists, please open a new ticket under the Monero repository, not here.


## cc45 | 2018-05-30T13:28:38+00:00
I did all the above, plus dragongod suggested. Still didn't work, ive moved on. I mean if you cant get something as basic as the wallet to function, if its this hard it will never catch on but for a small part of the population base. It needs to be "wellsfargo easy". Not wasting any more time on it, I do wish them well as I really like the coin and the fact its asic resistant. 

## stoffu | 2018-05-30T14:51:03+00:00
@cc45 Did you manage to get your monerod.exe fully synced (does it show SYNCHRONIZED OK message in green)? If not, open a new ticket in https://github.com/monero-project/monero, not here (this repo is specific to the GUI). Also, please post the content of C:/ProgramData/bitmonero/bitmonero.log to either fpaste.org or paste.debian.net.

## daedalus21 | 2018-06-03T15:12:14+00:00
same problem. on Mac, running lithium luna. had to force quit the GUI and it have been unable to get it started ever since. 

here's the error message from the terminal when I tried to start monerod manually, following @leonklingele's suggestion: 
https://paste.ubuntu.com/p/WZ5NB3vprN/

any help would be much appreciated. 

edit: turns out monerod was running in the background already and was causing its failure to start. closing monerod in activity monitor and relaunching resolved it. 

## MattyBv3 | 2018-07-12T02:20:38+00:00
If you're using Win 7/8/10 be sure to right-click / run as admin
I know, it's basic, but hadn't seen it posted and it solved the daemon not starting for quite a few friends of mine.

## selsta | 2019-04-27T00:10:10+00:00
+invalid

## Magu-James | 2022-05-21T23:15:37+00:00
There are 2 reasons why daemon fails to start. 1. Your antivirus might have deleted monerod.exe file or the firewall is stopping daemon from accessing the network. or 2. Your blockchain file might be corrupted due to ungraceful shutdown.

# Action History
- Created by: gitmehubscotty | 2017-09-22T18:36:24+00:00
- Closed at: 2019-04-27T01:00:37+00:00
