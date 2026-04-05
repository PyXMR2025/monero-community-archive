---
title: Build fails with -DWITH_LIBCPUID=OFF
source_url: https://github.com/xmrig/xmrig/issues/615
author: esfomeado
assignees: []
labels:
- bug
created_at: '2018-05-07T10:56:05+00:00'
updated_at: '2018-05-07T23:19:35+00:00'
type: issue
status: closed
closed_at: '2018-05-07T23:19:35+00:00'
---

# Original Description
When building on Windows the 2.6.2 version with the flag -DWITH_LIBCPUID=OFF gives the following errors:

```
\src\cpu_stub.cpp(113): error C2371: 'm_totalThreads': redefinition; different basic types
\src\cpu.h(62): note: see declaration of 'm_totalThreads'
\src\cpu_stub.cpp(117): error C2511: 'int Cpu::optimalThreadsCount(int,bool,int)': overloaded member function not found in 'Cpu'
\src\cpu.h(32): note: see declaration of 'Cpu'


# Discussion History
## xmrig | 2018-05-07T23:19:35+00:00
Fixed. Thank you.

# Action History
- Created by: esfomeado | 2018-05-07T10:56:05+00:00
- Closed at: 2018-05-07T23:19:35+00:00
