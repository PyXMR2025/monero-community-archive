---
title: Error compiling for Windows
source_url: https://github.com/monero-project/monero-gui/issues/3855
author: tjmitchem
assignees: []
labels: []
created_at: '2022-03-09T23:26:14+00:00'
updated_at: '2023-04-16T17:19:50+00:00'
type: issue
status: closed
closed_at: '2022-04-06T02:46:25+00:00'
---

# Original Description
After following the instructions for compiling for Windows, I hit this error at the end of "make deploy".

`
[100%] Built target monero-wallet-gui
Copying DLLs to target folder
Error copying file "D:/apps/msys64/mingw64/bin/libicudt68.dll" to "D:/dev/monero-gui/build/release/bin".
Error copying file "D:/apps/msys64/mingw64/bin/libicuin68.dll" to "D:/dev/monero-gui/build/release/bin".
Error copying file "D:/apps/msys64/mingw64/bin/libicuio68.dll" to "D:/dev/monero-gui/build/release/bin".
Error copying file "D:/apps/msys64/mingw64/bin/libicutu68.dll" to "D:/dev/monero-gui/build/release/bin".
Error copying file "D:/apps/msys64/mingw64/bin/libicuuc68.dll" to "D:/dev/monero-gui/build/release/bin".
make[3]: *** [src/CMakeFiles/deploy.dir/build.make:71: deploy] Error 1
make[2]: *** [CMakeFiles/Makefile2:4525: src/CMakeFiles/deploy.dir/all] Error 2
make[1]: *** [CMakeFiles/Makefile2:4532: src/CMakeFiles/deploy.dir/rule] Error 2
make: *** [Makefile:1547: deploy] Error 2
`

As far as I can tell, I have a newer version of these libs (69) from the MSYS2 install, and I can't seem to find the "68" version.

What do I need to change in the source to use the newer libs?

# Discussion History
## selsta | 2022-03-09T23:29:42+00:00
Try changing them here: https://github.com/monero-project/monero-gui/blob/master/cmake/Deploy.cmake

## tjmitchem | 2022-03-09T23:38:04+00:00
> Try changing them here: https://github.com/monero-project/monero-gui/blob/master/cmake/Deploy.cmake

Is this something that could be detected as part of the build process?


## selsta | 2022-04-06T02:46:24+00:00
I don't know, it's not really something we use. I added it to CI so that we will see once it fails: #3855

## elibroftw | 2022-12-05T02:42:03+00:00
@selsta , could you add `mingw-w64-x86_64-pcre` to the MSYS2 deps? `make deploy` was failing but I was able to fix it after installing this dep

## selsta | 2022-12-05T09:32:14+00:00
@elibroftw do you remember the exact error message? We run `make deploy` on CI and it doesn't fail so I'm confused why it failed on your system.

## elibroftw | 2022-12-05T14:32:29+00:00
Yes libprec-16-1.dll and the -1.dll failed to copy from the msys bin dir. Then I installed the library and voila no error. 

## Cerlancism | 2023-04-16T17:19:50+00:00
Tried with fresh msys2 install:
```
Error copying file "Z:/msys64/mingw64/bin/libpcre16-0.dll" to "Z:/msys64/home/CHE/git/monero-gui/bui
ld/release/bin".
Error copying file "Z:/msys64/mingw64/bin/libpcre-1.dll" to "Z:/msys64/home/CHE/git/monero-gui/build
/release/bin".
make[3]: *** [src/CMakeFiles/deploy.dir/build.make:71: deploy] Error 1
make[2]: *** [CMakeFiles/Makefile2:4358: src/CMakeFiles/deploy.dir/all] Error 2
make[1]: *** [CMakeFiles/Makefile2:4365: src/CMakeFiles/deploy.dir/rule] Error 2
make: *** [Makefile:1508: deploy] Error 2
```

Succeed after running
`pacman -S mingw-w64-x86_64-pcre`

# Action History
- Created by: tjmitchem | 2022-03-09T23:26:14+00:00
- Closed at: 2022-04-06T02:46:25+00:00
