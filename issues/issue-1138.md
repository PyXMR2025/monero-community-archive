---
title: '"no active pools, stop mining"'
source_url: https://github.com/xmrig/xmrig/issues/1138
author: rhlug
assignees: []
labels:
- bug
created_at: '2019-08-24T00:58:51+00:00'
updated_at: '2022-10-26T14:30:07+00:00'
type: issue
status: closed
closed_at: '2019-08-31T03:04:47+00:00'
---

# Original Description
Randomly my mining will just stop.  It wont try to reconnect once it receives the message "no active pools, stop mining".     If I stop and restart the mining, it resumes just fine.

```
# ./xmrig -V
XMRig 2.99.4-beta
 built on Aug  7 2019 with GCC 7.4.0
 features: 64-bit AES

libuv/1.18.0
OpenSSL/1.1.0g
hwloc/1
```

Here are a couple recent runs from 2 different rigs that I just had to restart.

```
[2019-08-24 00:12:42.250] accepted (3857/0) diff 180007 (209 ms)
[2019-08-24 00:13:00.267] new job from pool.loki.hashvault.pro:3333 diff 180090 algo rx/loki height 343199
[2019-08-24 00:13:02.345] accepted (3858/0) diff 180090 (196 ms)
[2019-08-24 00:13:17.721] speed 10s/60s/15m 5919.7 5918.3 5915.4 H/s max 6390.0 H/s
[2019-08-24 00:13:52.396] accepted (3859/0) diff 180090 (205 ms)
[2019-08-24 00:14:17.771] speed 10s/60s/15m 5915.1 5902.0 5914.4 H/s max 6390.0 H/s
[2019-08-24 00:14:27.220] no active pools, stop mining
[2019-08-24 00:15:17.850] speed 10s/60s/15m n/a 5907.0 5914.3 H/s max 6390.0 H/s
[2019-08-24 00:16:17.953] speed 10s/60s/15m n/a n/a 5914.2 H/s max 6390.0 H/s
[2019-08-24 00:17:18.055] speed 10s/60s/15m n/a n/a 5914.3 H/s max 6390.0 H/s
[2019-08-24 00:18:18.153] speed 10s/60s/15m n/a n/a 5914.3 H/s max 6390.0 H/s
```


```
[2019-08-24 00:04:18.624] accepted (3944/0) diff 165873 (229 ms)
[2019-08-24 00:05:00.201] new job from pool.loki.hashvault.pro:3333 diff 167582 algo rx/loki height 343194
[2019-08-24 00:05:00.693] accepted (3945/0) diff 167582 (195 ms)
[2019-08-24 00:05:08.436] speed 10s/60s/15m 6138.0 6141.3 6148.9 H/s max 6585.7 H/s
[2019-08-24 00:05:09.325] accepted (3946/0) diff 167582 (176 ms)
[2019-08-24 00:05:27.380] accepted (3947/0) diff 167582 (178 ms)
[2019-08-24 00:05:49.445] new job from pool.loki.hashvault.pro:3333 diff 167582 algo rx/loki height 343195
[2019-08-24 00:06:08.471] speed 10s/60s/15m 6114.3 6134.0 6147.7 H/s max 6585.7 H/s
[2019-08-24 00:06:16.979] no active pools, stop mining
[2019-08-24 00:07:08.555] speed 10s/60s/15m n/a 6136.5 6147.0 H/s max 6585.7 H/s
[2019-08-24 00:08:08.636] speed 10s/60s/15m n/a n/a 6146.4 H/s max 6585.7 H/s
[2019-08-24 00:09:08.726] speed 10s/60s/15m n/a n/a 6145.5 H/s max 6585.7 H/s
[2019-08-24 00:10:08.815] speed 10s/60s/15m n/a n/a 6145.1 H/s max 6585.7 H/s
[2019-08-24 00:11:08.907] speed 10s/60s/15m n/a n/a 6143.8 H/s max 6585.7 H/s
[2019-08-24 00:12:09.001] speed 10s/60s/15m n/a n/a 6142.3 H/s max 6585.7 H/s
```

