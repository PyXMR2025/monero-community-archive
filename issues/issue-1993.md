---
title: CL_OUT_OF_HOST_MEMORY with AMD Radeon Vega 8 (gfx902)
source_url: https://github.com/xmrig/xmrig/issues/1993
author: ulitosCoder
assignees: []
labels: []
created_at: '2020-12-22T02:01:37+00:00'
updated_at: '2021-04-12T14:27:16+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:27:16+00:00'
---

# Original Description
When i start xmrig in windows 10 with command line I get eventually get CL_OUT_OF_HOST_MEMORY.

xmrig won't stop but would disable opencl backend.

![image](https://user-images.githubusercontent.com/17461642/102839687-ad98f400-43c6-11eb-9869-db9d8980c535.png)

**Required data**
 - Config file or command line (without wallets)
 - Windows 10
 - AMD Radeon Vega 8 (gfx902)
 - command line: xmrig.exe --no-cpu -a Kawpow -o rvn-eu1.nanopool.org:12222 -u WALLET/worker/email@example.com -p x --opencl -k



# Discussion History
## Spudz76 | 2020-12-22T05:16:20+00:00
How much host memory do you have free?

## ulitosCoder | 2020-12-22T05:38:16+00:00
45% free, using 2.9GB out of 5.9GB

# Action History
- Created by: ulitosCoder | 2020-12-22T02:01:37+00:00
- Closed at: 2021-04-12T14:27:16+00:00
