---
title: monerod segfaults immediately after upgrade
source_url: https://github.com/monero-project/monero/issues/5338
author: cryptosven76
assignees: []
labels: []
created_at: '2019-03-23T23:11:21+00:00'
updated_at: '2019-03-24T01:54:18+00:00'
type: issue
status: closed
closed_at: '2019-03-24T01:54:18+00:00'
---

# Original Description
i did a fresh git checkout this morning and compiled . segfaults immediately : 

root@monerod:/home/crypt/binaries/monero/build# /home/crypt/binaries/monero/build/bin/monerod --rpc-bind-ip 0.0.0.0 --confirm-external-bind --rpc-ssl disabled
2019-03-23 23:06:40.562     7fcf68c25bc0        INFO    global  src/daemon/main.cpp:280 Monero 'Boron Butterfly' (v0.14.1.0-cd776b19)
2019-03-23 23:06:40.563     7fcf68c25bc0        INFO    global  src/daemon/protocol.h:53        Initializing cryptonote protocol...
2019-03-23 23:06:40.564     7fcf68c25bc0        INFO    global  src/daemon/protocol.h:58        Cryptonote protocol initialized OK
2019-03-23 23:06:40.564     7fcf68c25bc0        INFO    global  src/daemon/p2p.h:63     Initializing p2p server...
Segmentation fault (core dumped)
root@monerod:/home/crypt/binaries/monero/build#

last successful build was 4 weeks ago. 

running it in gdb i get : 

Temporary breakpoint 1 at 0x1daf00
Starting program: /home/crypt/binaries/monero/build/bin/monerod
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Temporary breakpoint 1, 0x000055555572ef00 in main ()
(gdb) run
The program being debugged has been started already.
Start it from the beginning? (y or n) n
Program not restarted.
(gdb) cont
Continuing.
2019-03-23 23:10:45.238     7ffff7fd9bc0        INFO    global  src/daemon/main.cpp:280 Monero 'Boron Butterfly' (v0.14.1.0-cd776b19)
2019-03-23 23:10:45.238     7ffff7fd9bc0        INFO    global  src/daemon/protocol.h:53        Initializing cryptonote protocol...
2019-03-23 23:10:45.238     7ffff7fd9bc0        INFO    global  src/daemon/protocol.h:58        Cryptonote protocol initialized OK
2019-03-23 23:10:45.239     7ffff7fd9bc0        INFO    global  src/daemon/p2p.h:63     Initializing p2p server...
[New Thread 0x7ffff14c7700 (LWP 307)]
[New Thread 0x7ffff0cc6700 (LWP 308)]
[New Thread 0x7fffebfff700 (LWP 309)]
[New Thread 0x7fffeb7fe700 (LWP 310)]

Thread 2 "monerod" received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0x7ffff14c7700 (LWP 307)]
0x0000555555aeed7d in tools::dns_utils::parse_dns_public[abi:cxx11](char const*) ()
(gdb) bt
#0  0x0000555555aeed7d in tools::dns_utils::parse_dns_public[abi:cxx11](char const*) ()
#1  0x0000555555af04a2 in tools::DNSResolver::DNSResolver() ()
#2  0x0000555555af0d2c in tools::DNSResolver::instance() ()
#3  0x000055555598333d in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::init(boost::program_options::variables_map const&)::{lambda()#1}::operator()() const
    ()
#4  0x00007ffff590bbcd in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.65.1
#5  0x00007ffff4da36db in start_thread (arg=0x7ffff14c7700) at pthread_create.c:463
#6  0x00007ffff4acc88f in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95
(gdb)


# Discussion History
## moneromooo-monero | 2019-03-23T23:49:13+00:00
https://github.com/monero-project/monero/pull/5324

## cryptosven76 | 2019-03-24T01:54:17+00:00
the patch fixes the problem : 

root@monerod:/home/crypt/binaries/monero/build# /home/crypt/binaries/monero/build/bin/monerod --rpc-bind-ip 0.0.0.0 --confirm-external-bind --rpc-ssl disabled
2019-03-24 01:53:27.115     7f701afecbc0        INFO    global  src/daemon/main.cpp:280 Monero 'Boron Butterfly' (v0.14.1.0-cd776b19)
2019-03-24 01:53:27.115     7f701afecbc0        INFO    global  src/daemon/protocol.h:53        Initializing cryptonote protocol...
2019-03-24 01:53:27.115     7f701afecbc0        INFO    global  src/daemon/protocol.h:58        Cryptonote protocol initialized OK
2019-03-24 01:53:27.115     7f701afecbc0        INFO    global  src/daemon/p2p.h:63     Initializing p2p server...
2019-03-24 01:53:48.212     7f701afecbc0        INFO    global  src/daemon/p2p.h:68     p2p server initialized OK
2019-03-24 01:53:48.213     7f701afecbc0        INFO    global  src/daemon/rpc.h:62     Initializing core RPC server...

thanks 

# Action History
- Created by: cryptosven76 | 2019-03-23T23:11:21+00:00
- Closed at: 2019-03-24T01:54:18+00:00
