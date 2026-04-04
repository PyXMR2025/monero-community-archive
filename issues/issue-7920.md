---
title: Error Building on Mac M1
source_url: https://github.com/monero-project/monero/issues/7920
author: wwessex
assignees: []
labels: []
created_at: '2021-09-06T14:24:46+00:00'
updated_at: '2021-10-06T02:22:20+00:00'
type: issue
status: closed
closed_at: '2021-10-06T02:22:20+00:00'
---

# Original Description
Error: 
"[ 16%] Built target obj_cncrypto
[ 16%] Building CXX object src/device/CMakeFiles/obj_device.dir/device_default.cpp.o
[ 16%] Built target obj_ringct
[ 16%] Building CXX object src/device/CMakeFiles/obj_device.dir/log.cpp.o
[ 16%] Building CXX object src/device/CMakeFiles/obj_device.dir/device_ledger.cpp.o
[ 17%] Building CXX object src/device/CMakeFiles/obj_device.dir/device_io_hid.cpp.o
[ 17%] Built target obj_ringct_basic
[ 17%] Built target obj_device
make[1]: *** [all] Error 2
make: *** [release-all] Error 2"


# Discussion History
## hyc | 2021-09-06T14:44:00+00:00
Builds fine on my M1 Macbook Pro. Looks like you need to provide more of the build output since there are no actual build error messages in the above.

I note that even though it builds fine and runs, it is plagued with connection hangs and unexplained disconnects. I don't recommend running monerod on this platform, it's a waste of time.

## wwessex | 2021-09-06T16:01:34+00:00
Sorry here is the rest of it:
"-- Configuring done
CMake Warning (dev) at src/CMakeLists.txt:93 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /Users/williamwinter/p2pool/build/monero/src/rpc/instanciations.cpp
Call Stack (most recent call first):
  src/CMakeLists.txt:81 (monero_add_library_with_deps)
  src/rpc/CMakeLists.txt:101 (monero_add_library)
This warning is for project developers.  Use -Wno-dev to suppress it.

-- Generating done
-- Build files have been written to: /Users/williamwinter/p2pool/build/monero/build/Darwin/p2pool-api-v0.17/release
Consolidate compiler generated dependencies of target libminiupnpc-static
Consolidate compiler generated dependencies of target lmdb
[  1%] Built target generate_translations_header
Consolidate compiler generated dependencies of target obj_cncrypto
[  1%] Building CXX object external/qrcodegen/CMakeFiles/qrcodegen.dir/QrCode.cpp.o
[  1%] Built target genversion
Consolidate compiler generated dependencies of target randomx
[  1%] Built target lmdb
[  4%] Built target libminiupnpc-static
Consolidate compiler generated dependencies of target obj_ringct
clang: error: the clang compiler does not support '-march=x86-64'
make[3]: *** [external/qrcodegen/CMakeFiles/qrcodegen.dir/QrCode.cpp.o] Error 1
make[2]: *** [external/qrcodegen/CMakeFiles/qrcodegen.dir/all] Error 2
make[2]: *** Waiting for unfinished jobs....
Consolidate compiler generated dependencies of target obj_ringct_basic
[  4%] Building CXX object external/easylogging++/CMakeFiles/easylogging.dir/easylogging++.cc.o
Consolidate compiler generated dependencies of target obj_cryptonote_format_utils_basic
Consolidate compiler generated dependencies of target obj_device
clang: error: the clang compiler does not support '-march=x86-64'
[ 10%] Built target randomx
make[3]: *** [external/easylogging++/CMakeFiles/easylogging.dir/easylogging++.cc.o] Error 1
make[2]: *** [external/easylogging++/CMakeFiles/easylogging.dir/all] Error 2
[ 15%] Built target obj_cncrypto
[ 15%] Built target obj_ringct
[ 15%] Built target obj_cryptonote_format_utils_basic
[ 16%] Built target obj_ringct_basic
[ 17%] Built target obj_device
make[1]: *** [all] Error 2
make: *** [release-all] Error 2
"

## hyc | 2021-09-06T16:19:53+00:00
What version are you trying to build? You're missing this patch 1ac7134832b8daaa8a04e7b1cad1b38d41e21a84 which was written back in March.

## selsta | 2021-10-06T02:22:20+00:00
Build master or manually apply the patch from hyc's comment.

It should be included in the next release: #7997

# Action History
- Created by: wwessex | 2021-09-06T14:24:46+00:00
- Closed at: 2021-10-06T02:22:20+00:00
