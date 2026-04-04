---
title: GUI Wallet is not connected to daemon
source_url: https://github.com/monero-project/monero-gui/issues/1303
author: joelstahre
assignees: []
labels:
- resolved
created_at: '2018-04-09T20:27:02+00:00'
updated_at: '2018-07-04T09:54:28+00:00'
type: issue
status: closed
closed_at: '2018-07-04T09:54:28+00:00'
---

# Original Description
I updated to Lithium Luna, im on Linux Ubuntu.
I Followed the upgrade instructions on getmonero.

I have the GUI version, so i just downloaded the new version to a new directory, and started it by doing 
 ```
./start-gui.sh
```

It loads my wallet file. (i can see my balance)


monerod is running


``` 
ps aux | grep mone
3199  8.4  3.3 1033524 130720 pts/20 Sl+  22:13   0:05 ./monero-wallet-gui
3494  0.0  0.0  15756   864 pts/19   S+   22:14   0:00 grep --color=auto mone
32448  1.6  4.3 82165380 170772 ?     Sl   18:08   4:10 /home/skynet/monero-gui-v0.12.0.0/monerod --detach --check-updates disabled

``` 

But the gui says that it is not connected.

```
GUI Wallet is not connected to daemon (Start deamon)
```

```
Network Status
Disconnected
```

Manage deamon (Status) output

```
Height: 1547643/1547643 (100.0%) on mainnet, not mining, net hash 420.55 MH/s, v7, up to date, 8(out)+4(in) connections, uptime 0d 4h 8m 7s

Height: 1547643/1547643 (100.0%) on mainnet, not mining, net hash 420.55 MH/s, v7, up to date, 8(out)+4(in) connections, uptime 0d 4h 8m 15s

Height: 1547651/1547651 (100.0%) on mainnet, not mining, net hash 425.19 MH/s, v7, up to date, 8(out)+4(in) connections, uptime 0d 4h 18m 8s

Height: 1547652/1547652 (100.0%) on mainnet, not mining, net hash 425.01 MH/s, v7, up to date, 8(out)+4(in) connections, uptime 0d 4h 18m 12s
```


# Discussion History
## sanderfoobar | 2018-04-09T20:45:46+00:00
For debugging purposes; which Ubuntu version are you on?

Also; `sudo netstat -tulpn | grep -i monero`

## dEBRUYNE-1 | 2018-04-09T21:21:36+00:00
Similar to #1261 probably. 

## joelstahre | 2018-04-10T19:02:44+00:00
@skftn  im running Ubuntu 16.04 LTS

```
sudo netstat -tulpn | grep -i monero
tcp        0      0 0.0.0.0:18080           0.0.0.0:*               LISTEN      32448/monerod   
tcp        0      0 127.0.0.1:18081         0.0.0.0:*               LISTEN      32448/monerod   
tcp        0      0 127.0.0.1:18082         0.0.0.0:*               LISTEN      32448/monerod 
```

## joelstahre | 2018-04-10T19:04:11+00:00
@dEBRUYNE-1 Yes, very similar. I also get ERROR logs saying

```
2018-04-08 10:43:36.934	    7f5af5d76840	ERROR	default	src/wallet/api/utils.cpp:46	error: std::bad_cast
```

## robione-nr | 2018-04-15T00:37:01+00:00
Same issues. Same result from netstat.

I popped off blocks from chain until I was prior to the release of 0.12.0.0. That got the daemon working. My log reads as follows:

    2018-04-15 00:49:43.333	    7f1cd29347c0	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
    2018-04-15 00:49:47.858	    7f1cd29347c0	ERROR	default	src/wallet/api/utils.cpp:46	error: std::bad_cast
    2018-04-15 00:49:48.973	    7f1caff1d700	WARN 	net.dns	src/common/dns_utils.cpp:508	WARNING: no two valid MoneroPulse DNS checkpoint records were received
    2018-04-15 00:49:56.669	    7f1cd29347c0	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
    2018-04-15 00:49:56.876	    7f1caff1d700	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:5610	!r. THROW EXCEPTION: error::no_connection_to_daemon
    2018-04-15 00:49:56.876	    7f1caff1d700	WARN 	net.http	src/wallet/wallet_errors.h:794	/home/vagrant/slave/monero-gui-ubuntu-amd64/build/monero/src/wallet/wallet2.cpp:5610:N5tools5error23no_connection_to_daemonE: no connection to daemon, request = gettransactions
    2018-04-15 00:49:56.876	    7f1caff1d700	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:3827	Failed to save rings, will try again next time
    2018-04-15 00:49:56.914	    7f1cd29347c0	ERROR	default	src/wallet/api/utils.cpp:46	error: std::bad_cast
`

## sanderfoobar | 2018-04-15T10:16:40+00:00
@robione-nr @joelstahre bad_cast error is related to issue #1261

You could try https://build.getmonero.org/builders/monero-gui-linux-qt57/builds/4 in the meantime

## robione-nr | 2018-04-15T20:12:37+00:00
I'm above the average user but don't really have time to delve into things when they don't seem to go right. (Waaaay too many projects.) I installed `libunwind8` as that was my first error message running the wallet from that build, then `libqt5quick5` which was my second. I then had to download and install (it seemed) QT 5.7 and I did. It still didn't work. (Maybe path issue... not `-dev` version. /shrugs)

Figured I'd just erase my wallets and start/recover  0.11.0.0 wallet with 0.12.0.0 daemon, setting ring size to 7 until it gets figured out..

## joelstahre | 2018-04-16T20:09:05+00:00
@skftn any directions on what steps i need to do to test that?

## PanderMusubi | 2018-04-27T18:05:25+00:00
https://github.com/monero-project/monero-gui/issues/1261 has a fix

## dEBRUYNE-1 | 2018-07-04T08:39:32+00:00
This particular issue is resolved in GUI v0.12.2.0: 

https://www.reddit.com/r/Monero/comments/8vkx2g/gui_v01220_released/

## dEBRUYNE-1 | 2018-07-04T08:39:36+00:00
+resolved

# Action History
- Created by: joelstahre | 2018-04-09T20:27:02+00:00
- Closed at: 2018-07-04T09:54:28+00:00
