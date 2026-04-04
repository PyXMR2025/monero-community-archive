---
title: bitmonerod aborting
source_url: https://github.com/monero-project/monero/issues/373
author: skunk73
assignees: []
labels: []
created_at: '2015-08-14T19:13:53+00:00'
updated_at: '2016-02-24T15:59:52+00:00'
type: issue
status: closed
closed_at: '2016-02-24T15:59:52+00:00'
---

# Original Description
on linux latest bitmonerod master code stops from time to time with the following message:

bitmonerod: /usr/include/boost/thread/pthread/recursive_mutex.hpp:110: void boost::recursive_mutex::lock(): Assertion `!pthread_mutex_lock(&m)' failed.
Aborted

$ ldd bin/bitmonerod 
        linux-vdso.so.1 (0x00007ffc19f9b000)
        librt.so.1 => /lib64/librt.so.1 (0x00007fce98899000)
        libboost_chrono.so.1.56.0 => /usr/lib64/libboost_chrono.so.1.56.0 (0x00007fce98692000)
        libboost_filesystem.so.1.56.0 => /usr/lib64/libboost_filesystem.so.1.56.0 (0x00007fce9847b000)
        libboost_program_options.so.1.56.0 => /usr/lib64/libboost_program_options.so.1.56.0 (0x00007fce98205000)
        libboost_regex.so.1.56.0 => /usr/lib64/libboost_regex.so.1.56.0 (0x00007fce97f01000)
        libboost_system.so.1.56.0 => /usr/lib64/libboost_system.so.1.56.0 (0x00007fce97cfe000)
        libboost_thread.so.1.56.0 => /usr/lib64/libboost_thread.so.1.56.0 (0x00007fce97adb000)
        libminiupnpc.so.9 => /usr/lib64/libminiupnpc.so.9 (0x00007fce978cf000)
        libdb_cxx-5.1.so => /usr/lib64/libdb_cxx-5.1.so (0x00007fce9752d000)
        libboost_serialization.so.1.56.0 => /usr/lib64/libboost_serialization.so.1.56.0 (0x00007fce972cb000)
        libunbound.so.2 => /usr/lib64/libunbound.so.2 (0x00007fce96ffa000)
        libboost_date_time.so.1.56.0 => /usr/lib64/libboost_date_time.so.1.56.0 (0x00007fce96de9000)
        libstdc++.so.6 => /usr/lib/gcc/x86_64-pc-linux-gnu/4.9.2/libstdc++.so.6 (0x00007fce96ade000)
        libm.so.6 => /lib64/libm.so.6 (0x00007fce967e2000)
        libgcc_s.so.1 => /usr/lib/gcc/x86_64-pc-linux-gnu/4.9.2/libgcc_s.so.1 (0x00007fce965cc000)
        libpthread.so.0 => /lib64/libpthread.so.0 (0x00007fce963b0000)
        libc.so.6 => /lib64/libc.so.6 (0x00007fce96013000)
        libicuuc.so.55 => /usr/lib64/libicuuc.so.55 (0x00007fce95c85000)
        libicui18n.so.55 => /usr/lib64/libicui18n.so.55 (0x00007fce95827000)
        libicudata.so.55 => /usr/lib64/libicudata.so.55 (0x00007fce93d71000)
        libssl.so.1.0.0 => /usr/lib64/libssl.so.1.0.0 (0x00007fce93b05000)
        libevent-2.0.so.5 => /usr/lib64/libevent-2.0.so.5 (0x00007fce938c0000)
        libdl.so.2 => /lib64/libdl.so.2 (0x00007fce936bc000)
        libpython2.7.so.1.0 => /usr/lib64/libpython2.7.so.1.0 (0x00007fce932f3000)
        libcrypto.so.1.0.0 => /usr/lib64/libcrypto.so.1.0.0 (0x00007fce92f1d000)
        /lib64/ld-linux-x86-64.so.2 (0x00007fce98aa1000)
        libutil.so.1 => /lib64/libutil.so.1 (0x00007fce92d1a000)
        libz.so.1 => /lib64/libz.so.1 (0x00007fce92b04000)


# Discussion History
## skunk73 | 2015-08-14T19:17:16+00:00
/usr/include/boost/thread/pthread/recursive_mutex.hpp:

[...]
#ifdef BOOST_HAS_PTHREAD_MUTEXATTR_SETTYPE
        void lock()
        {
            BOOST_VERIFY(!pthread_mutex_lock(&m));           <--- line 110
        }
[...]


## skunk73 | 2015-09-03T02:48:20+00:00
commit f43d465da20864e9fc25fc3dd3f904c1a35bd8f9 makes bitmonerod segfault at start...

Creating the logger system
2015-Sep-03 04:40:17.127173 Initializing cryptonote protocol...
2015-Sep-03 04:40:17.127280 Cryptonote protocol initialized OK
2015-Sep-03 04:40:17.127561 Initializing p2p server...
**\* Error in `./bitmonerod': free(): invalid pointer: 0x00007f951c001280 ***
Segmentation fault


