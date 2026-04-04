---
title: DNS failure while making transfer
source_url: https://github.com/monero-project/monero/issues/5269
author: reardenlife
assignees: []
labels: []
created_at: '2019-03-12T05:22:25+00:00'
updated_at: '2019-08-19T22:30:43+00:00'
type: issue
status: closed
closed_at: '2019-08-19T22:30:43+00:00'
---

# Original Description
Running monero client (v.0.14.0.2) through remote node over tor:

```sh
DNS_PUBLIC=tcp \
  TORSOCKS_ALLOW_INBOUND=1 \
  torsocks \
  ./monero-wallet-cli --wallet-file Proxy --password moneroCryptoPassword --daemon-address node.moneroworld.com:18089
```

Sync is going OK, but when I am trying to send a transaction, I am getting repeated error:


```text
C1552359991 ERROR torsocks[5982]: General SOCKS server failure (in socks5_recv_connect_reply() at socks5.c:527)
[1552359991] libunbound[5982:0] error: outgoing tcp: connect: Connection refused for 77.109.148.137
1552359992 ERROR torsocks[5982]: General SOCKS server failure (in socks5_recv_connect_reply() at socks5.c:527)
[1552359992] libunbound[5982:0] error: outgoing tcp: connect: Connection refused for 77.109.148.137
^C1552360118 ERROR torsocks[5982]: General SOCKS server failure (in socks5_recv_connect_reply() at socks5.c:527)
[1552360118] libunbound[5982:0] error: outgoing tcp: connect: Connection refused for 77.109.148.137
./
[root@v48807 ~]#
```

I am looking into the source code: https://github.com/monero-project/monero/blob/master/src/common/dns_utils.cpp#L51

And it seems that the problem is connected with DNS.  I wonder WTF..

# Discussion History
## reardenlife | 2019-03-12T05:54:24+00:00
So it looks like only one of the servers in the list is down:

```sh
[root@v48807 .monero]# nslookup google.com 194.150.168.168
Server:         194.150.168.168
Address:        194.150.168.168#53

Non-authoritative answer:
Name:   google.com
Address: 172.217.19.206

[root@v48807 .monero]# nslookup google.com 80.67.169.40
Server:         80.67.169.40
Address:        80.67.169.40#53

Non-authoritative answer:
Name:   google.com
Address: 216.58.198.206

[root@v48807 .monero]# nslookup google.com 89.233.43.71
Server:         89.233.43.71
Address:        89.233.43.71#53

Non-authoritative answer:
Name:   google.com                                                                        Address: 172.217.22.174

[root@v48807 .monero]# nslookup google.com 109.69.8.51
Server:         109.69.8.51
Address:        109.69.8.51#53
Non-authoritative answer:
Name:   google.com
Address: 216.58.211.46

[root@v48807 .monero]# nslookup google.com 193.58.251.251
Server:         193.58.251.251
Address:        193.58.251.251#53

Non-authoritative answer:
Name:   google.com
Address: 64.233.162.100
Name:   google.com
Address: 64.233.162.102
Name:   google.com
Address: 64.233.162.139
Name:   google.com
Address: 64.233.162.138
Name:   google.com
Address: 64.233.162.113
Name:   google.com
Address: 64.233.162.101

[root@v48807 .monero]# nslookup google.com 77.109.148.137
;; connection timed out; no servers could be reached
```

But why it causes the transfer failure?

## reardenlife | 2019-03-12T06:35:33+00:00
Another server on the list seems to be down:

