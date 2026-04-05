---
title: Problems making XMRig in Raspberry PI
source_url: https://github.com/xmrig/xmrig/issues/2281
author: fintan226
assignees: []
labels: []
created_at: '2021-04-18T22:56:11+00:00'
updated_at: '2021-04-20T10:54:08+00:00'
type: issue
status: closed
closed_at: '2021-04-20T10:54:03+00:00'
---

# Original Description
/home/pi/xmrig/src/crypto/cn/sse2neon.h:122:2: error: #error "Unsupported tar. Must be either ARMv7-A+NEON or ARMv8-A."
 #error "Unsupported target. Must be either ARMv7-A+NEON or ARMv8-A."
  ^~~~~
^Cmake[2]: *** [CMakeFiles/xmrig.dir/build.make:2403: CMakeFiles/xmrig.dir/srrypto/cn/CnHash.cpp.o] Interrupt
make[1]: *** [CMakeFiles/Makefile2:118: CMakeFiles/xmrig.dir/all] Interrupt
make: *** [Makefile:84: all] Interrupt
This is the error I get when trying to make XMRig.

# Discussion History
## SChernykh | 2021-04-20T06:59:54+00:00
`#error "Unsupported target. Must be either ARMv7-A+NEON or ARMv8-A."`
Compile for ARMv8-A - install 64-bit Linux and 64-bit compiler.

# Action History
- Created by: fintan226 | 2021-04-18T22:56:11+00:00
- Closed at: 2021-04-20T10:54:03+00:00
