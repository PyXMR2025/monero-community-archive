---
title: Limit Threads / CPU Cores
source_url: https://github.com/xmrig/xmrig/issues/2944
author: wchorski
assignees: []
labels:
- question
created_at: '2022-02-24T21:17:12+00:00'
updated_at: '2022-04-03T08:00:51+00:00'
type: issue
status: closed
closed_at: '2022-04-03T08:00:51+00:00'
---

# Original Description
**Describe the bug**
Whenever I try to change `make -j$(nproc) `to another number, my system still uses all cores at 100%. I was hoping to relieve some CPU power for other tasks. I started by following the instructions line by line and now I want to reduce the CPU load. 

I tried `make -j$(10)` and even `make -j$(3)` just to see if anything changed but with no luck

**To Reproduce**
I followed the legendary instructions
1. sudo apt-get install git build-essential cmake libuv1-dev libssl-dev libhwloc-dev
2. git clone https://github.com/xmrig/xmrig.git
3. mkdir xmrig/build && cd xmrig/build
4. cmake ..
5. make -j$(nproc)

I even tried a new install. A whole new xmrig folder with the same result. My `config.json` comes from the Wizard. Nothing about thread or core count used in my json file.

**Config.json**
```
{
    "autosave": true,
    "donate-level": 5,
    "cpu": true,
    "opencl": false,
    "cuda": false,
    "pools": [
        {
            "url": "monerohash.com:9999",
            "user": "123",
            "keepalive": true,
            "tls": true
        }
    ]
}
```


**Questions**
Am I able to hot fix this problem? After I add this thread / core limit, where do i need to build again to initialize the new config?


# Discussion History
## Spudz76 | 2022-02-25T00:31:26+00:00
`-j` is an option for `make` and sets how many code compile threads are used, and has nothing to do with any other type of thread.

After you run once with that config edit the config again and the `cpu` section will have definition arrays.  Remove some elements from the array for whichever algorithm you are tuning.

# Action History
- Created by: wchorski | 2022-02-24T21:17:12+00:00
- Closed at: 2022-04-03T08:00:51+00:00
