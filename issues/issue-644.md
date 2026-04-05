---
title: xmrig can't run on ARM v7?
source_url: https://github.com/xmrig/xmrig/issues/644
author: truelv
assignees: []
labels:
- arm
created_at: '2018-05-22T06:58:21+00:00'
updated_at: '2018-06-07T01:48:53+00:00'
type: issue
status: closed
closed_at: '2018-06-07T01:48:53+00:00'
---

# Original Description
SOC :    XILNX    ZYNQ-7000    (ARM v7)

# Discussion History
## truelv | 2018-05-25T06:02:57+00:00
[100%] Linking CXX executable xmrig
/usr/bin/cmake -E cmake_link_script CMakeFiles/xmrig.dir/link.txt --verbose=1
/opt/gcc-linaro-5.4.1-2017.01-i686_arm-linux-gnueabihf/bin/arm-linux-gnueabihf-g++    -Wall -fno-exceptions -fno-rtti -mfpu=neon -flax-vector-conversions -O3 -DNDEBUG -finline-functions -ffast-math -funroll-loops -fvariable-expansion-in-unroller -ftree-loop-if-convert-stores -fmerge-all-constants -fbranch-target-load-optimize2   -static CMakeFiles/xmrig.dir/src/api/Api.cpp.o CMakeFiles/xmrig.dir/src/api/ApiState.cpp.o CMakeFiles/xmrig.dir/src/api/NetworkState.cpp.o CMakeFiles/xmrig.dir/src/App.cpp.o CMakeFiles/xmrig.dir/src/Console.cpp.o CMakeFiles/xmrig.dir/src/log/ConsoleLog.cpp.o CMakeFiles/xmrig.dir/src/log/FileLog.cpp.o CMakeFiles/xmrig.dir/src/log/Log.cpp.o CMakeFiles/xmrig.dir/src/Mem.cpp.o CMakeFiles/xmrig.dir/src/net/Client.cpp.o CMakeFiles/xmrig.dir/src/net/Job.cpp.o CMakeFiles/xmrig.dir/src/net/Network.cpp.o CMakeFiles/xmrig.dir/src/net/strategies/DonateStrategy.cpp.o CMakeFiles/xmrig.dir/src/net/strategies/FailoverStrategy.cpp.o CMakeFiles/xmrig.dir/src/net/strategies/SinglePoolStrategy.cpp.o CMakeFiles/xmrig.dir/src/net/SubmitResult.cpp.o CMakeFiles/xmrig.dir/src/net/Url.cpp.o CMakeFiles/xmrig.dir/src/Options.cpp.o CMakeFiles/xmrig.dir/src/Platform.cpp.o CMakeFiles/xmrig.dir/src/Summary.cpp.o CMakeFiles/xmrig.dir/src/workers/DoubleWorker.cpp.o CMakeFiles/xmrig.dir/src/workers/Handle.cpp.o CMakeFiles/xmrig.dir/src/workers/Hashrate.cpp.o CMakeFiles/xmrig.dir/src/workers/SingleWorker.cpp.o CMakeFiles/xmrig.dir/src/workers/Worker.cpp.o CMakeFiles/xmrig.dir/src/workers/Workers.cpp.o CMakeFiles/xmrig.dir/src/xmrig.cpp.o CMakeFiles/xmrig.dir/src/App_unix.cpp.o CMakeFiles/xmrig.dir/src/Cpu_unix.cpp.o CMakeFiles/xmrig.dir/src/Mem_unix.cpp.o CMakeFiles/xmrig.dir/src/Platform_unix.cpp.o CMakeFiles/xmrig.dir/src/Cpu_arm.cpp.o CMakeFiles/xmrig.dir/src/crypto/c_keccak.c.o CMakeFiles/xmrig.dir/src/crypto/c_groestl.c.o CMakeFiles/xmrig.dir/src/crypto/c_blake256.c.o CMakeFiles/xmrig.dir/src/crypto/c_jh.c.o CMakeFiles/xmrig.dir/src/crypto/c_skein.c.o CMakeFiles/xmrig.dir/src/crypto/CryptoNight.cpp.o CMakeFiles/xmrig.dir/src/log/SysLog.cpp.o  -o xmrig -rdynamic -lpthread -lrt 
CMakeFiles/xmrig.dir/src/workers/Workers.cpp.o: In function `Workers::onResult(uv_async_s*)':
Workers.cpp:(.text+0x126): undefined reference to `uv_mutex_lock'
Workers.cpp:(.text+0x176): undefined reference to `uv_mutex_unlock'
CMakeFiles/xmrig.dir/src/workers/Workers.cpp.o: In function `Workers::job()':
Workers.cpp:(.text+0x1ca): undefined reference to `uv_rwlock_rdlock'
Workers.cpp:(.text+0x1dc): undefined reference to `uv_rwlock_rdunlock'
CMakeFiles/xmrig.dir/src/workers/Workers.cpp.o: In function `Workers::setJob(Job const&, bool)':
Workers.cpp:(.text+0x264): undefined reference to `uv_rwlock_wrlock'
Workers.cpp:(.text+0x362): undefined reference to `uv_rwlock_wrunlock'
CMakeFiles/xmrig.dir/src/workers/Workers.cpp.o: In function `Workers::stop()':
Workers.cpp:(.text+0x41c): undefined reference to `uv_timer_stop'
Workers.cpp:(.text+0x42c): undefined reference to `uv_close'
CMakeFiles/xmrig.dir/src/workers/Workers.cpp.o: In function `Workers::submit(JobResult const&)':
Workers.cpp:(.text+0x48e): undefined reference to `uv_mutex_lock'
Workers.cpp:(.text+0x4bc): undefined reference to `uv_mutex_unlock'
CMakeFiles/xmrig.dir/src/workers/Workers.cpp.o: In function `Workers::start(long long, int)':
Workers.cpp:(.text+0x506): undefined reference to `uv_mutex_init'
Workers.cpp:(.text+0x50e): undefined reference to `uv_rwlock_init'
Workers.cpp:(.text+0x538): undefined reference to `uv_default_loop'
Workers.cpp:(.text+0x548): undefined reference to `uv_async_init'
Workers.cpp:(.text+0x54c): undefined reference to `uv_default_loop'
Workers.cpp:(.text+0x554): undefined reference to `uv_timer_init'
Workers.cpp:(.text+0x56e): undefined reference to `uv_timer_start'
CMakeFiles/xmrig.dir/src/workers/Workers.cpp.o: In function `Workers::submit(JobResult const&)':
Workers.cpp:(.text+0x4c8): undefined reference to `uv_async_send'
CMakeFiles/xmrig.dir/src/api/Api.cpp.o: In function `Api::start()':
Api.cpp:(.text+0xc): undefined reference to `uv_mutex_init'
CMakeFiles/xmrig.dir/src/api/Api.cpp.o: In function `Api::get(char const*, int*)':
Api.cpp:(.text+0x58): undefined reference to `uv_mutex_lock'
Api.cpp:(.text+0x6a): undefined reference to `uv_mutex_unlock'
CMakeFiles/xmrig.dir/src/api/Api.cpp.o: In function `Api::tick(Hashrate const*)':
Api.cpp:(.text+0x8a): undefined reference to `uv_mutex_lock'
CMakeFiles/xmrig.dir/src/api/Api.cpp.o: In function `Api::tick(NetworkState const&)':


## truelv | 2018-05-25T06:09:21+00:00
To compile libuv1 ：
I download libuv1-1.8.0  and write a compile scipts like below 

ARM_GCC_HOME=/opt/gcc-linaro-5.4.1-2017.01-i686_arm-linux-gnueabihf                                                                                                             
./configure --host=arm  \                                                                                      
  CC="$ARM_GCC_HOME/bin/arm-linux-gnueabihf-gcc"  \                                                          
  CFLAGS="-I$ARM_GCC_HOME/arm-linux-gnueabihf/libc/usr/include" \                                            
  LDFLAGS="-L$ARM_GCC_HOME/lib -L$ARM_GCC_HOME/arm-linux-gnueabihf/lib" \ 

libuv looks like builded correctly but unfortunetly xmrig not .  xmrig compile option like below:

cmake -D UV_INCLUDE_DIR=/opt/libuv1-1.8.0/include -D UV_LIBRARY=/opt/libuv1-1.8.0/.libs -D CMAKE_SYSTEM_PROCESSOR=armv7l -D CMAKE_C_COMPILER=/opt/gcc-linaro-5.4.1-2017.01-i686_arm-linux-gnueabihf/bin/arm-linux-gnueabihf-gcc -D CMAKE_CXX_COMPILER=/opt/gcc-linaro-5.4.1-2017.01-i686_arm-linux-gnueabihf/bin/arm-linux-gnueabihf-g++ -DWITH_HTTPD=OFF .. 

How could I solve this compiling issue ? Thanks a lot!

## truelv | 2018-05-25T08:26:02+00:00
finnally It is compiled successfully for ARM Cortex A9 but can't run on it . Here is the error.

-sh: ./xmrig: cannot execute binary file: Exec format error


## baryluk | 2018-06-06T21:53:01+00:00
What distro are you using? Are you doing cross compilation or compiling on target machine?

FYI. There is libuv1 (1.20.3-2) in Debian testing and Ubuntu, including devel packages (headers).


## truelv | 2018-06-07T01:48:08+00:00
Based on the compile option I post. I finaly made it on the server development environment but still can't on my local virtual machine . I haven't catch the point of error . Maybe the reason is just an error on the development environment.

Thx for your reply. 


# Action History
- Created by: truelv | 2018-05-22T06:58:21+00:00
- Closed at: 2018-06-07T01:48:53+00:00
