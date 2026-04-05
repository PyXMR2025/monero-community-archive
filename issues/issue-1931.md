---
title: compilation fails for xmrig-6.5.0
source_url: https://github.com/xmrig/xmrig/issues/1931
author: jfikar
assignees: []
labels:
- bug
created_at: '2020-11-06T17:48:23+00:00'
updated_at: '2020-11-08T14:02:01+00:00'
type: issue
status: closed
closed_at: '2020-11-08T14:02:01+00:00'
---

# Original Description
Compilation of xmrig-6.5.0 fails with:

```
~/test/xmrig-6.5.0/src/backend/common/Benchmark.cpp: In member function 'bool xmrig::Benchmark::finish(uint64_t)':
~/test/xmrig-6.5.0/src/backend/common/Benchmark.cpp:87:68: error: 'const class xmrig::IBackend' has no member named 'toJSON'
   87 |         doc.AddMember("backend",                        m_backend->toJSON(doc), allocator);
      |                                                                    ^~~~~~
make[2]: *** [CMakeFiles/xmrig.dir/build.make:798: CMakeFiles/xmrig.dir/src/backend/common/Benchmark.cpp.o] Error 1
```

Probably some small typo in the new benchmark code?


# Discussion History
## xmrig | 2020-11-06T17:50:31+00:00
#1929 

## jfikar | 2020-11-06T19:26:30+00:00
I see. I've used the dev branch and it works, including the 1G huge pages on ARM. Good job!

## xmrig | 2020-11-08T14:02:01+00:00
https://github.com/xmrig/xmrig/releases/tag/v6.5.1

# Action History
- Created by: jfikar | 2020-11-06T17:48:23+00:00
- Closed at: 2020-11-08T14:02:01+00:00
