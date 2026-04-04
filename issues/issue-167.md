---
title: 'Build: can''t connect with RDP to Win32 build machine onion'
source_url: https://github.com/monero-project/meta/issues/167
author: anonimal
assignees: []
labels: []
created_at: '2018-01-24T16:58:13+00:00'
updated_at: '2018-01-24T19:21:07+00:00'
type: issue
status: closed
closed_at: '2018-01-24T19:21:07+00:00'
---

# Original Description
```
[INFO][com.freerdp.client.common.cmdline] - loading channelEx cliprdr
[ERROR][com.freerdp.core] - failed to connect to [redacted.onion]  
[ERROR][com.freerdp.core.nego] - Protocol Security Negotiation Failure 
[ERROR][com.freerdp.core] - freerdp_set_last_error ERRCONNECT_SECURITY_NEGO_CONNECT_FAILED [0x0002000C]
[ERROR][com.freerdp.core.connection] - Error: protocol security negotiation or connection failure
[ERROR][com.freerdp.client.x11] - Freerdp connect error exit status 1
```

# Discussion History
## anonimal | 2018-01-24T19:21:07+00:00
Bad circuits on either end. Works now.

# Action History
- Created by: anonimal | 2018-01-24T16:58:13+00:00
- Closed at: 2018-01-24T19:21:07+00:00
