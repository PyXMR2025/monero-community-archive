---
title: 'monerod: High CPU usage after 2-3 days'
source_url: https://github.com/monero-project/monero/issues/8685
author: BotoX
assignees: []
labels: []
created_at: '2022-12-21T20:36:22+00:00'
updated_at: '2023-06-27T16:29:04+00:00'
type: issue
status: closed
closed_at: '2023-06-27T16:29:04+00:00'
---

# Original Description
I've been running a monero node "Monero 'Fluorine Fermi' (v0.18.1.2-release)" on Archlinux for a few months now.
Every few days I have to restart monerod, as it will constantly use around 160-180% CPU.
Regular CPU usage is around 2-10%

I think that this hasn't been an issue from the start, but is now constantly plaguing me.
I can still connect and use the daemon as a remote wallet when this happens.

Here's my config:
```
# Configuration for monerod
# Syntax: any command line option may be specified as 'clioptionname=value'.
#         Boolean options such as 'no-igd' are specified as 'no-igd=1'.
# See 'monerod --help' for all available options.

# Data directory (blockchain db and indices)
data-dir=/var/lib/monero

# Log file
log-file=/var/log/monero/monerod.log
log-level=0
max-log-file-size=0            # Prevent monerod from managing the log files; we want logrotate to take care of that

# P2P full node
p2p-bind-ip=0.0.0.0            # Bind to all interfaces (the default)
p2p-bind-port=18080            # Bind to default port

# RPC open node
rpc-bind-ip=0.0.0.0            # Bind to all interfaces
rpc-bind-port=18081            # Bind on default port
confirm-external-bind=1        # Open node (confirm)
restricted-rpc=1               # Prevent unsafe RPC calls
rpc-ssl=enabled
rpc-ssl-certificate=/etc/ssl/private/monerod.pem
rpc-ssl-private-key=/etc/ssl/private/monerod.key
rpc-login=****
no-igd=1                       # Disable UPnP port mapping
no-zmq=1                       # Disable ZMQ RPC server to decrease attack surface (it's not used)


# Emergency checkpoints set by MoneroPulse operators will be enforced to workaround potential consensus bugs
# Check https://monerodocs.org/infrastructure/monero-pulse/ for explanation and trade-offs
enforce-dns-checkpointing=1
enable-dns-blocklist=1

out-peers=16              # This will enable much faster sync and tx awareness; the default 8 is suboptimal nowadays
in-peers=64               # The default is unlimited; we prefer to put a cap on this

limit-rate-up=30000     # 1048576 kB/s == 1GB/s; a raise from default 2048 kB/s; contribute more to p2p network
limit-rate-down=100000   # 1048576 kB/s == 1GB/s; a raise from default 8192 kB/s; allow for faster initial sync
```

