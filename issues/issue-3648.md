---
title: Error during installation on ARM
source_url: https://github.com/xmrig/xmrig/issues/3648
author: Mail-Critic
assignees: []
labels:
- arm
created_at: '2025-03-27T13:53:47+00:00'
updated_at: '2025-06-16T15:13:56+00:00'
type: issue
status: closed
closed_at: '2025-06-16T15:13:56+00:00'
---

# Original Description
**Describe the bug**
While making I'm getting the following error.
[  0%] Building CXX object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/ghostrider.cpp.o
In file included from /home/musicbox/xmrig/src/crypto/ghostrider/ghostrider.cpp:59:
/home/musicbox/xmrig/src/crypto/ghostrider/../../crypto/cn/sse2neon.h:231:2: error: #error "You must enable NEON instructions (e.g. -mfpu=neon-fp-armv8) to use SSE2NEON."
  231 | #error \
      |  ^~~~~
make[2]: *** [src/crypto/ghostrider/CMakeFiles/ghostrider.dir/build.make:290: src/crypto/ghostrider/CMakeFiles/ghostrider.dir/ghostrider.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:240: src/crypto/ghostrider/CMakeFiles/ghostrider.dir/all] Error 2
make: *** [Makefile:103: all] Error 2

**To Reproduce**
All I have is a default raspbian os (bullseye) in a pi4

**Expected behavior**
As per the gudelines I have downloaded the rep from the current release and built it with no errors using cmake. But when it comes to make it was creating the following error.  

**Required data**
 - XMRig version
    - https://github.com/xmrig/xmrig/
 - [  0%] Building CXX object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/ghostrider.cpp.o
In file included from /home/musicbox/xmrig/src/crypto/ghostrider/ghostrider.cpp:59:
/home/musicbox/xmrig/src/crypto/ghostrider/../../crypto/cn/sse2neon.h:231:2: error: #error "You must enable NEON instructions (e.g. -mfpu=neon-fp-armv8) to use SSE2NEON."
  231 | #error \
      |  ^~~~~
make[2]: *** [src/crypto/ghostrider/CMakeFiles/ghostrider.dir/build.make:290: src/crypto/ghostrider/CMakeFiles/ghostrider.dir/ghostrider.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:240: src/crypto/ghostrider/CMakeFiles/ghostrider.dir/all] Error 2
make: *** [Makefile:103: all] Error 2

 -Issue falls here make -j$(nproc)
 - OS:Raspbian
 


# Discussion History
## SChernykh | 2025-03-27T14:48:14+00:00
> All I have is a default raspbian os (bullseye) in a pi4

Is it 64-bit? IIRC it only compiles fine on a 64-bit ARM OS.

## Mail-Critic | 2025-03-27T20:30:33+00:00
getconf LONG_BIT
It's a 32 bit version

cat /etc/os-release
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


## SChernykh | 2025-03-28T07:43:41+00:00
You need to install 64-bit Raspbian.

# Action History
- Created by: Mail-Critic | 2025-03-27T13:53:47+00:00
- Closed at: 2025-06-16T15:13:56+00:00