# Discussion History
## xmrig | 2019-08-26T11:46:31+00:00
Please update to recent version (3.1.0)
Thank you.

## k0ste | 2019-08-28T00:51:20+00:00
@xmrig, we also catch this issue on 3.1.0. When network guys do maintenance with access switch uplink - all miners behind this switch stop working. And can't recovery.


```
Aug 27 21:15:36 r9-s1-01-01 xmrig[762]: speed 10s/60s/15m 712.3 712.3 710.0 H/s max 721.2 H/s                                                                                                            [609/1825]
Aug 27 21:15:59 r9-s1-01-01 xmrig[762]: new job from monero.napaster.name:14433 diff 120001 algo cn/r height 1910036
Aug 27 21:16:12 r9-s1-01-01 xmrig[762]: new job from monero.napaster.name:14433 diff 120001 algo cn/r height 1910037
Aug 27 21:16:27 r9-s1-01-01 xmrig[762]: new job from monero.napaster.name:14433 diff 120001 algo cn/r height 1910038
Aug 27 21:16:36 r9-s1-01-01 xmrig[762]: speed 10s/60s/15m 701.8 711.7 709.6 H/s max 721.2 H/s
Aug 27 21:17:36 r9-s1-01-01 xmrig[762]: speed 10s/60s/15m 700.0 699.9 708.5 H/s max 721.2 H/s
Aug 27 21:18:36 r9-s1-01-01 xmrig[762]: speed 10s/60s/15m 700.1 700.0 707.6 H/s max 721.2 H/s
Aug 27 21:19:36 r9-s1-01-01 xmrig[762]: speed 10s/60s/15m 699.7 699.9 707.7 H/s max 721.2 H/s
Aug 27 21:20:36 r9-s1-01-01 xmrig[762]: speed 10s/60s/15m 699.5 699.9 707.0 H/s max 721.2 H/s
Aug 27 21:21:36 r9-s1-01-01 xmrig[762]: speed 10s/60s/15m 699.8 699.8 707.7 H/s max 721.2 H/s                                                                 
Aug 27 21:22:36 r9-s1-01-01 xmrig[762]: speed 10s/60s/15m 699.8 700.0 707.1 H/s max 721.2 H/s
Aug 27 21:23:36 r9-s1-01-01 xmrig[762]: speed 10s/60s/15m 699.9 699.9 706.1 H/s max 721.2 H/s                                               
Aug 27 21:24:36 r9-s1-01-01 xmrig[762]: speed 10s/60s/15m 700.0 700.0 705.3 H/s max 721.2 H/s
Aug 27 21:25:36 r9-s1-01-01 xmrig[762]: speed 10s/60s/15m 699.9 699.9 704.7 H/s max 721.2 H/s
Aug 27 21:26:36 r9-s1-01-01 xmrig[762]: speed 10s/60s/15m 699.9 699.9 704.0 H/s max 721.2 H/s
Aug 27 21:27:36 r9-s1-01-01 xmrig[762]: speed 10s/60s/15m 699.9 699.9 703.2 H/s max 721.2 H/s
Aug 27 21:28:36 r9-s1-01-01 xmrig[762]: speed 10s/60s/15m 699.9 699.9 702.3 H/s max 721.2 H/s                                               
Aug 27 21:29:36 r9-s1-01-01 xmrig[762]: speed 10s/60s/15m 700.0 699.9 701.5 H/s max 721.2 H/s
Aug 27 21:30:36 r9-s1-01-01 xmrig[762]: speed 10s/60s/15m 699.9 699.9 700.7 H/s max 721.2 H/s
Aug 27 21:31:36 r9-s1-01-01 xmrig[762]: speed 10s/60s/15m 700.0 699.9 699.9 H/s max 721.2 H/s
Aug 27 21:32:36 r9-s1-01-01 xmrig[762]: speed 10s/60s/15m 700.0 699.9 699.9 H/s max 721.2 H/s
Aug 27 21:33:36 r9-s1-01-01 xmrig[762]: speed 10s/60s/15m 699.9 699.8 699.9 H/s max 721.2 H/s
Aug 27 21:33:58 r9-s1-01-01 xmrig[762]: no active pools, stop mining                                                                        
Aug 27 21:34:36 r9-s1-01-01 xmrig[762]: speed 10s/60s/15m n/a 699.9 699.9 H/s max 721.2 H/s                                                                   
Aug 27 21:35:36 r9-s1-01-01 xmrig[762]: speed 10s/60s/15m n/a n/a 699.9 H/s max 721.2 H/s                                                                     
Aug 27 21:36:36 r9-s1-01-01 xmrig[762]: speed 10s/60s/15m n/a n/a 699.9 H/s max 721.2 H/s                                                                                           
Aug 27 21:37:37 r9-s1-01-01 xmrig[762]: speed 10s/60s/15m n/a n/a 699.9 H/s max 721.2 H/s                                                                                           
Aug 27 21:38:37 r9-s1-01-01 xmrig[762]: speed 10s/60s/15m n/a n/a 699.9 H/s max 721.2 H/s                                                                                           
Aug 27 21:39:37 r9-s1-01-01 xmrig[762]: speed 10s/60s/15m n/a n/a 699.9 H/s max 721.2 H/s                                                                                           
Aug 27 21:40:37 r9-s1-01-01 xmrig[762]: speed 10s/60s/15m n/a n/a 699.9 H/s max 721.2 H/s                                                                                           
Aug 27 21:41:37 r9-s1-01-01 xmrig[762]: speed 10s/60s/15m n/a n/a 699.9 H/s max 721.2 H/s                                                                                                                          
Aug 27 21:42:37 r9-s1-01-01 xmrig[762]: speed 10s/60s/15m n/a n/a 699.9 H/s max 721.2 H/s                                                                                                                          
Aug 27 21:43:37 r9-s1-01-01 xmrig[762]: speed 10s/60s/15m n/a n/a 699.9 H/s max 721.2 H/s                                                                                                                          
Aug 27 21:44:37 r9-s1-01-01 xmrig[762]: speed 10s/60s/15m n/a n/a 699.9 H/s max 721.2 H/s                                                                                                                          
Aug 27 21:45:37 r9-s1-01-01 xmrig[762]: speed 10s/60s/15m n/a n/a 699.9 H/s max 721.2 H/s                                                                                                                          
Aug 27 21:46:37 r9-s1-01-01 xmrig[762]: speed 10s/60s/15m n/a n/a 699.9 H/s max 721.2 H/s                                                                                                                          
Aug 27 21:47:37 r9-s1-01-01 xmrig[762]: speed 10s/60s/15m n/a n/a 699.9 H/s max 721.2 H/s                                                                                                                          
Aug 27 21:48:37 r9-s1-01-01 xmrig[762]: speed 10s/60s/15m n/a n/a 699.9 H/s max 721.2 H/s                                                                                                                          
Aug 27 21:49:37 r9-s1-01-01 xmrig[762]: speed 10s/60s/15m n/a n/a n/a H/s max 721.2 H/s                                                                                                                            
Aug 27 21:50:37 r9-s1-01-01 xmrig[762]: speed 10s/60s/15m n/a n/a n/a H/s max 721.2 H/s                                                                                                                            
Aug 27 21:51:37 r9-s1-01-01 xmrig[762]: speed 10s/60s/15m n/a n/a n/a H/s max 721.2 H/s                                                                                                                            
Aug 27 21:52:37 r9-s1-01-01 xmrig[762]: speed 10s/60s/15m n/a n/a n/a H/s max 721.2 H/s                                                                                                                            
Aug 27 21:53:37 r9-s1-01-01 xmrig[762]: speed 10s/60s/15m n/a n/a n/a H/s max 721.2 H/s                                                                                                                            
Aug 27 21:54:37 r9-s1-01-01 xmrig[762]: speed 10s/60s/15m n/a n/a n/a H/s max 721.2 H/s                                                                                                                            
Aug 27 21:55:37 r9-s1-01-01 xmrig[762]: speed 10s/60s/15m n/a n/a n/a H/s max 721.2 H/s                                                                                                                            
Aug 27 21:56:37 r9-s1-01-01 xmrig[762]: speed 10s/60s/15m n/a n/a n/a H/s max 721.2 H/s                                                                                                                            
Aug 27 21:57:37 r9-s1-01-01 xmrig[762]: speed 10s/60s/15m n/a n/a n/a H/s max 721.2 H/s                                                                                                                            
Aug 27 21:58:37 r9-s1-01-01 xmrig[762]: speed 10s/60s/15m n/a n/a n/a H/s max 721.2 H/s                                                 
```

