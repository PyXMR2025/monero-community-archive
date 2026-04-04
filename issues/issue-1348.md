---
title: Wallet crashes when importing key images and outputs files
source_url: https://github.com/monero-project/monero/issues/1348
author: moneroexamples
assignees: []
labels: []
created_at: '2016-11-16T23:38:41+00:00'
updated_at: '2016-11-21T23:49:10+00:00'
type: issue
status: closed
closed_at: '2016-11-21T23:49:10+00:00'
---

# Original Description
Wanted to test new signing tx, but found that importing key images and output files crashes the wallet. 

```
[wallet 41vEA7]: import_key_images ki
*** Error in `/opt/monero/monero-wallet-cli': free(): corrupted unsorted chunks: 0x00005570a9a2cfb0 ***
======= Backtrace: =========
/lib/x86_64-linux-gnu/libc.so.6(+0x790cb)[0x7f90e7af20cb]
/lib/x86_64-linux-gnu/libc.so.6(+0x8275a)[0x7f90e7afb75a]
/lib/x86_64-linux-gnu/libc.so.6(cfree+0x4c)[0x7f90e7aff18c]
/opt/monero/monero-wallet-cli(_ZN10cryptonote13simple_wallet17import_key_imagesERKSt6vectorINSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEESaIS7_EE+0x181)[0x5570a6686661]
/opt/monero/monero-wallet-cli(_ZN4epee15command_handler19process_command_strERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE+0x39f)[0x5570a6670b5f]
/opt/monero/monero-wallet-cli(_ZN10cryptonote13simple_wallet3runEv+0xbcd)[0x5570a668f53d]
/opt/monero/monero-wallet-cli(main+0xfdb)[0x5570a665d29b]
/lib/x86_64-linux-gnu/libc.so.6(__libc_start_main+0xf1)[0x7f90e7a993f1]
/opt/monero/monero-wallet-cli(_start+0x2a)[0x5570a6669b1a]
======= Memory map: ========
5570a65bd000-5570a68db000 r-xp 00000000 08:01 4068770                    /opt/monero/monero-wallet-cli
5570a6ada000-5570a6aea000 r--p 0031d000 08:01 4068770                    /opt/monero/monero-wallet-cli
5570a6aea000-5570a6aeb000 rw-p 0032d000 08:01 4068770                    /opt/monero/monero-wallet-cli
5570a6aeb000-5570a6aef000 rw-p 00000000 00:00 0 
5570a81ca000-5570a9dcc000 rw-p 00000000 00:00 0                          [heap]
7f90c7979000-7f90cc000000 rw-p 00000000 00:00 0 
7f90cc000000-7f90cc043000 rw-p 00000000 00:00 0 
7f90cc043000-7f90d0000000 ---p 00000000 00:00 0 
7f90d0000000-7f90d0021000 rw-p 00000000 00:00 0 
7f90d0021000-7f90d4000000 ---p 00000000 00:00 0 
7f90d4000000-7f90d60fa000 rw-p 00000000 00:00 0 
7f90d60fa000-7f90d8000000 ---p 00000000 00:00 0 
7f90e0754000-7f90e0755000 ---p 00000000 00:00 0 
7f90e0755000-7f90e0f55000 rw-p 00000000 00:00 0 
7f90e0f55000-7f90e0f56000 ---p 00000000 00:00 0 
7f90e0f56000-7f90e1756000 rw-p 00000000 00:00 0 
7f90e1756000-7f90e1757000 ---p 00000000 00:00 0 
7f90e1757000-7f90e2158000 rw-p 00000000 00:00 0 
7f90e2158000-7f90e2159000 ---p 00000000 00:00 0 
7f90e2159000-7f90e2959000 rw-p 00000000 00:00 0 
7f90e2959000-7f90e41d5000 r-xp 00000000 08:01 4202074                    /usr/lib/x86_64-linux-gnu/libicudata.so.57.1
7f90e41d5000-7f90e43d4000 ---p 0187c000 08:01 4202074                    /usr/lib/x86_64-linux-gnu/libicudata.so.57.1
7f90e43d4000-7f90e43d5000 r--p 0187b000 08:01 4202074                    /usr/lib/x86_64-linux-gnu/libicudata.so.57.1
7f90e43d5000-7f90e43d6000 rw-p 0187c000 08:01 4202074                    /usr/lib/x86_64-linux-gnu/libicudata.so.57.1
7f90e43d6000-7f90e43f8000 r-xp 00000000 08:01 135787                     /lib/x86_64-linux-gnu/liblzma.so.5.0.0
7f90e43f8000-7f90e45f7000 ---p 00022000 08:01 135787                     /lib/x86_64-linux-gnu/liblzma.so.5.0.0
7f90e45f7000-7f90e45f8000 r--p 00021000 08:01 135787                     /lib/x86_64-linux-gnu/liblzma.so.5.0.0
7f90e45f8000-7f90e45f9000 rw-p 00022000 08:01 135787                     /lib/x86_64-linux-gnu/liblzma.so.5.0.0
7f90e45f9000-7f90e4812000 r-xp 00000000 08:01 135736                     /lib/x86_64-linux-gnu/libcrypto.so.1.0.0
7f90e4812000-7f90e4a12000 ---p 00219000 08:01 135736                     /lib/x86_64-linux-gnu/libcrypto.so.1.0.0
7f90e4a12000-7f90e4a2e000 r--p 00219000 08:01 135736                     /lib/x86_64-linux-gnu/libcrypto.so.1.0.0
7f90e4a2e000-7f90e4a3a000 rw-p 00235000 08:01 135736                     /lib/x86_64-linux-gnu/libcrypto.so.1.0.0
7f90e4a3a000-7f90e4a3d000 rw-p 00000000 00:00 0 
7f90e4a3d000-7f90e4a9b000 r-xp 00000000 08:01 135885                     /lib/x86_64-linux-gnu/libssl.so.1.0.0
7f90e4a9b000-7f90e4c9b000 ---p 0005e000 08:01 135885                     /lib/x86_64-linux-gnu/libssl.so.1.0.0
7f90e4c9b000-7f90e4c9f000 r--p 0005e000 08:01 135885                     /lib/x86_64-linux-gnu/libssl.so.1.0.0
7f90e4c9f000-7f90e4ca6000 rw-p 00062000 08:01 135885                     /lib/x86_64-linux-gnu/libssl.so.1.0.0
7f90e4ca6000-7f90e4e3a000 r-xp 00000000 08:01 4202088                    /usr/lib/x86_64-linux-gnu/libicuuc.so.57.1
7f90e4e3a000-7f90e5039000 ---p 00194000 08:01 4202088                    /usr/lib/x86_64-linux-gnu/libicuuc.so.57.1
7f90e5039000-7f90e504b000 r--p 00193000 08:01 4202088                    /usr/lib/x86_64-linux-gnu/libicuuc.so.57.1
7f90e504b000-7f90e504c000 rw-p 001a5000 08:01 4202088                    /usr/lib/x86_64-linux-gnu/libicuuc.so.57.1
7f90e504c000-7f90e504e000 rw-p 00000000 00:00 0 
7f90e504e000-7f90e52b9000 r-xp 00000000 08:01 4202076                    /usr/lib/x86_64-linux-gnu/libicui18n.so.57.1
7f90e52b9000-7f90e54b8000 ---p 0026b000 08:01 4202076                    /usr/lib/x86_64-linux-gnu/libicui18n.so.57.1
7f90e54b8000-7f90e54c5000 r--p 0026a000 08:01 4202076                    /usr/lib/x86_64-linux-gnu/libicui18n.so.57.1
7f90e54c5000-7f90e54c7000 rw-p 00277000 08:01 4202076                    /usr/lib/x86_64-linux-gnu/libicui18n.so.57.1
7f90e54c7000-7f90e54c8000 rw-p 00000000 00:00 0 
7f90e54c8000-7f90e54cf000 r-xp 00000000 08:01 135873                     /lib/x86_64-linux-gnu/librt-2.24.so
7f90e54cf000-7f90e56ce000 ---p 00007000 08:01 135873                     /lib/x86_64-linux-gnu/librt-2.24.so
7f90e56ce000-7f90e56cf000 r--p 00006000 08:01 135873                     /lib/x86_64-linux-gnu/librt-2.24.so
7f90e56cf000-7f90e56d0000 rw-p 00007000 08:01 135873                     /lib/x86_64-linux-gnu/librt-2.24.so
7f90e56d0000-7f90e56e8000 r-xp 00000000 08:01 135865                     /lib/x86_64-linux-gnu/libpthread-2.24.so
7f90e56e8000-7f90e58e8000 ---p 00018000 08:01 135865                     /lib/x86_64-linux-gnu/libpthread-2.24.so
7f90e58e8000-7f90e58e9000 r--p 00018000 08:01 135865                     /lib/x86_64-linux-gnu/libpthread-2.24.so
7f90e58e9000-7f90e58ea000 rw-p 00019000 08:01 135865                     /lib/x86_64-linux-gnu/libpthread-2.24.so
7f90e58ea000-7f90e58ee000 rw-p 00000000 00:00 0 
7f90e58ee000-7f90e5904000 r-xp 00000000 08:01 135762                     /lib/x86_64-linux-gnu/libgcc_s.so.1
7f90e5904000-7f90e5b03000 ---p 00016000 08:01 135762                     /lib/x86_64-linux-gnu/libgcc_s.so.1
7f90e5b03000-7f90e5b04000 r--p 00015000 08:01 135762                     /lib/x86_64-linux-gnu/libgcc_s.so.1
7f90e5b04000-7f90e5b05000 rw-p 00016000 08:01 135762                     /lib/x86_64-linux-gnu/libgcc_s.so.1
7f90e5b05000-7f90e5c0d000 r-xp 00000000 08:01 135790                     /lib/x86_64-linux-gnu/libm-2.24.so
7f90e5c0d000-7f90e5e0c000 ---p 00108000 08:01 135790                     /lib/x86_64-linux-gnu/libm-2.24.so
7f90e5e0c000-7f90e5e0d000 r--p 00107000 08:01 135790                     /lib/x86_64-linux-gnu/libm-2.24.so
7f90e5e0d000-7f90e5e0e000 rw-p 00108000 08:01 135790                     /lib/x86_64-linux-gnu/libm-2.24.so
7f90e5e0e000-7f90e5f86000 r-xp 00000000 08:01 4202509                    /usr/lib/x86_64-linux-gnu/libstdc++.so.6.0.22
7f90e5f86000-7f90e6186000 ---p 00178000 08:01 4202509                    /usr/lib/x86_64-linux-gnu/libstdc++.so.6.0.22
7f90e6186000-7f90e6190000 r--p 00178000 08:01 4202509                    /usr/lib/x86_64-linux-gnu/libstdc++.so.6.0.22
7f90e6190000-7f90e6192000 rw-p 00182000 08:01 4202509                    /usr/lib/x86_64-linux-gnu/libstdc++.so.6.0.22
7f90e6192000-7f90e6196000 rw-p 00000000 00:00 0 
7f90e6196000-7f90e6199000 r-xp 00000000 08:01 4201619                    /usr/lib/x86_64-linux-gnu/libboost_system.so.1.61.0
7f90e6199000-7f90e6398000 ---p 00003000 08:01 4201619                    /usr/lib/x86_64-linux-gnu/libboost_system.so.1.61.0
7f90e6398000-7f90e6399000 r--p 00002000 08:01 4201619                    /usr/lib/x86_64-linux-gnu/libboost_system.so.1.61.0
7f90e6399000-7f90e639a000 rw-p 00003000 08:01 4201619                    /usr/lib/x86_64-linux-gnu/libboost_system.so.1.61.0
7f90e639a000-7f90e63a9000 r-xp 00000000 08:01 4201616                    /usr/lib/x86_64-linux-gnu/libboost_date_time.so.1.61.0
7f90e63a9000-7f90e65a9000 ---p 0000f000 08:01 4201616                    /usr/lib/x86_64-linux-gnu/libboost_date_time.so.1.61.0
7f90e65a9000-7f90e65aa000 r--p 0000f000 08:01 4201616                    /usr/lib/x86_64-linux-gnu/libboost_date_time.so.1.61.0
7f90e65aa000-7f90e65ab000 rw-p 00010000 08:01 4201616                    /usr/lib/x86_64-linux-gnu/libboost_date_time.so.1.61.0
7f90e65ab000-7f90e65b7000 r-xp 00000000 08:01 4208928                    /usr/lib/x86_64-linux-gnu/libunwind.so.8.0.1
7f90e65b7000-7f90e67b6000 ---p 0000c000 08:01 4208928                    /usr/lib/x86_64-linux-gnu/libunwind.so.8.0.1
7f90e67b6000-7f90e67b7000 r--p 0000b000 08:01 4208928                    /usr/lib/x86_64-linux-gnu/libunwind.so.8.0.1
7f90e67b7000-7f90e67b8000 rw-p 0000c000 08:01 4208928                    /usr/lib/x86_64-linux-gnu/libunwind.so.8.0.1
7f90e67b8000-7f90e67c6000 rw-p 00000000 00:00 0 
7f90e67c6000-7f90e685c000 r-xp 00000000 08:01 4208920                    /usr/lib/x86_64-linux-gnu/libunbound.so.2.4.0
7f90e685c000-7f90e6a5c000 ---p 00096000 08:01 4208920                    /usr/lib/x86_64-linux-gnu/libunbound.so.2.4.0
7f90e6a5c000-7f90e6a5d000 r--p 00096000 08:01 4208920                    /usr/lib/x86_64-linux-gnu/libunbound.so.2.4.0
7f90e6a5d000-7f90e6a61000 rw-p 00097000 08:01 4208920                    /usr/lib/x86_64-linux-gnu/libunbound.so.2.4.0
7f90e6a61000-7f90e6a9e000 r-xp 00000000 08:01 4208107                    /usr/lib/x86_64-linux-gnu/libboost_serialization.so.1.61.0
7f90e6a9e000-7f90e6c9d000 ---p 0003d000 08:01 4208107                    /usr/lib/x86_64-linux-gnu/libboost_serialization.so.1.61.0
7f90e6c9d000-7f90e6ca0000 r--p 0003c000 08:01 4208107                    /usr/lib/x86_64-linux-gnu/libboost_serialization.so.1.61.0
7f90e6ca0000-7f90e6ca1000 rw-p 0003f000 08:01 4208107                    /usr/lib/x86_64-linux-gnu/libboost_serialization.so.1.61.0
7f90e6ca1000-7f90e6dac000 r-xp 00000000 08:01 4208120                    /usr/lib/x86_64-linux-gnu/libboost_regex.so.1.61.0
7f90e6dac000-7f90e6fab000 ---p 0010b000 08:01 4208120                    /usr/lib/x86_64-linux-gnu/libboost_regex.so.1.61.0
7f90e6fab000-7f90e6fb0000 r--p 0010a000 08:01 4208120                    /usr/lib/x86_64-linux-gnu/libboost_regex.so.1.61.0
7f90e6fb0000-7f90e6fb1000 rw-p 0010f000 08:01 4208120                    /usr/lib/x86_64-linux-gnu/libboost_regex.so.1.61.0
7f90e6fb1000-7f90e6fd6000 r-xp 00000000 08:01 4201620                    /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.61.0
7f90e6fd6000-7f90e71d5000 ---p 00025000 08:01 4201620                    /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.61.0
7f90e71d5000-7f90e71d7000 r--p 00024000 08:01 4201620                    /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.61.0
7f90e71d7000-7f90e71d8000 rw-p 00026000 08:01 4201620                    /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.61.0
7f90e71d8000-7f90e71ef000 r-xp 00000000 08:01 4201617                    /usr/lib/x86_64-linux-gnu/libboost_filesystem.so.1.61.0
7f90e71ef000-7f90e73ef000 ---p 00017000 08:01 4201617                    /usr/lib/x86_64-linux-gnu/libboost_filesystem.so.1.61.0
7f90e73ef000-7f90e73f0000 r--p 00017000 08:01 4201617                    /usr/lib/x86_64-linux-gnu/libboost_filesystem.so.1.61.0
7f90e73f0000-7f90e73f1000 rw-p 00018000 08:01 4201617                    /usr/lib/x86_64-linux-gnu/libboost_filesystem.so.1.61.0
7f90e73f1000-7f90e746a000 r-xp 00000000 08:01 4208584                    /usr/lib/x86_64-linux-gnu/libboost_program_options.so.1.61.0
7f90e746a000-7f90e766a000 ---p 00079000 08:01 4208584                    /usr/lib/x86_64-linux-gnu/libboost_program_options.so.1.61.0
7f90e766a000-7f90e766d000 r--p 00079000 08:01 4208584                    /usr/lib/x86_64-linux-gnu/libboost_program_options.so.1.61.0
7f90e766d000-7f90e766e000 rw-p 0007c000 08:01 4208584                    /usr/lib/x86_64-linux-gnu/libboost_program_options.so.1.61.0
7f90e766e000-7f90e7673000 r-xp 00000000 08:01 4208098                    /usr/lib/x86_64-linux-gnu/libboost_chrono.so.1.61.0
7f90e7673000-7f90e7873000 ---p 00005000 08:01 4208098                    /usr/lib/x86_64-linux-gnu/libboost_chrono.so.1.61.0
7f90e7873000-7f90e7874000 r--p 00005000 08:01 4208098                    /usr/lib/x86_64-linux-gnu/libboost_chrono.so.1.61.0
7f90e7874000-7f90e7875000 rw-p 00006000 08:01 4208098                    /usr/lib/x86_64-linux-gnu/libboost_chrono.so.1.61.0
7f90e7875000-7f90e7878000 r-xp 00000000 08:01 135748                     /lib/x86_64-linux-gnu/libdl-2.24.so
7f90e7878000-7f90e7a77000 ---p 00003000 08:01 135748                     /lib/x86_64-linux-gnu/libdl-2.24.so
7f90e7a77000-7f90e7a78000 r--p 00002000 08:01 135748                     /lib/x86_64-linux-gnu/libdl-2.24.so
7f90e7a78000-7f90e7a79000 rw-p 00003000 08:01 135748                     /lib/x86_64-linux-gnu/libdl-2.24.so
7f90e7a79000-7f90e7c36000 r-xp 00000000 08:01 135722                     /lib/x86_64-linux-gnu/libc-2.24.so
7f90e7c36000-7f90e7e36000 ---p 001bd000 08:01 135722                     /lib/x86_64-linux-gnu/libc-2.24.so
7f90e7e36000-7f90e7e3a000 r--p 001bd000 08:01 135722                     /lib/x86_64-linux-gnu/libc-2.24.so
7f90e7e3a000-7f90e7e3c000 rw-p 001c1000 08:01 135722                     /lib/x86_64-linux-gnu/libc-2.24.so
7f90e7e3c000-7f90e7e40000 rw-p 00000000 00:00 0 
7f90e7e40000-7f90e7e65000 r-xp 00000000 08:01 135694                     /lib/x86_64-linux-gnu/ld-2.24.so
7f90e8000000-7f90e8035000 r--s 00000000 08:01 2104078                    /var/cache/nscd/hosts
7f90e8035000-7f90e8049000 rw-p 00000000 00:00 0 
7f90e8060000-7f90e8064000 rw-p 00000000 00:00 0 
7f90e8064000-7f90e8065000 r--p 00024000 08:01 135694                     /lib/x86_64-linux-gnu/ld-2.24.so
7f90e8065000-7f90e8066000 rw-p 00025000 08:01 135694                     /lib/x86_64-linux-gnu/ld-2.24.so
7f90e8066000-7f90e8067000 rw-p 00000000 00:00 0 
7ffe521db000-7ffe521fc000 rw-p 00000000 00:00 0                          [stack]
7ffe521fc000-7ffe521fe000 r--p 00000000 00:00 0                          [vvar]
7ffe521fe000-7ffe52200000 r-xp 00000000 00:00 0                          [vdso]
ffffffffff600000-ffffffffff601000 r-xp 00000000 00:00 0                  [vsyscall]
rlwrap: warning: monero-wallet-cli crashed, killed by SIGABRT (core dumped).
rlwrap itself has not crashed, but for transparency,
it will now kill itself with the same signal
```

And this occur in both Ubuntu 16.10 x64 and up-to-date Arch Linux. Wonder if any one has similar problem? The monero was build from current master branch.

This is what `gdb` says for core dump:

```
Core was generated by `/opt/monero/monero-wallet-cli --wallet-file /home/mwo/wallet2view --password  -'.
Program terminated with signal SIGABRT, Aborted.
#0  __GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:58
58	../sysdeps/unix/sysv/linux/raise.c: No such file or directory.
[Current thread is 1 (Thread 0x7faca6d7b6c0 (LWP 28664))]
(gdb) where 
#0  __GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:58
#1  0x00007faca67eb3ea in __GI_abort () at abort.c:89
#2  0x00007faca682d0d0 in __libc_message (do_abort=do_abort@entry=2, 
    fmt=fmt@entry=0x7faca6942368 "*** Error in `%s': %s: 0x%s ***\n") at ../sysdeps/posix/libc_fatal.c:175
