---
title: Crash on close
source_url: https://github.com/xmrig/xmrig/issues/40
author: BiTOk
assignees: []
labels: []
created_at: '2017-07-18T13:46:05+00:00'
updated_at: '2017-07-19T23:57:14+00:00'
type: issue
status: closed
closed_at: '2017-07-19T23:57:14+00:00'
---

# Original Description
I get segfault on xmrig close on linux with gcc 7.1.1. I tried 2.0.2 and 2.1.0-dev#e00c568ae xmrig versions.
In console:
SEGINT received, exiting
no active pools, pause mining
SEGFAULT

# Discussion History
## xmrig | 2017-07-18T14:25:36+00:00
Thank you, I know, working on it.

## xmrig | 2017-07-19T01:35:02+00:00
I fixed crash, please verify.

## BiTOk | 2017-07-19T07:33:24+00:00
@xmrig It looks good, thank you for fix.

# Action History
- Created by: BiTOk | 2017-07-18T13:46:05+00:00
- Closed at: 2017-07-19T23:57:14+00:00
