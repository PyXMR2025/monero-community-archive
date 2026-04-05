---
title: 'Build failure on ARMv7: ''vld1q_u8_x4'' was not declared in this scope; did
  you mean ''vld1q_u8''?'
source_url: https://github.com/xmrig/xmrig/issues/3143
author: benthetechguy
assignees: []
labels:
- bug
created_at: '2022-10-23T20:38:52+00:00'
updated_at: '2022-12-13T14:31:57+00:00'
type: issue
status: closed
closed_at: '2022-12-13T14:31:56+00:00'
---

# Original Description
**Describe the bug**
The build fails on ARMv7.

**To Reproduce**
1. Find a 32 bit ARM device like a Raspberry Pi 2 or make an armv7l virtual machine, and install modern Linux such as Debian testing/unstable or Arch Linux ARM.
2. Build XMRig following the normal build instructions.

**Expected behavior**
XMRig builds and runs.

**Required data**
```
In file included from /home/alarm/xmrig/src/crypto/ghostrider/ghostrider.cpp:57:
/home/alarm/xmrig/src/crypto/ghostrider/../../crypto/cn/sse2neon.h: In function 'uint8x16x4_t _sse2neon_vld1q_u8_x4(const uint8_t*)':
/home/alarm/xmrig/src/crypto/ghostrider/../../crypto/cn/sse2neon.h:363:12: error: 'vld1q_u8_x4' was not declared in this scope; did you mean 'vld1q_u8'?
  363 |     return vld1q_u8_x4(p);
      |            ^~~~~~~~~~~
      |            vld1q_u8
make[2]: *** [src/crypto/ghostrider/CMakeFiles/ghostrider.dir/build.make:300: src/crypto/ghostrider/CMakeFiles/ghostrider.dir/ghostrider.cpp.o] Error 1
```

**Additional context**
It builds and runs fine on Debian 11 (bullseye), but not rolling Debian testing or Arch Linux ARM, so this is probably the code being incompatible with newer build tools.

# Discussion History
## benthetechguy | 2022-10-23T20:52:11+00:00
Just went to check if it was the same issue I've posted three times now, but for GCC 12 (see #2876 and #2175), and of course it is. The problem is probably fixed by changing https://github.com/xmrig/xmrig/blob/28e81bd7c09c88f8dfe5ab5fb1fbd62f3bca1f8b/src/crypto/cn/sse2neon.h#L347 to use 12 instead of 11. Can't there be a better way to do this than specifying the current newest GCC version until it breaks again the next time distros update to a new major version of GCC?

## Spudz76 | 2022-10-23T21:08:11+00:00
Dunno, that file [is from here](https://github.com/DLTcollab/sse2neon) so questions about how dumb it might be should be directed over there.

## benthetechguy | 2022-10-23T21:09:22+00:00
It's still causing XMRig to fail to build on ARMv7 every time a new major version of GCC is adopted by distributions.

## Spudz76 | 2022-10-23T21:09:42+00:00
Cool.  Still not "our" file so...

## benthetechguy | 2022-10-23T21:10:45+00:00
"their" file is already fixed for GCC 12
https://github.com/DLTcollab/sse2neon/blob/c0a1262d4d797d3fd19177a7c7149f4507c44aa3/sse2neon.h#L472

## Spudz76 | 2022-10-23T21:15:06+00:00
Correct.  Someone should update the copy in this tree and submit a PR so that @SChernykh can refuse to merge it.

# Action History
- Created by: benthetechguy | 2022-10-23T20:38:52+00:00
- Closed at: 2022-12-13T14:31:56+00:00
