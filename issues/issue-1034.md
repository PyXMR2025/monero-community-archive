---
title: Compiling xmrig as 32 bits dll
source_url: https://github.com/xmrig/xmrig/issues/1034
author: noname29
assignees: []
labels: []
created_at: '2019-06-13T22:40:47+00:00'
updated_at: '2019-07-26T02:24:30+00:00'
type: issue
status: closed
closed_at: '2019-06-14T18:50:17+00:00'
---

# Original Description
Hello I was able to compile xmrig as a dll and run it for 64 bits using` cmake .. -G "Visual Studio 15 2017 Win64" -DXMRIG_DEPS=C:\Users\USERNAME\Desktop\xmr\xmrig-deps-3.3\msvc2017\x86 -DCMAKE_WINDOWS_EXPORT_ALL_SYMBOLS=TRUE -DBUILD_SHARED_LIBS=TRUE ` and ive also changed cmakelists from `add_executable` to `add_library`.  It ran fine without issues. Now I am trying the same with 32 bits, after build I changed every instance of `machine:x64` to `machine:x86` under `xmrig.vcxproj` opened my visual studio 2017 and done an `ALL_BUILD` I got 1 error saying that 
`Error	LNK1112	module machine type 'x64' conflicts with target machine type 'x86'	xmrig	C:\Users\USERNAME\Desktop\xmr\xmrig-master\build\xmrig.dir\Debug\NetworkState.obj`

How do I fix this? Please help me compile my 32 bit dll xmrig 

# Discussion History
## expressups | 2019-07-26T02:24:30+00:00
Hello, have you solved your problem?


# Action History
- Created by: noname29 | 2019-06-13T22:40:47+00:00
- Closed at: 2019-06-14T18:50:17+00:00
