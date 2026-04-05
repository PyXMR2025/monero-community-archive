---
title: Major TLS (Transport Layer Security) subsystem update
source_url: https://github.com/xmrig/xmrig/issues/1596
author: xmrig
assignees: []
labels:
- enhancement
- META
created_at: '2020-03-18T20:24:41+00:00'
updated_at: '2022-05-07T02:48:34+00:00'
type: issue
status: closed
closed_at: '2020-06-02T14:33:50+00:00'
---

# Original Description
Version 5.10.x brings major TLS (Transport Layer Security) subsystem update since it was firstly implemented.

Major changes:
* Automatic TLS certificate generation for xmrig-proxy and the miner.
* TLS zero configuration for the proxy out of box. https://xmrig.com/docs/proxy/tls
* HTTPS support for API (automatic detection).
* Automatic TLS detection for the proxy ports.
* Multiple other fixes and improvements.


# Discussion History
## Spudz76 | 2020-03-21T20:54:37+00:00
#1601 may be related

## ttsite | 2022-05-07T02:48:34+00:00
Can you just enable this TLS in xmrig proxy? It should also be enabled in xmrig How to change the specific configuration file

# Action History
- Created by: xmrig | 2020-03-18T20:24:41+00:00
- Closed at: 2020-06-02T14:33:50+00:00
