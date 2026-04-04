---
title: 'ZMQ DESTROYED by p2pool daemon. '
source_url: https://github.com/monero-project/monero/issues/8199
author: Gingeropolous
assignees: []
labels: []
created_at: '2022-03-02T03:47:09+00:00'
updated_at: '2025-12-28T22:45:44+00:00'
type: issue
status: closed
closed_at: '2025-12-28T22:45:44+00:00'
---

# Original Description
I checked on my p2pool daemon to discover it thought the monerod daemon was stuck.

a restart of monerod fixed it.

grepping the logs for ERROR returned this

 2022-02-28 15:01:43.241 [P2P3]  ERROR   net.zmq src/rpc/zmq_pub.cpp:546 Unable to send ZMQ/Pub - ZMQ server destroyed

 2022-02-28 14:59:05.955     7f74597fa700        ERROR   net.zmq src/rpc/zmq_server.cpp:174      ZMQ RPC Server Error: thrown at zmq_server.cpp:
161: Resource temporarily unavailable

please lemme know if more logs are needed before the great logrotate devours the logs forever. 

so far has only happened once, and it happened after updating to the most recent p2pool. Prior to this update, I had never experienced this before - I've been running p2pool since its launch.... months ago?

# Discussion History
## sethforprivacy | 2022-03-02T13:37:33+00:00
I have also seen this happen once, and a monerod restart resolved it and has not occurred since.

Will keep an eye out for it happening again in the future!

## sethforprivacy | 2022-09-14T12:47:24+00:00
I have had this relatively frequently, and last seen with high CPU usage by monerod. Still seems to be an issue on v0.18.1.0.

## sethforprivacy | 2022-09-20T17:59:23+00:00
I get this log entry before the log spam:

`ZMQ RPC Server Error: thrown at zmq_server.cpp:161: Resource temporarily unavailable`

## SChernykh | 2022-09-20T19:38:07+00:00
@vtnerd 
My thoughts from IRC so they don't get lost:
```
<sech1> https://splunktool.com/zmq-resource-temporarily-unavailable-when-connecting-zmq-socket
<sech1> zmq calls can throw exceptions, so it makes sense to add try...catch in zmq_server.cpp
<sech1> no, wait, it's not zmq that throws an exception
<sech1> zmq returns error EAGAIN (resource temporarily unavailable) and then MONERO_UNWRAP macro throws
<sech1> so it should probably check for EAGAIN there and just ignore it
<sech1> EAGAIN means non-blocking sockets can't receive/send data right now, so it should just continue with the next loop iteration instead of throwing up
```

## vtnerd | 2022-09-20T20:37:14+00:00
The problem is that there is a poll call and I botched the array setup sequence - the values are never reset for the next poll call. So if ZeroMQ doesn't reset the values, our server code is getting an old value and being told to read a socket in non-blocking mode that potentially has no data.

## vtnerd | 2022-09-24T00:48:56+00:00
I've looked into this, and the docs state that `revent` should be cleared before returning. There's tons of code paths within the ZeroMQ for this function, so I haven't been able to confirm this. The only other thing I spot is the code should be checking for `ZMQ_POLLIN` instead of checking for _any_ flags. Otherwise, this could be a bug within ZeroMQ. A `ZMQ_POLLIN` is supposed to indicate that at least one _message_ is available on the socket, so `EAGAIN` should never be returned afaik.

I'll have a PR for tomorrow for testing which simply clears `revents` and checks for `ZMQ_POLLIN` directly. I'll need @Gingeropolous and @sethforprivacy to test because I'm not sure how to reproduce (easily in a consistent way) at the moment.

## vtnerd | 2022-09-24T15:20:21+00:00
See #8592 . @SChernykh I haven't dropped the `MONERO_UNWRAP` code (yet) because in the worse case this becomes a busy spin loop. The poll code should only be returning when there is a message to read.

