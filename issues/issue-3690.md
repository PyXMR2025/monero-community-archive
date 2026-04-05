---
title: xmrig only consuming 4% cpu
source_url: https://github.com/xmrig/xmrig/issues/3690
author: nova2moon
assignees: []
labels: []
created_at: '2025-08-02T10:47:42+00:00'
updated_at: '2025-08-19T17:41:56+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Running latest xmrig on Linux Mint, daemon running on another linux server on LAN 192.168.1.2 port 18081.

had to run as ROOT otherwise it fails to get MSR, this output is when running as root, but still gets very low mining , about 3-4% cpu despite letting it run for long time..  machine specs in output below:

![Image](https://github.com/user-attachments/assets/4b949304-5600-4497-8b5f-35e0267f7945)

` * ABOUT        XMRig/6.24.0 gcc/13.2.1 (built for Linux x86-64, 64 bit)
 * LIBS         libuv/1.51.0 OpenSSL/3.0.16 hwloc/2.12.1
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          12th Gen Intel(R) Core(TM) i5-1240P (1) 64-bit AES
                L2:9.0 MB L3:12.0 MB 12C/16T NUMA:1
 * MEMORY       4.8/62.5 GB (8%)
                Controller0-ChannelA-DIMM0: 32 GB DDR4 @ 3200 MHz                     
                Controller1-ChannelA-DIMM0: 32 GB DDR4 @ 3200 MHz                     
 * MOTHERBOARD  JHZD - BQM5
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      192.168.1.2:18081 coin Monero
 * COMMANDS     hashrate, pause, resume, results, connection
[2025-08-02 13:01:39.564]  net      use daemon 192.168.1.2:18081 TLSv1.3 192.168.1.2
[2025-08-02 13:01:39.565]  net      fingerprint (SHA-256): "a7847a968925dd1ab7d7b57f7e0b25d4df43decdff31d288da49cb631678d71f"
[2025-08-02 13:01:39.565]  net      new job from 192.168.1.2:18081 diff 637G algo rx/0 height 3468973 (110 tx)
[2025-08-02 13:01:39.565]  cpu      use argon2 implementation AVX2
[2025-08-02 13:01:39.565]  msr      0x000001a4:0x000000000000000f -> 0x000000000000000f
[2025-08-02 13:01:39.566]  msr      register values for "intel" preset have been set successfully (1 ms)
[2025-08-02 13:01:39.566]  randomx  init dataset algo rx/0 (16 threads) seed 1ef55c414084773a...
[2025-08-02 13:01:39.882]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (316 ms)
[2025-08-02 13:01:42.120]  randomx  dataset ready (2238 ms)
[2025-08-02 13:01:42.120]  cpu      use profile  rx  (10 threads) scratchpad 2048 KB
[2025-08-02 13:01:42.127]  cpu      READY threads 10/10 (10) huge pages 100% 10/10 memory 20480 KB (7 ms)
[2025-08-02 13:01:54.606]  net      new job from 192.168.1.2:18081 diff 637G algo rx/0 height 3468973 (112 tx)
[2025-08-02 13:02:03.569]  net      no active pools, stop mining
[2025-08-02 13:02:42.181]  miner    speed 10s/60s/15m 0.00 n/a n/a H/s max 3893.6 H/s
[2025-08-02 13:03:42.245]  miner    speed 10s/60s/15m 0.00 0.00 n/a H/s max 3893.6 H/s
[2025-08-02 13:04:42.312]  miner    speed 10s/60s/15m 0.00 0.00 n/a H/s max 3893.6 H/s
[2025-08-02 13:05:42.379]  miner    speed 10s/60s/15m 0.00 0.00 n/a H/s max 3893.6 H/s
[2025-08-02 13:06:42.447]  miner    speed 10s/60s/15m 0.00 0.00 n/a H/s max 3893.6 H/s
[2025-08-02 13:07:42.519]  miner    speed 10s/60s/15m 0.00 0.00 n/a H/s max 3893.6 H/s
[2025-08-02 13:08:42.593]  miner    speed 10s/60s/15m 0.00 0.00 n/a H/s max 3893.6 H/s
[2025-08-02 13:09:42.664]  miner    speed 10s/60s/15m 0.00 0.00 n/a H/s max 3893.6 H/s
[2025-08-02 13:10:42.740]  miner    speed 10s/60s/15m 0.00 0.00 n/a H/s max 3893.6 H/s
[2025-08-02 13:11:42.815]  miner    speed 10s/60s/15m 0.00 0.00 n/a H/s max 3893.6 H/s
[2025-08-02 13:12:42.876]  miner    speed 10s/60s/15m 0.00 0.00 n/a H/s max 3893.6 H/s
[2025-08-02 13:13:42.914]  miner    speed 10s/60s/15m 0.00 0.00 n/a H/s max 3893.6 H/s
[2025-08-02 13:14:42.956]  miner    speed 10s/60s/15m 0.00 0.00 n/a H/s max 3893.6 H/s
`
any tips/ideas to run with more debug ?

As for "no active pools", for now trying to do solo mining, just to try out:, this is pools section from xmrig json file:

`    "pools": [{
            "algo": null,
            "coin": "XMR",
            "url": "192.168.1.2:18081",
            "user": "45qrd<snipxHWWgLMfYXWHzwx9LhoeM",
            "enabled": true,
            "tls": true,
            "sni": false,
            "tls-fingerprint": null,
            "daemon": true,
            "socks5": null,
            "daemon-poll-interval": 1000,
            "daemon-job-timeout": 15000,
            "daemon-zmq-port": -1
        }],
`


# Discussion History
## geekwilliams | 2025-08-02T16:12:35+00:00
What are you using to run the node? 

Getting one successful job, and then the no-active-pools message to me would indicate a problem with the local node

## nova2moon | 2025-08-02T18:34:00+00:00
local node running fine on separate linux machine on LAN:

` 4507 root      261g S    monerod --rpc-bind-ip=192.168.1.2 --confirm-external-bin --enable-dns-blocklist --disable-dns-checkpoints
`
fully synced, both can ssh/ping one another
```
# du -sh lmdb/
233.2G  lmdb/
```

No errors in log, question how to debug, xmrig should soak more cpus, I'm not trying to mine to pool, just solo..

running wallet cli noticed eeach time must set daemon:
```
[wallet 45qrdV (no daemon)]: set_daemon https://192.168.1.2:18081 trusted
Daemon set to https://192.168.1.2:18081, trusted
[wallet 45qrdV]: status
Refreshed 3469244/3469244, synced, daemon RPC v3.14, SSL
```
could it be something with setup, memory/cpu/privs?  tried sudo and directly as root, same results.

## nova2moon | 2025-08-02T19:02:45+00:00
Binaries from official website:
`a6a710135483296b9a943dc3ed31d6a1396b5cfeb127ab0d7e5c6bf49785130a  config.json
0c748b9e8bc6b5b4fe989df67655f3301d28ef81617b9cbe8e0f6a19d4f9b657  xmrig
-rwxr-xr-x 1 moon moon 8334576 Jun 23 03:46 xmrig
sha256sum -c SHA256SUMS 
config.json: OK
xmrig: OK

`

## nova2moon | 2025-08-03T05:37:23+00:00
The node running monerod has bitmonero.log with very clean output, tail shows only blocked nodes without any errors:

`2025-08-02 22:09:05.425 [P2P9]  INFO    global  src/p2p/net_node.inl:327        Host 185.220.100.249 blocked.
2025-08-03 00:37:03.832 [P2P4]  INFO    global  src/p2p/net_node.inl:327        Host 45.84.107.76 blocked.`

decided to rule out the Linux/xmrig and downloaded on Win10 on Lenovo laptop, got another error:

```
 * ABOUT        XMRig/6.24.0 MSVC/2022 (built for Windows x86-64, 64 bit)
 * LIBS         libuv/1.51.0 OpenSSL/3.0.16 hwloc/2.12.1
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (1) 64-bit AES VM
                L2:1.0 MB L3:6.0 MB 4C/8T NUMA:1
 * MEMORY       15.6/31.6 GB (49%)
                DIMM_A0: 16 GB DDR4 @ 2400 MHz HMA82GS6AFR8N-UH
                DIMM_B0: 16 GB DDR4 @ 2400 MHz M4S16S682QMMM52-12
 * MOTHERBOARD  LENOVO - 20LTS3C716
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      192.168.1.2:18081 coin Monero
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2025-08-03 01:22:02.141]  net      192.168.1.2:18081 write error: "software caused connection abort"
[2025-08-03 01:22:08.139]  net      192.168.1.2:18081 write error: "software caused connection abort"
[2025-08-03 01:22:13.182]  net      192.168.1.2:18081 write error: "software caused connection abort"
[2025-08-03 01:22:18.231]  net      192.168.1.2:18081 write error: "software caused connection abort"
[2025-08-03 01:22:23.281]  net      192.168.1.2:18081 write error: "software caused connection abort"

```

here win/defender firewall is in DISABLED state , all machines are on same LAN connected with 8port switch.  is there any --debug flag to get more info ?

## SChernykh | 2025-08-03T07:34:14+00:00
Can you try to run both XMRig and Monero node on the same machine, and connect to 127.0.0.1:18081? This will exclude all the networking steps that happen between the two programs. The problem must be somewhere in-between.

## zacharydrew | 2025-08-18T03:49:31+00:00
I believe I am experiencing the same problem. I have an ubuntu host running monerod + xmrig plus a Windows 11 host running xmrig with **solo mining**. The problem occurs when I upgrade monero release binaries.

monero-x86_64-linux-gnu-**v0.18.3.2** to monero-x86_64-linux-gnu-**v0.18.4.1**

The problem disappears again when I revert to the earlier version.

Both my XMRigs, local and remote, stop mining with these messages and zero hashrate:

```
[2025-08-17 19:18:19.700]  net      new job from 127.0.0.1:18081 diff 644G algo rx/0 height 3480222 (3 tx)
[2025-08-17 19:18:38.692]  net      no active pools, stop mining
```
I upgraded XMRig on ubuntu to latest git branch with no improvement. Restarts don't help.

Monerod command line option:

`monero-x86_64-linux-gnu-v0.18.3.2/monerod --confirm-external-bind --restricted-rpc --rpc-bind-ip 0.0.0.0 --enable-dns-blocklist`

I suspect the problem has something to do with solo mining as I believe most people use pools.

I can attempt to isolate which intermediate version introduced the problem later this week.

@nova2moon try an earlier release to see if it fixes your problem, such as v0.18.3.2 like I am using.


## SChernykh | 2025-08-18T07:33:12+00:00
@zacharydrew I can't reproduce it with my local node and latest XMRig. What's your XMRig command line (or config.json)?

## zacharydrew | 2025-08-18T15:58:42+00:00
@SChernykh 

```
{
    "api": {
        "id": null,
        "worker-id": null
    },
    "http": {
        "enabled": false,
        "host": "127.0.0.1",
        "port": 0,
        "access-token": null,
        "restricted": true
    },
    "autosave": true,
    "background": false,
    "colors": true,
    "title": true,
    "randomx": {
        "init": -1,
        "init-avx2": -1,
        "mode": "auto",
        "1gb-pages": true,
        "rdmsr": true,
        "wrmsr": true,
        "cache_qos": false,
        "numa": true,
        "scratchpad_prefetch_mode": 1
    },
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "huge-pages-jit": false,
        "hw-aes": null,
        "priority": null,
        "memory-pool": false,
        "yield": true,
        "asm": true,
        "argon2-impl": null,
        "argon2": [0, 16, 1, 17, 2, 18, 3, 19, 4, 20, 5, 21, 6, 22, 7, 23, 8, 24, 9, 25, 10, 26, 11, 27, 12, 28, 13, 29, 14, 30, 15, 31],
        "astrobwt": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
        "cn": [
            [1, 0],
            [1, 16],
            [1, 1],
            [1, 17],
            [1, 2],
            [1, 18],
            [1, 3],
            [1, 19],
            [1, 4],
            [1, 20],
            [1, 5],
            [1, 21],
            [1, 6],
            [1, 22],
            [1, 7],
            [1, 23],
            [1, 8],
            [1, 24],
            [1, 9],
            [1, 25],
            [1, 10],
            [1, 26],
            [1, 11],
            [1, 27],
            [1, 12],
            [1, 28],
            [1, 13],
            [1, 29],
            [1, 14],
            [1, 30],
            [1, 15],
            [1, 31]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 4],
            [1, 5],
            [1, 6],
            [1, 7],
            [1, 8],
            [1, 9],
            [1, 10],
            [1, 11],
            [1, 12],
            [1, 13],
            [1, 14],
            [1, 15]
        ],
        "cn-lite": [
            [1, 0],
            [1, 16],
            [1, 1],
            [1, 17],
            [1, 2],
            [1, 18],
            [1, 3],
            [1, 19],
            [1, 4],
            [1, 20],
            [1, 5],
            [1, 21],
            [1, 6],
            [1, 22],
            [1, 7],
            [1, 23],
            [1, 8],
            [1, 24],
            [1, 9],
            [1, 25],
            [1, 10],
            [1, 26],
            [1, 11],
            [1, 27],
            [1, 12],
            [1, 28],
            [1, 13],
            [1, 29],
            [1, 14],
            [1, 30],
            [1, 15],
            [1, 31]
        ],
        "cn-pico": [
            [2, 0],
            [2, 16],
            [2, 1],
            [2, 17],
            [2, 2],
            [2, 18],
            [2, 3],
            [2, 19],
            [2, 4],
            [2, 20],
            [2, 5],
            [2, 21],
            [2, 6],
            [2, 22],
            [2, 7],
            [2, 23],
            [2, 8],
            [2, 24],
            [2, 9],
            [2, 25],
            [2, 10],
            [2, 26],
            [2, 11],
            [2, 27],
            [2, 12],
            [2, 28],
            [2, 13],
            [2, 29],
            [2, 14],
            [2, 30],
            [2, 15],
            [2, 31]
        ],
        "cn/gpu": [0, 16, 1, 17, 2, 18, 3, 19, 4, 20, 5, 21, 6, 22, 7, 23, 8, 24, 9, 25, 10, 26, 11, 27, 12, 28, 13, 29, 14, 30, 15, 31],
        "cn/upx2": [
            [2, 0],
            [2, 12],
            [2, 1],
            [2, 13],
            [2, 2],
            [2, 14],
            [2, 3],
            [2, 15],
            [2, 4],
            [2, 16],
            [2, 5],
            [2, 17],
            [2, 6],
            [2, 18],
            [2, 7],
            [2, 19],
            [2, 8],
            [2, 20],
            [2, 9],
            [2, 21],
            [2, 10],
            [2, 22],
            [2, 11],
            [2, 23]
        ],
        "ghostrider": [
            [8, 0],
            [8, 1],
            [8, 2],
            [8, 3],
            [8, 4],
            [8, 5],
            [8, 6],
            [8, 7],
            [8, 8],
            [8, 9],
            [8, 10],
            [8, 11]
        ],
        "rx": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 4],
            [1, 5],
            [1, 6],
            [1, 7],
            [1, 8],
            [1, 9],
            [1, 10],
            [1, 11],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1]
        ],
        "rx/wow": [0, 16, 1, 17, 2, 18, 3, 19, 4, 20, 5, 21, 6, 22, 7, 23, 8, 24, 9, 25, 10, 26, 11, 27, 12, 28, 13, 29, 14, 30, 15, 31],
        "cn-lite/0": false,
        "cn/0": false,
        "rx/arq": "rx/wow",
        "rx/keva": "rx/wow"
    },
    "opencl": {
        "enabled": false,
        "cache": true,
        "loader": null,
        "platform": "AMD",
        "adl": true
    },
    "cuda": {
        "enabled": false,
        "loader": null,
        "nvml": true
    },
    "log-file": "xmrlog",
    "donate-level": 0,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": null,
            "coin": "XMR",
            "url": "127.0.0.1:18081",
            "user": "<REDACTED>",
            "enabled": true,
            "tls": true,
            "tls-fingerprint": null,
            "daemon": true,
            "socks5": null,
            "daemon-poll-interval": 1000,
            "daemon-zmq-port": -1
        }
    ],
    "retries": 5,
    "retry-pause": 5,
    "print-time": 60,
    "health-print-time": 60,
    "dmi": true,
    "syslog": false,
    "tls": {
        "enabled": false,
        "protocols": null,
        "cert": null,
        "cert_key": null,
        "ciphers": null,
        "ciphersuites": null,
        "dhparam": null
    },
    "dns": {
        "ipv6": false,
        "ttl": 30
    },
    "user-agent": null,
    "verbose": 0,
    "watch": true,
    "pause-on-battery": false,
    "pause-on-active": false
}
```

## zacharydrew | 2025-08-18T16:12:04+00:00
@SChernykh 

The problem seems to have been introduced with release **v0.18.4.0**. Solo mining works fine with release **v0.18.3.4**.

## nova2moon | 2025-08-18T16:46:19+00:00
> I believe I am experiencing the same problem. I have an ubuntu host running monerod + xmrig plus a Windows 11 host running xmrig with **solo mining**. The problem occurs when I upgrade monero release binaries.
> 
> monero-x86_64-linux-gnu-**v0.18.3.2** to monero-x86_64-linux-gnu-**v0.18.4.1**
> 

WOW, truly, WOW, the power of sharing, thanks so much - decided, what the... lets try this.. pulled the 18.3.2 monerod binary, the xmrig was running all along, all did was send an EXIT to current version, and ran the new one, here is log showing it instantly started mining!!

```
[2025-08-18 09:37:54.964]  miner    speed 10s/60s/15m 0.00 0.00 n/a H/s max 3834.7 H/s
[2025-08-18 09:38:55.033]  miner    speed 10s/60s/15m 0.00 0.00 n/a H/s max 3834.7 H/s
[2025-08-18 09:39:55.106]  miner    speed 10s/60s/15m 0.00 0.00 n/a H/s max 3834.7 H/s
[2025-08-18 09:40:55.187]  miner    speed 10s/60s/15m 0.00 0.00 n/a H/s max 3834.7 H/s
[2025-08-18 09:41:36.429]  net      use daemon 192.168.1.2:18089 TLSv1.3 192.168.1.2
[2025-08-18 09:41:36.429]  net      fingerprint (SHA-256): "xxxf89c53cfdcxxx875d73f48cee2"
[2025-08-18 09:41:36.429]  net      new job from 192.168.1.2:18089 diff 650G algo rx/0 height 3480673 (35 tx)
[2025-08-18 09:41:51.483]  net      new job from 192.168.1.2:18089 diff 650G algo rx/0 height 3480673 (40 tx)
[2025-08-18 09:41:55.257]  miner    speed 10s/60s/15m 3793.7 1210.5 n/a H/s max 3868.8 H/s
[2025-08-18 09:42:07.481]  net      new job from 192.168.1.2:18089 diff 650G algo rx/0 height 3480673 (44 tx)
[2025-08-18 09:42:23.483]  net      new job from 192.168.1.2:18089 diff 650G algo rx/0 height 3480673 (46 tx)
[2025-08-18 09:42:39.488]  net      new job from 192.168.1.2:18089 diff 650G algo rx/0 height 3480673 (53 tx)
```
(I've since moved to port 18089)  thanks for this workaround!!

## SChernykh | 2025-08-18T18:03:04+00:00
Monero v0.18.4.0 was a big release, a lot has changed there. I need to look into why it's broken now.

## zacharydrew | 2025-08-19T03:23:43+00:00
I've narrowed down to the commit I believe to be responsible:

[13ff355cf](https://github.com/monero-project/monero/pull/9775/commits/13ff355cf6081776fd7379080c17246e35c1236d) Set response limits on http server connections

Commit 70afa6b7b - works
Commit 13ff355cf   - fails

[Pull #9775](https://github.com/monero-project/monero/pull/9775) by @vtnerd 

Here is the [problem description](https://github.com/xmrig/xmrig/issues/3690#issuecomment-3195011876).

I hope this helps!



## vtnerd | 2025-08-19T03:46:59+00:00
This is so bad, assuming your details are true. The quick work-around is to use ZMQ-PORT, this is probably why @SChernykh couldn't reproduce. My box solo mines with ZMQ-PORT anyway, with 100% CPU.

And the referenced PR was to fix another serious issue, but looks like I botched the fix. How embarrassing. Anyway get the word out about ZMQ fix (after you confirm this works), so that people are actually mining properly.

## vtnerd | 2025-08-19T03:47:48+00:00
Also, ZMQ-PORT should be more efficient any quicker to update than the traditional API. So its not all bad to bump to it.

## vtnerd | 2025-08-19T03:50:10+00:00
Nevermind, I couldn't reproduce by switching directly to HTTP. Foot in mouth again. Try the ZMQ-PORT anyway, as that doesn't use the HTTP server.

There might be something deeper than just solo mining + http server.

## zacharydrew | 2025-08-19T15:10:52+00:00
Yeah I do not think this is affecting a huge number of people. It's probably something to do with my XMRig config.json being very old. I also assume a lot of miners maybe aren't keeping their software up to date. I touch my setup very infrequently and was trying to migrate to p2pool so my hashrate would be more visible.

Still it would be nice not to break older mining setups given how critical hashrate is at the moment. I was able to easily isolate the problem but many others won't be. For example OP on this issue seems to have been setting up mining for the first time and still landed on this problem, probably from very stale how to's that remain persistent on the web. I still run into people trying to setup GPU mining so it's clearly hard for newer information to replace the old stuff still floating around.

I will keep chipping away at it as time allows.

## SChernykh | 2025-08-19T15:41:12+00:00
I reproduced it with the release v0.18.4.2 monero node and the latest XMRig-dev branch.

## vtnerd | 2025-08-19T17:30:10+00:00
@SChernykh I'm assuming you're looking at the `monerod` side unless you tell me otherwise. Sounds like I would need to use the config verbatim to reproduce for my own testing.

## SChernykh | 2025-08-19T17:37:16+00:00
No, I looked at XMRig side, and I can only confirm that XMRig keeps trying to connect, but connection gets closed from monerod side. I'm not familiar with that monerod code.

## nova2moon | 2025-08-19T17:41:56+00:00
Friends, correct, it is brand new setup, first time doing it, if there's any mistake or thing to change in the setup on node side or xmrig/client, do let me know, for now, running the OLDER node back end, makes the newer xmrig work fine.
also, running via gupax gui front end allows the NEW monerod to also work just fine, probably b/c it adds the p2pool... so, 2 workarounds :) 

# Action History
- Created by: nova2moon | 2025-08-02T10:47:42+00:00
