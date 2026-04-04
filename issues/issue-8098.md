---
title: Debian Bullseye build. SIGBUS, Bus error
source_url: https://github.com/monero-project/monero/issues/8098
author: shermand100
assignees: []
labels: []
created_at: '2021-11-30T20:02:04+00:00'
updated_at: '2022-07-12T01:51:09+00:00'
type: issue
status: closed
closed_at: '2022-07-12T01:51:09+00:00'
---

# Original Description
Using the steps https://github.com/monero-project/monero#compiling-monero-from-source for years on Debian Jessie/Buster worked fine.

Fresh install of Bullseye however, Monerod builds on Raspberry Pi/Odroid XU4/Rock64 (I've tried different hardware) but runs as far as synchronising blocks, then exits with "Bus error". Three other users are reporting the same issue.

**Extra Help please:** I'll put the readouts and logs below, but I'm annoyed I can't be of more help. I've used monero for several years and have had problems before that google usually points me in the right direction to solve. I've spent 2 days so far trying to find this issue but with my lack of experience I've hit a wall.
_I would really appreciate a pointer for how to go about solving this generally_ should I take a web course in cmake/debugging or another topic? I feel I'm lacking skills to help in this case and as I plan to be using Monero for many more years so now's the best time to start leveling myself up. Any advice appreciated.

Anyway...

Below, separated by headers in order: Normal running with Bus Error, GDB + BT FULL (debug fails to build), CMakeError.log

Armbian 21.08.6 Bullseye with Linux 5.4.160-odroidxu4
Bullseye change notes:
https://www.debian.org/releases/bullseye/amd64/release-notes/ch-information.en.html

### Running

> pinodexmr@odroidxu4:~/monero/build/release/bin$ ./monerod
> 2021-11-30 19:44:32.768 I Monero 'Oxygen Orion' (v0.17.3.0-0ea5cc9bd)
> 2021-11-30 19:44:32.769 I Initializing cryptonote protocol...
> 2021-11-30 19:44:32.769 I Cryptonote protocol initialized OK
> 2021-11-30 19:44:32.780 I Initializing core...
> 2021-11-30 19:44:32.781 I Loading blockchain from folder /home/pinodexmr/.bitmonero/lmdb ...
> 2021-11-30 19:44:33.581 I Loading checkpoints
> 2021-11-30 19:44:33.582 I Core initialized OK
> 2021-11-30 19:44:33.582 I Initializing p2p server...
> 2021-11-30 19:44:33.587 I p2p server initialized OK
> 2021-11-30 19:44:33.587 I Initializing core RPC server...
> 2021-11-30 19:44:33.588 I Binding on 127.0.0.1 (IPv4):18081
> 2021-11-30 19:44:35.646 I core RPC server initialized OK on port: 18081
> 2021-11-30 19:44:35.653 I Starting core RPC server...
> 2021-11-30 19:44:35.654 I core RPC server started ok
> 2021-11-30 19:44:35.659 I Starting p2p net loop...
> 2021-11-30 19:44:36.661 I
> 2021-11-30 19:44:36.661 I **********************************************************************
> 2021-11-30 19:44:36.661 I The daemon will start synchronizing with the network. This may take a long time to complete.
> 2021-11-30 19:44:36.662 I
> 2021-11-30 19:44:36.662 I You can set the level of process detailization through "set_log <level|categories>" command,
> 2021-11-30 19:44:36.662 I where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).
> 2021-11-30 19:44:36.663 I
> 2021-11-30 19:44:36.663 I Use the "help" command to see the list of available commands.
> 2021-11-30 19:44:36.663 I Use "help <command>" to see a command's documentation.
> 2021-11-30 19:44:36.663 I **********************************************************************
> 2021-11-30 19:44:42.541 I [91.180.182.225:18080 OUT] Sync data returned a new top block candidate: 11901 -> 2504787 [Your node is 2492886 blocks (7.6 years) behind]
> 2021-11-30 19:44:42.541 I SYNCHRONIZATION started
> 2021-11-30 19:44:44.374 I Synced 12001/2504787 (0%, 2492786 left)
> 2021-11-30 19:44:46.295 I Synced 12101/2504787 (0%, 2492686 left)
> 2021-11-30 19:44:47.253 I Synced 12201/2504787 (0%, 2492586 left)
> 2021-11-30 19:44:48.349 I Synced 12301/2504787 (0%, 2492486 left)
> 2021-11-30 19:44:49.254 I Synced 12401/2504787 (0%, 2492386 left)
> 2021-11-30 19:44:50.156 I Synced 12501/2504787 (0%, 2492286 left)
> 2021-11-30 19:44:51.423 I Synced 12601/2504787 (0%, 2492186 left)
> 2021-11-30 19:44:52.736 I Synced 12701/2504787 (0%, 2492086 left)
> 2021-11-30 19:44:53.841 I Synced 12801/2504787 (0%, 2491986 left)
> 2021-11-30 19:44:54.864 I Synced 12901/2504787 (0%, 2491886 left)
> 2021-11-30 19:44:55.729 I Synced 13001/2504787 (0%, 2491786 left)
> 2021-11-30 19:44:56.534 I Synced 13101/2504787 (0%, 2491686 left)
> 2021-11-30 19:44:57.374 I Synced 13201/2504787 (0%, 2491586 left)
> 2021-11-30 19:44:58.268 I Synced 13301/2504787 (0%, 2491486 left)
> 2021-11-30 19:44:59.064 I Synced 13401/2504787 (0%, 2491386 left)
> 2021-11-30 19:44:59.843 I Synced 13501/2504787 (0%, 2491286 left)
> 2021-11-30 19:45:00.596 I Synced 13601/2504787 (0%, 2491186 left)
> 2021-11-30 19:45:01.552 I Synced 13701/2504787 (0%, 2491086 left)
> 2021-11-30 19:45:03.046 I Synced 13801/2504787 (0%, 2490986 left)
> 2021-11-30 19:45:04.800 I Synced 13901/2504787 (0%, 2490886 left)
> 2021-11-30 19:45:06.873 I Synced 14001/2504787 (0%, 2490786 left)
> 2021-11-30 19:45:07.520 I Synced 14101/2504787 (0%, 2490686 left)
> 2021-11-30 19:45:08.120 I Synced 14201/2504787 (0%, 2490586 left)
> 2021-11-30 19:45:08.733 I Synced 14301/2504787 (0%, 2490486 left)
> 2021-11-30 19:45:09.443 I Synced 14401/2504787 (0%, 2490386 left)
> 2021-11-30 19:45:11.186 I Synced 14501/2504787 (0%, 2490286 left)
> 2021-11-30 19:45:12.475 I Synced 14601/2504787 (0%, 2490186 left)
> 2021-11-30 19:45:13.935 I Synced 14701/2504787 (0%, 2490086 left)
> Bus error

### GDB + BT FULL