This time range matches with actual network maintenance, log from distribution switch:

```
<13> AUG 27 21:16:41 10.100.10.1-1 TRAPMGR[126170688]: traputil.c(636) 1923 %% Link Down: 0/15
<13> AUG 27 21:50:00 10.100.10.1-1 TRAPMGR[126170688]: traputil.c(636) 1953 %% Link Up: 0/15
```

So reason for this is network, miner should try to reconnect. xmrig 2.14.4 doesn't have this issue.

## xmrig | 2019-08-28T03:32:38+00:00
@k0ste Can you build miner with `-DWITH_DEBUG_LOG=ON`? with this option miner will print network state and traffic to log. I was try various ways to simulate networks issue, but't I can't reproduce the issue, also seems `keepalive` option disabled it helps detect network issues quickly and your pool support it. 
Thank you.

## k0ste | 2019-08-28T04:16:53+00:00
@xmrig, ok we try to reproduce this.
Also I catched that not only switch uplink is down, but also access port to miner node is flaps sometimes. And segfault of xmrig is a service restart.

```shell
[Tue Aug 27 21:16:40 2019] e1000e: eth0 NIC Link is Down
[Tue Aug 27 21:18:44 2019] e1000e: eth0 NIC Link is Up 100 Mbps Full Duplex, Flow Control: None
[Tue Aug 27 21:18:44 2019] e1000e 0000:09:00.0 eth0: 10/100 speed: disabling TSO
[Tue Aug 27 21:19:26 2019] e1000e: eth0 NIC Link is Down
[Tue Aug 27 21:19:28 2019] e1000e: eth0 NIC Link is Up 100 Mbps Full Duplex, Flow Control: None
[Tue Aug 27 21:19:28 2019] e1000e 0000:09:00.0 eth0: 10/100 speed: disabling TSO
[Tue Aug 27 21:19:35 2019] e1000e: eth0 NIC Link is Down
[Tue Aug 27 21:20:24 2019] e1000e: eth0 NIC Link is Up 100 Mbps Full Duplex, Flow Control: None
[Tue Aug 27 21:20:24 2019] e1000e 0000:09:00.0 eth0: 10/100 speed: disabling TSO
[Wed Aug 28 07:42:30 2019] xmrig[762]: segfault at 10 ip 00005602174ce22f sp 00007ffd88f64a20 error 4 in xmrig[56021741e000+30d000]
[Wed Aug 28 07:42:30 2019] Code: 89 ef 48 8d 35 72 00 00 00 5b 5d ff 25 ca 81 26 00 66 2e 0f 1f 84 00 00 00 00 00 55 53 48 89 fb 48 83 ec 08 ff 15 61 8b 26 00 <48> 8b 6b 10 48 85 ed 74 0d 48 89 ef ff 15 97 8a 26 00 85 c0 74 13
```

