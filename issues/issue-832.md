---
title: 'connect error: "connection refused"'
source_url: https://github.com/xmrig/xmrig/issues/832
author: webnavard
assignees: []
labels: []
created_at: '2018-10-21T05:26:30+00:00'
updated_at: '2018-10-22T15:39:56+00:00'
type: issue
status: closed
closed_at: '2018-10-22T15:39:56+00:00'
---

# Original Description
Hello
in version 2.8.3 I get this error in Nanopool : 
[2018-10-21 08:54:34] [xmr-eu1.nanopool.org] connect error: "connection refused"
[2018-10-21 08:54:34] READY (CPU) threads 20(20) huge pages 0/40 0% memory 80.0 MB
[2018-10-21 08:54:40] [xmr-eu1.nanopool.org] connect error: "connection refused"


# Discussion History
## gboelter | 2018-10-21T06:32:37+00:00
If you are looking for help, you should _at least_ show as the 'Pool part' from your config.json file.

## webnavard | 2018-10-21T15:45:02+00:00
it's linux base and the start command =>
./xmrig -a cryptonight --api-port 14444 --api-worker-id hpserv --max-cpu-usage 100 --cpu-priority 3 -o xmr-eu2.nanopool.org -u 4AzQhCVnK9XTbVWXTvUaTHuQ6VXMwbhWfaVoKGyebygDrcHgXJnaKwVHZHagYrkiwYfLVB5f -p x -k


## webnavard | 2018-10-21T15:46:20+00:00
and this is for win =>
{
    "algo": "cryptonight",
    "api": {
        "port": 14444,
        "access-token": null,
        "id": null,
        "worker-id": "hpserv",
        "ipv6": false,
        "restricted": true
    },
    "autosave": true,
    "av": 0,
    "background": false,
    "colors": true,
    "cpu-affinity": null,
    "cpu-priority": 3,
    "donate-level": 5,
    "huge-pages": true,
    "hw-aes": null,
    "log-file": null,
    "max-cpu-usage": 100,
    "pools": [
        {
            "url": "xmr-eu1.nanopool.org",
            "user": "4AzQWYZPQiNhCVnK9XTbVWXTvUaTHuQ6VXMwbhWgPDN8bkhJCDfaVoKGyebygDrcHgXJnaKwVHZHagYrkiwYfLV***",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": true,
            "variant": 0,
            "tls": true,
            "tls-fingerprint": null
        }
    ],
    "print-time": 60,
    "retries": 5,
    "retry-pause": 5,
    "safe": false,
    "threads": [
        {
            "low_power_mode": 1,
            "affine_to_cpu": false
        },
        {
            "low_power_mode": 1,
            "affine_to_cpu": false
        },
        {
            "low_power_mode": 1,
            "affine_to_cpu": false
        },
        {
            "low_power_mode": 1,
            "affine_to_cpu": false
        }
    ],
    "user-agent": null,
    "watch": false
}

## webnavard | 2018-10-21T16:03:59+00:00
 * ABOUT        XMRig/2.8.1 gcc/4.8.5
 * LIBS         libuv/1.22.0 OpenSSL/1.0.2k microhttpd/0.9.33
 * CPU          Intel(R) Xeon(R) CPU E5-2620 v2 @ 2.10GHz (10) x64 AES
 * CPU L2/L3    50.0 MB/150.0 MB
 * THREADS      20, cryptonight, av=0, donate=1%
 * ASSEMBLY     auto:intel
 * POOL #1      xmr-eu1.nanopool.org variant auto
 * COMMANDS     hashrate, pause, resume
[2018-10-21 19:33:02] [xmr-eu1.nanopool.org] connect error: "connection refused"
[2018-10-21 19:33:03] READY (CPU) threads 20(20) huge pages 0/20 0% memory 40.0 

## xmrig | 2018-10-21T16:06:36+00:00
`xmr-eu1.nanopool.org:14433` you must use port number too.



# Action History
- Created by: webnavard | 2018-10-21T05:26:30+00:00
- Closed at: 2018-10-22T15:39:56+00:00
