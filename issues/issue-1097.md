---
title: v2.99.3-beta compiling error
source_url: https://github.com/xmrig/xmrig/issues/1097
author: martinalebachew
assignees: []
labels:
- question
created_at: '2019-08-03T07:19:10+00:00'
updated_at: '2019-08-05T11:22:07+00:00'
type: issue
status: closed
closed_at: '2019-08-05T11:22:07+00:00'
---

# Original Description
`$ make
Scanning dependencies of target xmrig-asm
[  1%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/win64/cn_main_loop.S.obj
[  2%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/CryptonightR_template.S.obj
[  3%] Linking C static library libxmrig-asm.a
[  3%] Built target xmrig-asm
Scanning dependencies of target xmrig
[  3%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuLaunchData.cpp.obj
[  4%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Console.cpp.obj
[  5%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/Json.cpp.obj
[  6%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/JsonChain.cpp.obj
[  7%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/JsonRequest.cpp.obj
[  8%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/ConsoleLog.cpp.obj
[  9%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/FileLog.cpp.obj
[  9%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/Log.cpp.obj
[ 10%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Watcher.cpp.obj
[ 11%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Base.cpp.obj
[ 12%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/BaseConfig.cpp.obj
[ 13%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/BaseTransform.cpp.obj
[ 14%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Entry.cpp.obj
[ 15%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform.cpp.obj
[ 15%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Process.cpp.obj
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Signals.cpp.obj
[ 17%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/Dns.cpp.obj
[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsRecord.cpp.obj
[ 19%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/Http.cpp.obj
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/BaseClient.cpp.obj
[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Client.cpp.obj
[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Job.cpp.obj
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Pool.cpp.obj
[ 23%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Pools.cpp.obj
[ 24%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/strategies/FailoverStrategy.cpp.obj
[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/strategies/SinglePoolStrategy.cpp.obj
[ 26%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Arguments.cpp.obj
[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Buffer.cpp.obj
[ 28%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/String.cpp.obj
[ 28%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Timer.cpp.obj
[ 29%] Building C object CMakeFiles/xmrig.dir/src/3rdparty/http-parser/http_parser.c.obj
[ 30%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpApiResponse.cpp.obj
[ 31%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpClient.cpp.obj
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpContext.cpp.obj
[ 33%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpResponse.cpp.obj
[ 34%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpServer.cpp.obj
[ 34%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/DaemonClient.cpp.obj
[ 35%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tools/TcpServer.cpp.obj
[ 36%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Hashrate.cpp.obj
[ 37%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Threads.cpp.obj
[ 38%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Worker.cpp.obj
[ 39%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.obj
[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/Cpu.cpp.obj
[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuBackend.cpp.obj
[ 41%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuConfig.cpp.obj
[ 42%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuThread.cpp.obj
[ 43%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.obj
[ 44%] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.obj
[ 45%] Building CXX object CMakeFiles/xmrig.dir/src/core/config/Config.cpp.obj
[ 46%] Building CXX object CMakeFiles/xmrig.dir/src/core/config/ConfigTransform.cpp.obj
[ 46%] Building CXX object CMakeFiles/xmrig.dir/src/core/Controller.cpp.obj
[ 47%] Building CXX object CMakeFiles/xmrig.dir/src/core/Miner.cpp.obj
[ 48%] Building CXX object CMakeFiles/xmrig.dir/src/net/JobResults.cpp.obj
[ 49%] Building CXX object CMakeFiles/xmrig.dir/src/net/Network.cpp.obj
[ 50%] Building CXX object CMakeFiles/xmrig.dir/src/net/NetworkState.cpp.obj
[ 51%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/DonateStrategy.cpp.obj
[ 52%] Building CXX object CMakeFiles/xmrig.dir/src/Summary.cpp.obj
[ 53%] Building CXX object CMakeFiles/xmrig.dir/src/xmrig.cpp.obj
[ 53%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/Json_win.cpp.obj
[ 54%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform_win.cpp.obj
[ 55%] Building RC object CMakeFiles/xmrig.dir/res/app.rc.obj
gcc: error: XMRig\: No such file or directory
gcc: error: CPU/gcc/x64/include: No such file or directory
gcc: error: XMRig\: No such file or directory
gcc: error: CPU/src/crypto/randomx: No such file or directory
gcc: error: XMRig\: No such file or directory
gcc: error: CPU/src: No such file or directory
gcc: error: XMRig\: No such file or directory
gcc: error: CPU/src/3rdparty: No such file or directory
C:\msys64\mingw64\bin\windres.exe: preprocessing failed.
make[2]: *** [CMakeFiles/xmrig.dir/build.make:903: CMakeFiles/xmrig.dir/res/app.rc.obj] Error 1
make[1]: *** [CMakeFiles/Makefile2:105: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:84: all] Error 2
`

