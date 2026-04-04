---
title: Stopping daemon hangs/crashes
source_url: https://github.com/monero-project/monero/issues/264
author: arnuschky
assignees: []
labels: []
created_at: '2015-04-12T15:06:09+00:00'
updated_at: '2016-07-20T00:50:23+00:00'
type: issue
status: closed
closed_at: '2016-01-25T18:11:09+00:00'
---

# Original Description
Stopping the daemon via CTRL-C seems to initiate shutdown sequence, but hangs after a a while. Pressing CTRL-C again kills/crashes daemon:

```
^C2015-Apr-12 15:08:23.597921 [SRV_MAIN][node] Stop signal sent
2015-Apr-12 15:08:23.598184 [SRV_MAIN]Stopping core rpc server...
2015-Apr-12 15:08:23.598287 [SRV_MAIN]Deinitializing rpc server...
2015-Apr-12 15:08:23.598358 [SRV_MAIN]Deinitializing p2p...
2015-Apr-12 15:08:31.886116 [SRV_MAIN]Deinitializing core...
2015-Apr-12 15:08:31.886188 [SRV_MAIN]Mining has been stopped, 0 finished
2015-Apr-12 15:08:31.990331 [SRV_MAIN]Mining has been stopped, 0 finished
2015-Apr-12 15:08:31.990407 [SRV_MAIN]Deinitializing cryptonote_protocol...

^Cterminate called after throwing an instance of 'std::runtime_error'
  what():  Can't stop stopped daemon
[1]    16793 abort      ./bitmonerod
```


# Discussion History
## arnuschky | 2015-04-12T15:58:25+00:00
Another one:

```
2015-Apr-12 17:57:43.620677 [SRV_MAIN]Deinitializing core...
2015-Apr-12 17:57:43.620955 [SRV_MAIN]Mining has been stopped, 0 finished
2015-Apr-12 17:57:43.746504 [SRV_MAIN]Mining has been stopped, 0 finished
2015-Apr-12 17:57:43.757285 [SRV_MAIN]Deinitializing cryptonote_protocol...
terminate called after throwing an instance of 'boost::exception_detail::clone_impl<boost::exception_detail::error_info_injector<boost::lock_error> >'
  what():  boost: mutex lock failed in pthread_mutex_lock: Invalid argument
```


## arnuschky | 2015-04-13T19:34:31+00:00
Another similar one:

