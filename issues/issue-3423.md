---
title: Compile error ubuntu 22.04, recompile with fpie
source_url: https://github.com/xmrig/xmrig/issues/3423
author: dcutugno
assignees: []
labels: []
created_at: '2024-02-17T14:45:48+00:00'
updated_at: '2025-06-16T19:47:18+00:00'
type: issue
status: closed
closed_at: '2025-06-16T19:47:18+00:00'
---

# Original Description
When I try to compile I get this error at the end:

100%] Linking CXX executable xmrig
/usr/bin/ld: CMakeFiles/xmrig.dir/src/base/tools/cryptonote/crypto-ops.c.o: relocation R_X86_64_32S against symbol `ge_base' can not be used when making a PIE object; recompile with -fPIE
/usr/bin/ld: failed to set dynamic section sizes: bad value
collect2: error: ld returned 1 exit status
make[2]: *** [CMakeFiles/xmrig.dir/build.make:3856: xmrig] Error 1
make[1]: *** [CMakeFiles/Makefile2:182: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:91: all] Error 2

# Discussion History
## SChernykh | 2024-02-17T19:27:09+00:00
How exactly did you compile it? Did you follow instructions from https://xmrig.com/docs/miner/build/ubuntu ? If yes, was it basic or advanced build instructions?

## dcutugno | 2024-02-17T19:38:39+00:00
Yes followed both basic and advanced 

## dcutugno | 2024-02-18T22:46:01+00:00
An update to this issue, the error was due to have installed from source gcc 13.0.1 experimental, now reverting back to gcc 11 it compiled fine with basic and advanced, I will try switching to most recent gcc with update-alternatives and recompile it...
Built fine with 13.1

# Action History
- Created by: dcutugno | 2024-02-17T14:45:48+00:00
- Closed at: 2025-06-16T19:47:18+00:00
