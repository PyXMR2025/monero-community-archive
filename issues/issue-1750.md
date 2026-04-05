---
title: Can't compile on macOS 10.15.5
source_url: https://github.com/xmrig/xmrig/issues/1750
author: TakahikoKarasawa
assignees: []
labels: []
created_at: '2020-06-26T12:23:08+00:00'
updated_at: '2020-06-26T22:41:44+00:00'
type: issue
status: closed
closed_at: '2020-06-26T22:41:44+00:00'
---

# Original Description
**Describe the bug**
I 

**To Reproduce**
press `make` command after installing and useing cmake command.

**Expected behavior**
Successfully install xmrig.
I'm trying to install by following this resorce.
https://medium.com/@th_s4m0ht/how-to-mine-monero-on-your-macbook-and-tweak-the-source-code-although-you-shouldnt-8d57d966ac26

** Error message**
```
pasokon:xmrig shiranui$ make
[  1%] Built target argon2-sse2
[  3%] Built target xmrig-asm
[  4%] Built target argon2-avx512f
[  5%] Built target argon2-avx2
[  6%] Built target argon2-xop
[  7%] Built target argon2-ssse3
[ 10%] Built target argon2
[ 11%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Pools.cpp.o
/Users/shiranui/xmrig/src/base/net/stratum/Pools.cpp:165:18: error: use of
      undeclared identifier 'kMinimumDonateLevel'; did you mean
      'kDefaultDonateLevel'?
    if (level >= kMinimumDonateLevel && level <= 99) {
                 ^~~~~~~~~~~~~~~~~~~
                 kDefaultDonateLevel
/Users/shiranui/xmrig/src/donate.h:47:21: note: 'kDefaultDonateLevel' declared
      here
constexpr const int kDefaultDonateLevel = 0;
                    ^
1 error generated.
make[2]: *** [CMakeFiles/xmrig.dir/src/base/net/stratum/Pools.cpp.o] Error 1
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2
```


# Discussion History
## TakahikoKarasawa | 2020-06-26T12:26:45+00:00
Here is my environment.

```
pc:xmrig user$ gcc -v
Configured with: --prefix=/Applications/Xcode.app/Contents/Developer/usr --with-gxx-include-dir=/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/c++/4.2.1
Apple clang version 11.0.3 (clang-1103.0.32.62)
Target: x86_64-apple-darwin19.5.0
Thread model: posix
InstalledDir: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin

```

# Action History
- Created by: TakahikoKarasawa | 2020-06-26T12:23:08+00:00
- Closed at: 2020-06-26T22:41:44+00:00
