---
title: 'Failure to compile on armv7l: ‘vld1q_u8_x4’ was not declared in this scope;
  did you mean ‘vld1q_u8’?'
source_url: https://github.com/xmrig/xmrig/issues/2876
author: benthetechguy
assignees: []
labels:
- bug
- arm
created_at: '2022-01-19T03:51:19+00:00'
updated_at: '2022-01-21T18:17:15+00:00'
type: issue
status: closed
closed_at: '2022-01-21T16:52:59+00:00'
---

# Original Description
**Describe the bug**
I am attempting to package xmrig for Debian, and everything is going well so far, except compilation on the `armhf` architecture (armv7l). I ran into this exact issue (#2175) last time I used the normal compilation instructions on Raspbian, Ubuntu, and Arch Linux ARM, and it seemed to have been fixed back then, but is now reappearing.

**To Reproduce**
1. Install Debian sid/unstable on an armv7l machine or VM
2. `sudo apt install build-essential devscripts` (Install package building essentials)
3. `dget -x https://mentors.debian.net/debian/pool/main/x/xmrig/xmrig_6.16.2-1.dsc` (Download the prototype of my package)
4. `cd xmrig-6.16.2 && sudo apt build-dep .` (Install build dependencies)
5. `debuild` (Build the package)
6. See compilation fail

**Expected behavior**
I expected xmrig to compile successfully and the package to build like on the other architectures.

**Required data**
Excerpt of the compilation output ([full output here](https://github.com/xmrig/xmrig/files/7893946/pkgbuild.log)):
```
In file included from /home/ben/xmrig-6.16.2/src/crypto/ghostrider/ghostrider.cpp:57:
/home/ben/xmrig-6.16.2/src/crypto/ghostrider/../../crypto/cn/sse2neon.h: In function ‘uint8x16x4_t _sse2neon_vld1q_u8_x4(const uint8_t*)’:
/home/ben/xmrig-6.16.2/src/crypto/ghostrider/../../crypto/cn/sse2neon.h:363:12: error: ‘vld1q_u8_x4’ was not declared in this scope; did you mean ‘vld1q_u8’?
  363 |     return vld1q_u8_x4(p);
      |            ^~~~~~~~~~~
      |            vld1q_u8
make[3]: *** [src/crypto/ghostrider/CMakeFiles/ghostrider.dir/build.make:303: src/crypto/ghostrider/CMakeFiles/ghostrider.dir/ghostrider.cpp.o] Error 1
```

# Discussion History
## Spudz76 | 2022-01-19T07:53:47+00:00
What is the gcc version being used for the build?

## benthetechguy | 2022-01-19T12:41:04+00:00
11.2


## Spudz76 | 2022-01-19T15:32:44+00:00
Please try with small change of `10` to `11` in `src/crypto/cn/sse2neon.h` line 347:

`    ((__GNUC__ <= 11 && defined(__arm__)) ||                           \`

Should work and if so, I will submit the patch.

## benthetechguy | 2022-01-19T22:30:35+00:00
Thanks, it compiled correctly. There's a new problem though, I ran a test benchmark and got this:
```
[2022-01-19 12:28:47.917]  cpu      use profile  rx  (2 threads) scratchpad 2048 KB
[ 1639.859563] Alignment trap: not handling instruction f9430a2f at [<005fa0a2>]
[ 1639.860023] Alignment trap: not handling instruction f9430a2f at [<005fa0a2>]
[ 1639.860321] 8<--- cut here ---
[ 1639.860338] Unhandled fault: alignment exception (0xa21) at 0xb5000618
[ 1639.860375] pgd = 248d079d
[ 1639.860547] [b5000618] *pgd=45a37003, *pmd=13f815003
[ 1639.861673] 8<--- cut here ---
[ 1639.861892] Unhandled fault: alignment exception (0xa21) at 0xb5100618
[ 1639.862646] pgd = 248d079d
[ 1639.862712] [b5100618] *pgd=45a37003, *pmd=13f815003
Bus error
```

## Spudz76 | 2022-01-19T22:58:49+00:00
Meh.  Looks like VM spin-up will be required.  Hoped it was as easy as the previous stab.

## benthetechguy | 2022-01-21T18:17:15+00:00
Could this be reopened since there's still an issue? It's a different issue however, so I'm fine with renaming this or just creating an entirely new issue.

# Action History
- Created by: benthetechguy | 2022-01-19T03:51:19+00:00
- Closed at: 2022-01-21T16:52:59+00:00
