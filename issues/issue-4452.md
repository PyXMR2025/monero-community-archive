---
title: monerod Illegal instruction on oDroid c2 with ubuntu 18.04
source_url: https://github.com/monero-project/monero/issues/4452
author: Onefox
assignees: []
labels: []
created_at: '2018-09-26T07:25:32+00:00'
updated_at: '2022-02-22T21:46:41+00:00'
type: issue
status: closed
closed_at: '2022-02-22T21:46:41+00:00'
---

# Original Description
I started getting Illegal instruction crashes while syncing the chain.


I build the current master, here is the build log:
https://pastebin.com/A9r5M4vR

I only used USE_SINGLE_BUILDDIR=1.

With the same device I was able to run a self compiled node under ubuntu 16.04.

This is the ldd output if its usefull:
   
  ````linux-vdso.so.1 (0x0000007f8b2d2000)
        libboost_chrono.so.1.65.1 => /usr/lib/aarch64-linux-gnu/libboost_chrono.so.1.65.1 (0x0000007f8aaf9000)
        libboost_filesystem.so.1.65.1 => /usr/lib/aarch64-linux-gnu/libboost_filesystem.so.1.65.1 (0x0000007f8aacf000)
        libboost_program_options.so.1.65.1 => /usr/lib/aarch64-linux-gnu/libboost_program_options.so.1.65.1 (0x0000007f8aa3d000)
        libboost_regex.so.1.65.1 => /usr/lib/aarch64-linux-gnu/libboost_regex.so.1.65.1 (0x0000007f8a924000)
        libboost_system.so.1.65.1 => /usr/lib/aarch64-linux-gnu/libboost_system.so.1.65.1 (0x0000007f8a90f000)
        libzmq.so.5 => /usr/lib/aarch64-linux-gnu/libzmq.so.5 (0x0000007f8a86a000)
        libsodium.so.23 => /usr/lib/aarch64-linux-gnu/libsodium.so.23 (0x0000007f8a82b000)
        libreadline.so.7 => /lib/aarch64-linux-gnu/libreadline.so.7 (0x0000007f8a7d5000)
        libdl.so.2 => /lib/aarch64-linux-gnu/libdl.so.2 (0x0000007f8a7c0000)
        libunbound.so.2 => /usr/lib/aarch64-linux-gnu/libunbound.so.2 (0x0000007f8a704000)
        libssl.so.1.1 => /usr/lib/aarch64-linux-gnu/libssl.so.1.1 (0x0000007f8a699000)
        libcrypto.so.1.1 => /usr/lib/aarch64-linux-gnu/libcrypto.so.1.1 (0x0000007f8a49c000)
        libboost_serialization.so.1.65.1 => /usr/lib/aarch64-linux-gnu/libboost_serialization.so.1.65.1 (0x0000007f8a44a000)
        libboost_thread.so.1.65.1 => /usr/lib/aarch64-linux-gnu/libboost_thread.so.1.65.1 (0x0000007f8a414000)
        libstdc++.so.6 => /usr/lib/aarch64-linux-gnu/libstdc++.so.6 (0x0000007f8a281000)
        libm.so.6 => /lib/aarch64-linux-gnu/libm.so.6 (0x0000007f8a1c7000)
        libgcc_s.so.1 => /lib/aarch64-linux-gnu/libgcc_s.so.1 (0x0000007f8a1a3000)
        libpthread.so.0 => /lib/aarch64-linux-gnu/libpthread.so.0 (0x0000007f8a177000)
        libc.so.6 => /lib/aarch64-linux-gnu/libc.so.6 (0x0000007f8a01c000)
        /lib/ld-linux-aarch64.so.1 (0x0000007f8b2a8000)
        libicui18n.so.60 => /usr/lib/aarch64-linux-gnu/libicui18n.so.60 (0x0000007f89d5f000)
        libicuuc.so.60 => /usr/lib/aarch64-linux-gnu/libicuuc.so.60 (0x0000007f89b8a000)
        libpgm-5.2.so.0 => /usr/lib/aarch64-linux-gnu/libpgm-5.2.so.0 (0x0000007f89b31000)
        libnorm.so.1 => /usr/lib/aarch64-linux-gnu/libnorm.so.1 (0x0000007f899f1000)
        libtinfo.so.5 => /lib/aarch64-linux-gnu/libtinfo.so.5 (0x0000007f899b7000)
        libevent-2.1.so.6 => /usr/lib/aarch64-linux-gnu/libevent-2.1.so.6 (0x0000007f8995d000)
        libhogweed.so.4 => /usr/lib/aarch64-linux-gnu/libhogweed.so.4 (0x0000007f8991c000)
        libnettle.so.6 => /usr/lib/aarch64-linux-gnu/libnettle.so.6 (0x0000007f898db000)
        libgmp.so.10 => /usr/lib/aarch64-linux-gnu/libgmp.so.10 (0x0000007f8985e000)
        libicudata.so.60 => /usr/lib/aarch64-linux-gnu/libicudata.so.60 (0x0000007f87ea3000)
