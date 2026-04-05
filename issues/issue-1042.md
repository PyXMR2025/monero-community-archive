---
title: 32bit on linux?
source_url: https://github.com/xmrig/xmrig/issues/1042
author: genericc
assignees: []
labels:
- question
created_at: '2019-06-28T02:55:25+00:00'
updated_at: '2019-08-02T11:42:07+00:00'
type: issue
status: closed
closed_at: '2019-08-02T11:42:07+00:00'
---

# Original Description
hi is any idea about 32bit on linux? or works only on 64?thanks.

# Discussion History
## skuroedov | 2019-06-30T18:06:34+00:00
Download source and write ```cmake -DCMAKE_CXX_FLAGS=-m32 -DCMAKE_C_FLAGS=-m32 .```

# Action History
- Created by: genericc | 2019-06-28T02:55:25+00:00
- Closed at: 2019-08-02T11:42:07+00:00
