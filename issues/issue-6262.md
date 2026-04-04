---
title: monerod sometimes stops accepting incoming RPC connections
source_url: https://github.com/monero-project/monero/issues/6262
author: AJIekceu4
assignees: []
labels: []
created_at: '2019-12-28T15:19:46+00:00'
updated_at: '2022-07-16T15:55:48+00:00'
type: issue
status: closed
closed_at: '2022-07-16T15:55:47+00:00'
---

# Original Description
Hello all. I run public node and have problem with it. After some time after monerod was started, it stop serving incoming connections to restricted rpc port.

> help
> Monero 'Carbon Chamaeleon' (v0.15.0.1-release)

> status
> Height: 1998815/1998815 (100.0%) on mainnet, not mining, net hash 1.03 GH/s, v12, up to date, 8(out)+60(in) connections, uptime 1d 21h 27m 17s

> uname -a
> Linux eu1.node.monero.net 4.15.0-72-generic #81-Ubuntu SMP Tue Nov 26 12:20:02 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux

Startup command (with log-level 2 to catch this problem):

> screen -d -m -S public_node /monero/monerod --p2p-bind-ip 185.152.65.135 --rpc-bind-ip 185.152.65.135 --confirm-external-bind --rpc-bind-port=13666 --rpc-restricted-bind-port=18081 --public-node --log-level=2 --max-log-file-size=0 --data-dir /root/public_node/ --limit-rate-up=131072 --limit-rate-down=131072

Access to port 13666 is closed by iptables and only my own service have access to this port.
Access to port 18081 is available for all. 

After some time, monerod stops accepting incoming RPC connections from all IPs to port 18081 (but port 13666 is still working good, i see it, because my service make 1 RPC connections every 10 seconds to this port). Also i have another service which make 1 connection every 60 seconds to public port 18081 and sometimes it just stop working (together with all RPC clients).  For example today it was already 2 times.

95.216.x.x - my service, 1 RPC connections every 60 seconds to 18081 port. Last successful connections was 2019-12-28 02:13:01 and next only 2 hours later at  2019-12-28 04:26:57. Also all RPC clients was disconnected from the node (i also store number of active RPC clients  and see problem in my database), i am also have complain from one of users who have been used this node in this period of time. So, problem not local.

> cat /root/public_node/bitmonero.log | grep '2019-12-28' | grep '185.152.65.135:18081 <--> 95.216.x.x'

> ...
> 2019-12-28 02:11:01.467	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:45224 (via 95.216.x.x:45224)
> 2019-12-28 02:12:01.708	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:45228 (via 95.216.x.x:45228)
> 2019-12-28 02:13:01.205	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:45232 (via 95.216.x.x:45232)
> 2019-12-28 04:26:57.701	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:45234 (via 95.216.x.x:45234)
> 2019-12-28 04:26:57.701	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:45238 (via 95.216.x.x:45238)
> 2019-12-28 04:26:57.702	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:45244 (via 95.216.x.x:45244)
> 2019-12-28 04:26:57.703	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:45248 (via 95.216.x.x:45248)
> 2019-12-28 04:26:57.706	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:45250 (via 95.216.x.x:45250)
> ...

But, at this same time another my service (195.201.x.x) have access to port 13666 every 10 seconds without any problem all this time:

> cat /root/public_node/bitmonero.log | grep '185.152.65.135:13666 <--> 195.201.x.x' | grep '2019-12-28 02:1'

> ...
> 2019-12-28 02:12:51.615	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:13666 <--> 195.201.x.x:36886 (via 195.201.x.x:36886)
> 2019-12-28 02:13:01.692	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:13666 <--> 195.201.x.x:36888 (via 195.201.x.x:36888)
> 2019-12-28 02:13:11.698	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:13666 <--> 195.201.x.x:36890 (via 195.201.x.x:36890)
> 2019-12-28 02:13:21.698	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:13666 <--> 195.201.x.x:36892 (via 195.201.x.x:36892)
> 2019-12-28 02:13:31.706	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:13666 <--> 195.201.x.x:36894 (via 195.201.x.x:36894)
> 2019-12-28 02:13:41.703	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:13666 <--> 195.201.x.x:36896 (via 195.201.x.x:36896)
> 2019-12-28 02:13:51.707	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:13666 <--> 195.201.x.x:36898 (via 195.201.x.x:36898)
> 2019-12-28 02:14:01.782	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:13666 <--> 195.201.x.x:36900 (via 195.201.x.x:36900)
> 2019-12-28 02:14:11.798	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:13666 <--> 195.201.x.x:36904 (via 195.201.x.x:36904)
> 2019-12-28 02:14:21.798	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:13666 <--> 195.201.x.x:36906 (via 195.201.x.x:36906)
> 2019-12-28 02:14:31.797	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:13666 <--> 195.201.x.x:36908 (via 195.201.x.x:36908)
> 2019-12-28 02:14:41.792	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:13666 <--> 195.201.x.x:36910 (via 195.201.x.x:36910)
> 2019-12-28 02:14:51.785	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:13666 <--> 195.201.x.x:36912 (via 195.201.x.x:36912)
> 2019-12-28 02:15:01.877	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:13666 <--> 195.201.x.x:36914 (via 195.201.x.x:36914)
> 2019-12-28 02:15:11.887	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:13666 <--> 195.201.x.x:36948 (via 195.201.x.x:36948)
> 2019-12-28 02:15:21.889	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:13666 <--> 195.201.x.x:36964 (via 195.201.x.x:36964)
> 2019-12-28 02:15:21.923	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:13666 <--> 195.201.x.x:36966 (via 195.201.x.x:36966)
> ...

I also have catch this problem when it have been appears at second time and nothing in bitmonero.log related to client IP:

Client:
> telnet eu1.node.monero.net 18081
> Trying 185.152.65.135...
> telnet: Unable to connect to remote host: Connection timed out

Node:
> tcpdump -nn | grep '95.213.x.x'
> tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
> listening on eno1, link-type EN10MB (Ethernet), capture size 262144 bytes
> 14:02:11.347708 IP 95.213.x.x.19125 > 185.152.65.135.18081: Flags [S], seq 2270572889, win 29200, options [mss 1460,sackOK,TS val 3358958909 ecr 0,nop,wscale 7], length 0
> 14:02:12.370911 IP 95.213.x.x.19125 > 185.152.65.135.18081: Flags [S], seq 2270572889, win 29200, options [mss 1460,sackOK,TS val 3358959932 ecr 0,nop,wscale 7], length 0
> 14:02:14.386906 IP 95.213.x.x.19125 > 185.152.65.135.18081: Flags [S], seq 2270572889, win 29200, options [mss 1460,sackOK,TS val 3358961948 ecr 0,nop,wscale 7], length 0
> 14:02:18.578920 IP 95.213.x.x.19125 > 185.152.65.135.18081: Flags [S], seq 2270572889, win 29200, options [mss 1460,sackOK,TS val 3358966140 ecr 0,nop,wscale 7], length 0
> 14:02:26.770894 IP 95.213.x.x.19125 > 185.152.65.135.18081: Flags [S], seq 2270572889, win 29200, options [mss 1460,sackOK,TS val 3358974331 ecr 0,nop,wscale 7], length 0
> ...

But no RPC connection (or any other info related to this IP) in bitmonero.log.

I have full log (set_log 2, about 9 GB) from the moment when node have been started and can send full or part of it to dev without modification, but not in public place ;) 




# Discussion History
## hyc | 2019-12-28T19:04:00+00:00
> telnet eu1.node.monero.net 18081
> Trying 185.152.65.135...
> telnet: Unable to connect to remote host: Connection timed out

If there's not a firewall rule blocking things, this usually means the daemon's listen() backlog limit has been hit. It can happen if there were a lot of connections opened and closed in rapid succession; it will take 2 minutes for the TCP timeouts to clear.

## AJIekceu4 | 2019-12-28T22:03:18+00:00
> > telnet eu1.node.monero.net 18081
> > Trying 185.152.65.135...
> > telnet: Unable to connect to remote host: Connection timed out
> 
> If there's not a firewall rule blocking things, this usually means the daemon's listen() backlog limit has been hit. It can happen if there were a lot of connections opened and closed in rapid succession; it will take 2 minutes for the TCP timeouts to clear.

Thank you for reply. But this problem persist few hours and during all this time my another server (which made 1 NEW connection every 10 seconds, more than 720 new connections for this few hours ) connect to another port 13666 of same node without any problems. Is "daemon's listen() backlog limit" separate for restricted and unrestricted ports?

Also I just noticed, that after fresh start of the node (few seconds after start), in logs i see:

> 2019-12-26 15:54:01.628	[**RPC0**]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:49626 (via 95.216.x.x:49626)
> 2019-12-26 15:55:01.225	[**RPC1**]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:49632 (via 95.216.x.x:49632)

**RPC0** and **RPC1**, and they switch position in logs, BUT after some time, log (for port 18081) looks like this:

> 2019-12-26 21:42:01.976	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:53720 (via 95.216.x.x:53720)
> 2019-12-26 21:43:01.447	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:53726 (via 95.216.x.x:53726)
> 2019-12-26 21:44:01.586	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:53730 (via 95.216.x.x:53730)
> 2019-12-26 21:45:02.113	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:53738 (via 95.216.x.x:53738)
> 2019-12-26 21:46:01.603	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:53744 (via 95.216.x.x:53744)
> 2019-12-26 21:47:02.066	[**RPC0**]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:53748 (via 95.216.x.x:53748)
> 2019-12-26 21:48:01.211	[**RPC0**]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:53750 (via 95.216.x.x:53750)
> 2019-12-26 21:49:01.705	[**RPC0**]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:53756 (via 95.216.x.x:53756)
> 2019-12-26 21:50:01.952	[**RPC0**]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:53762 (via 95.216.x.x:53762)
> 2019-12-26 21:51:01.475	[**RPC0**]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:53818 (via 95.216.x.x:53818)
> **2019-12-26 21:52:01.794**	[**RPC0**]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:53840 (via 95.216.x.x:53840)
...                                            **_(skipped, only RPC0 in log)_**
> **2019-12-26 23:54:02.004**	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:55226 (via 95.216.x.x:55226)
> 2019-12-26 23:55:01.550	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:55232 (via 95.216.x.x:55232)
> 2019-12-26 23:56:01.123	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:55240 (via 95.216.x.x:55240)
> 2019-12-26 23:57:01.591	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:55246 (via 95.216.x.x:55246)
> 2019-12-26 23:58:01.817	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:55250 (via 95.216.x.x:55250)
**2019-12-26 23:59:01.337	[RPC1]**	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:55256 (via 95.216.x.x:55256)
> 2019-12-27 00:00:01.489	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:55258 (via 95.216.x.x:55258)
> 2019-12-27 00:01:02.012	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:55318 (via 95.216.x.x:55318)
> 2019-12-27 00:02:01.227	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:55340 (via 95.216.x.x:55340)
> 2019-12-27 00:04:01.930	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:55348 (via 95.216.x.x:55348)

Only **RPC0** in log until 2019-12-26 23:59:01 (more than 2 hours). After this same situation repeat, but this time only **RPC0** in logs appears almost 9 hours (from 2019-12-27 00:56:35.835 until 2019-12-27 09:44:01.915) in a row and node stop to serving RPC connections:

> 2019-12-27 00:56:35.835	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:55788 (via 95.216.x.x:55788)
> 2019-12-27 00:56:35.843	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:55792 (via 95.216.x.x:55792)
> 2019-12-27 00:56:35.844	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:55794 (via 95.216.x.x:55794)
...                                            **_(skipped, only RPC0 in log)_**
> 2019-12-27 09:41:01.969	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:33718 (via 95.216.x.x:33718)
> 2019-12-27 09:42:01.221	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:33722 (via 95.216.x.x:33722)
> 2019-12-27 09:43:01.705	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:33726 (via 95.216.x.x:33726)
> 2019-12-27 **09:44:01.915**	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:33730 (via 95.216.x.x:33730)
> 2019-12-27 **11:55:52.072**	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:33736 (via 95.216.x.x:33736)
> 2019-12-27 11:55:52.081	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:33742 (via 95.216.x.x:33742)
> 2019-12-27 11:55:52.083	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:33746 (via 95.216.x.x:33746)
> 2019-12-27 11:55:52.086	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:33748 (via 95.216.x.x:33748)

After this (**2019-12-27 11:55:52.072**) in logs appears **ONLY RPC1** more than 24 hours, until i restart node. Does it normal behaviour? Because on another port (13666) on the same node - RPC1 & RPC0 in logs all the time.




## AJIekceu4 | 2019-12-29T10:15:59+00:00
After node restart, same problem again:

