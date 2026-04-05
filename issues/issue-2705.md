---
title: gcc not found
source_url: https://github.com/xmrig/xmrig/issues/2705
author: pranshuthegamer
assignees: []
labels: []
created_at: '2021-11-18T09:02:48+00:00'
updated_at: '2021-11-20T06:30:44+00:00'
type: issue
status: closed
closed_at: '2021-11-19T15:51:34+00:00'
---

# Original Description
**Describe the bug**
` "c:\Program Files\CMake\bin\cmake.exe" .. -G "Unix Makefiles" -DXMRIG_DEPS=c:/xmrig-deps/gcc/x64
-- The C compiler identification is unknown
-- The CXX compiler identification is unknown
CMake Error at CMakeLists.txt:2 (project):
  No CMAKE_C_COMPILER could be found.

  Tell CMake where to find the compiler by setting either the environment
  variable "CC" or the CMake cache entry CMAKE_C_COMPILER to the full path to
  the compiler, or to the compiler name if it is in the PATH.


CMake Error at CMakeLists.txt:2 (project):
  No CMAKE_CXX_COMPILER could be found.

  Tell CMake where to find the compiler by setting either the environment
  variable "CXX" or the CMake cache entry CMAKE_CXX_COMPILER to the full path
  to the compiler, or to the compiler name if it is in the PATH.


-- Configuring incomplete, errors occurred!
See also "C:/msys64/home/Pranshu TG/xmrig/build/CMakeFiles/CMakeOutput.log".
See also "C:/msys64/home/Pranshu TG/xmrig/build/CMakeFiles/CMakeError.log".
`

**Expected behavior**
i should be able to use make to build it

**Required data**
 - Miner log as text or screenshot
 - Config file or command line (without wallets)
 - OS: Windows 10


# Discussion History
## Titaniumtown | 2021-11-19T14:10:53+00:00
did you install gcc?

## Spudz76 | 2021-11-19T14:11:48+00:00
Not sure, I have never gotten anything but MSVC compile to work on Windows.  Maybe I will try it again and see.

My guess is you are missing some msys64 packages or it isn't in your Windows PATH environment variable.

[This seems like a decent howto](https://www.devdungeon.com/content/install-gcc-compiler-windows-msys2-cc), see if you've missed some pacman things or the adding to path.

## pranshuthegamer | 2021-11-19T15:51:34+00:00
problem solved btw i did install gcc

## Spudz76 | 2021-11-20T06:13:10+00:00
Then it was the PATH?

## pranshuthegamer | 2021-11-20T06:30:44+00:00
i think the tutorial on the xmrig wiki doesnt work but the one you sent me
does work

On Sat, Nov 20, 2021, 11:43 Tony Butler ***@***.***> wrote:

> Then it was the PATH?
>
> —
> You are receiving this because you modified the open/close state.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/2705#issuecomment-974602149>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AOUJCTZLOEAHEEI4S2S3Y2LUM44ABANCNFSM5IJB23PQ>
> .
> Triage notifications on the go with GitHub Mobile for iOS
> <https://apps.apple.com/app/apple-store/id1477376905?ct=notification-email&mt=8&pt=524675>
> or Android
> <https://play.google.com/store/apps/details?id=com.github.android&referrer=utm_campaign%3Dnotification-email%26utm_medium%3Demail%26utm_source%3Dgithub>.
>
>


# Action History
- Created by: pranshuthegamer | 2021-11-18T09:02:48+00:00
- Closed at: 2021-11-19T15:51:34+00:00