#3  0x00007faca683675a in malloc_printerr (ar_ptr=<optimised out>, ptr=<optimised out>, 
    str=0x7faca6942408 "free(): corrupted unsorted chunks", action=3) at malloc.c:5046
#4  _int_free (av=<optimised out>, p=<optimised out>, have_lock=<optimised out>) at malloc.c:3902
#5  0x00007faca683a18c in __GI___libc_free (mem=<optimised out>) at malloc.c:2982
#6  0x00005619192f6661 in cryptonote::simple_wallet::import_key_images(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&) ()
#7  0x00005619192e0b5f in epee::command_handler::process_command_str(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) ()
#8  0x00005619192ff53d in cryptonote::simple_wallet::run() ()
#9  0x00005619192cd29b in main ()
```

# Discussion History
## moneromooo-monero | 2016-11-17T20:24:19+00:00
https://github.com/monero-project/monero/pull/1351


## ghost | 2016-11-17T21:07:18+00:00
Lightning fast ;)


## moneroexamples | 2016-11-17T23:53:39+00:00
Thanks! 
But now is other problem. Importing still does not work, 

```
Error: Failed to import key images: Signature check failed: input 136/141, key image 91c360f88019520848e1efb471a931fc30e59f2b8877eb7ebee80d025d6e92b8, signature a9ec60088467689ffc103f10d7cbb53e74d5ceb56fccb8ffd37848d12c494b0a462650d4279de822aba08a31b935179878e2739a388daeede0e9a9aaba761902, pubkey 8c812d2449df28b8d808c3562e8fabda1daf729cfa8f109f70958d47a30567a2
```

Similarly cant sign translations now: 

```
Error: Failed to sign transaction: key_image generated ephemeral public key not matched with output_key at index 136
```

associated tx: http://explore.moneroworld.com/tx/e95046c4421d46fe98166dd68d7ad748af0ab86f5b2ed88959afffed43f2b68c

I guess the reason is that extra field in signing tx was incorrect for a while, and txs with wrong extras are now in blockchain. So  importing checks the signature using wrong tx public keys for the extra. 

ould it be the case? 


## moneromooo-monero | 2016-11-18T18:00:25+00:00
The two wallets could be out of sync. Import outputs first, then export key images.


## moneromooo-monero | 2016-11-19T08:33:33+00:00
BTW, if you were using a cold wallet setup, some outputs (change when signed with a cold wallet) weren't seen (fixed with https://github.com/monero-project/monero/pull/1344), so rescanning will cause a more complete set of outputs, thus going out of sync with the counterpart wallet.


## moneromooo-monero | 2016-11-19T08:51:54+00:00
After looking at the code, you're right that this (wrong tx key being used) can happen. That's a bit annoying because we can't easily "try both" like with processing a new tx. I could use the last one, which'd work all the time, but it feels a bit brittle. I'll think about it.


## moneromooo-monero | 2016-11-19T08:53:14+00:00
Actually, I can do this like with processing a new tx :)


## moneromooo-monero | 2016-11-19T09:38:37+00:00
https://github.com/monero-project/monero/pull/1358 should fix it.


## moneroexamples | 2016-11-20T00:10:05+00:00
@moneromooo-monero 

Thanks for your prompt replies. Yes, I think using second public key should do the trick. Will try to check as soon as posible.


## moneroexamples | 2016-11-20T23:56:25+00:00
@moneromooo-monero

Importing keys working now. Thank you. I think I have no other comments for this thread, so if you want you can close it, unless someone else has some more info.

## moneromooo-monero | 2016-11-21T09:45:46+00:00
Thanks for the confirmation. I can't close anything, only a core team member or the reporter can do so.

# Action History
- Created by: moneroexamples | 2016-11-16T23:38:41+00:00
- Closed at: 2016-11-21T23:49:10+00:00
