---
title: 'Facing issue on compiling on x64. '
source_url: https://github.com/xmrig/xmrig/issues/146
author: dheerajnagpal
assignees: []
labels: []
created_at: '2017-10-10T02:13:35+00:00'
updated_at: '2020-07-28T01:57:27+00:00'
type: issue
status: closed
closed_at: '2017-10-12T16:26:13+00:00'
---

# Original Description
For some reason, I am facing issues on compiling this on x64 on Windows

I am able to compile this on MSYS2 MinGW 32Bit on Windows and am also able to compile this on Ubuntu without any issues. But on the same instance of MSYS2 with MinGW 64, it just refuses to make. 

This is the error that I get. I know Winsock2 is present but not sure what breaks after that. Any clues what could be causing this. 


[ 14%] Building CXX object CMakeFiles/xmrig.dir/src/workers/DoubleWorker.cpp.obj
In file included from C:/msys64/xmrig-code/Dependencies/gcc/libuv/x64/include/uv                                                                                                                -win.h:32:0,
                 from C:/msys64/xmrig-code/Dependencies/gcc/libuv/x64/include/uv                                                                                                                .h:60,
                 from C:/msys64/xmrig-code/src/workers/Workers.h:30,
                 from C:/msys64/xmrig-code/src/workers/DoubleWorker.cpp:30:
C:/msys64/mingw64/x86_64-w64-mingw32/include/winsock2.h:15:2: warning: #warning                                                                                                                 Please include winsock2.h before windows.h [-Wcpp]
 #warning Please include winsock2.h before windows.h
  ^~~~~~~
In file included from C:/msys64/xmrig-code/src/workers/DoubleWorker.cpp:25:0:
C:/msys64/mingw64/include/c++/7.2.0/thread: In function 'bool std::operator==(st                                                                                                                d::thread::id, std::thread::id)':
C:/msys64/mingw64/include/c++/7.2.0/thread:276:26: error: no match for 'operator                                                                                                                ==' (operand types are 'std::thread::native_handle_type {aka ptw32_handle_t}' an                                                                                                                d 'std::thread::native_handle_type {aka ptw32_handle_t}')
     return __x._M_thread == __y._M_thread;
            ~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~
In file included from C:/msys64/mingw64/include/c++/7.2.0/bits/stl_algobase.h:64                                                                                                                :0,
                 from C:/msys64/mingw64/include/c++/7.2.0/memory:62,
                 from C:/msys64/mingw64/include/c++/7.2.0/thread:39,
                 from C:/msys64/xmrig-code/src/workers/DoubleWorker.cpp:25:
C:/msys64/mingw64/include/c++/7.2.0/bits/stl_pair.h:443:5: note: candidate: temp                                                                                                                late<class _T1, class _T2> constexpr bool std::operator==(const std::pair<_T1, _                                                                                                                T2>&, const std::pair<_T1, _T2>&)
     operator==(const pair<_T1, _T2>& __x, const pair<_T1, _T2>& __y)
     ^~~~~~~~


# Discussion History
## xmrig | 2017-10-10T13:18:19+00:00
Where and how you get libuv? I think something wrong with it.
Thank you.

## dheerajnagpal | 2017-10-10T13:56:54+00:00
I got that from the dependencies. 

https://github.com/xmrig/xmrig-deps/releases



## dheerajnagpal | 2017-10-12T16:26:13+00:00
Thanks for the guidance. 

I built it on a new machine with no previous MSYS deployment and it was successful. It seems to be picking up a wrong Libuv on my regular machine. 

## alterhu2020 | 2020-07-28T01:57:26+00:00
I think msys2 not works for xmrig, you should use vs2019 to compire ,maybe this helps : https://code.pingbook.top/blog/setup/bitcoin-mining-setup.html#%E6%8E%A8%E8%8D%90%E4%B8%80%E9%94%AE%E6%8C%96%E7%9F%BF%E8%84%9A%E6%9C%AC

# Action History
- Created by: dheerajnagpal | 2017-10-10T02:13:35+00:00
- Closed at: 2017-10-12T16:26:13+00:00
