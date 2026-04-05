---
title: (LINUX CPU mining) HTTP Daemon failed to start
source_url: https://github.com/xmrig/xmrig/issues/451
author: survivor303
assignees: []
labels: []
created_at: '2018-03-15T14:59:58+00:00'
updated_at: '2018-03-16T17:45:39+00:00'
type: issue
status: closed
closed_at: '2018-03-16T17:45:39+00:00'
---

# Original Description
When i start xmrig, first line is:
HTTP Daemon failed to start.
I dont find any documentation for this error, so what it is and can i just ignore it?

# Discussion History
## xmrig | 2018-03-15T15:05:59+00:00
This error means port used to HTTP API already used (most likely) or other error occurred. HTTP API disabled by default, so that means you already enable it by choice some port for it, until this error exists you can't use API. Mining functions not affected.
Thank you.

# Action History
- Created by: survivor303 | 2018-03-15T14:59:58+00:00
- Closed at: 2018-03-16T17:45:39+00:00
