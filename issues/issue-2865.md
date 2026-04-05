---
title: ghostrider algo uses more CPU than expected
source_url: https://github.com/xmrig/xmrig/issues/2865
author: mintro32
assignees: []
labels: []
created_at: '2022-01-15T08:12:55+00:00'
updated_at: '2024-09-03T17:49:30+00:00'
type: issue
status: closed
closed_at: '2022-01-20T01:37:02+00:00'
---

# Original Description
**Describe the bug**
CPU usage is significantly higher than what I specified in the config file when using ghostrider algo.

**To Reproduce**
Put this as the setting for ghostrider in the config file: (generated from an appropriate initial "cpu-max-threads-hint")
```
"ghostrider": [
            [8, 0]
        ]
```

**Expected behavior**
The miner's CPU usage should be very close to 1

**Required data**
![image](https://user-images.githubusercontent.com/81028826/149614431-2ef1c7ca-3804-4fce-9854-b7703c04e034.png)
CPU usage of the miner is significantly higher than 1: 
![image](https://user-images.githubusercontent.com/81028826/149614468-084e3c3d-75f0-4f2a-85b3-c012cac62dff.png)
![image](https://user-images.githubusercontent.com/81028826/149614457-a366d082-0154-4478-91f9-dfa4e60e30ff.png)

 - OS: Linux



# Discussion History
## SChernykh | 2022-01-15T17:10:56+00:00
XMRig runs threads in pairs for GhostRider (each thread in config = 2 threads running), so this is expected behavior.

## mintro32 | 2022-01-20T01:37:02+00:00
Thanks for the explanation. I guess I would just try to adjust with that in mind.

## mwp-foss | 2024-09-03T17:49:29+00:00
> XMRig runs threads in pairs for GhostRider (each thread in config = 2 threads running), so this is expected behavior.

This behavior is counter intuitive to `cpu-max-threads-hint`. The algorithm should query `cpu-max-threads-hint` and auto set itself to thread pairs within the suggested limit, not double the limit because it needs thread-pairs.

For example:

`cpu-max-threads-hint` is set to `25` on a 16c/32t processor, this would mean use a max of 8 threads; GhostRider would set itself to 4 thread pairs

`cpu-max-threads-hint` is set to `22` on a 16c/32t processor, this would mean use a max of 7 threads; GhostRider would set itself to 3 thread pairs

# Action History
- Created by: mintro32 | 2022-01-15T08:12:55+00:00
- Closed at: 2022-01-20T01:37:02+00:00
