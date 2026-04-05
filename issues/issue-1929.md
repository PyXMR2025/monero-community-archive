---
title: Cannot compile without HTTP_API
source_url: https://github.com/xmrig/xmrig/issues/1929
author: danez
assignees: []
labels: []
created_at: '2020-11-04T22:47:57+00:00'
updated_at: '2020-11-05T08:49:33+00:00'
type: issue
status: closed
closed_at: '2020-11-05T08:49:33+00:00'
---

# Original Description
**Describe the bug**
When compiling without http api the compile fails

**To Reproduce**
```
cmake -DWITH_CUDA=OFF -DWITH_OPENCL=OFF -DWITH_HTTP=OFF ..
make
```

```
/opt/xmrig/src/backend/common/Benchmark.cpp: In member function ‘bool xmrig::Benchmark::finish(uint64_t)’:
/opt/xmrig/src/backend/common/Benchmark.cpp:87:68: error: ‘const class xmrig::IBackend’ has no member named ‘toJSON’
   87 |         doc.AddMember("backend",                        m_backend->toJSON(doc), allocator);
      |                                                                    ^~~~~~
make[2]: *** [CMakeFiles/xmrig.dir/build.make:778: CMakeFiles/xmrig.dir/src/backend/common/Benchmark.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:163: CMakeFiles/xmrig.dir/all] Error 2
```

**Expected behavior**
no compile error like with 6.4.0

**Required data**
 - OS: Gentoo Linux


# Discussion History
## SChernykh | 2020-11-04T23:31:53+00:00
This is fixed in the dev branch, wait for the next release.

## danez | 2020-11-05T08:49:27+00:00
Ah thanks. I'll close then

# Action History
- Created by: danez | 2020-11-04T22:47:57+00:00
- Closed at: 2020-11-05T08:49:33+00:00
