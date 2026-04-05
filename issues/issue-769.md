---
title: Escape characters in the log file with --no-color argument (2.8.0-rc)
source_url: https://github.com/xmrig/xmrig/issues/769
author: timk74
assignees: []
labels:
- bug
created_at: '2018-10-02T01:30:33+00:00'
updated_at: '2018-10-03T10:16:15+00:00'
type: issue
status: closed
closed_at: '2018-10-02T10:15:13+00:00'
---

# Original Description
Escape characters is present in tls info even if using --no-color command line argument:
```
[2018-10-02 11:22:34] use pool xmr-eu1.nanopool.org:14433 TLSv1.2 139.162.81.90
[2018-10-02 11:22:34] [1;30mfingerprint (SHA-256): "c38886efdee542ebd99801b75c75d3498d97978bbcdec07c7271cb19729e014f"
```


# Discussion History
## xmrig | 2018-10-02T10:06:05+00:00
Confirmed. Thank you.

## xmrig | 2018-10-02T10:15:13+00:00
Fixed.

# Action History
- Created by: timk74 | 2018-10-02T01:30:33+00:00
- Closed at: 2018-10-02T10:15:13+00:00