## crypto750 | 2015-09-03T07:20:26+00:00
I compiled with commit f43d465 on linux, no segfault at start. This is my setup:

ldd ./bitmonerod
    linux-vdso.so.1 (0x00007fffb7dea000)
    librt.so.1 => /lib/x86_64-linux-gnu/librt.so.1 (0x00007ffb84122000)
    libboost_chrono.so.1.58.0 => /usr/lib/x86_64-linux-gnu/libboost_chrono.so.1.58.0 (0x00007ffb83f1a000)
    libboost_filesystem.so.1.58.0 => /usr/lib/x86_64-linux-gnu/libboost_filesystem.so.1.58.0 (0x00007ffb83d00000)
    libboost_program_options.so.1.58.0 => /usr/lib/x86_64-linux-gnu/libboost_program_options.so.1.58.0 (0x00007ffb83a82000)
    libboost_regex.so.1.58.0 => /usr/lib/x86_64-linux-gnu/libboost_regex.so.1.58.0 (0x00007ffb83774000)
    libboost_system.so.1.58.0 => /usr/lib/x86_64-linux-gnu/libboost_system.so.1.58.0 (0x00007ffb8356f000)
    libboost_thread.so.1.58.0 => /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0 (0x00007ffb83349000)
    libminiupnpc.so.10 => /usr/lib/x86_64-linux-gnu/libminiupnpc.so.10 (0x00007ffb8313d000)
    libdb_cxx-5.3.so => /usr/lib/x86_64-linux-gnu/libdb_cxx-5.3.so (0x00007ffb82d55000)
    libboost_serialization.so.1.58.0 => /usr/lib/x86_64-linux-gnu/libboost_serialization.so.1.58.0 (0x00007ffb82af2000)
    libunbound.so.2 => /usr/lib/x86_64-linux-gnu/libunbound.so.2 (0x00007ffb82864000)
    libboost_date_time.so.1.58.0 => /usr/lib/x86_64-linux-gnu/libboost_date_time.so.1.58.0 (0x00007ffb82652000)
    libstdc++.so.6 => /usr/lib/x86_64-linux-gnu/libstdc++.so.6 (0x00007ffb822d7000)
    libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007ffb81fd6000)
    libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007ffb81dbf000)
    libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007ffb81ba2000)
    libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007ffb817f9000)
    libicudata.so.55 => /usr/lib/x86_64-linux-gnu/libicudata.so.55 (0x00007ffb7fd41000)
    libicui18n.so.55 => /usr/lib/x86_64-linux-gnu/libicui18n.so.55 (0x00007ffb7f8de000)
    libicuuc.so.55 => /usr/lib/x86_64-linux-gnu/libicuuc.so.55 (0x00007ffb7f54a000)
    libssl.so.1.0.0 => /usr/lib/x86_64-linux-gnu/libssl.so.1.0.0 (0x00007ffb7f2df000)
    libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007ffb7f0db000)
    libcrypto.so.1.0.0 => /usr/lib/x86_64-linux-gnu/libcrypto.so.1.0.0 (0x00007ffb7ec79000)
    /lib64/ld-linux-x86-64.so.2 (0x00007ffb84338000)


## skunk73 | 2015-09-08T17:15:50+00:00
after rebuilding master with cmake -DCMAKE_BUILD_TYPE=Debug
i ran bitmonerod inside gdb and got the following result:

