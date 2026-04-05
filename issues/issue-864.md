---
title: hardcoded Add logFile error
source_url: https://github.com/xmrig/xmrig/issues/864
author: luxig
assignees: []
labels:
- question
created_at: '2018-11-02T06:17:27+00:00'
updated_at: '2018-11-05T06:54:56+00:00'
type: issue
status: closed
closed_at: '2018-11-05T06:54:56+00:00'
---

# Original Description
hardcoded Add logFile error
Ex: m_pools.push_back(Pool("Poolurl.com", 12345, "username", "pw"));    success

Ex: m_pools.push_back(Pool("Poolurl.com", 12345, "username", "pw", "-l /root/xmrig/build/log"));    error

Add logFile What is the specific format?


# Discussion History
## xmrig | 2018-11-05T06:54:56+00:00
Oh, you should learn C++ a little. Add new line after `m_pools.push_back`: `m_logFile = "/root/xmrig/build/log";`

# Action History
- Created by: luxig | 2018-11-02T06:17:27+00:00
- Closed at: 2018-11-05T06:54:56+00:00
