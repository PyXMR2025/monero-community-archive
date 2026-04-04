---
title: '[WINDOWS] No success on building 0.14.1 tag'
source_url: https://github.com/monero-project/monero-gui/issues/2233
author: JochananCZ
assignees: []
labels:
- invalid
created_at: '2019-06-23T20:24:24+00:00'
updated_at: '2019-12-30T10:45:42+00:00'
type: issue
status: closed
closed_at: '2019-12-30T10:45:42+00:00'
---

# Original Description
I have tried to build it from the scratch. I have followed the manual on the mainpage up to the point of the building. I did a command

source ./build.sh release-static 

Which after some time just closed the MSYS2 console. When i reopened and try to process with another step (linking), it just fails.

I have redirected output to the textfile (see the attachment)
[build.log](https://github.com/monero-project/monero-gui/files/3318519/build.log)


# Discussion History
## selsta | 2019-06-23T20:31:49+00:00
I don't see any errors in your logs.

If you want a Windows build and don’t want to wait on the official release you can use the buildbot binary (`buildbot/monero-gui-win64`) from here: https://github.com/monero-project/monero-gui/pull/2218

## xiphon | 2019-06-23T20:41:20+00:00
* Could you check whether the file `/home/User007/monero-gui/build/release/bin/monero-wallet-gui.exe` exists or not?
* Run `./build.sh release-static` (without `source`)

## JochananCZ | 2019-06-23T20:57:05+00:00
> Could you check whether the file /home/User007/monero-gui/build/release/bin/monero-wallet-gui.exe exists or not?

Folder is empty
> Run ./build.sh release-static (without source)

At least have not crashed and gave me this errors
> E:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/8.3.0/../../../../x86_64-w64-mingw32/bin/ld.exe: cannot find -lwallet_merged
E:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/8.3.0/../../../../x86_64-w64-mingw32/bin/ld.exe: cannot find -llmdb
E:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/8.3.0/../../../../x86_64-w64-mingw32/bin/ld.exe: cannot find -lepee
E:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/8.3.0/../../../../x86_64-w64-mingw32/bin/ld.exe: cannot find -lunbound
E:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/8.3.0/../../../../x86_64-w64-mingw32/bin/ld.exe: cannot find -leasylogging
collect2.exe: error: ld returned 1 exit status
make[1]: *** [Makefile.Release:453: release/bin/monero-wallet-gui.exe] Chyba 1
make[1]: Opouští se adresář „/home/User007/monero-gui/build“
make: *** [Makefile:38: release] Chyba 2


## xiphon | 2019-06-23T22:24:54+00:00
It failed to build monero core. Please attach the complete log

## JochananCZ | 2019-06-24T06:41:56+00:00
I was not able to obtain complete log (> output only non errors), but these are errors, that appeared on the build console:
[build.log](https://github.com/monero-project/monero-gui/files/3319511/build.log)
There is a problem with OpenSSL
> Could NOT find OpenSSL, try to set the path to OpenSSL root folder in the

## xiphon | 2019-06-24T10:38:25+00:00
> Could NOT find OpenSSL, try to set the path to OpenSSL root folder in the

Did you install mingw-w64-x86_64-openssl package?

## JochananCZ | 2019-06-24T10:54:43+00:00
Yes, i did. I even checked when I saw that error (when I tried to install it again, it told me, that it is already there) 

## xiphon | 2019-06-24T13:26:50+00:00
> \> output only non errors

use ` > build.log 2>&1`

## JochananCZ | 2019-06-24T14:02:55+00:00
[build.log](https://github.com/monero-project/monero-gui/files/3321170/build.log)


## TomBPotochek | 2019-06-30T00:06:33+00:00
I was having the same problem. Then I tried using ./build instead of source as well and managed to finish without the mysys window closing. After cd-ing to build/ and doing a `make deploy` I was getting something like `cannot 'stat' over '/mingw64/bin/libicudt62.dll': No such file or directory` but was able to fix it by editing the 'windeploy_helper.sh' file and changing this line 
`ICU_FILES=(libicudt62.dll libicuin64.dll libicuio62.dll libicutu62.dll libicuuc62.dll)` 
to
`ICU_FILES=(libicudt64.dll libicuin64.dll libicuio64.dll libicutu64.dll libicuuc64.dll)`.
I'm not sure if this is your same issue as I could not find references to this in your logs though.

edit: Some aspects of the gui seem a bit broken so maybe this isn't such a proper solution.
![example](https://user-images.githubusercontent.com/43979399/60390776-5c9b8e80-9ab4-11e9-9825-cbc6f621f998.jpg)


## selsta | 2019-11-11T22:54:17+00:00
Please check if this is fixed with v0.15.0.0.

## selsta | 2019-12-30T10:37:07+00:00
#2677

+invalid

# Action History
- Created by: JochananCZ | 2019-06-23T20:24:24+00:00
- Closed at: 2019-12-30T10:45:42+00:00
