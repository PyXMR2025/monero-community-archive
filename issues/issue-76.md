---
title: unable to build on arch linux
source_url: https://github.com/xmrig/xmrig/issues/76
author: dash042
assignees: []
labels: []
created_at: '2017-08-29T21:22:59+00:00'
updated_at: '2023-02-08T07:06:29+00:00'
type: issue
status: closed
closed_at: '2017-08-29T21:34:22+00:00'
---

# Original Description
hi!

make[2]: *** no rule for target „/usr/lib/x86_64-linux-gnu/libuv.a“...

libuv is installed in version 1.14.0-1

thank you!

# Discussion History
## xmrig | 2017-08-29T21:32:43+00:00
You can build with dynamic libuv.so, in that case cmake probably find it without help, no need explicitly specify path.
libuv.a for static link, that path valid for Ubuntu, but in Arch looks like it different.

## dash042 | 2017-08-29T21:33:40+00:00
got it working:
pacman -S libuv
cmake .. -DCMAKE_BUILD_TYPE=Release
make

## lachesis | 2023-02-08T07:06:16+00:00
I hit this issue again on Ubuntu 22.04 Jammy. The fix for me was:
```
cmake .. -DCMAKE_BUILD_TYPE=Release -DUV_LIBRARY=/usr/lib/x86_64-linux-gnu/libuv_a.a
```

# Action History
- Created by: dash042 | 2017-08-29T21:22:59+00:00
- Closed at: 2017-08-29T21:34:22+00:00
