---
title: Unable to compile RxDataset.cpp on ARMv8 NanoPI NEO2 board with Armbian Focal
source_url: https://github.com/xmrig/xmrig/issues/1825
author: OTLabs
assignees: []
labels:
- bug
- arm
created_at: '2020-09-06T05:11:54+00:00'
updated_at: '2021-04-12T14:49:37+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:49:37+00:00'
---

# Original Description
**Describe the bug**
I get `c++: fatal error: Killed signal terminated program cc1plus compilation terminated.` while compiling RxDataset.cpp on ARMv8 NanoPi NEO2 board with Armbian Focal.

**To Reproduce**
```
cmake ..
make
```

**Expected behavior**
Successful compilation.

**Required data**
```
otlabs@nanopineo2:~/xmrig-6.3.3/build$ uname -a
Linux nanopineo2 5.8.6-sunxi64 #20.08.2 SMP Fri Sep 4 08:52:31 CEST 2020 aarch64 aarch64 aarch64 GNU/Linux
otlabs@nanopineo2:~/xmrig-6.3.3/build$ free
              total        used        free      shared  buff/cache   available
Mem:        1009396       90476      861708         476       57212      856288
Swap:        504696       41772      462924
```

**Additional context**
```
otlabs@nanopineo2:~/xmrig-6.3.3/build$ cmake ..
-- The C compiler identification is GNU 9.3.0
-- The CXX compiler identification is GNU 9.3.0
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Use ARM_TARGET=8 (aarch64)
-- Performing Test XMRIG_ARM_CRYPTO
-- Performing Test XMRIG_ARM_CRYPTO - Success
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Found HWLOC: /usr/lib/aarch64-linux-gnu/libhwloc.so  
-- Found UV: /usr/lib/aarch64-linux-gnu/libuv.a  
-- Looking for __builtin___clear_cache
-- Looking for __builtin___clear_cache - found
-- WITH_MSR=OFF
-- Found OpenSSL: /usr/lib/aarch64-linux-gnu/libcrypto.so (found version "1.1.1f")  
-- Configuring done
-- Generating done
-- Build files have been written to: /home/otlabs/xmrig-6.3.3/build

otlabs@nanopineo2:~/xmrig-6.3.3/build$ make
Scanning dependencies of target ethash
[  1%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.o
...
[ 90%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxCache.cpp.o
[ 90%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxConfig.cpp.o
[ 91%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxDataset.cpp.o
c++: fatal error: Killed signal terminated program cc1plus
compilation terminated.
make[2]: *** [CMakeFiles/xmrig.dir/build.make:2546: CMakeFiles/xmrig.dir/src/crypto/rx/RxDataset.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:118: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:84: all] Error 2
```


# Discussion History
## xmrig | 2020-09-06T11:24:57+00:00
Not enough memory, compiler was killed by OOM killer, anyway 1 GB of memory not enough to mine RandomX in full memory mode, if you looking for other algorithms you can disable RandomX by `cmake .. -DWITH_RANDOMX=OFF`.
Thank you.

## OTLabs | 2020-09-06T19:31:31+00:00
Thank you! The build was successful in this case!

Do you have any estimate how much memory could be enough to build RxDataset.cpp?

## woodycal | 2020-10-01T19:31:33+00:00
Hi getting same error with focal but i am using a khadas vim3 4gb which works fine in bionic with randomx on arqma but when i try build the same xmrig miner on focal i get the below error. Is their a precompiled version for arm?

cc1plus: out of memory allocating 5190462000 bytes after a total of 1040551936 bytes
make[2]: *** [CMakeFiles/xmrig.dir/build.make:2546: CMakeFiles/xmrig.dir/src/crypto/rx/RxDataset.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:118: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:84: all] Error 2

@Khadas:~/xmrig/build$ free
              total        used        free      shared  buff/cache   available
Mem:        3846004      150828     3303516        6036      391660     3647920
Swap:       1048560           0     1048560






## OTLabs | 2020-10-01T20:29:40+00:00
Does it mean I need about 6GB to compile it?

## woodycal | 2020-10-02T19:15:58+00:00
> Does it mean I need about 6GB to compile it?

Hope not myself. Reverted back to bionic in mean time till a solution.

## xmrig | 2020-11-02T12:59:52+00:00
This issue should be fixed in dev branch https://github.com/xmrig/xmrig/pull/1926
Thank you.

## OTLabs | 2020-11-08T22:38:59+00:00
@xmrig Thanks a lot! Worked like a charm!

# Action History
- Created by: OTLabs | 2020-09-06T05:11:54+00:00
- Closed at: 2021-04-12T14:49:37+00:00
