---
title: ARM64 Raspberry Pi with Debian - Illegal instruction (core dumped)
source_url: https://github.com/monero-project/monero/issues/2858
author: calvintam236
assignees: []
labels:
- invalid
created_at: '2017-11-24T10:15:15+00:00'
updated_at: '2020-12-21T02:42:08+00:00'
type: issue
status: closed
closed_at: '2017-11-26T07:00:23+00:00'
---

# Original Description
```bash
$ monerod --log-level 2
2017-11-24 10:09:50.037	    ffff9e515420	INFO 	global	src/daemon/main.cpp:279	Monero 'Helium Hydra' (v0.11.1.0-release)
2017-11-24 10:09:50.040	    ffff9e515420	INFO 	daemon	src/daemon/main.cpp:281	Moving from main() into the daemonize now.
2017-11-24 10:09:50.040	    ffff9e515420	INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2017-11-24 10:09:50.041	    ffff9e515420	INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
2017-11-24 10:09:50.050	    ffff9e515420	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2017-11-24 10:09:50.054	    ffff9d3be1f0	DEBUG	net.p2p	src/p2p/net_node.inl:461	dns_threads[0] created for: seeds.moneroseeds.se
2017-11-24 10:09:50.059	    ffff9e515420	DEBUG	net.p2p	src/p2p/net_node.inl:489	dns_threads created, now waiting for completion or timeout of 20000ms
2017-11-24 10:09:50.064	    ffff9cbbe1f0	DEBUG	net.p2p	src/p2p/net_node.inl:461	dns_threads[1] created for: seeds.moneroseeds.ae.org
2017-11-24 10:09:50.066	    ffff97fff1f0	DEBUG	net.p2p	src/p2p/net_node.inl:461	dns_threads[2] created for: seeds.moneroseeds.ch
2017-11-24 10:09:50.071	    ffff977ff1f0	DEBUG	net.p2p	src/p2p/net_node.inl:461	dns_threads[3] created for: seeds.moneroseeds.li
[1511518190] libunbound[3934:0] info: warning: unsupported algorithm for trust anchor . DS IN
[1511518190] libunbound[3934:0] warning: trust anchor . has no supported algorithms, the anchor is ignored (check if you need to upgrade unbound and openssl)
2017-11-24 10:09:50.130	    ffff9d3be1f0	DEBUG	net.p2p	src/p2p/net_node.inl:469	dns_threads[0] DNS resolve done
2017-11-24 10:09:50.130	    ffff9d3be1f0	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[0] addr_str: seeds.moneroseeds.se  number of results: 0
2017-11-24 10:09:50.137	    ffff9cbbe1f0	DEBUG	net.p2p	src/p2p/net_node.inl:469	dns_threads[1] DNS resolve done
2017-11-24 10:09:50.145	    ffff9cbbe1f0	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[1] addr_str: seeds.moneroseeds.ae.org  number of results: 0
2017-11-24 10:09:50.172	    ffff97fff1f0	DEBUG	net.p2p	src/p2p/net_node.inl:469	dns_threads[2] DNS resolve done
2017-11-24 10:09:50.172	    ffff97fff1f0	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[2] addr_str: seeds.moneroseeds.ch  number of results: 0
2017-11-24 10:09:50.175	    ffff977ff1f0	DEBUG	net.p2p	src/p2p/net_node.inl:469	dns_threads[3] DNS resolve done
2017-11-24 10:09:50.176	    ffff977ff1f0	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[3] addr_str: seeds.moneroseeds.li  number of results: 0
2017-11-24 10:09:50.178	    ffff9e515420	DEBUG	net.p2p	src/p2p/net_node.inl:505	DNS lookup for seeds.moneroseeds.se: 0 results
2017-11-24 10:09:50.179	    ffff9e515420	DEBUG	net.p2p	src/p2p/net_node.inl:505	DNS lookup for seeds.moneroseeds.ae.org: 0 results
2017-11-24 10:09:50.180	    ffff9e515420	DEBUG	net.p2p	src/p2p/net_node.inl:505	DNS lookup for seeds.moneroseeds.ch: 0 results
2017-11-24 10:09:50.182	    ffff9e515420	DEBUG	net.p2p	src/p2p/net_node.inl:505	DNS lookup for seeds.moneroseeds.li: 0 results
2017-11-24 10:09:50.182	    ffff9e515420	INFO 	net.p2p	src/p2p/net_node.inl:519	DNS seed node lookup either timed out or failed, falling back to defaults
2017-11-24 10:09:50.183	    ffff9e515420	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 107.152.130.98:18080
2017-11-24 10:09:50.190	    ffff9e515420	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 107.152.130.98:18080
2017-11-24 10:09:50.191	    ffff9e515420	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 161.67.132.39:18080
2017-11-24 10:09:50.192	    ffff9e515420	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 161.67.132.39:18080
2017-11-24 10:09:50.193	    ffff9e515420	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 163.172.182.165:18080
2017-11-24 10:09:50.194	    ffff9e515420	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 163.172.182.165:18080
2017-11-24 10:09:50.195	    ffff9e515420	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 195.154.123.123:28080
2017-11-24 10:09:50.197	    ffff9e515420	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 195.154.123.123:28080
2017-11-24 10:09:50.198	    ffff9e515420	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 198.74.231.92:18080
2017-11-24 10:09:50.200	    ffff9e515420	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 198.74.231.92:18080
2017-11-24 10:09:50.202	    ffff9e515420	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 212.83.172.165:28080
2017-11-24 10:09:50.203	    ffff9e515420	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 212.83.172.165:28080
2017-11-24 10:09:50.205	    ffff9e515420	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 212.83.175.67:18080
2017-11-24 10:09:50.206	    ffff9e515420	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 212.83.175.67:18080
2017-11-24 10:09:50.208	    ffff9e515420	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 5.9.100.248:18080
2017-11-24 10:09:50.210	    ffff9e515420	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 5.9.100.248:18080
2017-11-24 10:09:50.211	    ffff9e515420	DEBUG	net.p2p	src/p2p/net_node.inl:533	Number of seed nodes: 8
2017-11-24 10:09:50.212	    ffff9e515420	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:162	Setting LIMIT: 4.40402e+06 kbps
2017-11-24 10:09:50.213	    ffff9e515420	INFO 	net.p2p	src/p2p/net_node.inl:1883	Set limit-up to 2048 kB/s
2017-11-24 10:09:50.213	    ffff9e515420	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:162	Setting LIMIT: 8.38861e+06 kbps
2017-11-24 10:09:50.214	    ffff9e515420	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:162	Setting LIMIT: 8.38861e+06 kbps
2017-11-24 10:09:50.220	    ffff9e515420	INFO 	net.p2p	src/p2p/net_node.inl:1897	Set limit-down to 8192 kB/s
2017-11-24 10:09:50.220	    ffff9e515420	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:162	Setting LIMIT: 4.40402e+06 kbps
2017-11-24 10:09:50.220	    ffff9e515420	INFO 	net.p2p	src/p2p/net_node.inl:1919	Set limit-up to 2048 kB/s
2017-11-24 10:09:50.221	    ffff9e515420	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:162	Setting LIMIT: 8.38861e+06 kbps
2017-11-24 10:09:50.221	    ffff9e515420	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:162	Setting LIMIT: 8.38861e+06 kbps
2017-11-24 10:09:50.222	    ffff9e515420	INFO 	net.p2p	src/p2p/net_node.inl:1923	Set limit-down to 8192 kB/s
2017-11-24 10:09:50.224	    ffff9e515420	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:795	Set server type to: 2 from name: P2P, prefix_name = P2P
2017-11-24 10:09:50.224	    ffff9e515420	INFO 	net.p2p	src/p2p/net_node.inl:572	Binding on 0.0.0.0:18080
2017-11-24 10:09:50.226	    ffff9e515420	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:734	start accept
2017-11-24 10:09:50.227	    ffff9e515420	INFO 	net.p2p	src/p2p/connection_basic.cpp:164	Spawned connection p2p#0 to 0.0.0.0 currently we have sockets count:1
2017-11-24 10:09:50.227	    ffff9e515420	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:85	test, connection constructor set m_connection_type=2
2017-11-24 10:09:50.229	    ffff9e515420	INFO 	net.p2p	src/p2p/net_node.inl:577	Net service bound to 0.0.0.0:18080
2017-11-24 10:09:50.231	    ffff9e515420	DEBUG	net.p2p	src/p2p/net_node.inl:583	Attempting to add IGD port mapping.
2017-11-24 10:09:54.239	    ffff9e515420	INFO 	net.p2p	src/p2p/net_node.inl:622	No IGD was found.
2017-11-24 10:09:54.240	    ffff9e515420	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2017-11-24 10:09:54.241	    ffff9e515420	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
2017-11-24 10:09:54.241	    ffff9e515420	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:795	Set server type to: 1 from name: RPC, prefix_name = RPC
2017-11-24 10:09:54.242	    ffff9e515420	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:70	Binding on 127.0.0.1:18081
2017-11-24 10:09:54.242	    ffff9e515420	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:734	start accept
2017-11-24 10:09:54.243	    ffff9e515420	INFO 	net.p2p	src/p2p/connection_basic.cpp:164	Spawned connection p2p#0 to 0.0.0.0 currently we have sockets count:1
2017-11-24 10:09:54.244	    ffff9e515420	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:85	test, connection constructor set m_connection_type=1
2017-11-24 10:09:54.244	    ffff9e515420	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2017-11-24 10:09:54.245	    ffff9e515420	INFO 	global	src/daemon/core.h:73	Initializing core...
2017-11-24 10:09:54.247	    ffff9e515420	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:323	Loading blockchain from folder /root/.bitmonero/lmdb ...
2017-11-24 10:09:54.249	    ffff9e515420	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:339	option: fast
2017-11-24 10:09:54.249	    ffff9e515420	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:339	option: async
2017-11-24 10:09:54.249	    ffff9e515420	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:339	option: 1000
2017-11-24 10:09:54.262	    ffff9e515420	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:518	DB map size:     1073741824
2017-11-24 10:09:54.263	    ffff9e515420	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:519	Space used:      24576
2017-11-24 10:09:54.264	    ffff9e515420	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:520	Space remaining: 1073717248
2017-11-24 10:09:54.264	    ffff9e515420	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:521	Size threshold:  0
2017-11-24 10:09:54.266	    ffff9e515420	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:523	Percent used: 0.0000  Percent threshold: 0.8000
2017-11-24 10:09:54.280	    ffff9e515420	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1219	Setting m_height to: 0
2017-11-24 10:09:54.286	    ffff9e515420	DEBUG	hardfork	src/cryptonote_basic/hardfork.cpp:197	reorganizing from 1
2017-11-24 10:09:54.288	    ffff9e515420	DEBUG	hardfork	src/cryptonote_basic/hardfork.cpp:206	reorganization done
2017-11-24 10:09:54.289	    ffff9e515420	INFO 	blockchain	src/cryptonote_core/blockchain.cpp:342	Blockchain not loaded, generating genesis block.
Illegal instruction (core dumped)
```