```
$ gdb ./bin/bitmonerod
GNU gdb (Gentoo 7.9.1 vanilla) 7.9.1
Copyright (C) 2015 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-pc-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://bugs.gentoo.org/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
Reading symbols from ./bin/bitmonerod...done.
(gdb) run
Starting program: /home/skunk/bitcoin/bitmonero/build/bin/bitmonerod
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib64/libthread_db.so.1".
Creating the logger system
2015-Sep-08 19:02:03.615587 Initializing cryptonote protocol...
2015-Sep-08 19:02:03.666430 Cryptonote protocol initialized OK
2015-Sep-08 19:02:03.666692 Initializing p2p server...
[New Thread 0x7fffebfff700 (LWP 13586)]
[New Thread 0x7ffff0e3b700 (LWP 13585)]
[New Thread 0x7ffff163c700 (LWP 13584)]
[New Thread 0x7ffff1e3d700 (LWP 13583)]

Program received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0x7ffff0e3b700 (LWP 13585)]
0x00007ffff6361b80 in ?? () from /usr/lib64/libunbound.so.2
(gdb) bt
#0  0x00007ffff6361b80 in ?? () from /usr/lib64/libunbound.so.2
#1  0x00007ffff6361d10 in ?? () from /usr/lib64/libunbound.so.2
#2  0x00007ffff6345413 in ?? () from /usr/lib64/libunbound.so.2
#3  0x00007ffff63465bf in ub_resolve () from /usr/lib64/libunbound.so.2
#4  0x00000000007d1128 in tools::DNSResolver::get_record (this=0x7fffec0008c0, url=..., record_type=record_type@entry=1,
    reader=reader@entry=0x7d18f3 <tools::ipv4_to_string(char const*, unsigned long)>, dnssec_available=@0x7ffff0e3ac5e: false, dnssec_valid=@0x7ffff0e3ac5f: false)
    at /home/skunk/bitcoin/bitmonero/src/common/dns_utils.cpp:240
#5  0x00000000007d127b in tools::DNSResolver::get_ipv4 (this=<optimized out>, url=..., dnssec_available=@0x7ffff0e3ac5e: false, dnssec_valid=@0x7ffff0e3ac5f: false)
    at /home/skunk/bitcoin/bitmonero/src/common/dns_utils.cpp:258
#6  0x00000000005e3e39 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::init(boost::program_options::variables_map const&)::{lambda()#1}::operator()() const (__closure=0x1ddf9a8) at /home/skunk/bitcoin/bitmonero/src/p2p/net_node.inl:324
#7  0x00000000005e4404 in boost::detail::thread_data<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::init(boost::program_options::variables_map const&)::{lambda()#1}>::run() (this=<optimized out>) at /usr/include/boost/thread/detail/thread.hpp:115
#8  0x00007ffff6e2731a in ?? () from /usr/lib64/libboost_thread.so.1.56.0
#9  0x00007ffff56f15c4 in start_thread () from /lib64/libpthread.so.0
#10 0x00007ffff5436edd in clone () from /lib64/libc.so.6
```

any known issue with boost 1.56?
any kind soul able to share with me how to sort it out or how to better debug it?
thank you.


## crypto750 | 2015-09-09T10:44:35+00:00
Is this not a libunbound issue?
git clone https://github.com/jedisct1/unbound; ./configure --prefix=/usr --libdir=/usr/lib64; make; make install;


## skunk73 | 2015-09-09T11:16:04+00:00
the same happens with latest unbound-1.5.4


