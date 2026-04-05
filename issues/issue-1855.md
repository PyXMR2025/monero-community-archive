---
title: Is TLS 1.3 support by XMRig miner?
source_url: https://github.com/xmrig/xmrig/issues/1855
author: BKdilse
assignees: []
labels:
- question
created_at: '2020-09-26T23:13:33+00:00'
updated_at: '2020-09-27T08:35:32+00:00'
type: issue
status: closed
closed_at: '2020-09-27T08:35:32+00:00'
---

# Original Description
Just a question, I see XMRig using TLS 1.2.  Is TLS 1.3 supported or will it be at some point?

# Discussion History
## xmrig | 2020-09-27T01:04:18+00:00
It already supported with 2 conditions:
1. Miner built with OpenSSL 1.1.1.
2. Pool support, for example https://minexmr.com/.


## BKdilse | 2020-09-27T08:16:14+00:00
Thanks, I've confirmed TLS 1.3 is working with minxmr, but not with my pool.  Would you know if there is additional configuration required on the pool side?  The pool website and certificate show TLS 1.3 is enabled.


## xmrig | 2020-09-27T08:29:09+00:00
I guess this article contains all answers https://developer.ibm.com/blogs/migrating-to-tls13-in-nodejs/
Thank you.

## BKdilse | 2020-09-27T08:35:32+00:00
Yeah, just saw that, it looks like my old Node version may not support it.  Thanks for your help, I'll do some testing.


# Action History
- Created by: BKdilse | 2020-09-26T23:13:33+00:00
- Closed at: 2020-09-27T08:35:32+00:00