````

# Discussion History
## moneromooo-monero | 2018-09-26T08:39:42+00:00
Do you have a stack trace of that error ? You night need to be running a debug build in order for the stack trace to be intelligible.


## Onefox | 2018-09-27T19:17:52+00:00
Is there anything that I should do while building the debug build?

With make debug I get an error on the build:
````
make[3]: Leaving directory '/root/monero/build/Linux/master/debug'
[ 74%] Built target daemon_rpc_server
make[3]: Entering directory '/root/monero/build/Linux/master/debug'
make[3]: Leaving directory '/root/monero/build/Linux/master/debug'
make[3]: Entering directory '/root/monero/build/Linux/master/debug'
[ 75%] Building CXX object src/wallet/CMakeFiles/obj_wallet.dir/wallet2.cpp.o
c++: internal compiler error: Killed (program cc1plus)
Please submit a full bug report,
with preprocessed source if appropriate.
See <file:///usr/share/doc/gcc-7/README.Bugs> for instructions.
src/wallet/CMakeFiles/obj_wallet.dir/build.make:62: recipe for target 'src/wallet/CMakeFiles/obj_wallet.dir/wallet2.cpp.o'
failed
make[3]: *** [src/wallet/CMakeFiles/obj_wallet.dir/wallet2.cpp.o] Error 4
make[3]: Leaving directory '/root/monero/build/Linux/master/debug'
````


## moneromooo-monero | 2018-09-27T20:23:56+00:00
Free more memory.

## Onefox | 2018-10-04T17:04:38+00:00
Thanks, I could build the debug daemon now. Still the behavoir or output didn't change.

````
**********************************************************************
The daemon will start synchronizing with the network. This may take a long time to complete.

You can set the level of process detailization through "set_log <level|categories>" command,
where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).

Use the "help" command to see the list of available commands.
Use "help <command>" to see a command's documentation.
**********************************************************************

2018-10-04 17:01:24.434 [P2P1]  WARN    net.dns src/common/dns_utils.cpp:518    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2018-10-04 17:01:34.447 [P2P6]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:310     [xxx.xxx.xxx.xxx:8180 OUT] Sync data returned a new top block candidate: 1667312 -> 1675650 [Your node is 8338 blocks (11 days) behind]
SYNCHRONIZATION started
Illegal instruction

````


## moneromooo-monero | 2018-10-04T17:13:57+00:00
And what is the stack trace ?

## Onefox | 2018-10-04T17:20:11+00:00
Silly question but where do I find the stack trace?

## moneromooo-monero | 2018-10-04T17:23:06+00:00
See the README for detailed instructions.

## Onefox | 2018-10-04T18:25:14+00:00
````
~/monero/build/Linux/master/debug/bin# gdb ./monerod
GNU gdb (Ubuntu 8.1-0ubuntu3) 8.1.0.20180409-git
Copyright (C) 2018 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "aarch64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from ./monerod...done.
(gdb) run
Starting program: /root/monero/build/Linux/master/debug/bin/monerod
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/aarch64-linux-gnu/libthread_db.so.1".
2018-10-04 17:33:02,654 INFO  [default] Page size: 4096

Program received signal SIGILL, Illegal instruction.
0x0000007fb715e3a8 in ?? () from /usr/lib/aarch64-linux-gnu/libcrypto.so.1.1
(gdb) thread apply all bt

Thread 1 (Thread 0x7fb466c010 (LWP 1539)):
#0  0x0000007fb715e3a8 in ?? () from /usr/lib/aarch64-linux-gnu/libcrypto.so.1.1
#1  0x0000007fb72c7240 in ?? () from /usr/lib/aarch64-linux-gnu/libcrypto.so.1.1
Backtrace stopped: previous frame inner to this frame (corrupt stack?)
(gdb)
````

Not that much infromation here or?

## moneromooo-monero | 2018-10-04T18:36:08+00:00
Not much. You might have to build openssl with debug symbols and no opts. Not sure why it's getting used though.

## ghost | 2018-10-16T00:35:58+00:00
I suspect this is the issue I was having where it was compiling with crypto extensions on ARMv8, when the Odroid C2's chip doesn't support hardware AES.

I think you have to do `export NO_AES=1` before compiling. I'm hoping to fix this soon in CMakeLists.txt 

# Action History
- Created by: Onefox | 2018-09-26T07:25:32+00:00
- Closed at: 2022-02-22T21:46:41+00:00
