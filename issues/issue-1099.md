---
title: v2.99.4-beta Terrible RandomX hash rate on quad Opteron 6348 server
source_url: https://github.com/xmrig/xmrig/issues/1099
author: kio3i0j9024vkoenio
assignees: []
labels:
- NUMA
created_at: '2019-08-04T16:14:31+00:00'
updated_at: '2019-10-04T11:14:39+00:00'
type: issue
status: closed
closed_at: '2019-08-10T12:33:05+00:00'
---

# Original Description
System is:

Dell R815 Server with quad 12-core Opteron 6348's. 32GB of PC3-10600R memory is installed. 8GB per Opteron 6348 which is 4GB for each of the two NODEs in each Opteron 6348.

http://www.cpu-world.com/CPUs/Bulldozer/AMD-Opteron%206348%20-%20OS6348WKTCGHK.html

v2.99.4-beta is only getting 1644 H/s for RandomX whereas testing with randomx-benchmark produces 10612 H/s for RandomX

seq 0 7 | xargs -P 0 -I node numactl --localalloc -N node ./randomx-benchmark --mine --largePages --jit --nonces 100000 --init 6 --threads 6

It appears that v2.99.4-beta has broken NUMA/Thread Affinity and/or Memory Assignment rules.

This is the output of the run:

miner@R815-1:~/xmrig-2.99.4-beta/build$ ./xmrig                                                                                                                                              
 * ABOUT        XMRig/2.99.4-beta gcc/5.4.0
 * LIBS         libuv/1.8.0 OpenSSL/1.0.2g hwloc/1.11.2
 * CPU          AMD Opteron(tm) Processor 6348 (4) x64 AES -AVX2
                L2:48.0 MB L3:64.0 MB 48C/48T NUMA:8
 * DONATE       1%
 * ASSEMBLY     bulldozer
 * POOL #1      donate.v2.xmrig.com:3333 algo rx/0
 * COMMANDS     hashrate, pause, resume
[2019-08-04 11:01:10.908] use pool donate.v2.xmrig.com:3333  159.89.38.204
[2019-08-04 11:01:10.908] new job from donate.v2.xmrig.com:3333 diff 1000225 algo cn/r height 1893504
[2019-08-04 11:01:10.908]  cpu  use profile  cn  (48 threads) scratchpad 2048 KB
[2019-08-04 11:01:17.248]  cpu  READY threads 48(48) huge pages 48/48 100% memory 98304 KB (6339 ms)
|    CPU THREAD | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|             0 |        0 |    33.7 |     n/a |     n/a |                                                                                                                                   
|             1 |        1 |    34.0 |     n/a |     n/a |                                                                                                                                   
|             2 |        2 |    33.7 |     n/a |     n/a |                                                                                                                                   
|             3 |        3 |    33.7 |     n/a |     n/a |                                                                                                                                   
|             4 |        4 |    33.7 |     n/a |     n/a |                                                                                                                                   
|             5 |        5 |    34.6 |     n/a |     n/a |                                                                                                                                   
|             6 |        6 |    34.0 |     n/a |     n/a |                                                                                                                                   
|             7 |        7 |    33.6 |     n/a |     n/a |                                                                                                                                   
|             8 |        8 |    33.6 |     n/a |     n/a |                                                                                                                                   
|             9 |        9 |    33.9 |     n/a |     n/a |                                                                                                                                   
|            10 |       10 |    33.6 |     n/a |     n/a |                                                                                                                                   
|            11 |       11 |    34.0 |     n/a |     n/a |                                                                                                                                   
|            12 |       12 |    33.7 |     n/a |     n/a |                                                                                                                                   
|            13 |       13 |    33.9 |     n/a |     n/a |                                                                                                                                   
|            14 |       14 |    33.9 |     n/a |     n/a |                                                                                                                                   
|            15 |       15 |    34.0 |     n/a |     n/a |                                                                                                                                   
|            16 |       16 |    34.0 |     n/a |     n/a |                                                                                                                                   
|            17 |       17 |    33.9 |     n/a |     n/a |                                                                                                                                   
|            18 |       18 |    33.9 |     n/a |     n/a |                                                                                                                                   
|            19 |       19 |    33.9 |     n/a |     n/a |                                                                                                                                   
|            20 |       20 |    34.6 |     n/a |     n/a |                                                                                                                                   
|            21 |       21 |    34.0 |     n/a |     n/a |                                                                                                                                   
|            22 |       22 |    34.4 |     n/a |     n/a |                                                                                                                                   
|            23 |       23 |    34.2 |     n/a |     n/a |                                                                                                                                   
|            24 |       24 |    34.5 |     n/a |     n/a |                                                                                                                                   
|            25 |       25 |    34.0 |     n/a |     n/a |                                                                                                                                   
|            26 |       26 |    33.9 |     n/a |     n/a |                                                                                                                                   
|            27 |       27 |    34.0 |     n/a |     n/a |                                                                                                                                   
|            28 |       28 |    34.0 |     n/a |     n/a |                                                                                                                                   
|            29 |       29 |    34.2 |     n/a |     n/a |                                                                                                                                   
|            30 |       30 |    34.1 |     n/a |     n/a |                                                                                                                                   
|            31 |       31 |    34.4 |     n/a |     n/a |                                                                                                                                   
|            32 |       32 |    33.9 |     n/a |     n/a |                                                                                                                                   
|            33 |       33 |    33.6 |     n/a |     n/a |                                                                                                                                   
|            34 |       34 |    33.9 |     n/a |     n/a |                                                                                                                                   
|            35 |       35 |    33.7 |     n/a |     n/a |                                                                                                                                   
|            36 |       36 |    33.7 |     n/a |     n/a |                                                                                                                                   
|            37 |       37 |    33.9 |     n/a |     n/a |                                                                                                                                   
|            38 |       38 |    34.0 |     n/a |     n/a |                                                                                                                                   
|            39 |       39 |    34.6 |     n/a |     n/a |                                                                                                                                   
|            40 |       40 |    34.0 |     n/a |     n/a |                                                                                                                                   
|            41 |       41 |    33.9 |     n/a |     n/a |                                                                                                                                   
|            42 |       42 |    34.5 |     n/a |     n/a |                                                                                                                                   
|            43 |       43 |    34.1 |     n/a |     n/a |                                                                                                                                   
|            44 |       44 |    34.6 |     n/a |     n/a |                                                                                                                                   
|            45 |       45 |    34.2 |     n/a |     n/a |                                                                                                                                   
|            46 |       46 |    34.4 |     n/a |     n/a |                                                                                                                                   
|            47 |       47 |    33.7 |     n/a |     n/a |                                                                                                                                   
[2019-08-04 11:01:39.776] speed 10s/60s/15m 1632.5 n/a n/a H/s max 1644.0 H/s
[2019-08-04 11:01:42.260] Ctrl+C received, exiting
[2019-08-04 11:01:42.290]  cpu  stopped (31 ms)

