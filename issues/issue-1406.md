---
title: Pls update xmrig-deps
source_url: https://github.com/xmrig/xmrig/issues/1406
author: ValoWaking
assignees: []
labels: []
created_at: '2019-12-12T08:04:11+00:00'
updated_at: '2019-12-14T06:09:10+00:00'
type: issue
status: closed
closed_at: '2019-12-14T06:09:10+00:00'
---

# Original Description
Hi. We have old xmrig-deps 3.5. Please update it!

# Discussion History
## ValoWaking | 2019-12-12T08:12:19+00:00
ow, sorry! My bad.

## ValoWaking | 2019-12-12T08:30:12+00:00
Can't build with my VS2019 says that " fatal error C1047 libuv.lib" my VS is - VS2019 v16.4.1

## setuidroot | 2019-12-13T18:27:52+00:00
What commands are you using to build xmrig with MSVC?

Did you download xmrig-deps and link to the correct ones?

Like so:
````
cmake .. -G "Visual Studio 16 2019" -A x64 -DXMRIG_DEPS=c:\xmrig-deps\msvc2019\x64
````

^ This assumes that you first downloaded xmrig-deps (https://github.com/xmrig/xmrig-deps/archive/master.zip) unzipped it (use 7-zip: https://www.7-zip.org/a/7z1900-x64.exe) taken the unzipped file and renamed it to xmrig-deps (make sure that inside the newly renamed xmrig-deps folder you see the folder "msvc2019") then copy the whole xmrig-deps folder and paste a copy to the root of the "C" drive (located at C:\ ) otherwise you need to change the cmake command to reflect the actual path of xmrig-deps.  The not yet renamed downloaded master.zip from above, unzipped would probably be someplace like C:\Users\YourUsername\Downloads\master ... so your command would instead be:

````
cmake .. -G "Visual Studio 16 2019" -A x64 -DXMRIG_DEPS=c:\Users\YourUsername\Downloads\master\msvc2019\x64
````

The xmrig-deps don't magically appear at the root of the "C" drive after you've downloaded and unzipped them... you should really know about how file paths work before you worry about trying to compile the xmrig binary yourself.  I'm not saying that you don't know (because I don't know what you don't know.)  I'm just saying that if you're making a simple mistake such as this, you'd be better off to use the prebuilt binaries because people much more knowledgeable than either of us compiled them and compile time optimization flags can make a big difference in how well a binary runs.  I'm not good at windows (mostly because I dislike it's unnecessary overcomplication of everything, compiling a binary especially.)  So I'm not really the best person to give advice on Windows builds... my advice would be switch to Linux and enjoy easy building and many more options for runtime (and compile time) improvements.

But I don't even know what your particular problem is because you didn't post enough info to diagnose the issue... fatal error on libuv.lib means it must have found libuv (I guess) so you got the path (at least somewhat) correct...  maybe you linked it into the gcc or the msvc2017 (instead of msvc2019) folder?  I don't know.  I'm just trying to help you figure out and solve the issue yourself.  I'll be more helpful if you want to solve the Windows problem in general 😂


## ValoWaking | 2019-12-13T20:42:50+00:00
The problem in the xmrig-deps-3.5 ..\xmrig-deps-3.5\msvc2019\x64\lib\libuv.lib is compiled by VS2017, and when i compile with my VS2019 i have error
![1](https://user-images.githubusercontent.com/37003886/70830822-c48f2880-1df9-11ea-8c99-4f2d60098eaa.jpg)
![2](https://user-images.githubusercontent.com/37003886/70830830-cc4ecd00-1df9-11ea-961c-41f120a93d9c.jpg)
I used this:
"C:\Program Files\CMake\bin\cmake.exe" .. -G "Visual Studio 16 2019" -A x64 -DXMRIG_DEPS=c:\xmrig-deps-3.5\msvc2019\x64
and than:
"C:\Program Files\CMake\bin\cmake.exe" --build . --config Release





## ValoWaking | 2019-12-13T21:43:37+00:00
My wrong, im download old deps, sory. All's work fine :)

## xmrig | 2019-12-14T06:09:10+00:00
I pump xmrig-deps version, old 2019 deps was compiled with previous 2019 (not 2017) version, for example binary compatibility for 2017 deps was break by Microsoft multiple times (maybe about 6 times or so).
Thank you.

# Action History
- Created by: ValoWaking | 2019-12-12T08:04:11+00:00
- Closed at: 2019-12-14T06:09:10+00:00
