---
title: Api https support
source_url: https://github.com/xmrig/xmrig/issues/867
author: mk148a
assignees: []
labels:
- wontfix
created_at: '2018-11-03T00:04:36+00:00'
updated_at: '2018-11-05T07:07:48+00:00'
type: issue
status: closed
closed_at: '2018-11-05T06:47:20+00:00'
---

# Original Description
Hi, xmrig is have https secure api support?
Can you make it for data security?

# Discussion History
## lisergey | 2018-11-03T12:00:12+00:00
@mk148mk you can use nginx in front of xmrig http.
with Nginx it is superbous https.

There is no need to overload wonderful xmrig with that is already well done by others.

## xmrig | 2018-11-05T06:47:20+00:00
libmicrohttpd required GnuTLS, but miner itself use OpenSSL, so for https in API need use 2 different SSL libraries, so right now answer is no.

## xmrig | 2018-11-05T07:07:47+00:00
Duplicate #317 

# Action History
- Created by: mk148a | 2018-11-03T00:04:36+00:00
- Closed at: 2018-11-05T06:47:20+00:00
