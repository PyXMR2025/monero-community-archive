---
title: c++11 support in debian
source_url: https://github.com/xmrig/xmrig/issues/130
author: lamba84
assignees:
- xmrig
labels:
- bug
created_at: '2017-09-29T07:36:41+00:00'
updated_at: '2017-10-06T16:34:30+00:00'
type: issue
status: closed
closed_at: '2017-10-06T16:34:30+00:00'
---

# Original Description
Hi, testing around with dev branch.
probably debian is not the most used distro for rigs, but c++11 is still an option in g++ 4.9.
Flag like this in CMakeLists.txt make build flawless:

`if(UNIX)
    SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
endif()`

even better would be to check g++ version and see if it required.

Thanks for great job you're doing with this software!


# Discussion History
## xmrig | 2017-09-29T08:46:35+00:00
What version of CMake you use? Probably older than 3.1, so `set(CMAKE_CXX_STANDARD 11)` doesn't work, I wasn't check minimum cmake version when add this option, I will fix it.
Thank you.

## lamba84 | 2017-09-29T09:27:08+00:00
yes, you are right. cmake 3.0.2 is default on debian. thanks


On Fri, Sep 29, 2017 at 10:46 AM, xmrig <notifications@github.com> wrote:

> What version of CMake you use? Probably older than 3.1, so set(CMAKE_CXX_STANDARD
> 11) doesn't work, I wasn't check minimum cmake version when add this
> option, I will fix it.
> Thank you.
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/130#issuecomment-333069075>, or mute
> the thread
> <https://github.com/notifications/unsubscribe-auth/Ae4BYFjFGhUNdQwVZbLLA_de7ZWyt7BIks5snK5sgaJpZM4PoTX8>
> .
>


## xmrig | 2017-10-06T16:34:30+00:00
Fixed.

# Action History
- Created by: lamba84 | 2017-09-29T07:36:41+00:00
- Closed at: 2017-10-06T16:34:30+00:00
