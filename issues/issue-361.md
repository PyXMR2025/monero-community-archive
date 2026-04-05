---
title: MinGW32 7.2.0 build error
source_url: https://github.com/xmrig/xmrig/issues/361
author: rainxh11
assignees: []
labels: []
created_at: '2018-01-25T15:48:41+00:00'
updated_at: '2018-11-05T12:47:01+00:00'
type: issue
status: closed
closed_at: '2018-11-05T12:47:01+00:00'
---

# Original Description
[ 15%] Building CXX object CMakeFiles/xmrig.dir/src/api/Api.cpp.obj
[ 17%] Building CXX object CMakeFiles/xmrig.dir/src/api/ApiState.cpp.obj
[ 19%] Building CXX object CMakeFiles/xmrig.dir/src/api/NetworkState.cpp.obj
[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.obj
[ 23%] Building CXX object CMakeFiles/xmrig.dir/src/Console.cpp.obj
[ 26%] Building CXX object CMakeFiles/xmrig.dir/src/log/ConsoleLog.cpp.obj
[ 28%] Building CXX object CMakeFiles/xmrig.dir/src/log/FileLog.cpp.obj
[ 30%] Building CXX object CMakeFiles/xmrig.dir/src/log/Log.cpp.obj
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/Mem.cpp.obj
[ 34%] Building CXX object CMakeFiles/xmrig.dir/src/net/Client.cpp.obj
[ 36%] Building CXX object CMakeFiles/xmrig.dir/src/net/Job.cpp.obj
[ 39%] Building CXX object CMakeFiles/xmrig.dir/src/net/Network.cpp.obj
[ 41%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/DonateStrategy.cpp.obj
[ 43%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/FailoverStrategy.cpp.obj
[ 45%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/SinglePoolStrategy.cpp.obj
[ 47%] Building CXX object CMakeFiles/xmrig.dir/src/net/SubmitResult.cpp.obj
[ 50%] Building CXX object CMakeFiles/xmrig.dir/src/net/Url.cpp.obj
[ 52%] Building CXX object CMakeFiles/xmrig.dir/src/Options.cpp.obj
[ 54%] Building CXX object CMakeFiles/xmrig.dir/src/Platform.cpp.obj
[ 56%] Building CXX object CMakeFiles/xmrig.dir/src/Summary.cpp.obj
[ 58%] Building CXX object CMakeFiles/xmrig.dir/src/workers/DoubleWorker.cpp.obj
D:\MINE\git\xmrig\src\workers\DoubleWorker.cpp: In member function 'virtual void DoubleWorker::start()':
D:\MINE\git\xmrig\src\workers\DoubleWorker.cpp:68:22: error: 'std::this_thread' has not been declared
                 std::this_thread::sleep_for(std::chrono::milliseconds(200));
                      ^~~~~~~~~~~
D:\MINE\git\xmrig\src\workers\DoubleWorker.cpp:98:18: error: 'std::this_thread' has not been declared
             std::this_thread::yield();
                  ^~~~~~~~~~~
mingw32-make[2]: *** [CMakeFiles\xmrig.dir\build.make:563: CMakeFiles/xmrig.dir/src/workers/DoubleWorker.cpp.obj] Error 1
mingw32-make[1]: *** [CMakeFiles\Makefile2:67: CMakeFiles/xmrig.dir/all] Error 2
mingw32-make: *** [Makefile:83: all] Error 2

# Discussion History
## Gill1000 | 2018-01-28T03:24:13+00:00
did you change anything in doubleworker.cpp.........mine is working .......mine mingw32 and 64 working normal
 

# Action History
- Created by: rainxh11 | 2018-01-25T15:48:41+00:00
- Closed at: 2018-11-05T12:47:01+00:00