```text
1552372001 ERROR torsocks[18237]: Connection refused to Tor SOCKS (in socks5_recv_connect_reply() at socks5.c:543)                                                                                          [1552372001] libunbound[18237:0] error: outgoing tcp: connect: Connection refused for 193.58.251.251
1552372124 ERROR torsocks[18237]: General SOCKS server failure (in socks5_recv_connect_reply() at socks5.c:527)                                                                                             [1552372124] libunbound[18237:0] error: outgoing tcp: connect: Connection refused for 77.109.148.137
1552372124 ERROR torsocks[18237]: General SOCKS server failure (in socks5_recv_connect_reply() at socks5.c:527)                                                                                             [1552372124] libunbound[18237:0] error: outgoing tcp: connect: Connection refused for 77.109.148.137
1552372124 ERROR torsocks[18237]: General SOCKS server failure (in socks5_recv_connect_reply() at socks5.c:527)                                                                                             [1552372124] libunbound[18237:0] error: outgoing tcp: connect: Connection refused for 77.109.148.137
1552372125 ERROR torsocks[18237]: Connection refused to Tor SOCKS (in socks5_recv_connect_reply() at socks5.c:543)                                                                                          [1552372125] libunbound[18237:0] error: outgoing tcp: connect: Connection refused for 193.58.251.251
1552372126 ERROR torsocks[18237]: Connection refused to Tor SOCKS (in socks5_recv_connect_reply() at socks5.c:543)                                                                                          [1552372126] libunbound[18237:0] error: outgoing tcp: connect: Connection refused for 193.58.251.251
1552372126 ERROR torsocks[18237]: Connection refused to Tor SOCKS (in socks5_recv_connect_reply() at socks5.c:543)                                                                                          [1552372126] libunbound[18237:0] error: outgoing tcp: connect: Connection refused for 193.58.251.251
1552372127 ERROR torsocks[18237]: Connection refused to Tor SOCKS (in socks5_recv_connect_reply() at socks5.c:543)                                                                                          [1552372127] libunbound[18237:0] error: outgoing tcp: connect: Connection refused for 193.58.251.251
1552372128 ERROR torsocks[18237]: General SOCKS server failure (in socks5_recv_connect_reply() at socks5.c:527)                                                                                             [1552372128] libunbound[18237:0] error: outgoing tcp: connect: Connection refused for 77.109.148.137
1552372129 ERROR torsocks[18237]: Connection refused to Tor SOCKS (in socks5_recv_connect_reply() at socks5.c:543)                                                                                          [1552372129] libunbound[18237:0] error: outgoing tcp: connect: Connection refused for 193.58.251.251
```

## reardenlife | 2019-03-12T06:36:24+00:00
Some logs from the client:

```text

4272 2019-03-12 06:26:39.906     7f39ac295780  DEBUG wallet.wallet2  src/wallet/wallet2.cp
     p:6669 fake_outputs_count: 10
4273 2019-03-12 06:26:39.907     7f39977fe700  WARN  net.dns src/common/dns_utils.cpp:558
      Using default public DNS server(s): 194.150.168.168, 80.67.169.40, 89.233.43.71, 109
     .69.8.51, 77.109.148.137, 193.58.251.251 (TCP)
4274 2019-03-12 06:26:39.908     7f39977fe700  INFO  global  src/common/dns_utils.cpp:224
      Using public DNS server(s): 194.150.168.168, 80.67.169.40, 89.233.43.71, 109.69.8.51                 , 77.109.148.137, 193.58.251.251 (TCP)                                                           4275 2019-03-12 06:26:39.909     7f39977fe700  INFO  net.dns src/common/dns_utils.cpp:252
      adding trust anchor: . IN DS 19036 8 2 49AAC11D7B6F6446702E54A1607371607A1A41855200F                 D2CE1CDDE32F24E8FB5                                                                              4276
4277 2019-03-12 06:26:39.909     7f39977fe700  INFO  net.dns src/common/dns_utils.cpp:252                   adding trust anchor: . IN DS 20326 8 2 E06D44B80B8F1D39A95C0B0D7C65D08458E880409BBC6                 83457104237C7F8EC8D
4278                                                                                                  ~                                                                                                     ~
```

## reardenlife | 2019-03-12T07:15:42+00:00
So I am looking at this: https://github.com/monero-project/monero/blob/master/src/common/dns_utils.cpp#L289 ( get_record ).

It seems that the error is going on upon a call of a function ub_resolve. Apparently, because every public DNS is added into the list, a failure to resolve an IP on even one of them will result in an exception thrown and the whole resolution process repeating all over again.

This is bad.

## reardenlife | 2019-03-12T07:57:35+00:00
As a temporary solution I will just put the list of those DNS into the properties of my network connection and put the DNS_PUBLIC environment variable out of the way.

## moneromooo-monero | 2019-03-12T12:12:58+00:00
It's supposed to be redundant servers, not "all must succeed" servers.

## reardenlife | 2019-03-12T19:40:40+00:00
 @moneromooo-monero
