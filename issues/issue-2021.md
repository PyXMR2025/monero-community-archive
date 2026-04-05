---
title: Kawpow disabled ?
source_url: https://github.com/xmrig/xmrig/issues/2021
author: PvtSec
assignees: []
labels:
- question
created_at: '2021-01-04T09:54:05+00:00'
updated_at: '2021-01-10T00:56:50+00:00'
type: issue
status: closed
closed_at: '2021-01-10T00:56:50+00:00'
---

# Original Description
* Issued these arguments to start. But it shows the following error:

```xmrig -o asia.ravenminer.com:3838 -u xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx -k -a kawpow```
Output:
```[asia.ravenminer.com:3838] incompatible/disabled algorithm "kawpow" detected, reconnect```

# Discussion History
## SChernykh | 2021-01-04T13:45:13+00:00
Kawpow mining is supported only for GPUs, so you need to add `--opencl` for AMD or `--cuda` for NVIDIA to your command line.

# Action History
- Created by: PvtSec | 2021-01-04T09:54:05+00:00
- Closed at: 2021-01-10T00:56:50+00:00
