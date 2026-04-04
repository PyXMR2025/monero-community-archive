---
title: linking error bin/monero-wallet-cli.exe windows 7 monero v0.12
source_url: https://github.com/monero-project/monero/issues/3537
author: blockchainbuzz
assignees: []
labels: []
created_at: '2018-03-31T20:05:50+00:00'
updated_at: '2022-03-16T15:34:11+00:00'
type: issue
status: closed
closed_at: '2022-03-16T15:34:11+00:00'
---

# Original Description
stuck on this error, don't know how to fix it. any suggestion? it could not find `licuio` `licuin` `licuuc` `licudt` `licutu` . I don't have a problem when compiling in linux. any idea how to solve it?

`[ 92%] Linking CXX executable ../../bin/monero-wallet-cli.exe
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/7.3.0/../../../../x86_64-w64-mingw32/bin/ld.exe: cannot find -licuio
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/7.3.0/../../../../x86_64-w64-mingw32/bin/ld.exe: cannot find -licuin
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/7.3.0/../../../../x86_64-w64-mingw32/bin/ld.exe: cannot find -licuuc
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/7.3.0/../../../../x86_64-w64-mingw32/bin/ld.exe: cannot find -licudt
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/7.3.0/../../../../x86_64-w64-mingw32/bin/ld.exe: cannot find -licutu
collect2.exe: error: ld returned 1 exit status
make[3]: *** [src/simplewallet/CMakeFiles/simplewallet.dir/build.make:134: bin/monero-wallet-cli.exe] Error 1
`

# Discussion History
## moneromooo-monero | 2018-03-31T20:20:17+00:00
The icu libs changed name recently. Find what they are on your system, and change the makefiles to match. Ideally make a patch to detect both and use the right one ^_^

# Action History
- Created by: blockchainbuzz | 2018-03-31T20:05:50+00:00
- Closed at: 2022-03-16T15:34:11+00:00