> "It's supposed to be redundant servers, not "all must succeed" servers."

Wait a second.  So I could just simply ignore those errors and wait for the confirmation dialog with a commission calculated??

If so, such an output is very confusing - don't you think it would be better to explain what exactly going on and state that it is OK and one just have to wait some more?
Or, better yet, display an error only when ALL DNS servers failed?

## moneromooo-monero | 2019-03-12T19:50:38+00:00
Possibly, but it's torsocks printing those errors, not monero. The monero logs you posted don't say what happened after that, when the query is made. You could try running with "--log-level 0,\*dns\*:DEBUG" for more info.
Now, what I said in the previous post is just going from the man page. It might be wrong.

## tobtoht | 2019-06-19T10:02:59+00:00
CLI will now get stuck in a loop using torsocks on Tails when you attempt to send a transaction in v0.14.1.0. It will fail to send the transaction. GUI (buildbot monero-gui-ubuntu-amd64 2079) does not seem to be affected.

```
ERROR torsocks[3060]: General SOCKS server failure (in socks5_recv_connect_reply() at socks5.c:533)
libunbound[3060:0] error: outgoing tcp: connect: Connection refused for 77.109.148.137
```
Current workaround is to add --no-dns flag.


## sanderfoobar | 2019-06-20T03:53:51+00:00
Looks like same issue: https://www.reddit.com/r/Monero/comments/c2mu1m/monero_daemon_on_tails_error_perror_torsocks/

## tobtoht | 2019-06-20T04:42:04+00:00
```
2019-06-20 04:25:46.115	    7dc056587700	INFO	net.dns	src/common/dns_utils.cpp:240	adding trust anchor: . IN DS 19036 8 2 49AAC11D7B6F6446702E54A1607371607A1A41855200FD2CE1CDDE32F24E8FB5

2019-06-20 04:25:46.115	    7dc056587700	INFO	net.dns	src/common/dns_utils.cpp:240	adding trust anchor: . IN DS 20326 8 2 E06D44B80B8F1D39A95C0B0D7C65D08458E880409BBC683457104237C7F8EC8D

2019-06-20 04:25:46.122	    7dc056587700	INFO	net.dns	src/common/dns_utils.cpp:292	Failed to verify DNSSEC record from updates.moneropulse.org, falling back to TCP with well known DNSSEC resolvers
2019-06-20 04:25:46.123	    7dc056587700	INFO	net.dns	src/common/dns_utils.cpp:240	adding trust anchor: . IN DS 19036 8 2 49AAC11D7B6F6446702E54A1607371607A1A41855200FD2CE1CDDE32F24E8FB5

2019-06-20 04:25:46.123	    7dc056587700	INFO	net.dns	src/common/dns_utils.cpp:240	adding trust anchor: . IN DS 20326 8 2 E06D44B80B8F1D39A95C0B0D7C65D08458E880409BBC683457104237C7F8EC8D

2019-06-20 04:36:21.047	    7dc058b6d680	DEBUG	net.dns	src/common/dns_utils.cpp:541	DNSSEC not available for hostname: segheights.moneropulse.co, skipping.
2019-06-20 04:36:21.047	    7dc058b6d680	DEBUG	net.dns	src/common/dns_utils.cpp:546	DNSSEC validation failed for hostname: segheights.moneropulse.co, skipping.
2019-06-20 04:36:21.047	    7dc058b6d680	WARNING	net.dns	src/common/dns_utils.cpp:568	WARNING: no two valid DNS TXT records were received

```

## tobtoht | 2019-06-21T08:31:23+00:00
I should preface this by saying that I am not familiar with C++ at all, but I tried my hand at debugging this anyway.

I reverted commit `223c6b0796cf0f04042c48103fe22ede3ea6c1a6` and `9c4d403ae09fb5a07409467797bec84946352249`, this makes it work like before, no torsocks or libunbound error when attempting to send a transaction. 

The problem with the last commit I suspect is in this line `dns_utils.cpp#L296` where it causes dns resolvers to be added to `m_data->m_ub_context`. This didn't happen previous to those commits.

The line of code that is actually responsible for the issue is: `dns_utils.cpp#L331`

