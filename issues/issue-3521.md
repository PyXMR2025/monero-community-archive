---
title: 'cc1plus.exe: out of memory allocating 3154664 bytes'
source_url: https://github.com/monero-project/monero/issues/3521
author: italocoin-project
assignees: []
labels:
- invalid
created_at: '2018-03-29T17:24:54+00:00'
updated_at: '2021-08-13T04:23:45+00:00'
type: issue
status: closed
closed_at: '2021-08-13T04:23:45+00:00'
---

# Original Description
I tried to compile branch V12 on a win32 machine with mingw and i always get this error, any ideas?

[ 75%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/hex.cpp.obj

cc1plus.exe: out of memory allocating 3154664 bytes
make[3]: *** [src/wallet/CMakeFiles/obj_wallet.dir/build.make:63: src/wallet/CMakeFiles/obj_wallet.dir/wallet2.cpp.obj] Error 1
make[3]: Leaving directory '/home/xxx/monero-core/monero/build/release'
make[2]: *** [CMakeFiles/Makefile2:2281: src/wallet/CMakeFiles/obj_wallet.dir/all] Error 2
make[2]: *** Waiting for unfinished jobs....

# Discussion History
## moneromooo-monero | 2018-03-29T17:25:45+00:00
Add memory or swap, or set TMPDIR to a non tmpfs directory.

+invalid


## dEBRUYNE-1 | 2018-03-29T17:28:39+00:00
+resolved

## italocoin-project | 2018-03-29T17:33:18+00:00
I have memory 8GB of ram and CPU was never over 50%, this may be a files header is to large, this must be diagnosed!

## moneromooo-monero | 2018-03-29T17:37:13+00:00
8 GB should be way more than enough. Is that how much is free, or how much is in your machine ?

## italocoin-project | 2018-03-30T07:32:32+00:00
So for future reference i've resolved the issue, i will post it here maybe others will need it. You need to have at least 4GB of ram!

If your OS is 32bit, then in cmd (as Admin) put bcdedit /set IncreaseUserVa 3072
Install [masm32](http://masm32.com/download.htm);
open cmd (as admin too); 
put `cd C:\msys64\mingw32\lib\gcc\i686-w64-mingw32\[VERSION]`
put `C:\masm32\bin\editbin.exe /LARGEADDRESSAWARE cc1plus.exe`

Be sure to find out which cc1plus.exe you are using, this is for mingw if you use QT add its own pat, usually

put `cd C:\Qt\Tools\mingw492_32\libexec\gcc\i686-w64-mingw32\[VERSION]`
put `C:\masm32\bin\editbin.exe /LARGEADDRESSAWARE cc1plus.exe`

That's all. Hope it will be helpful:)

## italocoin-project | 2018-03-30T07:33:44+00:00
+resolved

## moneromooo-monero | 2018-03-30T09:33:30+00:00
Can you make a PR to the build instructions for windows ?

## italocoin-project | 2018-03-30T10:21:50+00:00
@moneromooo-monero i don't think this is a common problem, can you confirm is common? If you can test it on another machine and confirm i'll make a PR, let me know

## moneromooo-monero | 2018-03-30T12:12:01+00:00
I have no idea whether it's common. You're the one using windows :)

## italocoin-project | 2018-03-30T15:31:41+00:00
@monero-project `You're the one using windows` this was a low blow 🥇 We need more people to test it out, if they get the same results i will make a PR

## danrmiller | 2018-04-02T20:24:15+00:00
yes i have the same issue on windows 32-bit

## danrmiller | 2018-04-03T01:12:16+00:00
The steps here fix the problem for me too (windows 32-bit)

https://github.com/monero-project/monero/issues/3521#issuecomment-377466568



# Action History
- Created by: italocoin-project | 2018-03-29T17:24:54+00:00
- Closed at: 2021-08-13T04:23:45+00:00
