---
title: How to compile / build  xmrig source code
source_url: https://github.com/xmrig/xmrig/issues/197
author: howTOdoIT2
assignees: []
labels: []
created_at: '2017-11-12T21:24:46+00:00'
updated_at: '2018-12-21T16:51:50+00:00'
type: issue
status: closed
closed_at: '2018-03-14T23:24:52+00:00'
---

# Original Description
hi dude

First at all ..awesome app I get the highest H/s with your app but I wanna modified some stuff  I wanna make it available in other language (I wanna change all the English stuff from the app)
I install MSYS2  and CMake (cmake-gui)   also visual studio 2017

I never use those software before ..but  to change some text is not that  hard 

HOW CAN I  compiled the source code  ? I use  CMake (cmake-gui) select the source code "xmrig-2.4.2" and in Configured I choose "visual studio 15 2017 win64" I click generate but I get an error

```
Selecting Windows SDK version 10.0.16299.0 to target Windows 6.1.7601.
The C compiler identification is MSVC 19.11.25547.0
The CXX compiler identification is MSVC 19.11.25547.0
Check for working C compiler: C:/Program Files (x86)/Microsoft Visual Studio/2017/Professional/VC/Tools/MSVC/14.11.25503/bin/Hostx86/x64/cl.exe
Check for working C compiler: C:/Program Files (x86)/Microsoft Visual Studio/2017/Professional/VC/Tools/MSVC/14.11.25503/bin/Hostx86/x64/cl.exe -- works
Detecting C compiler ABI info
Detecting C compiler ABI info - done
Check for working CXX compiler: C:/Program Files (x86)/Microsoft Visual Studio/2017/Professional/VC/Tools/MSVC/14.11.25503/bin/Hostx86/x64/cl.exe
Check for working CXX compiler: C:/Program Files (x86)/Microsoft Visual Studio/2017/Professional/VC/Tools/MSVC/14.11.25503/bin/Hostx86/x64/cl.exe -- works
Detecting CXX compiler ABI info
Detecting CXX compiler ABI info - done
Detecting CXX compile features
Detecting CXX compile features - done
**CMake Error at C:/Program Files/CMake/share/cmake-3.10/Modules/FindPackageHandleStandardArgs.cmake:137 (message):
  Could NOT find UV (missing: UV_LIBRARY UV_INCLUDE_DIR)
Call Stack (most recent call first):
  C:/Program Files/CMake/share/cmake-3.10/Modules/FindPackageHandleStandardArgs.cmake:378 (_FPHSA_FAILURE_MESSAGE)
  cmake/FindUV.cmake:8 (find_package_handle_standard_args)
  CMakeLists.txt:147 (find_package)**
```

I download the **xmrig-deps-v2**  but I don't know where I need to put it.

Also can I compile  direct from visual studio 2017?  (I google it and find out how to clone a GIThub project)  but what is the start up item   app_win.cpp   xmrig.cpp ?

Can you  give a detailed step by step for  building the app from the source code?

thank you






# Discussion History
## YetAnotherRussian | 2017-11-13T07:35:34+00:00
1. Install VS 2017 community
2. Install the latest cmake-gui for windows
3. Extract xmrig-master.zip to C:\
4. Extract xmrig-deps-v2.zip somewhere, copy xmrig-deps-v2.zip\msvc2017\ contents (two folders there) to C:\deps\
5. Go to C:\xmrig-master folder, create "build" directory in it
6. Create .bat file in "build" directory with the following contents:

"%PROGRAMFILES%\CMake\bin\cmake" .. -G "Visual Studio 15 2017 Win64" -DUV_INCLUDE_DIR=C:\deps\libuv\x64\include -DUV_LIBRARY=C:\deps\libuv\Release\lib\libuv.lib
pause

7. Launch .bat file, wait for solution to be generated
8. Open .sln file in VS 2017
9. Switch build type to "Release"
10. Build => Build ALL_BUILD

Get your .exe in \xmrig-master\build\Release\ folder.

I don't know how to tell in a simplier way. That's it. 

I personally generate the project usin' intel compiler, but these goals are mine ;)

## howTOdoIT2 | 2017-11-13T09:42:05+00:00
that's why is not working  if you use other compiler ...