`get_record` is called 4 times asynchronously. `ub_resolve` is fed `m_data->m_ub_context`. I assume it picks a dns resolver randomly from this list. If this dns resolver happens to be xiala.net (which is down permanently), it will take libunbound nearly a minute to report that the connection was refused. It will subsequently use a different dns resolver and try again.

Eventually all 4 ub_resolve calls will return, but by then often the wallet will have lost its connection to the daemon (a separate issue with this release) resulting in:
`Error: RPC error: error in get_info RPC: Failed to connect to daemon`

https://i.ibb.co/6vwX15w/rpc-error.png

If luck strikes and the connection to the daemon works it will actually show you the transaction dialog:

https://i.ibb.co/5Fp368J/tx-dialog.jpg

Removing xiala.net from the list of dns resolvers could be a temporary solution. But if another dns resolver from the list goes down in the future the issue will reappear.

## reardenlife | 2019-07-11T17:49:54+00:00
@moneromooo-monero 

The debug logs, sir.  Grep'ed by 'dns':

```text

     7fd483245780        INFO    logging contrib/epee/src/mlog.cpp:277   New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO,*rpc*:DEBUG,*wallet*:DEBUG,*dns*:DEBUG
     7fd483245780        INFO    wallet.wallet2  src/wallet/wallet_args.cpp:207  Setting log level = 0,*rpc*:DEBUG,*wallet*:DEBUG,*dns*:DEBUG
     7fd478cc5700        INFO    net.dns src/common/dns_utils.cpp:252    adding trust anchor: . IN DS 19036 8 2 [scrubbed]
     7fd478cc5700        INFO    net.dns src/common/dns_utils.cpp:252    adding trust anchor: . IN DS 20326 8 2 [scrubbed]
     7fd483245780        DEBUG   net.dns src/common/dns_utils.cpp:492    DNSSEC not available for checkpoint update at URL: segheights.moneropulse.org, skipping.
     7fd483245780        DEBUG   net.dns src/common/dns_utils.cpp:497    DNSSEC validation failed for checkpoint update at URL: segheights.moneropulse.org, skipping.
     7fd483245780        DEBUG   net.dns src/common/dns_utils.cpp:492    DNSSEC not available for checkpoint update at URL: segheights.moneropulse.net, skipping.
     7fd483245780        DEBUG   net.dns src/common/dns_utils.cpp:497    DNSSEC validation failed for checkpoint update at URL: segheights.moneropulse.net, skipping.
     7fd483245780        DEBUG   net.dns src/common/dns_utils.cpp:492    DNSSEC not available for checkpoint update at URL: segheights.moneropulse.co, skipping.
     7fd483245780        DEBUG   net.dns src/common/dns_utils.cpp:497    DNSSEC validation failed for checkpoint update at URL: segheights.moneropulse.co, skipping.
     7fd483245780        DEBUG   net.dns src/common/dns_utils.cpp:492    DNSSEC not available for checkpoint update at URL: segheights.moneropulse.se, skipping.
     7fd483245780        DEBUG   net.dns src/common/dns_utils.cpp:497    DNSSEC validation failed for checkpoint update at URL: segheights.moneropulse.se, skipping.
     7fd483245780        WARN    net.dns src/common/dns_utils.cpp:519    WARNING: no two valid MoneroPulse DNS checkpoint records were received
     7fd483245780        DEBUG   net.dns src/common/dns_utils.cpp:492    DNSSEC not available for checkpoint update at URL: segheights.moneropulse.org, skipping.
     7fd483245780        DEBUG   net.dns src/common/dns_utils.cpp:497    DNSSEC validation failed for checkpoint update at URL: segheights.moneropulse.org, skipping.
     7fd483245780        DEBUG   net.dns src/common/dns_utils.cpp:492    DNSSEC not available for checkpoint update at URL: segheights.moneropulse.net, skipping.
     7fd483245780        DEBUG   net.dns src/common/dns_utils.cpp:497    DNSSEC validation failed for checkpoint update at URL: segheights.moneropulse.net, skipping.
     7fd483245780        DEBUG   net.dns src/common/dns_utils.cpp:492    DNSSEC not available for checkpoint update at URL: segheights.moneropulse.co, skipping.
     7fd483245780        DEBUG   net.dns src/common/dns_utils.cpp:497    DNSSEC validation failed for checkpoint update at URL: segheights.moneropulse.co, skipping.
     7fd483245780        DEBUG   net.dns src/common/dns_utils.cpp:492    DNSSEC not available for checkpoint update at URL: segheights.moneropulse.se, skipping.
     7fd483245780        DEBUG   net.dns src/common/dns_utils.cpp:497    DNSSEC validation failed for checkpoint update at URL: segheights.moneropulse.se, skipping.
     7fd483245780        WARN    net.dns src/common/dns_utils.cpp:519    WARNING: no two valid MoneroPulse DNS checkpoint records were received
     7fd483245780        DEBUG   net.dns src/common/dns_utils.cpp:492    DNSSEC not available for checkpoint update at URL: segheights.moneropulse.se, skipping.
     7fd483245780        DEBUG   net.dns src/common/dns_utils.cpp:497    DNSSEC validation failed for checkpoint update at URL: segheights.moneropulse.se, skipping.
     7fd483245780        DEBUG   net.dns src/common/dns_utils.cpp:492    DNSSEC not available for checkpoint update at URL: segheights.moneropulse.org, skipping.
     7fd483245780        DEBUG   net.dns src/common/dns_utils.cpp:497    DNSSEC validation failed for checkpoint update at URL: segheights.moneropulse.org, skipping.
     7fd483245780        DEBUG   net.dns src/common/dns_utils.cpp:492    DNSSEC not available for checkpoint update at URL: segheights.moneropulse.net, skipping.
     7fd483245780        DEBUG   net.dns src/common/dns_utils.cpp:497    DNSSEC validation failed for checkpoint update at URL: segheights.moneropulse.net, skipping.
     7fd483245780        DEBUG   net.dns src/common/dns_utils.cpp:492    DNSSEC not available for checkpoint update at URL: segheights.moneropulse.co, skipping.
     7fd483245780        DEBUG   net.dns src/common/dns_utils.cpp:497    DNSSEC validation failed for checkpoint update at URL: segheights.moneropulse.co, skipping.
     7fd483245780        WARN    net.dns src/common/dns_utils.cpp:519    WARNING: no two valid MoneroPulse DNS checkpoint records were received
     7fd483245780        DEBUG   net.dns src/common/dns_utils.cpp:492    DNSSEC not available for checkpoint update at URL: segheights.moneropulse.se, skipping.
     7fd483245780        DEBUG   net.dns src/common/dns_utils.cpp:497    DNSSEC validation failed for checkpoint update at URL: segheights.moneropulse.se, skipping.
     7fd483245780        DEBUG   net.dns src/common/dns_utils.cpp:492    DNSSEC not available for checkpoint update at URL: segheights.moneropulse.org, skipping.
     7fd483245780        DEBUG   net.dns src/common/dns_utils.cpp:497    DNSSEC validation failed for checkpoint update at URL: segheights.moneropulse.org, skipping.
     7fd483245780        DEBUG   net.dns src/common/dns_utils.cpp:492    DNSSEC not available for checkpoint update at URL: segheights.moneropulse.net, skipping.
     7fd483245780        DEBUG   net.dns src/common/dns_utils.cpp:497    DNSSEC validation failed for checkpoint update at URL: segheights.moneropulse.net, skipping.
     7fd483245780        DEBUG   net.dns src/common/dns_utils.cpp:492    DNSSEC not available for checkpoint update at URL: segheights.moneropulse.co, skipping.
     7fd483245780        DEBUG   net.dns src/common/dns_utils.cpp:497    DNSSEC validation failed for checkpoint update at URL: segheights.moneropulse.co, skipping.
     7fd483245780        WARN    net.dns src/common/dns_utils.cpp:519    WARNING: no two valid MoneroPulse DNS checkpoint records were received

```

