---
title: 'After compiling for the Mac, RandomX algorithms are auto changing to cn/r. '
source_url: https://github.com/xmrig/xmrig/issues/1091
author: tommyprevatt
assignees: []
labels:
- question
created_at: '2019-07-31T19:28:26+00:00'
updated_at: '2019-08-01T18:27:16+00:00'
type: issue
status: closed
closed_at: '2019-08-01T18:27:16+00:00'
---

# Original Description
I've tried running from the terminal, and from config, but either way it's changing to cn/r. This is specifically Wownero I'm trying. 


Terminal output:
` * ABOUT        XMRig/2.14.4 clang/10.0.0
 * LIBS         libuv/1.30.1 OpenSSL/1.0.2s microhttpd/0.9.63 
 * CPU          Intel(R) Core(TM) i7-2760QM CPU @ 2.40GHz (1) x64 AES -AVX2
 * CPU L2/L3    1.0 MB/6.0 MB
 * THREADS      3, cryptonight, donate=5%
 * ASSEMBLY     auto:intel
 * POOL #1      mine.wow.fairpool.xyz:6090 variant auto
 * COMMANDS     hashrate, pause, resume
[2019-07-31 12:18:10] use pool mine.wow.fairpool.xyz:6090  173.234.31.211 
[2019-07-31 12:18:10] new job from mine.wow.fairpool.xyz:6090 diff 2000 algo cn/r height 128667
[2019-07-31 12:18:11] READY (CPU) threads 3(3) huge pages 3/3 100% memory 6144 KB
[2019-07-31 12:18:13] rejected (0/1) diff 2000 "Wrong algorithm specified. Check the miner's settings" (857 ms)
[2019-07-31 12:18:13] [mine.wow.fairpool.xyz:6090] read error: "end of file"
[2019-07-31 12:18:13] no active pools, stop mining
[2019-07-31 12:18:16] Ctrl+C received, exiting
`

Config file:

> {
    "api": {
        "id": null,
        "worker-id": null
    },
    "autosave": true,
    "background": false,
    "colors": true,
    "donate-level": 5,
    "donate-over-proxy": 1,
    "http": {
        "enabled": false,
        "host": "127.0.0.1",
        "port": 0,
        "access-token": null,
        "restricted": true
    },
    "log-file": null,
    "pools": [
        {
            "algo": "rx/wow",
            "url": "mine.wow.fairpool.xyz:6090",
            "user": "Wo3zT3TeyVCaEJG9Y8ALnZiNDLTj1gtFq6UyDawENd4EBghbxo5ZamHTBU9QsSrkFdQJDwAJRcWxCQccZiEvuWNB27nvDHdWV",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
            "enabled": true,
            "tls": false,
            "tls-fingerprint": null,
            "daemon": false
        }
    ],
    "print-time": 60,
    "retries": 5,
    "retry-pause": 5,
    "syslog": false,
    "user-agent": null,
    "watch": true
}

# Discussion History
## xmrig | 2019-08-01T01:48:28+00:00
You use `2.14.4` version, for mine Wownero you should use `2.99.x`.
Thank you.

## tommyprevatt | 2019-08-01T09:45:42+00:00
Hmm. Wow. Didn't notice that. I cloned straight from github to download it. I'll download it manually and try again. 

## tommyprevatt | 2019-08-01T18:27:16+00:00
I'm assuming the reason is because it was pulling the most recent non-beta. duh me.. I have another problem now but I will post it as a separate issue. Thanks!

# Action History
- Created by: tommyprevatt | 2019-07-31T19:28:26+00:00
- Closed at: 2019-08-01T18:27:16+00:00