This is the output of randomx-benchmark:

Running benchmark (100000 nonces) ...                                                                                                                                                        
Calculated result: d6660144e9a2e68bf47d7cc8afc206672e72f82dfff69fe0d974531e85f7504f                                                                                                          
Performance: 1329.85 hashes per second                                                                                                                                                       
Calculated result: d6660144e9a2e68bf47d7cc8afc206672e72f82dfff69fe0d974531e85f7504f                                                                                                          
Performance: 1328.99 hashes per second                                                                                                                                                       
Calculated result: d6660144e9a2e68bf47d7cc8afc206672e72f82dfff69fe0d974531e85f7504f                                                                                                          
Performance: 1327.96 hashes per second                                                                                                                                                       
Calculated result: d6660144e9a2e68bf47d7cc8afc206672e72f82dfff69fe0d974531e85f7504f                                                                                                          
Performance: 1326.96 hashes per second                                                                                                                                                       
Calculated result: d6660144e9a2e68bf47d7cc8afc206672e72f82dfff69fe0d974531e85f7504f                                                                                                          
Performance: 1327.62 hashes per second                                                                                                                                                       
Calculated result: d6660144e9a2e68bf47d7cc8afc206672e72f82dfff69fe0d974531e85f7504f                                                                                                          
Performance: 1326.37 hashes per second                                                                                                                                                       
Calculated result: d6660144e9a2e68bf47d7cc8afc206672e72f82dfff69fe0d974531e85f7504f                                                                                                          
Performance: 1324.89 hashes per second                                                                                                                                                       
Calculated result: d6660144e9a2e68bf47d7cc8afc206672e72f82dfff69fe0d974531e85f7504f                                                                                                          
Performance: 1324.93 hashes per second                                                                                                                                                       
Total: 10617.57



# Discussion History
## xmrig | 2019-08-04T16:26:59+00:00
Please specify option `"algo": "rx/loki"`, in config file, currently you mine `cn/r`.
Thank you.

## xmrig | 2019-08-04T16:28:40+00:00
In addition please run `./xmrig --export-topology` and share `topology.xml`

## kio3i0j9024vkoenio | 2019-08-04T16:46:00+00:00
I had "algo": "rx", in the config which I assumed was RandomX.

Changed it to "algo": "rx/loki," and am currently testing.

It now does show RX but is taking 60-65 seconds to initialize the Dataset (memory) for each NODE.

miner@R815-1:~/xmrig-2.99.4-beta/build$ ./xmrig
 * ABOUT        XMRig/2.99.4-beta gcc/5.4.0
 * LIBS         libuv/1.8.0 OpenSSL/1.0.2g hwloc/1.11.2
 * CPU          AMD Opteron(tm) Processor 6348 (4) x64 AES -AVX2
                L2:48.0 MB L3:64.0 MB 48C/48T NUMA:8
 * DONATE       1%
 * ASSEMBLY     bulldozer
 * POOL #1      donate.v2.xmrig.com:3333 algo rx/loki
 * COMMANDS     hashrate, pause, resume