I was able to send the transaction though after a pause in a few minutes.

## singpenguin | 2019-08-07T15:56:28+00:00
I Running monero client (v.0.14.1.2)

DNS_PUBLIC=tcp ./monero-0.14.1.2/monero-wallet-rpc --rpc-bind-port 18088 --wallet-file walletfiles --password bepass --rpc-login username:pass

But the transfer was not successful. This is the log:

`2019-08-07 15:43:54.807	W Using default public DNS server(s): 194.150.168.168, 80.67.169.40, 89.233.43.71, 109.69.8.51, 193.58.251.251 (TCP)
2019-08-07 15:43:54.807	I Using public DNS server(s): 194.150.168.168, 80.67.169.40, 89.233.43.71, 109.69.8.51, 193.58.251.251 (TCP)
2019-08-07 15:43:54.808	I adding trust anchor: . IN DS 19036 8 2 49AAC11D7B6F6446702E54A1607371607A1A41855200FD2CE1CDDE32F24E8FB5

2019-08-07 15:43:54.808	I adding trust anchor: . IN DS 20326 8 2 E06D44B80B8F1D39A95C0B0D7C65D08458E880409BBC683457104237C7F8EC8D

2019-08-07 15:43:57.819	D DNSSEC not available for hostname: segheights.moneropulse.co, skipping.
2019-08-07 15:43:57.819	D DNSSEC validation failed for hostname: segheights.moneropulse.co, skipping.
2019-08-07 15:43:57.819	W WARNING: no two valid DNS TXT records were received
2019-08-07 15:43:57.840	W amount=0.999900000000, real_output=1, real_output_in_tx_index=0, indexes: 4958300 8313851 8731757 11245180 11585857 11639686 11667403 11692502 11702782 11708415 11709806 
2019-08-07 15:43:57.845	W amount=0.999900000000, real_output=1, real_output_in_tx_index=0, indexes: 4958300 8313851 8731757 11245180 11585857 11639686 11667403 11692502 11702782 11708415 11709806 
2019-08-07 15:43:57.852	D DNSSEC not available for hostname: segheights.moneropulse.co, skipping.
2019-08-07 15:43:57.852	D DNSSEC validation failed for hostname: segheights.moneropulse.co, skipping.
2019-08-07 15:43:57.852	W WARNING: no two valid DNS TXT records were received
2019-08-07 15:43:57.871	W amount=0.999900000000, real_output=0, real_output_in_tx_index=0, indexes: 8313851 11656451 11688668 11690337 11696072 11704081 11706744 11707210 11707941 11708838 11710186 
2019-08-07 15:43:57.871	W amount=0.001000000000, real_output=1, real_output_in_tx_index=0, indexes: 4413554 7737790 9275413 10763622 11431091 11519549 11676096 11676938 11708564 11709006 11709158 
2019-08-07 15:43:57.881	W amount=0.999900000000, real_output=0, real_output_in_tx_index=0, indexes: 8313851 11656451 11688668 11690337 11696072 11704081 11706744 11707210 11707941 11708838 11710186 
2019-08-07 15:43:57.881	W amount=0.001000000000, real_output=1, real_output_in_tx_index=0, indexes: 4413554 7737790 9275413 10763622 11431091 11519549 11676096 11676938 11708564 11709006 11709158 
2019-08-07 15:43:57.891	W amount=0.999900000000, real_output=0, real_output_in_tx_index=0, indexes: 8313851 11656451 11688668 11690337 11696072 11704081 11706744 11707210 11707941 11708838 11710186 
2019-08-07 15:43:57.891	W amount=0.001000000000, real_output=1, real_output_in_tx_index=0, indexes: 4413554 7737790 9275413 10763622 11431091 11519549 11676096 11676938 11708564 11709006 11709158 
2019-08-07 15:43:58.010	W saving 1 transactions
`

