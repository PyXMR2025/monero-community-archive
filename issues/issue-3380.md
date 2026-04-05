---
title: Please help me --,3704
source_url: https://github.com/xmrig/xmrig/issues/3380
author: kaungminsanz
assignees: []
labels: []
created_at: '2023-12-12T13:32:09+00:00'
updated_at: '2025-06-16T19:49:25+00:00'
type: issue
status: closed
closed_at: '2025-06-16T19:49:25+00:00'
---

# Original Description
userland@localhost:~$ git clone https://github.com/xmrig/xmrig.git
cd xmrig
mkdir build
cd build
cmake ..
make -j$(nproc)
fatal: destination path 'xmrig' already exists and is not an empty directory.
mkdir: cannot create directory 'build': File exists
-- Use ARM_TARGET=8 (aarch64)
-- WITH_MSR=OFF
-- Configuring done
-- Generating done
-- Build files have been written to: /home/userland/xmrig/build
Consolidate compiler generated dependencies of target ethash
Consolidate compiler generated dependencies of target argon2
Consolidate compiler generated dependencies of target ghostrider
[  1%] Built target ethash
[  4%] Built target argon2
[ 11%] Built target ghostrider
Consolidate compiler generated dependencies of target xmrig
[ 12%] Linking CXX executable xmrig
/usr/bin/ld: cannot open output file xmrig: Is a directory
collect2: error: ld returned 1 exit status
make[2]: *** [CMakeFiles/xmrig.dir/build.make:3704: xmrig] Error 1
make[1]: *** [CMakeFiles/Makefile2:138: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:91: all] Error 2

# Discussion History
## kaungminsanz | 2023-12-12T13:32:28+00:00
Help me


## SChernykh | 2023-12-12T16:09:19+00:00
`fatal: destination path 'xmrig' already exists and is not an empty directory.`

You're trying to clone `xmrig` but there's already a file with the same name in your working directory. Try to do everything again in an empty directory.

## kaungminsanz | 2023-12-12T16:18:07+00:00
Thank,  sir

On Tue, Dec 12, 2023, 10:39 PM SChernykh ***@***.***> wrote:

> fatal: destination path 'xmrig' already exists and is not an empty
> directory.
>
> You're trying to clone xmrig but there's already a file with the same
> name in your working directory. Try to do everything again in an empty
> directory.
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/3380#issuecomment-1852346034>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AVHXR6QJKMRLANMBCKVWDZDYJB6TTAVCNFSM6AAAAABARPM4G6VHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMYTQNJSGM2DMMBTGQ>
> .
> You are receiving this because you authored the thread.Message ID:
> ***@***.***>
>


# Action History
- Created by: kaungminsanz | 2023-12-12T13:32:09+00:00
- Closed at: 2025-06-16T19:49:25+00:00
