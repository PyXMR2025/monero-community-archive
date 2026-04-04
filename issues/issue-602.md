---
title: Bitmonero not close connections
source_url: https://github.com/monero-project/monero/issues/602
author: AJIekceu4
assignees: []
labels:
- bug
created_at: '2016-01-07T15:33:34+00:00'
updated_at: '2018-02-16T13:24:40+00:00'
type: issue
status: closed
closed_at: '2018-02-16T13:24:40+00:00'
---

# Original Description
I run public node: 

/bitmonerod --p2p-bind-ip 188.166.61.194 --p2p-bind-port 18080 --rpc-bind-ip 188.166.61.194 --rpc-bind-port 13666...
version: Monero 'Hydrogen Helix'

http://monero.net/images/graph/node_week.png
Sun 12-00 - upgrade from version v0.8.8.7-e175205 to v0.9.0.0-release. 
On this graph tcp connections to port 13666. All this connections is remain "established".
netstat -ntu | grep ESTAB | grep :13666 | awk '{print $5}' | cut -d: -f1 | sort | uniq -c | sort -nr
     **14** 171.5.241.66
      **4** 171.5.245.99
...
blablabla

171.5.241.66 - this is my own IP, i use my remote node from this IP **3 days ago**. Use 'exit' command, when i quit from wallet.
171.5.245.99 - this is my own IP, i use my remote node from this IP **2 days ago**. Use 'exit' command, when i quit from wallet.

netstat -ntu | grep ESTAB | grep :13666 | sort
tcp        0      0 188.166.61.194:13666    171.5.241.66:41626      ESTABLISHED
tcp        0      0 188.166.61.194:13666    171.5.241.66:41640      ESTABLISHED
tcp        0      0 188.166.61.194:13666    171.5.241.66:51419      ESTABLISHED
tcp        0      0 188.166.61.194:13666    171.5.241.66:51420      ESTABLISHED
tcp        0      0 188.166.61.194:13666    171.5.241.66:51452      ESTABLISHED
tcp        0      0 188.166.61.194:13666    171.5.241.66:51453      ESTABLISHED
tcp        0      0 188.166.61.194:13666    171.5.241.66:51461      ESTABLISHED
tcp        0      0 188.166.61.194:13666    171.5.241.66:51486      ESTABLISHED
tcp        0      0 188.166.61.194:13666    171.5.241.66:51487      ESTABLISHED
tcp        0      0 188.166.61.194:13666    171.5.241.66:51488      ESTABLISHED
tcp        0      0 188.166.61.194:13666    171.5.241.66:51489      ESTABLISHED
tcp        0      0 188.166.61.194:13666    171.5.241.66:51492      ESTABLISHED
tcp        0      0 188.166.61.194:13666    171.5.241.66:54915      ESTABLISHED
tcp        0      0 188.166.61.194:13666    171.5.241.66:54916      ESTABLISHED
tcp        0      0 188.166.61.194:13666    171.5.245.99:53898      ESTABLISHED
tcp        0      0 188.166.61.194:13666    171.5.245.99:53900      ESTABLISHED
tcp        0      0 188.166.61.194:13666    171.5.245.99:53901      ESTABLISHED
tcp        0      0 188.166.61.194:13666    171.5.245.99:53902      ESTABLISHED
...
blablabla

Why all this connection not closed after 2-3 days of inactive? With other service (apache) i don't see any problem with not closed connections.


# Discussion History
## moneromooo-monero | 2016-02-06T13:39:10+00:00
If you run just bitmonerod, and no wallet, do you see socket leaks like this if you run repeatedly:

curl -X POST http://127.0.0.1:28081/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_connections","parms":{}}' -H 'Content-Type: application/json'

Adapt the IP address and port to your RPC connection.

I don't see any leaking sockets here. Which boost version are you using ?


## AJIekceu4 | 2016-02-08T01:05:03+00:00
After updating libboost from 1.55 to 1.59 and recompiling bitmonerod from source - seems all OK.


## moneromooo-monero | 2016-02-20T18:52:50+00:00
For whoever still has the bug, this is a patch that adds logs that hopefully can help. If you run with it, it needs starting the daemon with --log-level 1.

http://fpaste.org/326679/99460414/raw/


## moneromooo-monero | 2016-02-26T21:30:57+00:00
This may not be related to the timing out handshakes, as first thought. I can now replicate the timeouts by forcing an error path in the protocol, so the connection gets dropped, and the peer times out. This does not end up in leaking sockets though.