When I use dns server 1.1.1.1, the log is :

`2019-08-07 15:45:35.295	I Using public DNS server(s): 1.1.1.1 (TCP)
2019-08-07 15:45:35.295	I adding trust anchor: . IN DS 19036 8 2 49AAC11D7B6F6446702E54A1607371607A1A41855200FD2CE1CDDE32F24E8FB5

2019-08-07 15:45:35.295	I adding trust anchor: . IN DS 20326 8 2 E06D44B80B8F1D39A95C0B0D7C65D08458E880409BBC683457104237C7F8EC8D

2019-08-07 15:45:35.388	D DNSSEC not available for hostname: segheights.moneropulse.co, skipping.
2019-08-07 15:45:35.388	D DNSSEC validation failed for hostname: segheights.moneropulse.co, skipping.
2019-08-07 15:45:35.388	W WARNING: no two valid DNS TXT records were received
2019-08-07 15:45:35.408	W amount=0.999900000000, real_output=1, real_output_in_tx_index=0, indexes: 3848503 8313851 11245181 11299200 11359614 11528757 11534333 11676846 11697399 11698285 11704698 
2019-08-07 15:45:35.413	W amount=0.999900000000, real_output=1, real_output_in_tx_index=0, indexes: 3848503 8313851 11245181 11299200 11359614 11528757 11534333 11676846 11697399 11698285 11704698 
2019-08-07 15:45:35.420	D DNSSEC not available for hostname: segheights.moneropulse.co, skipping.
2019-08-07 15:45:35.420	D DNSSEC validation failed for hostname: segheights.moneropulse.co, skipping.
2019-08-07 15:45:35.420	W WARNING: no two valid DNS TXT records were received
2019-08-07 15:45:35.439	W amount=0.999900000000, real_output=0, real_output_in_tx_index=0, indexes: 8313851 9519728 11468139 11609384 11645011 11684263 11684711 11700936 11705246 11707929 11709547 
2019-08-07 15:45:35.440	W amount=0.001000000000, real_output=0, real_output_in_tx_index=0, indexes: 7737790 10369379 11148819 11388922 11436692 11576977 11635159 11684823 11696765 11704580 11709649 
2019-08-07 15:45:35.450	W amount=0.999900000000, real_output=0, real_output_in_tx_index=0, indexes: 8313851 9519728 11468139 11609384 11645011 11684263 11684711 11700936 11705246 11707929 11709547 
2019-08-07 15:45:35.450	W amount=0.001000000000, real_output=0, real_output_in_tx_index=0, indexes: 7737790 10369379 11148819 11388922 11436692 11576977 11635159 11684823 11696765 11704580 11709649 
2019-08-07 15:45:35.460	W amount=0.999900000000, real_output=0, real_output_in_tx_index=0, indexes: 8313851 9519728 11468139 11609384 11645011 11684263 11684711 11700936 11705246 11707929 11709547 
2019-08-07 15:45:35.460	W amount=0.001000000000, real_output=0, real_output_in_tx_index=0, indexes: 7737790 10369379 11148819 11388922 11436692 11576977 11635159 11684823 11696765 11704580 11709649 
2019-08-07 15:45:35.578	W saving 1 transactions
`

