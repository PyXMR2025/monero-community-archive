---
title: Windows 64bit Receive Tab Lag
source_url: https://github.com/monero-project/monero-gui/issues/1264
author: keatond
assignees: []
labels:
- bug
- resolved
created_at: '2018-04-04T16:39:52+00:00'
updated_at: '2018-07-03T14:00:31+00:00'
type: issue
status: closed
closed_at: '2018-07-03T14:00:31+00:00'
---

# Original Description
Been working with dEBRUYNE for the past few hours to try to track this issue down. 

System: Windows 10 64 Bit
Sync: Fully Synced from personal remote node

Issue: Currently experience massive lag when switching to the "Receive" tab on the new v12 GUI. This issue only occurs when you have restored an old wallet with transactions + using a remote node.

*Update*
So I tested a few different methods and looks to be an issue with remote nodes. I have fully synced the local daemon and no longer have the issue. If I switch back to using my personal remote node then the lag comes back going to the receiving tab. I have also tried using MoneroWorld's remote node and still seeing lag.

# Discussion History
## dEBRUYNE-1 | 2018-04-04T22:46:49+00:00
+bug

## bitlamas | 2018-04-05T13:09:22+00:00
I'm also experiencing the same problem using remote nodes with the GUI. The use of remote nodes with CLI is working as expected.

I've noticed these lines when the bug occurs on `monero-wallet.gui.log`. The bold parts indicate that the GUI is trying to connect to a local daemon when on the Receive tab, maybe?

> 2018-04-05 13:00:20.150	7668	WARN 	net	contrib/epee/include/net/net_helper.h:188	Some problems at connect, message: No connection could be made because the target machine actively refused it
2018-04-05 13:00:20.150	7668	DEBUG	net.http	contrib/epee/include/net/http_client.h:368	**Failed to connect to localhost:18081**
2018-04-05 13:00:20.150	7668	INFO 	net.http	contrib/epee/include/storages/http_abstract_invoke.h:53	Failed to invoke http request to  /getinfo
2018-04-05 13:00:20.150	7668	DEBUG	net	contrib/epee/include/net/net_helper.h:515	Problems at shutdown: A request to send or receive data was disallowed because the socket is not connected and (when sending on a datagram socket using a sendto call) no address was supplied
2018-04-05 13:00:20.151	7668	DEBUG	net.http	contrib/epee/include/net/http_client.h:365	Reconnecting...
2018-04-05 13:00:21.154	7668	WARN 	net	contrib/epee/include/net/net_helper.h:188	Some problems at connect, message: No connection could be made because the target machine actively refused it
2018-04-05 13:00:21.154	7668	DEBUG	net.http	contrib/epee/include/net/http_client.h:368	**Failed to connect to localhost:18081**
2018-04-05 13:00:21.154	7668	INFO 	net.http	contrib/epee/include/storages/http_abstract_invoke.h:53	Failed to invoke http request to  /getinfo
2018-04-05 13:00:21.154	7668	DEBUG	net	contrib/epee/include/net/net_helper.h:515	Problems at shutdown: A request to send or receive data was disallowed because the socket is not connected and (when sending on a datagram socket using a sendto call) no address was supplied
2018-04-05 13:00:21.156	7668	DEBUG	net.http	contrib/epee/include/net/http_client.h:365	Reconnecting...

## kinghat | 2018-04-06T13:05:00+00:00
same for me. only happening with the remote node enabled. if local, everything is smooth.
win 10 64.

## stoffu | 2018-04-07T05:12:00+00:00
#1286 

## marki555 | 2018-04-07T06:45:53+00:00
I have the same issue. Workaround for me was to use Putty to forward localhost:18081 to node.moneroworld.com:18089 and input localhost:18081 as Remote node into the GUI.

## steffanjensen | 2018-04-07T17:44:37+00:00
How can i port forward with putty?

## marki555 | 2018-04-07T17:54:54+00:00
With putty you need to have some linux server, so that solution is not for everyone.
But even Windows itself can do port forwarding: https://stackoverflow.com/questions/11525703/port-forwarding-in-windows

`netsh interface portproxy add v4tov4 listenport=18081 listenaddress=127.0.0.1 connectport=18089 connectaddress=node.moneroworld.com` (I'm not sure if it accepts hostname or IP only)

To remove: `netsh interface portproxy delete v4tov4 listenport=18081 listenaddress=127.0.0.1`

## Javihache | 2018-07-02T00:32:17+00:00
I have this problem too!

## dEBRUYNE-1 | 2018-07-02T21:00:21+00:00
@Javihache - This particular issue is resolved in GUI v0.12.2.0: 

https://www.reddit.com/r/Monero/comments/8vkx2g/gui_v01220_released/

## dEBRUYNE-1 | 2018-07-03T13:54:11+00:00
+resolved

# Action History
- Created by: keatond | 2018-04-04T16:39:52+00:00
- Closed at: 2018-07-03T14:00:31+00:00
