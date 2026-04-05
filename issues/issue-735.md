---
title: Help to build xmrig with mingw32
source_url: https://github.com/xmrig/xmrig/issues/735
author: tkodka
assignees: []
labels:
- question
created_at: '2018-08-13T18:25:51+00:00'
updated_at: '2018-10-10T22:21:04+00:00'
type: issue
status: closed
closed_at: '2018-10-10T22:21:04+00:00'
---

# Original Description
Hello 
I am new to all this so please be patient from my ignorance of basic things. Just a few questions if anyone can help.
I made some adds in xmrig source and I have to include the lib wininet.If I complie in 64 b with Visual Studio it is ok but when I try to complie in 32b with mingw32 cannot find the library.Ignores the #pragma directive. I searched around to find somting but the solutions i found didn't resolve the issue. I search inside the dir of mingw and msys for the specific lib and I found only wininet.h not the lib.The lib is somwhere else to the win sdks of visual studio. Is it possible mingw32 need package i didn;t install?I follow th orders in the page of xmrig build but propably don't include wininet .Do anyone have an idea?
Something else. I am writing commercial applications for years now in Delphi and in Cbuilder. I didn't try yet to compile the source to cbuilder , do anyone knows if this can be done or I will mix everything?

Tassos

# Discussion History
## xmrig | 2018-08-13T19:07:48+00:00
Follow build documentation https://github.com/xmrig/xmrig/wiki/Windows-Build
Thank you.

## tkodka | 2018-08-13T19:22:27+00:00
It is not issue  building the original xmrig.I already did that but I need to add wininet. I add some stuff  that are in the specific librayr.I just ask if you have any idea .

## xmrig | 2018-08-13T20:04:55+00:00
It very simple, just add library here https://github.com/xmrig/xmrig/blob/master/CMakeLists.txt#L139

## tkodka | 2018-08-13T22:03:50+00:00
THANKS It works perfectly.!
About Cbuilder do anyone has experience of it? Did anyone tried to  build it with C++builder?And if yes with what version?

# Action History
- Created by: tkodka | 2018-08-13T18:25:51+00:00
- Closed at: 2018-10-10T22:21:04+00:00
