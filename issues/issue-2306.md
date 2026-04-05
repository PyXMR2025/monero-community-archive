---
title: 1GB page Segfault when xmrig running withing gvisor sandbox.
source_url: https://github.com/xmrig/xmrig/issues/2306
author: coffeeroaster
assignees: []
labels: []
created_at: '2021-04-24T01:41:26+00:00'
updated_at: '2023-09-12T15:59:08+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**
Runtime: Docker with gvisor sandbox.
Set `"1gb-pages" : true` in config file

When xmrig starts it immediately segfaults. Stack trace below:

**To Reproduce**
Enable `"1gb-pages": true` in config file.
Start xmrig within Docker (with gvisor sandbox). It will crash immediately with a segfault.

**Expected behavior**
Expected to run normally.
**Required data**
 - Miner log as text or screenshot
see below
 - Config file or command line (without wallets)
Generic config file.
 - OS: [e.g. Windows]
Ubuntu 20.04 (with Docker + gvisor sandbox)
 - For GPU related issues: information about GPUs and driver version.
N/A
**Additional context**

```
(gdb) run
Starting program: /root/xmrig 
warning: Error disabling address space randomization: Invalid argument
warning: Target and debugger are in different PID namespaces; thread lists and other data are likely unreliable.  Connect to gdbserver inside the container.
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
 * ABOUT        XMRig/6.11.2 gcc/9.3.0
 * LIBS         libuv/1.41.0 OpenSSL/1.1.1j 
 * HUGE PAGES   supported
 * 1GB PAGES    supported
 * CPU          AMD Ryzen 9 3950X 16-Core Processor (1) 64-bit AES
                threads:32
 * MEMORY       0.1/4.0 GB (3%)
 * DONATE       1%
 * ASSEMBLY     auto:ryzen
 * POOL #1      donate.v2.xmrig.com:3333 coin monero
[2021-04-24 01:31:09.213] POOLS --------------------------------------------------------------------
[2021-04-24 01:31:09.214] url:       donate.v2.xmrig.com:3333
[2021-04-24 01:31:09.214] host:      donate.v2.xmrig.com
[2021-04-24 01:31:09.214] port:      3333
[2021-04-24 01:31:09.214] user:      YOUR_WALLET_ADDRESS
[2021-04-24 01:31:09.214] pass:      x
[2021-04-24 01:31:09.214] rig-id     (null)
[2021-04-24 01:31:09.214] algo:      invalid
[2021-04-24 01:31:09.215] nicehash:  0
[2021-04-24 01:31:09.215] keepAlive: 0
[2021-04-24 01:31:09.215] --------------------------------------------------------------------------
 * COMMANDS     hashrate, pause, resume, results, connection
[New Thread 0x7f6516a00700 (LWP 906)]
 * OPENCL       disabled
 * CUDA         disabled
[2021-04-24 01:31:09.221] [donate.v2.xmrig.com:3333] state: "unconnected" -> "host-lookup"
[New Thread 0x7f6516000700 (LWP 907)]
[New Thread 0x7f6515600700 (LWP 908)]
[New Thread 0x7f6514c00700 (LWP 909)]
[New Thread 0x7f6514200700 (LWP 910)]
[2021-04-24 01:31:09.350] [donate.v2.xmrig.com:3333] state: "host-lookup" -> "connecting"
[2021-04-24 01:31:09.461] [donate.v2.xmrig.com:3333] state: "connecting" -> "connected"
[2021-04-24 01:31:09.461] [donate.v2.xmrig.com:3333] send (445 bytes): "{"id":1,"jsonrpc":"2.0","method":"login","params":{"login":"YOUR_WALLET_ADDRESS","pass":"x","agent":"XMRig/6.11.2 (Linux x86_64) libuv/1.41.0 gcc/9.3.0","algo":["cn/1","cn/2","cn/r","cn/fast","cn/half","cn/xao","cn/rto","cn/rwz","cn/zls","cn/double","cn-lite/1","cn-heavy/0","cn-heavy/tube","cn-heavy/xhv","cn-pico","cn-pico/tlo","cn/ccx","rx/0","rx/wow","rx/arq","rx/sfx","rx/keva","argon2/chukwa","argon2/chukwav2","argon2/wrkz","astrobwt"]}}"
[2021-04-24 01:31:09.598] [donate.v2.xmrig.com:3333] received (474 bytes): "{"jsonrpc":"2.0","id":1,"error":null,"result":{"id":"3d291adac5fb1dbe","job":{"blob":"0e0ed7e78d8406a9af192edd2ef9931d8952ed3bd7682efacef7823a5d2d56cfc0a9513c3bed3d0000001d4035fe4805e04df96d43b5aace10c736224e0698a37926e73a14daa0f598a24d07","job_id":"175912517644612","target":"c6100000","algo":"rx/0","height":2345982,"seed_hash":"15564c3122550436919ac2f8a71baf7cbaf9a4117b842d7f2b19dfd27dd178e9"},"extensions":["algo","nicehash","connect","tls","keepalive"],"status":"OK"}}"
[2021-04-24 01:31:09.599]  net      use pool donate.v2.xmrig.com:3333  199.247.27.41
[2021-04-24 01:31:09.599]  net      new job from donate.v2.xmrig.com:3333 diff 1000K algo rx/0 height 2345982
[2021-04-24 01:31:09.599]  cpu      use argon2 implementation AVX2
[Detaching after vfork from child process 911]
[2021-04-24 01:31:09.629]  msr      msr kernel module is not available
[2021-04-24 01:31:09.629]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
[2021-04-24 01:31:09.631]  randomx  init dataset algo rx/0 (32 threads) seed 15564c3122550436...
[2021-04-24 01:31:10.137]  randomx  1GB pages: m_scratchpadLimit = 3221225472 

[2021-04-24 01:31:10.138]  randomx  allocated 3072 MB (2080+256) huge pages 100% 3/3 +JIT (507 ms)

Thread 2 "xmrig" received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0x7f6516a00700 (LWP 906)]
0x000055afea8f3c70 in _mm256_storeu_si256 (__A=..., __P=0x7f6504021000) at /usr/lib/gcc/x86_64-linux-gnu/9/include/avxintrin.h:928
928	/usr/lib/gcc/x86_64-linux-gnu/9/include/avxintrin.h: No such file or directory.
(gdb) c
Continuing.
[2021-04-24 01:34:24.373] [donate.v2.xmrig.com:3333] send (82 bytes): "{"id":2,"jsonrpc":"2.0","method":"keepalived","params":{"id":"3d291adac5fb1dbe"}}"

Thread 2 "xmrig" received signal SIGSEGV, Segmentation fault.
tcache_get (tc_idx=<optimized out>) at malloc.c:2937
2937	malloc.c: No such file or directory.
```
Backtrace:
```
(gdb) bt
#0  tcache_get (tc_idx=<optimized out>) at malloc.c:2937
#1  __GI___libc_malloc (bytes=79) at malloc.c:3051
#2  0x000055afea8fc2e9 in operator new(unsigned long) ()
#3  0x000055afea494b7f in std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::_M_construct<char const*> (this=0x7f65169fc960, 
    __beg=0x55afeaca2380 "[2021-04-24 01:34:24\033[1;30m.374\033[0m] \033[1;33mSIGSEGV at 0x55afea8f3c70\033[0m\033[0m\n", __end=0x55afeaca23ce "") at /usr/include/c++/9/bits/basic_string.tcc:219
#4  0x000055afea39ac83 in xmrig::LogPrivate::print (this=0x55afeaca2380, level=xmrig::Log::INFO, fmt=0x55afeaa10ff0 "\033[1;33m%s at %p\033[0m", args=0x7f65169fc9d0)
    at /xmr-build/xmrig/src/base/io/log/Log.cpp:105
#5  0x000055afea39a860 in xmrig::Log::print (level=xmrig::Log::INFO, fmt=0x55afeaa10ff0 "\033[1;33m%s at %p\033[0m") at /xmr-build/xmrig/src/base/io/log/Log.cpp:253
#6  0x000055afea7341e4 in xmrig::MainLoopHandler (sig=11, info=0x7f65169fcc30, ucontext=0x7f65169fcb00) at /xmr-build/xmrig/src/crypto/rx/RxFix_linux.cpp:40
#7  <signal handler called>
#8  0x000055afea8f3c70 in _mm256_storeu_si256 (__A=..., __P=0x7f6504021000) at /usr/lib/gcc/x86_64-linux-gnu/9/include/avxintrin.h:928
#9  fill_block (s=0x7f65169fed40, ref_block=0x7f6504014c00, next_block=0x7f6504021000, with_xor=0) at /xmr-build/xmrig/src/3rdparty/argon2/arch/x86_64/lib/argon2-avx2.c:203
#10 0x000055afea8f40fa in xmrig_ar2_fill_segment_avx2 (instance=0x7f65169ffa40, position=...) at /xmr-build/xmrig/src/3rdparty/argon2/arch/x86_64/lib/argon2-avx2.c:319
#11 0x000055afea8ca5db in xmrig_ar2_fill_segment (instance=0x7f65169ffa40, position=...) at /xmr-build/xmrig/src/3rdparty/argon2/lib/impl-select.c:91
#12 0x000055afea8c875f in fill_memory_blocks_st (instance=0x7f65169ffa40) at /xmr-build/xmrig/src/3rdparty/argon2/lib/core.c:255
#13 0x000055afea8c87e5 in xmrig_ar2_fill_memory_blocks (instance=0x7f65169ffa40) at /xmr-build/xmrig/src/3rdparty/argon2/lib/core.c:271
#14 0x000055afea8c736e in argon2_ctx_mem (context=0x7f65169ffac0, type=Argon2_d, memory=0x7f6504000000, memory_size=268435456) at /xmr-build/xmrig/src/3rdparty/argon2/lib/argon2.c:108
#15 0x000055afea717378 in randomx::initCache (cache=0x7f6504000ff0, key=0x7f65040198e0, keySize=32) at /xmr-build/xmrig/src/crypto/randomx/dataset.cpp:96
#16 0x000055afea717423 in randomx::initCacheCompile (cache=0x7f6504000ff0, key=0x7f65040198e0, keySize=32) at /xmr-build/xmrig/src/crypto/randomx/dataset.cpp:105
#17 0x000055afea719474 in randomx_init_cache (cache=0x7f6504000ff0, key=0x7f65040198e0, keySize=32) at /xmr-build/xmrig/src/crypto/randomx/randomx.cpp:407
#18 0x000055afea723a53 in xmrig::RxCache::init (this=0x7f6504000fb0, seed=...) at /xmr-build/xmrig/src/crypto/rx/RxCache.cpp:67
#19 0x000055afea7268eb in xmrig::RxDataset::init (this=0x7f6504000c70, seed=..., numThreads=32, priority=-1) at /xmr-build/xmrig/src/crypto/rx/RxDataset.cpp:97
#20 0x000055afea723539 in xmrig::RxBasicStoragePrivate::initDataset (this=0x55afeaccf070, threads=32, priority=-1) at /xmr-build/xmrig/src/crypto/rx/RxBasicStorage.cpp:86
#21 0x000055afea723112 in xmrig::RxBasicStorage::init (this=0x55afeaccefc0, seed=..., threads=32, hugePages=true, oneGbPages=true, mode=xmrig::RxConfig::FastMode, priority=-1)
    at /xmr-build/xmrig/src/crypto/rx/RxBasicStorage.cpp:174
#22 0x000055afea7294ef in xmrig::RxQueue::backgroundInit (this=0x55afeacca8f0) at /xmr-build/xmrig/src/crypto/rx/RxQueue.cpp:156
#23 0x000055afea72c133 in std::__invoke_impl<void, void (xmrig::RxQueue::*)(), xmrig::RxQueue*> (
    __f=@0x55afeaccd4b0: (void (xmrig::RxQueue::*)(class xmrig::RxQueue * const)) 0x55afea7292e8 <xmrig::RxQueue::backgroundInit()>, __t=@0x55afeaccd4a8: 0x55afeacca8f0)
    at /usr/include/c++/9/bits/invoke.h:73
#24 0x000055afea72c04d in std::__invoke<void (xmrig::RxQueue::*)(), xmrig::RxQueue*> (
    __fn=@0x55afeaccd4b0: (void (xmrig::RxQueue::*)(class xmrig::RxQueue * const)) 0x55afea7292e8 <xmrig::RxQueue::backgroundInit()>) at /usr/include/c++/9/bits/invoke.h:95
#25 0x000055afea72bf9d in std::thread::_Invoker<std::tuple<void (xmrig::RxQueue::*)(), xmrig::RxQueue*> >::_M_invoke<0ul, 1ul> (this=0x55afeaccd4a8) at /usr/include/c++/9/thread:244
#26 0x000055afea72bf3f in std::thread::_Invoker<std::tuple<void (xmrig::RxQueue::*)(), xmrig::RxQueue*> >::operator() (this=0x55afeaccd4a8) at /usr/include/c++/9/thread:251
#27 0x000055afea72bf10 in std::thread::_State_impl<std::thread::_Invoker<std::tuple<void (xmrig::RxQueue::*)(), xmrig::RxQueue*> > >::_M_run (this=0x55afeaccd4a0) at /usr/include/c++/9/thread:195
#28 0x000055afea97eb44 in execute_native_thread_routine ()
#29 0x00007f6516eec609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#30 0x00007f6516cbe293 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95
(gdb) 

```