> pinodexmr@odroidxu4:~/monero/build/release/bin$ gdb ./monerod
> GNU gdb (Debian 10.1-1.7) 10.1.90.20210103-git
> Copyright (C) 2021 Free Software Foundation, Inc.
> License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
> This is free software: you are free to change and redistribute it.
> There is NO WARRANTY, to the extent permitted by law.
> Type "show copying" and "show warranty" for details.
> This GDB was configured as "arm-linux-gnueabihf".
> Type "show configuration" for configuration details.
> For bug reporting instructions, please see:
> <https://www.gnu.org/software/gdb/bugs/>.
> Find the GDB manual and other documentation resources online at:
>     <http://www.gnu.org/software/gdb/documentation/>.
> 
> For help, type "help".
> Type "apropos word" to search for commands related to "word"...
> Reading symbols from ./monerod...
> (No debugging symbols found in ./monerod)
> (gdb) run
> Starting program: /home/pinodexmr/monero/build/release/bin/monerod
> [Thread debugging using libthread_db enabled]
> Using host libthread_db library "/lib/arm-linux-gnueabihf/libthread_db.so.1".
> 2021-11-30 19:52:23.374 I Monero 'Oxygen Orion' (v0.17.3.0-0ea5cc9bd)
> 2021-11-30 19:52:23.374 I Initializing cryptonote protocol...
> 2021-11-30 19:52:23.374 I Cryptonote protocol initialized OK
> 2021-11-30 19:52:23.377 I Initializing core...
> 2021-11-30 19:52:23.377 I Loading blockchain from folder /home/pinodexmr/.bitmonero/lmdb ...
> [New Thread 0xb234d1e0 (LWP 27660)]
> 2021-11-30 19:52:23.761 I Loading checkpoints
> 2021-11-30 19:52:23.762 I Core initialized OK
> 2021-11-30 19:52:23.762 I Initializing p2p server...
> 2021-11-30 19:52:23.764 I p2p server initialized OK
> 2021-11-30 19:52:23.764 I Initializing core RPC server...
> 2021-11-30 19:52:23.765 I Binding on 127.0.0.1 (IPv4):18081
> 2021-11-30 19:52:41.867 I core RPC server initialized OK on port: 18081
> [New Thread 0xabb1f1e0 (LWP 27662)]
> [New Thread 0xab31e1e0 (LWP 27663)]
> [New Thread 0xaa9ff1e0 (LWP 27664)]
> 2021-11-30 19:52:41.913 I Starting core RPC server...
> [New Thread 0xaa1fe1e0 (LWP 27665)]
> [New Thread 0xa99fd1e0 (LWP 27666)]
> 2021-11-30 19:52:41.916 I core RPC server started ok
> [New Thread 0xa89851e0 (LWP 27667)]
> [New Thread 0xa81841e0 (LWP 27668)]
> [New Thread 0xa79831e0 (LWP 27669)]
> 2021-11-30 19:52:41.923 I Starting p2p net loop...
> [New Thread 0xa6fff1e0 (LWP 27670)]
> [New Thread 0xa65ff1e0 (LWP 27671)]
> [New Thread 0xa60fe1e0 (LWP 27672)]
> [New Thread 0xa57ff1e0 (LWP 27673)]
> [New Thread 0xa52fe1e0 (LWP 27674)]
> [New Thread 0xa4bfd1e0 (LWP 27675)]
> [New Thread 0xa46fc1e0 (LWP 27676)]
> [New Thread 0xa3fff1e0 (LWP 27677)]
> [New Thread 0xa38ff1e0 (LWP 27678)]
> [New Thread 0xa31ff1e0 (LWP 27679)]
> [New Thread 0xa2aff1e0 (LWP 27680)]
> [New Thread 0xa23ff1e0 (LWP 27681)]
> 2021-11-30 19:52:42.926 I
> 2021-11-30 19:52:42.926 I **********************************************************************
> [New Thread 0xa22fe1e0 (LWP 27682)]
> 2021-11-30 19:52:42.926 I The daemon will start synchronizing with the network. This may take a long time to complete.
> 2021-11-30 19:52:42.926 I
> 2021-11-30 19:52:42.926 I You can set the level of process detailization through "set_log <level|categories>" command,
> [New Thread 0xa21fd1e0 (LWP 27683)]
> [New Thread 0xa20fc1e0 (LWP 27684)]
> 2021-11-30 19:52:42.927 I where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).
> 2021-11-30 19:52:42.928 I
> 2021-11-30 19:52:42.928 I Use the "help" command to see the list of available commands.
> 2021-11-30 19:52:42.929 I Use "help <command>" to see a command's documentation.
> 2021-11-30 19:52:42.930 I **********************************************************************
> [New Thread 0xa1ffb1e0 (LWP 27685)]
> [New Thread 0xa1afa1e0 (LWP 27686)]
> [New Thread 0xa15f91e0 (LWP 27687)]
> [New Thread 0xa10f81e0 (LWP 27688)]
> [New Thread 0xa0bf71e0 (LWP 27689)]
> [New Thread 0xa02ff1e0 (LWP 27690)]
> [New Thread 0x9fdfe1e0 (LWP 27691)]
> [Thread 0xa20fc1e0 (LWP 27684) exited]
> [Thread 0xa22fe1e0 (LWP 27682) exited]
> [Thread 0xa21fd1e0 (LWP 27683) exited]
> [Thread 0xa23ff1e0 (LWP 27681) exited]
> 2021-11-30 19:52:43.796 I [68.6.155.153:18080 OUT] Sync data returned a new top block candidate: 14701 -> 2504791 [Your node is 2490090 blocks (7.6 years) behind]
> 2021-11-30 19:52:43.796 I SYNCHRONIZATION started
> 2021-11-30 19:52:45.946 I Synced 14801/2504791 (0%, 2489990 left)
> 
> Thread 21 "monerod" received signal SIGBUS, Bus error.
> [Switching to Thread 0xa2aff1e0 (LWP 27680)]
> 0x006b8f44 in bool epee::serialization::serialize_stl_container_t_obj<std::vector<nodetool::peerlist_entry_base<epee::net_utils::network_address>, std::allocator<nodetool::peerlist_entry_base<epee::net_utils::network_address> > >, epee::serialization::portable_storage>(std::vector<nodetool::peerlist_entry_base<epee::net_utils::network_address>, std::allocator<nodetool::peerlist_entry_base<epee::net_utils::network_address> > > const&, epee::serialization::portable_storage&, epee::serialization::portable_storage::hsection, char const*) [clone .constprop.0] [clone .isra.0] ()
> (gdb) bt full
> #0  0x006b8f44 in bool epee::serialization::serialize_stl_container_t_obj<std::vector<nodetool::peerlist_entry_base<epee::net_utils::network_address>, std::allocator<nodetool::peerlist_entry_base<epee::net_utils::network_address> > >, epee::serialization::portable_storage>(std::vector<nodetool::peerlist_entry_base<epee::net_utils::network_address>, std::allocator<nodetool::peerlist_entry_base<epee::net_utils::network_address> > > const&, epee::serialization::portable_storage&, epee::serialization::portable_storage::hsection, char const*) [clone .constprop.0] [clone .isra.0] ()
> No symbol table info available.
> #1  0x000003ea in ?? ()
> No symbol table info available.
> Backtrace stopped: previous frame identical to this frame (corrupt stack?)
> (gdb)


### Cmake output error monero (not debug)
/home/pinodexmr/monero/build/release/CMakeFiles/CMakeError.log

