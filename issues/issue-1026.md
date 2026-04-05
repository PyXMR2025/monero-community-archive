---
title: changes in evo (242ece) breaks iphone build
source_url: https://github.com/xmrig/xmrig/issues/1026
author: resistor4u
assignees: []
labels:
- bug
created_at: '2019-06-03T10:37:28+00:00'
updated_at: '2019-06-03T19:15:45+00:00'
type: issue
status: closed
closed_at: '2019-06-03T19:06:24+00:00'
---

# Original Description
Changes in evo branch (commit 242ece) are supposed to fix the ARM builds. I hacked a workaround in #985, but this hack no longer works at all. @xmrig can you provide some pointers on where to go to fix the build for iphones?

# Discussion History
## xmrig | 2019-06-03T12:03:39+00:00
Please check commit https://github.com/xmrig/xmrig/commit/f620ffe8990dd94bc063778f59f101488153fb99 it should fix build issue, but I can't verify it by myself, can you provide build instructions for iOS?
Thank you.

## resistor4u | 2019-06-03T19:06:24+00:00
RE: can I provide build instructions? Yes, happily.

To build:
------

Historically, I have had success building xmrig two ways. One uses [ios-cmake toolchain](https://github.com/leetal/ios-cmake), the other does not. In either case, you must also have successfully built `libuv`, which you can accomplish by again using the ios-cmake toolchain if you like. Here is the no-frills ios-cmake version. This build uses xcode 10.0.

```
cmake .. -DCMAKE_TOOLCHAIN_FILE=~/ios-cmake/ios.toolchain.cmake -DWITH_AEON=OFF -DWITH_HTTP=OFF -DUV_LIBRARY=~/libuv-cmake/build/libuv.a -DUV_INCLUDE_DIR=~/libuv-cmake/libuv/include -DCMAKE_HOST_SYSTEM_PROCESSOR=aarch64 -DCMAKE_SYSTEM_PROCESSOR=aarch64 -DIOS_DEPLOYMENT_TARGET=11.3 -DWITH_TLS=OFF -DWITH_SUMO=OFF -DWITH_CN_PICO=OFF -DWITH_CN_GPU=OFF && make -j4
```
Then, you must put the binary on the iphone, make sure it's executable, `ldid -Sent.xml xmrig-notls` and copy it to a dir in your path. To build without the ios.cmake.toolchain, simply cut those bits. (In the past, this has worked but it no longer does - I think I borked something, so stick with the ios.cmake.toolchain instructions.)

WIth https://github.com/xmrig/xmrig/commit/f620ffe8990dd94bc063778f59f101488153fb99 and the above settings, cmake will complain that `Looking for __builtin___clear_cache - not found` and the compiler will indicate:
```
In file included from ~/xmrig/src/net/Network.cpp:43:
~/xmrig/src/net/Network.h:81:17: warning: private field 'm_controller' is not used [-Wunused-private-field]
    Controller *m_controller;
                ^
```
But it will build and execute.

FWIW
------
When executed, the binary will settle at about 14.6 H/s on iPhone 6s, whereas the hackjob in #985 settles around 18.6 H/s on iPhone 6s. Newer phones should have higher rates. @xmrig thank you for taking the time to standardize a fix. Unless you can see a clear way to optimize the code further, I'll close this issue.

Edit, another FWIW
------
Before this fix, cmake did not appear to be setting `-DCMAKE_HOST_SYSTEM_PROCESSOR=aarch64 -DCMAKE_SYSTEM_PROCESSOR=aarch64` correctly, because the compiler (Apple's clang) kept thinking we were building for the `x86_64` architecture rather than arm64/aarch64. All object files would come out as `x86_64`. I think there was a missing definition in the cmake file, because it seemed like the compiler was instructed we were running BSD.

# Action History
- Created by: resistor4u | 2019-06-03T10:37:28+00:00
- Closed at: 2019-06-03T19:06:24+00:00
