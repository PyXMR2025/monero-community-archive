---
title: What happened to options.cpp?
source_url: https://github.com/xmrig/xmrig/issues/726
author: lolcocks123
assignees: []
labels:
- question
created_at: '2018-07-26T10:20:31+00:00'
updated_at: '2018-10-10T22:20:33+00:00'
type: issue
status: closed
closed_at: '2018-10-10T22:20:33+00:00'
---

# Original Description
Hello,

I am coming back to this project after a long time.

I remember there was an options.cpp file where in I used to add multiple pools as follows:

```
m_pools.push_back(new Url("monerohash.com", 3333, "ExampleAddress", "x", false, true));

m_pools.push_back(new Url("pool.minexmr.com", 4444, "ExampleAddress", "x", false, true));

m_pools.push_back(new Url("xmr.prohash.net", 2222, "ExampleAddress", "x", false, true));

```


How can I achieve this once again?

# Discussion History
## xmrig | 2018-07-26T19:20:53+00:00
https://github.com/xmrig/xmrig/issues/608#issuecomment-386882513
Also instead of `new Url(` use just `Pool(`. Thank you.

# Action History
- Created by: lolcocks123 | 2018-07-26T10:20:31+00:00
- Closed at: 2018-10-10T22:20:33+00:00
