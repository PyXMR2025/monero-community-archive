---
title: API Output Truncated
source_url: https://github.com/xmrig/xmrig/issues/290
author: adampointer
assignees: []
labels:
- bug
created_at: '2017-12-24T08:06:41+00:00'
updated_at: '2018-11-05T07:04:49+00:00'
type: issue
status: closed
closed_at: '2018-11-05T07:04:49+00:00'
---

# Original Description
Calling the API only gives partial output.

```
$ curl 192.168.0.32:8080
{
    "id": "2775735600056a5c",
    "worker_id": "rock64",
    "version": "2.4.3",
    "kind": "cpu",
    "ua": "XMRig/2.4.3 (Linux i686) libuv/1.8.0 gcc/5.4.0",
    "cpu": {
        "brand": "Unknown",
        "aes": true,
        "x64": true,
        "sockets": 1
    },
    "algo": "cryptonight",
    "hugepages": true,
    "donate_level": 1,
    "hashrate": {
        "total": [
            0.0,
            15.29,
            15.29
        ],
        "highest": 0.0,
        "threads": [
            [
```

Compiled from source on Ubuntu Xenial on an ARM7 SOC board. No extra flags passed to cmake.

EDIT: Building using GCC-7 fixed it.

# Discussion History
# Action History
- Created by: adampointer | 2017-12-24T08:06:41+00:00
- Closed at: 2018-11-05T07:04:49+00:00
