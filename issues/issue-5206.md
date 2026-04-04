---
title: '[RELEASE] Failed to compile wallet for iPhone '
source_url: https://github.com/monero-project/monero/issues/5206
author: naughtyfox
assignees: []
labels: []
created_at: '2019-02-27T15:57:52+00:00'
updated_at: '2019-03-05T13:57:42+00:00'
type: issue
status: closed
closed_at: '2019-03-05T13:57:42+00:00'
---

# Original Description
Here's some logs from our CI server building multi arch wallet libs for iphone:
```/Users/Shared/Jenkins/Home/workspace/monero-ios-lipo/monero-build-ios/monero/monero/src/crypto/CryptonightR_template.S:539:11: error: register %r9d is only available in 64-bit mode
 add ebx, r9d
          ^~~
/Users/Shared/Jenkins/Home/workspace/monero-ios-lipo/monero-build-ios/monero/monero/src/crypto/CryptonightR_template.S:539:11: error: register %r9d is only available in 64-bit mode
 add ebx, r9d
          ^~~
/Users/Shared/Jenkins/Home/workspace/monero-ios-lipo/monero-build-ios/monero/monero/src/crypto/CryptonightR_template.S:542:11: error: register %r9d is only available in 64-bit mode
 sub ebx, r9d
          ^~~
/Users/Shared/Jenkins/Home/workspace/monero-ios-lipo/monero-build-ios/monero/monero/src/crypto/CryptonightR_template.S:542:11: error: register %r9d is only available in 64-bit mode
 sub ebx, r9d
          ^~~
/Users/Shared/Jenkins/Home/workspace/monero-ios-lipo/monero-build-ios/monero/monero/src/crypto/CryptonightR_template.S:548:11: error: register %r9d is only available in 64-bit mode
 xor ebx, r9d
          ^~~
/Users/Shared/Jenkins/Home/workspace/monero-ios-lipo/monero-build-ios/monero/monero/src/crypto/CryptonightR_template.S:548:11: error: register %r9d is only available in 64-bit mode
 xor ebx, r9d
```

I think the problem is when we're building for `i386` arch (simulators, afaik) because in this case the [following condition](https://github.com/monero-project/monero/blob/7c863a9fa51e7c48f2bcb77c21324827fb7f5833/src/crypto/CMakeLists.txt#L51) is working:
```
if(ARCH_ID STREQUAL "i386" OR ARCH_ID STREQUAL "x86_64" OR ARCH_ID STREQUAL "x86-64")
    list(APPEND crypto_sources CryptonightR_template.S)
endif()
```

I think `i386` arch should be removed from here because extended `x64` registers are not available there

# Discussion History
## moneromooo-monero | 2019-02-27T16:21:03+00:00
Ah, didn't notice those x86_64 specific ones. i386 should be removed then, yes.

## naughtyfox | 2019-02-27T16:22:20+00:00
there are couple more places where it should be fixed. i made patch, after build is successful i can PR.
but it takes some time for multiarch ios

## moneromooo-monero | 2019-03-05T13:39:48+00:00
+resolved

# Action History
- Created by: naughtyfox | 2019-02-27T15:57:52+00:00
- Closed at: 2019-03-05T13:57:42+00:00
