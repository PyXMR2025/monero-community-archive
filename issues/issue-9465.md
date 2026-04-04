---
title: 'error: static assertion failed due to requirement ''std::is_pod<boost::uuids::uuid>::value'':
  t_type must be a POD type on mac mini'
source_url: https://github.com/monero-project/monero/issues/9465
author: R0BC0D3R
assignees: []
labels: []
created_at: '2024-08-30T16:04:22+00:00'
updated_at: '2024-09-01T01:30:41+00:00'
type: issue
status: closed
closed_at: '2024-08-30T16:46:30+00:00'
---

# Original Description
I have newly restored Mac mini that's running Sonoma 14.6.1. I get below error when trying to compile release-v0.18:
```
[ 41%] Linking CXX static library libcheckpoints.a
[ 41%] Built target checkpoints
[ 41%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/account.cpp.o
[ 41%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/connection_context.cpp.o
In file included from /Users/devmac/monero/src/cryptonote_basic/connection_context.cpp:33:
/Users/devmac/monero/src/p2p/p2p_protocol_defs.h:195:7: error: static assertion failed due to requirement 'std::is_pod<boost::uuids::uuid>::value': t_type must be a POD type.
      KV_SERIALIZE_VAL_POD_AS_BLOB(network_id)
      ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/Users/devmac/monero/contrib/epee/include/serialization/keyvalue_serialization.h:119:59: note: expanded from macro 'KV_SERIALIZE_VAL_POD_AS_BLOB'
#define KV_SERIALIZE_VAL_POD_AS_BLOB(varialble)           KV_SERIALIZE_VAL_POD_AS_BLOB_N(varialble, #varialble)
                                                          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/Users/devmac/monero/contrib/epee/include/serialization/keyvalue_serialization.h:102:3: note: expanded from macro 'KV_SERIALIZE_VAL_POD_AS_BLOB_N'
  static_assert(std::is_pod<decltype(this_ref.varialble)>::value, "t_type must be a POD type."); \
  ^             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

Some more info:
```
devmac@Roberts-Mac-mini monero % git checkout release-v0.18
M external/trezor-common
branch 'release-v0.18' set up to track 'origin/release-v0.18'.
Switched to a new branch 'release-v0.18'
devmac@Roberts-Mac-mini monero % make
mkdir -p build/"Darwin/release-v0.18"/release
cd build/"Darwin/release-v0.18"/release && cmake -D BUILD_TESTS=ON -D CMAKE_BUILD_TYPE=Release ../../../.. && /Library/Developer/CommandLineTools/usr/bin/make

-- Found PythonInterp: /opt/homebrew/bin/python3.12 (found version "3.12.5")
-- CMake version 3.30.3
-- The C compiler identification is AppleClang 15.0.0.15000309
-- The CXX compiler identification is AppleClang 15.0.0.15000309
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done

-- Building on arm64 for armv8-a
-- Checking to see if CXX compiler accepts flag -march=armv8-a+crypto
-- Checking to see if CXX compiler accepts flag -march=armv8-a+crypto - yes
-- Crypto extensions enabled for ARMv8

-- Found Boost Version: 108600
-- Found Doxygen: /opt/homebrew/bin/doxygen (found version "1.12.0") found components: doxygen dot
-- The C compiler identification is AppleClang 15.0.0.15000309
-- The CXX compiler identification is AppleClang 15.0.0.15000309
```

I can provide entire output if needed. I did get some errors with running brew file. Screenshot attached.

![mac_mini_build_failed_error](https://github.com/user-attachments/assets/1cd649ce-a77e-4bc9-872b-a61c47a11f10)
![mac_mini_build_failed_brewfile](https://github.com/user-attachments/assets/503711bb-3411-413e-b099-dcb297fdbc75)


# Discussion History
## selsta | 2024-08-30T16:05:50+00:00
Please see

#9450
#9462

## R0BC0D3R | 2024-08-30T16:46:16+00:00
Thank you! Pulled fix_kvser_boost_158_18 branch from:

#9462 

And I was able to build successfully. Marking as closed.

## preland | 2024-09-01T01:30:41+00:00
Is it correct to close the issue before the PR is merged?

(I also just ran into this exact issue while building monero-cpp)

# Action History
- Created by: R0BC0D3R | 2024-08-30T16:04:22+00:00
- Closed at: 2024-08-30T16:46:30+00:00
