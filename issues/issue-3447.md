---
title: '#error "You must enable NEON instructions (e.g. -mfpu=neon-fp-armv8) to use
  SSE2NEON."'
source_url: https://github.com/xmrig/xmrig/issues/3447
author: Jamesaarr
assignees: []
labels: []
created_at: '2024-03-18T01:41:33+00:00'
updated_at: '2024-03-18T03:01:06+00:00'
type: issue
status: closed
closed_at: '2024-03-18T03:00:44+00:00'
---

# Original Description
**Describe the bug**
When I run the make command - gives the error:
```
In file included from /home/user/xmrig/src/crypto/ghostrider/ghostrider.cpp:59:
/home/user/xmrig/src/crypto/ghostrider/../../crypto/cn/sse2neon.h:231:2: error: #error "You must enable NEON instructions (e.g. -mfpu=neon-fp-armv8) to use SSE2NEON."
  231 | #error \
      |  ^~~~~
make[2]: *** [src/crypto/ghostrider/CMakeFiles/ghostrider.dir/build.make:290: src/crypto/ghostrider/CMakeFiles/ghostrider.dir/ghostrider.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:240: src/crypto/ghostrider/CMakeFiles/ghostrider.dir/all] Error 2
make: *** [Makefile:103: all] Error 2
```


**To Reproduce**
I have built and ran cmake .. commands - but when running the make command - gives above error 

I've verified I'm using 64bit OS

**Expected behavior**
I expect it to run through the make process

**Required data**
 - OS: [e.g. Windows]  Raspian Bullseye aarch64


**Additional context**
Not sure what info is required


# Discussion History
## Jamesaarr | 2024-03-18T03:01:04+00:00
For peoples info - I just reinstalled the Pi OS and it worked on the new attempt 

# Action History
- Created by: Jamesaarr | 2024-03-18T01:41:33+00:00
- Closed at: 2024-03-18T03:00:44+00:00
