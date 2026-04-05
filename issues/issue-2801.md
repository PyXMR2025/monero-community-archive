---
title: 'Raspberry pi 4 64bit OS: c++: error: unrecognized command-line option ''-mavx2'''
source_url: https://github.com/xmrig/xmrig/issues/2801
author: get4gopim
assignees: []
labels: []
created_at: '2021-12-07T16:50:30+00:00'
updated_at: '2023-05-02T00:37:28+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**
I am trying to build xmrig from github using my Raspberry Pi 64 bit 4 GB Variant. I am getting the below error while doing cmake:

Performing C++ SOURCE FILE Test VAES_SUPPORTED failed with the following output:
Change Dir: /home/pi/xmrig/build/CMakeFiles/CMakeTmp

Run Build Command(s):/usr/bin/gmake cmTC_b5ce8/fast && /usr/bin/gmake  -f CMakeFiles/cmTC_b5ce8.dir/build.make CMakeFiles/cmTC_b5ce8.dir/build
gmake[1]: Entering directory '/home/pi/xmrig/build/CMakeFiles/CMakeTmp'
Building CXX object CMakeFiles/cmTC_b5ce8.dir/src.cxx.o
/usr/bin/c++   -DVAES_SUPPORTED   -mavx2 -mvaes -o CMakeFiles/cmTC_b5ce8.dir/src.cxx.o -c /home/pi/xmrig/build/CMakeFiles/CMakeTmp/src.cxx
c++: error: unrecognized command-line option '-mavx2'
c++: error: unrecognized command-line option '-mvaes'
gmake[1]: *** [CMakeFiles/cmTC_b5ce8.dir/build.make:85: CMakeFiles/cmTC_b5ce8.dir/src.cxx.o] Error 1
gmake[1]: Leaving directory '/home/pi/xmrig/build/CMakeFiles/CMakeTmp'
gmake: *** [Makefile:140: cmTC_b5ce8/fast] Error 2


Source file was:
int main() { return 0; }

Can some one help what I am missing ?

**To Reproduce**
System Info:
Linux pi4mine 5.10.63-v8+ #1459 SMP PREEMPT Wed Oct 6 16:42:49 BST 2021 aarch64 GNU/Linux

cat /etc/os-release 
PRETTY_NAME="Debian GNU/Linux 11 (bullseye)"
NAME="Debian GNU/Linux"
VERSION_ID="11"
VERSION="11 (bullseye)"
VERSION_CODENAME=bullseye
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"



**Expected behavior**
A clear and concise description of what you expected to happen.

**Required data**
 - OS: Raspberry Pi 64 bit 4 GB
 - 


**Additional context**
The same one is working fine in my another Raspberry Pi 8 GB version. I don't understand what i am missing. I tried reinstalling the OS several times but no luck.


# Discussion History
## kazmek | 2021-12-08T02:26:40+00:00
Verify you have 64 bit dependencies.
`sudo apt list git build-essential* cmake libuv1-dev* libssl-dev* libhwl
oc-dev* -i`

Be sure you run cmake as sudo. Also, don't forget the two periods. That tells it to jump back to the previous directory for the files. <https://xmrig.com/docs/miner/build/ubuntu>
`sudo cmake ..`

## ThanatosXingYu | 2023-05-01T01:40:35+00:00
I have run and all have installed
`sudo apt list git build-essential* cmake libuv1-dev* libssl-dev* libhwl oc-dev* -i`
Then I run`sudo cmake ..` in ./build
there's still a same error just like @get4gopim's issue.

**Error:**
-- Use ARM_TARGET=8 (aarch64)
CMake Error at /usr/share/cmake-3.18/Modules/FindPackageHandleStandardArgs.cmake:165 (message):
  Could NOT find HWLOC (missing: HWLOC_LIBRARY HWLOC_INCLUDE_DIR)
Call Stack (most recent call first):
  /usr/share/cmake-3.18/Modules/FindPackageHandleStandardArgs.cmake:458 (_FPHSA_FAILURE_MESSAGE)
  cmake/FindHWLOC.cmake:25 (find_package_handle_standard_args)
  src/backend/cpu/cpu.cmake:30 (find_package)
  src/backend/backend.cmake:1 (include)
  CMakeLists.txt:48 (include)


-- Configuring incomplete, errors occurred!
See also "/home/pi/xmrig/build/CMakeFiles/CMakeOutput.log".
See also "/home/pi/xmrig/build/CMakeFiles/CMakeError.log".

**Reproduce sys info:**
Linux raspberrypi 6.1.21-v8+ #1642 SMP PREEMPT Mon Apr  3 17:24:16 BST 2023 aarch64 GNU/Linux

PRETTY_NAME="Raspbian GNU/Linux 11 (bullseye)"
NAME="Raspbian GNU/Linux"
VERSION_ID="11"
VERSION="11 (bullseye)"
VERSION_CODENAME=bullseye
ID=raspbian
ID_LIKE=debian
HOME_URL="http://www.raspbian.org/"
SUPPORT_URL="http://www.raspbian.org/RaspbianForums"
BUG_REPORT_URL="http://www.raspbian.org/RaspbianBugs"

 I tried to reinstall this but still failed.
HOW CAN I SOVLE THIS?

## Spudz76 | 2023-05-02T00:37:28+00:00
Also need `libhwloc-dev`.  Or use `./scripts/build_deps.sh` and build all the deps with the tested versions vs whatever comes from the distribution.

# Action History
- Created by: get4gopim | 2021-12-07T16:50:30+00:00