## napaster | 2019-08-29T06:04:41+00:00
@xmrig 
Starting with **-DWITH_DEBUG_LOG=ON**

> [root@xmrigtest ~]# xmrig -V
XMRig 3.1.0
 built on Aug 29 2019 with GCC 9.1.0
 features: 64-bit AES
libuv/1.31.0
OpenSSL/1.1.1c
hwloc/1


> [root@xmrigtest ~]# sysctl -w net.ipv4.tcp_retries2=5

> Aug 29 12:59:02 xmrigtest systemd[1]: Starting XMRig Daemon for cpu...
Aug 29 12:59:02 xmrigtest xmrig[6806]:  * ABOUT        XMRig/3.1.0 gcc/9.1.0
Aug 29 12:59:02 xmrigtest xmrig[6806]:  * LIBS         libuv/1.31.0 OpenSSL/1.1.1c hwloc/1.11.12
Aug 29 12:59:02 xmrigtest xmrig[6806]:  * CPU          Intel(R) Celeron(R) CPU G1610 @ 2.60GHz (1) x64 -AES
Aug 29 12:59:02 xmrigtest xmrig[6806]:                 L2:0.5 MB L3:2.0 MB 2C/2T NUMA:1
Aug 29 12:59:02 xmrigtest xmrig[6806]:  * DONATE       5%
Aug 29 12:59:02 xmrigtest xmrig[6806]:  * ASSEMBLY     auto:none
Aug 29 12:59:02 xmrigtest xmrig[6806]:  * POOL #1      monero.napaster.name:14433 algo cn/r
Aug 29 12:59:02 xmrigtest xmrig[6806]: POOLS --------------------------------------------------------------------
Aug 29 12:59:02 xmrigtest xmrig[6806]: url:       monero.napaster.name:14433
Aug 29 12:59:02 xmrigtest xmrig[6806]: host:      monero.napaster.name
Aug 29 12:59:02 xmrigtest xmrig[6806]: port:      14433
Aug 29 12:59:02 xmrigtest xmrig[6806]: user:      4ASpxpBpBJbfKCxnt8CRKt7pvfxcazi51D1tD28Beejkcf8To93cBYzg5nGVSzUn9eSuoNFEwp3uyUQRAxCv2D3PU83v55H.xmrig_test
Aug 29 12:59:02 xmrigtest xmrig[6806]: pass:      x
Aug 29 12:59:02 xmrigtest xmrig[6806]: rig-id     (null)
Aug 29 12:59:02 xmrigtest xmrig[6806]: algo:      cryptonight/r
Aug 29 12:59:02 xmrigtest xmrig[6806]: nicehash:  0
Aug 29 12:59:02 xmrigtest xmrig[6806]: keepAlive: 60
Aug 29 12:59:02 xmrigtest xmrig[6806]: --------------------------------------------------------------------------
Aug 29 12:59:02 xmrigtest xmrig[6806]:  * COMMANDS     hashrate, pause, resume
Aug 29 12:59:02 xmrigtest xmrig[6806]: [monero.napaster.name:14433] state: "host-lookup"
Aug 29 12:59:02 xmrigtest systemd[1]: Started XMRig Daemon for cpu.
Aug 29 12:59:02 xmrigtest xmrig[6806]: [monero.napaster.name:14433] state: "connecting"
Aug 29 12:59:02 xmrigtest xmrig[6806]: [monero.napaster.name:14433] state: "connected"
Aug 29 12:59:02 xmrigtest xmrig[6806]: [monero.napaster.name:14433] TLS send     (293 bytes)
Aug 29 12:59:03 xmrigtest xmrig[6806]: [monero.napaster.name:14433] TLS received (1610 bytes)
Aug 29 12:59:03 xmrigtest xmrig[6806]: [monero.napaster.name:14433] TLS send     (126 bytes)
Aug 29 12:59:03 xmrigtest xmrig[6806]: [monero.napaster.name:14433] TLS received (226 bytes)
Aug 29 12:59:03 xmrigtest xmrig[6806]: [monero.napaster.name:14433] send (501 bytes): "{"id":1,"jsonrpc":"2.0","method":"login","params":{"login":"4ASpxpBpBJbfKCxnt8CRKt7pvfxcazi51D1tD28Beejkcf8To93cBYzg5nGVSzUn9eSuoNFEwp3uyUQRAxCv2D3PU83v55H.xmrig_test","pass":"x","agent":"XMRig/3.1.0 (Linux x86_64) libuv/1.31.0 gcc/9.1.0","algo":["cn/r","cn/1","cn/2","cn/0","cn/wow","cn/fast","cn/half","cn/xao","cn/rto","cn/rwz","cn/zls","cn/double","cn/gpu","cn-lite/0","cn-lite/1","cn-heavy/0","cn-heavy/tube","cn-heavy/xhv","cn-pico","rx/test","rx/wow","rx/loki","argon2/chukwa","argon2/wrkz"]}}"
Aug 29 12:59:03 xmrigtest xmrig[6806]: [monero.napaster.name:14433] TLS send     (530 bytes)
Aug 29 12:59:03 xmrigtest xmrig[6806]: [monero.napaster.name:14433] TLS received (325 bytes)
Aug 29 12:59:03 xmrigtest xmrig[6806]: [monero.napaster.name:14433] received (296 bytes): "{"id":1,"jsonrpc":"2.0","result":{"id":"1","job":{"blob":"0b0ba1d39deb053c02d0d93ab054e0cafff0cf54a6aa653fac4f7d7b0165cd52a6ebdec2141566000000005f6a688a859cb6c7a313bc1e4795aef06287e2b1bf93afd04cd4d07e95ad61ac03","job_id":"11676","target":"cf8b0000","height":1911226},"status":"OK"},"error":null}"
Aug 29 12:59:03 xmrigtest xmrig[6806]: use pool monero.napaster.name:14433 TLSv1.2 5.196.26.96
Aug 29 12:59:03 xmrigtest xmrig[6806]: fingerprint (SHA-256): "c38886efdee542ebd99801b75c75d3498d97978bbcdec07c7271cb19729e014f"
Aug 29 12:59:03 xmrigtest xmrig[6806]: new job from monero.napaster.name:14433 diff 120001 algo cn/r height 1911226
Aug 29 12:59:03 xmrigtest xmrig[6806]:  cpu  use profile  *  (2 threads) scratchpad 2048 KB
Aug 29 12:59:05 xmrigtest xmrig[6806]:  cpu  READY threads 2(2) huge pages 2/2 100% memory 4096 KB (2569 ms)
Aug 29 12:59:57 xmrigtest xmrig[6806]: [monero.napaster.name:14433] TLS received (289 bytes)
Aug 29 12:59:57 xmrigtest xmrig[6806]: [monero.napaster.name:14433] received (260 bytes): "{"jsonrpc":"2.0","method":"job","params":{"blob":"0b0bddd39deb053c02d0d93ab054e0cafff0cf54a6aa653fac4f7d7b0165cd52a6ebdec214156600000000be0c55ae577c49b24013d804798a2ef95e4a08e2b18c0370d7484d24e38d359408","job_id":"11677","target":"cf8b0000","height":1911226}}"
Aug 29 12:59:57 xmrigtest xmrig[6806]: new job from monero.napaster.name:14433 diff 120001 algo cn/r height 1911226
Aug 29 13:00:03 xmrigtest xmrig[6806]: speed 10s/60s/15m 28.7 n/a n/a H/s max 28.7 H/s
Aug 29 13:00:58 xmrigtest xmrig[6806]: [monero.napaster.name:14433] send (67 bytes): "{"id":2,"jsonrpc":"2.0","method":"keepalived","params":{"id":"1"}}"
Aug 29 13:00:58 xmrigtest xmrig[6806]: [monero.napaster.name:14433] TLS send     (96 bytes)
Aug 29 13:00:59 xmrigtest xmrig[6806]: [monero.napaster.name:14433] send (67 bytes): "{"id":3,"jsonrpc":"2.0","method":"keepalived","params":{"id":"1"}}"
Aug 29 13:00:59 xmrigtest xmrig[6806]: [monero.napaster.name:14433] TLS send     (96 bytes)
Aug 29 13:01:00 xmrigtest xmrig[6806]: [monero.napaster.name:14433] send (67 bytes): "{"id":4,"jsonrpc":"2.0","method":"keepalived","params":{"id":"1"}}"
Aug 29 13:01:00 xmrigtest xmrig[6806]: [monero.napaster.name:14433] TLS send     (96 bytes)
Aug 29 13:01:01 xmrigtest xmrig[6806]: [monero.napaster.name:14433] send (67 bytes): "{"id":5,"jsonrpc":"2.0","method":"keepalived","params":{"id":"1"}}"
Aug 29 13:01:01 xmrigtest xmrig[6806]: [monero.napaster.name:14433] TLS send     (96 bytes)
Aug 29 13:01:02 xmrigtest xmrig[6806]: [monero.napaster.name:14433] send (67 bytes): "{"id":6,"jsonrpc":"2.0","method":"keepalived","params":{"id":"1"}}"
Aug 29 13:01:02 xmrigtest xmrig[6806]: [monero.napaster.name:14433] TLS send     (96 bytes)
Aug 29 13:01:03 xmrigtest xmrig[6806]: speed 10s/60s/15m 28.6 28.7 n/a H/s max 28.7 H/s
Aug 29 13:01:03 xmrigtest xmrig[6806]: [monero.napaster.name:14433] send (67 bytes): "{"id":7,"jsonrpc":"2.0","method":"keepalived","params":{"id":"1"}}"
Aug 29 13:01:03 xmrigtest xmrig[6806]: [monero.napaster.name:14433] TLS send     (96 bytes)
Aug 29 13:01:04 xmrigtest xmrig[6806]: [monero.napaster.name:14433] send (67 bytes): "{"id":8,"jsonrpc":"2.0","method":"keepalived","params":{"id":"1"}}"
Aug 29 13:01:04 xmrigtest xmrig[6806]: [monero.napaster.name:14433] TLS send     (96 bytes)
Aug 29 13:01:05 xmrigtest xmrig[6806]: [monero.napaster.name:14433] send (67 bytes): "{"id":9,"jsonrpc":"2.0","method":"keepalived","params":{"id":"1"}}"
Aug 29 13:01:05 xmrigtest xmrig[6806]: [monero.napaster.name:14433] TLS send     (96 bytes)
Aug 29 13:01:06 xmrigtest xmrig[6806]: [monero.napaster.name:14433] send (68 bytes): "{"id":10,"jsonrpc":"2.0","method":"keepalived","params":{"id":"1"}}"
Aug 29 13:01:06 xmrigtest xmrig[6806]: [monero.napaster.name:14433] TLS send     (97 bytes)
Aug 29 13:01:07 xmrigtest xmrig[6806]: [monero.napaster.name:14433] send (68 bytes): "{"id":11,"jsonrpc":"2.0","method":"keepalived","params":{"id":"1"}}"
Aug 29 13:01:07 xmrigtest xmrig[6806]: [monero.napaster.name:14433] TLS send     (97 bytes)
Aug 29 13:01:08 xmrigtest xmrig[6806]: [monero.napaster.name:14433] read error: "connection timed out"
Aug 29 13:01:08 xmrigtest xmrig[6806]: [monero.napaster.name:14433] state: "closing"
Aug 29 13:01:08 xmrigtest xmrig[6806]: [monero.napaster.name:14433] state: "unconnected"
Aug 29 13:01:08 xmrigtest xmrig[6806]: [monero.napaster.name:14433] state: "connecting"
Aug 29 13:01:08 xmrigtest xmrig[6806]: no active pools, stop mining
Aug 29 13:01:13 xmrigtest xmrig[6806]: [monero.napaster.name:14433] state: "host-lookup"
Aug 29 13:01:13 xmrigtest xmrig[6806]: [monero.napaster.name:14433] state: "connecting"
Aug 29 13:02:03 xmrigtest xmrig[6806]: speed 10s/60s/15m n/a 28.5 n/a H/s max 28.7 H/s
Aug 29 13:03:03 xmrigtest xmrig[6806]: speed 10s/60s/15m n/a n/a n/a H/s max 28.7 H/s