## moneromooo-monero | 2016-02-27T13:28:27+00:00
Can you please try again with the patch here: http://fpaste.org/330341/14565796/raw/

It replaces the previous patch. Run with --log-level 1

I will need to know the local port of the lingering connections (ie, as shown by netstat)


## moneromooo-monero | 2016-02-28T12:56:43+00:00
Possible fix: http://fpaste.org/330766/66641701/raw/


## moneromooo-monero | 2016-02-28T23:08:22+00:00
The above was not thread safe, this should make it so: http://fpaste.org/330911/70084414/


## moneromooo-monero | 2016-03-06T18:53:48+00:00
Again, a new patch which replaces the previous ones: http://fpaste.org/334868/57290305/

I think I've found a couple issues. One is fixed in this patch, the other not yet. If the logs go my way, I will fix that second one too (fixing the second one now would hide whether the first is fixed).

Please run with --log-level 1 again.


## moneromooo-monero | 2016-03-20T12:30:41+00:00
If anyone else wants to test, the latest patch is now at https://github.com/moneromooo-monero/bitmonero/tree/leaking-sockets and includes hyc's race fixes for db errors.


## ghost | 2016-10-03T01:08:44+00:00
Hi @moneromooo-monero, has this been folded into core since your post or should I still pick up the patch from hyc's repo?


## moneromooo-monero | 2016-10-10T16:59:13+00:00
Looks like the bug fix one git merged, but not the belt and braces one, since it doesn't address the root cause.


## AJIekceu4 | 2016-10-10T17:14:31+00:00
In the version 'Wolfram Warptangent' (v0.10.0.0-80c5de9)
Problem still exist. 


## ghost | 2016-12-15T20:01:24+00:00
@AJIekceu4 with @vtnerd's thread changes for 0.10.1, would you now try with 0.10.1 and let us know?

## vtnerd | 2016-12-15T23:19:37+00:00
My changes should have no affect on this (haven't completely changed the background tasking code). Although, if it somehow fixed it, celebrate.

## AJIekceu4 | 2016-12-18T13:10:09+00:00
Hello all, i use new version 3 days and at this time no problem with connections, but may be it is just coincidence. I will test it few weeks more and make feedback here.

## AJIekceu4 | 2017-01-25T19:09:03+00:00
I test it and unfortunally nothing change. Some connections still not closing.

## moneromooo-monero | 2017-02-19T18:43:04+00:00
With current master, we can have a lot better information, as the old _info type logs are now going into the normal log. Can you try again with this setting please: --log-level 2,\*net\*:3

## moneromooo-monero | 2017-02-19T18:47:30+00:00
Along with a note saying which IP leaked at what time if known, as the logs may be pretty large :)

## AJIekceu4 | 2017-02-26T19:12:45+00:00
OK, i will post information later, when (if ;) detect this bug again in new version.

## AJIekceu4 | 2017-02-27T16:35:44+00:00
netstat -ntu | grep ESTAB | grep :13666
tcp        0      0 188.166.61.194:13666    188.166.61.194:47858    ESTABLISHED
tcp        0      0 188.166.61.194:13666    188.166.61.194:47859    ESTABLISHED
tcp        0      0 188.166.61.194:47858    188.166.61.194:13666    ESTABLISHED
tcp        0      0 188.166.61.194:47859    188.166.61.194:13666    ESTABLISHED
tcp        0      0 188.166.61.194:13666    91.211.144.242:56812    ESTABLISHED

91.211.144.242 - my own IP and no active connection to rpc port between my pc and my remote node.

Log file (not from start, but from moment, when problem connection detected, port 56812, ip 91.211.144.242):
http://monero.net/logs.7z

cat /root/public_node/bitmonero.log-2017-02-27-11-23-11 | grep 56812
2017-02-27 10:33:27.906 [RPC1]  INFO    net     contrib/epee/include/net/abstract_tcp_server2.inl:270    connection type RPC 188.166.61.194:13666 <--> 91.211.144.242:56812

daemon - Monero 'Wolfram Warptangent' (v0.10.2.1-release)
wallet - Monero 'Wolfram Warptangent' (v0.10.1.0-29735c8)

## moneromooo-monero | 2017-02-28T22:40:32+00:00
Seems even less helpful than before. That bug's a real stinker :(

