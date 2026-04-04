---
title: Error building RandomX in a RPi
source_url: https://github.com/monero-project/monero/issues/6784
author: vdo
assignees: []
labels: []
created_at: '2020-08-27T15:02:58+00:00'
updated_at: '2021-09-29T10:14:00+00:00'
type: issue
status: closed
closed_at: '2021-09-29T10:14:00+00:00'
---

# Original Description
I get this error when building with a adapted Dockerfile the version `v0.16.0.3` in a Raspberry Pi 4:
```
[ 25%] Building CXX object external/randomx/CMakeFiles/randomx.dir/src/aes_hash.cpp.o
In file included from /src/external/randomx/src/soft_aes.h:32:0,
                 from /src/external/randomx/src/aes_hash.cpp:29:
/src/external/randomx/src/intrin_portable.h: In function 'rx_vec_f128 rx_swap_vec_f128(rx_vec_f128)':
/src/external/randomx/src/intrin_portable.h:412:39: error: 'vcopyq_laneq_f64' was not declared in this scope
  temp = vcopyq_laneq_f64(temp, 1, a, 1);
                                       ^
/src/external/randomx/src/intrin_portable.h: In function 'rx_vec_f128 rx_set_vec_f128(uint64_t, uint64_t)':
/src/external/randomx/src/intrin_portable.h:420:66: error: 'vcopyq_laneq_u64' was not declared in this scope
  return vreinterpretq_f64_u64(vcopyq_laneq_u64(temp0, 1, temp1, 0));
                                                                  ^
make[3]: *** [external/randomx/CMakeFiles/randomx.dir/src/aes_hash.cpp.o] Error 1
external/randomx/CMakeFiles/randomx.dir/build.make:62: recipe for target 'external/randomx/CMakeFiles/randomx.dir/src/aes_hash.cpp.o' failed
make[3]: Leaving directory '/src/build/release'
make[2]: *** [external/randomx/CMakeFiles/randomx.dir/all] Error 2
make[2]: *** Waiting for unfinished jobs....
```

I tried adding the `-D NO_AES=ON` flag to the Makefile line but I get the same result.

# Discussion History
## selsta | 2020-08-27T15:04:18+00:00
Which GCC version?

## vdo | 2020-08-27T15:12:07+00:00
I'm using the Dockerfile provided, with few changes for aarch64 compilation
```
-- CMake version 3.14.6
-- The C compiler identification is GNU 5.4.0
-- The CXX compiler identification is GNU 5.4.0
```
I also added to the CXXFLAGS: `-std=c++11`


## vdo | 2020-08-27T15:32:38+00:00
Ok I saw your comment on another issue:
https://github.com/monero-project/monero/issues/6483#issuecomment-620120754

Looks like the base image is outdated... trying with a newer one

## Gingeropolous | 2021-03-31T03:24:53+00:00
@vdo, did it work? 

# Action History
- Created by: vdo | 2020-08-27T15:02:58+00:00
- Closed at: 2021-09-29T10:14:00+00:00
