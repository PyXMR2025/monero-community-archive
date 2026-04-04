---
title: make command failing
source_url: https://github.com/monero-project/monero/issues/7834
author: S1700
assignees: []
labels: []
created_at: '2021-08-05T21:29:29+00:00'
updated_at: '2021-08-13T03:57:00+00:00'
type: issue
status: closed
closed_at: '2021-08-13T03:57:00+00:00'
---

# Original Description
The make commands returns this error:
```
root@rkfaucets:~/monero-pool/monero# git checkout release-v0.17
M       external/miniupnp
Already on 'release-v0.17'
Your branch is up to date with 'origin/release-v0.17'.
root@rkfaucets:~/monero-pool/monero# make
mkdir -p build/"Linux/release-v0.17"/release
cd build/"Linux/release-v0.17"/release && cmake -D BUILD_TESTS=ON -D CMAKE_BUILD_TYPE=release ../../../.. && make
/bin/sh: 1: cmake: not found
make: *** [Makefile:103: release-all] Error 127
```
Thanks

# Discussion History
## selsta | 2021-08-05T21:30:28+00:00
Did you install dependencies including cmake?

## S1700 | 2021-08-05T21:32:30+00:00
oh now that I look into the error more I see that in need to install cmake 
sorry!

## S1700 | 2021-08-05T21:33:24+00:00
ah but after installing cmake and running the command again i get a new error:
```
CMake Error at CMakeLists.txt:263 (message):
  Submodule 'external/miniupnp' is not up-to-date.  Please update all
  submodules with

  git submodule update --init --force

  or run cmake with -DMANUAL_SUBMODULES=1

Call Stack (most recent call first):
  CMakeLists.txt:268 (check_submodule)


-- Configuring incomplete, errors occurred!
See also "/root/monero-pool/monero/build/Linux/release-v0.17/release/CMakeFiles/CMakeOutput.log".
make: *** [Makefile:103: release-all] Error 1
root@rkfaucets:~/monero-pool/monero#
```
should i get the log file?

## selsta | 2021-08-05T21:34:43+00:00
Please update all submodules with:

`git submodule update --init --force`


## S1700 | 2021-08-05T21:35:57+00:00
damn got another error
```
root@rkfaucets:~/monero-pool/monero# git submodule update --init --force
fatal: remote error: upload-pack: not our ref 4c700e09526a7d546394e85628c57e9490feefa0
Fetched in submodule path 'external/miniupnp', but it did not contain 4c700e09526a7d546394e85628c57e9490feefa0. Direct fetching of that commit failed.
```

## selsta | 2021-08-05T21:36:28+00:00
git submodule sync

git submodule update --init --force