No idea how to fix this. Using the binary from [https://downloads.getmonero.org/cli/linuxarm8](https://downloads.getmonero.org/cli/linuxarm8).

# Discussion History
## moneromooo-monero | 2017-11-24T17:25:42+00:00
Are you running on armv8 or armv7 ? If the latter, use the armv7 binary.

## calvintam236 | 2017-11-24T19:22:19+00:00
It's raspberry Pi 3 model B, and it is running 64bit kernel (aarch64).

## hyc | 2017-11-26T06:57:20+00:00
raspberry Pi 3 can't run our armv8 binaries since we use AES instructions and the pi 3 CPU doesn't implement them. Use the ARMv7 binary.

## hyc | 2017-11-26T06:57:26+00:00
+invalid

## calvintam236 | 2017-11-26T10:08:27+00:00
@hyc I get this error when I run armv7 version binary: `cannot execute binary file: Exec format error`.. sadly, the only remaining option is to build one on my ARM64..

It will be great to add software AES support on `monerod`..

## hyc | 2017-11-26T13:39:00+00:00
You can use the `NO_AES` option when running cmake to turn it off before building. 

## Zenitur | 2017-12-12T19:57:12+00:00
Will RPi 3 CPU run AES code with aarch64 Linux kernel? Is it presented in hardware? http://www.tal.org/tutorials/raspberry-pi3-build-64-bit-kernel

## hyc | 2017-12-13T00:19:19+00:00
@Zenitur no. I stated that explicitly already in https://github.com/monero-project/monero/issues/2858#issuecomment-346988798

Pi 3 is worthless for Monero.

## nasaWelder | 2017-12-13T00:36:07+00:00
Pi2 runs it fine. Arm 64 is not the correct build. Need arch 7

On Dec 12, 2017 5:19 PM, "hyc" <notifications@github.com> wrote:

> @Zenitur <https://github.com/zenitur> no. I stated that explicitly
> already in #2858 (comment)
> <https://github.com/monero-project/monero/issues/2858#issuecomment-346988798>
>
> Pi 3 is worthless for Monero.
>
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/2858#issuecomment-351239466>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AgV3MzgQf6kHoG3bJgQcoQtTBUe8HblVks5s_xgRgaJpZM4QpnpE>
> .
>


## realindiahotel | 2020-12-19T03:07:16+00:00
> @Zenitur no. I stated that explicitly already in [#2858 (comment)](https://github.com/monero-project/monero/issues/2858#issuecomment-346988798)
> 
> Pi 3 is worthless for Monero.

This is 100% false information. I ran a Monero full node on my Pi 3b+ very successfully until yas broke it in v16. Worthless for mining, sure. But as a full node contributing to the network it is fantastic, 15w max power draw means I can keep it on 24/7 for minimal expense and contribute to the P2P network, and importantly, it serves me as a trusted node for my Cake wallet. So what you are saying is 100% incorrect and I suspect it's dunces like yourself spouting this misinformation that has steered the project away from having proper Pi support.

## hyc | 2020-12-19T05:57:52+00:00
And I was the one who ported the Monero code base to ARM and raspberry pi *1* in the first place. Of course it runs, but Pi is still worthless junk. Get an Odroid or a Pine64.

## realindiahotel | 2020-12-19T06:00:10+00:00
> And I was the one who ported the Monero code base to ARM and raspberry pi _1_ in the first place. Of course it runs, but Pi is still worthless junk. Get an Odroid or a Pine64.

This is a biased opinion. As I said it worked wonderfully on my 3b+. The fact that you don't like the hardware is irrelevant.

Having a quick look at Pine64 I'm not seeing anything matching my Pi4 8GB

## hyc | 2020-12-19T06:11:08+00:00
No Pi processor has hardware AES support - that's a simple fact. Every Pi device up to Model 3 ships with a 32bit OS, that's also a fact. Every Pi up to Model 3 has a total I/O bandwidth of only 20MB/s, again simple fact. These facts together mean that every Pi will use more electricity than any other comparable ARM64 device and operate more slowly. Too slowly to be useful as network activity grows. While we measure other CPUs in Hashes per second, on Pis we measure in seconds per hash.

## realindiahotel | 2020-12-19T06:15:03+00:00
> No Pi processor has hardware AES support

And yet when I'm looking at the PineAP I am seeing it is using the same Arm-cortex-v72 CPU as the Pi 4 (or at least the ROCKPro64 which I'm guessing is the flagship?). What do you need AES-NI for when you are not mining anyway? You will never mine successfully on a single board so the comparison is absolutely pointless.

## vtnerd | 2020-12-19T06:23:30+00:00
The crypto portion is optional, and the Pi 4 does not have that optional extension in the CPU. The AES instructions are still used for block verification. You can do a custom build with AES instruction disabled.

## hyc | 2020-12-19T06:26:01+00:00
You're clearly too stupid to be having this conversation.

AES-NI is an optional part of the Cortex instruction set. Raspberry/Broadcom cheaped out and didn't license it for their chips. Every other ARM64 vendor supports it though. Raspberry/Broadcom is literally the bottom of the barrel implementation of Cortex.

And you still need AES for validating incoming blocks. Try syncing the blockchain from scratch on a Pi. I finally gave up on my Pi when I calculated it would never catch up to the network. Try catching up after being offline for only 1 day.

And - on other machines like RockPro64, you *can* mine, and the power efficiency is better than Intel chips so no, the comparison is not pointless.

## realindiahotel | 2020-12-19T06:31:20+00:00
> You're clearly too stupid to be having this conversation.

LOL



> And you still need AES for validating incoming blocks.

Demonstrating that you have no clue what you are talking about. My Pi 3b+ as I mentioned, worked as a full node completely fine without AES-NI.

> Try syncing the blockchain from scratch on a Pi. I finally gave up on my Pi when I calculated it would never catch up to the network. Try catching up after being offline for only 1 day.

I did exactly this on my pi 3b+. Just because you are too useless to make it work doesn't mean it doesn't work for others. And I could have my node down for a month and bring it up and it would sync, take some time sure but that's fine, I don't expect a Pi to be a trail blazer, long as it works, which it does.

> you _can_ mine, and the power efficiency is better than Intel chips

You can mine on the Pi too..... but doesn't mean you're going to, it's pointless you'd be lucky to make 10 cents.


## realindiahotel | 2020-12-19T06:32:33+00:00
> The AES instructions are still used for block verification. You can do a custom build with AES instruction disabled.

Thanks yes that's what I'm trying now. Is the compiler smart enough to detect no AES-NI and disable it automatically or do I have to set flags?

## hyc | 2020-12-19T06:51:16+00:00
> Just because you are too useless to make it work doesn't mean it doesn't work for others.

Haha you're funny. I'm the guy who made it work on ARM64 in the first place.

https://github.com/monero-project/monero/commit/69b59186f309609ee9d7b6ff3a35dd5e32d9d7dc#diff-1791ca6db56ff6236c17c6b8c2d6bc1516adbf806345d2e0ffc3b3a1b60e8287

Since you've never contributed any code here, you're in no position to be calling actual developers useless.


## realindiahotel | 2020-12-19T06:52:43+00:00
> Haha you're funny. I'm the guy who made it work on ARM64 in the first place.

Yet you could not get it to work properly for you, where others have had great success. Instead you gave up and called the Pi 3 worthless.

> Since you've never contributed any code here, you're in no position to be calling actual developers useless.

I disagree. Contributing code doesn't grant you immunity from uselessness.

## hyc | 2020-12-19T06:56:06+00:00
No, the code works fine. I wrote support for ARM64 both with and without AES-NI, so of course it works. But Pis are still too slow to be useful, and other systems are better, for about the same price. 

The only reason you're able to use it is because I wrote the code that supports it. Both with
https://github.com/monero-project/monero/commit/69b59186f309609ee9d7b6ff3a35dd5e32d9d7dc#diff-1791ca6db56ff6236c17c6b8c2d6bc1516adbf806345d2e0ffc3b3a1b60e8287R684

and without crypto extensions 
https://github.com/monero-project/monero/commit/69b59186f309609ee9d7b6ff3a35dd5e32d9d7dc#diff-1791ca6db56ff6236c17c6b8c2d6bc1516adbf806345d2e0ffc3b3a1b60e8287R979

I've tested on Allwinner, Amlogic, HiSilicon, Mediatek, Qualcomm, Rockchip , (and of course Broadcom) - basically every ARM64 maker that consumers can get their hands on. All of them perform better than Broadcom, all of them perform better than Pis, and they're all readily available.

You're just a non-contributing complainer.

## realindiahotel | 2020-12-19T06:58:58+00:00
> But Pis are still too slow to be useful, and other systems are better, for about the same price.

They are useful as a full node. And also these words are useless for anyone who receives a Pi for xmas or already has one. It's true that it takes some time to sync, but once it syncs it's fine. I can run an XMR full node and PMS from the one Pi Simultaneously (without video transcoding) no problems at all.

Or at least I could until v16, which is when I'm guessing AES-NI started being forced on the binaries

> You're just a non-contributing complainer.

Disagree, I think that wanting to run a full node 24/7 and support the network is contributing.

> and without crypto extensions

Which for some reason isn't compiled and supplied to the community as a bin. Probably because of your rubbish misconceptions that the Pi is useless, as I've said.

## realindiahotel | 2020-12-21T02:37:30+00:00
For anyone coming across this in the future wanting to run a full node on their Pi, follow the install instructions on the monero repo however before running your make command, edit the `Makefile` and any line that has `-D xxxx` also add `-DAES_NO=ON` and then it will work.

If you have a Pi 4b 8GB I recommend running `make -j 4` as the 4 threads smash the compile out in about an hour (and you should also OC your Pi 4b to 2000Mhz it does so at very low temps I never get above 56 deg c with a fan case).

# Action History
- Created by: calvintam236 | 2017-11-24T10:15:15+00:00
- Closed at: 2017-11-26T07:00:23+00:00