My next investigation is whether `ZMQ_POLLIN` is returned when 1+ plus parts of the message, but not the whole message, is received. This would explain why its so transient.

## trasherdk | 2022-10-05T03:53:06+00:00
I've got a lot of those. This is on `stagenet`. `testnet` is pretty much the same.

It's not like the host is under load `Load average: 0.63 0.67 0.73`. 
If I remember correctly, this started with `0.18.1.0`.

```
2022-10-05 03:31:32.536        E Unable to send ZMQ/Pub - ZMQ server destroyed
2022-10-05 03:31:32.536        E Unable to send ZMQ/Pub - ZMQ server destroyed
2022-10-05 03:31:47.469        E Unable to send ZMQ/Pub - ZMQ server destroyed
2022-10-05 03:32:20.679        E Unable to send ZMQ/Pub - ZMQ server destroyed
2022-10-05 03:32:20.679        E Unable to send ZMQ/Pub - ZMQ server destroyed
2022-10-05 03:34:06.663        I background mining is enabled, but not started, waiting until start triggers
2022-10-05 03:34:27.632        I background mining is enabled, but not started, waiting until start triggers
```

```
status
Height: 1194260/1194260 (100.0%) on stagenet, smart mining at 63 H/s, net hash 2.08 kH/s, v16, 5(out)+6(in) connections, uptime 3d 20h 32m 53s
print_net_stats
Received 755791649 bytes (720.78 MB) in 617365 packets in 3.9 days, average 2.21 kB/s = 0.22% of the limit of 1.00 MB/s
Sent 598561517 bytes (570.83 MB) in 345441 packets in 3.9 days, average 1.75 kB/s = 0.17% of the limit of 1.00 MB/s
```

```
2022-10-05 03:34:48.639   I background mining is enabled, but not started, waiting until start triggers
2022-10-05 03:35:09.761        I background mining is enabled, but not started, waiting until start triggers
2022-10-05 03:35:42.600        E Unable to send ZMQ/Pub - ZMQ server destroyed
2022-10-05 03:35:42.600        E Unable to send ZMQ/Pub - ZMQ server destroyed
2022-10-05 03:36:20.769        I background mining is enabled, but not started, waiting until start triggers
```

```
version 
0.18.1.1-release
```
```
2022-10-05 03:37:11.777   I background mining is enabled, but not started, waiting until start triggers
2022-10-05 03:37:32.777        I background mining is enabled, but not started, waiting until start triggers
2022-10-05 03:37:37.159        E Unable to send ZMQ/Pub - ZMQ server destroyed
2022-10-05 03:37:37.159        E Unable to send ZMQ/Pub - ZMQ server destroyed
```

## SChernykh | 2022-10-05T05:40:44+00:00
@trasherdk then you should compile monerod with https://github.com/monero-project/monero/pull/8592 and check if it fixes the problem.

## trasherdk | 2023-01-18T22:36:59+00:00
Okay, it took a while, but #8592 did not fix this thing.

When it started to happen on the `mainnet` node, I firewalled `ZMQ` to be accessible to my IP addresses only, so that's safe.
On both `stagenet` and `testnet`  nodes, ZMQ is down this morning. 
`testnet` is running `0.18.1.2-release` and `stagenet` is running `0.18.1.1-41ca021ee` => #8592
```
2023-01-18 09:05:56.008        I Version 0.18.1.2 of monero for linux-x64 is available: https://downloads.getmonero.org/cli/monero-linux-x64-v0.18.1.2.tar.bz2, SHA256 hash 7d51e7072351f65d0c7909e745827cfd3b00abe5e7c4cc4c104a3c9b526da07e
2023-01-18 09:30:12.437        I background mining is enabled, but not started, waiting until start triggers
2023-01-18 09:30:33.439        I background mining is enabled, but not started, waiting until start triggers
2023-01-18 09:44:49.883        I Found block <2ce32bb09b37945e0011ab62d4151a63a76557c318a14c4cd83281756ce2c5c3> at height 1269679 for difficulty: 451280
2023-01-18 09:58:36.438        I Found block <ab87d88928dcb4b6995c2d21251c1a3856ef22386ca87c8c1e78f52ccd6d9df2> at height 1269687 for difficulty: 449642
2023-01-18 10:00:25.389        I background mining is enabled, but not started, waiting until start triggers
2023-01-18 10:18:52.155        E ZMQ RPC Server Error: thrown at zmq_server.cpp:161: Resource temporarily unavailable
2023-01-18 10:22:00.081        E Unable to send ZMQ/Pub - ZMQ server destroyed
2023-01-18 10:22:00.081        E Unable to send ZMQ/Pub - ZMQ server destroyed
```