> Performing C SOURCE FILE Test CMAKE_HAVE_LIBC_PTHREAD failed with the following output:
> Change Dir: /home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp
> 
> Run Build Command(s):/usr/bin/gmake cmTC_4460f/fast && gmake[1]: Entering directory '/home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp'
> /usr/bin/gmake  -f CMakeFiles/cmTC_4460f.dir/build.make CMakeFiles/cmTC_4460f.dir/build
> gmake[2]: Entering directory '/home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp'
> Building C object CMakeFiles/cmTC_4460f.dir/src.c.o
> /usr/bin/cc   -DCMAKE_HAVE_LIBC_PTHREAD -o CMakeFiles/cmTC_4460f.dir/src.c.o -c /home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp/src.c
> Linking C executable cmTC_4460f
> /usr/bin/cmake -E cmake_link_script CMakeFiles/cmTC_4460f.dir/link.txt --verbose=1
> /usr/bin/cc  -DCMAKE_HAVE_LIBC_PTHREAD -rdynamic CMakeFiles/cmTC_4460f.dir/src.c.o -o cmTC_4460f 
> /usr/bin/ld: CMakeFiles/cmTC_4460f.dir/src.c.o: in function `main':
> src.c:(.text+0x26): undefined reference to `pthread_create'
> /usr/bin/ld: src.c:(.text+0x2e): undefined reference to `pthread_detach'
> /usr/bin/ld: src.c:(.text+0x36): undefined reference to `pthread_cancel'
> /usr/bin/ld: src.c:(.text+0x40): undefined reference to `pthread_join'
> collect2: error: ld returned 1 exit status
> gmake[2]: *** [CMakeFiles/cmTC_4460f.dir/build.make:106: cmTC_4460f] Error 1
> gmake[2]: Leaving directory '/home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp'
> gmake[1]: *** [Makefile:140: cmTC_4460f/fast] Error 2
> gmake[1]: Leaving directory '/home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp'
> 
> 
> Source file was:
> #include <pthread.h>
> 
> void* test_func(void* data)
> {
>   return data;
> }
> 
> int main(void)
> {
>   pthread_t thread;
>   pthread_create(&thread, NULL, test_func, NULL);
>   pthread_detach(thread);
>   pthread_cancel(thread);
>   pthread_join(thread, NULL);
>   pthread_atfork(NULL, NULL, NULL);
>   pthread_exit(NULL);
> 
>   return 0;
> }
> 
> Determining if the function memset_s exists in the c failed with the following output:
> Change Dir: /home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp
> 
> Run Build Command(s):/usr/bin/gmake cmTC_1b546/fast && gmake[1]: Entering directory '/home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp'
> /usr/bin/gmake  -f CMakeFiles/cmTC_1b546.dir/build.make CMakeFiles/cmTC_1b546.dir/build
> gmake[2]: Entering directory '/home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp'
> Building C object CMakeFiles/cmTC_1b546.dir/CheckFunctionExists.c.o
> /usr/bin/cc   -pthread -DCHECK_FUNCTION_EXISTS=memset_s -o CMakeFiles/cmTC_1b546.dir/CheckFunctionExists.c.o -c /usr/share/cmake-3.18/Modules/CheckFunctionExists.c
> Linking C executable cmTC_1b546
> /usr/bin/cmake -E cmake_link_script CMakeFiles/cmTC_1b546.dir/link.txt --verbose=1
> /usr/bin/cc  -pthread -DCHECK_FUNCTION_EXISTS=memset_s -rdynamic CMakeFiles/cmTC_1b546.dir/CheckFunctionExists.c.o -o cmTC_1b546   -L/home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp/string.h  -Wl,-rpath,/home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp/string.h -lc 
> /usr/bin/ld: CMakeFiles/cmTC_1b546.dir/CheckFunctionExists.c.o: in function `main':
> CheckFunctionExists.c:(.text+0xa): undefined reference to `memset_s'
> collect2: error: ld returned 1 exit status
> gmake[2]: *** [CMakeFiles/cmTC_1b546.dir/build.make:106: cmTC_1b546] Error 1
> gmake[2]: Leaving directory '/home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp'
> gmake[1]: *** [Makefile:140: cmTC_1b546/fast] Error 2
> gmake[1]: Leaving directory '/home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp'
> 
> 
> 
> Performing C SOURCE FILE Test _Werror__Wformat_security_c failed with the following output:
> Change Dir: /home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp
> 
> Run Build Command(s):/usr/bin/gmake cmTC_093ed/fast && gmake[1]: Entering directory '/home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp'
> /usr/bin/gmake  -f CMakeFiles/cmTC_093ed.dir/build.make CMakeFiles/cmTC_093ed.dir/build
> gmake[2]: Entering directory '/home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp'
> Building C object CMakeFiles/cmTC_093ed.dir/src.c.o
> /usr/bin/cc  -I/usr/include/libusb-1.0 -pthread -march=native -fno-strict-aliasing -D_Werror__Wformat_security_c   -Werror -Wformat-security -o CMakeFiles/cmTC_093ed.dir/src.c.o -c /home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp/src.c
> cc1: error: '-Wformat-security' ignored without '-Wformat' [-Werror=format-security]
> cc1: all warnings being treated as errors
> gmake[2]: *** [CMakeFiles/cmTC_093ed.dir/build.make:85: CMakeFiles/cmTC_093ed.dir/src.c.o] Error 1
> gmake[2]: Leaving directory '/home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp'
> gmake[1]: *** [Makefile:140: cmTC_093ed/fast] Error 2
> gmake[1]: Leaving directory '/home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp'
> 
> 
> Source file was:
> int main(void) { return 0; }
> Performing C++ SOURCE FILE Test _Werror__Wformat_security_cxx failed with the following output:
> Change Dir: /home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp
> 
> Run Build Command(s):/usr/bin/gmake cmTC_371c2/fast && gmake[1]: Entering directory '/home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp'
> /usr/bin/gmake  -f CMakeFiles/cmTC_371c2.dir/build.make CMakeFiles/cmTC_371c2.dir/build
> gmake[2]: Entering directory '/home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp'
> Building CXX object CMakeFiles/cmTC_371c2.dir/src.cxx.o
> /usr/bin/c++  -I/usr/include/libusb-1.0 -pthread -march=native -fno-strict-aliasing -D_Werror__Wformat_security_cxx   -Werror -Wformat-security -o CMakeFiles/cmTC_371c2.dir/src.cxx.o -c /home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp/src.cxx
> cc1plus: error: '-Wformat-security' ignored without '-Wformat' [-Werror=format-security]
> cc1plus: all warnings being treated as errors
> gmake[2]: *** [CMakeFiles/cmTC_371c2.dir/build.make:85: CMakeFiles/cmTC_371c2.dir/src.cxx.o] Error 1
> gmake[2]: Leaving directory '/home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp'
> gmake[1]: *** [Makefile:140: cmTC_371c2/fast] Error 2
> gmake[1]: Leaving directory '/home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp'
> 
> 
> Source file was:
> int main() { return 0; }
> Performing C SOURCE FILE Test _Werror__fcf_protection=full_c failed with the following output:
> Change Dir: /home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp
> 
> Run Build Command(s):/usr/bin/gmake cmTC_b4a26/fast && gmake[1]: Entering directory '/home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp'
> /usr/bin/gmake  -f CMakeFiles/cmTC_b4a26.dir/build.make CMakeFiles/cmTC_b4a26.dir/build
> gmake[2]: Entering directory '/home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp'
> Building C object CMakeFiles/cmTC_b4a26.dir/src.c.o
> /usr/bin/cc  -I/usr/include/libusb-1.0 -pthread -march=native -fno-strict-aliasing -D_Werror__fcf_protection=full_c   -Werror -fcf-protection=full -o CMakeFiles/cmTC_b4a26.dir/src.c.o -c /home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp/src.c
> cc1: error: '-fcf-protection=full' is not supported for this target
> gmake[2]: *** [CMakeFiles/cmTC_b4a26.dir/build.make:85: CMakeFiles/cmTC_b4a26.dir/src.c.o] Error 1
> gmake[2]: Leaving directory '/home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp'
> gmake[1]: *** [Makefile:140: cmTC_b4a26/fast] Error 2
> gmake[1]: Leaving directory '/home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp'
> 
> 
> Source file was:
> int main(void) { return 0; }
> Performing C++ SOURCE FILE Test _Werror__fcf_protection=full_cxx failed with the following output:
> Change Dir: /home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp
> 
> Run Build Command(s):/usr/bin/gmake cmTC_96bef/fast && gmake[1]: Entering directory '/home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp'
> /usr/bin/gmake  -f CMakeFiles/cmTC_96bef.dir/build.make CMakeFiles/cmTC_96bef.dir/build
> gmake[2]: Entering directory '/home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp'
> Building CXX object CMakeFiles/cmTC_96bef.dir/src.cxx.o
> /usr/bin/c++  -I/usr/include/libusb-1.0 -pthread -march=native -fno-strict-aliasing -D_Werror__fcf_protection=full_cxx   -Werror -fcf-protection=full -o CMakeFiles/cmTC_96bef.dir/src.cxx.o -c /home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp/src.cxx
> cc1plus: error: '-fcf-protection=full' is not supported for this target
> gmake[2]: *** [CMakeFiles/cmTC_96bef.dir/build.make:85: CMakeFiles/cmTC_96bef.dir/src.cxx.o] Error 1
> gmake[2]: Leaving directory '/home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp'
> gmake[1]: *** [Makefile:140: cmTC_96bef/fast] Error 2
> gmake[1]: Leaving directory '/home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp'
> 
> 
> Source file was:
> int main() { return 0; }
> Determining if the -Wl,-z,noexecheap linker flag is supported failed with the following output:
> Change Dir: /home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp
> 
> Run Build Command(s):/usr/bin/gmake cmTC_d1266/fast && gmake[1]: Entering directory '/home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp'
> /usr/bin/gmake  -f CMakeFiles/cmTC_d1266.dir/build.make CMakeFiles/cmTC_d1266.dir/build
> gmake[2]: Entering directory '/home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp'
> Building C object CMakeFiles/cmTC_d1266.dir/CheckLinkerFlag.c.o
> /usr/bin/cc   -Wl,-z,noexecheap    -Wl,-z,noexecheap -o CMakeFiles/cmTC_d1266.dir/CheckLinkerFlag.c.o -c /home/pinodexmr/monero/cmake/CheckLinkerFlag.c
> Linking C executable cmTC_d1266
> /usr/bin/cmake -E cmake_link_script CMakeFiles/cmTC_d1266.dir/link.txt --verbose=1
> /usr/bin/cc -Wl,-z,noexecheap  -rdynamic CMakeFiles/cmTC_d1266.dir/CheckLinkerFlag.c.o -o cmTC_d1266 
> /usr/bin/ld: warning: -z noexecheap ignored
> gmake[2]: Leaving directory '/home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp'
> gmake[1]: Leaving directory '/home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp'
> 
> 
> 
> Determining if the CXX compiler accepts the flag -mfpu=vfp3-d16 failed with the following output:
> Change Dir: /home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp
> 
> Run Build Command(s):/usr/bin/gmake cmTC_66e1a/fast && gmake[1]: Entering directory '/home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp'
> /usr/bin/gmake  -f CMakeFiles/cmTC_66e1a.dir/build.make CMakeFiles/cmTC_66e1a.dir/build
> gmake[2]: Entering directory '/home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp'
> Building CXX object CMakeFiles/cmTC_66e1a.dir/DummyCXXFile.cxx.o
> /usr/bin/c++   -pthread -march=native -fno-strict-aliasing -D_GNU_SOURCE   -Wall -Wextra -Wpointer-arith -Wundef -Wvla -Wwrite-strings -Wno-error=extra -Wno-error=deprecated-declarations -Wno-unused-parameter -Wno-unused-variable -Wno-error=unused-variable -Wno-error=undef -Wno-error=uninitialized -Wlogical-op -Wno-error=maybe-uninitialized -Wno-error=cpp -Wno-reorder -Wno-missing-field-initializers  -fPIC  -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -fstack-protector -fstack-protector-strong -fstack-clash-protection -fno-strict-aliasing -mfpu=vfp3-d16 -o CMakeFiles/cmTC_66e1a.dir/DummyCXXFile.cxx.o -c /usr/share/cmake-3.18/Modules/DummyCXXFile.cxx
> c++: error: unrecognized argument in option ‘-mfpu=vfp3-d16’
> c++: note: valid arguments to ‘-mfpu=’ are: auto crypto-neon-fp-armv8 fp-armv8 fpv4-sp-d16 fpv5-d16 fpv5-sp-d16 neon neon-fp-armv8 neon-fp16 neon-vfpv3 neon-vfpv4 vfp vfp3 vfpv2 vfpv3 vfpv3-d16 vfpv3-d16-fp16 vfpv3-fp16 vfpv3xd vfpv3xd-fp16 vfpv4 vfpv4-d16; did you mean ‘vfpv3-d16’?
> gmake[2]: *** [CMakeFiles/cmTC_66e1a.dir/build.make:85: CMakeFiles/cmTC_66e1a.dir/DummyCXXFile.cxx.o] Error 1
> gmake[2]: Leaving directory '/home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp'
> gmake[1]: *** [Makefile:140: cmTC_66e1a/fast] Error 2
> gmake[1]: Leaving directory '/home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp'
> 
> 
> 
> Determining if the CXX compiler accepts the flag -mfpu=vfp4 failed with the following output:
> Change Dir: /home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp
> 
> Run Build Command(s):/usr/bin/gmake cmTC_04760/fast && gmake[1]: Entering directory '/home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp'
> /usr/bin/gmake  -f CMakeFiles/cmTC_04760.dir/build.make CMakeFiles/cmTC_04760.dir/build
> gmake[2]: Entering directory '/home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp'
> Building CXX object CMakeFiles/cmTC_04760.dir/DummyCXXFile.cxx.o
> /usr/bin/c++   -pthread -march=native -fno-strict-aliasing -D_GNU_SOURCE   -Wall -Wextra -Wpointer-arith -Wundef -Wvla -Wwrite-strings -Wno-error=extra -Wno-error=deprecated-declarations -Wno-unused-parameter -Wno-unused-variable -Wno-error=unused-variable -Wno-error=undef -Wno-error=uninitialized -Wlogical-op -Wno-error=maybe-uninitialized -Wno-error=cpp -Wno-reorder -Wno-missing-field-initializers  -fPIC  -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -fstack-protector -fstack-protector-strong -fstack-clash-protection -fno-strict-aliasing -mfpu=vfp4 -o CMakeFiles/cmTC_04760.dir/DummyCXXFile.cxx.o -c /usr/share/cmake-3.18/Modules/DummyCXXFile.cxx
> c++: error: unrecognized argument in option ‘-mfpu=vfp4’
> c++: note: valid arguments to ‘-mfpu=’ are: auto crypto-neon-fp-armv8 fp-armv8 fpv4-sp-d16 fpv5-d16 fpv5-sp-d16 neon neon-fp-armv8 neon-fp16 neon-vfpv3 neon-vfpv4 vfp vfp3 vfpv2 vfpv3 vfpv3-d16 vfpv3-d16-fp16 vfpv3-fp16 vfpv3xd vfpv3xd-fp16 vfpv4 vfpv4-d16; did you mean ‘vfp’?
> gmake[2]: *** [CMakeFiles/cmTC_04760.dir/build.make:85: CMakeFiles/cmTC_04760.dir/DummyCXXFile.cxx.o] Error 1
> gmake[2]: Leaving directory '/home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp'
> gmake[1]: *** [Makefile:140: cmTC_04760/fast] Error 2
> gmake[1]: Leaving directory '/home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp'
> 
> 
> 
> Determining if the CXX compiler accepts the flag -mfloat-abi=softfp failed with the following output:
> Change Dir: /home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp
> 
> Run Build Command(s):/usr/bin/gmake cmTC_eb3f2/fast && gmake[1]: Entering directory '/home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp'
> /usr/bin/gmake  -f CMakeFiles/cmTC_eb3f2.dir/build.make CMakeFiles/cmTC_eb3f2.dir/build
> gmake[2]: Entering directory '/home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp'
> Building CXX object CMakeFiles/cmTC_eb3f2.dir/DummyCXXFile.cxx.o
> /usr/bin/c++   -pthread -march=native -fno-strict-aliasing -D_GNU_SOURCE   -Wall -Wextra -Wpointer-arith -Wundef -Wvla -Wwrite-strings -Wno-error=extra -Wno-error=deprecated-declarations -Wno-unused-parameter -Wno-unused-variable -Wno-error=unused-variable -Wno-error=undef -Wno-error=uninitialized -Wlogical-op -Wno-error=maybe-uninitialized -Wno-error=cpp -Wno-reorder -Wno-missing-field-initializers  -fPIC  -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -fstack-protector -fstack-protector-strong -fstack-clash-protection -fno-strict-aliasing -mfloat-abi=softfp -o CMakeFiles/cmTC_eb3f2.dir/DummyCXXFile.cxx.o -c /usr/share/cmake-3.18/Modules/DummyCXXFile.cxx
> Linking CXX executable cmTC_eb3f2
> /usr/bin/cmake -E cmake_link_script CMakeFiles/cmTC_eb3f2.dir/link.txt --verbose=1
> /usr/bin/c++  -pthread -march=native -fno-strict-aliasing -D_GNU_SOURCE   -Wall -Wextra -Wpointer-arith -Wundef -Wvla -Wwrite-strings -Wno-error=extra -Wno-error=deprecated-declarations -Wno-unused-parameter -Wno-unused-variable -Wno-error=unused-variable -Wno-error=undef -Wno-error=uninitialized -Wlogical-op -Wno-error=maybe-uninitialized -Wno-error=cpp -Wno-reorder -Wno-missing-field-initializers  -fPIC  -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -fstack-protector -fstack-protector-strong -fstack-clash-protection -fno-strict-aliasing -mfloat-abi=softfp -rdynamic CMakeFiles/cmTC_eb3f2.dir/DummyCXXFile.cxx.o -o cmTC_eb3f2 
> /usr/bin/ld: error: cmTC_eb3f2 uses VFP register arguments, CMakeFiles/cmTC_eb3f2.dir/DummyCXXFile.cxx.o does not
> /usr/bin/ld: failed to merge target specific data of file CMakeFiles/cmTC_eb3f2.dir/DummyCXXFile.cxx.o
> collect2: error: ld returned 1 exit status
> gmake[2]: *** [CMakeFiles/cmTC_eb3f2.dir/build.make:106: cmTC_eb3f2] Error 1
> gmake[2]: Leaving directory '/home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp'
> gmake[1]: *** [Makefile:140: cmTC_eb3f2/fast] Error 2
> gmake[1]: Leaving directory '/home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp'
> 
> 
> 
> Performing C SOURCE FILE Test _Werror__fcf_protection=full_c failed with the following output:
> Change Dir: /home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp
> 
> Run Build Command(s):/usr/bin/gmake cmTC_1a493/fast && gmake[1]: Entering directory '/home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp'
> /usr/bin/gmake  -f CMakeFiles/cmTC_1a493.dir/build.make CMakeFiles/cmTC_1a493.dir/build
> gmake[2]: Entering directory '/home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp'
> Building C object CMakeFiles/cmTC_1a493.dir/src.c.o
> /usr/bin/cc  -I/usr/include/libusb-1.0 -pthread -march=native -fno-strict-aliasing -D_Werror__fcf_protection=full_c   -Werror -fcf-protection=full -o CMakeFiles/cmTC_1a493.dir/src.c.o -c /home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp/src.c
> cc1: error: '-fcf-protection=full' is not supported for this target
> gmake[2]: *** [CMakeFiles/cmTC_1a493.dir/build.make:85: CMakeFiles/cmTC_1a493.dir/src.c.o] Error 1
> gmake[2]: Leaving directory '/home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp'
> gmake[1]: *** [Makefile:140: cmTC_1a493/fast] Error 2
> gmake[1]: Leaving directory '/home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp'
> 
> 
> Source file was:
> int main(void) { return 0; }
> Performing C++ SOURCE FILE Test _Werror__fcf_protection=full_cxx failed with the following output:
> Change Dir: /home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp
> 
> Run Build Command(s):/usr/bin/gmake cmTC_7a2ad/fast && gmake[1]: Entering directory '/home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp'
> /usr/bin/gmake  -f CMakeFiles/cmTC_7a2ad.dir/build.make CMakeFiles/cmTC_7a2ad.dir/build
> gmake[2]: Entering directory '/home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp'
> Building CXX object CMakeFiles/cmTC_7a2ad.dir/src.cxx.o
> /usr/bin/c++  -I/usr/include/libusb-1.0 -pthread -march=native -fno-strict-aliasing -D_Werror__fcf_protection=full_cxx   -Werror -fcf-protection=full -o CMakeFiles/cmTC_7a2ad.dir/src.cxx.o -c /home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp/src.cxx
> cc1plus: error: '-fcf-protection=full' is not supported for this target
> gmake[2]: *** [CMakeFiles/cmTC_7a2ad.dir/build.make:85: CMakeFiles/cmTC_7a2ad.dir/src.cxx.o] Error 1
> gmake[2]: Leaving directory '/home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp'
> gmake[1]: *** [Makefile:140: cmTC_7a2ad/fast] Error 2
> gmake[1]: Leaving directory '/home/pinodexmr/monero/build/release/CMakeFiles/CMakeTmp'
> 
> 
> Source file was:
> int main() { return 0; }



# Discussion History
## selsta | 2021-11-30T21:31:12+00:00
Just to clarify, are you able to build debug or release build? Seeing that you were able to run monerod, I assume you were able to compile it successfully.

Regarding your bus error, can you try release-v0.17 branch + https://github.com/monero-project/monero/pull/7998 applied?

## shermand100 | 2021-11-30T22:42:37+00:00
Thanks for getting back to me so quickly. It's currently building with:

git clone --recursive https://github.com/monero-project/monero.git
git fetch origin pull/7998/head:release-v0.17
USE_SINGLE_BUILDDIR=1 make release

And will likely take quite some time, I'll update on progress tomorrow (GMT)

Edit1/Update:
Build was successful for 'release'. Monerod when running exits with "Bus error" whilst syncing, as above. Monerod usually exits with this error in <10seconds.

Edit2:
Debug Monerod build was successful, and runs. It's been running for over 5mins without error, I'll leave it running over night.

## shermand100 | 2021-12-01T10:34:11+00:00
So after leaving it running overnight with pull request 7998 included:
/monero/build/**debug**/bin/monerod seems to run fine (it sync'd to ~14% without issue)

Tried /monero/build/**release**/bin/monerod again. Same issue. Bus Error within 10 seconds of sync.
So:

Deleted /monero/build/**release**
cd monero
make clean
git fetch origin pull/7998/head:release-v0.17
USE_SINGLE_BUILDDIR=1 make release

./monero/build/**release**/bin/monerod Still same issue. Bus Error within 10 seconds of sync.

Is this what you were expecting?
I see now why you went for the serialisation pull from the limited GDB output. I just wouldn't have expected debug to work but not release.

## shermand100 | 2021-12-06T17:54:03+00:00
@selsta I assume you're busy with the multisig stuff but I've done some more learning about debugging to try and give more useful info.

So I added `set(CMAKE_BUILD_TYPE RelWithDebInfo)` to line 32 of /monero/CMakeLists.txt

This was then able to build monerod with debugging flags for the pull/7998 your recomended above giving me a v0.17.0.0-release that when run normally gives the "Bus error"

It's given the additional info:

(Two headers below "gdb ./monerod & run" and "BT FULL")
BT FULL has some entries for serialisation again and then some mentions of BOOST near the end.
If I can try something else to try and diagnose this please let me know.

### gdb ./monerod (built with pull 7998) & run

> pinodexmr@PiNodeXMR:~/monero/build/release/bin $ gdb ./monerod
> GNU gdb (Raspbian 10.1-1.7) 10.1.90.20210103-git
> Copyright (C) 2021 Free Software Foundation, Inc.
> License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
> This is free software: you are free to change and redistribute it.
> There is NO WARRANTY, to the extent permitted by law.
> Type "show copying" and "show warranty" for details.
> This GDB was configured as "arm-linux-gnueabihf".
> Type "show configuration" for configuration details.
> For bug reporting instructions, please see:
> <https://www.gnu.org/software/gdb/bugs/>.
> Find the GDB manual and other documentation resources online at:
>     <http://www.gnu.org/software/gdb/documentation/>.
> 
> For help, type "help".
> Type "apropos word" to search for commands related to "word"...
> Reading symbols from ./monerod...
> (gdb) run
> Starting program: /home/pinodexmr/monero/build/release/bin/monerod
> [Thread debugging using libthread_db enabled]
> Using host libthread_db library "/lib/arm-linux-gnueabihf/libthread_db.so.1".
> 2021-12-06 17:40:13.739 I Monero 'Oxygen Orion' (v0.17.0.0-cc9ca953a)

### Edit 07/12/21 bulky GDB log removed for better formatting in this issue.. Wrong build. Irrelevant.



## selsta | 2021-12-06T18:09:25+00:00
It seems like you compiled it incorrectly (you built master branch instead of release-v0.17 branch), the backtrace shows that 7998 is missing. Can you try these steps?

```
git clone --recursive https://github.com/monero-project/monero/
cd monero
git checkout release-v0.17
git pull origin pull/7998/head
make
```

Afterwards check if you still get SIGBUS error.

## shermand100 | 2021-12-07T13:21:35+00:00
So yeah, I double checked and:

> git clone --recursive https://github.com/monero-project/monero/
> cd monero
> git checkout release-v0.17
> git pull origin pull/7998/head
> make

Results in a v0.17.3.0-release, which I'm assuming we don't want

I've manged to get a v0.17.2.3-bbabbf0d4 build (which matches the PR7998) I think? with:

git clone --recursive https://github.com/monero-project/monero/
cd monero
git checkout release-v0.17
git submodule update --init --force #(forced by git for libunbound)
git pull origin pull/7998/head:pr7998
git checkout pr7998
make

Still get SIGBUS, Bus error but different GDB output:
Two headings again for formatting: GDB+RUN, and BT FULL

### GDB ./monerod+RUN

> pinodexmr@odroidxu4:~/monero/build/Linux/pr7998/release/bin$ gdb ./monerod
> GNU gdb (Debian 10.1-1.7) 10.1.90.20210103-git
> Copyright (C) 2021 Free Software Foundation, Inc.
> License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
> This is free software: you are free to change and redistribute it.
> There is NO WARRANTY, to the extent permitted by law.
> Type "show copying" and "show warranty" for details.
> This GDB was configured as "arm-linux-gnueabihf".
> Type "show configuration" for configuration details.
> For bug reporting instructions, please see:
> <https://www.gnu.org/software/gdb/bugs/>.
> Find the GDB manual and other documentation resources online at:
>     <http://www.gnu.org/software/gdb/documentation/>.
> 
> For help, type "help".
> Type "apropos word" to search for commands related to "word"...
> Reading symbols from ./monerod...
> (No debugging symbols found in ./monerod)
> (gdb) run
> Starting program: /home/pinodexmr/monero/build/Linux/pr7998/release/bin/monerod
> [Thread debugging using libthread_db enabled]
> Using host libthread_db library "/lib/arm-linux-gnueabihf/libthread_db.so.1".
> 2021-12-07 13:16:28.128 I Monero 'Oxygen Orion' (v0.17.2.3-bbabbf0d4)
> 2021-12-07 13:16:28.128 I Initializing cryptonote protocol...
> 2021-12-07 13:16:28.128 I Cryptonote protocol initialized OK
> 2021-12-07 13:16:28.132 I Initializing core...
> 2021-12-07 13:16:28.133 I Loading blockchain from folder /home/pinodexmr/.bitmonero/lmdb ...
> [New Thread 0xb330f1e0 (LWP 2686)]
> 2021-12-07 13:16:28.456 I Loading checkpoints
> 2021-12-07 13:16:28.456 I Core initialized OK
> 2021-12-07 13:16:28.456 I Initializing p2p server...
> 2021-12-07 13:16:28.458 I p2p server initialized OK
> 2021-12-07 13:16:28.459 I Initializing core RPC server...
> 2021-12-07 13:16:28.459 I Binding on 127.0.0.1 (IPv4):18081
> 2021-12-07 13:16:38.607 I core RPC server initialized OK on port: 18081
> [New Thread 0xacde71e0 (LWP 2687)]
> [New Thread 0xac5e61e0 (LWP 2688)]
> [New Thread 0xabbff1e0 (LWP 2689)]
> 2021-12-07 13:16:38.652 I Starting core RPC server...
> [New Thread 0xab3fe1e0 (LWP 2690)]
> [New Thread 0xaabfd1e0 (LWP 2691)]
> 2021-12-07 13:16:38.655 I core RPC server started ok
> [New Thread 0xa9b851e0 (LWP 2692)]
> [New Thread 0xa93841e0 (LWP 2693)]
> [New Thread 0xa8b831e0 (LWP 2694)]
> 2021-12-07 13:16:38.661 I Starting p2p net loop...
> [New Thread 0xa81ff1e0 (LWP 2695)]
> [New Thread 0xa77ff1e0 (LWP 2696)]
> [New Thread 0xa72fe1e0 (LWP 2697)]
> [New Thread 0xa6bff1e0 (LWP 2698)]
> [New Thread 0xa64ff1e0 (LWP 2699)]
> [New Thread 0xa5dff1e0 (LWP 2700)]
> [New Thread 0xa56ff1e0 (LWP 2701)]
> [New Thread 0xa4fff1e0 (LWP 2702)]
> [New Thread 0xa48ff1e0 (LWP 2703)]
> [New Thread 0xa41ff1e0 (LWP 2704)]
> [New Thread 0xa3aff1e0 (LWP 2705)]
> 2021-12-07 13:16:39.664 I
> 2021-12-07 13:16:39.664 I **********************************************************************
> [New Thread 0xa33ff1e0 (LWP 2706)]
> 2021-12-07 13:16:39.665 I The daemon will start synchronizing with the network. This may take a long time to complete.
> 2021-12-07 13:16:39.665 I
> 2021-12-07 13:16:39.665 I You can set the level of process detailization through "set_log <level|categories>" command,
> 2021-12-07 13:16:39.666 I where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).
> [New Thread 0xa32fe1e0 (LWP 2707)]
> [New Thread 0xa31fd1e0 (LWP 2708)]
> 2021-12-07 13:16:39.667 I
> 2021-12-07 13:16:39.668 I Use the "help" command to see the list of available commands.
> 2021-12-07 13:16:39.669 I Use "help <command>" to see a command's documentation.
> 2021-12-07 13:16:39.669 I **********************************************************************
> [New Thread 0xa30fc1e0 (LWP 2709)]
> [Thread 0xa33ff1e0 (LWP 2706) exited]
> [Thread 0xa31fd1e0 (LWP 2708) exited]
> [Thread 0xa30fc1e0 (LWP 2709) exited]
> [Thread 0xa32fe1e0 (LWP 2707) exited]
> 2021-12-07 13:16:40.036 I [172.105.69.27:18080 OUT] Sync data returned a new top block candidate: 4401 -> 2509632 [Your node is 2505231 blocks (7.6 years) behind]
> 2021-12-07 13:16:40.037 I SYNCHRONIZATION started
> 
> Thread 17 "monerod" received signal SIGBUS, Bus error.
> [Switching to Thread 0xa56ff1e0 (LWP 2701)]
> 0x009b63bc in _ZN15portable_scheme12binary_codec6decodeINS_10tags_space7map_tagIJNS2_9field_tagINS_9key_space5key_tIJLc99ELc117ELc109ELc117ELc108ELc97ELc116ELc105ELc118ELc101ELc95ELc100ELc105ELc102ELc102ELc105ELc99ELc117ELc108ELc116ELc121EEEENS2_8base_tagIyLNS2_8endian_tE0EEELNS2_10optional_tE0EEENS4_INS6_IJLc99ELc117ELc109ELc117ELc108ELc97ELc116ELc105ELc118ELc101ELc95ELc100ELc105ELc102ELc102ELc105ELc99ELc117ELc108ELc116ELc121ELc95ELc116ELc111ELc112ELc54ELc52EEEESA_LSB_0EEENS4_INS6_IJLc102ELc105ELc114ELc115ELc116ELc95ELc98ELc108ELc111ELc99ELc107EEEENS2_8span_tagILj0EEELSB_0EEENS4_INS6_IJLc109ELc95ELc98ELc108ELc111ELc99ELc107ELc95ELc105ELc100ELc115EEEESH_LSB_0EEENS4_INS6_IJLc109ELc95ELc98ELc108ELc111ELc99ELc107ELc95ELc119ELc101ELc105ELc103ELc104ELc116ELc115EEEESH_LSB_0EEENS4_INS6_IJLc115ELc116ELc97ELc114ELc116ELc95ELc104ELc101ELc105ELc103ELc104ELc116EEEESA_LSB_0EEENS4_INS6_IJLc116ELc111ELc116ELc97ELc108ELc95ELc104ELc101ELc105ELc103ELc104ELc116EEEESA_LSB_0EEEEEENS_12scheme_space6schemeIN4epee10misc_utils11struct_initIN10cryptonote27NOTIFY_RESPONSE_CHAIN_ENTRY9request_tEEEvE7write_tEEESt4pairIbjEOT0_PKhjj ()
> 

### BT FULL

> (gdb) bt full
> #0  0x009b63bc in _ZN15portable_scheme12binary_codec6decodeINS_10tags_space7map_tagIJNS2_9field_tagINS_9key_space5key_tIJLc99ELc117ELc109ELc117ELc108ELc97ELc116ELc105ELc118ELc101ELc95ELc100ELc105ELc102ELc102ELc105ELc99ELc117ELc108ELc116ELc121EEEENS2_8base_tagIyLNS2_8endian_tE0EEELNS2_10optional_tE0EEENS4_INS6_IJLc99ELc117ELc109ELc117ELc108ELc97ELc116ELc105ELc118ELc101ELc95ELc100ELc105ELc102ELc102ELc105ELc99ELc117ELc108ELc116ELc121ELc95ELc116ELc111ELc112ELc54ELc52EEEESA_LSB_0EEENS4_INS6_IJLc102ELc105ELc114ELc115ELc116ELc95ELc98ELc108ELc111ELc99ELc107EEEENS2_8span_tagILj0EEELSB_0EEENS4_INS6_IJLc109ELc95ELc98ELc108ELc111ELc99ELc107ELc95ELc105ELc100ELc115EEEESH_LSB_0EEENS4_INS6_IJLc109ELc95ELc98ELc108ELc111ELc99ELc107ELc95ELc119ELc101ELc105ELc103ELc104ELc116ELc115EEEESH_LSB_0EEENS4_INS6_IJLc115ELc116ELc97ELc114ELc116ELc95ELc104ELc101ELc105ELc103ELc104ELc116EEEESA_LSB_0EEENS4_INS6_IJLc116ELc111ELc116ELc97ELc108ELc95ELc104ELc101ELc105ELc103ELc104ELc116EEEESA_LSB_0EEEEEENS_12scheme_space6schemeIN4epee10misc_utils11struct_initIN10cryptonote27NOTIFY_RESPONSE_CHAIN_ENTRY9request_tEEEvE7write_tEEESt4pairIbjEOT0_PKhjj ()
> No symbol table info available.
> #1  0x009b64f2 in bool portable_scheme::load_from_binary<epee::misc_utils::struct_init<cryptonote::NOTIFY_RESPONSE_CHAIN_ENTRY::request_t> >(epee::misc_utils::struct_init<cryptonote::NOTIFY_RESPONSE_CHAIN_ENTRY::request_t>&, epee::span<unsigned char const> const&) ()
> No symbol table info available.
> #2  0x006c80be in int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, epee::span<unsigned char const>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&) ()
> No symbol table info available.
> #3  0x006c8e30 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::notify(int, epee::span<unsigned char const>, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&) ()
> No symbol table info available.
> #4  0x00881b68 in epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv(void const*, unsigned int) ()
> No symbol table info available.
> #5  0x008bef34 in epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_read(boost::system::error_code const&, unsigned int) ()
> No symbol table info available.
> #6  0x008a5db8 in void boost::asio::detail::strand_service::dispatch<boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned int>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned int> >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned int>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned int>&) ()
> No symbol table info available.
> #7  0x008a632a in boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned int>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned int>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned int>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > >, boost::asio::io_context::basic_executor_type<std::allocator<void>, 0u> >::do_complete(void*, boost::asio::detail::scheduler_operation*, boost::system::error_code const&, unsigned int) ()
> No symbol table info available.
> #8  0x008a65f6 in void boost::asio::detail::strand_service::dispatch<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned int>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned int>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned int>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned int>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned int>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned int>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > >&) ()
> No symbol table info available.
> #9  0x008a68da in boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned int>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::asio::execution::any_executor<boost::asio::execution::context_as_t<boost::asio::execution_context&>, boost::asio::execution::detail::blocking::never_t<0>, boost::asio::execution::prefer_only<boost::asio::execution::detail::blocking::possibly_t<0> >, boost::asio::execution::prefer_only<boost::asio::execution::detail::outstanding_work::tracked_t<0> >, boost::asio::execution::prefer_only<boost::asio::execution::detail::outstanding_work::untracked_t<0> >, boost::asio::execution::prefer_only<boost::asio::execution::detail::relationship::fork_t<0> >, boost::asio::execution::prefer_only<boost::asio::execution::detail::relationship::continuation_t<0> > > >::do_complete(void*, boost::asio::detail::scheduler_operation*, boost::system::error_code const&, unsigned int) ()
> No symbol table info available.
> #10 0x006bd112 in boost::asio::detail::scheduler::do_run_one(boost::asio::detail::conditionally_enabled_mutex::scoped_lock&, boost::asio::detail::scheduler_thread_info&, boost::system::error_code const&) ()
> No symbol table info available.
> #11 0x008616a6 in boost::asio::detail::scheduler::run(boost::system::error_code&) [clone .isra.0] ()
> No symbol table info available.
> #12 0x00884e5a in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
> No symbol table info available.
> #13 0xb6a8d200 in ?? () from /lib/arm-linux-gnueabihf/libboost_thread.so.1.74.0
> No symbol table info available.
> #14 0xb685d98e in start_thread () from /lib/arm-linux-gnueabihf/libpthread.so.0
> No symbol table info available.
> #15 0xb67f8bec in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
> No symbol table info available.
> Backtrace stopped: previous frame identical to this frame (corrupt stack?)
> (gdb)
> 

## selsta | 2021-12-11T02:28:49+00:00
So when did this issue start happening exactly? And you said it happens on different hardware?

Did you also try the binary from getmonero.org? Does the same issue exist there?

## shermand100 | 2021-12-11T11:36:30+00:00
So this is from the PiNodeXMR project I manage (https://github.com/monero-ecosystem/PiNode-XMR). It builds from source as we use the onion-monero-blockchain-explorer. This was reported to me by one of my users who was using the new Debian Bullseye. I replicated it with my Raspberry Pi (which now pushes Bullseye as the default OS), and Odroid XU4 using the Armbian Bullseye OS. A third user has also experienced the same with Bullseye.

Using Debian Buster builds and runs Monero without this issue.

As a temporary measure the project is now using the ARMv7 binaries from getmonero.org and there is no problem using them. All Error free.
Using the binaries though mean we've lost functionality of the block explorer so I'm keen to find a solution.

## selsta | 2021-12-11T18:10:50+00:00
Can you show me the exact steps that are used to build the binary? (Link to the script for example)

## shermand100 | 2021-12-11T23:56:32+00:00
Edit: So there is the script method (1) below how the issue was found, but to avoid you having to dig through clutter I've added a separate header bellow (2) that shows todays build on a clean Bullseye install with resulting Bus Error:

### (1) Script
Sure. This was the script: https://github.com/monero-ecosystem/PiNode-XMR/blob/164a713ce3438000a7bb051fb3d086b04ea159a9/raspbian-pinodexmr.sh

Dependencies install lines 27-52
Monero Install 155-177 (Where `$RELEASE` is `release-v0.17`).

In future though I'd like to build by latest tag.
Monero was installed in the above way for a little over a year I guess, which I initially got from https://github.com/moneroexamples/monero-compilation/blob/master/README.md#example-compilation-of-monero-on-ubuntu-2004

I have since on fresh installs followed https://github.com/monero-project/monero#compiling-monero-from-source including following note [1] of the dependencies table.
One compilation I tried following the table exactly line by line rather than the "Install all dependencies at once on Debian/Ubuntu:" section.

So in summary, the first script of mine I linked to used to work. On finding the error I've solely relied on the Monero github instructions for building. This SIGBUS error again only on Bullseye. Either way above builds and runs fine on Buster.

### (2) line-by-line install

Download disk image "Armbian_21.08.6_Odroidxu4_bullseye_current_5.4.160" from https://www.armbian.com/odroid-xu4/
Login as "root" and set password
Create user "pinodexmr"
Set locale/language as "en_GB.UTF.8"
`sudo apt update && sudo apt upgrade -y`
`reboot`

**Login as "pinodexmr"
Download Monero dependencies:**
`sudo apt update && sudo apt install git build-essential cmake pkg-config libssl-dev libzmq3-dev libunbound-dev libsodium-dev libunwind8-dev liblzma-dev libreadline6-dev libldns-dev libexpat1-dev libpgm-dev qttools5-dev-tools libhidapi-dev libusb-1.0-0-dev libprotobuf-dev protobuf-compiler libudev-dev libboost-chrono-dev libboost-date-time-dev libboost-filesystem-dev libboost-locale-dev libboost-program-options-dev libboost-regex-dev libboost-serialization-dev libboost-system-dev libboost-thread-dev ccache doxygen graphviz` #list copied from https://github.com/monero-project/monero#dependencies + git added

**Dependencies continued. (Note [1] of https://github.com/monero-project/monero#dependencies)**
`sudo apt-get install libgtest-dev && cd /usr/src/gtest && sudo cmake . && sudo make`
Debian instructions show empty directory, Ubuntu path below is actual location:
`sudo mv lib/libg* /usr/lib/`

**Clone and build Monero
At user pinodexmr home:**
`git clone --recursive https://github.com/monero-project/monero`
`cd monero`
`git checkout release-v0.17`
`git submodule init && git submodule update`
`make`