I've attached the monerod log file here, from start to finish:
[monerod.log.txt](https://github.com/monero-project/monero/files/10280925/monerod.log.txt)
Though I suppose I should've raised the log-level to 1 before reporting this, in any case I have now so just need to wait another two to three days.

CPU usage started rising around 2022-12-21 11:32:00
![image](https://user-images.githubusercontent.com/395711/208996920-5d1d66a4-4016-4755-98c8-f92f1ed368d0.png)

I've also made a core dump before restarting the monero daemon:
https://cloud.botox.bz/s/HrgRyR8d9Nk3gxb

Edit: I should've run perf to find out where exactly monerod was wasting cpu cycles, ooops. will do soon.

# Discussion History
## selsta | 2022-12-21T23:07:18+00:00
`perf` output and `--log-level 2` would be interesting.

## vtnerd | 2022-12-22T13:54:29+00:00
You can also look up poorman's profiler which can be run at anytime after launch using special `gdb` commands. This is probably TCP server related, but its easier with at least some stack trace to begin the investigation.

## jkhsjdhjs | 2022-12-22T18:00:43+00:00
Downstream bug report: https://bugs.archlinux.org/task/76735 (It also contains links to perf top outputs)

I've been trying to debug this issue for a while already. Also asked on the IRC channel, no luck.
Since it doesn't occur with the binary from the monero website, I'm currently trying various build configurations with older dependencies since I thought that maybe a recent version of a library is buggy (Arch's packages are usually far more up to date than most distributions).
Last thing I tried was building with boost 1.74 (Arch currently has 1.80), but the same issue appeared.

But maybe you have an idea of what's wrong by looking at the perf output.

## jkhsjdhjs | 2022-12-23T15:04:10+00:00
I gathered 2 stack traces with poor man's profiler (`gdb -ex "set pagination 0" -ex "thread apply all bt"   --batch -p $(pidof monerod)`): https://gist.github.com/jkhsjdhjs/0f7a3dd8d3aaba4636588958df6c6293

Thread 38 seems to be one of the threads causing high CPU usage, since the stack traces matches with the `perf top -a` output. Not sure which thread the other one is though.

If I count the main process of monerod as thread 1, then monerod has exactly 56 threads as gdb says. Counting this way, the threads causing high cpu usage would be 37 and 38.

## BotoX | 2022-12-27T16:17:48+00:00
The issue happened again within a few days, however I was sick so I've just attached gdb and let it sleep until I was feeling good enough to come back to it.

A `perf record -F 99 -p <pid> -g -- sleep 120` fed into FlameGraph identifies the epoll loop as a cluprit.
![monerod](https://user-images.githubusercontent.com/395711/209672898-802cb3ea-d5b9-4394-a8ef-4e912d059703.svg)

Sadly I have not recompiled monero with symbols, so information is missing on monerod function names...

Here's a screenshots from perf report:
![image](https://user-images.githubusercontent.com/395711/209673135-e0487f98-c01f-46f4-8954-bcd58860d4e6.png)

I have now built the monero arch pkg with '!strip' and CMAKE_BUILD_TYPE=debug and started it with `valgrind --tool=callgrind --instr-atstart=no` (and then use callgrind_control -i on when the CPU usage rises again).
~~So in 2-3 days I should hopefully have a nice callgrind file that can be loaded into KCachegrind, etc. and analyzed.~~
(Btw. I had to recompile valgrind and raise the virtual memory limit to 512GB, lmdb wasn't able to open the blockchain)
Nevermind, monerod won't sync a single block while running under valgrind...
But at least I have symbols now for perf

## BotoX | 2022-12-29T21:19:15+00:00
New perf report:
![image](https://user-images.githubusercontent.com/395711/210012021-c7405766-3176-415b-9133-c2e920afc02c.png)

and FlameGraph:
![monerod](https://user-images.githubusercontent.com/395711/210012050-466d94bd-071a-407a-8e50-0030dc95492d.svg)

poor mans profiler output:
```
awk: cmd. line:4: warning: regexp escape sequence `\#' is not a known regexp operator
      9 ??,pthread_cond_wait,boost::asio::detail::posix_event::wait<boost::asio::detail::conditionally_enabled_mutex::scoped_lock>,this=0x555e7103f158),lock=...,,boost::asio::detail::scheduler::run,boost::asio::io_context::run,>::worker_thread,??,??,??
      7 ??,pthread_cond_wait,boost::posix::pthread_cond_wait,<tools::threadpool::getInstanceForIO()::instance+80>,,tools::threadpool::run,??,??,??
      5 ??,pthread_cond_wait,boost::posix::pthread_cond_wait,<tools::threadpool::getInstanceForCompute()::instance+80>,,tools::threadpool::run,??,??,??
      1 ??,pthread_cond_wait,??,boost::thread::join_noexcept(),boost::thread::join,>::run_server,nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>,daemonize::t_p2p::run,daemonize::t_daemon::run,daemonize::t_executor::run_non_interactive,daemonizer::daemonize<daemonize::t_executor>,out>,,out>,
      1 ??,pthread_cond_wait,boost::asio::detail::posix_event::wait<boost::asio::detail::conditionally_enabled_mutex::scoped_lock>,this=0x555e70c737b8),lock=...,,boost::asio::detail::scheduler::run,boost::asio::io_context::run,??,??,??
      1 ??,pthread_cond_timedwait,boost::posix::pthread_cond_timedwait,m=...,,(pred=<optimized,at,at,operator(),(this=0x555e710ffd40),??,??,??
      1 ??,pthread_cond_timedwait,boost::posix::pthread_cond_timedwait,m=...,,1000000000l>,1l>,,1l>,nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>,??,??,??
      1 OPENSSL_init_crypto,??,??,boost::asio::ssl::detail::engine::perform,boost::asio::ssl::detail::engine::shutdown,0,,boost::asio::ssl::detail::shutdown_op,,boost::asio::ssl::detail::async_io<boost::asio::basic_stream_socket<boost::asio::ip::tcp,,>::initiate_async_shutdown::operator()<boost::asio::detail::wrapped_handler<boost::asio::io_context::strand,,>::start_shutdown()::{lambda(boost::system::error_code,>::start_shutdown()::{lambda(boost::system::error_code,>::async_shutdown<boost::asio::detail::wrapped_handler<boost::asio::io_context::strand,,const,>::start_shutdown()::{lambda()#2}&,,epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base>,boost::asio::io_context::basic_executor_type<std::allocator<void>,,boost::asio::io_context::basic_executor_type<std::allocator<void>,,boost::asio::detail::scheduler_operation::complete,base=0x7f399002d620,,boost::asio::detail::scheduler_operation::complete,lock=...,,boost::asio::detail::scheduler::run,boost::asio::io_context::run,(this=0x555e710e5f88),??,??,??
      1 epoll_wait,boost::asio::detail::epoll_reactor::run,boost::asio::detail::scheduler::do_run_one,boost::asio::detail::scheduler::run,boost::asio::io_context::run,>::worker_thread,??,??,??
      1 epoll_wait,boost::asio::detail::epoll_reactor::run,boost::asio::detail::scheduler::do_run_one,boost::asio::detail::scheduler::run,boost::asio::io_context::run,(this=0x555e710e5f88),??,??,??
      1
```

full gdb output `gdb -ex "set pagination 0" -ex "thread apply all bt" --batch -p $(pidof monerod)`:
```

Thread 28 (Thread 0x7f397f5fd6c0 (LWP 41160) "monerod"):
#0  0x00007f628a5f8096 in epoll_wait () from /usr/lib/libc.so.6
#1  0x0000555e6f1422db in boost::asio::detail::epoll_reactor::run (this=0x555e70d00260, usec=<optimized out>, ops=...) at /usr/include/boost/asio/detail/impl/epoll_reactor.ipp:501
#2  0x0000555e6f151ddf in boost::asio::detail::scheduler::do_run_one (this=0x555e7103f0f0, lock=..., this_thread=..., ec=...) at /usr/include/boost/asio/detail/impl/scheduler.ipp:476
#3  0x00007f628bd39cf2 in boost::asio::detail::scheduler::run (this=0x555e7103f0f0, ec=...) at /usr/include/boost/asio/detail/impl/scheduler.ipp:210
#4  0x00007f628bd7d32f in boost::asio::io_context::run (this=<optimized out>) at /usr/include/boost/asio/impl/io_context.ipp:63
#5  epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread (this=0x555e710639d0) at /usr/src/debug/monero/monero/contrib/epee/include/net/abstract_tcp_server2.inl:1320
#6  0x00007f628aa7acbb in ?? () from /usr/lib/libboost_thread.so.1.80.0
#7  0x00007f628a5768fd in ?? () from /usr/lib/libc.so.6
#8  0x00007f628a5f8a60 in ?? () from /usr/lib/libc.so.6

Thread 27 (Thread 0x7f397fafe6c0 (LWP 41159) "monerod"):
#0  0x00007f628a5734b6 in ?? () from /usr/lib/libc.so.6
#1  0x00007f628a575cd0 in pthread_cond_wait () from /usr/lib/libc.so.6
#2  0x0000555e6f151f7c in boost::asio::detail::posix_event::wait<boost::asio::detail::conditionally_enabled_mutex::scoped_lock> (lock=..., this=0x555e7103f160) at /usr/include/boost/asio/detail/conditionally_enabled_mutex.hpp:98
#3  boost::asio::detail::conditionally_enabled_event::wait (lock=..., this=0x555e7103f158) at /usr/include/boost/asio/detail/conditionally_enabled_event.hpp:97
#4  boost::asio::detail::scheduler::do_run_one (this=0x555e7103f0f0, lock=..., this_thread=..., ec=...) at /usr/include/boost/asio/detail/impl/scheduler.ipp:501
#5  0x00007f628bd39cf2 in boost::asio::detail::scheduler::run (this=0x555e7103f0f0, ec=...) at /usr/include/boost/asio/detail/impl/scheduler.ipp:210
#6  0x00007f628bd7d32f in boost::asio::io_context::run (this=<optimized out>) at /usr/include/boost/asio/impl/io_context.ipp:63
#7  epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread (this=0x555e710639d0) at /usr/src/debug/monero/monero/contrib/epee/include/net/abstract_tcp_server2.inl:1320
#8  0x00007f628aa7acbb in ?? () from /usr/lib/libboost_thread.so.1.80.0
#9  0x00007f628a5768fd in ?? () from /usr/lib/libc.so.6
#10 0x00007f628a5f8a60 in ?? () from /usr/lib/libc.so.6

Thread 26 (Thread 0x7f397ffff6c0 (LWP 41158) "monerod"):
#0  0x00007f628a5734b6 in ?? () from /usr/lib/libc.so.6
#1  0x00007f628a575cd0 in pthread_cond_wait () from /usr/lib/libc.so.6
#2  0x0000555e6f151f7c in boost::asio::detail::posix_event::wait<boost::asio::detail::conditionally_enabled_mutex::scoped_lock> (lock=..., this=0x555e7103f160) at /usr/include/boost/asio/detail/conditionally_enabled_mutex.hpp:98
#3  boost::asio::detail::conditionally_enabled_event::wait (lock=..., this=0x555e7103f158) at /usr/include/boost/asio/detail/conditionally_enabled_event.hpp:97
#4  boost::asio::detail::scheduler::do_run_one (this=0x555e7103f0f0, lock=..., this_thread=..., ec=...) at /usr/include/boost/asio/detail/impl/scheduler.ipp:501
#5  0x00007f628bd39cf2 in boost::asio::detail::scheduler::run (this=0x555e7103f0f0, ec=...) at /usr/include/boost/asio/detail/impl/scheduler.ipp:210
#6  0x00007f628bd7d32f in boost::asio::io_context::run (this=<optimized out>) at /usr/include/boost/asio/impl/io_context.ipp:63
#7  epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread (this=0x555e710639d0) at /usr/src/debug/monero/monero/contrib/epee/include/net/abstract_tcp_server2.inl:1320
#8  0x00007f628aa7acbb in ?? () from /usr/lib/libboost_thread.so.1.80.0
#9  0x00007f628a5768fd in ?? () from /usr/lib/libc.so.6
#10 0x00007f628a5f8a60 in ?? () from /usr/lib/libc.so.6

Thread 25 (Thread 0x7f39989f66c0 (LWP 41157) "monerod"):
#0  0x00007f628a5734b6 in ?? () from /usr/lib/libc.so.6
#1  0x00007f628a575cd0 in pthread_cond_wait () from /usr/lib/libc.so.6
#2  0x0000555e6f151f7c in boost::asio::detail::posix_event::wait<boost::asio::detail::conditionally_enabled_mutex::scoped_lock> (lock=..., this=0x555e7103f160) at /usr/include/boost/asio/detail/conditionally_enabled_mutex.hpp:98
#3  boost::asio::detail::conditionally_enabled_event::wait (lock=..., this=0x555e7103f158) at /usr/include/boost/asio/detail/conditionally_enabled_event.hpp:97
#4  boost::asio::detail::scheduler::do_run_one (this=0x555e7103f0f0, lock=..., this_thread=..., ec=...) at /usr/include/boost/asio/detail/impl/scheduler.ipp:501
#5  0x00007f628bd39cf2 in boost::asio::detail::scheduler::run (this=0x555e7103f0f0, ec=...) at /usr/include/boost/asio/detail/impl/scheduler.ipp:210
#6  0x00007f628bd7d32f in boost::asio::io_context::run (this=<optimized out>) at /usr/include/boost/asio/impl/io_context.ipp:63
#7  epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread (this=0x555e710639d0) at /usr/src/debug/monero/monero/contrib/epee/include/net/abstract_tcp_server2.inl:1320
#8  0x00007f628aa7acbb in ?? () from /usr/lib/libboost_thread.so.1.80.0
#9  0x00007f628a5768fd in ?? () from /usr/lib/libc.so.6
#10 0x00007f628a5f8a60 in ?? () from /usr/lib/libc.so.6

Thread 24 (Thread 0x7f3998ef76c0 (LWP 41156) "monerod"):
#0  0x00007f628a5734b6 in ?? () from /usr/lib/libc.so.6
#1  0x00007f628a575cd0 in pthread_cond_wait () from /usr/lib/libc.so.6
#2  0x0000555e6f151f7c in boost::asio::detail::posix_event::wait<boost::asio::detail::conditionally_enabled_mutex::scoped_lock> (lock=..., this=0x555e7103f160) at /usr/include/boost/asio/detail/conditionally_enabled_mutex.hpp:98
#3  boost::asio::detail::conditionally_enabled_event::wait (lock=..., this=0x555e7103f158) at /usr/include/boost/asio/detail/conditionally_enabled_event.hpp:97
#4  boost::asio::detail::scheduler::do_run_one (this=0x555e7103f0f0, lock=..., this_thread=..., ec=...) at /usr/include/boost/asio/detail/impl/scheduler.ipp:501
#5  0x00007f628bd39cf2 in boost::asio::detail::scheduler::run (this=0x555e7103f0f0, ec=...) at /usr/include/boost/asio/detail/impl/scheduler.ipp:210
#6  0x00007f628bd7d32f in boost::asio::io_context::run (this=<optimized out>) at /usr/include/boost/asio/impl/io_context.ipp:63
#7  epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread (this=0x555e710639d0) at /usr/src/debug/monero/monero/contrib/epee/include/net/abstract_tcp_server2.inl:1320
#8  0x00007f628aa7acbb in ?? () from /usr/lib/libboost_thread.so.1.80.0
#9  0x00007f628a5768fd in ?? () from /usr/lib/libc.so.6
#10 0x00007f628a5f8a60 in ?? () from /usr/lib/libc.so.6

Thread 23 (Thread 0x7f39993f86c0 (LWP 41155) "monerod"):
#0  0x00007f628a5734b6 in ?? () from /usr/lib/libc.so.6
#1  0x00007f628a575cd0 in pthread_cond_wait () from /usr/lib/libc.so.6
#2  0x0000555e6f151f7c in boost::asio::detail::posix_event::wait<boost::asio::detail::conditionally_enabled_mutex::scoped_lock> (lock=..., this=0x555e7103f160) at /usr/include/boost/asio/detail/conditionally_enabled_mutex.hpp:98
#3  boost::asio::detail::conditionally_enabled_event::wait (lock=..., this=0x555e7103f158) at /usr/include/boost/asio/detail/conditionally_enabled_event.hpp:97
#4  boost::asio::detail::scheduler::do_run_one (this=0x555e7103f0f0, lock=..., this_thread=..., ec=...) at /usr/include/boost/asio/detail/impl/scheduler.ipp:501
#5  0x00007f628bd39cf2 in boost::asio::detail::scheduler::run (this=0x555e7103f0f0, ec=...) at /usr/include/boost/asio/detail/impl/scheduler.ipp:210
#6  0x00007f628bd7d32f in boost::asio::io_context::run (this=<optimized out>) at /usr/include/boost/asio/impl/io_context.ipp:63
#7  epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread (this=0x555e710639d0) at /usr/src/debug/monero/monero/contrib/epee/include/net/abstract_tcp_server2.inl:1320
#8  0x00007f628aa7acbb in ?? () from /usr/lib/libboost_thread.so.1.80.0
#9  0x00007f628a5768fd in ?? () from /usr/lib/libc.so.6
#10 0x00007f628a5f8a60 in ?? () from /usr/lib/libc.so.6

Thread 22 (Thread 0x7f39998f96c0 (LWP 41154) "monerod"):
#0  0x00007f628a5734b6 in ?? () from /usr/lib/libc.so.6
#1  0x00007f628a575cd0 in pthread_cond_wait () from /usr/lib/libc.so.6
#2  0x0000555e6f151f7c in boost::asio::detail::posix_event::wait<boost::asio::detail::conditionally_enabled_mutex::scoped_lock> (lock=..., this=0x555e7103f160) at /usr/include/boost/asio/detail/conditionally_enabled_mutex.hpp:98
#3  boost::asio::detail::conditionally_enabled_event::wait (lock=..., this=0x555e7103f158) at /usr/include/boost/asio/detail/conditionally_enabled_event.hpp:97
#4  boost::asio::detail::scheduler::do_run_one (this=0x555e7103f0f0, lock=..., this_thread=..., ec=...) at /usr/include/boost/asio/detail/impl/scheduler.ipp:501
#5  0x00007f628bd39cf2 in boost::asio::detail::scheduler::run (this=0x555e7103f0f0, ec=...) at /usr/include/boost/asio/detail/impl/scheduler.ipp:210
#6  0x00007f628bd7d32f in boost::asio::io_context::run (this=<optimized out>) at /usr/include/boost/asio/impl/io_context.ipp:63
#7  epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread (this=0x555e710639d0) at /usr/src/debug/monero/monero/contrib/epee/include/net/abstract_tcp_server2.inl:1320
#8  0x00007f628aa7acbb in ?? () from /usr/lib/libboost_thread.so.1.80.0
#9  0x00007f628a5768fd in ?? () from /usr/lib/libc.so.6
#10 0x00007f628a5f8a60 in ?? () from /usr/lib/libc.so.6

Thread 21 (Thread 0x7f3999dfa6c0 (LWP 41153) "monerod"):
#0  0x00007f628a5734b6 in ?? () from /usr/lib/libc.so.6
#1  0x00007f628a575cd0 in pthread_cond_wait () from /usr/lib/libc.so.6
#2  0x0000555e6f151f7c in boost::asio::detail::posix_event::wait<boost::asio::detail::conditionally_enabled_mutex::scoped_lock> (lock=..., this=0x555e7103f160) at /usr/include/boost/asio/detail/conditionally_enabled_mutex.hpp:98
#3  boost::asio::detail::conditionally_enabled_event::wait (lock=..., this=0x555e7103f158) at /usr/include/boost/asio/detail/conditionally_enabled_event.hpp:97
#4  boost::asio::detail::scheduler::do_run_one (this=0x555e7103f0f0, lock=..., this_thread=..., ec=...) at /usr/include/boost/asio/detail/impl/scheduler.ipp:501
#5  0x00007f628bd39cf2 in boost::asio::detail::scheduler::run (this=0x555e7103f0f0, ec=...) at /usr/include/boost/asio/detail/impl/scheduler.ipp:210
#6  0x00007f628bd7d32f in boost::asio::io_context::run (this=<optimized out>) at /usr/include/boost/asio/impl/io_context.ipp:63
#7  epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread (this=0x555e710639d0) at /usr/src/debug/monero/monero/contrib/epee/include/net/abstract_tcp_server2.inl:1320
#8  0x00007f628aa7acbb in ?? () from /usr/lib/libboost_thread.so.1.80.0
#9  0x00007f628a5768fd in ?? () from /usr/lib/libc.so.6
#10 0x00007f628a5f8a60 in ?? () from /usr/lib/libc.so.6

Thread 20 (Thread 0x7f399a2fb6c0 (LWP 41152) "monerod"):
#0  0x00007f628a5734b6 in ?? () from /usr/lib/libc.so.6
#1  0x00007f628a575cd0 in pthread_cond_wait () from /usr/lib/libc.so.6
#2  0x0000555e6f151f7c in boost::asio::detail::posix_event::wait<boost::asio::detail::conditionally_enabled_mutex::scoped_lock> (lock=..., this=0x555e7103f160) at /usr/include/boost/asio/detail/conditionally_enabled_mutex.hpp:98
#3  boost::asio::detail::conditionally_enabled_event::wait (lock=..., this=0x555e7103f158) at /usr/include/boost/asio/detail/conditionally_enabled_event.hpp:97
#4  boost::asio::detail::scheduler::do_run_one (this=0x555e7103f0f0, lock=..., this_thread=..., ec=...) at /usr/include/boost/asio/detail/impl/scheduler.ipp:501
#5  0x00007f628bd39cf2 in boost::asio::detail::scheduler::run (this=0x555e7103f0f0, ec=...) at /usr/include/boost/asio/detail/impl/scheduler.ipp:210
#6  0x00007f628bd7d32f in boost::asio::io_context::run (this=<optimized out>) at /usr/include/boost/asio/impl/io_context.ipp:63
#7  epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread (this=0x555e710639d0) at /usr/src/debug/monero/monero/contrib/epee/include/net/abstract_tcp_server2.inl:1320
#8  0x00007f628aa7acbb in ?? () from /usr/lib/libboost_thread.so.1.80.0
#9  0x00007f628a5768fd in ?? () from /usr/lib/libc.so.6
#10 0x00007f628a5f8a60 in ?? () from /usr/lib/libc.so.6

Thread 19 (Thread 0x7f399a7fc6c0 (LWP 41151) "monerod"):
#0  0x00007f628a5734b6 in ?? () from /usr/lib/libc.so.6
#1  0x00007f628a575cd0 in pthread_cond_wait () from /usr/lib/libc.so.6
#2  0x0000555e6f151f7c in boost::asio::detail::posix_event::wait<boost::asio::detail::conditionally_enabled_mutex::scoped_lock> (lock=..., this=0x555e7103f160) at /usr/include/boost/asio/detail/conditionally_enabled_mutex.hpp:98
#3  boost::asio::detail::conditionally_enabled_event::wait (lock=..., this=0x555e7103f158) at /usr/include/boost/asio/detail/conditionally_enabled_event.hpp:97
#4  boost::asio::detail::scheduler::do_run_one (this=0x555e7103f0f0, lock=..., this_thread=..., ec=...) at /usr/include/boost/asio/detail/impl/scheduler.ipp:501
#5  0x00007f628bd39cf2 in boost::asio::detail::scheduler::run (this=0x555e7103f0f0, ec=...) at /usr/include/boost/asio/detail/impl/scheduler.ipp:210
#6  0x00007f628bd7d32f in boost::asio::io_context::run (this=<optimized out>) at /usr/include/boost/asio/impl/io_context.ipp:63
#7  epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread (this=0x555e710639d0) at /usr/src/debug/monero/monero/contrib/epee/include/net/abstract_tcp_server2.inl:1320
#8  0x00007f628aa7acbb in ?? () from /usr/lib/libboost_thread.so.1.80.0
#9  0x00007f628a5768fd in ?? () from /usr/lib/libc.so.6
#10 0x00007f628a5f8a60 in ?? () from /usr/lib/libc.so.6

Thread 18 (Thread 0x7f399affd6c0 (LWP 41150) "monerod"):
#0  0x00007f628a5734b6 in ?? () from /usr/lib/libc.so.6
#1  0x00007f628a575fd4 in pthread_cond_timedwait () from /usr/lib/libc.so.6
#2  0x00007f628bd71a4f in boost::posix::pthread_cond_timedwait (t=0x7f399affc940, m=0x7f399affc9f0, c=0x7f399affca18) at /usr/include/boost/thread/pthread/pthread_helpers.hpp:123
#3  boost::condition_variable::do_wait_until (timeout=..., m=..., this=0x7f399affc9f0) at /usr/include/boost/thread/pthread/condition_variable.hpp:122
#4  boost::condition_variable::wait_until<boost::chrono::duration<long, boost::ratio<1l, 1000000000l> >, bool (*)()> (t=..., pred=<optimized out>, lock=..., this=0x7f399affc9f0) at /usr/include/boost/thread/pthread/condition_variable_fwd.hpp:288
#5  boost::condition_variable::wait_for<long, boost::ratio<1l, 1l>, bool (*)()> (pred=<optimized out>, d=..., lock=..., this=0x7f399affc9f0) at /usr/include/boost/thread/pthread/condition_variable_fwd.hpp:321
#6  boost::this_thread::sleep_for<long, boost::ratio<1l, 1l> > (d=...) at /usr/include/boost/thread/pthread/thread_data.hpp:300
#7  0x00007f628bd7eb0c in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::run()::{lambda()#1}::operator()() const (__closure=<optimized out>) at /usr/src/debug/monero/monero/src/p2p/net_node.inl:1034
#8  0x00007f628aa7acbb in ?? () from /usr/lib/libboost_thread.so.1.80.0
#9  0x00007f628a5768fd in ?? () from /usr/lib/libc.so.6
#10 0x00007f628a5f8a60 in ?? () from /usr/lib/libc.so.6

Thread 17 (Thread 0x7f399b7fe6c0 (LWP 41149) "monerod"):
#0  0x00007f628a5f8096 in epoll_wait () from /usr/lib/libc.so.6
#1  0x0000555e6f1422db in boost::asio::detail::epoll_reactor::run (this=0x555e710e9f30, usec=<optimized out>, ops=...) at /usr/include/boost/asio/detail/impl/epoll_reactor.ipp:501
#2  0x0000555e6f151ddf in boost::asio::detail::scheduler::do_run_one (this=this@entry=0x555e710e9dd0, lock=..., this_thread=..., ec=...) at /usr/include/boost/asio/detail/impl/scheduler.ipp:476
#3  0x0000555e6f12f492 in boost::asio::detail::scheduler::run (this=0x555e710e9dd0, ec=...) at /usr/include/boost/asio/detail/impl/scheduler.ipp:210
#4  0x0000555e6f1624ab in boost::asio::io_context::run (this=<optimized out>) at /usr/include/boost/asio/impl/io_context.ipp:63
#5  epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::worker_thread (this=0x555e710e5f88) at /usr/src/debug/monero/monero/contrib/epee/include/net/abstract_tcp_server2.inl:1320
#6  0x00007f628aa7acbb in ?? () from /usr/lib/libboost_thread.so.1.80.0
#7  0x00007f628a5768fd in ?? () from /usr/lib/libc.so.6
#8  0x00007f628a5f8a60 in ?? () from /usr/lib/libc.so.6

Thread 16 (Thread 0x7f399bfff6c0 (LWP 41148) "monerod"):
#0  0x00007f628a579b32 in pthread_mutex_lock () from /usr/lib/libc.so.6
#1  0x0000555e6f187271 in __gthread_mutex_lock (__mutex=0x7f3988078158) at /usr/include/c++/12.2.0/x86_64-pc-linux-gnu/bits/gthr-default.h:749
#2  std::mutex::lock (this=0x7f3988078158) at /usr/include/c++/12.2.0/bits/std_mutex.h:100
#3  std::lock_guard<std::mutex>::lock_guard (__m=..., this=<synthetic pointer>) at /usr/include/c++/12.2.0/bits/std_mutex.h:229
#4  epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}::operator()(boost::system::error_code const&) const (ec=..., __closure=0x7f399bffe220) at /usr/src/debug/monero/monero/contrib/epee/include/net/abstract_tcp_server2.inl:567
#5  boost::asio::detail::binder1<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::system::error_code>::operator()() (this=0x7f399bffe220) at /usr/include/boost/asio/detail/bind_handler.hpp:171
#6  boost::asio::asio_handler_invoke<boost::asio::detail::binder1<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::system::error_code> >(boost::asio::detail::binder1<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::system::error_code>&, ...) (function=...) at /usr/include/boost/asio/handler_invoke_hook.hpp:88
#7  boost_asio_handler_invoke_helpers::invoke<boost::asio::detail::binder1<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::system::error_code>, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}>(boost::asio::detail::binder1<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::system::error_code>&, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}&) (context=..., function=...) at /usr/include/boost/asio/detail/handler_invoke_helpers.hpp:54
#8  boost::asio::detail::asio_handler_invoke<boost::asio::detail::binder1<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::system::error_code>, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::system::error_code>(boost::asio::detail::binder1<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::system::error_code>&, boost::asio::detail::binder1<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::system::error_code>*) (this_handler=0x7f399bffe220, function=...) at /usr/include/boost/asio/detail/bind_handler.hpp:224
#9  boost_asio_handler_invoke_helpers::invoke<boost::asio::detail::binder1<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::system::error_code>, boost::asio::detail::binder1<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::system::error_code> >(boost::asio::detail::binder1<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::system::error_code>&, boost::asio::detail::binder1<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::system::error_code>&) (context=..., function=...) at /usr/include/boost/asio/detail/handler_invoke_helpers.hpp:54
#10 boost::asio::detail::strand_service::dispatch<boost::asio::detail::binder1<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::system::error_code> >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::binder1<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::system::error_code>&) (this=0x555e7122ac70, impl=@0x7f399bffe3a0: 0x7f399002d620, handler=...) at /usr/include/boost/asio/detail/impl/strand_service.hpp:44
#11 0x0000555e6f18fbab in boost::asio::io_context::strand::initiate_dispatch::operator()<boost::asio::detail::binder1<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::system::error_code> >(boost::asio::detail::binder1<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::system::error_code>&&, boost::asio::io_context::strand*) const (self=0x7f399bffe398, handler=..., this=<optimized out>) at /usr/include/boost/asio/detail/non_const_lvalue.hpp:31
#12 boost::asio::detail::completion_handler_async_result<boost::asio::detail::binder1<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::system::error_code>, void ()>::initiate<boost::asio::io_context::strand::initiate_dispatch, boost::asio::detail::binder1<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::system::error_code>, boost::asio::io_context::strand*>(boost::asio::io_context::strand::initiate_dispatch&&, boost::asio::detail::binder1<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::system::error_code>&&, boost::asio::io_context::strand*&&) (token=..., initiation=...) at /usr/include/boost/asio/async_result.hpp:482
#13 boost::asio::async_initiate<boost::asio::detail::binder1<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::system::error_code>, void (), boost::asio::io_context::strand::initiate_dispatch, boost::asio::io_context::strand*>(boost::asio::io_context::strand::initiate_dispatch&&, boost::asio::detail::binder1<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::system::error_code>&, boost::asio::io_context::strand*&&) (token=..., initiation=...) at /usr/include/boost/asio/async_result.hpp:896
#14 boost::asio::io_context::strand::dispatch<boost::asio::detail::binder1<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::system::error_code> >(boost::asio::detail::binder1<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::system::error_code>&&) (handler=..., this=0x7f399bffe398) at /usr/include/boost/asio/io_context_strand.hpp:199
#15 boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running>::operator()<boost::system::error_code>(boost::system::error_code const&) (arg1=..., this=0x7f399bffe398) at /usr/include/boost/asio/detail/wrapped_handler.hpp:87
#16 boost::asio::ssl::detail::shutdown_op::call_handler<boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running> >(boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running>&, boost::system::error_code const&, unsigned long const&) const (this=0x7f399bffe368, ec=..., handler=...) at /usr/include/boost/asio/ssl/detail/shutdown_op.hpp:59
#17 boost::asio::ssl::detail::io_op<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::any_io_executor>, boost::asio::ssl::detail::shutdown_op, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running> >::operator()(boost::system::error_code, unsigned long, int) (this=this@entry=0x7f399bffe358, ec=..., bytes_transferred=<optimized out>, start=start@entry=0) at /usr/include/boost/asio/ssl/detail/io.hpp:309
#18 0x0000555e6f19ada9 in boost::asio::detail::binder2<boost::asio::ssl::detail::io_op<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::any_io_executor>, boost::asio::ssl::detail::shutdown_op, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running> >, boost::system::error_code, unsigned long>::operator()() (this=0x7f399bffe358) at /usr/include/boost/asio/detail/bind_handler.hpp:289
#19 boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::ssl::detail::io_op<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::any_io_executor>, boost::asio::ssl::detail::shutdown_op, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running> >, boost::system::error_code, unsigned long>, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}>::operator()() (this=0x7f399bffe340) at /usr/include/boost/asio/detail/wrapped_handler.hpp:191
#20 boost::asio::asio_handler_invoke<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::ssl::detail::io_op<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::any_io_executor>, boost::asio::ssl::detail::shutdown_op, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running> >, boost::system::error_code, unsigned long>, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}> >(boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::ssl::detail::io_op<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::any_io_executor>, boost::asio::ssl::detail::shutdown_op, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running> >, boost::system::error_code, unsigned long>, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}>&, ...) (function=...) at /usr/include/boost/asio/handler_invoke_hook.hpp:88
#21 boost_asio_handler_invoke_helpers::invoke<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::ssl::detail::io_op<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::any_io_executor>, boost::asio::ssl::detail::shutdown_op, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running> >, boost::system::error_code, unsigned long>, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}>, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}>(boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::ssl::detail::io_op<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::any_io_executor>, boost::asio::ssl::detail::shutdown_op, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running> >, boost::system::error_code, unsigned long>, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}>&, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}&) (context=..., function=...) at /usr/include/boost/asio/detail/handler_invoke_helpers.hpp:54
#22 boost::asio::detail::asio_handler_invoke<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::ssl::detail::io_op<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::any_io_executor>, boost::asio::ssl::detail::shutdown_op, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running> >, boost::system::error_code, unsigned long>, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}>, boost::asio::detail::binder2<boost::asio::ssl::detail::io_op<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::any_io_executor>, boost::asio::ssl::detail::shutdown_op, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running> >, boost::system::error_code, unsigned long>, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}>(boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::ssl::detail::io_op<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::any_io_executor>, boost::asio::ssl::detail::shutdown_op, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running> >, boost::system::error_code, unsigned long>, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}>&, boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::ssl::detail::io_op<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::any_io_executor>, boost::asio::ssl::detail::shutdown_op, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running> >, boost::system::error_code, unsigned long>, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}>*) (this_handler=0x7f399bffe340, function=...) at /usr/include/boost/asio/detail/wrapped_handler.hpp:304
#23 boost_asio_handler_invoke_helpers::invoke<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::ssl::detail::io_op<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::any_io_executor>, boost::asio::ssl::detail::shutdown_op, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running> >, boost::system::error_code, unsigned long>, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}>, boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::ssl::detail::io_op<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::any_io_executor>, boost::asio::ssl::detail::shutdown_op, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running> >, boost::system::error_code, unsigned long>, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}> >(boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::ssl::detail::io_op<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::any_io_executor>, boost::asio::ssl::detail::shutdown_op, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running> >, boost::system::error_code, unsigned long>, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}>&, boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::ssl::detail::io_op<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::any_io_executor>, boost::asio::ssl::detail::shutdown_op, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running> >, boost::system::error_code, unsigned long>, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}>&) (context=..., function=...) at /usr/include/boost/asio/detail/handler_invoke_helpers.hpp:54
#24 boost::asio::detail::handler_work<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::ssl::detail::io_op<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::any_io_executor>, boost::asio::ssl::detail::shutdown_op, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running> >, boost::system::error_code, unsigned long>, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}>, boost::asio::io_context::basic_executor_type<std::allocator<void>, 0ul>, void>::complete<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::ssl::detail::io_op<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::any_io_executor>, boost::asio::ssl::detail::shutdown_op, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running> >, boost::system::error_code, unsigned long>, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}> >(boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::ssl::detail::io_op<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::any_io_executor>, boost::asio::ssl::detail::shutdown_op, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running> >, boost::system::error_code, unsigned long>, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}>&, boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::ssl::detail::io_op<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::any_io_executor>, boost::asio::ssl::detail::shutdown_op, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running> >, boost::system::error_code, unsigned long>, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}>&) (handler=..., function=..., this=<synthetic pointer>) at /usr/include/boost/asio/detail/handler_work.hpp:512
#25 boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::ssl::detail::io_op<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::any_io_executor>, boost::asio::ssl::detail::shutdown_op, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running> >, boost::system::error_code, unsigned long>, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}>, boost::asio::io_context::basic_executor_type<std::allocator<void>, 0ul> >::do_complete(void*, boost::asio::detail::scheduler_operation*, boost::system::error_code const&, unsigned long) (owner=0x555e710e9dd0, base=0x7f3990059850) at /usr/include/boost/asio/detail/completion_handler.hpp:74
#26 0x0000555e6f1536d5 in boost::asio::detail::scheduler_operation::complete (bytes_transferred=0, ec=..., owner=0x555e710e9dd0, this=0x7f3990059850) at /usr/include/boost/asio/detail/scheduler_operation.hpp:40
#27 boost::asio::detail::strand_service::do_dispatch (this=<optimized out>, impl=@0x7f399bffe5e8: 0x7f399002d620, op=0x7f3990059850) at /usr/include/boost/asio/detail/impl/strand_service.ipp:131
#28 0x0000555e6f19b0be in boost::asio::detail::strand_service::dispatch<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::ssl::detail::io_op<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::any_io_executor>, boost::asio::ssl::detail::shutdown_op, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running> >, boost::system::error_code, unsigned long>, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}> >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::ssl::detail::io_op<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::any_io_executor>, boost::asio::ssl::detail::shutdown_op, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running> >, boost::system::error_code, unsigned long>, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}>&) (this=0x555e7122ac70, impl=@0x7f399bffe5e8: 0x7f399002d620, handler=...) at /usr/include/boost/asio/io_context.hpp:688
#29 0x0000555e6f19b509 in boost::asio::io_context::strand::initiate_dispatch::operator()<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::ssl::detail::io_op<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::any_io_executor>, boost::asio::ssl::detail::shutdown_op, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running> >, boost::system::error_code, unsigned long>, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}> >(boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::ssl::detail::io_op<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::any_io_executor>, boost::asio::ssl::detail::shutdown_op, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running> >, boost::system::error_code, unsigned long>, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}>&&, boost::asio::io_context::strand*) const (self=0x7f399bffe5e0, handler=..., this=<optimized out>) at /usr/include/boost/asio/io_context_strand.hpp:356
#30 boost::asio::detail::completion_handler_async_result<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::ssl::detail::io_op<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::any_io_executor>, boost::asio::ssl::detail::shutdown_op, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running> >, boost::system::error_code, unsigned long>, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}>, void ()>::initiate<boost::asio::io_context::strand::initiate_dispatch, boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::ssl::detail::io_op<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::any_io_executor>, boost::asio::ssl::detail::shutdown_op, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running> >, boost::system::error_code, unsigned long>, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}>, boost::asio::io_context::strand*>(boost::asio::io_context::strand::initiate_dispatch&&, boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::ssl::detail::io_op<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::any_io_executor>, boost::asio::ssl::detail::shutdown_op, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running> >, boost::system::error_code, unsigned long>, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}>&&, boost::asio::io_context::strand*&&) (token=..., initiation=...) at /usr/include/boost/asio/async_result.hpp:482
#31 boost::asio::async_initiate<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::ssl::detail::io_op<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::any_io_executor>, boost::asio::ssl::detail::shutdown_op, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running> >, boost::system::error_code, unsigned long>, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}>, void (), boost::asio::io_context::strand::initiate_dispatch, boost::asio::io_context::strand*>(boost::asio::io_context::strand::initiate_dispatch&&, boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::ssl::detail::io_op<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::any_io_executor>, boost::asio::ssl::detail::shutdown_op, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running> >, boost::system::error_code, unsigned long>, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}>&, boost::asio::io_context::strand*&&) (token=..., initiation=...) at /usr/include/boost/asio/async_result.hpp:896
#32 boost::asio::io_context::strand::dispatch<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::ssl::detail::io_op<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::any_io_executor>, boost::asio::ssl::detail::shutdown_op, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running> >, boost::system::error_code, unsigned long>, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}> >(boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::ssl::detail::io_op<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::any_io_executor>, boost::asio::ssl::detail::shutdown_op, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running> >, boost::system::error_code, unsigned long>, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}>&&) (handler=..., this=0x7f399bffe5e0) at /usr/include/boost/asio/io_context_strand.hpp:199
#33 boost::asio::detail::asio_handler_invoke<boost::asio::detail::binder2<boost::asio::ssl::detail::io_op<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::any_io_executor>, boost::asio::ssl::detail::shutdown_op, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running> >, boost::system::error_code, unsigned long>, boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running>(boost::asio::detail::binder2<boost::asio::ssl::detail::io_op<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::any_io_executor>, boost::asio::ssl::detail::shutdown_op, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running> >, boost::system::error_code, unsigned long>&, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running>*) (this_handler=0x7f399bffe5e0, function=...) at /usr/include/boost/asio/detail/wrapped_handler.hpp:243
#34 boost_asio_handler_invoke_helpers::invoke<boost::asio::detail::binder2<boost::asio::ssl::detail::io_op<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::any_io_executor>, boost::asio::ssl::detail::shutdown_op, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running> >, boost::system::error_code, unsigned long>, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running> >(boost::asio::detail::binder2<boost::asio::ssl::detail::io_op<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::any_io_executor>, boost::asio::ssl::detail::shutdown_op, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running> >, boost::system::error_code, unsigned long>&, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running>&) (context=..., function=...) at /usr/include/boost/asio/detail/handler_invoke_helpers.hpp:54
#35 boost::asio::ssl::detail::asio_handler_invoke<boost::asio::detail::binder2<boost::asio::ssl::detail::io_op<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::any_io_executor>, boost::asio::ssl::detail::shutdown_op, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running> >, boost::system::error_code, unsigned long>, boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::any_io_executor>, boost::asio::ssl::detail::shutdown_op, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running> >(boost::asio::detail::binder2<boost::asio::ssl::detail::io_op<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::any_io_executor>, boost::asio::ssl::detail::shutdown_op, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running> >, boost::system::error_code, unsigned long>&, boost::asio::ssl::detail::io_op<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::any_io_executor>, boost::asio::ssl::detail::shutdown_op, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running> >*) (this_handler=0x7f399bffe5a0, function=...) at /usr/include/boost/asio/ssl/detail/io.hpp:374
#36 boost_asio_handler_invoke_helpers::invoke<boost::asio::detail::binder2<boost::asio::ssl::detail::io_op<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::any_io_executor>, boost::asio::ssl::detail::shutdown_op, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running> >, boost::system::error_code, unsigned long>, boost::asio::ssl::detail::io_op<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::any_io_executor>, boost::asio::ssl::detail::shutdown_op, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running> > >(boost::asio::detail::binder2<boost::asio::ssl::detail::io_op<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::any_io_executor>, boost::asio::ssl::detail::shutdown_op, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running> >, boost::system::error_code, unsigned long>&, boost::asio::ssl::detail::io_op<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::any_io_executor>, boost::asio::ssl::detail::shutdown_op, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running> >&) (context=..., function=...) at /usr/include/boost/asio/detail/handler_invoke_helpers.hpp:54
#37 boost::asio::detail::handler_work<boost::asio::ssl::detail::io_op<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::any_io_executor>, boost::asio::ssl::detail::shutdown_op, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running> >, boost::asio::any_io_executor, void>::complete<boost::asio::detail::binder2<boost::asio::ssl::detail::io_op<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::any_io_executor>, boost::asio::ssl::detail::shutdown_op, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running> >, boost::system::error_code, unsigned long> >(boost::asio::detail::binder2<boost::asio::ssl::detail::io_op<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::any_io_executor>, boost::asio::ssl::detail::shutdown_op, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running> >, boost::system::error_code, unsigned long>&, boost::asio::ssl::detail::io_op<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::any_io_executor>, boost::asio::ssl::detail::shutdown_op, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running> >&) (handler=..., function=..., this=0x7f399bffe520) at /usr/include/boost/asio/detail/handler_work.hpp:512
#38 boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::ssl::detail::io_op<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::any_io_executor>, boost::asio::ssl::detail::shutdown_op, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()::{lambda(boost::system::error_code const&)#1}, boost::asio::detail::is_continuation_if_running> >, boost::asio::any_io_executor>::do_complete(void*, boost::asio::detail::scheduler_operation*, boost::system::error_code const&, unsigned long) (owner=0x555e710e9dd0, base=0x7f3990059850) at /usr/include/boost/asio/detail/reactive_socket_recv_op.hpp:147
#39 0x0000555e6f1520ca in boost::asio::detail::scheduler_operation::complete (bytes_transferred=<optimized out>, ec=..., owner=0x555e710e9dd0, this=0x7f3990059850) at /usr/include/boost/asio/detail/scheduler_operation.hpp:40
#40 boost::asio::detail::scheduler::do_run_one (this=this@entry=0x555e710e9dd0, lock=..., this_thread=..., ec=...) at /usr/include/boost/asio/detail/impl/scheduler.ipp:492
#41 0x0000555e6f12f492 in boost::asio::detail::scheduler::run (this=0x555e710e9dd0, ec=...) at /usr/include/boost/asio/detail/impl/scheduler.ipp:210
#42 0x0000555e6f1624ab in boost::asio::io_context::run (this=<optimized out>) at /usr/include/boost/asio/impl/io_context.ipp:63
#43 epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::worker_thread (this=0x555e710e5f88) at /usr/src/debug/monero/monero/contrib/epee/include/net/abstract_tcp_server2.inl:1320
#44 0x00007f628aa7acbb in ?? () from /usr/lib/libboost_thread.so.1.80.0
#45 0x00007f628a5768fd in ?? () from /usr/lib/libc.so.6
#46 0x00007f628a5f8a60 in ?? () from /usr/lib/libc.so.6

Thread 15 (Thread 0x7f39b88556c0 (LWP 41147) "monerod"):
#0  0x00007f628a5734b6 in ?? () from /usr/lib/libc.so.6
#1  0x00007f628a575fd4 in pthread_cond_timedwait () from /usr/lib/libc.so.6
#2  0x00007f628b069aef in boost::posix::pthread_cond_timedwait (t=0x7f39b8854a20, m=0x7f39b8854af0, c=0x7f39b8854b18) at /usr/include/boost/thread/pthread/pthread_helpers.hpp:123
#3  boost::condition_variable::do_wait_until (timeout=..., m=..., this=0x7f39b8854af0) at /usr/include/boost/thread/pthread/condition_variable.hpp:122
#4  boost::condition_variable::timed_wait<bool (*)()> (pred=<optimized out>, abs_time=..., m=..., this=0x7f39b8854af0) at /usr/include/boost/thread/pthread/condition_variable_fwd.hpp:179
#5  boost::this_thread::sleep (abs_time=...) at /usr/include/boost/thread/pthread/thread_data.hpp:271
#6  epee::misc_utils::sleep_no_w (ms=ms@entry=100) at /usr/src/debug/monero/monero/contrib/epee/src/misc_language.cpp:37
#7  0x0000555e6f12c11b in operator() (__closure=0x555e710ffe78) at /usr/src/debug/monero/monero/src/daemon/daemon.cpp:181
#8  boost::detail::thread_data<daemonize::t_daemon::run(bool)::<lambda()> >::run(void) (this=0x555e710ffd40) at /usr/include/boost/thread/detail/thread.hpp:120
#9  0x00007f628aa7acbb in ?? () from /usr/lib/libboost_thread.so.1.80.0
#10 0x00007f628a5768fd in ?? () from /usr/lib/libc.so.6
#11 0x00007f628a5f8a60 in ?? () from /usr/lib/libc.so.6

Thread 14 (Thread 0x7f39b8d566c0 (LWP 41145) "monerod"):
#0  0x00007f628a5734b6 in ?? () from /usr/lib/libc.so.6
#1  0x00007f628a575cd0 in pthread_cond_wait () from /usr/lib/libc.so.6
#2  0x0000555e6f1255dc in boost::posix::pthread_cond_wait (m=<optimized out>, c=<optimized out>) at /usr/include/boost/thread/pthread/pthread_helpers.hpp:112
#3  boost::condition_variable::wait (this=0x7f628b2dfa30 <tools::threadpool::getInstanceForIO()::instance+80>, m=...) at /usr/include/boost/thread/pthread/condition_variable.hpp:79
#4  0x00007f628b20527e in tools::threadpool::run (this=0x7f628b2df9e0 <tools::threadpool::getInstanceForIO()::instance>, flush=false) at /usr/src/debug/monero/monero/src/common/threadpool.cpp:159
#5  0x00007f628aa7acbb in ?? () from /usr/lib/libboost_thread.so.1.80.0
#6  0x00007f628a5768fd in ?? () from /usr/lib/libc.so.6
#7  0x00007f628a5f8a60 in ?? () from /usr/lib/libc.so.6

Thread 13 (Thread 0x7f39b92576c0 (LWP 41144) "monerod"):
#0  0x00007f628a5734b6 in ?? () from /usr/lib/libc.so.6
#1  0x00007f628a575cd0 in pthread_cond_wait () from /usr/lib/libc.so.6
#2  0x0000555e6f1255dc in boost::posix::pthread_cond_wait (m=<optimized out>, c=<optimized out>) at /usr/include/boost/thread/pthread/pthread_helpers.hpp:112
#3  boost::condition_variable::wait (this=0x7f628b2dfa30 <tools::threadpool::getInstanceForIO()::instance+80>, m=...) at /usr/include/boost/thread/pthread/condition_variable.hpp:79
#4  0x00007f628b20527e in tools::threadpool::run (this=0x7f628b2df9e0 <tools::threadpool::getInstanceForIO()::instance>, flush=false) at /usr/src/debug/monero/monero/src/common/threadpool.cpp:159
#5  0x00007f628aa7acbb in ?? () from /usr/lib/libboost_thread.so.1.80.0
#6  0x00007f628a5768fd in ?? () from /usr/lib/libc.so.6
#7  0x00007f628a5f8a60 in ?? () from /usr/lib/libc.so.6

Thread 12 (Thread 0x7f39b97586c0 (LWP 41143) "monerod"):
#0  0x00007f628a5734b6 in ?? () from /usr/lib/libc.so.6
#1  0x00007f628a575cd0 in pthread_cond_wait () from /usr/lib/libc.so.6
#2  0x0000555e6f1255dc in boost::posix::pthread_cond_wait (m=<optimized out>, c=<optimized out>) at /usr/include/boost/thread/pthread/pthread_helpers.hpp:112
#3  boost::condition_variable::wait (this=0x7f628b2dfa30 <tools::threadpool::getInstanceForIO()::instance+80>, m=...) at /usr/include/boost/thread/pthread/condition_variable.hpp:79
#4  0x00007f628b20527e in tools::threadpool::run (this=0x7f628b2df9e0 <tools::threadpool::getInstanceForIO()::instance>, flush=false) at /usr/src/debug/monero/monero/src/common/threadpool.cpp:159
#5  0x00007f628aa7acbb in ?? () from /usr/lib/libboost_thread.so.1.80.0
#6  0x00007f628a5768fd in ?? () from /usr/lib/libc.so.6
#7  0x00007f628a5f8a60 in ?? () from /usr/lib/libc.so.6

Thread 11 (Thread 0x7f39b9c596c0 (LWP 41142) "monerod"):
#0  0x00007f628a5734b6 in ?? () from /usr/lib/libc.so.6
#1  0x00007f628a575cd0 in pthread_cond_wait () from /usr/lib/libc.so.6
#2  0x0000555e6f1255dc in boost::posix::pthread_cond_wait (m=<optimized out>, c=<optimized out>) at /usr/include/boost/thread/pthread/pthread_helpers.hpp:112
#3  boost::condition_variable::wait (this=0x7f628b2dfa30 <tools::threadpool::getInstanceForIO()::instance+80>, m=...) at /usr/include/boost/thread/pthread/condition_variable.hpp:79
#4  0x00007f628b20527e in tools::threadpool::run (this=0x7f628b2df9e0 <tools::threadpool::getInstanceForIO()::instance>, flush=false) at /usr/src/debug/monero/monero/src/common/threadpool.cpp:159
#5  0x00007f628aa7acbb in ?? () from /usr/lib/libboost_thread.so.1.80.0
#6  0x00007f628a5768fd in ?? () from /usr/lib/libc.so.6
#7  0x00007f628a5f8a60 in ?? () from /usr/lib/libc.so.6

Thread 10 (Thread 0x7f39ba15a6c0 (LWP 41141) "monerod"):
#0  0x00007f628a5734b6 in ?? () from /usr/lib/libc.so.6
#1  0x00007f628a575cd0 in pthread_cond_wait () from /usr/lib/libc.so.6
#2  0x0000555e6f1255dc in boost::posix::pthread_cond_wait (m=<optimized out>, c=<optimized out>) at /usr/include/boost/thread/pthread/pthread_helpers.hpp:112
#3  boost::condition_variable::wait (this=0x7f628b2dfa30 <tools::threadpool::getInstanceForIO()::instance+80>, m=...) at /usr/include/boost/thread/pthread/condition_variable.hpp:79
#4  0x00007f628b20527e in tools::threadpool::run (this=0x7f628b2df9e0 <tools::threadpool::getInstanceForIO()::instance>, flush=false) at /usr/src/debug/monero/monero/src/common/threadpool.cpp:159
#5  0x00007f628aa7acbb in ?? () from /usr/lib/libboost_thread.so.1.80.0
#6  0x00007f628a5768fd in ?? () from /usr/lib/libc.so.6
#7  0x00007f628a5f8a60 in ?? () from /usr/lib/libc.so.6

Thread 9 (Thread 0x7f39ba65b6c0 (LWP 41140) "monerod"):
#0  0x00007f628a5734b6 in ?? () from /usr/lib/libc.so.6
#1  0x00007f628a575cd0 in pthread_cond_wait () from /usr/lib/libc.so.6
#2  0x0000555e6f1255dc in boost::posix::pthread_cond_wait (m=<optimized out>, c=<optimized out>) at /usr/include/boost/thread/pthread/pthread_helpers.hpp:112
#3  boost::condition_variable::wait (this=0x7f628b2dfa30 <tools::threadpool::getInstanceForIO()::instance+80>, m=...) at /usr/include/boost/thread/pthread/condition_variable.hpp:79
#4  0x00007f628b20527e in tools::threadpool::run (this=0x7f628b2df9e0 <tools::threadpool::getInstanceForIO()::instance>, flush=false) at /usr/src/debug/monero/monero/src/common/threadpool.cpp:159
#5  0x00007f628aa7acbb in ?? () from /usr/lib/libboost_thread.so.1.80.0
#6  0x00007f628a5768fd in ?? () from /usr/lib/libc.so.6
#7  0x00007f628a5f8a60 in ?? () from /usr/lib/libc.so.6

Thread 8 (Thread 0x7f39bab5c6c0 (LWP 41139) "monerod"):
#0  0x00007f628a5734b6 in ?? () from /usr/lib/libc.so.6
#1  0x00007f628a575cd0 in pthread_cond_wait () from /usr/lib/libc.so.6
#2  0x0000555e6f1255dc in boost::posix::pthread_cond_wait (m=<optimized out>, c=<optimized out>) at /usr/include/boost/thread/pthread/pthread_helpers.hpp:112
#3  boost::condition_variable::wait (this=0x7f628b2dfa30 <tools::threadpool::getInstanceForIO()::instance+80>, m=...) at /usr/include/boost/thread/pthread/condition_variable.hpp:79
#4  0x00007f628b20527e in tools::threadpool::run (this=0x7f628b2df9e0 <tools::threadpool::getInstanceForIO()::instance>, flush=false) at /usr/src/debug/monero/monero/src/common/threadpool.cpp:159
#5  0x00007f628aa7acbb in ?? () from /usr/lib/libboost_thread.so.1.80.0
#6  0x00007f628a5768fd in ?? () from /usr/lib/libc.so.6
#7  0x00007f628a5f8a60 in ?? () from /usr/lib/libc.so.6

Thread 7 (Thread 0x7f39bb05d6c0 (LWP 41138) "monerod"):
#0  0x00007f628a5734b6 in ?? () from /usr/lib/libc.so.6
#1  0x00007f628a575cd0 in pthread_cond_wait () from /usr/lib/libc.so.6
#2  0x0000555e6f1255dc in boost::posix::pthread_cond_wait (m=<optimized out>, c=<optimized out>) at /usr/include/boost/thread/pthread/pthread_helpers.hpp:112
#3  boost::condition_variable::wait (this=0x7f628b780550 <tools::threadpool::getInstanceForCompute()::instance+80>, m=...) at /usr/include/boost/thread/pthread/condition_variable.hpp:79
#4  0x00007f628b20527e in tools::threadpool::run (this=0x7f628b780500 <tools::threadpool::getInstanceForCompute()::instance>, flush=false) at /usr/src/debug/monero/monero/src/common/threadpool.cpp:159
#5  0x00007f628aa7acbb in ?? () from /usr/lib/libboost_thread.so.1.80.0
#6  0x00007f628a5768fd in ?? () from /usr/lib/libc.so.6
#7  0x00007f628a5f8a60 in ?? () from /usr/lib/libc.so.6

Thread 6 (Thread 0x7f39bb55e6c0 (LWP 41137) "monerod"):
#0  0x00007f628a5734b6 in ?? () from /usr/lib/libc.so.6
#1  0x00007f628a575cd0 in pthread_cond_wait () from /usr/lib/libc.so.6
#2  0x0000555e6f1255dc in boost::posix::pthread_cond_wait (m=<optimized out>, c=<optimized out>) at /usr/include/boost/thread/pthread/pthread_helpers.hpp:112
#3  boost::condition_variable::wait (this=0x7f628b780550 <tools::threadpool::getInstanceForCompute()::instance+80>, m=...) at /usr/include/boost/thread/pthread/condition_variable.hpp:79
#4  0x00007f628b20527e in tools::threadpool::run (this=0x7f628b780500 <tools::threadpool::getInstanceForCompute()::instance>, flush=false) at /usr/src/debug/monero/monero/src/common/threadpool.cpp:159
#5  0x00007f628aa7acbb in ?? () from /usr/lib/libboost_thread.so.1.80.0
#6  0x00007f628a5768fd in ?? () from /usr/lib/libc.so.6
#7  0x00007f628a5f8a60 in ?? () from /usr/lib/libc.so.6

Thread 5 (Thread 0x7f39bba5f6c0 (LWP 41136) "monerod"):
#0  0x00007f628a5734b6 in ?? () from /usr/lib/libc.so.6
#1  0x00007f628a575cd0 in pthread_cond_wait () from /usr/lib/libc.so.6
#2  0x0000555e6f1255dc in boost::posix::pthread_cond_wait (m=<optimized out>, c=<optimized out>) at /usr/include/boost/thread/pthread/pthread_helpers.hpp:112
#3  boost::condition_variable::wait (this=0x7f628b780550 <tools::threadpool::getInstanceForCompute()::instance+80>, m=...) at /usr/include/boost/thread/pthread/condition_variable.hpp:79
#4  0x00007f628b20527e in tools::threadpool::run (this=0x7f628b780500 <tools::threadpool::getInstanceForCompute()::instance>, flush=false) at /usr/src/debug/monero/monero/src/common/threadpool.cpp:159
#5  0x00007f628aa7acbb in ?? () from /usr/lib/libboost_thread.so.1.80.0
#6  0x00007f628a5768fd in ?? () from /usr/lib/libc.so.6
#7  0x00007f628a5f8a60 in ?? () from /usr/lib/libc.so.6

Thread 4 (Thread 0x7f39bbf606c0 (LWP 41135) "monerod"):
#0  0x00007f628a5734b6 in ?? () from /usr/lib/libc.so.6
#1  0x00007f628a575cd0 in pthread_cond_wait () from /usr/lib/libc.so.6
#2  0x0000555e6f1255dc in boost::posix::pthread_cond_wait (m=<optimized out>, c=<optimized out>) at /usr/include/boost/thread/pthread/pthread_helpers.hpp:112
#3  boost::condition_variable::wait (this=0x7f628b780550 <tools::threadpool::getInstanceForCompute()::instance+80>, m=...) at /usr/include/boost/thread/pthread/condition_variable.hpp:79
#4  0x00007f628b20527e in tools::threadpool::run (this=0x7f628b780500 <tools::threadpool::getInstanceForCompute()::instance>, flush=false) at /usr/src/debug/monero/monero/src/common/threadpool.cpp:159
#5  0x00007f628aa7acbb in ?? () from /usr/lib/libboost_thread.so.1.80.0
#6  0x00007f628a5768fd in ?? () from /usr/lib/libc.so.6
#7  0x00007f628a5f8a60 in ?? () from /usr/lib/libc.so.6

Thread 3 (Thread 0x7f39bc4616c0 (LWP 41134) "monerod"):
#0  0x00007f628a5734b6 in ?? () from /usr/lib/libc.so.6
#1  0x00007f628a575cd0 in pthread_cond_wait () from /usr/lib/libc.so.6
#2  0x0000555e6f1255dc in boost::posix::pthread_cond_wait (m=<optimized out>, c=<optimized out>) at /usr/include/boost/thread/pthread/pthread_helpers.hpp:112
#3  boost::condition_variable::wait (this=0x7f628b780550 <tools::threadpool::getInstanceForCompute()::instance+80>, m=...) at /usr/include/boost/thread/pthread/condition_variable.hpp:79
#4  0x00007f628b20527e in tools::threadpool::run (this=0x7f628b780500 <tools::threadpool::getInstanceForCompute()::instance>, flush=false) at /usr/src/debug/monero/monero/src/common/threadpool.cpp:159
#5  0x00007f628aa7acbb in ?? () from /usr/lib/libboost_thread.so.1.80.0
#6  0x00007f628a5768fd in ?? () from /usr/lib/libc.so.6
#7  0x00007f628a5f8a60 in ?? () from /usr/lib/libc.so.6

Thread 2 (Thread 0x7f39bcc626c0 (LWP 41133) "monerod"):
#0  0x00007f628a5734b6 in ?? () from /usr/lib/libc.so.6
#1  0x00007f628a575cd0 in pthread_cond_wait () from /usr/lib/libc.so.6
#2  0x0000555e6f151f7c in boost::asio::detail::posix_event::wait<boost::asio::detail::conditionally_enabled_mutex::scoped_lock> (lock=..., this=0x555e70c737c0) at /usr/include/boost/asio/detail/conditionally_enabled_mutex.hpp:98
#3  boost::asio::detail::conditionally_enabled_event::wait (lock=..., this=0x555e70c737b8) at /usr/include/boost/asio/detail/conditionally_enabled_event.hpp:97
#4  boost::asio::detail::scheduler::do_run_one (this=0x555e70c73750, lock=..., this_thread=..., ec=...) at /usr/include/boost/asio/detail/impl/scheduler.ipp:501
#5  0x00007f628b6c9c7a in boost::asio::detail::scheduler::run (this=0x555e70c73750, ec=...) at /usr/include/boost/asio/detail/impl/scheduler.ipp:210
#6  0x00007f628b6cc2fe in boost::asio::io_context::run (this=<optimized out>) at /usr/include/boost/asio/impl/io_context.ipp:63
#7  0x00007f628aa7acbb in ?? () from /usr/lib/libboost_thread.so.1.80.0
#8  0x00007f628a5768fd in ?? () from /usr/lib/libc.so.6
#9  0x00007f628a5f8a60 in ?? () from /usr/lib/libc.so.6

Thread 1 (Thread 0x7f6289da3a40 (LWP 41132) "monerod"):
#0  0x00007f628a5734b6 in ?? () from /usr/lib/libc.so.6
#1  0x00007f628a575cd0 in pthread_cond_wait () from /usr/lib/libc.so.6
#2  0x00007f628aa79fc4 in ?? () from /usr/lib/libboost_thread.so.1.80.0
#3  0x00007f628aa7a15c in boost::thread::join_noexcept() () from /usr/lib/libboost_thread.so.1.80.0
#4  0x00007f628bdd57a6 in boost::thread::join (this=0x555e710e8e00) at /usr/include/boost/thread/detail/thread.hpp:762
#5  epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::run_server (this=this@entry=0x555e710639d0, threads_count=threads_count@entry=10, wait=wait@entry=true, attrs=...) at /usr/src/debug/monero/monero/contrib/epee/include/net/abstract_tcp_server2.inl:1379
#6  0x00007f628bdd70f0 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::run (this=this@entry=0x555e70c82a50) at /usr/src/debug/monero/monero/src/p2p/net_node.inl:1048
#7  0x0000555e6f153ea0 in daemonize::t_p2p::run (this=0x555e70c82a50) at /usr/src/debug/monero/monero/src/daemon/p2p.h:80
#8  0x0000555e6f13e699 in daemonize::t_daemon::run (this=this@entry=0x7ffcf9d61f50, interactive=interactive@entry=false) at /usr/include/c++/12.2.0/bits/unique_ptr.h:191
#9  0x0000555e6f1cad94 in daemonize::t_executor::run_non_interactive (this=this@entry=0x7ffcf9d62040, vm=...) at /usr/src/debug/monero/monero/src/daemon/executor.cpp:69
#10 0x0000555e6f10f145 in daemonizer::daemonize<daemonize::t_executor> (argc=<optimized out>, argv=<optimized out>, vm=..., executor=...) at /usr/src/debug/monero/monero/src/daemonizer/posix_daemonizer.inl:99
#11 daemonizer::daemonize<daemonize::t_executor> (argc=<optimized out>, argv=<optimized out>, vm=..., executor=...) at /usr/src/debug/monero/monero/src/daemonizer/posix_daemonizer.inl:79
#12 main (argc=<optimized out>, argv=<optimized out>) at /usr/src/debug/monero/monero/src/daemon/main.cpp:360
```

thread 16 and 17 use 80% CPU each

any other wishes? froze the process with gdb.

## moneromooo-monero | 2023-01-02T15:46:25+00:00
At a guess, start_shutdown and on_interrupt might be called ping pong fast. You can check by adding something like:
```
 MGINFO(__FUNC__);
```
at the start of both, and see whether you can a spam of those when the CPU spike happens.

If it does, then something in the logic of that code is likely buggy. If not, the issue is probably elsewhere.

## BotoX | 2023-01-07T15:46:21+00:00
recompiled with:
```diff
diff --git a/contrib/epee/include/net/abstract_tcp_server2.inl b/contrib/epee/include/net/abstract_tcp_server2.inl
index 81aa725d1..90d2e59f7 100644
--- a/contrib/epee/include/net/abstract_tcp_server2.inl
+++ b/contrib/epee/include/net/abstract_tcp_server2.inl
@@ -559,6 +559,7 @@ namespace net_utils
   template<typename T>
   void connection<T>::start_shutdown()
   {
+    MGINFO(__func__);
     if (m_state.socket.wait_shutdown)
       return;
     auto self = connection<T>::shared_from_this();
@@ -661,6 +662,7 @@ namespace net_utils
   template<typename T>
   void connection<T>::on_interrupted()
   {
+    MGINFO(__func__);
     assert(m_state.status == status_t::INTERRUPTED);
     if (m_state.timers.general.wait_expire)
       return;
```


## BotoX | 2023-01-12T19:05:42+00:00
Update: @moneromooo-monero was right.

My log file is 66 GB big and getting spammed with this crap:

```
2023-01-12 19:01:35.442 [RPC1]  INFO    global  contrib/epee/include/net/abstract_tcp_server2.inl:562 start_shutdown
2023-01-12 19:01:35.442 [RPC0]  INFO    global  contrib/epee/include/net/abstract_tcp_server2.inl:665 on_interrupted
2023-01-12 19:01:35.442 [RPC0]  INFO    global  contrib/epee/include/net/abstract_tcp_server2.inl:665 on_interrupted
2023-01-12 19:01:35.442 [RPC0]  INFO    global  contrib/epee/include/net/abstract_tcp_server2.inl:665 on_interrupted
2023-01-12 19:01:35.442 [RPC0]  INFO    global  contrib/epee/include/net/abstract_tcp_server2.inl:665 on_interrupted
2023-01-12 19:01:35.442 [RPC0]  INFO    global  contrib/epee/include/net/abstract_tcp_server2.inl:562 start_shutdown
2023-01-12 19:01:35.442 [RPC1]  INFO    global  contrib/epee/include/net/abstract_tcp_server2.inl:665 on_interrupted
2023-01-12 19:01:35.442 [RPC1]  INFO    global  contrib/epee/include/net/abstract_tcp_server2.inl:562 start_shutdown
2023-01-12 19:01:35.443 [RPC0]  INFO    global  contrib/epee/include/net/abstract_tcp_server2.inl:665 on_interrupted
2023-01-12 19:01:35.443 [RPC0]  INFO    global  contrib/epee/include/net/abstract_tcp_server2.inl:562 start_shutdown
2023-01-12 19:01:35.443 [RPC1]  INFO    global  contrib/epee/include/net/abstract_tcp_server2.inl:665 on_interrupted
2023-01-12 19:01:35.443 [RPC0]  INFO    global  contrib/epee/include/net/abstract_tcp_server2.inl:665 on_interrupted
2023-01-12 19:01:35.443 [RPC1]  INFO    global  contrib/epee/include/net/abstract_tcp_server2.inl:665 on_interrupted
2023-01-12 19:01:35.443 [RPC0]  INFO    global  contrib/epee/include/net/abstract_tcp_server2.inl:665 on_interrupted
2023-01-12 19:01:35.443 [RPC0]  INFO    global  contrib/epee/include/net/abstract_tcp_server2.inl:562 start_shutdown
```

https://asciinema.org/a/Rtso2l9aZceB8lBFDzn81qJF3

I froze the monero process again, if you want me to poke around with gdb or post a core dump.

## moneromooo-monero | 2023-01-12T20:50:01+00:00
An all thread stack trace would be nice in this state:

thread apply all bt full

## moneromooo-monero | 2023-01-12T20:52:30+00:00
Actually, better even:

"break epee::net_utils::connection" TAB TAB , etc, etc, till you complete to on_interrupted
Same with start_shutdown

Now cont till it breaks in either. Then "thread apply all bt full".
Then cont till it breaks in the other one. Then "thread apply all bt full".

That way we see where the calls from those some from. Possibly from a boost async scheduled call, but you never know.

## BotoX | 2023-01-12T21:42:33+00:00
> An all thread stack trace would be nice in this state:
> 
> thread apply all bt full

[thread apply all bt full.txt](https://github.com/monero-project/monero/files/10406051/thread.apply.all.bt.full.txt)



> Actually, better even:
> 
> "break epee::net_utils::connection" TAB TAB , etc, etc, till you complete to on_interrupted Same with start_shutdown

There is:

```
epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::on_interrupted()
epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::on_interrupted()
```

and

```
epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::start_shutdown()
epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()
```

Starting with the HTTP ones:
```
(gdb) break epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::on_interrupted()
Breakpoint 3 at 0x55df84b67650: epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::on_interrupted(). (2 locations)
(gdb) break epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown()
Breakpoint 4 at 0x55df84b672e0: epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::start_shutdown(). (2 locations)
```

doing continue and holding down enter blocks on every log line:
[1.txt](https://github.com/monero-project/monero/files/10406111/1.txt)


Next one:
```
(gdb) break epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::on_interrupted()
Breakpoint 11 at 0x55df84b729e0: epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::on_interrupted(). (2 locations)
(gdb) break epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::start_shutdown()
Breakpoint 12 at 0x55df84b72580: epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::start_shutdown(). (2 locations)
```

[2.txt](https://github.com/monero-project/monero/files/10406119/2.txt)
barely anything and then just keeps on running for a minute (and spamming the log) until I ^C it.
so it's the HTTP one it seems


And now a few "continue" + "bt full" with the http breakpoints:
[3.txt](https://github.com/monero-project/monero/files/10406137/3.txt)


Here's a on_shutdown "thread apply all bt full":
[4.txt](https://github.com/monero-project/monero/files/10406153/4.txt)

Finally a on_interrupted "thread apply all bt full":
[5.txt](https://github.com/monero-project/monero/files/10406172/5.txt)

Also uploading the monerod binary + build directory (for libraries, is this because I did a debug build?) + core dump:
https://cloud.botox.bz/s/2KHwq6Ha8p4QWDb



## moneromooo-monero | 2023-01-12T22:08:10+00:00
This might work, though I do not know the semantics of this code, so even if it works it's not certain to be a good fix.
It basically prevents calling shutdown while a shutdown is in progress. I don't think the author of this code is around anymore to give an opinion on the patch (or make a better fix) though.

```
diff --git a/contrib/epee/include/net/abstract_tcp_server2.inl b/contrib/epee/include/net/abstract_tcp_server2.inl
index 81aa725d1..333a1144e 100644
--- a/contrib/epee/include/net/abstract_tcp_server2.inl
+++ b/contrib/epee/include/net/abstract_tcp_server2.inl
@@ -565,7 +565,7 @@ namespace net_utils
     m_state.socket.wait_shutdown = true;
     auto on_shutdown = [this, self](const ec_t &ec){
       std::lock_guard<std::mutex> guard(m_state.lock);
-      m_state.socket.wait_shutdown = false;
+      epee::misc_utils::auto_scope_leave_caller scope_exit_handler = epee::misc_utils::create_scope_leave_handler([&](){ m_state.socket.wait_shutdown = false; });
       if (m_state.socket.cancel_shutdown) {
         m_state.socket.cancel_shutdown = false;
         switch (m_state.status)
```

## j-berman | 2023-01-19T09:14:34+00:00
Taking a stab at this... from what I recall in discussions with the author, their intent behind the connection's interrupted status was to allow the server to reuse a connection that hasn't been terminated yet. But the author didn't actually implement the code to reuse an interrupted connection (I don't see a way for a connection's status to go from `INTERRUPTED` to anything but `TERMINATING` or `WASTED`). I believe they intended to implement the ability to reuse the underlying TCP connection *in a future PR* building off this interrupted status.

In this `on_interrupted` -> `start_shutdown` infinite ping pong (good spot @moneromooo-monero), it looks like the server just keeps attempting to re-shut the SSL stream down, while leaving the connection in an interrupted state (and leaving the underlying TCP connection alone). I'm thinking until someone actually writes the code to reuse an "interrupted" connection, it makes sense to simply complete the connection termination sequence (and shut down the TCP connection) *after* the server shuts the SSL stream down. This way the server isn't leaving a connection around in this interrupted state that can't be "un-interrupted."

This would be my proposed patch:

```
diff --git a/contrib/epee/include/net/abstract_tcp_server2.inl b/contrib/epee/include/net/abstract_tcp_server2.inl
index 81aa725d1..fb935a9cb 100644
--- a/contrib/epee/include/net/abstract_tcp_server2.inl
+++ b/contrib/epee/include/net/abstract_tcp_server2.inl
@@ -586,8 +586,7 @@ namespace net_utils
       else if (ec.value())
         terminate();
       else {
-        cancel_timer();
-        on_interrupted();
+        terminate();
       }
     };
     m_strand.post(
```

This is a blunt stab of a solution on my end. After some attempts, I still haven't figured out how to repro this bug on my machine, but I think this makes a bit more sense as a patch since it doesn't leave the connection in an interrupted state forever (with the timer that would terminate the TCP connection on expiry canceled forever too).

## BotoX | 2023-01-20T19:16:50+00:00
Seems like the proposed fix from @moneromooo-monero didn't work, cpu load at 200% now after a few days :D
![image](https://user-images.githubusercontent.com/395711/213784712-cfd09fd2-c5bb-4cc2-aa32-4660daa8cd7c.png)

I've just compiled and deployed the patch proposed by @j-berman


## BotoX | 2023-01-27T17:32:20+00:00
It's been a week and my CPU is not on fire. 👍
![image](https://user-images.githubusercontent.com/395711/215154780-51d8f146-dd8a-4bcf-86ce-2b88513e3c86.png)


## jkhsjdhjs | 2023-02-02T11:40:02+00:00
Works for me as well!
![cpu usage graph](https://screens.totally.rip/2023/02/63db9f1bbddca.png)

But since this was an issue with the handling of interrupted connections, I do wonder why it was only present in the binaries compiled by distributions or by myself, but not in the official binaries published on https://www.getmonero.org.

## hajes | 2023-03-08T15:05:55+00:00
been there, disable public RPC node. it uses extra 10Wh and hogs CPU.

i used to have no issues for weeks, then it started without reason. restart monerod...it works...sometimes repeat itself..

i use only local RPC node for my wallet...works flawlressly so far

## g00g1 | 2023-04-23T10:34:30+00:00
I don't observe high cpu usage anymore after applying the suggested patch, can confirm that after monitoring for almost a week.

![image](https://user-images.githubusercontent.com/91201021/233834614-5b1ecfe8-caae-4269-8f35-20129fba3d9a.png)

# Action History
- Created by: BotoX | 2022-12-21T20:36:22+00:00
- Closed at: 2023-06-27T16:29:04+00:00