It has been unsuccessful to send, it has been 2 weeks.
Thanks.

## reardenlife | 2019-08-17T17:00:16+00:00
@singpenguin

> DNS_PUBLIC=tcp ./monero-0.14.1.2/monero-wallet-rpc --rpc-bind-port 18088 --wallet-file walletfiles --password bepass --rpc-login username:pass

Did you use your own daemon,  not the remote node?

BTW plz use special tag to put the logs in it.

## reardenlife | 2019-08-17T17:52:14+00:00
Alright.
As @tobtoht noted, there seems to be a problem in libunbound with high dns timeout as well as in monero itself.
The temporary solution that I am using right now is to put all working dns servers into the properties of network adaptor and make monero-client read from it (by not using DNS_PUBLIC env variable).
Here is code on bash which does it (tested on CentOS7):

```bash
#!/usr/bin/env bash
echo '# Seems to work:'
echo '# 194.150.168.168,80.67.169.40,89.233.43.71,109.69.8.51,193.58.251.251'
echo '# '
echo '# Were not working:'
echo '# 77.109.148.137'
echo

read -e -i "$(echo $(nmcli connection show System\ eth0 | grep -F 'ipv4.dns:' | grep -Eo '[0-9.,]+' | tail -n1))" dns
nmcli connection modify System\ eth0 ipv4.dns "$dns"
systemctl restart NetworkManager
```

Hmm.. https://monerodocs.org/infrastructure/monero-pulse/
It seems that one could specify dns servers in DNS_PUBLIC variable.

```bash
DNS_PUBLIC=tcp://1.1.1.1
```

But will it work for the client (monero-wallet-cli say), not the daemon as showed in the example?

## moneromooo-monero | 2019-08-19T17:05:54+00:00
The new wallet has a --no-dns flag. Moreover, https://github.com/monero-project/monero/pull/5681 removed a dead DNS server. DNS_PUBLIC should work for the wallet client too.

# Action History
- Created by: reardenlife | 2019-03-12T05:22:25+00:00
- Closed at: 2019-08-19T22:30:43+00:00
