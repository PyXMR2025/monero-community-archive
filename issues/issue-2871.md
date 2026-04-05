---
title: xmrig fails to mine Ghostrider on single-core (VM)
source_url: https://github.com/xmrig/xmrig/issues/2871
author: APT-ZERO
assignees: []
labels:
- bug
created_at: '2022-01-17T15:06:23+00:00'
updated_at: '2022-01-19T09:56:46+00:00'
type: issue
status: closed
closed_at: '2022-01-19T09:56:46+00:00'
---

# Original Description
**Describe the bug**
xmrig fails to mine Ghostrider on single-core (VM)
there is no error, it just exits

**To Reproduce**
Make a Windows VM with only 1 core
`xmrig.exe -o flockpool.com:5555 -u {WALLET} -a gr -p x --tls` (run as administrator)
xmrig versions used: 6.16.2 and 6.16.3 (dev)

then add another core to your VM, and it can Mine even with `-t 1`
problem is only when there is only 1 core

# Discussion History
# Action History
- Created by: APT-ZERO | 2022-01-17T15:06:23+00:00
- Closed at: 2022-01-19T09:56:46+00:00
