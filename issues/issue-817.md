---
title: Please add the possibility to specify API bind interface
source_url: https://github.com/xmrig/xmrig/issues/817
author: Nashatyrev
assignees: []
labels:
- review later
created_at: '2018-10-19T08:15:18+00:00'
updated_at: '2019-08-02T12:08:34+00:00'
type: issue
status: closed
closed_at: '2019-08-02T12:08:34+00:00'
---

# Original Description
Now it always binds to `0.0.0.0` (all net interfaces) even if no `--api-no-restricted` option set.
This makes firewall asking questions

```
 * API BIND     0.0.0.0:8111
```

# Discussion History
## xmrig | 2019-08-02T12:08:34+00:00
#1007 

# Action History
- Created by: Nashatyrev | 2018-10-19T08:15:18+00:00
- Closed at: 2019-08-02T12:08:34+00:00