## moneromooo-monero | 2016-02-06T13:43:05+00:00
Does it also happen if you build with "make release-static" ? This builds with the libunbound in the monero tree. If it still does, gdb might give some more info on the stack. If not, and you know how to switch release to debug, you can do that (BUILD_TYPE=Debug instead of Release, there's no target for this apparently). This should give better debug info from inside libunbound calls.


## skunk73 | 2016-02-15T13:45:26+00:00
$ make release-static
make: **\* No rule to make target 'release-static'.  Stop.

thank you


## moneromooo-monero | 2016-02-21T16:18:20+00:00
Are you running that in the root of the monero tree ?
If so, paste the Makefile file on fpaste.org.


## skunk73 | 2016-02-21T17:31:58+00:00
ran it from root's tree right afer "cmake -DBERKELEY_DB_INCLUDE_DIR=/usr/include/db5.3 "

https://bpaste.net/show/660d35a7ed51

thank you


## moneromooo-monero | 2016-02-22T08:39:32+00:00
Looks like cmake has nuked the makefile. Restore the original one.


## moneromooo-monero | 2016-02-22T08:40:53+00:00
And you want:

mkdir build/release
cd build/release
cmake -DBERKELEY_DB_INCLUDE_DIR=/usr/include/db5.3 ../..

to avoid cmake overwriting the monero makefile.


## skunk73 | 2016-02-23T13:14:13+00:00
same result:

```
skunk@mescalito ~/bitcoin $ git clone https://github.com/monero-project/bitmonero.git
Cloning into 'bitmonero'...
remote: Counting objects: 15750, done.
remote: Compressing objects: 100% (22/22), done.
remote: Total 15750 (delta 8), reused 0 (delta 0), pack-reused 15728
Receiving objects: 100% (15750/15750), 42.45 MiB | 1.41 MiB/s, done.
Resolving deltas: 100% (11326/11326), done.
Checking connectivity... done.
skunk@mescalito ~/bitcoin $ cd bitmonero
skunk@mescalito ~/bitcoin/bitmonero $ mkdir -p build/release
skunk@mescalito ~/bitcoin/bitmonero $ cd build/release
skunk@mescalito ~/bitcoin/bitmonero/build/release $ cmake -DBERKELEY_DB_INCLUDE_DIR=/usr/include/db5.3 ../..
-- The C compiler identification is GNU 4.9.3
-- The CXX compiler identification is GNU 4.9.3
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Could not find DEVELOPER_LOCAL_TOOLS in env (not required)
-- BOOST_IGNORE_SYSTEM_PATHS defaults to OFF
-- Could not find DEVELOPER_LIBUNBOUND_OLD in env (not required)
-- Building for a 64-bit system
-- Could not find DATABASE in env (not required unless you want to change database type from default: lmdb)
-- Found Berkeley: /usr/include/db5.3  
-- Found BerkeleyDB include (db.h) in /usr/include/db5.3
-- Found BerkeleyDB shared library
-- Using LMDB as default DB type
-- Looking for include file pthread.h
-- Looking for include file pthread.h - found
-- Looking for pthread_create
-- Looking for pthread_create - not found
-- Check if compiler accepts -pthread
-- Check if compiler accepts -pthread - yes
-- Found Threads: TRUE  
-- Found the miniupnpc libraries at /usr/lib64/libminiupnpc.so
-- Found the miniupnpc headers at /usr/include/miniupnpc
-- Detecting version of miniupnpc in path: /usr/include/miniupnpc
-- Performing Test MINIUPNPC_VERSION_1_7_OR_HIGHER
-- Performing Test MINIUPNPC_VERSION_1_7_OR_HIGHER - Success
-- Found miniupnpc version is v1.7 or higher
-- Using shared miniupnpc found at /usr/include/miniupnpc
-- Looking for libunbound
-- Found libunbound include (unbound.h) in /usr/include
-- Found libunbound shared library
-- Using 64-bit LMDB from source tree
-- Enabling AES support
-- Found Git: /usr/bin/git
Doxygen: graphviz not found - graphs disabled
-- Found Doxygen: /usr/bin/doxygen (found version "1.8.10") 
-- Configuring done
-- Generating done
-- Build files have been written to: /home/skunk/bitcoin/bitmonero/build/release
skunk@mescalito ~/bitcoin/bitmonero/build/release $ make release-static
make: *** No rule to make target 'release-static'.  Stop.
```


## moneromooo-monero | 2016-02-24T15:03:19+00:00
You need to run make in the root tree. Only cmake in build/release.


## skunk73 | 2016-02-24T15:59:49+00:00
ops... sorry...
after rebuilding the boost package statically, bitmonerod builds and runs fine.
thank you!


# Action History
- Created by: skunk73 | 2015-08-14T19:13:53+00:00
- Closed at: 2016-02-24T15:59:52+00:00
