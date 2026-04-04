---
title: 'E: duplicate key: support_flags'
source_url: https://github.com/monero-project/monero/issues/8062
author: S1700
assignees: []
labels: []
created_at: '2021-11-15T16:44:57+00:00'
updated_at: '2021-11-18T17:45:04+00:00'
type: issue
status: closed
closed_at: '2021-11-18T17:45:04+00:00'
---

# Original Description
![image](https://user-images.githubusercontent.com/68336568/141820479-e248d86c-106e-4c0c-8be1-3e5b9cb1cf7d.png)
don't know why and how but I'm getting it every time i run monerod


# Discussion History
## selsta | 2021-11-15T23:19:16+00:00
It's someone running a broken node, you can try to ban that IP.

## S1700 | 2021-11-16T16:24:51+00:00
how would i find and ban the IP?

## selsta | 2021-11-17T02:12:44+00:00
I guess you can delete ~/.bitmonero/p2pstate.bin file, then you will connect to new nodes, hopefully the broken node isn't part of it.

# Action History
- Created by: S1700 | 2021-11-15T16:44:57+00:00
- Closed at: 2021-11-18T17:45:04+00:00
