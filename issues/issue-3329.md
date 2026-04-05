---
title: '[100%] Linking CXX executable xmrig.exe'
source_url: https://github.com/xmrig/xmrig/issues/3329
author: Zhiming-Cai
assignees: []
labels: []
created_at: '2023-09-10T20:22:47+00:00'
updated_at: '2023-09-11T13:00:49+00:00'
type: issue
status: closed
closed_at: '2023-09-11T13:00:49+00:00'
---

# Original Description
Dear all,
When I compile xmrig.exe on Windows10, something happened.👇

[100%] Linking CXX executable xmrig.exe
D:/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: D:/libuv/sdk/lib/libuv.a(process.c.obj):process.c:(.text+0x286d): undefined reference to `__imp_SymGetOptions'
D:/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: D:/libuv/sdk/lib/libuv.a(process.c.obj):process.c:(.text+0x2889): undefined reference to `__imp_SymSetOptions'
D:/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: D:/libuv/sdk/lib/libuv.a(process.c.obj):process.c:(.text+0x28d9): undefined reference to `MiniDumpWriteDump'
D:/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: D:/libuv/sdk/lib/libuv.a(process.c.obj):process.c:(.text+0x291b): undefined reference to `__imp_SymSetOptions'
collect2.exe: error: ld returned 1 exit status
mingw32-make[2]: *** [CMakeFiles\xmrig.dir\build.make:3837: xmrig.exe] Error 1
mingw32-make[1]: *** [CMakeFiles\Makefile2:182: CMakeFiles/xmrig.dir/all] Error 2
mingw32-make: *** [Makefile:103: all] Error 2

I don't know why, help me please😢

# Discussion History
## SChernykh | 2023-09-11T07:16:08+00:00
You're compiling XMRig with mingw64, but you're using libuv from some weird location outside of mingw64's folder. This is probably the reason. I recommend to follow the instructions in https://xmrig.com/docs/miner/build/windows

## Zhiming-Cai | 2023-09-11T13:00:37+00:00
> You're compiling XMRig with mingw64, but you're using libuv from some weird location outside of mingw64's folder. This is probably the reason. I recommend to follow the instructions in https://xmrig.com/docs/miner/build/windows

Thank you very much for your reply! I followed your advice, went to the link you sent me and downloaded the entire x64, then used the -DCMAKE_DEPS option in cmake to specify the location in the x64 directory, and it compiled successfully.😊

# Action History
- Created by: Zhiming-Cai | 2023-09-10T20:22:47+00:00
- Closed at: 2023-09-11T13:00:49+00:00