```
2015-Apr-13 21:33:10.071900 [SRV_MAIN]Deinitializing rpc server...
2015-Apr-13 21:33:10.072427 [SRV_MAIN]Deinitializing p2p...
2015-Apr-13 21:33:13.545315 [SRV_MAIN]Deinitializing core...
2015-Apr-13 21:33:13.545614 [SRV_MAIN]Mining has been stopped, 0 finished
2015-Apr-13 21:33:13.569789 [SRV_MAIN]Mining has been stopped, 0 finished
2015-Apr-13 21:33:13.570160 [SRV_MAIN]Deinitializing cryptonote_protocol...
bitmonerod: ../nptl/pthread_mutex_lock.c:350: __pthread_mutex_lock_full: Assertion `(-(e)) != 3 || !robust' failed.
```


## chocolatebarxmr | 2015-07-18T16:42:47+00:00
On Ubuntu 15.04, I'm experiencing this issue as well on a build of the newest git code as of today. 

Ctrl+c to exit the terminal:

2015-Jul-18 11:57:04.970245 [P2P4]Blockchain stored OK, took: 11 ms
2015-Jul-18 11:57:37.248617 [P2P9]HASH: + VIN/VOUT: 4/5 H: 656410 chcktx: 10
^C2015-Jul-18 11:58:14.773372 [SRV_MAIN][node] Stop signal sent
2015-Jul-18 11:58:14.773676 [SRV_MAIN]Stopping core rpc server...
2015-Jul-18 11:58:14.774034 [SRV_MAIN]Deinitializing rpc server...
2015-Jul-18 11:58:14.775047 [SRV_MAIN]Deinitializing p2p...
2015-Jul-18 11:58:15.690555 [SRV_MAIN]Deinitializing core...
2015-Jul-18 11:58:15.690830 [SRV_MAIN]Mining has been stopped, 0 finished
2015-Jul-18 11:58:15.692087 [SRV_MAIN]Closing IO Service.
2015-Jul-18 11:58:15.704310 [SRV_MAIN]Mining has been stopped, 0 finished
2015-Jul-18 11:58:15.704562 [SRV_MAIN]Deinitializing cryptonote_protocol...

...and hangs there indefinitely. Ctrl+c again results in:

^Cterminate called after throwing an instance of 'std::runtime_error'
  what():  Can't stop stopped daemon
Aborted (core dumped)

I'm new to this bug reporting stuff so let me know if there's a way I can provide better information.


## warptangent | 2015-07-18T18:29:21+00:00
Try typing exit to initiate a clean exit. Ctrl-D should behave similarly. Ctrl-C is different and may not have well-defined behavior here.


## otila | 2015-09-28T10:43:15+00:00
"exit" does not have nice behavior... have to kill -9 .
git master 1e7fc9c0

```
Thread 9 (Thread 0x7f56df7c9700 (LWP 11526)):
#0  0x00007f56e59efc7d in nanosleep () at ../sysdeps/unix/syscall-template.S:81
#1  0x000000000081d652 in epee::net_utils::data_logger::data_logger()::{lambda()#1}::operator()() const [clone .constprop.105] ()
#2  0x00007f56e61d4350 in std::(anonymous namespace)::execute_native_thread_routine (__p=<optimized out>) at ../../../../../libstdc++-v3/src/c++11/thread.cc:84
#3  0x00007f56e59e7555 in start_thread (arg=0x7f56df7c9700) at pthread_create.c:333
#4  0x00007f56e5722b9d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109
Thread 8 (Thread 0x7f56dffca700 (LWP 11527)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x0000000000768e30 in boost::asio::detail::task_io_service::run(boost::system::error_code&) ()
#2  0x000000000076a016 in boost::asio::io_service::run() ()
#3  0x00007f56e71f4585 in thread_proxy () from /lib64/libboost_thread.so.1.57.0
#4  0x00007f56e59e7555 in start_thread (arg=0x7f56dffca700) at pthread_create.c:333
#5  0x00007f56e5722b9d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109
Thread 7 (Thread 0x7f56e07cb700 (LWP 11528)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x00000000006821bc in epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::worker_thread() ()
#2  0x00007f56e71f4585 in thread_proxy () from /lib64/libboost_thread.so.1.57.0
#3  0x00007f56e59e7555 in start_thread (arg=0x7f56e07cb700) at pthread_create.c:333
#4  0x00007f56e5722b9d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109
Thread 6 (Thread 0x7f56e0fcc700 (LWP 11529)):
#0  0x00007f56e5723193 in epoll_wait () at ../sysdeps/unix/syscall-template.S:81
#1  0x0000000000681e13 in epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::worker_thread() ()
#2  0x00007f56e71f4585 in thread_proxy () from /lib64/libboost_thread.so.1.57.0
#3  0x00007f56e59e7555 in start_thread (arg=0x7f56e0fcc700) at pthread_create.c:333
#4  0x00007f56e5722b9d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109
Thread 5 (Thread 0x7f56decc6700 (LWP 11530)):
#0  0x00007f56e5719063 in select () at ../sysdeps/unix/syscall-template.S:81
#1  0x0000000000568eaa in epee::async_stdin_reader::reader_thread_func() ()
#2  0x00007f56e61d4350 in std::(anonymous namespace)::execute_native_thread_routine (__p=<optimized out>) at ../../../../../libstdc++-v3/src/c++11/thread.cc:84
#3  0x00007f56e59e7555 in start_thread (arg=0x7f56decc6700) at pthread_create.c:333
#4  0x00007f56e5722b9d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109
Thread 4 (Thread 0x7f56de4c5700 (LWP 11531)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x00007f56e61ceefc in __gthread_cond_wait (__mutex=<optimized out>, __cond=<optimized out>) at /usr/src/debug/gcc-5.2.1-20150902/obj-x86_64-redhat-linux/x86_64-redhat-linux/libstdc++-v3/include/x86_64-redhat-linux/bits/gthr-default.h:864
#2  std::condition_variable::wait (this=<optimized out>, __lock=...) at ../../../../../libstdc++-v3/src/c++11/condition_variable.cc:53
#3  0x000000000056c4a0 in bool epee::async_console_handler::run<bool epee::async_console_handler::run<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::string const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > > >(boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::string const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > >, std::string const&, std::string const&, std::function<void ()>)::{lambda(std::string const&)#1}>(std::string const&, std::string const&, bool epee::async_console_handler::run<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::string const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > > >(boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::string const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > >, std::string const&, std::string const&, std::function<void ()>)::{lambda(std::string const&)#1} const&, std::function<void ()>) ()
#4  0x000000000056cd59 in epee::console_handlers_binder::run_handling(std::string const&, std::string const&, std::function<void ()>) ()
#5  0x00000000005684d6 in boost::detail::thread_data<boost::_bi::bind_t<bool, boost::_mfi::mf3<bool, epee::console_handlers_binder, std::string const&, std::string const&, std::function<void ()> >, boost::_bi::list4<boost::_bi::value<epee::console_handlers_binder*>, boost::_bi::value<std::string>, boost::_bi::value<std::string>, boost::_bi::value<std::function<void ()> > > > >::run() ()
#6  0x00007f56e71f4585 in thread_proxy () from /lib64/libboost_thread.so.1.57.0
#7  0x00007f56e59e7555 in start_thread (arg=0x7f56de4c5700) at pthread_create.c:333
#8  0x00007f56e5722b9d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109
Thread 3 (Thread 0x7f56ddcc4700 (LWP 11532)):
#0  0x00007f56e59efc7d in nanosleep () at ../sysdeps/unix/syscall-template.S:81
#1  0x00000000006945fe in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::run()::{lambda()#1}::operator()() const ()
#2  0x00007f56e61d4350 in std::(anonymous namespace)::execute_native_thread_routine (__p=<optimized out>) at ../../../../../libstdc++-v3/src/c++11/thread.cc:84
#3  0x00007f56e59e7555 in start_thread (arg=0x7f56ddcc4700) at pthread_create.c:333
#4  0x00007f56e5722b9d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109
Thread 2 (Thread 0x7f56dcfc2700 (LWP 11534)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x00007f56e61ceefc in __gthread_cond_wait (__mutex=<optimized out>, __cond=<optimized out>) at /usr/src/debug/gcc-5.2.1-20150902/obj-x86_64-redhat-linux/x86_64-redhat-linux/libstdc++-v3/include/x86_64-redhat-linux/bits/gthr-default.h:864
#2  std::condition_variable::wait (this=<optimized out>, __lock=...) at ../../../../../libstdc++-v3/src/c++11/condition_variable.cc:53
#3  0x0000000000619b3f in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::do_handshake_with_peer(unsigned long&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool) ()
#4  0x00000000006dac33 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::try_to_connect_and_handshake_with_new_peer(nodetool::net_address const&, bool, unsigned long, bool) ()
#5  0x00000000006dc135 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::make_new_connection_from_peerlist(bool) ()
#6  0x00000000006e0009 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::make_expected_connections_count(bool, unsigned long) ()
#7  0x00000000006e051f in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::connections_maker() ()
#8  0x000000000057abe4 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::idle_worker() ()
#9  0x00000000005a068e in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::global_timer_handler(boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base>) ()
#10 0x000000000057f3ac in boost::asio::detail::wait_handler<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> > > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#11 0x000000000067ed2d in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#12 0x00007f56e71f4585 in thread_proxy () from /lib64/libboost_thread.so.1.57.0
#13 0x00007f56e59e7555 in start_thread (arg=0x7f56dcfc2700) at pthread_create.c:333
#14 0x00007f56e5722b9d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109
Thread 1 (Thread 0x7f56e8488840 (LWP 11518)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x00007f56e71f71db in boost::thread::join_noexcept() () from /lib64/libboost_thread.so.1.57.0
#2  0x0000000000671b91 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::run_server(unsigned long, bool, boost::thread_attributes const&) ()
#3  0x000000000067b34e in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::run() ()
#4  0x0000000000577d8e in daemonize::t_daemon::run(bool) ()
#5  0x00000000006e938b in daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) ()
#6  0x00000000006efe53 in bool daemonizer::daemonize<daemonize::t_executor>(int, char const**, daemonize::t_executor&&, boost::program_options::variables_map const&) ()
#7  0x000000000054d4c4 in main ()
```


## fluffypony | 2016-01-25T18:11:09+00:00
This should be fixed, please reopen if it occurs with 0.9.1 and above.


## freelion93 | 2016-07-20T00:50:23+00:00
get problem on debian 8.5


# Action History
- Created by: arnuschky | 2015-04-12T15:06:09+00:00
- Closed at: 2016-01-25T18:11:09+00:00
