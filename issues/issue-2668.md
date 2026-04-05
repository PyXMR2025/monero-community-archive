---
title: AstroBWT.cpp warning!
source_url: https://github.com/xmrig/xmrig/issues/2668
author: snipeTR
assignees: []
labels: []
created_at: '2021-11-02T20:11:57+00:00'
updated_at: '2021-11-02T21:12:48+00:00'
type: issue
status: closed
closed_at: '2021-11-02T21:12:48+00:00'
---

# Original Description
[ 95%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/astrobwt/AstroBWT.cpp.obj
C:/msys32/home/cxz/xmrig-6.15.3/src/crypto/astrobwt/AstroBWT.cpp:80:13: warning: 'void Salsa20_XORKeyStream_AVX256(const void*, void*, size_t)' defined but not used [-Wunused-function]
   80 | static void Salsa20_XORKeyStream_AVX256(const void* key, void* output, size_t size)

# Discussion History
## SChernykh | 2021-11-02T20:17:54+00:00
Because it's only enabled in 64-bit builds and you're building 32-bit binary in msys32. It's just a warning, so not a problem.

# Action History
- Created by: snipeTR | 2021-11-02T20:11:57+00:00
- Closed at: 2021-11-02T21:12:48+00:00
