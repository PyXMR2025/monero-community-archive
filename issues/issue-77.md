---
title: proxy support
source_url: https://github.com/xmrig/xmrig/issues/77
author: dash042
assignees: []
labels: []
created_at: '2017-08-29T21:36:15+00:00'
updated_at: '2017-10-02T11:58:48+00:00'
type: issue
status: closed
closed_at: '2017-10-02T11:58:48+00:00'
---

# Original Description
hi!
on one server I'm having trouble with the proxy - is there a way to define one?
(export http_proxy is set...)
thank you!

# Discussion History
## xmrig | 2017-08-29T23:53:16+00:00
HTTP proxy not supported at all. There no HTTP protocol. Of course if proxy support CONNECT method for it will work, but... There other special proxy https://github.com/xmrig/xmrig-proxy but not sure it helps in your case.
Thank you.

# Action History
- Created by: dash042 | 2017-08-29T21:36:15+00:00
- Closed at: 2017-10-02T11:58:48+00:00