# Discussion History
## xmrig | 2019-08-03T13:40:57+00:00
Path to XMRig source must not contain spaces, because `windres.exe` is buggy with it. Good practice not use long names, spaces, non latin and special characters.
Thank you.

## martinalebachew | 2019-08-03T20:10:08+00:00
now getting this
`$ make
Scanning dependencies of target xmrig-asm
[  1%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/win64/cn_main_loop.S.obj
[  2%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/CryptonightR_template.S.obj
[  3%] Linking C static library libxmrig-asm.a
[  3%] Built target xmrig-asm
Scanning dependencies of target xmrig
[  3%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuLaunchData.cpp.obj
[  4%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Console.cpp.obj
[  5%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/Json.cpp.obj
[  6%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/JsonChain.cpp.obj
[  7%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/JsonRequest.cpp.obj
[  8%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/ConsoleLog.cpp.obj
[  9%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/FileLog.cpp.obj
[  9%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/Log.cpp.obj
[ 10%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Watcher.cpp.obj
[ 11%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Base.cpp.obj
[ 12%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/BaseConfig.cpp.obj
[ 13%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/BaseTransform.cpp.obj
[ 14%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Entry.cpp.obj
[ 15%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform.cpp.obj
[ 15%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Process.cpp.obj
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Signals.cpp.obj
[ 17%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/Dns.cpp.obj
[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsRecord.cpp.obj
[ 19%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/Http.cpp.obj
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/BaseClient.cpp.obj
[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Client.cpp.obj
[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Job.cpp.obj
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Pool.cpp.obj
[ 23%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Pools.cpp.obj
[ 24%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/strategies/FailoverStrategy.cpp.obj
[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/strategies/SinglePoolStrategy.cpp.obj
[ 26%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Arguments.cpp.obj
[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Buffer.cpp.obj
[ 28%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/String.cpp.obj
[ 28%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Timer.cpp.obj
[ 29%] Building C object CMakeFiles/xmrig.dir/src/3rdparty/http-parser/http_parser.c.obj
[ 30%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpApiResponse.cpp.obj
[ 31%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpClient.cpp.obj
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpContext.cpp.obj
[ 33%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpResponse.cpp.obj
[ 34%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpServer.cpp.obj
[ 34%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/DaemonClient.cpp.obj
[ 35%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tools/TcpServer.cpp.obj
[ 36%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Hashrate.cpp.obj
[ 37%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Threads.cpp.obj
[ 38%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Worker.cpp.obj
[ 39%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.obj
[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/Cpu.cpp.obj
[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuBackend.cpp.obj
[ 41%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuConfig.cpp.obj
[ 42%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuThread.cpp.obj
[ 43%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.obj
[ 44%] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.obj
[ 45%] Building CXX object CMakeFiles/xmrig.dir/src/core/config/Config.cpp.obj
[ 46%] Building CXX object CMakeFiles/xmrig.dir/src/core/config/ConfigTransform.cpp.obj
[ 46%] Building CXX object CMakeFiles/xmrig.dir/src/core/Controller.cpp.obj
[ 47%] Building CXX object CMakeFiles/xmrig.dir/src/core/Miner.cpp.obj
[ 48%] Building CXX object CMakeFiles/xmrig.dir/src/net/JobResults.cpp.obj
[ 49%] Building CXX object CMakeFiles/xmrig.dir/src/net/Network.cpp.obj
[ 50%] Building CXX object CMakeFiles/xmrig.dir/src/net/NetworkState.cpp.obj
[ 51%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/DonateStrategy.cpp.obj
[ 52%] Building CXX object CMakeFiles/xmrig.dir/src/Summary.cpp.obj
[ 53%] Building CXX object CMakeFiles/xmrig.dir/src/xmrig.cpp.obj
[ 53%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/Json_win.cpp.obj
[ 54%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform_win.cpp.obj
[ 55%] Building RC object CMakeFiles/xmrig.dir/res/app.rc.obj
C:\msys64\mingw64\bin\windres.exe: Z:/FlareXMRig/CPU/res/app.rc:23: syntax error
make[2]: *** [CMakeFiles/xmrig.dir/build.make:903: CMakeFiles/xmrig.dir/res/app.rc.obj] Error 1
make[1]: *** [CMakeFiles/Makefile2:105: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:84: all] Error 2
`

## xmrig | 2019-08-04T08:08:30+00:00
If you modified app.rc or version.h it's now your responsibility, otherwise you should not get this error.
Thank you.

# Action History
- Created by: martinalebachew | 2019-08-03T07:19:10+00:00
- Closed at: 2019-08-05T11:22:07+00:00