[2019-08-04 11:35:53.901] use pool donate.v2.xmrig.com:3333  185.92.222.223
[2019-08-04 11:35:53.901] new job from donate.v2.xmrig.com:3333 diff 1000225 algo rx/loki height 329337
[2019-08-04 11:35:53.901]  rx   init datasets algo rx/loki (48 threads) seed db194afda36bd91a...
[2019-08-04 11:35:53.902]  cpu  use profile  rx  (48 threads) scratchpad 2048 KB
[2019-08-04 11:35:57.798]  rx   #6 allocate 2336 MB (2080+256) for RandomX dataset & cache
[2019-08-04 11:35:58.802]  rx   #6 allocate done huge pages 1168/1168 100% +JIT (4901 ms)
[2019-08-04 11:35:58.834]  cpu  READY threads 48(48) huge pages 48/48 100% memory 98304 KB (4933 ms)
[2019-08-04 11:36:37.003] new job from donate.v2.xmrig.com:3333 diff 1000225 algo rx/loki height 329338
[2019-08-04 11:36:58.642]  rx   #6 init done (64740 ms)
[2019-08-04 11:36:58.693]  rx   #1 allocate 2336 MB (2080+256) for RandomX dataset & cache
[2019-08-04 11:36:59.416]  rx   #1 allocate done huge pages 1168/1168 100% +JIT (773 ms)
[2019-08-04 11:37:59.542]  rx   #1 init done (60899 ms)
[2019-08-04 11:37:59.593]  rx   #2 allocate 2336 MB (2080+256) for RandomX dataset & cache
[2019-08-04 11:38:00.236]  rx   #2 allocate done huge pages 1168/1168 100% +JIT (694 ms)
[2019-08-04 11:38:59.650]  rx   #2 init done (60107 ms)
[2019-08-04 11:38:59.697]  rx   #3 allocate 2336 MB (2080+256) for RandomX dataset & cache
[2019-08-04 11:39:00.481]  rx   #3 allocate done huge pages 1168/1168 100% +JIT (831 ms)
[2019-08-04 11:40:00.116]  rx   #3 init done (60466 ms)
[2019-08-04 11:40:00.165]  rx   #4 allocate 2336 MB (2080+256) for RandomX dataset & cache
[2019-08-04 11:40:00.832]  rx   #4 allocate done huge pages 1168/1168 100% +JIT (716 ms)
[2019-08-04 11:41:00.493]  rx   #4 init done (60377 ms)
[2019-08-04 11:41:00.541]  rx   #5 allocate 2336 MB (2080+256) for RandomX dataset & cache
[2019-08-04 11:41:01.340]  rx   #5 allocate done huge pages 1168/1168 100% +JIT (846 ms)
[2019-08-04 11:42:00.953]  rx   #5 init done (60460 ms)
[2019-08-04 11:42:01.001]  rx   #0 allocate 2336 MB (2080+256) for RandomX dataset & cache
[2019-08-04 11:42:01.725]  rx   #0 allocate done huge pages 1168/1168 100% +JIT (772 ms)
[2019-08-04 11:43:01.389]  rx   #0 init done (60435 ms)
[2019-08-04 11:43:01.437]  rx   #7 allocate 2336 MB (2080+256) for RandomX dataset & cache
[2019-08-04 11:43:02.158]  rx   #7 allocate done huge pages 1168/1168 100% +JIT (769 ms)
[2019-08-04 11:44:01.865]  rx   #7 init done (60477 ms)
[2019-08-04 11:44:01.889] new job from donate.v2.xmrig.com:3333 diff 1000225 algo rx/loki height 329339
[2019-08-04 11:44:01.889] new job from donate.v2.xmrig.com:3333 diff 1000225 algo rx/loki height 329340
[2019-08-04 11:44:01.889] new job from donate.v2.xmrig.com:3333 diff 1000225 algo rx/loki height 329341
[2019-08-04 11:44:01.889] new job from donate.v2.xmrig.com:3333 diff 1000225 algo rx/loki height 329342

Is there some way to speed up the init?

EDIT:

If I do: ./xmrig --randomx-init=6

Then INIT time is reduced to 6-9 seconds from 60-65 seconds.

Which makes sense as each NODE in an Opteron 6348 has 6 threads.

However if I change the "init" in the config.json from -1 to 6:

"randomx": {
    "init": 6,

The INIT time goes to 12-14 seconds.

The "-1" or "6" for "init" in config.json is not optimal and takes much more time to INIT than doing the --randomx-init=6 on the command line.

Why?
                                                                                               

## kio3i0j9024vkoenio | 2019-08-04T16:50:40+00:00
My results for RandomX test are:

[2019-08-04 11:46:44.753] speed 10s/60s/15m 9479.1 9477.9 n/a H/s max 9482.1 H/s

The 9482 H/s is 10.6% lower than the 10612 I was getting with randomx-benchmark.

seq 0 7 | xargs -P 0 -I node numactl --localalloc -N node ./randomx-benchmark --mine --largePages --jit --nonces 100000 --init 6 --threads 6


## kio3i0j9024vkoenio | 2019-08-04T17:27:47+00:00
Attached file topology.xml for the Dell R815 Server with quad 12-core Opteron 6348's.
[Dell R815 quad 6348 Opterons topology.zip](https://github.com/xmrig/xmrig/files/3465128/Dell.R815.quad.6348.Opterons.topology.zip)





## xmrig | 2019-08-04T18:28:46+00:00
### Init
Init don't use NUMA specific bindings, I use this machine:
```
 * CPU          Intel(R) Xeon(R) Silver 4114 CPU @ 2.20GHz (2) x64 AES AVX2
                L2:20.0 MB L3:27.5 MB 20C/40T NUMA:2
```
for verify NUMA bindings, but it much simpler that Opterons, I don't have access to such CPUs right now. For Intel I found, use more threads is better (all 40) init each dataset take less than 3 seconds.

Bug with long initialization (about 60 seconds) was fixed in v2.99.2, init was start from one of mining threads, but if affinity used, all 40 threads use same core, (it Linux specific) now init started from main thread. If change somehow affinity of main thread it will not work correctly.

if you run `./xmrig --randomx-init=6` config value override it, actual threads number can be found in miner log, line like ` rx   init datasets algo rx/0 (40 threads) seed eef87d46a582fa1a...`.

You can use tools like `htop` to view actual CPUs load while miner init dataset.

### perfomance
I can't confirm noticeable difference between randomx-benchmark and the miner, both do about 8240 H/s (+/- 20 H/s) on CPUs above. Difference between miner and benchmark, miner use affinity and benchmark don't.

## kio3i0j9024vkoenio | 2019-08-04T18:38:08+00:00
I believe a lot of the issues I am having in performance INIT timing being over 60 seconds and performance being 10.6% low has to do with the libraries that get used when compiling from the source.

Going back and testing the compiled version from the source and the pre-compiled version I have found that the pre-compiled version is both faster doing INIT and in hash rates.

With the pre-compiled version I see these libraries being used:

libuv/1.24.1 OpenSSL/1.1.1a hwloc/2.0.4

whereas if I compile from the source it uses these libraries:

libuv/1.8.0 OpenSSL/1.0.2g hwloc/1.11.2

I have done the:

sudo apt update
sudo apt upgrade

but that does not get any new updates to these libraries.

Where might I obtain the same libraries used in the pre-compiled version?


## kio3i0j9024vkoenio | 2019-08-04T18:50:22+00:00
Using the Pre-compiled version of XMRig my results for RandomX test are:

[2019-08-04 13:46:55.611] speed 10s/60s/15m 10193.6 10192.3 n/a H/s max 10196.4 H/s

The 10196 H/s is only 3.9% lower than the 10612 I was getting with randomx-benchmark so I believe that this hash rate of 10196 is very acceptable as this is a REAL miner and probably has some overhead compared to just the randomx-benchmark program.

Well Done.

## xmrig | 2019-08-05T05:19:06+00:00
I use custom static libraries builds for simple reason, reduce external dependencies, you can verify it by `ldd xmrig`, only hwloc can affect hashrate if something going wrong, eg. memory bindings.

Can you try make a build with hwloc 2.0.4?
Thank you.

```
cd ~
wget https://download.open-mpi.org/release/hwloc/v2.0/hwloc-2.0.4.tar.bz2
tar xjf hwloc-2.0.4.tar.bz2
cd hwloc-2.0.4
./configure --disable-shared --enable-static --disable-io --disable-libudev --disable-libxml2
make
```

Then go to xmrig build directory and:
```
cmake .. -DHWLOC_INCLUDE_DIR=~/hwloc-2.0.4/include/ -DHWLOC_LIBRARY=~/hwloc-2.0.4/hwloc/.libs/libhwloc.a
make
```

## lexansoft | 2019-08-05T06:20:02+00:00
Still


Segmentation fault (core dumped)

Alexandre Naverniouk


On Sun, Aug 4, 2019 at 10:19 PM xmrig <notifications@github.com> wrote:

> Reopened #1099 <https://github.com/xmrig/xmrig/issues/1099>.
>
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/1099?email_source=notifications&email_token=AAQHPJD4BUSDDGSNE5DY5PLQC6Z43A5CNFSM4IJFWGD2YY3PNVWWK3TUL52HS4DFWZEXG43VMVCXMZLOORHG65DJMZUWGYLUNFXW5KTDN5WW2ZLOORPWSZGOS3YEQ5Y#event-2532329591>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AAQHPJDNARS6IUMSDALVZWLQC6Z43ANCNFSM4IJFWGDQ>
> .
>


## fadatsai | 2019-08-08T09:13:02+00:00
> cmake .. -DHWLOC_INCLUDE_DIR=~/hwloc-2.0.4/include/ -DHWLOC_LIBRARY=~/hwloc-2.0.4/hwloc/.libs/libhwloc.a


I try compile, but I failed

```
# cmake  ..  -DHWLOC_INCLUDE_DIR=/opt/hwloc-2.0.4/include/ -DHWLOC_LIBRARY=/opt/hwloc-2.0.4/hwloc/.libs/libhwloc.a  -DCMAKE_BUILD_TYPE=Release -DUV_LIBRARY=/opt/libuv/lib/libuv.a  -DUV_INCLUDE_DIR=/opt/libuv/include/

-- The C compiler identification is GNU 7.3.1
-- The CXX compiler identification is GNU 7.3.1
-- Check for working C compiler: /opt/rh/devtoolset-7/root/usr/bin/cc
-- Check for working C compiler: /opt/rh/devtoolset-7/root/usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /opt/rh/devtoolset-7/root/usr/bin/c++
-- Check for working CXX compiler: /opt/rh/devtoolset-7/root/usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Found HWLOC: /opt/hwloc-2.0.4/hwloc/.libs/libhwloc.a
-- Found UV: /opt/libuv/lib/libuv.a
-- Looking for __builtin___clear_cache
-- Looking for __builtin___clear_cache - found
-- Found OpenSSL: /usr/lib64/libssl.so (found version "1.0.1e")
-- The ASM compiler identification is GNU
-- Found assembler: /opt/rh/devtoolset-7/root/usr/bin/cc
-- Configuring done
-- Generating done
-- Build files have been written to: /opt/xmrig-evo/build


# make -j8
Scanning dependencies of target xmrig-asm
[  1%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/cn_main_loop.S.o
[  2%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/CryptonightR_template.S.o
[  3%] Linking C static library libxmrig-asm.a
[  3%] Built target xmrig-asm
Scanning dependencies of target xmrig
[  3%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuLaunchData.cpp.o
[  4%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Console.cpp.o
[  5%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/Json.cpp.o
[  6%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/JsonChain.cpp.o
[  7%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/ConsoleLog.cpp.o
[  7%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/FileLog.cpp.o
[  8%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/JsonRequest.cpp.o
[  9%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/Log.cpp.o
[ 10%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Watcher.cpp.o
[ 11%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Base.cpp.o
[ 12%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/BaseConfig.cpp.o
[ 13%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/BaseTransform.cpp.o
[ 14%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Entry.cpp.o
[ 14%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform.cpp.o
[ 15%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Process.cpp.o
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Signals.cpp.o
[ 17%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/Dns.cpp.o
[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsRecord.cpp.o
[ 19%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/Http.cpp.o
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/BaseClient.cpp.o
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Client.cpp.o
[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Job.cpp.o
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Pool.cpp.o
[ 23%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Pools.cpp.o
[ 24%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/strategies/FailoverStrategy.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/strategies/SinglePoolStrategy.cpp.o
[ 26%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Arguments.cpp.o
[ 26%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Buffer.cpp.o
[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/String.cpp.o
[ 28%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Timer.cpp.o
[ 29%] Building C object CMakeFiles/xmrig.dir/src/3rdparty/http-parser/http_parser.c.o
[ 30%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpApiResponse.cpp.o
[ 31%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpClient.cpp.o
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpContext.cpp.o
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpResponse.cpp.o
[ 33%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpServer.cpp.o
[ 34%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/DaemonClient.cpp.o
[ 35%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tools/TcpServer.cpp.o
[ 36%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Hashrate.cpp.o
[ 37%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Threads.cpp.o
[ 38%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Worker.cpp.o
[ 38%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o
[ 39%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/Cpu.cpp.o
[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuBackend.cpp.o
[ 41%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuConfig.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuThread.cpp.o
[ 43%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuThreads.cpp.o
[ 44%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o
[ 44%] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.o
[ 45%] Building CXX object CMakeFiles/xmrig.dir/src/core/config/Config.cpp.o
[ 46%] Building CXX object CMakeFiles/xmrig.dir/src/core/config/ConfigTransform.cpp.o
[ 47%] Building CXX object CMakeFiles/xmrig.dir/src/core/Controller.cpp.o
[ 48%] Building CXX object CMakeFiles/xmrig.dir/src/core/Miner.cpp.o
[ 49%] Building CXX object CMakeFiles/xmrig.dir/src/net/JobResults.cpp.o
[ 50%] Building CXX object CMakeFiles/xmrig.dir/src/net/Network.cpp.o
[ 50%] Building CXX object CMakeFiles/xmrig.dir/src/net/NetworkState.cpp.o
[ 51%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/DonateStrategy.cpp.o
[ 52%] Building CXX object CMakeFiles/xmrig.dir/src/Summary.cpp.o
[ 53%] Building CXX object CMakeFiles/xmrig.dir/src/xmrig.cpp.o
[ 54%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/Json_unix.cpp.o
[ 55%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform_unix.cpp.o
[ 55%] Building CXX object CMakeFiles/xmrig.dir/src/App_unix.cpp.o
[ 56%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/VirtualMemory_unix.cpp.o
[ 57%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/HwlocCpuInfo.cpp.o
[ 58%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/BasicCpuInfo.cpp.o
[ 59%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_blake256.c.o
[ 60%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_groestl.c.o
[ 61%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_jh.c.o
[ 61%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_skein.c.o
[ 62%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/CnCtx.cpp.o
[ 63%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/CnHash.cpp.o
[ 64%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/Algorithm.cpp.o
[ 65%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/keccak.cpp.o
[ 66%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/Nonce.cpp.o
[ 67%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/VirtualMemory.cpp.o
[ 67%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/aes_hash.cpp.o
[ 68%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/allocator.cpp.o
[ 69%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/argon2_core.c.o
[ 70%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/argon2_ref.c.o
[ 71%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/blake2_generator.cpp.o
[ 72%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/blake2/blake2b.c.o
[ 73%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/bytecode_machine.cpp.o
[ 73%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/dataset.cpp.o
[ 74%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/instructions_portable.cpp.o
[ 75%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/randomx.cpp.o
[ 76%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/reciprocal.c.o
[ 77%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/soft_aes.cpp.o
[ 78%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/superscalar.cpp.o
[ 79%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/virtual_machine.cpp.o
[ 79%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/virtual_memory.cpp.o
[ 80%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_compiled_light.cpp.o
[ 81%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_compiled.cpp.o
[ 82%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_interpreted_light.cpp.o
[ 83%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_interpreted.cpp.o
[ 84%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/Rx.cpp.o
[ 85%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxAlgo.cpp.o
[ 85%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxCache.cpp.o
[ 86%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxConfig.cpp.o
[ 87%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxDataset.cpp.o
[ 89%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/jit_compiler_x86_static.S.o
[ 89%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxVm.cpp.o
[ 90%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/jit_compiler_x86.cpp.o
[ 91%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/SysLog.cpp.o
[ 91%] Building CXX object CMakeFiles/xmrig.dir/src/api/Api.cpp.o
[ 92%] Building CXX object CMakeFiles/xmrig.dir/src/api/Httpd.cpp.o
[ 93%] Building CXX object CMakeFiles/xmrig.dir/src/api/requests/ApiRequest.cpp.o
[ 94%] Building CXX object CMakeFiles/xmrig.dir/src/api/requests/HttpApiRequest.cpp.o
[ 95%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Tls.cpp.o
[ 96%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpsClient.cpp.o
[ 97%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/Assembly.cpp.o
[ 97%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/r/CryptonightR_gen.cpp.o
[ 98%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/gpu/cn_gpu_avx.cpp.o
[ 99%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/gpu/cn_gpu_ssse3.cpp.o
[100%] Linking CXX executable xmrig
/opt/hwloc-2.0.4/hwloc/.libs/libhwloc.a(topology-linux.o): In function `hwloc_linux_component_instantiate':
/opt/hwloc-2.0.4/hwloc/topology-linux.c:4827: undefined reference to `udev_new'
/opt/hwloc-2.0.4/hwloc/.libs/libhwloc.a(topology-linux.o): In function `hwloc_linux_backend_disable':
/opt/hwloc-2.0.4/hwloc/topology-linux.c:4754: undefined reference to `udev_unref'
/opt/hwloc-2.0.4/hwloc/.libs/libhwloc.a(topology-xml-libxml.o): In function `hwloc_libxml_free_buffer':
/opt/hwloc-2.0.4/hwloc/topology-xml-libxml.c:590: undefined reference to `xmlFree'
/opt/hwloc-2.0.4/hwloc/.libs/libhwloc.a(topology-xml-libxml.o): In function `hwloc_libxml_free_buffers':
/opt/hwloc-2.0.4/hwloc/topology-xml-libxml.c:244: undefined reference to `xmlFreeDoc'
/opt/hwloc-2.0.4/hwloc/.libs/libhwloc.a(topology-xml-libxml.o): In function `hwloc__libxml_export_new_child':
/opt/hwloc-2.0.4/hwloc/topology-xml-libxml.c:411: undefined reference to `xmlNewChild'
/opt/hwloc-2.0.4/hwloc/.libs/libhwloc.a(topology-xml-libxml.o): In function `hwloc_libxml_free_buffers':
/opt/hwloc-2.0.4/hwloc/topology-xml-libxml.c:244: undefined reference to `xmlFreeDoc'
/opt/hwloc-2.0.4/hwloc/.libs/libhwloc.a(topology-xml-libxml.o): In function `hwloc_libxml_look_init':
/opt/hwloc-2.0.4/hwloc/topology-xml-libxml.c:185: undefined reference to `xmlGetIntSubset'
/opt/hwloc-2.0.4/hwloc/topology-xml-libxml.c:197: undefined reference to `xmlDocGetRootElement'
/opt/hwloc-2.0.4/hwloc/topology-xml-libxml.c:204: undefined reference to `xmlGetProp'
/opt/hwloc-2.0.4/hwloc/topology-xml-libxml.c:212: undefined reference to `xmlFree'
/opt/hwloc-2.0.4/hwloc/.libs/libhwloc.a(topology-xml-libxml.o): In function `hwloc_libxml2_init_once':
/opt/hwloc-2.0.4/hwloc/topology-xml-libxml.c:36: undefined reference to `xmlSetGenericErrorFunc'
/opt/hwloc-2.0.4/hwloc/topology-xml-libxml.c:36: undefined reference to `__xmlGenericError'
/opt/hwloc-2.0.4/hwloc/.libs/libhwloc.a(topology-xml-libxml.o): In function `hwloc__libxml2_prepare_export_diff':
/opt/hwloc-2.0.4/hwloc/topology-xml-libxml.c:523: undefined reference to `xmlCheckVersion'
/opt/hwloc-2.0.4/hwloc/topology-xml-libxml.c:527: undefined reference to `xmlNewDoc'
/opt/hwloc-2.0.4/hwloc/topology-xml-libxml.c:528: undefined reference to `xmlNewNode'
/opt/hwloc-2.0.4/hwloc/topology-xml-libxml.c:530: undefined reference to `xmlNewProp'
/opt/hwloc-2.0.4/hwloc/topology-xml-libxml.c:531: undefined reference to `xmlDocSetRootElement'
/opt/hwloc-2.0.4/hwloc/topology-xml-libxml.c:534: undefined reference to `xmlCreateIntSubset'
/opt/hwloc-2.0.4/hwloc/.libs/libhwloc.a(topology-xml-libxml.o): In function `hwloc_libxml_export_diff_buffer':
/opt/hwloc-2.0.4/hwloc/topology-xml-libxml.c:576: undefined reference to `xmlDocDumpFormatMemoryEnc'
/opt/hwloc-2.0.4/hwloc/topology-xml-libxml.c:577: undefined reference to `xmlFreeDoc'
/opt/hwloc-2.0.4/hwloc/.libs/libhwloc.a(topology-xml-libxml.o): In function `hwloc_libxml2_cleanup':
/opt/hwloc-2.0.4/hwloc/topology-xml-libxml.c:48: undefined reference to `xmlCleanupParser'
/opt/hwloc-2.0.4/hwloc/.libs/libhwloc.a(topology-xml-libxml.o): In function `hwloc_libxml_export_diff_file':
/opt/hwloc-2.0.4/hwloc/topology-xml-libxml.c:557: undefined reference to `xmlSaveFormatFileEnc'
/opt/hwloc-2.0.4/hwloc/topology-xml-libxml.c:558: undefined reference to `xmlFreeDoc'
/opt/hwloc-2.0.4/hwloc/.libs/libhwloc.a(topology-xml-libxml.o): In function `hwloc_libxml2_cleanup':
/opt/hwloc-2.0.4/hwloc/topology-xml-libxml.c:48: undefined reference to `xmlCleanupParser'
/opt/hwloc-2.0.4/hwloc/.libs/libhwloc.a(topology-xml-libxml.o): In function `hwloc_libxml_import_diff':
/opt/hwloc-2.0.4/hwloc/topology-xml-libxml.c:267: undefined reference to `xmlCheckVersion'
/opt/hwloc-2.0.4/hwloc/topology-xml-libxml.c:273: undefined reference to `xmlReadFile'
/opt/hwloc-2.0.4/hwloc/topology-xml-libxml.c:285: undefined reference to `xmlGetIntSubset'
/opt/hwloc-2.0.4/hwloc/topology-xml-libxml.c:296: undefined reference to `xmlDocGetRootElement'
/opt/hwloc-2.0.4/hwloc/topology-xml-libxml.c:334: undefined reference to `xmlFreeDoc'
/opt/hwloc-2.0.4/hwloc/.libs/libhwloc.a(topology-xml-libxml.o): In function `hwloc_libxml2_cleanup':
/opt/hwloc-2.0.4/hwloc/topology-xml-libxml.c:48: undefined reference to `xmlCleanupParser'
/opt/hwloc-2.0.4/hwloc/.libs/libhwloc.a(topology-xml-libxml.o): In function `hwloc_libxml_import_diff':
/opt/hwloc-2.0.4/hwloc/topology-xml-libxml.c:275: undefined reference to `xmlReadMemory'
/opt/hwloc-2.0.4/hwloc/.libs/libhwloc.a(topology-xml-libxml.o): In function `hwloc_libxml2_cleanup':
/opt/hwloc-2.0.4/hwloc/topology-xml-libxml.c:48: undefined reference to `xmlCleanupParser'
/opt/hwloc-2.0.4/hwloc/.libs/libhwloc.a(topology-xml-libxml.o): In function `hwloc_libxml_import_diff':
/opt/hwloc-2.0.4/hwloc/topology-xml-libxml.c:340: undefined reference to `xmlFreeDoc'
/opt/hwloc-2.0.4/hwloc/.libs/libhwloc.a(topology-xml-libxml.o): In function `hwloc__libxml2_prepare_export':
/opt/hwloc-2.0.4/hwloc/topology-xml-libxml.c:446: undefined reference to `xmlCheckVersion'
/opt/hwloc-2.0.4/hwloc/topology-xml-libxml.c:450: undefined reference to `xmlNewDoc'
/opt/hwloc-2.0.4/hwloc/topology-xml-libxml.c:451: undefined reference to `xmlNewNode'
/opt/hwloc-2.0.4/hwloc/topology-xml-libxml.c:454: undefined reference to `xmlDocSetRootElement'
/opt/hwloc-2.0.4/hwloc/topology-xml-libxml.c:457: undefined reference to `xmlCreateIntSubset'
/opt/hwloc-2.0.4/hwloc/topology-xml-libxml.c:453: undefined reference to `xmlNewProp'
/opt/hwloc-2.0.4/hwloc/.libs/libhwloc.a(topology-xml-libxml.o): In function `hwloc_libxml_export_buffer':
/opt/hwloc-2.0.4/hwloc/topology-xml-libxml.c:502: undefined reference to `xmlDocDumpFormatMemoryEnc'
/opt/hwloc-2.0.4/hwloc/topology-xml-libxml.c:503: undefined reference to `xmlFreeDoc'
/opt/hwloc-2.0.4/hwloc/.libs/libhwloc.a(topology-xml-libxml.o): In function `hwloc_libxml2_cleanup':
/opt/hwloc-2.0.4/hwloc/topology-xml-libxml.c:48: undefined reference to `xmlCleanupParser'
/opt/hwloc-2.0.4/hwloc/.libs/libhwloc.a(topology-xml-libxml.o): In function `hwloc_libxml_export_file':
/opt/hwloc-2.0.4/hwloc/topology-xml-libxml.c:482: undefined reference to `xmlSaveFormatFileEnc'
/opt/hwloc-2.0.4/hwloc/topology-xml-libxml.c:483: undefined reference to `xmlFreeDoc'
/opt/hwloc-2.0.4/hwloc/.libs/libhwloc.a(topology-xml-libxml.o): In function `hwloc_libxml2_cleanup':
/opt/hwloc-2.0.4/hwloc/topology-xml-libxml.c:48: undefined reference to `xmlCleanupParser'
/opt/hwloc-2.0.4/hwloc/.libs/libhwloc.a(topology-xml-libxml.o): In function `hwloc_libxml_backend_init':
/opt/hwloc-2.0.4/hwloc/topology-xml-libxml.c:363: undefined reference to `xmlCheckVersion'
/opt/hwloc-2.0.4/hwloc/topology-xml-libxml.c:369: undefined reference to `xmlReadFile'
/opt/hwloc-2.0.4/hwloc/topology-xml-libxml.c:371: undefined reference to `xmlReadMemory'
/opt/hwloc-2.0.4/hwloc/.libs/libhwloc.a(topology-xml-libxml.o): In function `hwloc_libxml2_cleanup':
/opt/hwloc-2.0.4/hwloc/topology-xml-libxml.c:48: undefined reference to `xmlCleanupParser'
/opt/hwloc-2.0.4/hwloc/.libs/libhwloc.a(topology-xml-libxml.o): In function `hwloc__libxml_export_new_prop':
/opt/hwloc-2.0.4/hwloc/topology-xml-libxml.c:418: undefined reference to `xmlNewProp'
/opt/hwloc-2.0.4/hwloc/.libs/libhwloc.a(topology-xml-libxml.o): In function `hwloc__libxml_export_add_content':
/opt/hwloc-2.0.4/hwloc/topology-xml-libxml.c:431: undefined reference to `xmlNodeAddContentLen'
/opt/hwloc-2.0.4/hwloc/.libs/libhwloc.a(topology-xml-libxml.o): In function `hwloc_libxml2_cleanup':
/opt/hwloc-2.0.4/hwloc/topology-xml-libxml.c:48: undefined reference to `xmlCleanupParser'
/opt/hwloc-2.0.4/hwloc/topology-xml-libxml.c:48: undefined reference to `xmlCleanupParser'
collect2: error: ld returned 1 exit status
make[2]: *** [CMakeFiles/xmrig.dir/build.make:3012: xmrig] Error 1
make[1]: *** [CMakeFiles/Makefile2:68: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:84: all] Error 2

```

## xmrig | 2019-08-08T12:56:53+00:00
Okay I updated manual, `./configure` need extra options `--disable-libudev --disable-libxml2`

## xmrig | 2019-08-10T12:33:05+00:00
#1111 

## sloppycoffee | 2019-09-19T17:53:39+00:00
> Using the Pre-compiled version of XMRig my results for RandomX test are:
> 
> [2019-08-04 13:46:55.611] speed 10s/60s/15m 10193.6 10192.3 n/a H/s max 10196.4 H/s
> 
> The 10196 H/s is only 3.9% lower than the 10612 I was getting with randomx-benchmark so I believe that this hash rate of 10196 is very acceptable as this is a REAL miner and probably has some overhead compared to just the randomx-benchmark program.
> 
> Well Done.

Hey what speed ram and size and amount of sticks did you use? DDR3? 1600mhz? 16 4gb sticks?

## duku1 | 2019-10-04T11:14:38+00:00
Hi, what wrong? I have 2 times less hashrate than I can see in test from others.
`* ABOUT        XMRig/4.2.1-beta gcc/9.2.0
 * LIBS         libuv/1.31.0 OpenSSL/1.1.1c hwloc/2.0.4
 * HUGE PAGES   permission granted
 * CPU          AMD Opteron(TM) Processor 6272 (4) x64 AES
                L2:64.0 MB L3:48.0 MB 32C/64T NUMA:8
 * DONATE       1%
 * ASSEMBLY     auto:bulldozer
 * POOL #1      pool.loki.hashvault.pro:3333 algo auto
 * COMMANDS     hashrate, pause, resume
 * OPENCL       disabled
[2019-10-04 14:07:58.210] use pool pool.loki.hashvault.pro:3333  193.164.16.124
[2019-10-04 14:07:58.210] new job from pool.loki.hashvault.pro:3333 diff 30000 algo rx/loki height 373018
[2019-10-04 14:07:58.226]  rx   init datasets algo rx/loki (6 threads) seed e3e6be0bc7258fd7...
[2019-10-04 14:07:58.241]  rx   #0 allocate 2336 MB (2080+256) for RandomX dataset & cache
[2019-10-04 14:07:58.273]  rx   #0 allocate done huge pages 1168/1168 100% +JIT (39 ms)
[2019-10-04 14:08:00.007] new job from pool.loki.hashvault.pro:3333 diff 56250 algo rx/loki height 373018
[2019-10-04 14:08:12.788]  rx   #0 init done 1/8 (14556 ms)
[2019-10-04 14:08:12.804]  rx   #4 allocate 2336 MB (2080+256) for RandomX dataset & cache
[2019-10-04 14:08:12.835]  rx   #4 allocate done huge pages 1168/1168 100% +JIT (41 ms)
[2019-10-04 14:08:27.367]  rx   #4 init done 2/8 (14576 ms)
[2019-10-04 14:08:27.382]  rx   #5 allocate 2336 MB (2080+256) for RandomX dataset & cache
[2019-10-04 14:08:27.414]  rx   #5 allocate done huge pages 1168/1168 100% +JIT (55 ms)
[2019-10-04 14:08:41.789]  rx   #5 init done 3/8 (14420 ms)
[2019-10-04 14:08:41.789]  rx   #1 allocate 2336 MB (2080+256) for RandomX dataset & cache
[2019-10-04 14:08:41.836]  rx   #1 allocate done huge pages 1168/1168 100% +JIT (42 ms)
[2019-10-04 14:08:56.836]  rx   #1 init done 4/8 (15051 ms)
[2019-10-04 14:08:56.851]  rx   #3 allocate 2336 MB (2080+256) for RandomX dataset & cache
[2019-10-04 14:08:56.883]  rx   #3 allocate done huge pages 1168/1168 100% +JIT (39 ms)
[2019-10-04 14:09:11.273]  rx   #3 init done 5/8 (14429 ms)
[2019-10-04 14:09:11.273]  rx   #2 allocate 2336 MB (2080+256) for RandomX dataset & cache
[2019-10-04 14:09:11.304]  rx   #2 allocate done huge pages 1168/1168 100% +JIT (42 ms)
[2019-10-04 14:09:25.742]  rx   #2 init done 6/8 (14464 ms)
[2019-10-04 14:09:25.742]  rx   #6 allocate 2336 MB (2080+256) for RandomX dataset & cache
[2019-10-04 14:09:25.773]  rx   #6 allocate done huge pages 1168/1168 100% +JIT (41 ms)
[2019-10-04 14:09:40.445]  rx   #6 init done 7/8 (14707 ms)
[2019-10-04 14:09:40.461]  rx   #7 allocate 2336 MB (2080+256) for RandomX dataset & cache
[2019-10-04 14:09:40.492]  rx   #7 allocate done huge pages 1168/1168 100% +JIT (42 ms)
[2019-10-04 14:09:55.367]  rx   #7 init done 8/8 (14920 ms)
[2019-10-04 14:09:55.367]  cpu  use profile  rx  (56 threads) scratchpad 2048 KB
[2019-10-04 14:09:55.398] new job from pool.loki.hashvault.pro:3333 diff 37499 algo rx/loki height 373018
[2019-10-04 14:09:55.414] new job from pool.loki.hashvault.pro:3333 diff 37499 algo rx/loki height 373018
[2019-10-04 14:09:55.414] new job from pool.loki.hashvault.pro:3333 diff 37499 algo rx/loki height 373019
[2019-10-04 14:09:55.414] new job from pool.loki.hashvault.pro:3333 diff 37499 algo rx/loki height 373020
[2019-10-04 14:09:55.555]  cpu  READY threads 56/56 (56) huge pages 56/56 100% memory 114688 KB (188 ms)
[2019-10-04 14:10:00.023] new job from pool.loki.hashvault.pro:3333 diff 24999 algo rx/loki height 373020
[2019-10-04 14:10:00.461] accepted (1/0) diff 24999 (46 ms)
...
[2019-10-04 14:10:54.008] accepted (17/0) diff 24999 (34 ms)
[2019-10-04 14:10:55.946] speed 10s/60s/15m 4486.4 4481.5 n/a H/s max 4494.1 H/s`

# Action History
- Created by: kio3i0j9024vkoenio | 2019-08-04T16:14:31+00:00
- Closed at: 2019-08-10T12:33:05+00:00