## vtnerd | 2023-01-19T16:34:36+00:00
@trasherdk are you using the binaries provided by Monero core? or this custom built? I'm mainly curious of the ZMQ version you are running. Also, are you using the ZMQ server? Monero-lws or similar?

## trasherdk | 2023-01-20T07:13:12+00:00
@vtnerd mainnet and testnet is the release binaries. stagenet is `Monero 'Fluorine Fermi' (v0.18.1.1-41ca021ee)` binaries provided by @selsta (i think it was).

I'm not doing anything hitting the ZMQ port. I'm guessing something nasty on the wire is causing this issue.
I should probably firewall testnet and stagenet too :(

## trasherdk | 2023-01-20T14:32:13+00:00
Okay, firewall it is then.
```
status
Height: 1271118/1271118 (100.0%) on stagenet, smart mining at 103 H/s, net hash 3.09 kH/s, v16, 11(out)+12(in) connections, uptime 1d 10h 21m 33s
print_net_stats
Received 90464724 bytes (86.27 MB) in 198275 packets in 1.4 days, average 731 B/s = 0.07% of the limit of 1.00 MB/s
Sent 129308398 bytes (123.32 MB) in 153587 packets in 1.4 days, average 1.02 kB/s = 0.10% of the limit of 1.00 MB/s
2023-01-20 09:21:16.417   I background mining is enabled, but not started, waiting until start triggers
2023-01-20 09:21:37.428        I background mining is enabled, but not started, waiting until start triggers
2023-01-20 09:30:08.463        I background mining is enabled, but not started, waiting until start triggers
2023-01-20 09:30:29.467        I background mining is enabled, but not started, waiting until start triggers
2023-01-20 09:33:43.801        E ZMQ RPC Server Error: thrown at zmq_server.cpp:161: Resource temporarily unavailable
2023-01-20 09:35:13.843        E Unable to send ZMQ/Pub - ZMQ server destroyed
```

## vtnerd | 2023-01-21T21:06:15+00:00
The ZMQ port should only be listening on the localhost. Can you confirm this? I'm leaning towards some memory corruption bug (possibly elsewhere in the system).

## trasherdk | 2023-01-23T14:12:22+00:00
Well, the client hitting the ZMQ server is not on the same host, so the localhost thingy is out.

The firewall looks like this, if you are a stranger.

```
PORT      STATE    SERVICE
18081/tcp filtered unknown
18082/tcp filtered unknown
18083/tcp filtered unknown
28080/tcp open     thor-engine
28081/tcp filtered unknown   <=== rpc-bind-port (localhost)
28082/tcp filtered unknown   <=== zmq-rpc-bind
28083/tcp filtered unknown   <=== zmq-pub=tcp
28084/tcp open     unknown   <=== rpc-restricted-bind
38080/tcp open     unknown
38081/tcp filtered unknown   <=== rpc-bind-port (localhost)
38082/tcp filtered unknown   <=== zmq-rpc-bind
38083/tcp filtered unknown   <=== zmq-pub=tcp
38084/tcp open     unknown   <=== rpc-restricted-bind
38091/tcp open     unknown
38092/tcp open     unknown
38094/tcp open     unknown
```

And when one of my hosts take a peek, No `mainnet` ports, no daemon running.

```
PORT      STATE SERVICE
28080/tcp open  unknown
28082/tcp open  unknown
28083/tcp open  unknown
28084/tcp open  unknown
38080/tcp open  unknown
38082/tcp open  unknown
38083/tcp open  unknown
38084/tcp open  unknown
38091/tcp open  unknown
38092/tcp open  unknown
38094/tcp open  unknown
```

It could be a memory corruption issue, but it's caused by something hitting the port from outside.
Memory is never exhausted. Less than 50% used of 8GB. CPU max at 1.3 on 4 cores.

After the firewall thingy got up, I have had zero problems.

```sh
$ node monero/src/node-zmq-5.x.js 
Loading network specific config from /path/to/node-test-snippets/.env.stagenet
Subscriber connecting to host.example.com:38083 on stagenet
[{"id":"d11962fdf2547e2442cd00652bddb2875e23915231777c4ef043282d69a249ab","blob_size":2206,"weight":2206,"fee":242660000}]
[{"id":"b148f4170021075b639df5e7603adbf2036416efcdb57e05fcf91b1e0520d0ac","blob_size":1527,"weight":1527,"fee":656610000}]
[{"id":"14bc006c2a877dc872def6f6725e659fdfd8f3da168b13b86d65635d470417c7","blob_size":2209,"weight":2209,"fee":949870000}]
[{"id":"4bf5b7859e34e4449524dc304b6b9ff77e74dabe7b49402da8af13afec77a9ca","blob_size":2204,"weight":2204,"fee":947720000}]
[{"id":"c264c33fc272867acccbceef057f3ab1c1048c2af37ccc920f59cdcdbc7e705e","blob_size":2215,"weight":2215,"fee":243650000}]
[{"id":"57cd6239744c3a7b42505dd87c41173467a4c38effe98b0959c004935a5aeaae","blob_size":1653,"weight":2113,"fee":232430000}]
[{"id":"8848414b6a0596ad41ce9c4d4081913f73080825c36e29bc5146475b708fe469","blob_size":1528,"weight":1528,"fee":168080000}]
[{"id":"5b5ab21c14a3215363c3c1bd40079e57e019969264ea22984af039abb395d001","blob_size":1529,"weight":1529,"fee":168190000}]
[{"id":"8b9b2c2b26ce3b62ecf2a648e5f94dd62cf7f8eb4b9777cfca07be713dbe4116","blob_size":2204,"weight":2204,"fee":947720000}]
[{"id":"7d972e2f4ee2cc8ddc0f0f9b775e0bd8711dba26c9188e8206be7be411e476a7","blob_size":2210,"weight":2210,"fee":243100000}]
[{"id":"46317bce180e066e96022ac6754c747d20af802973a7dc2fc0758e9d56baffc7","blob_size":1530,"weight":1530,"fee":168300000}]
[{"id":"c893f7d17382a09f1fb4e043b0fed22142d48a20811ba2491528038e0fcd9b78","blob_size":1529,"weight":1529,"fee":168190000}]
[{"id":"a123a0cdb7ec7242aedb2ad9e5deb8b28e4afad79abc9a32e3fdafc6f153af4e","blob_size":2206,"weight":2206,"fee":242660000}]
[{"id":"8166b3d6a8823070bc999d69741ccc04854f429d572ae6d6d18ede544592f68e","blob_size":2208,"weight":2208,"fee":242880000}]
[{"id":"39d7599a39b19d512866f7275e90f059e98f8e31e593f69689a8ec1caad0ab19","blob_size":2204,"weight":2204,"fee":242440000}]
[{"id":"0c65a041ddaf32175406bbdbc455df7ba63e12bbdfc24ef312ed1e2fa10d4fcb","blob_size":2208,"weight":2208,"fee":949440000}]
[{"id":"0046b74faf244e8abf25de940e248f92cfea3521d6cd4c7a290abac659e1df84","blob_size":2209,"weight":2209,"fee":242990000}]
[{"id":"350ae1d698589ef8b89466b5ef32fafe74a853727a00e784da494d4496be0dc6","blob_size":1525,"weight":1525,"fee":167750000}]
[{"id":"ab076728403f639adb7814b39f547faf578eb2811432e96d3030696639d4607d","blob_size":2204,"weight":2204,"fee":242440000}]
[{"id":"8a952ce07fa26901ed4a06361620ebd4b545837dcb04e21c98c12ae3c0ae9458","blob_size":2207,"weight":2207,"fee":242770000}]
[{"id":"657388b69b1b8f8db927694da35c172188f597516ec9bcf714f265fc1b563175","blob_size":1527,"weight":1527,"fee":167970000}]
[{"id":"836ecd2de63bc488caafdb2803ff24a20ebc77ad64e0f2d16b10f9349918060d","blob_size":2203,"weight":2203,"fee":242330000}]
[{"id":"6043ec54ad76f56b37c10566e1807e9f74945859c2376e9a5d8ea9a53b4c3523","blob_size":2213,"weight":2213,"fee":951590000}]
[{"id":"3baba4717bb2ae52ea10f35e26f0028287cc98a2c09abe4037a213d20605b810","blob_size":2032,"weight":3465,"fee":381150000}]
[{"id":"fb2c1002af32990aaf0d1d4cbeaf5320f1f017a9e8ba6381da0cca165d80c3de","blob_size":1524,"weight":1524,"fee":167640000}]
[{"id":"ff09c3649a57e97708455696f3ba8534e76a7de7ca1e996f86998b266b9160cb","blob_size":1527,"weight":1527,"fee":167970000}]
```

## vtnerd | 2023-01-24T15:42:17+00:00
@trasherdk so you enabled pub/sub too on `monerod`?

## trasherdk | 2023-01-27T03:03:43+00:00
Yes. Both.
```
18082/tcp filtered unknown   <=== zmq-rpc-bind
18083/tcp filtered unknown   <=== zmq-pub=tcp
```

```sh
$ MONERO_NET=mainnet node monero/src/node-zmq-5.x.js 
Loading network specific config from /path/to/node-test-snippets/.env.mainnet
Subscriber connecting to host.example.com:18083 on mainnet
[{"id":"fb2af27d464fba15ca18ffb5e2104ceea2f6aeca0e66202bd2206ee9ba3f9702","blob_size":1530,"weight":1530,"fee":30600000}]
[{"id":"046087f621a2b00259b10fc19ee838931f92ddccd85c989fa5ce0a69a309c5ff","blob_size":2223,"weight":2223,"fee":45300000}]
[{"id":"6b697143e1840e4182242697e2d287913328e49ce101e183317b7813e01cafb6","blob_size":2213,"weight":2213,"fee":44260000}]
[{"id":"650ee3f8058eb8214d58fdb2f027316d9ab24f7335830e5660826faf3f84afc7","blob_size":1534,"weight":1534,"fee":30680000}]
[{"id":"51fe3f5e02c20461820b26fbff2816936a5a08295a81b2d3d6484f077dc46f99","blob_size":1535,"weight":1535,"fee":30700000}]
[{"id":"c39b7184efedaf5a990278212460c6b7c16b92648194d9101eab3913295acacd","blob_size":1531,"weight":1531,"fee":122480000}]
```

## SChernykh | 2023-08-11T08:21:52+00:00
I got this error, my monerod binary was built from https://github.com/SChernykh/monero/commit/2f05267f8c519a21dbba44fcb954b9a5ad29743b
So #8592 doesn't fix it @vtnerd 
```
2023-08-10 19:15:49.458	    7ef8637fe700	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::system_error
2023-08-10 19:15:49.458	    7ef8637fe700	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2023-08-10 19:15:49.458	    7ef8637fe700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0x116) [0x561a3c76655c]:__cxa_throw+0x116) [0x561a3c76655c]
2023-08-10 19:15:49.458	    7ef8637fe700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] ./monerod(+0xc0f9b) [0x561a3c761f9b] 
2023-08-10 19:15:49.459	    7ef8637fe700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3] ./monerod(+0x660665) [0x561a3cd01665] 
2023-08-10 19:15:49.459	    7ef8637fe700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4]  0x1143b) [0x7f246b22743b]:_64-linux-gnu/libboost_thread.so.1.71.0(+0x1143b) [0x7f246b22743b]
2023-08-10 19:15:49.459	    7ef8637fe700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5]  0x8609) [0x7f246ae33609]:_64-linux-gnu/libpthread.so.0(+0x8609) [0x7f246ae33609]
2023-08-10 19:15:49.459	    7ef8637fe700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6]  0x43) [0x7f246ad56133]:_64-linux-gnu/libc.so.6(clone+0x43) [0x7f246ad56133]
2023-08-10 19:15:49.459	    7ef8637fe700	INFO	stacktrace	src/common/stack_trace.cpp:172	
2023-08-10 19:15:49.460	    7ef8637fe700	ERROR	net.zmq	src/rpc/zmq_server.cpp:177	ZMQ RPC Server Error: thrown at zmq_server.cpp:161: Resource temporarily unavailable
2023-08-10 19:15:49.591	[P2P9]	ERROR	net.zmq	src/rpc/zmq_pub.cpp:547	Unable to send ZMQ/Pub - ZMQ server destroyed
2023-08-10 19:16:01.898	[P2P9]	ERROR	net.zmq	src/rpc/zmq_pub.cpp:547	Unable to send ZMQ/Pub - ZMQ server destroyed
2023-08-10 19:16:08.997	[P2P2]	ERROR	net.zmq	src/rpc/zmq_pub.cpp:547	Unable to send ZMQ/Pub - ZMQ server destroyed
2023-08-10 19:16:15.351	[P2P6]	ERROR	net.zmq	src/rpc/zmq_pub.cpp:547	Unable to send ZMQ/Pub - ZMQ server destroyed
2023-08-10 19:16:41.788	[P2P4]	ERROR	net.zmq	src/rpc/zmq_pub.cpp:547	Unable to send ZMQ/Pub - ZMQ server destroyed
2023-08-10 19:16:43.948	[P2P3]	ERROR	net.zmq	src/rpc/zmq_pub.cpp:547	Unable to send ZMQ/Pub - ZMQ server destroyed
```

## vtnerd | 2023-08-11T13:27:32+00:00
I guess we'll have to make this a soft error. Hopefully the next loop iteration the poll code doesn't return that data is available, because that would turn this into a busy spin loop (as already mentioned).

## vtnerd | 2023-08-13T18:44:10+00:00
@SChernykh you think its possible that there is a out-of-bounds write somewhere in the code producing this? Usually more stuff goes haywire than just one specific issue but this is really odd the more I look into it.

## SChernykh | 2023-08-13T18:46:58+00:00
It is possible of course. Did anyone try to run monerod with address sanitizer or valgrind?

## vtnerd | 2023-08-13T19:05:46+00:00
@SChernykh I have not done so recently, sounds like a good idea on one of my Gentoo boxes. In the meantime #8592 now has an additional commit that turns an `EAGAIN` error in the ZMQ server into a `MWARNING` without shutdown. The thinking is to detect whether its one-time spurious event or some permanent state of the ZMQ code. 

## vtnerd | 2023-08-13T22:57:00+00:00
#8238 might be related. Now running `monerod` with address sanitizer. Nothing issues in the early startup or sync stages.

# Action History
- Created by: Gingeropolous | 2022-03-02T03:47:09+00:00
- Closed at: 2025-12-28T22:45:44+00:00