```
C:\Users\minerX\Desktop\111\xmrig-2.4.2\build>"C:\Program Files\CMake\bin\cmake" ..
 -G "Visual Studio 15 2017 Win64" -DUV_INCLUDE_DIR=C:\Users\minerX\Desktop\111\deps
\libuv\x64\include -DUV_LIBRARY=C:\Users\minerX\Desktop\111\deps\libuv\x64\lib\libu
v.lib
-- Selecting Windows SDK version 10.0.16299.0 to target Windows 6.1.7601.
-- The C compiler identification is MSVC 19.11.25547.0
-- The CXX compiler identification is MSVC 19.11.25547.0
-- Check for working C compiler: C:/Program Files (x86)/Microsoft Visual Studio/
2017/Professional/VC/Tools/MSVC/14.11.25503/bin/Hostx86/x64/cl.exe
-- Check for working C compiler: C:/Program Files (x86)/Microsoft Visual Studio/
2017/Professional/VC/Tools/MSVC/14.11.25503/bin/Hostx86/x64/cl.exe -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler: C:/Program Files (x86)/Microsoft Visual Studi
o/2017/Professional/VC/Tools/MSVC/14.11.25503/bin/Hostx86/x64/cl.exe
-- Check for working CXX compiler: C:/Program Files (x86)/Microsoft Visual Studi
o/2017/Professional/VC/Tools/MSVC/14.11.25503/bin/Hostx86/x64/cl.exe -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found UV: C:/Users/minerX/Desktop/111/deps/libuv/x64/lib/libuv.lib
-- The ASM_MASM compiler identification is MSVC
-- Found assembler: C:/Program Files (x86)/Microsoft Visual Studio/2017/Professi
onal/VC/Tools/MSVC/14.11.25503/bin/Hostx86/x64/ml64.exe
-- Looking for syslog.h
-- Looking for syslog.h - not found
-- Could NOT find mhd (missing: MHD_INCLUDE_DIR MHD_LIBRARY)
CMake Error at CMakeLists.txt:228 (message):
  microhttpd NOT found: use `-DWITH_HTTPD=OFF` to build without http deamon
  support


-- Configuring incomplete, errors occurred!
See also "C:/Users/minerX/Desktop/111/xmrig-2.4.2/build/CMakeFiles/CMakeOutput.log"
.
See also "C:/Users/minerX/Desktop/111/xmrig-2.4.2/build/CMakeFiles/CMakeError.log".


C:\Users\minerX\Desktop\111\xmrig-2.4.2\build>pause
Press any key to continue . . .

```

**-- Looking for syslog.h - not found** bullshit the file is there in source code /xmrig-2.4.2\src\log

but as you said you use a total different method to compile so ..this one I'm sure is not working..


## YetAnotherRussian | 2017-11-13T10:39:34+00:00
Your error is related to microhttpd (forget about syslog header file), see code:

    if (MHD_FOUND)
        include_directories(${MHD_INCLUDE_DIRS})
        set(HTTPD_SOURCES src/api/Httpd.h src/api/Httpd.cpp)
    else()
        message(FATAL_ERROR "microhttpd NOT found: use `-DWITH_HTTPD=OFF` to build without http deamon support")

Just copy microhttpd.h and libmicrohttpd.lib from x64 deps folder to %PROGRAMFILES(x86)% or %PROGRAMFILES% folder, it should look like this:

C:\Program Files (x86)\libmicrohttpd.lib
C:\Program Files (x86)\microhttpd.h

So, cmake will find them automatically.


## howTOdoIT2 | 2017-11-13T10:59:24+00:00
well well well  my dear tovarishch  that's something else   I did get the xmrig.sln and then with visual studio I build it  and I have a fresh xmrig.exe  

why those damn software can't be made using just one application ..God knows and the coders ...anyway   spasiba


## mariocaptain | 2017-11-17T07:30:03+00:00
Following your guidance I have succeeded in compiling in VS 2015 into x64. But when I compile for x86, Visual Studio 's linker reports 7 errors, like below:

`Error	LNK2001	unresolved external symbol _MHD_start_daemon	xmrig	C:\xmrig-master\build\Httpd.obj	1	`

This is my build.bat for x86:

```
"%PROGRAMFILES%\CMake\bin\cmake" .. -G "Visual Studio 14 2015" -DUV_INCLUDE_DIR=C:\deps\libuv\x86\include -DUV_LIBRARY=C:\deps\libuv\x86\lib\libuv.lib
pause
```

Any idea how to fix this?
Thanks so much!

