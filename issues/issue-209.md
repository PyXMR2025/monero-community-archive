---
title: C API
source_url: https://github.com/xmrig/xmrig/issues/209
author: alanhoff
assignees: []
labels:
- enhancement
- wontfix
created_at: '2017-11-20T01:36:32+00:00'
updated_at: '2019-08-02T12:31:33+00:00'
type: issue
status: closed
closed_at: '2019-08-02T12:31:33+00:00'
---

# Original Description
Hello there, I had this crazy idea about building a software that uses user's idle CPU to mine Monero for charity. For that I would need a C API so I could easily use it as a library into another program. Do you know if that's possible?

Cheers!

# Discussion History
## xmrig | 2017-11-20T09:54:58+00:00
It possible, but I don't sure how high level shoud be library API.
For example, load config, start mine, maybe pause/resume, etc.
Thank you.

## alanhoff | 2017-11-20T10:59:40+00:00
An external function for configurating, starting, pausing and resuming looks like all I need. Btw it would be awesome if we could statically link `xmriglib` 😊

# Action History
- Created by: alanhoff | 2017-11-20T01:36:32+00:00
- Closed at: 2019-08-02T12:31:33+00:00
