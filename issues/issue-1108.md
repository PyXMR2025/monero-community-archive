---
title: 2.99.4 does not compile on Mac
source_url: https://github.com/xmrig/xmrig/issues/1108
author: lexansoft
assignees: []
labels:
- bug
created_at: '2019-08-09T21:21:50+00:00'
updated_at: '2019-08-14T16:06:28+00:00'
type: issue
status: closed
closed_at: '2019-08-14T16:06:27+00:00'
---

# Original Description
In file included from /Users/alexnaverniuk/xmrig/src/backend/cpu/CpuBackend.cpp:43:
/Users/alexnaverniuk/xmrig/src/3rdparty/rapidjson/document.h:1680:22: error: call to constructor of
      'rapidjson::GenericValue<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator> >' is
      ambiguous
        GenericValue v(value);
                     ^ ~~~~~

# Discussion History
# Action History
- Created by: lexansoft | 2019-08-09T21:21:50+00:00
- Closed at: 2019-08-14T16:06:27+00:00
