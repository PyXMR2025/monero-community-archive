---
title: Donation problem
source_url: https://github.com/xmrig/xmrig/issues/597
author: oneoy
assignees: []
labels: []
created_at: '2018-05-01T15:50:47+00:00'
updated_at: '2018-06-17T18:11:59+00:00'
type: issue
status: closed
closed_at: '2018-06-17T18:11:59+00:00'
---

# Original Description
Xmrig how to remove the donation, how to pay to you once

# Discussion History
## ghost | 2018-05-01T16:06:38+00:00
Just read https://github.com/xmrig/xmrig/blob/master/src/donate.h#L37
And:
```
constexpr const int kDonateLevel = 0; 
```
Remove donate.

## oneoy | 2018-05-01T16:11:52+00:00
In that folder? I haven't found it yet.

## ghost | 2018-05-01T16:33:27+00:00
@DaiziOuyang in `src` dir

## oneoy | 2018-05-01T17:09:31+00:00
I can run on win10, but I report this error on the 2008 server. I want to ask for help. I want to know why.
![1](https://user-images.githubusercontent.com/38435398/39483573-7324c3f4-4da5-11e8-845b-c3ad26012a84.png)


## CthulhuVRN | 2018-05-01T17:44:45+00:00
@DaiziOuyang, what error message tells you?

## oneoy | 2018-05-01T17:47:00+00:00
Lose MSVCP140D.dll

## CthulhuVRN | 2018-05-01T17:50:26+00:00
@DaiziOuyang, so that’s why xmrig won’t start.

## xmrig | 2018-05-01T17:52:39+00:00
@DaiziOuyang You didn't change build type to `Release`. Change it and rebuild again.
Thank you.

## oneoy | 2018-05-01T18:02:51+00:00

I changed it and changed to Release at the beginning.

## oneoy | 2018-05-01T18:03:48+00:00
![o 0_ 3s sv r0wqv2rv pe](https://user-images.githubusercontent.com/38435398/39485951-099f6288-4dad-11e8-8b09-ce086fe2eda8.png)


## oneoy | 2018-05-01T18:06:53+00:00
现在重新编译又出现了>>CMake Error: CMake was unable to find a build program corresponding to "Unix Makefiles". CMAKE_MAKE_PROGRAM is not set. You probably need to select a different build tool.
CMake Error: CMAKE_C_COMPILER not set, after EnableLanguage
CMake Error: CMAKE_CXX_COMPILER not set, after EnableLanguage
-- Configuring incomplete, errors occurred!
现在重新编译又出现了>>CMake Error: CMake was unable to find a build program corresponding to "Unix Makefiles".  CMAKE_MAKE_PROGRAM is not set.  You probably need to select a different build tool.
CMake Error: CMAKE_C_COMPILER not set, after EnableLanguage
CMake Error: CMAKE_CXX_COMPILER not set, after EnableLanguage
-- Configuring incomplete, errors occurred!
>>CMake Error: CMake was unable to find a build program corresponding to.
CMake Error: CMAKE_C_COMPILER not set, after EnableLanguage
CMake Error: CMAKE_CXX_COMPILER not set, after EnableLanguage
- Configuring incomplete, errors occurred!

## ghost | 2018-05-01T18:54:18+00:00
If you want to build in Visual Studio - don`t use "Unix Makefiles" use "Visual Studio 15 2017 Win64" (to x64 ) and "Visual Studio 15 2017" (to x32)

## adi3yz | 2018-05-02T01:08:37+00:00
if u dont know what u doing then just use release version from dev, and pls support dev.. 1 minute from 100 minute not to much. dev also human which need drink and food.

## enwillyado | 2018-05-03T20:59:47+00:00
@DaiziOuyang u can use my version, it is compatible with VS natively.

## focaeppe | 2018-05-05T18:00:56+00:00
@enwillyado 
Thank you
I did tried your version but after the compilation the miner doesn't work SSL error (not supported)even when i change  "ssl": true,   to false nothing change

## oneoy | 2018-05-05T18:05:48+00:00
I've been wrong, but I found that the compiling absenteeism is only 15h/s (i7 7700hq) and you can use your absenteeism to reach 300h/s. Is it a compiler where to forget to modify it?

# Action History
- Created by: oneoy | 2018-05-01T15:50:47+00:00
- Closed at: 2018-06-17T18:11:59+00:00
