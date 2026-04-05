---
title: xmrig 2.8.0 is not reported about pool connection issues
source_url: https://github.com/xmrig/xmrig/issues/777
author: k0ste
assignees: []
labels:
- bug
created_at: '2018-10-05T03:45:10+00:00'
updated_at: '2018-10-10T22:23:18+00:00'
type: issue
status: closed
closed_at: '2018-10-10T22:23:18+00:00'
---

# Original Description
Perhaps this is caused `tls` is enabled. Operator should see log about connection issues and reconnection try's.

```
 * ABOUT        XMRig-AMD/2.8.0-rc gcc/8.2.1
 * LIBS         libuv/1.23.1 OpenCL/2.0 OpenSSL/1.1.1 microhttpd/0.9.59 
 * CPU                Intel(R) Celeron(R) CPU  J1800  @ 2.41GHz x64 -AES
 * ALGO         cryptonight, donate=0%
 * POOL #1      killallasics.moneroworld.com:7777 variant auto
 * API BIND     0.0.0.0:8088
 * COMMANDS     hashrate, pause, resume
[2018-10-05 10:36:23] compiling code and initializing GPUs. This will take a while...
[2018-10-05 10:36:26] found AMD platform index: 0, name: Advanced Micro Devices, Inc.
[2018-10-05 10:36:26] #0, GPU #0 , intensity: 400 (8/256), unroll: 8, cu: 20
[2018-10-05 10:36:26] #1, GPU #0 , intensity: 400 (8/256), unroll: 8, cu: 20
[2018-10-05 10:36:26] #2, GPU #1 , intensity: 400 (8/256), unroll: 8, cu: 16
[2018-10-05 10:36:26] #3, GPU #1 , intensity: 400 (8/256), unroll: 8, cu: 16
[2018-10-05 10:36:26] #4, GPU #2 , intensity: 400 (8/256), unroll: 8, cu: 20
[2018-10-05 10:36:26] #5, GPU #2 , intensity: 400 (8/256), unroll: 8, cu: 20
[2018-10-05 10:36:26] #6, GPU #3 , intensity: 400 (8/256), unroll: 8, cu: 16
[2018-10-05 10:36:26] #7, GPU #3 , intensity: 400 (8/256), unroll: 8, cu: 16
[2018-10-05 10:36:26] #8, GPU #4 , intensity: 400 (8/256), unroll: 8, cu: 20
[2018-10-05 10:36:26] #9, GPU #4 , intensity: 400 (8/256), unroll: 8, cu: 20
[2018-10-05 10:36:26] #10, GPU #5 , intensity: 400 (8/256), unroll: 8, cu: 16
[2018-10-05 10:36:26] #11, GPU #5 , intensity: 400 (8/256), unroll: 8, cu: 16
[2018-10-05 10:36:36] speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
[2018-10-05 10:36:46] speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
[2018-10-05 10:36:56] speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
[2018-10-05 10:37:06] speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
[2018-10-05 10:37:16] speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
[2018-10-05 10:37:26] speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
[2018-10-05 10:37:36] speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
[2018-10-05 10:37:46] speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
[2018-10-05 10:37:56] speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
[2018-10-05 10:38:06] speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
[2018-10-05 10:38:16] speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
[2018-10-05 10:38:26] speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
[2018-10-05 10:38:36] speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
[2018-10-05 10:38:46] speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
[2018-10-05 10:38:56] speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
[2018-10-05 10:39:06] speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
[2018-10-05 10:39:16] speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
```

test data:

```
// xmrig.conf
// Ansible managed: /home/k0ste/sandbox/Mining/leko-ansible/roles/xmrig/templates/xmrig.j2 modified on 2018-07-30 21:42:08 by k0ste on WorkStation
// Do not edit manually

{
  "algo": "cryptonight",
  "syslog": true,
  "watch": false,
  "print-time": 10,
  "threads": [
    {
      "index": 0,
      "intensity": 400,
      "worksize": 8,
    },
    {
      "index": 0,
      "intensity": 400,
      "worksize": 8,
    },
    {
      "index": 1,
      "intensity": 400,
      "worksize": 8,
    },
    {
      "index": 1,
      "intensity": 400,
      "worksize": 8,
    },
    {
      "index": 2,
      "intensity": 400,
      "worksize": 8,
    },
    {
      "index": 2,
      "intensity": 400,
      "worksize": 8,
    },
    {
      "index": 3,
      "intensity": 400,
      "worksize": 8,
    },
    {
      "index": 3,
      "intensity": 400,
      "worksize": 8,
    },
    {
      "index": 4,
      "intensity": 400,
      "worksize": 8,
    },
    {
      "index": 4,
      "intensity": 400,
      "worksize": 8,
    },
    {
      "index": 5,
      "intensity": 400,
      "worksize": 8,
    },
    {
      "index": 5,
      "intensity": 400,
      "worksize": 8,
    }
  ],
  "api": {
    "port": 8088,
    "access-token": null,
    "worker-id": null,
    "ipv6": false,
  },
  "pools": [
    {
      "keepalive": true,
      "url": "killallasics.moneroworld.com:7777",
      "pass": "x",
      "user": "9v4vTVwqZzfjCFyPi7b9Uv1hHntJxycC4XvRyEscqwtq8aycw5xGpTxFyasurgf2KRBfbdAJY4AVcemL1JCegXU4EZfMtaz",
      "rig-id": "dummy",
      "tls": true,
    }
  ]
}
```

# Discussion History
## xmrig | 2018-10-08T20:51:19+00:00
Fixed, now it will be looks like `[killallasics.moneroworld.com:7777] read error: "end of file"` error text not well describe itself, but it was exactly what happen and notify user about connection issues.
Thank you.

# Action History
- Created by: k0ste | 2018-10-05T03:45:10+00:00
- Closed at: 2018-10-10T22:23:18+00:00