> pinodexmr@odroidxu4:~/monero/build/Linux/release-v0.17/release/bin$ ./monerod
> 2021-12-12 18:02:31.016 I Monero 'Oxygen Orion' (v0.17.3.0-release)
> 2021-12-12 18:02:31.016 I Initializing cryptonote protocol...
> 2021-12-12 18:02:31.016 I Cryptonote protocol initialized OK
> 2021-12-12 18:02:31.020 I Initializing core...
> 2021-12-12 18:02:31.024 I Loading blockchain from folder /home/pinodexmr/.bitmonero/lmdb ...
> 2021-12-12 18:02:31.677 I Loading checkpoints
> 2021-12-12 18:02:31.677 I Core initialized OK
> 2021-12-12 18:02:31.677 I Initializing p2p server...
> 2021-12-12 18:02:31.688 I p2p server initialized OK
> 2021-12-12 18:02:31.689 I Initializing core RPC server...
> 2021-12-12 18:02:31.689 I Binding on 127.0.0.1 (IPv4):18081
> 2021-12-12 18:02:45.466 I core RPC server initialized OK on port: 18081
> 2021-12-12 18:02:45.491 I Starting core RPC server...
> 2021-12-12 18:02:45.492 I core RPC server started ok
> 2021-12-12 18:02:45.525 I Starting p2p net loop...
> 2021-12-12 18:02:46.528 I
> 2021-12-12 18:02:46.528 I **********************************************************************
> 2021-12-12 18:02:46.528 I The daemon will start synchronizing with the network. This may take a long time to complete.
> 2021-12-12 18:02:46.529 I
> 2021-12-12 18:02:46.529 I You can set the level of process detailization through "set_log <level|categories>" command,
> 2021-12-12 18:02:46.529 I where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).
> 2021-12-12 18:02:46.530 I
> 2021-12-12 18:02:46.530 I Use the "help" command to see the list of available commands.
> 2021-12-12 18:02:46.531 I Use "help <command>" to see a command's documentation.
> 2021-12-12 18:02:46.531 I **********************************************************************
> 2021-12-12 18:02:47.627 I [38.34.39.91:18080 OUT] Sync data returned a new top block candidate: 1 -> 9201 [Your node is 9200 blocks (6.4 days) behind]
> 2021-12-12 18:02:47.628 I SYNCHRONIZATION started
> 2021-12-12 18:02:47.774 I [95.216.13.126:18080 OUT] Sync data returned a new top block candidate: 1 -> 2513412 [Your node is 2513411 blocks (7.6 years) behind]
> 2021-12-12 18:02:47.774 I SYNCHRONIZATION started
> 2021-12-12 18:02:48.452 I Synced 101/2513412 (0%, 2513311 left)
> 2021-12-12 18:02:48.677 I Synced 201/2513412 (0%, 2513211 left)
> 2021-12-12 18:02:49.057 I Synced 301/2513412 (0%, 2513111 left)
> 2021-12-12 18:02:49.573 I Synced 401/2513412 (0%, 2513011 left)
> 2021-12-12 18:02:50.049 I Synced 501/2513412 (0%, 2512911 left)
> 2021-12-12 18:02:50.721 I Synced 601/2513412 (0%, 2512811 left)
> 2021-12-12 18:02:51.433 I Synced 701/2513412 (0%, 2512711 left)
> 2021-12-12 18:02:52.290 I Synced 801/2513412 (0%, 2512611 left)
> 2021-12-12 18:02:53.237 I Synced 901/2513412 (0%, 2512511 left)
> 2021-12-12 18:02:54.253 I Synced 1001/2513412 (0%, 2512411 left)
> Bus error

