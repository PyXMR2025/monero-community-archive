---
title: Benchmark and mining different rates
source_url: https://github.com/xmrig/xmrig/issues/3643
author: ntstatus-cc
assignees: []
labels:
- question
created_at: '2025-03-09T14:43:53+00:00'
updated_at: '2025-06-16T19:31:23+00:00'
type: issue
status: closed
closed_at: '2025-06-16T19:31:23+00:00'
---

# Original Description
Hello.

First off. hopefully this is ez and I am missing something stupid.  I am fairly new to this.  I have dug thru the archives and havent found anything so far that matches this.

My benchmark scores any my mining scores are vastly different.  My benchmark scores are not great considering the rig, but thats a different issue.  As I mentioned nothing stands out.  I have two of these servers and they both do the same thing.  Any guidance would be appreciated.  Below is the config and screenshots of the BM and the Rig running.

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
        "1gb-pages": false,
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
        "argon2": [0, 2, 4, 6, 5, 7],
        "cn": [
            [1, 0],
            [1, 2],
            [1, 4]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 2]
        ],
        "cn-lite": [
            [1, 0],
            [1, 2],
            [1, 4],
            [1, 6],
            [1, 5],
            [1, 7]
        ],
        "cn-pico": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3],
            [2, 4],
            [2, 5],
            [2, 6],
            [2, 7]
        ],
        "cn/upx2": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3],
            [2, 4],
            [2, 5],
            [2, 6],
            [2, 7]
        ],
        "ghostrider": [
            [8, 0],
            [8, 2],
            [8, 4]
        ],
        "rx": [0, 1, 2, 3, 4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],
        "rx/arq": [0, 1, 2, 3, 4, 5, 6, 7],
        "rx/wow": [0, 2, 4, 6, 5, 7],
        "cn-lite/0": false,
        "cn/0": false
    },
    "opencl": {
        "enabled": false,
        "cache": true,
        "loader": null,
        "platform": "AMD",
        "adl": true,
        "cn-lite/0": false,
        "cn/0": false
    },
    "cuda": {
        "enabled": false,
        "loader": null,
        "nvml": true,
        "cn-lite/0": false,
        "cn/0": false
    },
    "log-file": null,
    "donate-level": 1,
    "donate-over-proxy": 1,
    "pools": [

![Image](https://github.com/user-attachments/assets/bb30c5a7-ca4a-4a22-a3c1-dc024de5344c)

![Image](https://github.com/user-attachments/assets/7ed40820-d46e-4b59-92fc-4f6aadea8ed9)

![Image](https://github.com/user-attachments/assets/7ad7258a-6391-444f-b959-1fda2f8728e8)

# Discussion History
## ntstatus-cc | 2025-03-09T14:47:08+00:00
I apologize for the double screenshot.  The second capture didnt take.

![Image](https://github.com/user-attachments/assets/dd23651e-fc78-4516-bc3e-ff38851e1069)

## SChernykh | 2025-03-09T15:58:03+00:00
```
"rx": [0, 1, 2, 3, 4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],
```
Try to delete this line in config.json and start mining again.

## ntstatus-cc | 2025-03-09T16:05:15+00:00
Worked like a charm.  Thank you!

## chatkhoipt | 2025-04-07T13:32:53+00:00
yo that's a powerful computer


# Action History
- Created by: ntstatus-cc | 2025-03-09T14:43:53+00:00
- Closed at: 2025-06-16T19:31:23+00:00
