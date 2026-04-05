---
title: Bug in L2 Exclusive Logic in optimalThreadsCount?
source_url: https://github.com/xmrig/xmrig/issues/1025
author: brandonlehmann
assignees: []
labels:
- question
created_at: '2019-05-28T13:05:54+00:00'
updated_at: '2019-08-02T11:47:01+00:00'
type: issue
status: closed
closed_at: '2019-08-02T11:47:00+00:00'
---

# Original Description
https://github.com/xmrig/xmrig/blob/1d4bc030fb4ccb366765cd4feb31b95ebd9db9a5/src/core/cpu/AdvancedCpuInfo.cpp#L100

If I'm reading this correctly, shouldn't this be `cache = m_L2_exclusive ? m_L2 : (m_L2 + m_L3);` ?

# Discussion History
## xmrig | 2019-08-02T11:47:00+00:00
It's correct if L2 cache exclusive, we can sum L2 and L3, otherwise effective cache size limited to L3 size.
Thank you.

# Action History
- Created by: brandonlehmann | 2019-05-28T13:05:54+00:00
- Closed at: 2019-08-02T11:47:00+00:00
