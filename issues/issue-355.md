---
title: MSVC 2017 Failed Build issue
source_url: https://github.com/xmrig/xmrig/issues/355
author: rainxh11
assignees: []
labels: []
created_at: '2018-01-21T18:03:04+00:00'
updated_at: '2018-11-05T12:38:11+00:00'
type: issue
status: closed
closed_at: '2018-11-05T12:38:11+00:00'
---

# Original Description
1>------ Build started: Project: ZERO_CHECK, Configuration: Release x64 ------
1>Checking Build System
1>CMake does not need to re-run because D:/MINE/git/xmrig/xmrig/build/CMakeFiles/generate.stamp is up-to-date.
1>CMake does not need to re-run because D:/MINE/git/xmrig/xmrig/build/src/3rdparty/libcpuid/CMakeFiles/generate.stamp is up-to-date.
2>------ Build started: Project: cpuid, Configuration: Release x64 ------
2>Building Custom Rule D:/MINE/git/xmrig/xmrig/src/3rdparty/libcpuid/CMakeLists.txt
2>CMake does not need to re-run because D:/MINE/git/xmrig/xmrig/build/src/3rdparty/libcpuid/CMakeFiles/generate.stamp is up-to-date.
2>Assembling D:\MINE\git\xmrig\xmrig\src\3rdparty\libcpuid\masm-x64.asm...
2>cpuid_main.c
2>asm-bits.c
2>recog_amd.c
2>recog_intel.c
2>libcpuid_util.c
2>LINK : MSIL .netmodule or module compiled with /GL found; restarting link with /LTCG; add /LTCG to the link command line to improve linker performance
2>cpuid.vcxproj -> D:\MINE\git\xmrig\xmrig\build\src\3rdparty\libcpuid\Release\cpuid.lib
3>------ Build started: Project: xmrig, Configuration: Release x64 ------
3>Building Custom Rule D:/MINE/git/xmrig/xmrig/CMakeLists.txt
3>CMake does not need to re-run because D:/MINE/git/xmrig/xmrig/build/CMakeFiles/generate.stamp is up-to-date.
3>Api.cpp
3>ApiState.cpp
3>D:\MINE\git\xmrig\xmrig\src\3rdparty\rapidjson/prettywriter.h(225): warning C4390: ';': empty controlled statement found; is this the intent?
3>D:\MINE\git\xmrig\xmrig\src\3rdparty\rapidjson/prettywriter.h(190): note: while compiling class template member function 'void rapidjson::PrettyWriter<rapidjson::StringBuffer,rapidjson::UTF8<char>,rapidjson::UTF8<char>,rapidjson::CrtAllocator,0>::PrettyPrefix(rapidjson::Type)'
3>D:\MINE\git\xmrig\xmrig\src\3rdparty\rapidjson/prettywriter.h(144): note: see reference to function template instantiation 'void rapidjson::PrettyWriter<rapidjson::StringBuffer,rapidjson::UTF8<char>,rapidjson::UTF8<char>,rapidjson::CrtAllocator,0>::PrettyPrefix(rapidjson::Type)' being compiled
3>D:\MINE\git\xmrig\xmrig\src\api\ApiState.cpp(128): note: see reference to class template instantiation 'rapidjson::PrettyWriter<rapidjson::StringBuffer,rapidjson::UTF8<char>,rapidjson::UTF8<char>,rapidjson::CrtAllocator,0>' being compiled
3>NetworkState.cpp
3>D:\MINE\git\xmrig\xmrig\src\api\NetworkState.cpp(49): warning C4244: 'return': conversion from 'uint64_t' to 'int', possible loss of data
3>D:\MINE\git\xmrig\xmrig\src\api\NetworkState.cpp(59): warning C4267: 'return': conversion from 'size_t' to 'uint32_t', possible loss of data
3>App.cpp
3>Console.cpp
3>ConsoleLog.cpp
3>FileLog.cpp
3>Log.cpp
3>Mem.cpp
3>Client.cpp
3>D:\MINE\git\xmrig\xmrig\src\net\Client.cpp(535): warning C4267: '=': conversion from 'size_t' to 'ULONG', possible loss of data
3>D:\MINE\git\xmrig\xmrig\src\3rdparty\rapidjson/writer.h(448): warning C4390: ';': empty controlled statement found; is this the intent?
3>D:\MINE\git\xmrig\xmrig\src\3rdparty\rapidjson/writer.h(437): note: while compiling class template member function 'void rapidjson::Writer<rapidjson::StringBuffer,rapidjson::UTF8<char>,rapidjson::UTF8<char>,rapidjson::CrtAllocator,0>::Prefix(rapidjson::Type)'
3>D:\MINE\git\xmrig\xmrig\src\3rdparty\rapidjson/writer.h(221): note: see reference to function template instantiation 'void rapidjson::Writer<rapidjson::StringBuffer,rapidjson::UTF8<char>,rapidjson::UTF8<char>,rapidjson::CrtAllocator,0>::Prefix(rapidjson::Type)' being compiled
3>D:\MINE\git\xmrig\xmrig\src\3rdparty\rapidjson/writer.h(478): note: see reference to class template instantiation 'rapidjson::Writer<rapidjson::StringBuffer,rapidjson::UTF8<char>,rapidjson::UTF8<char>,rapidjson::CrtAllocator,0>' being compiled
3>Job.cpp
3>Network.cpp
3>DonateStrategy.cpp
3>FailoverStrategy.cpp
3>SinglePoolStrategy.cpp
3>SubmitResult.cpp
3>Url.cpp
3>Options.cpp
3>Platform.cpp
3>Summary.cpp
3>Compiling...
3>DoubleWorker.cpp
3>Handle.cpp
3>Hashrate.cpp
3>SingleWorker.cpp
3>Worker.cpp
3>Workers.cpp
3>xmrig.cpp
3>App_win.cpp
3>Cpu_win.cpp
3>Mem_win.cpp
3>Platform_win.cpp
3>Cpu.cpp
3>CryptoNight.cpp
3>SysLog.cpp
3>D:\MINE\git\xmrig\xmrig\src\log\SysLog.cpp(40): error C2664: 'void vsyslog(int,char *,va_list)': cannot convert argument 2 from 'const char *' to 'char *'
3>D:\MINE\git\xmrig\xmrig\src\log\SysLog.cpp(40): note: Conversion loses qualifiers
3>Done building project "xmrig.vcxproj" -- FAILED.
4>------ Skipped Build: Project: ALL_BUILD, Configuration: Release x64 ------
4>Project not selected to build for this solution configuration 
========== Build: 2 succeeded, 1 failed, 0 up-to-date, 1 skipped ==========


# Discussion History
## xmrig | 2018-01-21T18:18:10+00:00
Did you follow the build docs https://github.com/xmrig/xmrig/wiki/Windows-Build#microsoft-visual-studio-2017 ?
Please remove all files and run cmake again and show output.

https://github.com/xmrig/xmrig/blob/master/CMakeLists.txt#L178 syslog not available for Windows and this feature should not build.
Thank you.

## rainxh11 | 2018-01-21T19:18:17+00:00
awesome, i removed syslog.h and syslog.cpp and the build was successful, thank you :)

# Action History
- Created by: rainxh11 | 2018-01-21T18:03:04+00:00
- Closed at: 2018-11-05T12:38:11+00:00