## AJIekceu4 | 2017-05-12T20:39:49+00:00
I change server:
Old server:  3.2.0-4-amd64 #1 SMP Debian 3.2.54-2 x86_64 GNU/Linux
New server: 4.8.0-49-generic #52~16.04.1-Ubuntu SMP Thu Apr 20 10:55:59 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux
First server and second is VDS (common in both cases), not physical server.
And... nothing change :(

How reproduce bug:
Connect to remote node with some wallet, wait until "Background refresh thread started" and after ~5 hours type "exit" on wallet-cli. And after this on daemon side appears 1 not closed connection, like this:
> tcp        0      0 172.31.xxx.xxx:13666      91.xxx.xxx.xxx:38006    ESTABLISHED

I log all network data between my pc and remote node (via tcpflow) and check this connection data transfer (to 38006 port and from 38006 port):

This is from my pc to remote node
> GET /getheight HTTP/1.1
> Host: node.monero.net
> Content-Length: 4
> {
> }

This is answer from remote node to my pc:
> HTTP/1.1 200 Ok
> Server: Epee-based
> Content-Length: 44
> Content-Type: application/json
> Last-Modified: Fri, 12 May 2017 14:34:33 GMT
> Accept-Ranges: bytes
> 
> {
>   "height": 1308576,
>   "status": "OK"
> }

And _this is ALL network activity for this connection (port 38006) for 5 hours, while my wallet-cli was active_. Wallet-cli create separate connection only for this **one** getheight query and after few hours this connection became zombie on  daemon side ;)
If this connection get only  "height" for 1 time and not using anymore (for fully sync wallet), why it don't automatically closed by wallet-cli after successfully answer or it must be used for anything else?
As i can see, if i start sync wallet from 0, getheight  occurs every ~30 second until it fully sync and after this data transfer also stopped, connection remain established and not used by wallet-cli.

## moneromooo-monero | 2017-06-30T16:39:12+00:00
Can you try this branch ?
https://github.com/moneromooo-monero/bitmonero/tree/socket-error-shutdown

## AJIekceu4 | 2017-07-01T13:43:53+00:00
Hello. I am testing it now. I will post some info after few days of using this version ;)

## AJIekceu4 | 2017-07-01T19:40:01+00:00
After some time, i get this error and monerod stopped:

***
2017-07-01 18:31:04.956  [P2P9]  INFO    net.p2p.msg     src/cryptonote_protocol/cryptonote_protocol_handler.inl:1017    [92.135.206.9:60040 INC] Received NOTIFY_REQUEST_CHAIN (27 blocks
2017-07-01 18:31:04.975  [P2P4]  DEBUG   net     contrib/epee/include/net/levin_protocol_handler_async.h:394     [92.135.206.9:18080 OUT] LEVIN_PACKET_RECIEVED. [len=38, flags2, r?=0, cmd = 1003, v=1
2017-07-01 18:31:04.975  [P2P4]  ERROR   net.p2p src/p2p/net_node.inl:1555       [92.135.206.9:18080 OUT] back ping invoke wrong response "OK" from92.135.206.9:18080, hsh_peer_id=5b2b527fefe904a0, rsp.peer_id=c1825469c16019a6
***

This is last line,after this monerod stop work:
> [92.135.206.9:18080 OUT] back ping invoke wrong response "OK" from92.135.206.9:18080, hsh_peer_id=5b2b527fefe904a0, rsp.peer_id=c1825469c16019a6

## moneromooo-monero | 2017-10-19T16:08:08+00:00
Can you try https://github.com/monero-project/monero/pull/2685 ?

## AJIekceu4 | 2017-10-20T17:10:45+00:00
Testing it now. I will report info few days later.

## AJIekceu4 | 2017-10-22T15:40:49+00:00
Nothing change. I still can reproduce bug with this:

> How reproduce bug:
Connect to remote node with some wallet, wait until "Background refresh thread started" and after ~5 hours type "exit" on wallet-cli. And after this on daemon side appears 1 not closed connection, like this:

## dEBRUYNE-1 | 2018-01-08T12:27:56+00:00
+bug

## hyc | 2018-02-11T22:07:57+00:00
I find it strange that the wallet client can cleanly exit and yet the kernel on the monerod side still sees the connection in ESTABLISHED state instead of e.g. TIME_WAIT or some other pending-close state. I suggest we turn on KEEPALIVE on the sockets; that ought to get the kernel to eventually notice the connection is dead.

# Action History
- Created by: AJIekceu4 | 2016-01-07T15:33:34+00:00
- Closed at: 2018-02-16T13:24:40+00:00