> ...(skipped, from node start all OK, working good RPC0&RPC1 in logs until 2019-12-29 09:24:01.
After this time node stop to serving connections  09:27:01...09:44:25. And in 09:44:25 in log appears MULTIPLE connections (45!) in just ONE minute. Some of this connections from my own service (must be 1 rpc connections per 60 seconds). Because of tcp timeout i think, all this connections (which does not closed because tcp timeout) established in one second, right after node became to serve connections.
> 2019-12-29 09:24:01.486	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:38490 (via 95.216.x.x:38490)
> 2019-12-29 09:25:01.225	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:38494 (via 95.216.x.x:38494)
> 2019-12-29 09:26:01.658	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:38500 (via 95.216.x.x:38500)
> 2019-12-29 09:27:01.111	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:38504 (via 95.216.x.x:38504)
> 2019-12-29 09:44:25.122	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:38506 (via 95.216.x.x:38506)
> 2019-12-29 09:44:25.126	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:38510 (via 95.216.x.x:38510)
> 2019-12-29 09:44:25.127	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 194.99.x.x:45750 (via 194.99.x.x:45750)
> 2019-12-29 09:44:25.190	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:38514 (via 95.216.x.x:38514)
> 2019-12-29 09:44:25.422	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 194.99.x.x:45768 (via 194.99.x.x:45768)
> 2019-12-29 09:44:25.607	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 194.99.x.x:45776 (via 194.99.x.x:45776)
> 2019-12-29 09:44:25.640	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 194.99.x.x:45780 (via 194.99.x.x:45780)
> 2019-12-29 09:44:25.643	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:38586 (via 95.216.x.x:38586)
> 2019-12-29 09:44:25.644	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 194.99.x.x:45784 (via 194.99.x.x:45784)
> 2019-12-29 09:44:25.736	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 194.99.x.x:45846 (via 194.99.x.x:45846)
> 2019-12-29 09:44:26.290	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 31.43.x.x:59574 (via 31.43.x.x:59574)
> 2019-12-29 09:44:26.444	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 67.185.x.x:55735 (via 67.185.x.x:55735)
> 2019-12-29 09:44:26.599	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:38588 (via 95.216.x.x:38588)
> 2019-12-29 09:44:26.882	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 31.43.x.x:59660 (via 31.43.x.x:59660)
> 2019-12-29 09:44:27.128	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 31.43.x.x:59740 (via 31.43.x.x:59740)
> 2019-12-29 09:44:27.411	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 31.43.x.x:59800 (via 31.43.x.x:59800)
> 2019-12-29 09:44:27.658	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:38592 (via 95.216.x.x:38592)
> 2019-12-29 09:44:27.967	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 31.43.x.x:59816 (via 31.43.x.x:59816)
> 2019-12-29 09:44:28.458	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 31.43.x.x:59850 (via 31.43.x.x:59850)
> 2019-12-29 09:44:28.916	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 31.43.x.x:59854 (via 31.43.x.x:59854)
> 2019-12-29 09:44:29.346	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:38594 (via 95.216.x.x:38594)
> 2019-12-29 09:44:29.775	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:38598 (via 95.216.x.x:38598)
> 2019-12-29 09:44:29.989	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 31.43.x.x:59950 (via 31.43.x.x:59950)
> 2019-12-29 09:44:30.205	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:38604 (via 95.216.x.x:38604)
> 2019-12-29 09:44:30.481	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 82.196.x.x:12747 (via 82.196.x.x:12747)
> 2019-12-29 09:44:30.758	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 82.196.x.x:52365 (via 82.196.x.x:52365)
> 2019-12-29 09:44:31.034	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:38608 (via 95.216.x.x:38608)
> 2019-12-29 09:44:31.401	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 82.196.x.x:40354 (via 82.196.x.x:40354)
> 2019-12-29 09:44:31.767	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 82.196.x.x:28179 (via 82.196.x.x:28179)
> 2019-12-29 09:44:32.409	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:38610 (via 95.216.x.x:38610)
> 2019-12-29 09:44:32.715	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 82.196.x.x:15874 (via 82.196.x.x:15874)
> 2019-12-29 09:44:33.144	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:38614 (via 95.216.x.x:38614)
> 2019-12-29 09:44:33.450	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 82.196.x.x:40733 (via 82.196.x.x:40733)
> 2019-12-29 09:44:33.665	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 31.43.x.x:60160 (via 31.43.x.x:60160)
> 2019-12-29 09:44:33.945	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:38616 (via 95.216.x.x:38616)
> 2019-12-29 09:44:34.315	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 31.43.x.x:60186 (via 31.43.x.x:60186)
> 2019-12-29 09:44:34.571	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 82.196.x.x:16065 (via 82.196.x.x:16065)
> 2019-12-29 09:44:35.243	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:38672 (via 95.216.x.x:38672)
> 2019-12-29 09:44:35.549	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 82.196.x.x:41232 (via 82.196.x.x:41232)
> 2019-12-29 09:44:35.978	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 31.43.x.x:59478 (via 31.43.x.x:59478)
> 2019-12-29 09:44:36.345	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:38692 (via 95.216.x.x:38692)
> 2019-12-29 09:44:36.751	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 82.196.x.x:16662 (via 82.196.x.x:16662)
> 2019-12-29 09:44:37.059	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 31.43.x.x:59480 (via 31.43.x.x:59480)
> 2019-12-29 09:44:37.061	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 31.43.x.x:59482 (via 31.43.x.x:59482)
> 2019-12-29 09:44:37.061	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:38696 (via 95.216.x.x:38696)
> 2019-12-29 09:44:37.062	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:38698 (via 95.216.x.x:38698)
> 2019-12-29 09:45:01.400	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:38702 (via 95.216.x.x:38702)
> 2019-12-29 09:45:11.309	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 194.242.x.x:54044 (via 194.242.x.x:54044)
> 2019-12-29 09:46:01.982	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:38710 (via 95.216.x.x:38710)
> 2019-12-29 09:47:01.578	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:38716 (via 95.216.x.x:38716)
> 2019-12-29 09:48:01.772	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:38720 (via 95.216.x.x:38720)
> 2019-12-29 09:49:01.326	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:38726 (via 95.216.x.x:38726)
> 2019-12-29 09:49:51.098	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 31.43.x.x:59922 (via 31.43.x.x:59922)
> 2019-12-29 09:50:01.605	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:38732 (via 95.216.x.x:38732)
> 2019-12-29 09:51:01.643	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:38808 (via 95.216.x.x:38808)
> 2019-12-29 09:52:01.859	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:38812 (via 95.216.x.x:38812)
> 2019-12-29 09:52:46.882	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 5.8.x.x:34394 (via 5.8.x.x:34394)
> 2019-12-29 09:53:01.323	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:38818 (via 95.216.x.x:38818)
> 2019-12-29 09:54:01.466	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:38820 (via 95.216.x.x:38820)
> 2019-12-29 09:54:35.966	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 31.43.x.x:60054 (via 31.43.x.x:60054)
> 2019-12-29 09:55:01.681	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:38826 (via 95.216.x.x:38826)

Now i have compiled new version from source and restart the node. Will post any new info.



## AJIekceu4 | 2019-12-29T16:08:03+00:00
With compiled myself version of node same problem. I catch this moment and get connections stats on monerod server:
>       1 LAST_ACK
>       6 CLOSE_WAIT
>       7 LISTEN
>      14 TIME_WAIT
>     116 ESTABLISHED
Also i write small script on my VPS server (another IP, another NET, another Country), which use "get_last_block_header" method every 10 seconds and store status (from RPC answer) to file (to get more precise time of problem).

Again, in log file i see only RPC0 and after some time node stop accepting incoming rpc connections on 18081 port:

> 2019-12-29 15:29:51.910	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 78.47.x.x:50178 (via 78.47.x.x:50178)
> 2019-12-29 15:30:01.264	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:42654 (via 95.216.x.x:42654)
> 2019-12-29 15:30:01.340	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 78.47.x.x:50184 (via 78.47.x.x:50184)
> 2019-12-29 15:30:11.339	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 78.47.x.x:50188 (via 78.47.x.x:50188)
> 2019-12-29 15:30:21.341	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 78.47.x.x:50190 (via 78.47.x.x:50190)
> **2019-12-29 15:30:31.343**	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 78.47.x.x:50196 (via 78.47.x.x:50196)
> **2019-12-29 15:35:32.898**	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 78.47.x.x:50198 (via 78.47.x.x:50198)
> 2019-12-29 15:47:19.458	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 78.47.x.x:50202 (via 78.47.x.x:50202)
> 2019-12-29 15:47:19.729	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 78.47.x.x:50206 (via 78.47.x.x:50206)
> 2019-12-29 15:47:19.730	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 95.216.x.x:42710 (via 95.216.x.x:42710)
> 2019-12-29 15:47:19.732	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 78.47.x.x:50212 (via 78.47.x.x:50212)
> 2019-12-29 15:47:19.733	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 78.47.x.x:50216 (via 78.47.x.x:50216)
> 2019-12-29 15:47:19.734	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 78.47.x.x:50218 (via 78.47.x.x:50218)
> 2019-12-29 15:47:19.736	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 78.47.x.x:50224 (via 78.47.x.x:50224)

I look for time (2019-12-29 15:35:32.898) in log file (set_log 3 already :) and see this:

> 2019-12-29 15:35:32.898	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 78.47.x.x:50198 (via 78.47.x.x:50198)
> 2019-12-29 15:35:32.898	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 589884 < 590181 (last time 589885)
> 2019-12-29 15:35:32.898	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 589885 < 590181 (last time 589886)
> 2019-12-29 15:35:32.898	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 589886 < 590181 (last time 589887)
> 2019-12-29 15:35:32.898	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 589887 < 590181 (last time 589888)
> 2019-12-29 15:35:32.898	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 589888 < 590181 (last time 589889)
> 2019-12-29 15:35:32.898	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 589889 < 590181 (last time 589890)
> 2019-12-29 15:35:32.898	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 589890 < 590181 (last time 589891)
> 2019-12-29 15:35:32.898	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 589891 < 590181 (last time 589892)
> 2019-12-29 15:35:32.898	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 589892 < 590181 (last time 589893)
> 2019-12-29 15:35:32.898	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 589893 < 590181 (last time 589894)
> 2019-12-29 15:35:32.898	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 589894 < 590181 (last time 589895)
> 2019-12-29 15:35:32.898	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 589895 < 590181 (last time 589896)
> 2019-12-29 15:35:32.898	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 589896 < 590181 (last time 589897)
> 2019-12-29 15:35:32.898	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 589897 < 590181 (last time 589898)
> 2019-12-29 15:35:32.898	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 589898 < 590181 (last time 589899)
> 2019-12-29 15:35:32.899	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 589899 < 590181 (last time 589900)
> 2019-12-29 15:35:32.899	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 589900 < 590181 (last time 589901)
> 2019-12-29 15:35:32.899	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 589901 < 590181 (last time 589902)
> 2019-12-29 15:35:32.899	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 589902 < 590181 (last time 589903)
> 2019-12-29 15:35:32.899	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 589903 < 590181 (last time 589904)
> 2019-12-29 15:35:32.899	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 589904 < 590181 (last time 589905)
> 2019-12-29 15:35:32.899	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 589905 < 590181 (last time 589906)
> 2019-12-29 15:35:32.899	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 589906 < 590181 (last time 589907)
> 2019-12-29 15:35:32.899	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 589907 < 590181 (last time 589908)
> 2019-12-29 15:35:32.899	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 589908 < 590181 (last time 589909)
> 2019-12-29 15:35:32.899	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 589909 < 590181 (last time 589910)
> 2019-12-29 15:35:32.899	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 589910 < 590181 (last time 589911)
> 2019-12-29 15:35:32.899	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 589911 < 590181 (last time 589912)
> 2019-12-29 15:35:32.899	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 589912 < 590181 (last time 589913)
> 2019-12-29 15:35:32.899	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 589913 < 590181 (last time 589914)
> 2019-12-29 15:35:32.899	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 589914 < 590181 (last time 589915)
> 2019-12-29 15:35:32.900	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 589915 < 590181 (last time 589916)
> 2019-12-29 15:35:32.900	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 589916 < 590181 (last time 589917)
> 2019-12-29 15:35:32.900	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 589917 < 590181 (last time 589918)
> 2019-12-29 15:35:32.900	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 589918 < 590181 (last time 589919)
> 2019-12-29 15:35:32.900	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 589919 < 590181 (last time 589920)
> 2019-12-29 15:35:32.900	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 589920 < 590181 (last time 589921)
> 2019-12-29 15:35:32.900	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 589921 < 590181 (last time 589922)
> 2019-12-29 15:35:32.900	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 589922 < 590181 (last time 589923)
> 2019-12-29 15:35:32.900	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 589923 < 590181 (last time 589924)
> 2019-12-29 15:35:32.900	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 589924 < 590181 (last time 589925)
> 2019-12-29 15:35:32.900	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 589925 < 590181 (last time 589926)
> 2019-12-29 15:35:32.900	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 589926 < 590181 (last time 589927)
> 2019-12-29 15:35:32.900	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 589927 < 590181 (last time 589928)
> 2019-12-29 15:35:32.900	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 589928 < 590181 (last time 589929)
> 2019-12-29 15:35:32.900	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 589929 < 590181 (last time 589930)
> 2019-12-29 15:35:32.900	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 589930 < 590181 (last time 589931)
> 2019-12-29 15:35:32.901	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 589931 < 590181 (last time 589932)
> 2019-12-29 15:35:32.901	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 589932 < 590181 (last time 589933)
> 2019-12-29 15:35:32.901	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 589933 < 590181 (last time 589934)
**...skipped, repeated message 'Moving counter buffer by 1 second' (>240 times)**
> 2019-12-29 15:35:32.915	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 590177 < 590181 (last time 590178)
> 2019-12-29 15:35:32.915	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 590178 < 590181 (last time 590179)
> 2019-12-29 15:35:32.915	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 590179 < 590181 (last time 590180)
> 2019-12-29 15:35:32.915	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 590180 < 590181 (last time 590181)
> 2019-12-29 15:35:32.916	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:208	Throttle throttle_speed_in: packet of ~367b  (from 367 b) Speed AVG=   0[w=9.346]    0[w=9.346] /  Limit=16 KiB/sec  [367 0 0 0 0 0 0 0 0 0 ]
> 2019-12-29 15:35:32.916	[RPC1]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:208	Throttle <<< global-IN: packet of ~367b  (from 367 b) Speed AVG= 240[w=9.364]  240[w=9.364] /  Limit=131072 KiB/sec  [5839 37040 77593 509 3403 28854 83994 65388 953538 1048650 ]

Is it normal?


## Gingeropolous | 2019-12-29T19:07:20+00:00
i don't know if its normal, but one thing I would try is removing your port 13666 service. Perhaps monerod is having trouble with the 2 port bindings? The two port bindings is relatively new. 

Basically check to see if you get the same errors using

--rpc-bind-port 18081 --restricted-rpc

## AJIekceu4 | 2019-12-29T20:14:26+00:00
> i don't know if its normal, but one thing I would try is removing your port 13666 service. Perhaps monerod is having trouble with the 2 port bindings? The two port bindings is relatively new.
> 
> Basically check to see if you get the same errors using
> 
> --rpc-bind-port 18081 --restricted-rpc

Already do it. Remove " --limit-rate-up=131072 --limit-rate-down=131072" did not help. About 4 hours no problem with node (with --rpc-bind-port 18081 --restricted-rpc). Will post update tomorrow.

## AJIekceu4 | 2019-12-30T09:43:30+00:00
Unfortunately it did not help and the problem is still present. I also carefully examined the log file and found that log looks like
**for RPC0:**

> ... (skipped)
> 2019-12-29 20:45:35.520	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:683	do_send_chunk() NOW SENSD: packet=276 B
> 2019-12-29 **20:45:37**.434	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:769	[45.112.x.x:54332 INC] connection timeout, closing
> 2019-12-29 **21:32:32**.075	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:1263	handle_accept
> 2019-12-29 21:32:32.075	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:1287	New server for RPC connections, SSL autodetection
> 2019-12-29 21:32:32.075	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:903	set m_connection_type = RPC 

look for this ip address in the logs (45.112.x.x):

> ...
> 2019-12-29 20:40:36.824	[RPC0]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:95	HTTP [45.112.x.x] GET /get_transaction_pool_hashes.bin
> 2019-12-29 20:40:36.824	[RPC0]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:124	[45.112.x.x:54332 INC] calling /get_transaction_pool_hashes.bin
> 2019-12-29 20:40:37.124	[RPC0]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:95	HTTP [45.112.x.x] GET /gettransactions
> 2019-12-29 20:40:37.124	[RPC0]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:109	[45.112.x.x:54332 INC] calling /gettransactions
> 2019-12-29 20:40:37.433	[RPC0]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:95	HTTP [45.112.x.x] GET /getblocks.bin
> 2019-12-29 20:40:37.433	[RPC0]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:101	[45.112.x.x:54332 INC] calling /getblocks.bin
> 2019-12-29 **20:45:3**7.434	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:769	[45.112.x.x:54332 INC] connection timeout, closing
> 2019-12-29 **21:32:25**.439	[RPC1]	DEBUG	net.conn	contrib/epee/src/connection_basic.cpp:184	Destructing connection #154 to 45.112.x.x

Next problem:

> ... (skipped)
> 2019-12-30 00:30:30.370	[RPC0]	INFO	perf.daemon.rpc	src/common/perf_timer.cpp:156	PERF       34    get_blocks
> 2019-12-30 00:30:30.370	[RPC0]	DEBUG	daemon.rpc	src/rpc/core_rpc_server.h:101	/getblocks.bin() processed with 0/0/0ms
> 2019-12-30 00:30:30.370	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:683	do_send_chunk() NOW SENSD: packet=276 B
> 2019-12-30 **00:30:30**.613	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:769	[217.77.x.x:50462 INC] connection timeout, closing
> 2019-12-30 **08:04:32**.001	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:1263	handle_accept
> 2019-12-30 08:04:32.001	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:1287	New server for RPC connections, SSL autodetection
> 2019-12-30 08:04:32.002	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:903	set m_connection_type = RPC 

look for this ip address in the logs (217.77.x.x):

> ...
> 2019-12-30 00:25:20.509	[RPC0]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:95	HTTP [217.77.x.x] GET /gettransactions
> 2019-12-30 00:25:20.509	[RPC0]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:109	[217.77.x.x:50462 INC] calling /gettransactions
> 2019-12-30 00:25:20.559	[RPC0]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:95	HTTP [217.77.x.x] GET /getblocks.bin
> 2019-12-30 00:25:20.560	[RPC0]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:101	[217.77.x.x:50462 INC] calling /getblocks.bin
> 2019-12-30 00:25:30.612	[RPC0]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:95	HTTP [217.77.x.x] GET /getheight
> 2019-12-30 00:25:30.612	[RPC0]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:99	[217.77.x.x:50462 INC] calling /getheight
> 2019-12-30 **00:30:30**.613	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:769	[217.77.x.x:50462 INC] connection timeout, closing
> 2019-12-30 **08:04:25**.199	[RPC1]	DEBUG	net.conn	contrib/epee/src/connection_basic.cpp:184	Destructing connection #4060 to 217.77.x.x

**for RPC1:**

> ... (skipped)
> 2019-12-29 20:14:58.198	[RPC1]	DEBUG	daemon.rpc	src/rpc/core_rpc_server.h:101	/getblocks.bin() processed with 0/1/0ms
> 2019-12-29 20:14:58.198	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:683	do_send_chunk() NOW SENSD: packet=276 B
> 2019-12-29 **20:14:59**.860	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:769	[23.129.x.x:13685 INC] connection timeout, closing
> 2019-12-29 **21:25:20**.553	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:1263	handle_accept
> 2019-12-29 21:25:20.553	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:1287	New server for RPC connections, SSL autodetection
> 2019-12-29 21:25:20.553	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:903	set m_connection_type = RPC 

look for this ip address in the logs (23.129.x.x):

> ...
> 2019-12-29 20:09:48.701	[RPC0]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:95	HTTP [23.129.x.x] GET /getblocks.bin
> 2019-12-29 20:09:48.702	[RPC0]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:101	[23.129.x.x:13685 INC] calling /getblocks.bin
> 2019-12-29 20:09:59.172	[RPC1]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:95	HTTP [23.129.x.x] GET /get_transaction_pool_hashes.bin
> 2019-12-29 20:09:59.172	[RPC1]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:124	[23.129.x.x:13685 INC] calling /get_transaction_pool_hashes.bin
> 2019-12-29 20:09:59.859	[RPC1]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:95	HTTP [23.129.x.x] GET /getblocks.bin
> 2019-12-29 20:09:59.859	[RPC1]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:101	[23.129.x.x:13685 INC] calling /getblocks.bin
> 2019-12-29 **20:14:59**.860	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:769	[23.129.x.x:13685 INC] connection timeout, closing
> 2019-12-29 **21:25:20**.556	[RPC1]	DEBUG	net.conn	contrib/epee/src/connection_basic.cpp:184	Destructing connection #181 to 23.129.x.x

Next problem:

> ... (skipped)
> 2019-12-30 00:22:01.764	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:1287	New server for RPC connections, SSL autodetection
> 2019-12-30 00:22:01.764	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:903	set m_connection_type = RPC 
> 2019-12-30 00:22:01.765	[RPC1]	DEBUG	net.conn	contrib/epee/src/connection_basic.cpp:153	Spawned connection #4022 to 0.0.0.0 currently we have sockets count:8
> 2019-12-30 00:22:01.765	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:111	test, connection constructor set m_connection_type=1
> 2019-12-30 00:22:01.766	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 185.152.65.135:18081 <--> 195.201.x.x:52460 (via 195.201.x.x:52460)
> 2019-12-30 **00:22:03**.416	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:769	[108.211.x.x:49876 INC] connection timeout, closing
> 2019-12-30 **00:38:59**.104	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:1263	handle_accept
> 2019-12-30 00:38:59.104	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:1287	New server for RPC connections, SSL autodetection
> 2019-12-30 00:38:59.104	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:903	set m_connection_type = RPC

look for this ip address in the logs (108.211.x.x):

> ...
> 2019-12-30 00:17:03.214	[RPC1]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:95	HTTP [108.211.x.x] GET /gettransactions
> 2019-12-30 00:17:03.214	[RPC1]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:109	[108.211.x.x:49876 INC] calling /gettransactions
> 2019-12-30 00:17:03.414	[RPC1]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:95	HTTP [108.211.x.x] GET /getblocks.bin
> 2019-12-30 00:17:03.415	[RPC1]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:101	[108.211.x.x:49876 INC] calling /getblocks.bin
> 2019-12-30 00:22:03.416	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:769	[108.211.x.x:49876 INC] connection timeout, closing

Next problem:

> ... (skipped)
> 2019-12-30 08:24:11.386	[RPC1]	DEBUG	net.ssl	contrib/epee/src/net_ssl.cpp:396	SSL detection buffer, 217 bytes: 80 79 83 84 32 47 106 115 111
> 2019-12-30 08:24:11.386	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:466	That does not look like SSL
> 2019-12-30 08:24:11.386	[RPC1]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:95	HTTP [195.201.x.x] POST /json_rpc
> 2019-12-30 08:24:11.387	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:683	do_send_chunk() NOW SENSD: packet=268 B
> 2019-12-30 **08:24:14**.461	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:769	[185.103.x.x:56258 INC] connection timeout, closing
> 2019-12-30 **08:40:31**.357	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:1263	handle_accept
> 2019-12-30 08:40:31.357	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:1287	New server for RPC connections, SSL autodetection
> 2019-12-30 08:40:31.357	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:903	set m_connection_type = RPC 
> 2019-12-30 08:40:31.358	[RPC1]	DEBUG	net.conn	contrib/epee/src/connection_basic.cpp:153	Spawned connection #10961 to 0.0.0.0 currently we have sockets count:4
> 2019-12-30 08:40:31.358	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:111	test, connection constructor set m_connection_type=1

look for this ip address in the logs (185.103.x.x):

> ...
> 2019-12-30 08:19:03.909	[RPC0]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:95	HTTP [185.103.x.x] GET /getblocks.bin
> 2019-12-30 08:19:03.909	[RPC0]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:101	[185.103.x.x:56258 INC] calling /getblocks.bin
> 2019-12-30 08:19:14.155	[RPC1]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:95	HTTP [185.103.x.x] GET /get_transaction_pool_hashes.bin
> 2019-12-30 08:19:14.155	[RPC1]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:124	[185.103.x.x:56258 INC] calling /get_transaction_pool_hashes.bin
> 2019-12-30 08:19:14.460	[RPC0]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:95	HTTP [185.103.x.x] GET /getblocks.bin
> 2019-12-30 08:19:14.460	[RPC0]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:101	[185.103.x.x:56258 INC] calling /getblocks.bin
> 2019-12-30 08:24:14.461	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:769	[185.103.x.x:56258 INC] connection timeout, closing

So every time when both RPC0 and RPC1 stop to working, node stops accepting incoming RPC connections. And every time last line in log is `contrib/epee/include/net/abstract_tcp_server2.inl:769 connection timeout, closing`
Also all this IP (with connection timeout not my own, but some node clients). Hope this will help to find the bug.


## Gingeropolous | 2019-12-30T14:49:08+00:00
have you tried compiling and running the current master? Sometimes a bug may have been fixed without anyone really noticing it. 

## moneromooo-monero | 2019-12-30T14:56:48+00:00
Add perf*:INFO (gives you a log when a RPC ends). What you describe can happen if a RPC throws and the exception is not caught. The RPC server thread then dies. Your log does not show exceptions, but maybe you just don't have libunwind compiled in ?

## AJIekceu4 | 2019-12-30T19:27:35+00:00
> have you tried compiling and running the current master? Sometimes a bug may have been fixed without anyone really noticing it.

Yes. Right after my 3 message in this issue thread.

> Add perf*:INFO (gives you a log when a RPC ends). What you describe can happen if a RPC throws and the exception is not caught. The RPC server thread then dies. Your log does not show exceptions, but maybe you just don't have libunwind compiled in ?

This is logs for this IPs (after which RPC server thread die) from node start until node switch off by using "exit" command (2019-12-30 10:00:37). I only replace to x.x last two octet in ip address, no other modification.

45.112.x.x: [https://xmr.ru/45.112.x.x.txt](https://xmr.ru/45.112.x.x.txt)

217.77.x.x: [https://paste.debian.net/1123217/](https://paste.debian.net/1123217/)

23.129.x.x: [https://xmr.ru/23.129.x.x.txt](https://xmr.ru/23.129.x.x.txt)

108.211.x.x: [https://paste.debian.net/1123219/](https://paste.debian.net/1123219/)

185.103.x.x: [https://paste.debian.net/1123221/](https://paste.debian.net/1123221/)

and full log with string "perf.daemon.rpc" (11 MB):  [https://xmr.ru/perf.txt](https://xmr.ru/perf.txt)


## AJIekceu4 | 2020-03-23T11:39:05+00:00
In version v0.15.0.5 problem still exist. 

## AJIekceu4 | 2020-06-13T08:19:20+00:00
In version v0.16.0.0 problem still exist.

## AJIekceu4 | 2020-06-27T07:00:27+00:00
In version v0.16.0.1 problem still exist.

## normoes | 2020-07-29T05:11:15+00:00
Could this be connected to: https://github.com/monero-project/monero/issues/6724

## normoes | 2020-07-29T14:23:15+00:00
@AJIekceu4 Have a look at the issue I linked: https://github.com/monero-project/monero/issues/6724

There is some progress. Maybe that also affects your case.

## AJIekceu4 | 2020-07-30T08:01:51+00:00
@normoes thank you for info. I have been compiled this version https://github.com/moneromooo-monero/bitmonero/tree/ex
with third patch, but it did not help with my case. My problem related with number of RPC clients, if it 3-5 clients then this problem can take weeks to appears, but if node have  30-40 RPC clients simultaneously (mostly from light wallet i think) it takes few hours to problem appears again and again.

## AJIekceu4 | 2020-08-14T10:01:37+00:00
In version v0.16.0.3 problem still exist.

## AJIekceu4 | 2020-08-15T10:59:09+00:00
As a temporary solution i have changed in /src/daemon/rpc.h
`if (!m_server.run(2, false))` 
to 
`if (!m_server.run(32, false))`
And recompiled.
Now problem appears not so often when node serve many clients simultaneously 

## AJIekceu4 | 2020-10-10T14:43:41+00:00
In version v0.17.0.0 problem still exist. Without m_server.run modification node stop accepting connections after 3-5 minutes (80-100 RPC clients simultaneously). If i change RPC number to 32 and recompile, then it can work few hours without problem. But, after some time, CPU usage became insane:
![monerod_error](https://user-images.githubusercontent.com/16595267/95657735-bba4db80-0b1e-11eb-9adb-b3b187fbf054.jpg)

If look at daemon logs with 'ERROR" it is look like this:
`...
2020-10-10 14:38:25.260	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.260	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.260	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.260	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.260	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.260	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.260	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.260	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.260	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.260	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.260	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.260	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.260	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.260	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.260	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.260	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.260	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.260	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.260	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.260	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.260	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.260	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.260	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.261	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.261	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.261	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.261	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.261	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.261	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.261	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.261	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.261	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.261	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.261	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.261	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.261	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.261	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.261	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.261	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.261	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.261	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.261	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.261	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.261	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.261	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.261	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.261	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.261	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.261	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.261	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.261	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.261	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.261	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.261	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.261	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.261	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.261	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.261	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.261	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.261	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.261	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.261	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.261	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.261	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.261	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-10 14:38:25.262	[RPC24]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
...`

Seems all RPC threads (which stop working, not only RPC24 it is just one of them) flood this message to log. With set_log 0 CPU usage did not changed.   


## Gingeropolous | 2020-12-17T16:53:50+00:00
@AJIekceu4 , I am experiencing the same problem. I have just been restarting monerod using crontab, which is just hacky. Do your modifications in /src/daemon/rpc.h still "fix" the problem a bit?

## AJIekceu4 | 2020-12-17T17:30:42+00:00
> @AJIekceu4 , I am experiencing the same problem. I have just been restarting monerod using crontab, which is just hacky. Do your modifications in /src/daemon/rpc.h still "fix" the problem a bit?

Hi. This changes in rpc.h still help, because my node (v0.17.1.5) does not stop working every 5 minutes instead it stop accepting connections every 2-4 hours.But there are  direct connection between numbers of active RPC clients and how fast node will die. At this moment my rpc node have about 120-150 connections simultaneously, and my script restart it 6-10 times per 24 hours, because node not accepting new connections. On other hand it use almost 100% of CPU, after this RPC threads "stuck" as i mention in previous message.

## moneromooo-monero | 2020-12-17T22:09:53+00:00
Do you see this happen if you run this on an otherwise unused daemon ?
```
#!/bin/bash

function tcall()
{
  for i in `seq 100`
  do
    curl \
      -X POST "http://127.0.0.1:28081/get_info" \
      -d '{}' \
      -H 'Content-Type: application/json' -o /dev/null -s
  done
}

for i in `seq 20`
do
  tcall &
done

echo "waiting..."
wait

```

I see no leaks running this repeatedly. Which at least tells us it's probably due to one particular RPC.

## Gingeropolous | 2020-12-18T12:59:03+00:00
@moneromooo-monero 

> Which at least tells us it's probably due to one particular RPC.

So one particular RPC connection is causing a ddos? Or there is one particular RPC function that is causing this from normal behavior, and we just don't know what it is?

## AJIekceu4 | 2020-12-18T14:47:00+00:00
> Do you see this happen if you run this on an otherwise unused daemon ?
> 
> ```
> #!/bin/bash
> 
> function tcall()
> {
>   for i in `seq 100`
>   do
>     curl \
>       -X POST "http://127.0.0.1:28081/get_info" \
>       -d '{}' \
>       -H 'Content-Type: application/json' -o /dev/null -s
>   done
> }
> 
> for i in `seq 20`
> do
>   tcall &
> done
> 
> echo "waiting..."
> wait
> ```
> 
> I see no leaks running this repeatedly. Which at least tells us it's probably due to one particular RPC.

I have no problem with node by using this code. Also as i see it is related to some RPC function(s), because 'status' did not break rpc thread, i tested it more than year ago with a thousands of RPC request to my own node. I made few tests today: Download last release version 0.17.1.7 (it have only 2 RPC threads - RPC0 and RPC1) and start this version instead of my own (with 32 RPC threads) with set_log 2.
1) Node started at 13:30:59, full log size 9,6 MB

first RPC thread die at 13:36:06.406, last few lines from log with [RPC1]:
```
...
2020-12-18 13:36:06.334	[RPC1]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:97	HTTP [85.238.xxx.xxx] POST /gettransactions
2020-12-18 13:36:06.334	[RPC1]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:111	[85.238.xxx.xxx:62081 INC] calling /gettransactions
2020-12-18 13:36:06.334	[RPC1]	INFO	perf.daemon.rpc	src/common/perf_timer.cpp:120	PERF             ----------
2020-12-18 13:36:06.334	[RPC1]	DEBUG	daemon.rpc	src/rpc/core_rpc_server.cpp:866	Found 0/74 transactions on the blockchain
2020-12-18 13:36:06.374	[RPC1]	DEBUG	daemon.rpc	src/rpc/core_rpc_server.cpp:936	Found 74/74 transactions in the pool
2020-12-18 13:36:06.374	[RPC1]	DEBUG	daemon.rpc	src/rpc/core_rpc_server.cpp:1059	74 transactions found, 0 not found
2020-12-18 13:36:06.375	[RPC1]	INFO	perf.daemon.rpc	src/common/perf_timer.cpp:156	PERF    40587    get_transactions
2020-12-18 13:36:06.375	[RPC1]	DEBUG	daemon.rpc	src/rpc/core_rpc_server.h:111	/gettransactions processed with 0/41/0ms
2020-12-18 13:36:06.375	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:682	do_send_chunk() NOW SENSD: packet=75946 B
2020-12-18 13:36:06.406	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:779	[58.166.xxx.xxx:50048 INC] connection timeout, closing
```

second RPC thread die at 13:36:07.158, last few lines from log with [RPC0]:
```
...
2020-12-18 13:36:06.966	[RPC0]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:97	HTTP [46.155.xxx.xxx] POST /getblocks.bin
2020-12-18 13:36:06.966	[RPC0]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:103	[46.155.xxx.xxx:12882 INC] calling /getblocks.bin
2020-12-18 13:36:06.966	[RPC0]	INFO	perf.daemon.rpc	src/common/perf_timer.cpp:120	PERF             ----------
2020-12-18 13:36:07.145	[RPC0]	DEBUG	daemon.rpc	src/rpc/core_rpc_server.cpp:631	on_get_blocks: 1000 blocks, 5861 txes, size 3523209
2020-12-18 13:36:07.145	[RPC0]	INFO	perf.daemon.rpc	src/common/perf_timer.cpp:156	PERF   179358    get_blocks
2020-12-18 13:36:07.155	[RPC0]	DEBUG	daemon.rpc	src/rpc/core_rpc_server.h:103	/getblocks.bin() processed with 0/180/9ms
2020-12-18 13:36:07.156	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:682	do_send_chunk() NOW SENSD: packet=4089659 B
2020-12-18 13:36:07.157	[RPC0]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:97	HTTP [174.235.xxx.xxx] POST /json_rpc
2020-12-18 13:36:07.157	[RPC0]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:163	[174.235.xxx.xxx:3169 INC] Calling RPC method get_info
2020-12-18 13:36:07.157	[RPC0]	INFO	perf.daemon.rpc	src/common/perf_timer.cpp:120	PERF             ----------
2020-12-18 13:36:07.157	[RPC0]	INFO	perf.daemon.rpc	src/common/perf_timer.cpp:156	PERF      782    get_info
2020-12-18 13:36:07.157	[RPC0]	DEBUG	daemon.rpc	src/rpc/core_rpc_server.h:163	/json_rpc[get_info] processed with 0/1/0ms
2020-12-18 13:36:07.158	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:682	do_send_chunk() NOW SENSD: packet=1520 B
2020-12-18 13:36:07.158	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:779	[58.166.xxx.xxx:50047 INC] connection timeout, closing
```
After this my script kill process and restarted because it stop to answer to RPC calls.

2) Node started at 13:49:45, full log size 13,1 MB

first RPC thread die at 13:55:17.501, last few lines from log with [RPC0]:
```
...
2020-12-18 13:55:17.501	[RPC0]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:97	HTTP [95.161.xxx.xxx] POST /json_rpc
2020-12-18 13:55:17.501	[RPC0]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:163	[95.161.xxx.xxx:53273 INC] Calling RPC method get_info
2020-12-18 13:55:17.501	[RPC0]	INFO	perf.daemon.rpc	src/common/perf_timer.cpp:120	PERF             ----------
2020-12-18 13:55:17.505	[RPC0]	INFO	perf.daemon.rpc	src/common/perf_timer.cpp:156	PERF     3415    get_info
2020-12-18 13:55:17.505	[RPC0]	DEBUG	daemon.rpc	src/rpc/core_rpc_server.h:163	/json_rpc[get_info] processed with 0/3/1ms
2020-12-18 13:55:17.505	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:682	do_send_chunk() NOW SENSD: packet=1514 B
2020-12-18 13:55:17.556	[RPC0]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:97	HTTP [203.160.xxx.xxx] POST /getblocks.bin
2020-12-18 13:55:17.556	[RPC0]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:103	[203.160.xxx.xxx:63131 INC] calling /getblocks.bin
2020-12-18 13:55:17.556	[RPC0]	INFO	perf.daemon.rpc	src/common/perf_timer.cpp:120	PERF             ----------
2020-12-18 13:55:17.556	[RPC0]	INFO	perf.daemon.rpc	src/common/perf_timer.cpp:156	PERF       27    get_blocks
2020-12-18 13:55:17.556	[RPC0]	DEBUG	daemon.rpc	src/rpc/core_rpc_server.h:103	/getblocks.bin() processed with 0/0/0ms
2020-12-18 13:55:17.556	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:682	do_send_chunk() NOW SENSD: packet=276 B
2020-12-18 13:55:17.608	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:779	[24.217.xxx.xxx:50714 INC] connection timeout, closing
```

second RPC thread die at 13:56:08.760, last few lines from log with [RPC1]:
```
...
2020-12-18 13:56:08.638	[RPC1]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:97	HTTP [1.136.xxx.xxx] POST /get_transaction_pool_hashes.bin
2020-12-18 13:56:08.639	[RPC1]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:126	[1.136.xxx.xxx:6376 INC] calling /get_transaction_pool_hashes.bin
2020-12-18 13:56:08.639	[RPC1]	INFO	perf.daemon.rpc	src/common/perf_timer.cpp:120	PERF             ----------
2020-12-18 13:56:08.639	[RPC1]	INFO	perf.daemon.rpc	src/common/perf_timer.cpp:156	PERF       74    get_transaction_pool_hashes
2020-12-18 13:56:08.639	[RPC1]	DEBUG	daemon.rpc	src/rpc/core_rpc_server.h:126	/get_transaction_pool_hashes.bin processed with 0/0/0ms
2020-12-18 13:56:08.639	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:682	do_send_chunk() NOW SENSD: packet=358 B
2020-12-18 13:56:08.699	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:779	[172.58.xxx.xxx:42945 INC] connection timeout, closing
2020-12-18 13:56:08.730	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:779	[193.165.xxx.xxx:57818 INC] connection timeout, closing
2020-12-18 13:56:08.760	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:779	[67.175.xxx.xxx:56400 INC] connection timeout, closing
```
After this my script kill process and restarted because it stop to answer to RPC calls.

3) Node started at 14:10:40, **_full log size 2,6 GB_**. In log millions of lines with 'Setting timer on a shut down object'

first RPC thread die at 14:16:32.915, last few lines from log with [RPC0]:
```
2020-12-18 14:16:32.590	[RPC0]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-12-18 14:16:32.590	[RPC0]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-12-18 14:16:32.590	[RPC0]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-12-18 14:16:32.590	[RPC0]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-12-18 14:16:32.590	[RPC0]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-12-18 14:16:32.590	[RPC0]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-12-18 14:16:32.606	[RPC0]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:97	HTTP [107.117.xxx.xxx] POST /getblocks.bin
2020-12-18 14:16:32.606	[RPC0]	INFO	perf.daemon.rpc	src/common/perf_timer.cpp:156	PERF        7    get_blocks
2020-12-18 14:16:32.607	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:682	do_send_chunk() NOW SENSD: packet=276 B
2020-12-18 14:16:32.617	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:682	do_send_chunk() NOW SENSD: packet=1521 B
2020-12-18 14:16:32.672	[RPC0]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:97	HTTP [95.161.xxx.xxx] POST /get_transaction_pool_hashes.bin
2020-12-18 14:16:32.672	[RPC0]	INFO	perf.daemon.rpc	src/common/perf_timer.cpp:156	PERF       15    get_transaction_pool_hashes
2020-12-18 14:16:32.672	[RPC0]	DEBUG	daemon.rpc	src/rpc/core_rpc_server.h:126	/get_transaction_pool_hashes.bin processed with 0/0/0ms
2020-12-18 14:16:32.672	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:682	do_send_chunk() NOW SENSD: packet=3791 B
2020-12-18 14:16:32.770	[RPC0]	DEBUG	daemon.rpc	src/rpc/core_rpc_server.h:126	/get_transaction_pool_hashes.bin processed with 0/0/0ms
2020-12-18 14:16:32.770	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:682	do_send_chunk() NOW SENSD: packet=3791 B
2020-12-18 14:16:32.781	[RPC0]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:103	[74.82.xxx.xxx:42714 INC] calling /getblocks.bin
2020-12-18 14:16:32.781	[RPC0]	INFO	perf.daemon.rpc	src/common/perf_timer.cpp:120	PERF             ----------
2020-12-18 14:16:32.781	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:682	do_send_chunk() NOW SENSD: packet=276 B
2020-12-18 14:16:32.834	[RPC0]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:97	HTTP [95.161.xxx.xxx] POST /gettransactions
2020-12-18 14:16:32.876	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:682	do_send_chunk() NOW SENSD: packet=2381 B
2020-12-18 14:16:32.915	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:779	[24.34.xxx.xxx:50632 INC] connection timeout, closing

```

second RPC thread die at 13:56:08.760, last few lines from log with [RPC1]:

```
...
2020-12-18 14:17:57.393	[RPC1]	DEBUG	daemon.rpc	src/rpc/core_rpc_server.h:111	/gettransactions processed with 0/35/0ms
2020-12-18 14:17:57.394	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:682	do_send_chunk() NOW SENSD: packet=6445 B
2020-12-18 14:17:57.424	[RPC1]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:103	[86.123.xxx.xxx:45132 INC] calling /getblocks.bin
2020-12-18 14:17:57.424	[RPC1]	INFO	perf.daemon.rpc	src/common/perf_timer.cpp:120	PERF             ----------
2020-12-18 14:17:57.424	[RPC1]	INFO	perf.daemon.rpc	src/common/perf_timer.cpp:156	PERF      129    get_blocks
2020-12-18 14:17:57.424	[RPC1]	DEBUG	daemon.rpc	src/rpc/core_rpc_server.h:103	/getblocks.bin() processed with 0/1/0ms
2020-12-18 14:17:57.424	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:682	do_send_chunk() NOW SENSD: packet=276 B
2020-12-18 14:17:57.485	[RPC1]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:97	HTTP [173.19.xxx.xxx] POST /get_transaction_pool_hashes.bin
2020-12-18 14:17:57.485	[RPC1]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:126	[173.19.xxx.xxx:49312 INC] calling /get_transaction_pool_hashes.bin
2020-12-18 14:17:57.485	[RPC1]	INFO	perf.daemon.rpc	src/common/perf_timer.cpp:120	PERF             ----------
2020-12-18 14:17:57.485	[RPC1]	INFO	perf.daemon.rpc	src/common/perf_timer.cpp:156	PERF       81    get_transaction_pool_hashes
2020-12-18 14:17:57.485	[RPC1]	DEBUG	daemon.rpc	src/rpc/core_rpc_server.h:126	/get_transaction_pool_hashes.bin processed with 0/0/0ms
2020-12-18 14:17:57.485	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:682	do_send_chunk() NOW SENSD: packet=854 B
2020-12-18 14:17:57.516	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:779	[156.146.xxx.xxx:50155 INC] connection timeout, closing
```
After this my script kill process and restarted because it stop to answer to RPC calls.

I think because of millions of lines with 'Setting timer on a shut down object' CPU load became almost 100% after some time. Not sure it is related to problem with RPC thread died, but seems as a bug ;)

## AJIekceu4 | 2020-12-18T15:12:17+00:00
I also noticed that RPC in all 3 cases stop responding after 5 minutes+. Here is first and last time in log for each RPC thread for each test. In all 3 cases node have about 70-100 active RPC connections.
1)

307 seconds for RPC0
```
2020-12-18 13:31:00.827	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:1273	handle_accept
2020-12-18 13:36:07.158	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:779	[58.166.xxx.xxx:50047 INC] connection timeout, closing
```
306 seconds for RPC1
```
2020-12-18 13:31:00.829	[RPC1]	DEBUG	net.ssl	contrib/epee/src/net_ssl.cpp:407	SSL detection buffer, 160 bytes: 22 3 1 0 155 1 0 0 151
2020-12-18 13:36:06.406	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:779	[58.166.xxx.xxx:50048 INC] connection timeout, closing
```

2)
330 seconds for RPC0
```
2020-12-18 13:49:47.290	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:1273	handle_accept
2020-12-18 13:55:17.608	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:779	[24.217.xxx.xxx:50714 INC] connection timeout, closing
```
381 seconds for RPC1
```
2020-12-18 13:49:47.291	[RPC1]	DEBUG	net.ssl	contrib/epee/src/net_ssl.cpp:407	SSL detection buffer, 128 bytes: 80 79 83 84 32 47 106 115 111
2020-12-18 13:56:08.760	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:779	[67.175.xxx.xxx:56400 INC] connection timeout, closing
```

3)
350 seconds for RPC0
```
2020-12-18 14:10:42.526	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:1273	handle_accept
2020-12-18 14:16:32.915	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:779	[24.34.xxx.xxx:50632 INC] connection timeout, closing
```

435 seconds for RPC1
```
2020-12-18 14:10:42.527	[RPC1]	DEBUG	net.ssl	contrib/epee/src/net_ssl.cpp:407	SSL detection buffer, 160 bytes: 22 3 1 0 155 1 0 0 151
2020-12-18 14:17:57.516	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:779	[156.146.xxx.xxx:50155 INC] connection timeout, closing
```

May be it is some kind of timeout problem after specific RPC connection.

## moneromooo-monero | 2020-12-18T15:35:32+00:00
Can you get me this please ,from the logs above:

grep "58.166.xxx.xxx:50048 INC" logs-files-here

With xxx the actual IP that first times out.

## AJIekceu4 | 2020-12-18T15:54:34+00:00
> Can you get me this please ,from the logs above:
> 
> grep "58.166.xxx.xxx:50048 INC" logs-files-here
> 
> With xxx the actual IP that first times out.

```
2020-12-18 13:31:04.172	[RPC1]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:170	[58.166.xxx.xxx:50048 INC] Calling RPC method get_version
2020-12-18 13:31:05.060	[RPC1]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:163	[58.166.xxx.xxx:50048 INC] Calling RPC method get_info
2020-12-18 13:31:06.012	[RPC0]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:126	[58.166.xxx.xxx:50048 INC] calling /get_transaction_pool_hashes.bin
2020-12-18 13:31:06.373	[RPC1]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:103	[58.166.xxx.xxx:50048 INC] calling /getblocks.bin
2020-12-18 13:36:06.406	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:779	[58.166.xxx.xxx:50048 INC] connection timeout, closing
```

## moneromooo-monero | 2020-12-18T16:47:52+00:00
OK, that's log level 1 probably. I guess I'll try spamming getblocks.bin.

## moneromooo-monero | 2020-12-18T18:01:41+00:00
Still works. I decreased the timeout to get a "connection timeout, closing" pretty much every call, still works.

## moneromooo-monero | 2020-12-18T18:55:50+00:00
I rigged the network to randomize the timeout, so some connections timeout quick, some don't. I also rigged the wallet to refresh in a loop, and two running at once refreshing from the same dameon. No problem.

## AJIekceu4 | 2020-12-19T08:05:15+00:00
> I rigged the network to randomize the timeout, so some connections timeout quick, some don't. I also rigged the wallet to refresh in a loop, and two running at once refreshing from the same dameon. No problem.

I am also have no problem with not restricted RPC which is used only by my own services and hide with firewall (send transaction, status, etc.). Problem appears only with public RPC port which is used by other people. Also i think most of active RPC users is a cakewallet users from mobile device. 

## moneromooo-monero | 2020-12-20T14:07:10+00:00
Does this patch help ?

https://paste.debian.net/hidden/da8b1aa6/

xxd -r < FILENAME > patch.gz

This file is full of random tabs so best to paste it binary.


## MoneroArbo | 2020-12-21T03:05:08+00:00
I was experiencing high CPU usage that would temporarily resolve after restarting the daemon. I'm not sure how long it stayed resolved, no more than two or three hours.

So far I have been running this patch for 7 hours and the problem has not recurred.

## AJIekceu4 | 2020-12-21T10:08:04+00:00
> Does this patch help ?
> 
> https://paste.debian.net/hidden/da8b1aa6/
> 
> xxd -r < FILENAME > patch.gz
> 
> This file is full of random tabs so best to paste it binary.

I git clone last code from github, apply patch and compile without any changes. Add --log-level=2 to startup parameters and run node. Nothing change:
Node started at 09:32:54, first RPC die at 09:37:57, last lines from log with RPC1:
```
2020-12-21 09:37:57.411	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:699	do_send_chunk() NOW SENSD: packet=4685 B
2020-12-21 09:37:57.412	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:874	[sock 66] handle_write: 4685 bytes, Success
2020-12-21 09:37:57.487	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:337	[sock 145] handle_receive: 137 bytes, Success
2020-12-21 09:37:57.515	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:874	[sock 66] handle_write: 276 bytes, Success
2020-12-21 09:37:57.634	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:337	[sock 43] handle_receive: 964 bytes, Success
2020-12-21 09:37:57.634	[RPC1]	DEBUG	daemon.rpc	src/rpc/core_rpc_server.cpp:868	Found 0/10 transactions on the blockchain
2020-12-21 09:37:57.650	[RPC1]	DEBUG	daemon.rpc	src/rpc/core_rpc_server.cpp:938	Found 10/10 transactions in the pool
2020-12-21 09:37:57.650	[RPC1]	DEBUG	daemon.rpc	src/rpc/core_rpc_server.cpp:1061	10 transactions found, 0 not found
2020-12-21 09:37:57.650	[RPC1]	INFO	perf.daemon.rpc	src/common/perf_timer.cpp:156	PERF    15947    get_transactions
2020-12-21 09:37:57.650	[RPC1]	DEBUG	daemon.rpc	src/rpc/core_rpc_server.h:111	/gettransactions processed with 0/16/0ms
2020-12-21 09:37:57.650	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:699	do_send_chunk() NOW SENSD: packet=16726 B
2020-12-21 09:37:57.650	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:874	[sock 43] handle_write: 16726 bytes, Success
2020-12-21 09:37:57.759	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:337	[sock 91] handle_receive: 94 bytes, Success
2020-12-21 09:37:57.763	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:337	[sock 90] handle_receive: 94 bytes, Success
2020-12-21 09:37:57.779	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:337	[sock 145] handle_receive: 1031 bytes, Success
2020-12-21 09:37:57.779	[RPC1]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:97	HTTP [119.18.xxx.xxx] POST /gettransactions
2020-12-21 09:37:57.779	[RPC1]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:111	[119.18.xxx.xxx:30999 INC] calling /gettransactions
2020-12-21 09:37:57.779	[RPC1]	INFO	perf.daemon.rpc	src/common/perf_timer.cpp:120	PERF             ----------
2020-12-21 09:37:57.779	[RPC1]	DEBUG	daemon.rpc	src/rpc/core_rpc_server.cpp:868	Found 0/11 transactions on the blockchain
2020-12-21 09:37:57.823	[RPC1]	DEBUG	daemon.rpc	src/rpc/core_rpc_server.cpp:938	Found 11/11 transactions in the pool
2020-12-21 09:37:57.823	[RPC1]	DEBUG	daemon.rpc	src/rpc/core_rpc_server.cpp:1061	11 transactions found, 0 not found
2020-12-21 09:37:57.823	[RPC1]	INFO	perf.daemon.rpc	src/common/perf_timer.cpp:156	PERF    43942    get_transactions
2020-12-21 09:37:57.823	[RPC1]	DEBUG	daemon.rpc	src/rpc/core_rpc_server.h:111	/gettransactions processed with 0/44/1ms
2020-12-21 09:37:57.823	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:699	do_send_chunk() NOW SENSD: packet=17775 B
2020-12-21 09:37:57.823	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:874	[sock 145] handle_write: 17775 bytes, Success
2020-12-21 09:37:57.891	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:337	[sock 74] handle_receive: 88 bytes, Success
2020-12-21 09:37:57.931	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:796	[84.64.xxx.xxx:55639 INC] connection timeout, closing
2020-12-21 09:37:57.931	[RPC1]	INFO	net	contrib/epee/include/net/abstract_tcp_server2.inl:837	[sock 39] close called.
2020-12-21 09:37:57.931	[RPC1]	INFO	net	contrib/epee/include/net/abstract_tcp_server2.inl:846	[sock 39] queue empty in close, calling shutdown
2020-12-21 09:37:57.932	[RPC1]	INFO	net	contrib/epee/include/net/abstract_tcp_server2.inl:808	[sock 39] shutdown called
```
grep '84.64.xxx.xxx:55639 INC'
```
2020-12-21 09:32:57.456	[RPC1]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:170	[84.64.xxx.xxx:55639 INC] Calling RPC method get_version
2020-12-21 09:32:57.508	[RPC0]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:163	[84.64.xxx.xxx:55639 INC] Calling RPC method get_info
2020-12-21 09:32:57.569	[RPC0]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:126	[84.64.xxx.xxx:55639 INC] calling /get_transaction_pool_hashes.bin
2020-12-21 09:32:57.629	[RPC0]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:111	[84.64.xxx.xxx:55639 INC] calling /gettransactions
2020-12-21 09:32:57.856	[RPC1]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:103	[84.64.xxx.xxx:55639 INC] calling /getblocks.bin
2020-12-21 09:37:57.931	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:796	[84.64.239.212:55639 INC] connection timeout, closing
```

Second RPC thread die at 09:39:13, last lines from log with RPC0:
```
2020-12-21 09:39:12.395	[RPC0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3678	Using 0.000000008331/byte fee
2020-12-21 09:39:12.395	[RPC0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3264	Mixin: 10-10
2020-12-21 09:39:12.396	[RPC0]	INFO	perf.blockchain	src/common/perf_timer.cpp:156	PERF        1          expand_transaction_2
2020-12-21 09:39:12.399	[RPC0]	INFO	perf.ringct	src/common/perf_timer.cpp:156	PERF     2987            verRctCLSAGSimple
2020-12-21 09:39:12.399	[RPC0]	INFO	perf.ringct	src/common/perf_timer.cpp:156	PERF     3021          verRctNonSemanticsSimple
2020-12-21 09:39:12.399	[RPC0]	INFO	perf.blockchain	src/common/perf_timer.cpp:156	PERF     3571        check_tx_inputs
2020-12-21 09:39:12.399	[RPC0]	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:608	DB map size:     112933359616
2020-12-21 09:39:12.399	[RPC0]	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:609	Space used:      101319266304
2020-12-21 09:39:12.399	[RPC0]	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:610	Space remaining: 11614093312
2020-12-21 09:39:12.399	[RPC0]	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:611	Size threshold:  0
2020-12-21 09:39:12.399	[RPC0]	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:613	Percent used: 89.7160  Percent threshold: 90.0000
2020-12-21 09:39:12.401	[RPC0]	INFO	txpool	src/cryptonote_core/tx_pool.cpp:376	Transaction added to pool: txid <2c231b9500f832ae829924de457b7a12133ff42935b3e724782f0772ca009f06> weight: 1453 fee/byte: 8334.48
2020-12-21 09:39:12.401	[RPC0]	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:608	DB map size:     112933359616
2020-12-21 09:39:12.401	[RPC0]	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:609	Space used:      101319266304
2020-12-21 09:39:12.401	[RPC0]	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:610	Space remaining: 11614093312
2020-12-21 09:39:12.401	[RPC0]	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:611	Size threshold:  0
2020-12-21 09:39:12.401	[RPC0]	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:613	Percent used: 89.7160  Percent threshold: 90.0000
2020-12-21 09:39:12.401	[RPC0]	INFO	perf.txpool	src/common/perf_timer.cpp:156	PERF     5731      add_tx
2020-12-21 09:39:12.401	[RPC0]	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:1074	tx added: <2c231b9500f832ae829924de457b7a12133ff42935b3e724782f0772ca009f06>
2020-12-21 09:39:12.401	[RPC0]	INFO	perf.daemon.rpc	src/common/perf_timer.cpp:156	PERF    13228    send_raw_tx
2020-12-21 09:39:12.401	[RPC0]	DEBUG	daemon.rpc	src/rpc/core_rpc_server.h:115	/sendrawtransaction processed with 0/13/0ms
2020-12-21 09:39:12.401	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:699	do_send_chunk() NOW SENSD: packet=518 B
2020-12-21 09:39:12.401	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:874	[sock 158] handle_write: 518 bytes, Success
2020-12-21 09:39:12.538	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:874	[sock 109] handle_write: 11822925 bytes, Success
2020-12-21 09:39:12.579	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:874	[sock 141] handle_write: 5376958 bytes, Success
2020-12-21 09:39:12.907	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:337	[sock 168] handle_receive: 152 bytes, Success
2020-12-21 09:39:12.925	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:337	[sock 160] handle_receive: 136 bytes, Success
2020-12-21 09:39:12.998	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:337	[sock 118] handle_receive: 135 bytes, Success
2020-12-21 09:39:13.044	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:796	[120.17.xxx.xxx:5826 INC] connection timeout, closing
2020-12-21 09:39:13.045	[RPC0]	INFO	net	contrib/epee/include/net/abstract_tcp_server2.inl:837	[sock 124] close called.
2020-12-21 09:39:13.045	[RPC0]	INFO	net	contrib/epee/include/net/abstract_tcp_server2.inl:846	[sock 124] queue empty in close, calling shutdown
2020-12-21 09:39:13.045	[RPC0]	INFO	net	contrib/epee/include/net/abstract_tcp_server2.inl:808	[sock 124] shutdown called
```
grep '120.17.xxx.xxx:5826 INC'
```
2020-12-21 09:33:33.753	[RPC0]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:170	[120.17.xxx.xxx:5826 INC] Calling RPC method get_version
2020-12-21 09:33:34.310	[RPC1]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:163	[120.17.xxx.xxx:5826 INC] Calling RPC method get_info
2020-12-21 09:33:34.679	[RPC0]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:126	[120.17.xxx.xxx:5826 INC] calling /get_transaction_pool_hashes.bin
2020-12-21 09:33:35.047	[RPC1]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:111	[120.17.xxx.xxx:5826 INC] calling /gettransactions
2020-12-21 09:33:35.858	[RPC1]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:103	[120.17.xxx.xxx:5826 INC] calling /getblocks.bin
2020-12-21 09:33:45.057	[RPC0]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:103	[120.17.xxx.xxx:5826 INC] calling /getblocks.bin
2020-12-21 09:34:00.311	[RPC1]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:126	[120.17.xxx.xxx:5826 INC] calling /get_transaction_pool_hashes.bin
2020-12-21 09:34:00.678	[RPC0]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:111	[120.17.xxx.xxx:5826 INC] calling /gettransactions
2020-12-21 09:34:01.077	[RPC1]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:103	[120.17.xxx.xxx:5826 INC] calling /getblocks.bin
2020-12-21 09:34:11.498	[RPC0]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:163	[120.17.xxx.xxx:5826 INC] Calling RPC method get_info
2020-12-21 09:34:12.068	[RPC0]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:126	[120.17.xxx.xxx:5826 INC] calling /get_transaction_pool_hashes.bin
2020-12-21 09:34:12.682	[RPC1]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:111	[120.17.xxx.xxx:5826 INC] calling /gettransactions
2020-12-21 09:34:13.042	[RPC1]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:103	[120.17.xxx.xxx:5826 INC] calling /getblocks.bin
2020-12-21 09:39:13.044	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:796	[120.17.xxx.xxx:5826 INC] connection timeout, closing

```

## selsta | 2020-12-21T10:17:14+00:00
Could be two separate issues here. The patch mooo posted is against public rpc nodes suddenly using a lot of CPU, which seems to be a new issue.

@AJIekceu4 your issue seems to exist for a while and is not the same.

## moneromooo-monero | 2020-12-21T12:44:11+00:00
So it looks like when a getblocks.bin call gets timed out. I tried that in my earlier test but the RPC did not die, so there's some other condition involved.

## moneromooo-monero | 2020-12-21T13:17:44+00:00
MoneroArbo: I could do with a log of roughly when the high CPU load starts with log level: 0,net\*:DEBUG,net:TRACE,\*thr\*:ERROR
A few minutes either side (mostly before) if you can.

## AJIekceu4 | 2020-12-21T18:16:17+00:00
@moneromooo-monero  , @Gingeropolous  i was trying to use sniffer to catch data which kill the RPC thread and found out, that this problem every time related to SSL encryption in RPC. After i restart my node with flag --rpc-ssl=disabled it worked more than 1 hour without any problem (only 2 RPC thread, version v0.17.1.7-release) serving 140 RPC clients.

## moneromooo-monero | 2020-12-21T18:39:54+00:00
Very useful info, thanks.

## moneromooo-monero | 2020-12-21T21:17:43+00:00
https://paste.debian.net/hidden/1a4ec607/ replaces the patch above, might fix the ssl related bug.

## MoneroArbo | 2020-12-21T21:18:55+00:00
Rolled back to 0.17.1.7 release version (no patch) and the CPU usage issue still hasn't cropped back up after 7 hours. I'm running with the log levels you suggested though so if I do see the behavior again I can get those to you.

## Gingeropolous | 2020-12-22T04:47:23+00:00
I just went to add rpc-disabled to my conf file, and it turns out I already have it there. So I'm still running into these issues with rpc-disabled. 

## Gingeropolous | 2020-12-22T04:58:45+00:00
i tried applying the patch, and got this as an error output:

```
--- contrib/epee/include/net/abstract_tcp_server2.inl
+++ contrib/epee/include/net/abstract_tcp_server2.inl
@@ -690,12 +705,12 @@ PRAGMA_WARNING_DISABLE_VS(4355)
 
         if(m_send_que.size()!=1)
         {
-            _erro("Looks like no active operations, but send que size != 1!!");
+            _erro(context << "Looks like no active operations, but send que size != 1!!");
             return false;
         }
 
         auto size_now = m_send_que.front().size();
-        MDEBUG(context << "do_send_chunk() NOW SENSD: packet="<<size_now<<" B");
+        MDEBUG(context << "do_send_chunk() NOW SENDS: packet="<<size_now<<" B");
         if (speed_limit_is_enabled())
 			do_send_handler_write( m_send_que.back().data(), m_send_que.back().size() ); // (((H)))
```

still compiled though. And now its running. 

## AJIekceu4 | 2020-12-22T11:57:57+00:00
> https://paste.debian.net/hidden/1a4ec607/ replaces the patch above, might fix the ssl related bug.

```
git clone --recursive https://github.com/monero-project/monero
cd monero && git submodule init && git submodule update
git apply net-patch
error: patch failed: contrib/epee/include/net/abstract_tcp_server2.inl:675
error: contrib/epee/include/net/abstract_tcp_server2.inl: patch does not apply
```
What i do wrong?

## selsta | 2020-12-22T12:12:04+00:00
Try

```
patch -p1 < [patch-name].patch
```

You can ignore the part it fails to apply, as this is only logging related.

## AJIekceu4 | 2020-12-22T13:01:33+00:00
> patch -p1 < [patch-name].patch

I apply patch and compile: 
```
patch -p1 < net-patch 
patching file contrib/epee/include/net/abstract_tcp_server2.inl
Hunk #7 succeeded at 386 (offset -1 lines).
Hunk #8 succeeded at 408 (offset -1 lines).
Hunk #9 succeeded at 439 (offset -1 lines).
Hunk #10 succeeded at 454 (offset -1 lines).
Hunk #11 succeeded at 470 (offset -1 lines).
Hunk #12 succeeded at 485 (offset -1 lines).
Hunk #13 succeeded at 564 (offset -1 lines).
Hunk #14 succeeded at 577 (offset -1 lines).
Hunk #15 succeeded at 626 (offset -1 lines).
Hunk #16 succeeded at 659 (offset -1 lines).
Hunk #17 succeeded at 679 (offset -1 lines).
Hunk #18 FAILED at 690.
Hunk #19 succeeded at 763 (offset -1 lines).
Hunk #20 succeeded at 804 (offset -1 lines).
Hunk #21 succeeded at 821 (offset -1 lines).
Hunk #22 succeeded at 833 (offset -1 lines).
Hunk #23 succeeded at 842 (offset -1 lines).
Hunk #24 succeeded at 870 (offset -1 lines).
Hunk #25 succeeded at 889 (offset -2 lines).
Hunk #26 succeeded at 930 (offset -2 lines).
1 out of 26 hunks FAILED -- saving rejects to file contrib/epee/include/net/abstract_tcp_server2.inl.rej
```

but it did not help ;(

Node started at 12:35:37
First RPC thread die at 12:45:02, last lines from log with RPC1:
```
2020-12-22 12:45:02.103	[RPC1]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:97	HTTP [84.186.xxx.xxx] POST /json_rpc
2020-12-22 12:45:02.103	[RPC1]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:163	[84.186.xxx.xxx:53509 INC] Calling RPC method get_info
2020-12-22 12:45:02.103	[RPC1]	INFO	perf.daemon.rpc	src/common/perf_timer.cpp:120	PERF             ----------
2020-12-22 12:45:02.107	[RPC1]	INFO	perf.daemon.rpc	src/common/perf_timer.cpp:156	PERF     3557    get_info
2020-12-22 12:45:02.107	[RPC1]	DEBUG	daemon.rpc	src/rpc/core_rpc_server.h:163	/json_rpc[get_info] processed with 0/4/0ms
2020-12-22 12:45:02.107	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:697	do_send_chunk() NOW SENSD: packet=1576 B
2020-12-22 12:45:02.272	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:795	[194.35.xxx.xxx:51091 INC] connection timeout, closing
2020-12-22 12:45:02.272	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:836	[194.35.xxx.xxx:51091 INC] [sock 170] close called.
2020-12-22 12:45:02.273	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:845	[194.35.xxx.xxx:51091 INC] [sock 170] queue empty in close, calling shutdown
2020-12-22 12:45:02.273	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:807	[194.35.xxx.xxx:51091 INC] [sock 170] shutdown called
```

grep '194.35.xxx.xxx:51091 INC'
```
2020-12-22 12:39:31.586	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:329	 connection type RPC 185.152.65.135:18081 <--> 194.35.xxx.xxx:51091 (via 194.35.xxx.xxx:51091)
2020-12-22 12:39:31.586	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:473	[194.35.xxx.xxx:51091 INC] [sock 170] That looks like SSL
2020-12-22 12:39:31.966	[RPC1]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:170	[194.35.xxx.xxx:51091 INC] Calling RPC method get_version
2020-12-22 12:39:32.019	[RPC0]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:163	[194.35.xxx.xxx:51091 INC] Calling RPC method get_info
2020-12-22 12:40:02.098	[RPC0]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:163	[194.35.xxx.xxx:51091 INC] Calling RPC method get_info
2020-12-22 12:45:02.272	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:795	[194.35.xxx.xxx:51091 INC] connection timeout, closing
2020-12-22 12:45:02.272	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:836	[194.35.xxx.xxx:51091 INC] [sock 170] close called.
2020-12-22 12:45:02.273	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:845	[194.35.xxx.xxx:51091 INC] [sock 170] queue empty in close, calling shutdown
2020-12-22 12:45:02.273	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:807	[194.35.xxx.xxx:51091 INC] [sock 170] shutdown called
```

Second RPC thread die at 12:46:03, last lines from log with RPC0:
```
2020-12-22 12:46:03.360	[RPC0]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:97	HTTP [208.114.xxx.xxx] POST /getblocks.bin
2020-12-22 12:46:03.360	[RPC0]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:103	[208.114.xxx.xxx:10596 INC] calling /getblocks.bin
2020-12-22 12:46:03.360	[RPC0]	INFO	perf.daemon.rpc	src/common/perf_timer.cpp:120	PERF             ----------
2020-12-22 12:46:03.361	[RPC0]	INFO	perf.daemon.rpc	src/common/perf_timer.cpp:156	PERF       79    get_blocks
2020-12-22 12:46:03.361	[RPC0]	DEBUG	daemon.rpc	src/rpc/core_rpc_server.h:103	/getblocks.bin() processed with 0/0/0ms
2020-12-22 12:46:03.361	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:697	do_send_chunk() NOW SENSD: packet=276 B
2020-12-22 12:46:03.408	[RPC0]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:97	HTTP [68.112.xxx.xxx] POST /json_rpc
2020-12-22 12:46:03.408	[RPC0]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:163	[68.112.xxx.xxx:51482 INC] Calling RPC method get_info
2020-12-22 12:46:03.409	[RPC0]	INFO	perf.daemon.rpc	src/common/perf_timer.cpp:120	PERF             ----------
2020-12-22 12:46:03.412	[RPC0]	INFO	perf.daemon.rpc	src/common/perf_timer.cpp:156	PERF     3615    get_info
2020-12-22 12:46:03.412	[RPC0]	DEBUG	daemon.rpc	src/rpc/core_rpc_server.h:163	/json_rpc[get_info] processed with 0/4/0ms
2020-12-22 12:46:03.413	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:697	do_send_chunk() NOW SENSD: packet=1576 B
2020-12-22 12:46:03.429	[RPC0]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:97	HTTP [120.17.xxx.xxx] POST /json_rpc
2020-12-22 12:46:03.429	[RPC0]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:170	[120.17.xxx.xxx:4600 INC] Calling RPC method get_version
2020-12-22 12:46:03.429	[RPC0]	INFO	perf.daemon.rpc	src/common/perf_timer.cpp:120	PERF             ----------
2020-12-22 12:46:03.429	[RPC0]	INFO	perf.daemon.rpc	src/common/perf_timer.cpp:156	PERF       42    get_version
2020-12-22 12:46:03.430	[RPC0]	DEBUG	daemon.rpc	src/rpc/core_rpc_server.h:170	/json_rpc[get_version] processed with 0/0/0ms
2020-12-22 12:46:03.430	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:697	do_send_chunk() NOW SENSD: packet=311 B
2020-12-22 12:46:03.495	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:795	[97.119.xxx.xxx:58043 INC] connection timeout, closing
2020-12-22 12:46:03.495	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:836	[97.119.xxx.xxx:58043 INC] [sock 85] close called.
2020-12-22 12:46:03.495	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:845	[97.119.xxx.xxx:58043 INC] [sock 85] queue empty in close, calling shutdown
2020-12-22 12:46:03.495	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:807	[97.119.xxx.xxx:58043 INC] [sock 85] shutdown called
```

grep '97.119.xxx.xxx:58043 INC'
```
2020-12-22 12:41:02.874	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:329	 connection type RPC 185.152.65.135:18081 <--> 97.119.xxx.xxx:58043 (via 97.119.xxx.xxx:58043)
2020-12-22 12:41:02.874	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:473	[97.119.xxx.xxx:58043 INC] [sock 85] That looks like SSL
2020-12-22 12:41:03.333	[RPC1]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:170	[97.119.xxx.xxx:58043 INC] Calling RPC method get_version
2020-12-22 12:41:03.490	[RPC0]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:163	[97.119.xxx.xxx:58043 INC] Calling RPC method get_info
2020-12-22 12:46:03.495	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:795	[97.119.xxx.xxx:58043 INC] connection timeout, closing
2020-12-22 12:46:03.495	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:836	[97.119.xxx.xxx:58043 INC] [sock 85] close called.
2020-12-22 12:46:03.495	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:845	[97.119.xxx.xxx:58043 INC] [sock 85] queue empty in close, calling shutdown
2020-12-22 12:46:03.495	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:807	[97.119.xxx.xxx:58043 INC] [sock 85] shutdown called
```

## selsta | 2020-12-22T13:06:49+00:00
Like I previously said, I suspect we have two issues here.

This patch helps against the current attack / issue that has been going on since a week where CPU usage would suddenly increase drastically for public RPC nodes. See here as an example on one of my nodes:

<img width="1131" alt="Screenshot 2020-12-19 at 22 25 40" src="https://user-images.githubusercontent.com/7697454/102891822-277cbc00-445f-11eb-9c35-208c1d3a96a5.png">

Your issue seems to exist for a while and maybe is related but does not seem like the  exact same.

## moneromooo-monero | 2020-12-22T14:50:22+00:00
I can't see a stack trace in this issue. Did you catch one when this blocked RPC happens ?

## moneromooo-monero | 2020-12-22T18:58:31+00:00
I got a stack trace, the thread is actually stuck in shutdown. Timing out, most likely.

## Gingeropolous | 2020-12-22T19:56:52+00:00
@moneromooo-monero , i think this is a stack trace of this.

https://termbin.com/l6y3



## moneromooo-monero | 2020-12-23T00:59:05+00:00
This might fix it.
```
diff --git a/contrib/epee/include/net/abstract_tcp_server2.inl b/contrib/epee/include/net/abstract_tcp_server2.inl
index a1ecbe300..2eaf321fe 100644
--- a/contrib/epee/include/net/abstract_tcp_server2.inl
+++ b/contrib/epee/include/net/abstract_tcp_server2.inl
@@ -816,7 +817,10 @@ PRAGMA_WARNING_DISABLE_VS(4355)
     {
       const shared_state &state = static_cast<const shared_state&>(get_state());
       if (!state.stop_signal_sent)
+      {
+        socket().cancel(ignored_ec);
         socket_.shutdown(ignored_ec);
+      }
     }
     socket().shutdown(boost::asio::ip::tcp::socket::shutdown_both, ignored_ec);
     if (!m_host.empty())
```

## hyc | 2020-12-23T01:23:27+00:00
What's the difference between the `socket_.shutdown` and the `socket().shutdown` 3 lines after?

## moneromooo-monero | 2020-12-23T01:34:33+00:00
socket_ will be the SSL one, socket() will be the base one IIRC.

## AJIekceu4 | 2020-12-23T09:19:17+00:00
> This might fix it.
> 
> ```
> diff --git a/contrib/epee/include/net/abstract_tcp_server2.inl b/contrib/epee/include/net/abstract_tcp_server2.inl
> index a1ecbe300..2eaf321fe 100644
> --- a/contrib/epee/include/net/abstract_tcp_server2.inl
> +++ b/contrib/epee/include/net/abstract_tcp_server2.inl
> @@ -816,7 +817,10 @@ PRAGMA_WARNING_DISABLE_VS(4355)
>      {
>        const shared_state &state = static_cast<const shared_state&>(get_state());
>        if (!state.stop_signal_sent)
> +      {
> +        socket().cancel(ignored_ec);
>          socket_.shutdown(ignored_ec);
> +      }
>      }
>      socket().shutdown(boost::asio::ip::tcp::socket::shutdown_both, ignored_ec);
>      if (!m_host.empty())
> ```

Did not help. After applying patch above and compile - problem still exist.

This is stack trace (but i run gdb 5-7 minutes after all RPC stuck, if you need it right after problem i can run it one more time):
```
GNU gdb (Ubuntu 8.1.1-0ubuntu1) 8.1.1
Copyright (C) 2018 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from /root/23.12.2020/monero/build/Linux/master/release/bin/monerod...done.
Attaching to program: /root/23.12.2020/monero/build/Linux/master/release/bin/monerod, process 2133
[New LWP 2134]
[New LWP 2135]
[New LWP 2136]
[New LWP 2137]
[New LWP 2138]
[New LWP 2139]
[New LWP 2140]
[New LWP 2141]
[New LWP 2142]
[New LWP 2143]
[New LWP 2144]
[New LWP 2145]
[New LWP 2146]
[New LWP 2147]
[New LWP 2148]
[New LWP 2149]
[New LWP 2150]
[New LWP 2151]
[New LWP 2152]
[New LWP 2153]
[New LWP 2154]
[New LWP 2155]
[New LWP 2158]
[New LWP 2159]
[New LWP 2160]
[New LWP 2161]
[New LWP 2162]
[New LWP 2163]
[New LWP 2164]
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
0x00007f21eccbaad3 in futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55e3cce88758) at ../sysdeps/unix/sysv/linux/futex-internal.h:88
88	../sysdeps/unix/sysv/linux/futex-internal.h: No such file or directory.
(gdb) thread apply all bt

Thread 30 (Thread 0x7f0755cf8700 (LWP 2164)):
#0  0x00007f21eccbaad3 in futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55e3cb397ba4 <tools::threadpool::getInstance()::instance+164>) at ../sysdeps/unix/sysv/linux/futex-internal.h:88
#1  __pthread_cond_wait_common (abstime=0x0, mutex=0x55e3cb397b50 <tools::threadpool::getInstance()::instance+80>, cond=0x55e3cb397b78 <tools::threadpool::getInstance()::instance+120>) at pthread_cond_wait.c:502
#2  __pthread_cond_wait (cond=0x55e3cb397b78 <tools::threadpool::getInstance()::instance+120>, mutex=0x55e3cb397b50 <tools::threadpool::getInstance()::instance+80>) at pthread_cond_wait.c:655
#3  0x000055e3cacb6cdd in tools::threadpool::run(bool) ()
#4  0x00007f21eda5abcd in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.65.1
#5  0x00007f21eccb46db in start_thread (arg=0x7f0755cf8700) at pthread_create.c:463
#6  0x00007f21ec9dd71f in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 29 (Thread 0x7f07561f9700 (LWP 2163)):
#0  0x00007f21eccbaad3 in futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55e3cb397ba4 <tools::threadpool::getInstance()::instance+164>) at ../sysdeps/unix/sysv/linux/futex-internal.h:88
#1  __pthread_cond_wait_common (abstime=0x0, mutex=0x55e3cb397b50 <tools::threadpool::getInstance()::instance+80>, cond=0x55e3cb397b78 <tools::threadpool::getInstance()::instance+120>) at pthread_cond_wait.c:502
#2  __pthread_cond_wait (cond=0x55e3cb397b78 <tools::threadpool::getInstance()::instance+120>, mutex=0x55e3cb397b50 <tools::threadpool::getInstance()::instance+80>) at pthread_cond_wait.c:655
#3  0x000055e3cacb6cdd in tools::threadpool::run(bool) ()
#4  0x00007f21eda5abcd in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.65.1
#5  0x00007f21eccb46db in start_thread (arg=0x7f07561f9700) at pthread_create.c:463
#6  0x00007f21ec9dd71f in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 28 (Thread 0x7f07566fa700 (LWP 2162)):
#0  0x00007f21eccbaad3 in futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55e3cb397ba4 <tools::threadpool::getInstance()::instance+164>) at ../sysdeps/unix/sysv/linux/futex-internal.h:88
#1  __pthread_cond_wait_common (abstime=0x0, mutex=0x55e3cb397b50 <tools::threadpool::getInstance()::instance+80>, cond=0x55e3cb397b78 <tools::threadpool::getInstance()::instance+120>) at pthread_cond_wait.c:502
#2  __pthread_cond_wait (cond=0x55e3cb397b78 <tools::threadpool::getInstance()::instance+120>, mutex=0x55e3cb397b50 <tools::threadpool::getInstance()::instance+80>) at pthread_cond_wait.c:655
#3  0x000055e3cacb6cdd in tools::threadpool::run(bool) ()
#4  0x00007f21eda5abcd in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.65.1
#5  0x00007f21eccb46db in start_thread (arg=0x7f07566fa700) at pthread_create.c:463
#6  0x00007f21ec9dd71f in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 27 (Thread 0x7f0756bfb700 (LWP 2161)):
#0  0x00007f21eccbaad3 in futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55e3cb397ba0 <tools::threadpool::getInstance()::instance+160>) at ../sysdeps/unix/sysv/linux/futex-internal.h:88
#1  __pthread_cond_wait_common (abstime=0x0, mutex=0x55e3cb397b50 <tools::threadpool::getInstance()::instance+80>, cond=0x55e3cb397b78 <tools::threadpool::getInstance()::instance+120>) at pthread_cond_wait.c:502
#2  __pthread_cond_wait (cond=0x55e3cb397b78 <tools::threadpool::getInstance()::instance+120>, mutex=0x55e3cb397b50 <tools::threadpool::getInstance()::instance+80>) at pthread_cond_wait.c:655
#3  0x000055e3cacb6cdd in tools::threadpool::run(bool) ()
#4  0x00007f21eda5abcd in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.65.1
#5  0x00007f21eccb46db in start_thread (arg=0x7f0756bfb700) at pthread_create.c:463
#6  0x00007f21ec9dd71f in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 26 (Thread 0x7f07570fc700 (LWP 2160)):
#0  0x00007f21eccbaad3 in futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55e3cb397ba4 <tools::threadpool::getInstance()::instance+164>) at ../sysdeps/unix/sysv/linux/futex-internal.h:88
#1  __pthread_cond_wait_common (abstime=0x0, mutex=0x55e3cb397b50 <tools::threadpool::getInstance()::instance+80>, cond=0x55e3cb397b78 <tools::threadpool::getInstance()::instance+120>) at pthread_cond_wait.c:502
#2  __pthread_cond_wait (cond=0x55e3cb397b78 <tools::threadpool::getInstance()::instance+120>, mutex=0x55e3cb397b50 <tools::threadpool::getInstance()::instance+80>) at pthread_cond_wait.c:655
#3  0x000055e3cacb6cdd in tools::threadpool::run(bool) ()
#4  0x00007f21eda5abcd in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.65.1
#5  0x00007f21eccb46db in start_thread (arg=0x7f07570fc700) at pthread_create.c:463
#6  0x00007f21ec9dd71f in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 25 (Thread 0x7f07575fd700 (LWP 2159)):
#0  0x00007f21eccbaad3 in futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55e3cb397ba4 <tools::threadpool::getInstance()::instance+164>) at ../sysdeps/unix/sysv/linux/futex-internal.h:88
#1  __pthread_cond_wait_common (abstime=0x0, mutex=0x55e3cb397b50 <tools::threadpool::getInstance()::instance+80>, cond=0x55e3cb397b78 <tools::threadpool::getInstance()::instance+120>) at pthread_cond_wait.c:502
#2  __pthread_cond_wait (cond=0x55e3cb397b78 <tools::threadpool::getInstance()::instance+120>, mutex=0x55e3cb397b50 <tools::threadpool::getInstance()::instance+80>) at pthread_cond_wait.c:655
#3  0x000055e3cacb6cdd in tools::threadpool::run(bool) ()
#4  0x00007f21eda5abcd in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.65.1
#5  0x00007f21eccb46db in start_thread (arg=0x7f07575fd700) at pthread_create.c:463
#6  0x00007f21ec9dd71f in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 24 (Thread 0x7f0757afe700 (LWP 2158)):
---Type <return> to continue, or q <return> to quit---
#0  0x00007f21eccbaad3 in futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55e3cb397ba0 <tools::threadpool::getInstance()::instance+160>) at ../sysdeps/unix/sysv/linux/futex-internal.h:88
#1  __pthread_cond_wait_common (abstime=0x0, mutex=0x55e3cb397b50 <tools::threadpool::getInstance()::instance+80>, cond=0x55e3cb397b78 <tools::threadpool::getInstance()::instance+120>) at pthread_cond_wait.c:502
#2  __pthread_cond_wait (cond=0x55e3cb397b78 <tools::threadpool::getInstance()::instance+120>, mutex=0x55e3cb397b50 <tools::threadpool::getInstance()::instance+80>) at pthread_cond_wait.c:655
#3  0x000055e3cacb6cdd in tools::threadpool::run(bool) ()
#4  0x00007f21eda5abcd in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.65.1
#5  0x00007f21eccb46db in start_thread (arg=0x7f0757afe700) at pthread_create.c:463
#6  0x00007f21ec9dd71f in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 23 (Thread 0x7f0757fff700 (LWP 2155)):
#0  0x00007f21eccbaad3 in futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55e3ccd13920) at ../sysdeps/unix/sysv/linux/futex-internal.h:88
#1  __pthread_cond_wait_common (abstime=0x0, mutex=0x55e3ccd138d0, cond=0x55e3ccd138f8) at pthread_cond_wait.c:502
#2  __pthread_cond_wait (cond=0x55e3ccd138f8, mutex=0x55e3ccd138d0) at pthread_cond_wait.c:655
#3  0x000055e3ca86af97 in boost::asio::detail::task_io_service::do_run_one(boost::asio::detail::scoped_lock<boost::asio::detail::posix_mutex>&, boost::asio::detail::task_io_service_thread_info&, boost::system::error_code const&) ()
#4  0x000055e3cab4318d in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#5  0x00007f21eda5abcd in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.65.1
#6  0x00007f21eccb46db in start_thread (arg=0x7f0757fff700) at pthread_create.c:463
#7  0x00007f21ec9dd71f in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 22 (Thread 0x7f07807f5700 (LWP 2154)):
#0  0x00007f21eccbaad3 in futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55e3ccd13924) at ../sysdeps/unix/sysv/linux/futex-internal.h:88
#1  __pthread_cond_wait_common (abstime=0x0, mutex=0x55e3ccd138d0, cond=0x55e3ccd138f8) at pthread_cond_wait.c:502
#2  __pthread_cond_wait (cond=0x55e3ccd138f8, mutex=0x55e3ccd138d0) at pthread_cond_wait.c:655
#3  0x000055e3ca86af97 in boost::asio::detail::task_io_service::do_run_one(boost::asio::detail::scoped_lock<boost::asio::detail::posix_mutex>&, boost::asio::detail::task_io_service_thread_info&, boost::system::error_code const&) ()
#4  0x000055e3cab4318d in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#5  0x00007f21eda5abcd in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.65.1
#6  0x00007f21eccb46db in start_thread (arg=0x7f07807f5700) at pthread_create.c:463
#7  0x00007f21ec9dd71f in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 21 (Thread 0x7f0780cf6700 (LWP 2153)):
#0  0x00007f21eccbaad3 in futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55e3ccd13924) at ../sysdeps/unix/sysv/linux/futex-internal.h:88
#1  __pthread_cond_wait_common (abstime=0x0, mutex=0x55e3ccd138d0, cond=0x55e3ccd138f8) at pthread_cond_wait.c:502
#2  __pthread_cond_wait (cond=0x55e3ccd138f8, mutex=0x55e3ccd138d0) at pthread_cond_wait.c:655
#3  0x000055e3ca86af97 in boost::asio::detail::task_io_service::do_run_one(boost::asio::detail::scoped_lock<boost::asio::detail::posix_mutex>&, boost::asio::detail::task_io_service_thread_info&, boost::system::error_code const&) ()
#4  0x000055e3cab4318d in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#5  0x00007f21eda5abcd in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.65.1
#6  0x00007f21eccb46db in start_thread (arg=0x7f0780cf6700) at pthread_create.c:463
#7  0x00007f21ec9dd71f in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 20 (Thread 0x7f07811f7700 (LWP 2152)):
#0  0x00007f21ec9dda47 in epoll_wait (epfd=10, events=0x7f07811f6050, maxevents=128, timeout=-1) at ../sysdeps/unix/sysv/linux/epoll_wait.c:30
#1  0x000055e3ca86a3bb in boost::asio::detail::epoll_reactor::run(bool, boost::asio::detail::op_queue<boost::asio::detail::task_io_service_operation>&) ()
#2  0x000055e3ca86ae3a in boost::asio::detail::task_io_service::do_run_one(boost::asio::detail::scoped_lock<boost::asio::detail::posix_mutex>&, boost::asio::detail::task_io_service_thread_info&, boost::system::error_code const&) ()
#3  0x000055e3cab4318d in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#4  0x00007f21eda5abcd in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.65.1
#5  0x00007f21eccb46db in start_thread (arg=0x7f07811f7700) at pthread_create.c:463
#6  0x00007f21ec9dd71f in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 19 (Thread 0x7f07816f8700 (LWP 2151)):
#0  0x00007f21eccbaad3 in futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55e3ccd13924) at ../sysdeps/unix/sysv/linux/futex-internal.h:88
#1  __pthread_cond_wait_common (abstime=0x0, mutex=0x55e3ccd138d0, cond=0x55e3ccd138f8) at pthread_cond_wait.c:502
#2  __pthread_cond_wait (cond=0x55e3ccd138f8, mutex=0x55e3ccd138d0) at pthread_cond_wait.c:655
#3  0x000055e3ca86af97 in boost::asio::detail::task_io_service::do_run_one(boost::asio::detail::scoped_lock<boost::asio::detail::posix_mutex>&, boost::asio::detail::task_io_service_thread_info&, boost::system::error_code const&) ()
#4  0x000055e3cab4318d in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#5  0x00007f21eda5abcd in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.65.1
#6  0x00007f21eccb46db in start_thread (arg=0x7f07816f8700) at pthread_create.c:463
#7  0x00007f21ec9dd71f in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95
---Type <return> to continue, or q <return> to quit---

Thread 18 (Thread 0x7f0781bf9700 (LWP 2150)):
#0  0x00007f21eccbaad3 in futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55e3ccd13924) at ../sysdeps/unix/sysv/linux/futex-internal.h:88
#1  __pthread_cond_wait_common (abstime=0x0, mutex=0x55e3ccd138d0, cond=0x55e3ccd138f8) at pthread_cond_wait.c:502
#2  __pthread_cond_wait (cond=0x55e3ccd138f8, mutex=0x55e3ccd138d0) at pthread_cond_wait.c:655
#3  0x000055e3ca86af97 in boost::asio::detail::task_io_service::do_run_one(boost::asio::detail::scoped_lock<boost::asio::detail::posix_mutex>&, boost::asio::detail::task_io_service_thread_info&, boost::system::error_code const&) ()
#4  0x000055e3cab4318d in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#5  0x00007f21eda5abcd in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.65.1
#6  0x00007f21eccb46db in start_thread (arg=0x7f0781bf9700) at pthread_create.c:463
#7  0x00007f21ec9dd71f in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 17 (Thread 0x7f07820fa700 (LWP 2149)):
#0  0x00007f21eccbaad3 in futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55e3ccd13920) at ../sysdeps/unix/sysv/linux/futex-internal.h:88
#1  __pthread_cond_wait_common (abstime=0x0, mutex=0x55e3ccd138d0, cond=0x55e3ccd138f8) at pthread_cond_wait.c:502
#2  __pthread_cond_wait (cond=0x55e3ccd138f8, mutex=0x55e3ccd138d0) at pthread_cond_wait.c:655
#3  0x000055e3ca86af97 in boost::asio::detail::task_io_service::do_run_one(boost::asio::detail::scoped_lock<boost::asio::detail::posix_mutex>&, boost::asio::detail::task_io_service_thread_info&, boost::system::error_code const&) ()
#4  0x000055e3cab4318d in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#5  0x00007f21eda5abcd in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.65.1
#6  0x00007f21eccb46db in start_thread (arg=0x7f07820fa700) at pthread_create.c:463
#7  0x00007f21ec9dd71f in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 16 (Thread 0x7f07825fb700 (LWP 2148)):
#0  0x00007f21eccbaad3 in futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55e3ccd13924) at ../sysdeps/unix/sysv/linux/futex-internal.h:88
#1  __pthread_cond_wait_common (abstime=0x0, mutex=0x55e3ccd138d0, cond=0x55e3ccd138f8) at pthread_cond_wait.c:502
#2  __pthread_cond_wait (cond=0x55e3ccd138f8, mutex=0x55e3ccd138d0) at pthread_cond_wait.c:655
#3  0x000055e3ca86af97 in boost::asio::detail::task_io_service::do_run_one(boost::asio::detail::scoped_lock<boost::asio::detail::posix_mutex>&, boost::asio::detail::task_io_service_thread_info&, boost::system::error_code const&) ()
#4  0x000055e3cab4318d in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#5  0x00007f21eda5abcd in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.65.1
#6  0x00007f21eccb46db in start_thread (arg=0x7f07825fb700) at pthread_create.c:463
#7  0x00007f21ec9dd71f in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 15 (Thread 0x7f0782afc700 (LWP 2147)):
#0  0x00007f21eccbaad3 in futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55e3ccd13924) at ../sysdeps/unix/sysv/linux/futex-internal.h:88
#1  __pthread_cond_wait_common (abstime=0x0, mutex=0x55e3ccd138d0, cond=0x55e3ccd138f8) at pthread_cond_wait.c:502
#2  __pthread_cond_wait (cond=0x55e3ccd138f8, mutex=0x55e3ccd138d0) at pthread_cond_wait.c:655
#3  0x000055e3ca86af97 in boost::asio::detail::task_io_service::do_run_one(boost::asio::detail::scoped_lock<boost::asio::detail::posix_mutex>&, boost::asio::detail::task_io_service_thread_info&, boost::system::error_code const&) ()
#4  0x000055e3cab4318d in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#5  0x00007f21eda5abcd in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.65.1
#6  0x00007f21eccb46db in start_thread (arg=0x7f0782afc700) at pthread_create.c:463
#7  0x00007f21ec9dd71f in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 14 (Thread 0x7f0782ffd700 (LWP 2146)):
#0  0x00007f21eccbaad3 in futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55e3ccd13924) at ../sysdeps/unix/sysv/linux/futex-internal.h:88
#1  __pthread_cond_wait_common (abstime=0x0, mutex=0x55e3ccd138d0, cond=0x55e3ccd138f8) at pthread_cond_wait.c:502
#2  __pthread_cond_wait (cond=0x55e3ccd138f8, mutex=0x55e3ccd138d0) at pthread_cond_wait.c:655
#3  0x000055e3ca86af97 in boost::asio::detail::task_io_service::do_run_one(boost::asio::detail::scoped_lock<boost::asio::detail::posix_mutex>&, boost::asio::detail::task_io_service_thread_info&, boost::system::error_code const&) ()
#4  0x000055e3cab4318d in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#5  0x00007f21eda5abcd in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.65.1
#6  0x00007f21eccb46db in start_thread (arg=0x7f0782ffd700) at pthread_create.c:463
#7  0x00007f21ec9dd71f in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 13 (Thread 0x7f07837fe700 (LWP 2145)):
#0  0x00007f21eccbb065 in futex_abstimed_wait_cancelable (private=<optimized out>, abstime=0x7f07837fd8a0, expected=0, futex_word=0x55e3cccec9c8) at ../sysdeps/unix/sysv/linux/futex-internal.h:205
#1  __pthread_cond_wait_common (abstime=0x7f07837fd8a0, mutex=0x55e3cccec978, cond=0x55e3cccec9a0) at pthread_cond_wait.c:539
#2  __pthread_cond_timedwait (cond=0x55e3cccec9a0, mutex=0x55e3cccec978, abstime=0x7f07837fd8a0) at pthread_cond_wait.c:667
#3  0x00007f21eda62d72 in boost::condition_variable::do_wait_until(boost::unique_lock<boost::mutex>&, timespec const&) () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.65.1
---Type <return> to continue, or q <return> to quit---
#4  0x00007f21eda5b1ba in boost::this_thread::hidden::sleep_for(timespec const&) () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.65.1
#5  0x000055e3cab2ac44 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::run()::{lambda()#1}::operator()() const ()
#6  0x00007f21eda5abcd in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.65.1
#7  0x00007f21eccb46db in start_thread (arg=0x7f07837fe700) at pthread_create.c:463
#8  0x00007f21ec9dd71f in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 12 (Thread 0x7f0783fff700 (LWP 2144)):
#0  0x00007f21ec9d0cb9 in __GI___poll (fds=0x7f0783ffe560, nfds=1, timeout=-1) at ../sysdeps/unix/sysv/linux/poll.c:29
#1  0x00007f21ef16ebf7 in ?? () from /usr/lib/x86_64-linux-gnu/libzmq.so.5
#2  0x00007f21ef14c2ec in ?? () from /usr/lib/x86_64-linux-gnu/libzmq.so.5
#3  0x00007f21ef170932 in ?? () from /usr/lib/x86_64-linux-gnu/libzmq.so.5
#4  0x00007f21ef1713f6 in ?? () from /usr/lib/x86_64-linux-gnu/libzmq.so.5
#5  0x00007f21ef191fa9 in ?? () from /usr/lib/x86_64-linux-gnu/libzmq.so.5
#6  0x000055e3cadcca4d in net::zmq::receive[abi:cxx11](void*, int) ()
#7  0x000055e3cad0b915 in cryptonote::rpc::ZmqServer::serve() ()
#8  0x00007f21eda5abcd in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.65.1
#9  0x00007f21eccb46db in start_thread (arg=0x7f0783fff700) at pthread_create.c:463
#10 0x00007f21ec9dd71f in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 11 (Thread 0x7f079888e700 (LWP 2143)):
#0  0x00007f21eccbaad3 in futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55e3cccede90) at ../sysdeps/unix/sysv/linux/futex-internal.h:88
#1  __pthread_cond_wait_common (abstime=0x0, mutex=0x55e3cccede40, cond=0x55e3cccede68) at pthread_cond_wait.c:502
#2  __pthread_cond_wait (cond=0x55e3cccede68, mutex=0x55e3cccede40) at pthread_cond_wait.c:655
#3  0x000055e3ca84e8ed in boost::condition_variable::wait(boost::unique_lock<boost::mutex>&) ()
#4  0x000055e3ca85112b in bool epee::async_console_handler::run<bool epee::async_console_handler::run<std::_Bind<bool (epee::command_handler::*(epee::console_handlers_binder*, std::_Placeholder<1>))(boost::optional<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > const&)> >(std::_Bind<bool (epee::command_handler::*(epee::console_handlers_binder*, std::_Placeholder<1>))(boost::optional<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > const&)>, std::function<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > ()>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()>)::{lambda(boost::optional<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > const&)#1}>(std::function<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > ()>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, bool epee::async_console_handler::run<std::_Bind<bool (epee::command_handler::*(epee::console_handlers_binder*, std::_Placeholder<1>))(boost::optional<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > const&)> >(std::_Bind<bool (epee::command_handler::*(epee::console_handlers_binder*, std::_Placeholder<1>))(boost::optional<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > const&)>, std::function<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > ()>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()>)::{lambda(boost::optional<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > const&)#1} const&, std::function<void ()>) ()
#5  0x000055e3ca851fa1 in epee::console_handlers_binder::run_handling(std::function<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > ()>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()>) ()
#6  0x000055e3ca84f2df in boost::detail::thread_data<boost::_bi::bind_t<bool, boost::_mfi::mf3<bool, epee::console_handlers_binder, std::function<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > ()>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()> >, boost::_bi::list4<boost::_bi::value<epee::console_handlers_binder*>, boost::_bi::value<std::function<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > ()> >, boost::_bi::value<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, boost::_bi::value<std::function<void ()> > > > >::run() ()
#7  0x00007f21eda5abcd in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.65.1
#8  0x00007f21eccb46db in start_thread (arg=0x7f079888e700) at pthread_create.c:463
#9  0x00007f21ec9dd71f in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 10 (Thread 0x7f079908f700 (LWP 2142)):
#0  0x00007f21ec9d2e1f in __GI___select (nfds=1, readfds=0x7f079908e930, writefds=0x0, exceptfds=0x0, timeout=0x7f079908e900) at ../sysdeps/unix/sysv/linux/select.c:41
#1  0x000055e3ca84ed7a in epee::async_stdin_reader::reader_thread_func() ()
#2  0x00007f21eda5abcd in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.65.1
#3  0x00007f21eccb46db in start_thread (arg=0x7f079908f700) at pthread_create.c:463
#4  0x00007f21ec9dd71f in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 9 (Thread 0x7f0799890700 (LWP 2141)):
#0  0x00007f21ec9d0cb9 in __GI___poll (fds=0x7f079988df20, nfds=1, timeout=-1) at ../sysdeps/unix/sysv/linux/poll.c:29
#1  0x000055e3ca889aa2 in unsigned long boost::asio::ssl::detail::io<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >, boost::asio::ssl::detail::shutdown_op>(boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >&, boost::asio::ssl::detail::stream_core&, boost::asio::ssl::detail::shutdown_op const&, boost::system::error_code&) ()
#2  0x000055e3ca896f6e in epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::shutdown() ()
#3  0x000055e3ca897120 in epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::close() ()
#4  0x000055e3ca875aaf in boost::asio::detail::wait_handler<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::reset_timer(boost::date_time::subsecond_duration<boost::posix_time::time_duration, 1000l>, bool)::{lambda(boost::system::error_code const&)#1}>::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
---Type <return> to continue, or q <return> to quit---
#5  0x000055e3cae8933f in epee::net_utils::ssl_options_t::handshake(boost::asio::ssl::stream<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> > >&, boost::asio::ssl::stream_base::handshake_type, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::chrono::duration<long, std::ratio<1l, 1000l> >) const ()
#6  0x000055e3ca8f3c01 in epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::handle_receive(boost::system::error_code const&, unsigned long) ()
#7  0x000055e3ca89ae02 in void boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, std::_Bind<void (epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::*(boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > >, std::_Placeholder<1>, std::_Placeholder<2>))(boost::system::error_code const&, unsigned long)>, boost::asio::detail::is_continuation_if_running>::operator()<boost::system::error_code, unsigned long>(boost::system::error_code const&, unsigned long const&) ()
#8  0x000055e3ca8b0599 in boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, std::_Bind<void (epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::*(boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > >, std::_Placeholder<1>, std::_Placeholder<2>))(boost::system::error_code const&, unsigned long)>, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, std::_Bind<void (epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::*(boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > >, std::_Placeholder<1>, std::_Placeholder<2>))(boost::system::error_code const&, unsigned long)> > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#9  0x000055e3ca8b53df in void boost::asio::detail::strand_service::dispatch<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, std::_Bind<void (epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::*(boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > >, std::_Placeholder<1>, std::_Placeholder<2>))(boost::system::error_code const&, unsigned long)>, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, std::_Bind<void (epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::*(boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > >, std::_Placeholder<1>, std::_Placeholder<2>))(boost::system::error_code const&, unsigned long)> > >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, std::_Bind<void (epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::*(boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > >, std::_Placeholder<1>, std::_Placeholder<2>))(boost::system::error_code const&, unsigned long)>, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, std::_Bind<void (epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::*(boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > >, std::_Placeholder<1>, std::_Placeholder<2>))(boost::system::error_code const&, unsigned long)> >&) ()
#10 0x000055e3ca8b56b4 in boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, std::_Bind<void (epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::*(boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > >, std::_Placeholder<1>, std::_Placeholder<2>))(boost::system::error_code const&, unsigned long)>, boost::asio::detail::is_continuation_if_running> >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#11 0x000055e3ca87ca08 in epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::worker_thread() ()
#12 0x00007f21eda5abcd in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.65.1
#13 0x00007f21eccb46db in start_thread (arg=0x7f0799890700) at pthread_create.c:463
#14 0x00007f21ec9dd71f in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 8 (Thread 0x7f079a091700 (LWP 2140)):
#0  __lll_lock_wait () at ../sysdeps/unix/sysv/linux/x86_64/lowlevellock.S:135
#1  0x00007f21eccb70f4 in __GI___pthread_mutex_lock (mutex=0x7f07889ee4f8) at ../nptl/pthread_mutex_lock.c:115
#2  0x000055e3ca896d0b in epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::shutdown() ()
#3  0x000055e3ca8f29fa in epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::handle_read(boost::system::error_code const&, unsigned long) ()
#4  0x000055e3ca8af212 in void boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>::operator()<boost::system::error_code, unsigned long>(boost::system::error_code const&, unsigned long const&) ()
#5  0x000055e3ca8af7ea in boost::asio::ssl::detail::io_op<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >, boost::asio::ssl::detail::read_op<boost::asio::mutable_buffers_1>, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::operator()(boost::system::error_code, unsigned long, int) ()
#6  0x000055e3ca8bae28 in boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::ssl::detail::io_op<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >, boost::asio::ssl::detail::read_op<boost::asio::mutable_buffers_1>, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#7  0x000055e3ca8be18b in void boost::asio::detail::strand_service::dispatch<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::ssl::detail::io_op<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >, boost::asio::ssl::detail::read_op<boost::asio::mutable_buffers_1>, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::ssl::detail::io_op<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >, boost::asio::ssl::detail::read_op<boost::asio::mutable_buffers_1>, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_cus---Type <return> to continue, or q <return> to quit---
tom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > >&) ()
#8  0x000055e3ca8be56a in boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::ssl::detail::io_op<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >, boost::asio::ssl::detail::read_op<boost::asio::mutable_buffers_1>, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#9  0x000055e3ca87ca08 in epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::worker_thread() ()
#10 0x00007f21eda5abcd in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.65.1
#11 0x00007f21eccb46db in start_thread (arg=0x7f079a091700) at pthread_create.c:463
#12 0x00007f21ec9dd71f in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 7 (Thread 0x7f079a892700 (LWP 2139)):
#0  0x00007f21eccbaad3 in futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55e3ccd70ee0) at ../sysdeps/unix/sysv/linux/futex-internal.h:88
#1  __pthread_cond_wait_common (abstime=0x0, mutex=0x55e3ccd70e90, cond=0x55e3ccd70eb8) at pthread_cond_wait.c:502
#2  __pthread_cond_wait (cond=0x55e3ccd70eb8, mutex=0x55e3ccd70e90) at pthread_cond_wait.c:655
#3  0x000055e3ca87c8a8 in epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::worker_thread() ()
#4  0x00007f21eda5abcd in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.65.1
#5  0x00007f21eccb46db in start_thread (arg=0x7f079a892700) at pthread_create.c:463
#6  0x00007f21ec9dd71f in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 6 (Thread 0x7f079b093700 (LWP 2138)):
#0  0x00007f21ec9dda47 in epoll_wait (epfd=14, events=0x7f079b0923b0, maxevents=128, timeout=-1) at ../sysdeps/unix/sysv/linux/epoll_wait.c:30
#1  0x000055e3ca87c4ab in epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::worker_thread() ()
#2  0x00007f21eda5abcd in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.65.1
#3  0x00007f21eccb46db in start_thread (arg=0x7f079b093700) at pthread_create.c:463
#4  0x00007f21ec9dd71f in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 5 (Thread 0x7f079b894700 (LWP 2137)):
#0  0x00007f21eccbb065 in futex_abstimed_wait_cancelable (private=<optimized out>, abstime=0x7f079b8939b0, expected=0, futex_word=0x55e3cce5e668) at ../sysdeps/unix/sysv/linux/futex-internal.h:205
#1  __pthread_cond_wait_common (abstime=0x7f079b8939b0, mutex=0x55e3cce5e618, cond=0x55e3cce5e640) at pthread_cond_wait.c:539
#2  __pthread_cond_timedwait (cond=0x55e3cce5e640, mutex=0x55e3cce5e618, abstime=0x7f079b8939b0) at pthread_cond_wait.c:667
#3  0x00007f21eda62d72 in boost::condition_variable::do_wait_until(boost::unique_lock<boost::mutex>&, timespec const&) () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.65.1
#4  0x00007f21eda5b29e in boost::this_thread::hidden::sleep_until(timespec const&) () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.65.1
#5  0x000055e3ca858aff in boost::detail::thread_data<daemonize::t_daemon::run(bool)::{lambda()#1}>::run() ()
#6  0x00007f21eda5abcd in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.65.1
#7  0x00007f21eccb46db in start_thread (arg=0x7f079b894700) at pthread_create.c:463
#8  0x00007f21ec9dd71f in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 4 (Thread 0x7f079c095700 (LWP 2136)):
#0  0x00007f21ec9dda47 in epoll_wait (epfd=25, events=0x7f079c093d30, maxevents=256, timeout=-1) at ../sysdeps/unix/sysv/linux/epoll_wait.c:30
#1  0x00007f21ef146a71 in ?? () from /usr/lib/x86_64-linux-gnu/libzmq.so.5
#2  0x00007f21ef185dc4 in ?? () from /usr/lib/x86_64-linux-gnu/libzmq.so.5
#3  0x00007f21eccb46db in start_thread (arg=0x7f079c095700) at pthread_create.c:463
#4  0x00007f21ec9dd71f in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 3 (Thread 0x7f079c896700 (LWP 2135)):
#0  0x00007f21ec9dda47 in epoll_wait (epfd=23, events=0x7f079c894d30, maxevents=256, timeout=-1) at ../sysdeps/unix/sysv/linux/epoll_wait.c:30
#1  0x00007f21ef146a71 in ?? () from /usr/lib/x86_64-linux-gnu/libzmq.so.5
#2  0x00007f21ef185dc4 in ?? () from /usr/lib/x86_64-linux-gnu/libzmq.so.5
#3  0x00007f21eccb46db in start_thread (arg=0x7f079c896700) at pthread_create.c:463
#4  0x00007f21ec9dd71f in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 2 (Thread 0x7f079d2a9700 (LWP 2134)):
---Type <return> to continue, or q <return> to quit---
#0  0x00007f21eccbaad3 in futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55e3ccd30010) at ../sysdeps/unix/sysv/linux/futex-internal.h:88
#1  __pthread_cond_wait_common (abstime=0x0, mutex=0x55e3ccd2ffc0, cond=0x55e3ccd2ffe8) at pthread_cond_wait.c:502
#2  __pthread_cond_wait (cond=0x55e3ccd2ffe8, mutex=0x55e3ccd2ffc0) at pthread_cond_wait.c:655
#3  0x000055e3cac17eb8 in boost::asio::io_service::run() ()
#4  0x00007f21eda5abcd in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.65.1
#5  0x00007f21eccb46db in start_thread (arg=0x7f079d2a9700) at pthread_create.c:463
#6  0x00007f21ec9dd71f in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 1 (Thread 0x7f21f016ac00 (LWP 2133)):
#0  0x00007f21eccbaad3 in futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55e3cce88758) at ../sysdeps/unix/sysv/linux/futex-internal.h:88
#1  __pthread_cond_wait_common (abstime=0x0, mutex=0x55e3cce88708, cond=0x55e3cce88730) at pthread_cond_wait.c:502
#2  __pthread_cond_wait (cond=0x55e3cce88730, mutex=0x55e3cce88708) at pthread_cond_wait.c:655
#3  0x00007f21eda62b5d in boost::condition_variable::wait(boost::unique_lock<boost::mutex>&) () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.65.1
#4  0x00007f21eda5ad14 in boost::thread::join_noexcept() () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.65.1
#5  0x000055e3cab9495b in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::run_server(unsigned long, bool, boost::thread_attributes const&) ()
#6  0x000055e3cab967a9 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::run() ()
#7  0x000055e3ca86d454 in daemonize::t_p2p::run() ()
#8  0x000055e3ca85c4d0 in daemonize::t_daemon::run(bool) ()
#9  0x000055e3ca8f6b11 in daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) ()
#10 0x000055e3ca8fb49e in bool daemonizer::daemonize<daemonize::t_executor>(int, char const**, daemonize::t_executor&&, boost::program_options::variables_map const&) ()
#11 0x000055e3ca8277b3 in main ()
(gdb) 

```

## moneromooo-monero | 2020-12-23T16:20:43+00:00
Well, I'm stopping wasting more of my time on this poke and hope, it'll stay that way for a few more months till I get back to it.

## moneromooo-monero | 2020-12-23T16:22:42+00:00
FWIW, I suspect the problem is that the other side doesn't reply to the shutdown and shutdown goes into timeout, but various attempts to make a shutdown async so I can manually timeout and close just make things worse. So if someone groks networks and SSL well, go for it.

## Gingeropolous | 2020-12-23T19:37:56+00:00
stack trace

https://termbin.com/knyfd


## Gingeropolous | 2020-12-24T13:48:32+00:00
So, I was testing whether I could make new RPC connections by attempting a connect from a GUI. It turns out the IP I was trying to connect from had been banned by the remote nodes daemon. @AJIekceu4 , I don't know if this is how your testing RPC connectability, but if so you should check your bans for your clients IP. I caught it with log level 4. 

## AJIekceu4 | 2020-12-24T15:13:55+00:00
@Gingeropolous i just look into logs and trying find [RPC0] and [RPC1] strings. After RPC thread stuck, inside logfile there are no more RPC string and it is impossible to connect to 18081 from any IP (not only my own).

## AJIekceu4 | 2021-06-06T06:05:09+00:00
In version v0.17.2.0 problem still exist. Node stuck after few minutes until i did not disable ssl connection by using --rpc-ssl=disabled.

## selsta | 2021-06-06T06:08:22+00:00
Yes, this is still known.

https://github.com/monero-project/monero/pull/7649 might fix this issue but there are still discussions about it on what is the best way to fix this.

## selsta | 2021-06-22T19:35:36+00:00
@AJIekceu4 #7760 should also fix the issue but it needs a review first.

## selsta | 2022-07-16T15:55:47+00:00
Should be fixed in #8426 / v0.18.0.0, if not please comment and I will reopen.

# Action History
- Created by: AJIekceu4 | 2019-12-28T15:19:46+00:00
- Closed at: 2022-07-16T15:55:47+00:00
