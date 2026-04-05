---
title: Direct reading of mining information in v2.13.0
source_url: https://github.com/xmrig/xmrig/issues/941
author: ttsite
assignees: []
labels:
- question
created_at: '2019-02-22T08:38:29+00:00'
updated_at: '2019-04-06T12:51:17+00:00'
type: issue
status: closed
closed_at: '2019-02-23T05:06:00+00:00'
---

# Original Description
How do v2.13.0 want to write its own mine information directly in the source code? Where should it be written? Are there any specific samples? Thank you!

# Discussion History
## xmrig | 2019-02-22T10:30:44+00:00
Please better explain what exactly you need.
Thank you.

## ttsite | 2019-02-22T10:38:12+00:00
> Please better explain what exactly you need.
> Thank you.

I want to write my mine wallet and other information directly into the source code where to write in the new version, the previous version I remember written in commonconfig. CPP format as follows
m_pools.push_back(Pool("POOL ADDRESS", "PORT", "WALLET", "PASSWORD");
Now the new v2.13.0 does not know how to write, thank you!!!


## xmrig | 2019-02-23T02:48:01+00:00
I forgot about that use case, now code should looks like:
`m_data.push_back(Pool("POOL ADDRESS", 3333, "WALLET", "PASSWORD"));` m_pools replaced to m_data and located into Pools.cpp https://github.com/xmrig/xmrig/blob/master/src/base/net/Pools.cpp#L36

## ttsite | 2019-02-23T03:28:33+00:00
Thanks very much!!

## MasterDeflate | 2019-02-27T21:57:19+00:00
I tried this but fail i replace m_data.push_back as you said to Pools.cpp but when i run the xmrig after compile finish it ask me for config.json

## sailei00 | 2019-04-06T12:51:16+00:00
> I tried this but fail i replace m_data.push_back as you said to Pools.cpp but when i run the xmrig after compile finish it ask me for config.json

I have the same problem. Have you solved it?

# Action History
- Created by: ttsite | 2019-02-22T08:38:29+00:00
- Closed at: 2019-02-23T05:06:00+00:00
