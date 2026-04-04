---
title: monerod segfaults if unbound is not compiled with pthreads support
source_url: https://github.com/monero-project/monero/issues/1073
author: alown
assignees: []
labels: []
created_at: '2016-09-14T20:50:32+00:00'
updated_at: '2018-06-18T15:33:13+00:00'
type: issue
status: closed
closed_at: '2018-06-18T15:33:13+00:00'
---

# Original Description
Attempting to run monerod with unbound compiled without pthreads, produces something like the below trace. Compiling unbound with pthreads resolves the issue.

It is definitely worth adding a note to the readme, and potentially worth adding an extra check to cmake.

```
$ gdb monerod                                                                                                                                                                                                                                                                                                                                                                                                        [139] [21:41:12]
GNU gdb (GDB) 7.10
Copyright (C) 2015 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-pc-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from monerod...Reading symbols from /usr/x86_64-pc-linux-gnu/lib/debug//usr/x86_64-pc-linux-gnu/bin/monerod.debug...done.
done.
(gdb) run
Starting program: /usr/x86_64-pc-linux-gnu/bin/monerod 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/usr/x86_64-pc-linux-gnu/lib/libthread_db.so.1".
Creating the logger system
2016-Sep-14 21:41:14.635532 Initializing cryptonote protocol...
2016-Sep-14 21:41:14.635587 Cryptonote protocol initialized OK
2016-Sep-14 21:41:14.635736 Initializing p2p server...
[New Thread 0x7ffff2b16700 (LWP 25564)]
[New Thread 0x7ffff2315700 (LWP 25565)]
[New Thread 0x7ffff1b14700 (LWP 25566)]
[New Thread 0x7ffff1313700 (LWP 25567)]
*** Error in `/usr/x86_64-pc-linux-gnu/bin/monerod': double free or corruption (fasttop): 0x00007fffe41c3b50 ***
======= Backtrace: =========
/usr/x86_64-pc-linux-gnu/lib/libc.so.6(+0x70ec6)[0x7ffff5703ec6]
/usr/x86_64-pc-linux-gnu/lib/libc.so.6(+0x76425)[0x7ffff5709425]
/usr/x86_64-pc-linux-gnu/lib/libc.so.6(+0x76bee)[0x7ffff5709bee]
/usr/x86_64-pc-linux-gnu/lib/libunbound.so.2(+0x477af)[0x7ffff651f7af]
/usr/x86_64-pc-linux-gnu/lib/libunbound.so.2(+0x4e593)[0x7ffff6526593]
/usr/x86_64-pc-linux-gnu/lib/libunbound.so.2(+0x3f763)[0x7ffff6517763]
/usr/x86_64-pc-linux-gnu/lib/libunbound.so.2(+0x1a129)[0x7ffff64f2129]
/usr/x86_64-pc-linux-gnu/lib/libunbound.so.2(+0x52f45)[0x7ffff652af45]
/usr/x86_64-pc-linux-gnu/lib/libunbound.so.2(+0x49536)[0x7ffff6521536]
/usr/x86_64-pc-linux-gnu/lib/libunbound.so.2(+0x4dfe2)[0x7ffff6525fe2]
/usr/x86_64-pc-linux-gnu/lib/libunbound.so.2(+0x411d2)[0x7ffff65191d2]
/usr/x86_64-pc-linux-gnu/lib/libunbound.so.2(+0x42010)[0x7ffff651a010]
/usr/x86_64-pc-linux-gnu/lib/libunbound.so.2(+0x58bed)[0x7ffff6530bed]
/usr/x86_64-pc-linux-gnu/lib/libunbound.so.2(+0x25842)[0x7ffff64fd842]
/usr/x86_64-pc-linux-gnu/lib/libevent-2.0.so.5(event_base_loop+0x7c6)[0x7ffff2f59fde]
/usr/x86_64-pc-linux-gnu/lib/libunbound.so.2(+0x25a16)[0x7ffff64fda16]
/usr/x86_64-pc-linux-gnu/lib/libunbound.so.2(ub_resolve+0x136)[0x7ffff6538d16]
/usr/x86_64-pc-linux-gnu/bin/monerod(_ZN5tools11DNSResolver10get_recordERKSsiPFSsPKcmERbS7_+0x88)[0x82fe08]
/usr/x86_64-pc-linux-gnu/bin/monerod(_ZN5tools11DNSResolver8get_ipv4ERKSsRbS3_+0x1d)[0x83000d]
/usr/x86_64-pc-linux-gnu/bin/monerod(_ZZN8nodetool11node_serverIN10cryptonote29t_cryptonote_protocol_handlerINS1_4coreEEEE4initERKN5boost15program_options13variables_mapEENKUlvE_clEv+0x16b)[0x5d5d5b]
/usr/x86_64-pc-linux-gnu/lib/libboost_thread.so.1.61.0(+0x12fb5)[0x7ffff6bebfb5]
/usr/x86_64-pc-linux-gnu/lib/libpthread.so.0(+0x73fc)[0x7ffff5a3c3fc]
/usr/x86_64-pc-linux-gnu/lib/libc.so.6(clone+0x6d)[0x7ffff5779e8d]
======= Memory map: ========
00400000-00a14000 r-xp 00000000 08:05 103544521                          /usr/x86_64-pc-linux-gnu/bin/monerod
00c13000-02a9a000 rwxp 00613000 08:05 103544521                          /usr/x86_64-pc-linux-gnu/bin/monerod
02a9a000-02ad0000 rwxp 00000000 00:00 0                                  [heap]
7fffdc000000-7fffdc295000 rwxp 00000000 00:00 0 
7fffdc295000-7fffe0000000 ---p 00000000 00:00 0 
7fffe0000000-7fffe0021000 rwxp 00000000 00:00 0 
7fffe0021000-7fffe4000000 ---p 00000000 00:00 0 
7fffe4000000-7fffe4295000 rwxp 00000000 00:00 0 
7fffe4295000-7fffe8000000 ---p 00000000 00:00 0 
7fffe8000000-7fffe8295000 rwxp 00000000 00:00 0 
7fffe8295000-7fffec000000 ---p 00000000 00:00 0 
7fffec000000-7fffec2d6000 rwxp 00000000 00:00 0 
7fffec2d6000-7ffff0000000 ---p 00000000 00:00 0 
7ffff08fd000-7ffff0912000 r-xp 00000000 08:05 110955                     /usr/x86_64-pc-linux-gnu/lib/libgcc_s-5.1.so.1
7ffff0912000-7ffff0b12000 ---p 00015000 08:05 110955                     /usr/x86_64-pc-linux-gnu/lib/libgcc_s-5.1.so.1
7ffff0b12000-7ffff0b13000 rwxp 00015000 08:05 110955                     /usr/x86_64-pc-linux-gnu/lib/libgcc_s-5.1.so.1
7ffff0b13000-7ffff0b14000 ---p 00000000 00:00 0 
7ffff0b14000-7ffff1314000 rwxp 00000000 00:00 0 
7ffff1314000-7ffff1315000 ---p 00000000 00:00 0 
7ffff1315000-7ffff1b15000 rwxp 00000000 00:00 0 
7ffff1b15000-7ffff1b16000 ---p 00000000 00:00 0 
7ffff1b16000-7ffff2316000 rwxp 00000000 00:00 0 
7ffff2316000-7ffff2317000 ---p 00000000 00:00 0 
7ffff2317000-7ffff2b17000 rwxp 00000000 00:00 0 
7ffff2b17000-7ffff2d1e000 r-xp 00000000 08:05 1840863                    /usr/x86_64-pc-linux-gnu/lib/libcrypto.so.1.0.0
7ffff2d1e000-7ffff2f1d000 ---p 00207000 08:05 1840863                    /usr/x86_64-pc-linux-gnu/lib/libcrypto.so.1.0.0
7ffff2f1d000-7ffff2f46000 rwxp 00206000 08:05 1840863                    /usr/x86_64-pc-linux-gnu/lib/libcrypto.so.1.0.0
7ffff2f46000-7ffff2f4a000 rwxp 00000000 00:00 0 
7ffff2f4a000-7ffff2f8e000 r-xp 00000000 08:05 67151891                   /usr/x86_64-pc-linux-gnu/lib/libevent-2.0.so.5.1.9
7ffff2f8e000-7ffff318e000 ---p 00044000 08:05 67151891                   /usr/x86_64-pc-linux-gnu/lib/libevent-2.0.so.5.1.9
7ffff318e000-7ffff3190000 rwxp 00044000 08:05 67151891                   /usr/x86_64-pc-linux-gnu/lib/libevent-2.0.so.5.1.9
7ffff3190000-7ffff31f9000 r-xp 00000000 08:05 2136522                    /usr/x86_64-pc-linux-gnu/lib/libssl.so.1.0.0
7ffff31f9000-7ffff33f8000 ---p 00069000 08:05 2136522                    /usr/x86_64-pc-linux-gnu/lib/libssl.so.1.0.0
7ffff33f8000-7ffff3403000 rwxp 00068000 08:05 2136522                    /usr/x86_64-pc-linux-gnu/lib/libssl.so.1.0.0
7ffff3403000-7ffff3592000 r-xp 00000000 08:05 979254                     /usr/x86_64-pc-linux-gnu/lib/libicuuc.so.57.1
7ffff3592000-7ffff3792000 ---p 0018f000 08:05 979254                     /usr/x86_64-pc-linux-gnu/lib/libicuuc.so.57.1
7ffff3792000-7ffff37a4000 rwxp 0018f000 08:05 979254                     /usr/x86_64-pc-linux-gnu/lib/libicuuc.so.57.1
7ffff37a4000-7ffff37a7000 rwxp 00000000 00:00 0 
7ffff37a7000-7ffff3a08000 r-xp 00000000 08:05 979256                     /usr/x86_64-pc-linux-gnu/lib/libicui18n.so.57.1
7ffff3a08000-7ffff3c08000 ---p 00261000 08:05 979256                     /usr/x86_64-pc-linux-gnu/lib/libicui18n.so.57.1
7ffff3c08000-7ffff3c16000 rwxp 00261000 08:05 979256                     /usr/x86_64-pc-linux-gnu/lib/libicui18n.so.57.1
7ffff3c16000-7ffff3c17000 rwxp 00000000 00:00 0 
7ffff3c17000-7ffff5493000 r-xp 00000000 08:05 979255                     /usr/x86_64-pc-linux-gnu/lib/libicudata.so.57.1
7ffff5493000-7ffff5692000 ---p 0187c000 08:05 979255                     /usr/x86_64-pc-linux-gnu/lib/libicudata.so.57.1
7ffff5692000-7ffff5693000 rwxp 0187b000 08:05 979255                     /usr/x86_64-pc-linux-gnu/lib/libicudata.so.57.1
7ffff5693000-7ffff582b000 r-xp 00000000 08:05 602656                     /usr/x86_64-pc-linux-gnu/lib/libc-2.22.so
7ffff582b000-7ffff5a2b000 ---p 00198000 08:05 602656                     /usr/x86_64-pc-linux-gnu/lib/libc-2.22.so
7ffff5a2b000-7ffff5a2f000 r-xp 00198000 08:05 602656                     /usr/x86_64-pc-linux-gnu/lib/libc-2.22.so
7ffff5a2f000-7ffff5a31000 rwxp 0019c000 08:05 602656                     /usr/x86_64-pc-linux-gnu/lib/libc-2.22.so
7ffff5a31000-7ffff5a35000 rwxp 00000000 00:00 0 
7ffff5a35000-7ffff5a4d000 r-xp 00000000 08:05 602379                     /usr/x86_64-pc-linux-gnu/lib/libpthread-2.22.so
7ffff5a4d000-7ffff5c4c000 ---p 00018000 08:05 602379                     /usr/x86_64-pc-linux-gnu/lib/libpthread-2.22.so
7ffff5c4c000-7ffff5c4d000 r-xp 00017000 08:05 602379                     /usr/x86_64-pc-linux-gnu/lib/libpthread-2.22.so
7ffff5c4d000-7ffff5c4e000 rwxp 00018000 08:05 602379                     /usr/x86_64-pc-linux-gnu/lib/libpthread-2.22.so
7ffff5c4e000-7ffff5c52000 rwxp 00000000 00:00 0 
7ffff5c52000-7ffff5d42000 r-xp 00000000 08:05 112380                     /usr/x86_64-pc-linux-gnu/lib/libm-2.22.so
7ffff5d42000-7ffff5f41000 ---p 000f0000 08:05 112380                     /usr/x86_64-pc-linux-gnu/lib/libm-2.22.so
7ffff5f41000-7ffff5f42000 r-xp 000ef000 08:05 112380                     /usr/x86_64-pc-linux-gnu/lib/libm-2.22.so
7ffff5f42000-7ffff5f43000 rwxp 000f0000 08:05 112380                     /usr/x86_64-pc-linux-gnu/lib/libm-2.22.so
7ffff5f43000-7ffff60b3000 r-xp 00000000 08:05 110924                     /usr/x86_64-pc-linux-gnu/lib/libstdc++-5.1.so.6.0.21
7ffff60b3000-7ffff62b2000 ---p 00170000 08:05 110924                     /usr/x86_64-pc-linux-gnu/lib/libstdc++-5.1.so.6.0.21
7ffff62b2000-7ffff62bc000 r-xp 0016f000 08:05 110924                     /usr/x86_64-pc-linux-gnu/lib/libstdc++-5.1.so.6.0.21
7ffff62bc000-7ffff62be000 rwxp 00179000 08:05 110924                     /usr/x86_64-pc-linux-gnu/lib/libstdc++-5.1.so.6.0.21
7ffff62be000-7ffff62c2000 rwxp 00000000 00:00 0 
7ffff62c2000-7ffff62d7000 r-xp 00000000 08:05 11300453                   /usr/x86_64-pc-linux-gnu/lib/libboost_date_time.so.1.61.0
7ffff62d7000-7ffff64d6000 ---p 00015000 08:05 11300453                   /usr/x86_64-pc-linux-gnu/lib/libboost_date_time.so.1.61.0
7ffff64d6000-7ffff64d8000 rwxp 00014000 08:05 11300453                   /usr/x86_64-pc-linux-gnu/lib/libboost_date_time.so.1.61.0
7ffff64d8000-7ffff6564000 r-xp 00000000 08:05 5201688                    /usr/x86_64-pc-linux-gnu/lib/libunbound.so.2.4.1
7ffff6564000-7ffff6763000 ---p 0008c000 08:05 5201688                    /usr/x86_64-pc-linux-gnu/lib/libunbound.so.2.4.1
7ffff6763000-7ffff6768000 rwxp 0008b000 08:05 5201688                    /usr/x86_64-pc-linux-gnu/lib/libunbound.so.2.4.1
7ffff6768000-7ffff67cb000 r-xp 00000000 08:05 11300463                   /usr/x86_64-pc-linux-gnu/lib/libboost_serialization.so.1.61.0
7ffff67cb000-7ffff69ca000 ---p 00063000 08:05 11300463                   /usr/x86_64-pc-linux-gnu/lib/libboost_serialization.so.1.61.0
7ffff69ca000-7ffff69ce000 rwxp 00062000 08:05 11300463                   /usr/x86_64-pc-linux-gnu/lib/libboost_serialization.so.1.61.0
7ffff69ce000-7ffff69d8000 r-xp 00000000 08:05 604402                     /usr/x86_64-pc-linux-gnu/lib/libminiupnpc.so.9
7ffff69d8000-7ffff6bd8000 ---p 0000a000 08:05 604402                     /usr/x86_64-pc-linux-gnu/lib/libminiupnpc.so.9
7ffff6bd8000-7ffff6bd9000 rwxp 0000a000 08:05 604402                     /usr/x86_64-pc-linux-gnu/lib/libminiupnpc.so.9
7ffff6bd9000-7ffff6c04000 r-xp 00000000 08:05 7868548                    /usr/x86_64-pc-linux-gnu/lib/libboost_thread.so.1.61.0
7ffff6c04000-7ffff6e04000 ---p 0002b000 08:05 7868548                    /usr/x86_64-pc-linux-gnu/lib/libboost_thread.so.1.61.0
7ffff6e04000-7ffff6e06000 rwxp 0002b000 08:05 7868548                    /usr/x86_64-pc-linux-gnu/lib/libboost_thread.so.1.61.0
7ffff6e06000-7ffff6e0e000 r-xp 00000000 08:05 7868539                    /usr/x86_64-pc-linux-gnu/lib/libboost_system.so.1.61.0
7ffff6e0e000-7ffff700e000 ---p 00008000 08:05 7868539                    /usr/x86_64-pc-linux-gnu/lib/libboost_system.so.1.61.0
7ffff700e000-7ffff700f000 rwxp 00008000 08:05 7868539                    /usr/x86_64-pc-linux-gnu/lib/libboost_system.so.1.61.0
7ffff700f000-7ffff711d000 r-xp 00000000 08:05 11300462                   /usr/x86_64-pc-linux-gnu/lib/libboost_regex.so.1.61.0
7ffff711d000-7ffff731c000 ---p 0010e000 08:05 11300462                   /usr/x86_64-pc-linux-gnu/lib/libboost_regex.so.1.61.0
7ffff731c000-7ffff7323000 rwxp 0010d000 08:05 11300462                   /usr/x86_64-pc-linux-gnu/lib/libboost_regex.so.1.61.0
7ffff7323000-7ffff73a1000 r-xp 00000000 08:05 11300461                   /usr/x86_64-pc-linux-gnu/lib/libboost_program_options.so.1.61.0
7ffff73a1000-7ffff75a1000 ---p 0007e000 08:05 11300461                   /usr/x86_64-pc-linux-gnu/lib/libboost_program_options.so.1.61.0
7ffff75a1000-7ffff75a5000 rwxp 0007e000 08:05 11300461                   /usr/x86_64-pc-linux-gnu/lib/libboost_program_options.so.1.61.0
7ffff75a5000-7ffff75c2000 r-xp 00000000 08:05 11300466                   /usr/x86_64-pc-linux-gnu/lib/libboost_filesystem.so.1.61.0
7ffff75c2000-7ffff77c2000 ---p 0001d000 08:05 11300466                   /usr/x86_64-pc-linux-gnu/lib/libboost_filesystem.so.1.61.0
7ffff77c2000-7ffff77c3000 rwxp 0001d000 08:05 11300466                   /usr/x86_64-pc-linux-gnu/lib/libboost_filesystem.so.1.61.0
7ffff77c3000-7ffff77cf000 r-xp 00000000 08:05 7868540                    /usr/x86_64-pc-linux-gnu/lib/libboost_chrono.so.1.61.0
7ffff77cf000-7ffff79ce000 ---p 0000c000 08:05 7868540                    /usr/x86_64-pc-linux-gnu/lib/libboost_chrono.so.1.61.0
7ffff79ce000-7ffff79cf000 rwxp 0000b000 08:05 7868540                    /usr/x86_64-pc-linux-gnu/lib/libboost_chrono.so.1.61.0
7ffff79cf000-7ffff79d1000 r-xp 00000000 08:05 602347                     /usr/x86_64-pc-linux-gnu/lib/libdl-2.22.so
7ffff79d1000-7ffff7bd1000 ---p 00002000 08:05 602347                     /usr/x86_64-pc-linux-gnu/lib/libdl-2.22.so
7ffff7bd1000-7ffff7bd2000 r-xp 00002000 08:05 602347                     /usr/x86_64-pc-linux-gnu/lib/libdl-2.22.so
7ffff7bd2000-7ffff7bd3000 rwxp 00003000 08:05 602347                     /usr/x86_64-pc-linux-gnu/lib/libdl-2.22.so
7ffff7bd3000-7ffff7bda000 r-xp 00000000 08:05 602481                     /usr/x86_64-pc-linux-gnu/lib/librt-2.22.so
7ffff7bda000-7ffff7dd9000 ---p 00007000 08:05 602481                     /usr/x86_64-pc-linux-gnu/lib/librt-2.22.so
7ffff7dd9000-7ffff7dda000 r-xp 00006000 08:05 602481                     /usr/x86_64-pc-linux-gnu/lib/librt-2.22.so
7ffff7dda000-7ffff7ddb000 rwxp 00007000 08:05 602481                     /usr/x86_64-pc-linux-gnu/lib/librt-2.22.so
7ffff7ddb000-7ffff7dfc000 r-xp 00000000 08:05 602373                     /usr/x86_64-pc-linux-gnu/lib/ld-2.22.so
7ffff7ecd000-7ffff7f43000 rwxp 00000000 00:00 0 
7ffff7f7e000-7ffff7fd2000 rwxp 00000000 00:00 0 
7ffff7ff2000-7ffff7ff7000 rwxp 00000000 00:00 0 
7ffff7ff7000-7ffff7ffa000 r--p 00000000 00:00 0                          [vvar]
7ffff7ffa000-7ffff7ffc000 r-xp 00000000 00:00 0                          [vdso]
7ffff7ffc000-7ffff7ffd000 r-xp 00021000 08:05 602373                     /usr/x86_64-pc-linux-gnu/lib/ld-2.22.so
7ffff7ffd000-7ffff7ffe000 rwxp 00022000 08:05 602373                     /usr/x86_64-pc-linux-gnu/lib/ld-2.22.so
7ffff7ffe000-7ffff7fff000 rwxp 00000000 00:00 0 
7ffffffde000-7ffffffff000 rwxp 00000000 00:00 0                          [stack]
ffffffffff600000-ffffffffff601000 r-xp 00000000 00:00 0                  [vsyscall]