## k0ste | 2019-08-29T06:09:19+00:00
@xmrig, we reproduce this. In default linux environment tcp connection dies after ~15min. To speed-up this bug you can lower `net.ipv4.tcp_retries2` (default is 15).

![2018-04-27-linux-tcp-rto-retries2-b71ad2ef586126c2ad4180543f78d8b0a4bf66925fb88d69889f04c4b7aedeaa](https://user-images.githubusercontent.com/7759548/63914698-323b6280-ca5e-11e9-8cd2-17abe59843cd.png)


```
[Thu Aug 29 13:00:47 2019] r8169 0000:03:00.0 eth0: Link is Down
[Thu Aug 29 13:03:06 2019] r8169 0000:03:00.0 eth0: Link is Up - 1Gbps/Full - flow control off
```


## xmrig | 2019-08-29T11:42:21+00:00
@k0ste Thank you, I will check it tomorrow.

## xmrig | 2019-08-30T02:06:55+00:00
I found multiple bugs:
1. keepalve was don't work as expected, it should close connection without need to change system wide settings eg `net.ipv4.tcp_retries2` fixed https://github.com/xmrig/xmrig/commit/df91a8512880592594f289a11d675aacf6fb26f5.
2. I mistaken and xmr.nanopool.org (monero.napaster.name) don't support keepalive in bad way (don't respond at all) it can cause timeouts in normal workflow, but default timeout values and job rate hide this issue.
3. Miner defined connect timeout was not applied in all cases.
4. libuv don't call `onConnect` callback after use `uv_tcp_connect` if no network available, it seems libuv related issue, but with `3.` it make miner stuck forever.

