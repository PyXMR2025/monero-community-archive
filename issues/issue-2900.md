---
title: ' "unknown node or service"'
source_url: https://github.com/xmrig/xmrig/issues/2900
author: IzumiKazuto
assignees: []
labels: []
created_at: '2022-01-26T05:59:10+00:00'
updated_at: '2022-01-26T09:59:06+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
 rx.unmineable.com:3333 DNS error: "unknown node or service"

# Discussion History
## Spudz76 | 2022-01-26T09:59:06+00:00
```
rx.unmineable.com.      290     IN      CNAME   rx.unminable.com.
rx.unminable.com.       19      IN      CNAME   rx-us.unminable.com.
rx-us.unminable.com.    19      IN      A       139.59.164.251
```

Looks up fine from here.  Probably some security garbage blocking known mining sites.  Either whitelist on your local security thing (MS Defender or otherwise) or it might be up at the ISP level, in which case use a public DNS server (not the ISP, who could be filtering DNS) or at worst a VPN so that it can't block port 3333 (well known mining port).  Or use 80/443 if the pool allows, SSL also helps if the ISP is doing content detection filtering.

As a test for port blocking you could use the direct IP from above for the US endpoint at least and see if it connects.  Then it's DNS filtering blocking you.  If raw IP doesn't work then it's a port/content blockage.

# Action History
- Created by: IzumiKazuto | 2022-01-26T05:59:10+00:00