# Discussion History
## coffeeroaster | 2021-04-24T01:51:53+00:00
Any tips on how to debug? 

## Spudz76 | 2021-04-24T06:46:17+00:00
Where is Hwloc, it won't work very well without it...

## coffeeroaster | 2021-04-24T13:27:47+00:00
> Where is Hwloc, it won't work very well without it...
Not sure I understand the question. Here's how I built it (statically linked to hwloc 2.4.1)
```cmake .. -DHWLOC_DEBUG=ON  -DXMRIG_DEPS=scripts/deps -DWITH_DEBUG_LOG=ON  -DCMAKE_BUILD_TYPE=Debug -DWITH_INTERLEAVE_DEBUG_LOG=ON```

## Spudz76 | 2021-04-25T01:21:21+00:00
The "LIBS" line in your output does not mention hwloc, and should, like so:
```
 * LIBS         libuv/1.41.0 OpenSSL/1.1.1j hwloc/2.4.1
```

## coffeeroaster | 2021-04-25T13:48:08+00:00
> The "LIBS" line in your output does not mention hwloc, and should, like so:
> 
> ```
>  * LIBS         libuv/1.41.0 OpenSSL/1.1.1j hwloc/2.4.1
> ```

Good catch. I recompiled with hwloc and it still has the same problem. The gvisor sandbox doesn't mount the cgroup fs so not sure how much hwloc will actually help. 

## Spudz76 | 2021-04-25T14:59:13+00:00
That was my only guess; I'd approach gvisor people about why 1GB hugepages don't work.  Or perhaps it adds memory access fencing which defeats the purposes of reserving enormous regions and then hitting that region with multiple threads (in other words, the sandbox safety things it does, are forever incompatible).  Most of the cool stuff won't work in an actual hardware VM either I'm not sure how a container would be any better.

I did briefly search and saw some other apps that gvisor hates for similar reasons probably the answer is out there somewhere already but needs adaptation.

# Action History
- Created by: coffeeroaster | 2021-04-24T01:41:26+00:00
