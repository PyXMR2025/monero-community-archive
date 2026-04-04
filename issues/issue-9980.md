---
title: rpc_ssl certificate expiry
source_url: https://github.com/monero-project/monero/issues/9980
author: pannal
assignees: []
labels: []
created_at: '2025-07-11T11:33:25+00:00'
updated_at: '2025-07-19T18:35:55+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hey,

Judging from [the daemon code](https://github.com/monero-project/monero/blob/master/src/rpc/core_rpc_server.cpp#L355), it generates self signed certificates for SSL-enabled RPC, on ::init, valid for about half a year.

I can't find any logic in the daemon that'd suggest these get regenerated once they've expired, and/or even checked for expiry.


Am I wrong? Thanks!

# Discussion History
## pannal | 2025-07-11T11:46:38+00:00
Further investigation:
* the daemon always generates those certs on init
* once rpc_ssl.crt/key exist, their modification date doesn't change on the filesystem, but the certificate NotBefore/NotAfter show that they've been generated anew

Does this mean, that a long running monerod (6m+) will just end up with expired certificates, no matter what?

## nahuhh | 2025-07-19T15:26:58+00:00
@vtnerd

# Action History
- Created by: pannal | 2025-07-11T11:33:25+00:00
