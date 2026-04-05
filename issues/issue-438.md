---
title: Memory release size in Mem_unix.cpp does not take into account doubleHash
source_url: https://github.com/xmrig/xmrig/issues/438
author: ehoffman2
assignees: []
labels:
- bug
created_at: '2018-03-12T00:24:36+00:00'
updated_at: '2018-03-13T14:01:41+00:00'
type: issue
status: closed
closed_at: '2018-03-13T14:01:41+00:00'
---

# Original Description
In Mem_unix.cpp, you have Mem::allocate(), which allocate memory taking into account doubleHash:

```
const int ratio   = (doubleHash && algo != Options::ALGO_CRYPTONIGHT_LITE) ? 2 : 1;
const size_t size = MEMORY * (threads * ratio + 1);
...
mmap(0, size,...
madvise(m_memory, size,...
mlock(m_memory, size,...
```

However, in the corresponding Mem::release() function, the doubleHash is not took into account:

```
const int size = MEMORY * (m_threads + 1);
...
munlock(m_memory, size);
munmap(m_memory, size);
...
```

Regards,
Eric


# Discussion History
## xmrig | 2018-03-13T14:01:41+00:00
Fixed.

# Action History
- Created by: ehoffman2 | 2018-03-12T00:24:36+00:00
- Closed at: 2018-03-13T14:01:41+00:00
