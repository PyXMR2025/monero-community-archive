---
title: How do I write the configuration information directly in the source code?
source_url: https://github.com/xmrig/xmrig/issues/837
author: ttsite
assignees: []
labels: []
created_at: '2018-10-23T01:15:36+00:00'
updated_at: '2018-10-23T11:25:21+00:00'
type: issue
status: closed
closed_at: '2018-10-23T11:25:21+00:00'
---

# Original Description
I remember that there was a special place where the configuration information was written, and now I don't know where to write it. Are there any friends who can give an example to see? Thank you.
Previous writing is written in Options code.
m_pools.push_back(new Url("POOL ADDRESS", PORT, "WALLET", "PASSWORD"));

# Discussion History
## xxaamm | 2018-10-23T02:16:12+00:00
Here it is:
https://github.com/xmrig/xmrig/blob/2b0b71b9f695466f8b434fbbbcbfecfb3f9ecd60/src/common/config/CommonConfig.cpp#L89


## ttsite | 2018-10-23T02:44:19+00:00
Thank you very much.

# Action History
- Created by: ttsite | 2018-10-23T01:15:36+00:00
- Closed at: 2018-10-23T11:25:21+00:00
