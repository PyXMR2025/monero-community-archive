---
title: Issues Building [Complete Newbie]
source_url: https://github.com/xmrig/xmrig/issues/80
author: lolcocks123
assignees: []
labels:
- question
created_at: '2017-08-31T14:02:15+00:00'
updated_at: '2017-10-02T12:00:22+00:00'
type: issue
status: closed
closed_at: '2017-10-02T12:00:22+00:00'
---

# Original Description
Sorry for being a complete newbie in here.

I have been trying to build this project since yesterday. The Visual Studio 15 2017 solution.

I installed cmake from the link below:
https://cmake.org/download/

and the latest version of libuv from the link below:
https://dist.libuv.org/dist/


After which I ran the command stated inserting the path of the libuv.lib file.
Below is the error I am getting.


**Command:**
cmake .. -G "Visual Studio 15 2017 Win64" -T v140_xp -DCMAKE_BUILD_TYPE=Release -DUV_INCLUDE_DIR=c:\Program Files\libuv\include -DUV_LIBRARY=c:\Program Files\libuv\libuv.lib

**Error:**
CMake Error: The source directory "C:/Users/Test Server/Desktop/xmrig-master/Files/libuv/libuv.lib" does not exist.
Specify --help for usage, or press the help button on the CMake GUI.


What exactly am I doing wrong?


Sorry for the newbie troubles, first time I am building something.

# Discussion History
## therealseeku | 2017-08-31T20:42:36+00:00
Try using quotes for paths with spaces:

`cmake .. -G "Visual Studio 15 2017 Win64" -T v140_xp -DCMAKE_BUILD_TYPE=Release  DUV_INCLUDE_DIR="c:\Program Files\libuv\include" -DUV_LIBRARY="c:\Program Files\libuv\libuv.lib"`

## lolcocks123 | 2017-09-01T04:26:19+00:00
Thank you for your help @therealseeku but if I use the quotes then the path doesn't get recognized properly it seems.

C:\Users\Test Server\Desktop\xmrig-master\build>cmake .. -G "Visual Studio 15 2017 Win64" -T v140_xp -DCMAKE_BUILD_TYPE=Release DUV_INCLUDE_DIR="C:\Program Files\libuv\include"  -DUV_LIBRARY="C:\Program Files\libuv\libuv.lib"


CMake Error: The source directory "C:/Users/Test Server/Desktop/xmrig-master/build/DUV_INCLUDE_DIR=C:/Program Files/libuv/include" does not exist.
Specify --help for usage, or press the help button on the CMake GUI.



Have you tried building it yourself? Did it work?
I have no idea what I am doing wrong. 
Maybe something to do with the libuv libraries?

## therealseeku | 2017-09-01T08:51:28+00:00
Sorry, in my Answer the - before DUV... was missing

`cmake .. -G "Visual Studio 15 2017 Win64" -T v140_xp -DCMAKE_BUILD_TYPE=Release -DUV_INCLUDE_DIR="c:\Program Files\libuv\include" -DUV_LIBRARY="c:\Program Files\libuv\libuv.lib"`

## lolcocks123 | 2017-09-01T17:49:17+00:00
@therealseeku , 
Ah, well that was probably my bad as well, I should have properly looked into the command before executing it.
Thank you.


So I built it using the 141 Toolchain.
I have a few questions if you can answer them.

1. I used the 64 bit libuv library, so will my project work, once built through Visual Studio, work on 32 bit Windows?

2. The command states v140_xp of the toolchain but I used v141. What did the '_xp' part stand for?

## xmrig | 2017-09-02T00:51:30+00:00
1. 64 bit builds works only on 64 bit operating systems.
2. _xp enables support for older systems like Windows XP and 2003, required old platform SDK installed.

Anyway I don't use _xp trick for release build, for 32 bit, better use MSYS2 it faster and supports old systems as well.

## lolcocks123 | 2017-09-02T07:28:41+00:00
@xmrig Thank you. 

I will give MSYS2 a shot later. I am still at a pretty noob stage. I will try it after I am successful with the cmake builds.

One small question (and probably the last one, sorry for these entire series of noob questions).

`cmake .. -G "Visual Studio 15 2017 Win64" -T v141 -DCMAKE_BUILD_TYPE=Release -DUV_INCLUDE_DIR="C:\libuv-msvc2017-x86\include" -DUV_LIBRARY="C:\libuv-msvc2017-x86\lib\libuv.lib"`

I built it using the 32 bit libuv, however the command states "Win64". It builds a 64 bit application
How can I build a 32 bit application?

## xmrig | 2017-09-02T08:11:40+00:00
Just remove Win64, like `-G "Visual Studio 15 2017"`.

## lolcocks123 | 2017-09-02T09:00:42+00:00
@xmrig Ah, cool, thank you.

Dumb me was trying `-G "Visual Studio 15 2017 Win32"`

## lolcocks123 | 2017-09-03T09:16:50+00:00
@xmrig, <snip>

EDIT: Okay, I got it to compile using mingw64.
However, this being the first time I am using MSYS2, I am unable to find the final xmrig.exe that I may have built.
Embarrassing, I know, but I am literally a first timer to all this. 

## foxx3n | 2017-09-04T02:14:15+00:00
I'm also stuck, few days ago I just tried xmr-stak and it caused me many headaches and depression xD, but at the end we got an EXE file. Is there other steps to follow? In my case: Windows 10 and Visual Studio 17 installed, plus LIBUV compiled. Thanks.

# Action History
- Created by: lolcocks123 | 2017-08-31T14:02:15+00:00
- Closed at: 2017-10-02T12:00:22+00:00