## S1700 | 2021-08-05T21:38:58+00:00
sorry to tell you but we have another
```
-- Performing Test _fstack_clash_protection_c - Success
-- Performing Test _fstack_clash_protection_cxx
-- Performing Test _fstack_clash_protection_cxx - Success
-- Looking for -pie linker flag
-- Looking for -pie linker flag - found
-- Looking for -Wl,-z,relro linker flag
-- Looking for -Wl,-z,relro linker flag - found
-- Looking for -Wl,-z,now linker flag
-- Looking for -Wl,-z,now linker flag - found
-- Looking for -Wl,-z,noexecstack linker flag
-- Looking for -Wl,-z,noexecstack linker flag - found
-- Looking for -Wl,-z,noexecheap linker flag
-- Looking for -Wl,-z,noexecheap linker flag - not found
-- Using C security hardening flags:  -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -fcf-protection=full -fstack-clash-protection
-- Using C++ security hardening flags:  -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -fcf-protection=full -fstack-clash-protection
-- Using linker security hardening flags:  -pie -Wl,-z,relro -Wl,-z,now -Wl,-z,noexecstack
CMake Warning at /usr/share/cmake-3.18/Modules/FindBoost.cmake:1187 (message):
  New Boost version may have incorrect or missing dependencies and imported
  targets
Call Stack (most recent call first):
  /usr/share/cmake-3.18/Modules/FindBoost.cmake:1311 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/share/cmake-3.18/Modules/FindBoost.cmake:1919 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:950 (find_package)


CMake Warning at /usr/share/cmake-3.18/Modules/FindBoost.cmake:1187 (message):
  New Boost version may have incorrect or missing dependencies and imported
  targets
Call Stack (most recent call first):
  /usr/share/cmake-3.18/Modules/FindBoost.cmake:1311 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/share/cmake-3.18/Modules/FindBoost.cmake:1919 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:950 (find_package)


CMake Warning at /usr/share/cmake-3.18/Modules/FindBoost.cmake:1187 (message):
  New Boost version may have incorrect or missing dependencies and imported
  targets
Call Stack (most recent call first):
  /usr/share/cmake-3.18/Modules/FindBoost.cmake:1311 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/share/cmake-3.18/Modules/FindBoost.cmake:1919 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:950 (find_package)


CMake Warning at /usr/share/cmake-3.18/Modules/FindBoost.cmake:1187 (message):
  New Boost version may have incorrect or missing dependencies and imported
  targets
Call Stack (most recent call first):
  /usr/share/cmake-3.18/Modules/FindBoost.cmake:1311 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/share/cmake-3.18/Modules/FindBoost.cmake:1919 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:950 (find_package)


CMake Warning at /usr/share/cmake-3.18/Modules/FindBoost.cmake:1187 (message):
  New Boost version may have incorrect or missing dependencies and imported
  targets
Call Stack (most recent call first):
  /usr/share/cmake-3.18/Modules/FindBoost.cmake:1311 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/share/cmake-3.18/Modules/FindBoost.cmake:1919 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:950 (find_package)


CMake Warning at /usr/share/cmake-3.18/Modules/FindBoost.cmake:1187 (message):
  New Boost version may have incorrect or missing dependencies and imported
  targets
Call Stack (most recent call first):
  /usr/share/cmake-3.18/Modules/FindBoost.cmake:1311 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/share/cmake-3.18/Modules/FindBoost.cmake:1919 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:950 (find_package)


CMake Warning at /usr/share/cmake-3.18/Modules/FindBoost.cmake:1187 (message):
  New Boost version may have incorrect or missing dependencies and imported
  targets
Call Stack (most recent call first):
  /usr/share/cmake-3.18/Modules/FindBoost.cmake:1311 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/share/cmake-3.18/Modules/FindBoost.cmake:1919 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:950 (find_package)


CMake Warning at /usr/share/cmake-3.18/Modules/FindBoost.cmake:1187 (message):
  New Boost version may have incorrect or missing dependencies and imported
  targets
Call Stack (most recent call first):
  /usr/share/cmake-3.18/Modules/FindBoost.cmake:1311 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/share/cmake-3.18/Modules/FindBoost.cmake:1919 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:950 (find_package)


CMake Warning at /usr/share/cmake-3.18/Modules/FindBoost.cmake:1187 (message):
  New Boost version may have incorrect or missing dependencies and imported
  targets
Call Stack (most recent call first):
  /usr/share/cmake-3.18/Modules/FindBoost.cmake:1311 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/share/cmake-3.18/Modules/FindBoost.cmake:1919 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:950 (find_package)


CMake Warning at /usr/share/cmake-3.18/Modules/FindBoost.cmake:1187 (message):
  New Boost version may have incorrect or missing dependencies and imported
  targets
Call Stack (most recent call first):
  /usr/share/cmake-3.18/Modules/FindBoost.cmake:1311 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/share/cmake-3.18/Modules/FindBoost.cmake:1919 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:950 (find_package)


-- Found Boost Version: 107400
-- Could NOT find Readline (missing: Readline_INCLUDE_DIR Readline_LIBRARY)
-- Looking for rl_copy_text
-- Looking for rl_copy_text - not found
-- Looking for rl_filename_completion_function
-- Looking for rl_filename_completion_function - not found
-- Looking for rl_copy_text
-- Looking for rl_copy_text - not found
-- Looking for rl_filename_completion_function
-- Looking for rl_filename_completion_function - not found
-- Could not find GNU readline library so building without readline support
CMake Error at CMakeLists.txt:1054 (message):
  Could not find required header zmq.h


-- Configuring incomplete, errors occurred!
See also "/root/monero-pool/monero/build/Linux/release-v0.17/release/CMakeFiles/CMakeOutput.log".
See also "/root/monero-pool/monero/build/Linux/release-v0.17/release/CMakeFiles/CMakeError.log".
make: *** [Makefile:103: release-all] Error 1
root@rkfaucets:~/monero-pool/monero#

```