## lisaQLY | 2017-12-14T01:44:26+00:00
I have the same problem with you ,how can you solve the problem?
![image](https://user-images.githubusercontent.com/33770524/33971437-5a0dba38-e0b3-11e7-95ca-98616ccefc1c.png)


## howTOdoIT2 | 2017-12-14T02:57:16+00:00
lisaQLY

The shit work ..i compiled it..and    I don't know programming and how this apps work..but I read  and install all the shit  that   our  dear tovarishch   developer  say here

>
 Just copy microhttpd.h and libmicrohttpd.lib from x64 deps folder to %PROGRAMFILES(x86)% or %PROGRAMFILES% folder, it should look like this:

C:\Program Files (x86)\libmicrohttpd.lib
C:\Program Files (x86)\microhttpd.h

So, cmake will find them  automatically.
>

install ..update all the shit    install visual  stuff... and ir must work

but my question is...what you wanna change in XMrig? this app work very good at it is...for monero and aeon

to bad on hithub  you cant sent private mess to members:P


## mariocaptain | 2017-12-15T13:16:25+00:00
This is what I did: go to the official guide [HERE](https://github.com/xmrig/xmrig/wiki/Windows-Build)

Pull down you will see the guide for Microsoft Visual Studio 2017.
The given command is:
`cmake .. -G "Visual Studio 15 2017 Win64" -DUV_INCLUDE_DIR="c:\<path>\msvc2017\libuv\x64\include" -DUV_LIBRARY="c:\<path>\msvc2017\libuv\x64\lib\libuv.lib" -DMHD_INCLUDE_DIR="c:\<path>\msvc2017\libmicrohttpd\x64\include" -DMHD_LIBRARY="c:\<path>\msvc2017\libmicrohttpd\x64\lib\libmicrohttpd.lib"`

Now change it to:
`cmake .. -G "Visual Studio 15 2017" -DUV_INCLUDE_DIR="c:\<path>\msvc2017\libuv\x86\include" -DUV_LIBRARY="c:\<path>\msvc2017\libuv\x86\lib\libuv.lib" -DMHD_INCLUDE_DIR="c:\<path>\msvc2017\libmicrohttpd\x86\include" -DMHD_LIBRARY="c:\<path>\msvc2017\libmicrohttpd\x86\lib\libmicrohttpd.lib"`

## comsians123 | 2018-09-28T01:49:11+00:00
> 1. Install VS 2017 community
> 2. Install the latest cmake-gui for windows
> 3. Extract xmrig-master.zip to C:\
> 4. Extract xmrig-deps-v2.zip somewhere, copy xmrig-deps-v2.zip\msvc2017\ contents (two folders there) to C:\deps\
> 5. Go to C:\xmrig-master folder, create "build" directory in it
> 6. Create .bat file in "build" directory with the following contents:
> 
> "%PROGRAMFILES%\CMake\bin\cmake" .. -G "Visual Studio 15 2017 Win64" -DUV_INCLUDE_DIR=C:\deps\libuv\x64\include -DUV_LIBRARY=C:\deps\libuv\Release\lib\libuv.lib
> pause
> 
> 1. Launch .bat file, wait for solution to be generated
> 2. Open .sln file in VS 2017
> 3. Switch build type to "Release"
> 4. Build => Build ALL_BUILD
> 
> Get your .exe in \xmrig-master\build\Release\ folder.
> 
> I don't know how to tell in a simplier way. That's it.
> 
> I personally generate the project usin' intel compiler, but these goals are mine ;)

I followed your guidelines and I am getting these errors while building from Visual Studio. 
How can I solve these errors? 
Thanks 

![capture](https://user-images.githubusercontent.com/23478572/46183423-488aec80-c2ea-11e8-8889-dc1ba5cb7333.PNG)


## vasilevskykv | 2018-10-29T15:33:35+00:00
I made Build => Build ALL_BUILD and an error appeared:
1>I:\CLionProjects\monero-xmrig\src\App.cpp(26): fatal error C1083: Can't open file uv.h: No such file or directory. What directory, I don't understand? .bat executed without any problems

## vasilevskykv | 2018-10-29T15:34:02+00:00
Where should I copy uv.h?

## savenas | 2018-12-21T16:35:10+00:00
Updated:

Download and Install VS 2017 community https://visualstudio.microsoft.com/vs/whatsnew/
Download and Install the latest cmake for windows https://cmake.org/download/
Download CPU or GPU version of xmr https://github.com/xmrig/
Extract xmrig-master.zip or xmrig-amd-master.zip to C:\

Download xmrig-deps 3.3 https://github.com/xmrig/xmrig-deps/releases/tag/v3.3
Extract xmrig-deps 3.3 to C:\
Go to C:\xmrig-master or C:\xmrig-amd-master folder, create "build" directory in it
Create .bat file in "build" directory with the following contents:

```
"%PROGRAMFILES%\CMake\bin\cmake.exe" .. -G "Visual Studio 15 2017 Win64" -DXMRIG_DEPS=c:\xmrig-deps-3.3\msvc2017\x64
pause
```



Launch .bat file, wait for a solution to be generated
Open .sln file in VS 2017
Switch build type to "Release"
Build => Build ALL_BUILD
Get your .exe in c:\xmrig-master\build\Release\ or c:\xmrig-amd-master\build\Release\ folder.

Additionally:
Please note Windows defender will remove an executable file, you have to add into exception list 

# Action History
- Created by: howTOdoIT2 | 2017-11-12T21:24:46+00:00
- Closed at: 2018-03-14T23:24:52+00:00
