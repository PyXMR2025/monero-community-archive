---
title: Daemon sync via GUI; blocks per second sync a lot lower than usual
source_url: https://github.com/monero-project/monero/issues/9417
author: kdf8jsa1
assignees: []
labels:
- question
created_at: '2024-08-01T13:09:04+00:00'
updated_at: '2024-08-02T20:57:18+00:00'
type: issue
status: closed
closed_at: '2024-08-02T20:57:18+00:00'
---

# Original Description
Daemon sync via GUI is a lot slower than usual. Estimated time is 2.6 days for ~50,000 blocks

Last sync took 1.6 hours for 3539 blocks based on log:

```
2024-03-24 15:14:04.438 [P2P2]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:2493
Synced 3539 blocks in 1.6 hours (0.614 blocks per second)
```

I don't know if syncing should be around 0.614 blocks per second, like last time. At this rate, I would expect estimated time to be ~8 hours. Right now estimated time is 2.6 days.

Last sync was in March 2024:

```
$ less .bitmonero/bitmonero.log | grep synchronized | tail -1
2024-03-24 15:14:04.438	[P2P2]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2500	You are now synchronized with the network. You may now start monero-wallet-cli.
```

I am wondering if there is something wrong, or whether I am doing something wrong.

Here is some information I saw was asked in other threads (e.g. https://github.com/monero-project/monero/issues/8500)

```
$ tail .bitmonero/bitmonero.log 
2024-08-01 12:34:07.186	[P2P3]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1697	Synced 3154441/3205577 (98%, 51136 left)
2024-08-01 12:35:24.843	[P2P3]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1697	Synced 3154461/3205578 (98%, 51117 left, 31% of total synced, estimated 2.6 days left)
2024-08-01 12:37:07.615	[P2P3]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1697	Synced 3154481/3205580 (98%, 51099 left)
2024-08-01 12:38:17.931	[P2P3]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1697	Synced 3154501/3205580 (98%, 51079 left, 31% of total synced, estimated 2.6 days left)
2024-08-01 12:39:43.754	[P2P3]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1697	Synced 3154521/3205582 (98%, 51061 left)
2024-08-01 12:41:01.276	[P2P3]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1697	Synced 3154541/3205584 (98%, 51043 left, 31% of total synced, estimated 2.6 days left)
2024-08-01 12:42:05.974	[P2P3]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1697	Synced 3154561/3205584 (98%, 51023 left)
2024-08-01 12:43:03.399	[P2P3]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1697	Synced 3154581/3205584 (98%, 51003 left, 32% of total synced, estimated 2.6 days left)
2024-08-01 12:43:54.699	[P2P3]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1697	Synced 3154601/3205584 (98%, 50983 left)
2024-08-01 12:45:23.365	[P2P3]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1697	Synced 3154621/3205584 (98%, 50963 left, 32% of total synced, estimated 2.6 days left)
```


```
>>> status
[01/08/2024 14:09] 2024-08-01 12:08:42.815 I Monero 'Fluorine Fermi' (v0.18.3.3-release)
Height: 3154081/3205564 (98.4%) on mainnet, not mining, net hash 2.35 GH/s, v16, 13(out)+0(in) connections, uptime 1d 4h 53m 13s
```

```
>>> sync_info
[01/08/2024 14:23] 2024-08-01 12:22:57.698 I Monero 'Fluorine Fermi' (v0.18.3.3-release)
Height: 3154281, target: 3205572 (98.3999%)
Downloading at 298 kB/s
Next needed pruning seed: 4
13 peers
Remote Host Peer_ID State Prune_Seed Height DL kB/s, Queued Blocks / MB
135.181.249.92:18080 98a129913601f041 standby 0 3205572 2 kB/s, 240 blocks / 36.7134 MB queued
37.27.70.253:18080 c3adff8b106dc628 standby 0 3205572 2 kB/s, 180 blocks / 27.5174 MB queued
195.201.119.80:18080 0000000000000000 before_handshake 0 0 0 kB/s, 0 blocks / 0 MB queued
139.59.213.42:51312 7ad8fb534db956dc standby 0 3205572 2 kB/s, 180 blocks / 26.67 MB queued
23.113.152.136:18089 030ebae97e91b369 standby 0 3205572 2 kB/s, 220 blocks / 31.691 MB queued
193.142.4.232:18180 0000000000000000 before_handshake 0 0 0 kB/s, 0 blocks / 0 MB queued
89.58.3.58:18080 e07983702f20b581 standby 0 3205572 1 kB/s, 220 blocks / 31.8505 MB queued
201.6.152.211:18080 0000000000000000 before_handshake 0 0 0 kB/s, 0 blocks / 0 MB queued
51.9.35.180:18080 0000000000000000 before_handshake 0 0 0 kB/s, 0 blocks / 0 MB queued
167.99.55.243:18080 0000000000000000 before_handshake 0 0 0 kB/s, 0 blocks / 0 MB queued
86.170.149.80:18080 0000000000000000 before_handshake 0 0 0 kB/s, 0 blocks / 0 MB queued
193.142.4.189:18085 0000000000000000 before_handshake 0 0 0 kB/s, 0 blocks / 0 MB queued
65.183.108.255:18080 9c2801c21caebb85 synchronizing 0 3204739 289 kB/s, 0 blocks / 0 MB queued
53 spans, 157.018 MB
[moooooooooooooooooooooooooooooooooooooooooooooooooooo]
185.180.14.233:18080 20/182 (3154281 - 3154300, 2575 kB) 1827 kB/s (0.53)
139.59.213.42:51312 20/182 (3154301 - 3154320, 4049 kB) 972 kB/s (0.25)
23.113.152.136:18089 20/182 (3154321 - 3154340, 3186 kB) 1231 kB/s (0.42)
135.181.249.92:18080 20/182 (3154341 - 3154360, 3281 kB) 825 kB/s (0.41)
37.27.70.253:18080 20/182 (3154361 - 3154380, 3282 kB) 2535 kB/s (1)
37.27.70.253:18080 20/182 (3154381 - 3154400, 3678 kB) 3791 kB/s (1)
23.113.152.136:18089 20/182 (3154401 - 3154420, 3091 kB) 1907 kB/s (0.42)
135.181.249.92:18080 20/182 (3154421 - 3154440, 4108 kB) 2116 kB/s (0.41)
23.113.152.136:18089 20/182 (3154441 - 3154460, 2923 kB) 1292 kB/s (0.42)
135.181.249.92:18080 20/182 (3154461 - 3154480, 4370 kB) 1573 kB/s (0.41)
37.27.70.253:18080 20/182 (3154481 - 3154500, 2730 kB) 3668 kB/s (1)
139.59.213.42:51312 20/182 (3154501 - 3154520, 3770 kB) 899 kB/s (0.25)
89.58.3.58:18080 20/182 (3154521 - 3154540, 3592 kB) 764 kB/s (0.64)
89.58.3.58:18080 20/182 (3154541 - 3154560, 2887 kB) 2643 kB/s (0.64)
135.181.249.92:18080 20/182 (3154561 - 3154580, 2563 kB) 1532 kB/s (0.41)
139.59.213.42:51312 20/182 (3154581 - 3154600, 2442 kB) 952 kB/s (0.25)
37.27.70.253:18080 20/182 (3154601 - 3154620, 3889 kB) 3002 kB/s (1)
23.113.152.136:18089 20/182 (3154621 - 3154640, 2443 kB) 385 kB/s (0.42)
135.181.249.92:18080 20/182 (3154641 - 3154660, 2855 kB) 1343 kB/s (0.41)
89.58.3.58:18080 20/182 (3154661 - 3154680, 3037 kB) 1900 kB/s (0.64)
89.58.3.58:18080 20/182 (3154681 - 3154700, 2256 kB) 2990 kB/s (0.64)
23.113.152.136:18089 20/182 (3155321 - 3155340, 3543 kB) 1813 kB/s (0.42)
```

> What kind of OS and hardware do you have?

```
$ uname -a
Linux x220 5.15.0-100-generic #110+11.0trisquel26 SMP Sat Mar 9 20:37:47 UTC 2024 x86_64 x86_64 x86_64 GNU/Linux
$ lscpu
Architecture:            x86_64
  CPU op-mode(s):        32-bit, 64-bit
  Address sizes:         36 bits physical, 48 bits virtual
  Byte Order:            Little Endian
CPU(s):                  4
  On-line CPU(s) list:   0-3
Vendor ID:               GenuineIntel
  Model name:            Intel(R) Core(TM) i5-2520M CPU @ 2.50GHz
    CPU family:          6
    Model:               42
    Thread(s) per core:  2
    Core(s) per socket:  2
    Socket(s):           1
    Stepping:            7
    CPU max MHz:         3200.0000
    CPU min MHz:         800.0000
    BogoMIPS:            4988.43
```

> where is the blockchain saved?

```
$ ls -ahl .bitmonero/lmdb/data.mdb 
-rw------- 1 user user 193G Aug  1 14:41 .bitmonero/lmdb/data.mdb
```

> How many blocks does it sync in 10 minutes?

135. It went from 51445 to 51310 in ~10 minutes.

> And is the SSD internal or external?

SSD is internal.

Let me know if you need further information. 




# Discussion History
## selsta | 2024-08-01T21:32:17+00:00
There was a spam attack which caused full / large blocks for a couple weeks, it should later speed up again. Otherwise I can't think of anything that would explain slower sync.

## kdf8jsa1 | 2024-08-02T20:57:18+00:00
Thank you for the response @selsta, and for the info. 

I am closing this. The daemon is synchronized.

# Action History
- Created by: kdf8jsa1 | 2024-08-01T13:09:04+00:00
- Closed at: 2024-08-02T20:57:18+00:00
