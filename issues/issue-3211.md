---
title: Preserving MSR_AMD64_LS_CFG [0xc0011020] --randomx-wrmsr=-1
source_url: https://github.com/xmrig/xmrig/issues/3211
author: cyring
assignees: []
labels: []
created_at: '2023-02-11T10:44:50+00:00'
updated_at: '2023-02-12T02:09:59+00:00'
type: issue
status: closed
closed_at: '2023-02-12T02:09:59+00:00'
---

# Original Description
**Describe the bug**
L1 and L2 are not preserved to original state with `--randomx-wrmsr=-1`

**To Reproduce**
```
sudo xmrig --bench=1M --randomx-wrmsr=-1

./corefreq-cli -s
```

```
...
Technologies                                                                    
|- Instruction Cache Unit                                                       
   |- L1 IP Prefetcher                                          L1 HW IP   < ON>
|- Data Cache Unit                                                              
   |- L1 Prefetcher                                                L1 HW   <OFF>
   |- L2 Prefetcher                                                L2 HW   <OFF>
...
```

**Expected behavior**
Maintain bits in Register.

**Required data**
 - Miner log as text or screenshot
 - Config file or command line `sudo xmrig --bench=1M --randomx-wrmsr=-1`
 - OS: Linux 6.1.1
 - For GPU related issues: information about GPUs and driver version.

**Additional context**
None


# Discussion History
## Spudz76 | 2023-02-12T00:15:07+00:00
Doesn't work like that.  You've told it to set the msr registers to `static_cast<int64_t>(strtol("-1", nullptr, 10))` which is `0xffffffff` (who knows what that does)

The only way to disable writing MSR's is to edit `config.json` and set `randomx->wrmsr:false` there is no command line argument to do it.

## cyring | 2023-02-12T02:09:58+00:00
Ok through `config.json`

# Action History
- Created by: cyring | 2023-02-11T10:44:50+00:00
- Closed at: 2023-02-12T02:09:59+00:00