## selsta | 2021-08-05T21:40:57+00:00
You have to follow the readme: https://github.com/monero-project/monero#cloning-the-repository

That includes installing all the dependencies, as mentioned.

## S1700 | 2021-08-05T21:42:33+00:00
damn im starting to think that its me 
```
root@rkfaucets:~/monero-pool/monero# sudo apt update && sudo apt install build-essential cmake pkg-config libssl-dev libzmq3-dev libunbound-dev libsodium-dev libunwind8-dev liblzma-dev libreadline6-dev libldns-dev libexpat1-dev libpgm-dev qttools5-dev-tools libhidapi-dev libusb-1.0-0-dev libprotobuf-dev protobuf-compiler libudev-dev libboost-chrono-dev libboost-date-time-dev libboost-filesystem-dev libboost-locale-dev libboost-program-options-dev libboost-regex-dev libboost-serialization-dev libboost-system-dev libboost-thread-dev ccache doxygen graphviz
Ign:1 http://ppa.launchpad.net/bitcoin/bitcoin/ubuntu hirsute InRelease
Err:2 http://ppa.launchpad.net/bitcoin/bitcoin/ubuntu hirsute Release
  404  Not Found [IP: 2001:67c:1560:8008::19 80]
Hit:3 http://us.archive.ubuntu.com/ubuntu hirsute InRelease
Hit:4 http://us.archive.ubuntu.com/ubuntu hirsute-updates InRelease
Hit:5 http://us.archive.ubuntu.com/ubuntu hirsute-backports InRelease
Get:6 http://us.archive.ubuntu.com/ubuntu hirsute-security InRelease [101 kB]
Reading package lists... Done
E: The repository 'http://ppa.launchpad.net/bitcoin/bitcoin/ubuntu hirsute Release' does not have a Release file.
N: Updating from such a repository can't be done securely, and is therefore disabled by default.
N: See apt-secure(8) manpage for repository creation and user configuration details.

```

## selsta | 2021-08-05T21:49:22+00:00
It's an issue with your package manager.

Try just `sudo apt install build-essential cmake pkg-config libssl-dev libzmq3-dev libunbound-dev libsodium-dev libunwind8-dev liblzma-dev libreadline6-dev libldns-dev libexpat1-dev libpgm-dev qttools5-dev-tools libhidapi-dev libusb-1.0-0-dev libprotobuf-dev protobuf-compiler libudev-dev libboost-chrono-dev libboost-date-time-dev libboost-filesystem-dev libboost-locale-dev libboost-program-options-dev libboost-regex-dev libboost-serialization-dev libboost-system-dev libboost-thread-dev ccache doxygen graphviz`

## S1700 | 2021-08-05T21:56:34+00:00
Ok it looks like its working now and i think we made the longest issue thread on this repo. Thanks so much for helping me!

## cirocosta | 2021-08-08T12:04:49+00:00
I'm glad you got it to work, @Samuel20354 ! for troubleshooting problems like this, i'd advise joining IRC/matrix channels (see https://www.getmonero.org/community/hangouts) as those are way more geared towards interactive discussions.

cheers!

## mj-xmr | 2021-08-11T13:51:56+00:00
If your issue is resolved, please close it, so that we have less to scroll, when looking for new tasks.

# Action History
- Created by: S1700 | 2021-08-05T21:29:29+00:00
- Closed at: 2021-08-13T03:57:00+00:00