## Monerovirus | 2022-06-30T11:53:28+00:00
I want to note that I had this exact same issue on raspbian bullseye on a raspberry pi 4. It also seems to think my flash drive is a rotating disk for some reason. Thanks for the suggestion to use the armv7 binary file from getmonero.org, that solved the issue for me. 

## selsta | 2022-07-06T02:56:47+00:00
> It also seems to think my flash drive is a rotating disk for some reason.

@Monerovirus see https://github.com/monero-project/monero/issues/8104#issuecomment-1000199611, you can ignore it.

## shermand100 | 2022-07-11T09:17:50+00:00
Tldr: Can Close. Probably an issue with underlying kernel not Monero code.


The context of how this issue started is no longer a problem for me, put probably still exists. However the info below I think may help others to mitigate as I did. The PiNodeXMR project has moved from Debian Bullseye to Ubuntu Server 22.04 LTS and lots of compatibility issues have gone away.

As additional info for anyone else who stumbles across this I personally suspect (but have no way of confirming) that the Ubuntu images have better support for the Cortex A-53 / 72 processors used in the Raspberry Pi 3/4.  For reference there are known faults at the chip level: [Arm Developer errata notice](https://developer.arm.com/documentation/epm048406/2100/) where:

**835769:** AArch64 multiply-accumulate instruction might produce incorrect result (page 20 of that document)
and
**843419:** A load or store might access an incorrect address (page 22)


To mitigate for this gcc has additional build flags:

https://gcc.gnu.org/onlinedocs/gcc.pdf (Page 315)


> -mfix-cortex-a53-835769
> -mno-fix-cortex-a53-835769
> Enable or disable the workaround for the ARM Cortex-A53 erratum number
> 835769. This involves inserting a NOP instruction between memory instructions
> and 64-bit integer multiply-accumulate instructions.
> 
> 
> -mfix-cortex-a53-843419
> -mno-fix-cortex-a53-843419
> Enable or disable the workaround for the ARM Cortex-A53 erratum number
> 843419. This erratum workaround is made at link time and this will only pass
> the corresponding flag to the linker.


Which Monero implemented:

[monero-project/monero/commit/cf10e05cc6a0ed495dbdd44ec3a76b964b14edba](https://github.com/monero-project/monero/commit/cf10e05cc6a0ed495dbdd44ec3a76b964b14edba)



And can be seen working/triggered as during build. As I said above I doubt this is working properly with Debian Bullseye.



Moving forward I've found that when using:

 Raspberry Pi **3** building with Ubuntu Server **32**bit 22.04 LTS successfully builds Monero and the monero-onion-block-explorer and all functions correctly. (64 bit builds Monero but breaks block-explorer)

 Raspberry Pi **4** building with Ubuntu Server **64**bit 22.04 LTS successfully builds Monero, monero-onion-block-explorer and P2Pool and all functions correctly.



## selsta | 2022-07-12T01:51:09+00:00
Thank you for the update :) I'll keep it in mind if I see a similar issue report.

# Action History
- Created by: shermand100 | 2021-11-30T20:02:04+00:00
- Closed at: 2022-07-12T01:51:09+00:00
