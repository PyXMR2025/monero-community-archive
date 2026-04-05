---
title: Wrong exit code when json is not valid (need "dry-run" option).
source_url: https://github.com/xmrig/xmrig/issues/341
author: k0ste
assignees: []
labels:
- bug
created_at: '2018-01-16T15:36:23+00:00'
updated_at: '2018-01-20T13:44:55+00:00'
type: issue
status: closed
closed_at: '2018-01-20T13:44:54+00:00'
---

# Original Description
Exit code should be 2 or 1.

```shell
[root@linux01 xmrig]# xmrig -c xmrig.conf
xmrig.conf:78: Missing a comma or '}' after an object member.
unable to open /usr/bin/config.json: no such file or directory
No pool URL supplied. Exiting.
[root@linux01 xmrig]# echo $?
0
[root@linux01 xmrig]# 
```

Also will be very useful for automation tasks "--dry-run" option for configuration validation.

# Discussion History
## xmrig | 2018-01-20T13:44:54+00:00
Status code fixed and added option `--dry-run`.
Thank you.

# Action History
- Created by: k0ste | 2018-01-16T15:36:23+00:00
- Closed at: 2018-01-20T13:44:54+00:00