And main case why 2.14 works fine is new DNS cache, previous version got error after `host-lookup` and after that use forced reconnect, bug `3.` not happen.

Now work on final bugfix, needs check anything carefully.
Thank you.

## xmrig | 2019-08-30T03:05:11+00:00
This issue should be fixed in dev branch please confirm.
Thank you.

## k0ste | 2019-08-30T12:56:42+00:00
@xmrig, thanks.
I'm going on vacation, @napaster should test and feedback results of this patches.

## Bendr0id | 2019-08-30T14:17:27+00:00
Works! 
Tested: 
- Invalid DNS
- unplugging the cable 
- disconnecting the network adapter from the VM
- blocking ports

Tested on WIN10 and Debian bullseye

For me it always recovers.


## sukerl | 2019-08-30T20:58:55+00:00
@xmrig , I also can see this behavior in xmrig-amd version 2.14.5 on Ubuntu. Could you please apply the fix there as well?

Thanks

## xmrig | 2019-08-31T03:04:47+00:00
https://github.com/xmrig/xmrig/releases/tag/v3.1.1
https://github.com/xmrig/xmrig-proxy/releases/tag/v3.1.1
https://github.com/xmrig/xmrig-amd/releases/tag/v2.14.6
https://github.com/xmrig/xmrig-nvidia/releases/tag/v2.14.5

## sunbearc22 | 2022-02-03T05:31:26+00:00
I noticed several  `net      no active pools, stop mining` msgs in XMrig-6.16.3 linux Ubuntu 20.04 version too. Several such occurrences consistently happen per day.  All the jobs just stop and then new batches of jobs are started up. CPU cores load drops to 0 and then ramp back up again. 


## GradinIT | 2022-10-26T14:30:07+00:00
bug still pressent in version 6.18.1 of xmrig , running on mac m1 

# Action History
- Created by: rhlug | 2019-08-24T00:58:51+00:00
- Closed at: 2019-08-31T03:04:47+00:00
