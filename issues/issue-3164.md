---
title: Docker build not working
source_url: https://github.com/monero-project/monero/issues/3164
author: dahormez
assignees: []
labels: []
created_at: '2018-01-21T02:48:24+00:00'
updated_at: '2018-02-18T19:29:10+00:00'
type: issue
status: closed
closed_at: '2018-02-18T19:29:10+00:00'
---

# Original Description
Docker build currently not working in master branch
- macos high sierra 10.13.2

```
[ 93%] Linking CXX executable ../../bin/monero-blockchain-export
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libboost_filesystem.a(operations.o): relocation R_X86_64_32 against `.rodata.str1.1' can not be used when making a shared object; recompile with -fPIC
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libboost_filesystem.a: error adding symbols: Bad value
collect2: error: ld returned 1 exit status
src/blockchain_utilities/CMakeFiles/blockchain_export.dir/build.make:179: recipe for target 'bin/monero-blockchain-export' failed
make[3]: *** [bin/monero-blockchain-export] Error 1
```
```
[ 94%] Linking CXX executable ../../bin/monero-blockchain-import
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libboost_filesystem.a(operations.o): relocation R_X86_64_32 against `.rodata.str1.1' can not be used when making a shared object; recompile with -fPIC
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libboost_filesystem.a: error adding symbols: Bad value
collect2: error: ld returned 1 exit status
```

# Discussion History
## moneromooo-monero | 2018-01-21T10:48:32+00:00
You (or whoever writes the docker config) need to have static boost libs built with -fPIC, or link against boost dynamically.

## moneromooo-monero | 2018-02-18T19:22:09+00:00
+resolved

# Action History
- Created by: dahormez | 2018-01-21T02:48:24+00:00
- Closed at: 2018-02-18T19:29:10+00:00