Program received signal SIGABRT, Aborted.
[Switching to Thread 0x7ffff2b16700 (LWP 25564)]
0x00007ffff56c6037 in raise () from /usr/x86_64-pc-linux-gnu/lib/libc.so.6
(gdb) quit
A debugging session is active.

    Inferior 1 [process 25558] will be killed.

Quit anyway? (y or n) y

```


# Discussion History
## radfish | 2016-09-16T02:14:46+00:00
Thanks. Is it with a libunbound.so shipped by the distribution? If so which one? On Arch, ldd says libunbound.so depends on libpthread.so. 

UPDATE: also, could you specify what flags are needed when compiling libunbound? (is there a `configure` flag)?


## moneromooo-monero | 2016-09-17T15:46:41+00:00
Any chance you can run this with valgrind to see where it starts going wrong ?


## hyc | 2016-10-26T20:00:13+00:00
IMO we should stop listing unbound as a build dependency, and always just build/use the bundled copy.


## moneromooo-monero | 2018-01-26T19:14:27+00:00
monerod now warns if unbound was built without threads. 

## moneromooo-monero | 2018-06-18T15:10:01+00:00
Kinda resolved due to the above. Resolving since it appears to be a libunbound problem.

+resolved

# Action History
- Created by: alown | 2016-09-14T20:50:32+00:00
- Closed at: 2018-06-18T15:33:13+00:00
