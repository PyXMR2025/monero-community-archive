---
title: Help with the donation connection
source_url: https://github.com/xmrig/xmrig/issues/604
author: focaeppe
assignees: []
labels: []
created_at: '2018-05-05T17:57:02+00:00'
updated_at: '2018-05-06T06:59:49+00:00'
type: issue
status: closed
closed_at: '2018-05-06T06:59:49+00:00'
---

# Original Description
Hello,
I would like to point the donation server to my proxy server ,I have changed the address from (DonateStrategy) but no luck it doesn't connect to my proxy
I also reduced the time : 
idle(m_idleTime * randomf(0.5, 1.5)); to (0.05, 0.15)) for quick time to test it out
I'm not sure if it correct what i did or no

m_donateTime(level * 60 * 1000),
m_idleTime((100 - level) * 60 * 1000),
m_strategy(nullptr),
m_listener(listener)
How it calculate ?

Thank you

# Discussion History
# Action History
- Created by: focaeppe | 2018-05-05T17:57:02+00:00
- Closed at: 2018-05-06T06:59:49+00:00
