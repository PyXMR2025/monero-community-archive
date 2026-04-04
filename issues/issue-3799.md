---
title: New (rare) crash in readline on exit
source_url: https://github.com/monero-project/monero/issues/3799
author: moneromooo-monero
assignees: []
labels: []
created_at: '2018-05-13T13:17:15+00:00'
updated_at: '2020-11-29T07:55:24+00:00'
type: issue
status: closed
closed_at: '2020-11-29T07:55:24+00:00'
---

# Original Description
Using recent master (plus other unrelated patches). This was a normal ^D exit. I got this only once in a lot of cases, so pretty much unreproducible.

```
(gdb) thread apply all bt

Thread 10 (Thread 0x7ccbca0fa700 (LWP 28826)):
#0  0x00007ccc4e06a480 in pthread_cond_wait@@GLIBC_2.3.2 () from /lib64/libpthread.so.0
#1  0x00007ccc50515f6e in boost::condition_variable::wait (m=..., this=0x7ccc51ce80f0 <tools::threadpool::getInstance()::instance+80>)
    at /home/user/boost_1_65_1_install/include/boost/thread/pthread/condition_variable.hpp:81
#2  tools::threadpool::run (this=0x7ccc51ce80a0 <tools::threadpool::getInstance()::instance>, flush=false)
    at /home/user/src/bitmonero/src/common/threadpool.cpp:136
#3  0x00007ccc50518c36 in boost::_mfi::mf1<void, tools::threadpool, bool>::operator() (a1=<optimized out>, p=<optimized out>, 
    this=<optimized out>) at /home/user/boost_1_65_1_install/include/boost/bind/mem_fn_template.hpp:165
#4  boost::_bi::list2<boost::_bi::value<tools::threadpool*>, boost::_bi::value<bool> >::operator()<boost::_mfi::mf1<void, tools::threadpool, bool>, boost::_bi::list0> (a=<synthetic pointer>..., f=..., this=<optimized out>)
    at /home/user/boost_1_65_1_install/include/boost/bind/bind.hpp:319
#5  boost::_bi::bind_t<void, boost::_mfi::mf1<void, tools::threadpool, bool>, boost::_bi::list2<boost::_bi::value<tools::threadpool*>, boost::_bi::value<bool> > >::operator() (this=<optimized out>) at /home/user/boost_1_65_1_install/include/boost/bind/bind.hpp:1294
#6  boost::detail::thread_data<boost::_bi::bind_t<void, boost::_mfi::mf1<void, tools::threadpool, bool>, boost::_bi::list2<boost::_bi::value<tools::threadpool*>, boost::_bi::value<bool> > > >::run (this=<optimized out>)
    at /home/user/boost_1_65_1_install/include/boost/thread/detail/thread.hpp:116
#7  0x00007ccc4f0474c6 in thread_proxy () from /home/user/boost_1_65_1_install/lib/libboost_thread.so.1.65.1
#8  0x00007ccc4e06473a in start_thread () from /lib64/libpthread.so.0
#9  0x00007ccc4dd9ee7f in clone () from /lib64/libc.so.6

Thread 9 (Thread 0x7ccc490e5700 (LWP 28804)):
#0  0x00007ccc4e06a480 in pthread_cond_wait@@GLIBC_2.3.2 () from /lib64/libpthread.so.0
#1  0x00005572bf2b25a9 in boost::asio::detail::posix_event::wait<boost::asio::detail::scoped_lock<boost::asio::detail::posix_mutex> > (
    lock=..., this=0x5572c106cb28) at /home/user/boost_1_65_1_install/include/boost/asio/detail/posix_event.hpp:106
#2  boost::asio::detail::task_io_service::do_run_one (ec=..., this_thread=..., lock=..., this=0x5572c106cad0)
    at /home/user/boost_1_65_1_install/include/boost/asio/detail/impl/task_io_service.ipp:380
#3  boost::asio::detail::task_io_service::run (ec=..., this=0x5572c106cad0)
    at /home/user/boost_1_65_1_install/include/boost/asio/detail/impl/task_io_service.ipp:149
#4  boost::asio::io_service::run (this=<optimized out>) at /home/user/boost_1_65_1_install/include/boost/asio/impl/io_service.ipp:59
#5  epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::worker_thread (this=0x5572c10736d8) at /home/user/src/bitmonero/contrib/epee/include/net/abstract_tcp_server2.inl:779
#6  0x00005572bf2a0095 in boost::_mfi::mf0<bool, epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > >::operator() (p=<optimized out>, this=<optimized out>)
    at /home/user/boost_1_65_1_install/include/boost/bind/mem_fn_template.hpp:49
#7  boost::_bi::list1<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >*> >::operator()<bool, boost::_mfi::mf0<bool, epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > >, boost::_bi::list0> (a=<synthetic pointer>..., f=..., this=<optimized out>)
---Type <return> to continue, or q <return> to quit---
    at /home/user/boost_1_65_1_install/include/boost/bind/bind.hpp:249
#8  boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > >, boost::_bi::list1<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >*> > >::operator() (this=<optimized out>)
    at /home/user/boost_1_65_1_install/include/boost/bind/bind.hpp:1294
#9  boost::detail::thread_data<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > >, boost::_bi::list1<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >*> > > >::run (this=<optimized out>)
    at /home/user/boost_1_65_1_install/include/boost/thread/detail/thread.hpp:116
#10 0x00007ccc4f0474c6 in thread_proxy () from /home/user/boost_1_65_1_install/lib/libboost_thread.so.1.65.1
#11 0x00007ccc4e06473a in start_thread () from /lib64/libpthread.so.0
#12 0x00007ccc4dd9ee7f in clone () from /lib64/libc.so.6

Thread 8 (Thread 0x7ccc46cdf700 (LWP 28803)):
#0  0x00007ccc4dd9f473 in epoll_wait () from /lib64/libc.so.6
#1  0x00005572bf2b20d9 in boost::asio::detail::epoll_reactor::run (ops=..., block=<optimized out>, this=0x5572c106be80)
    at /home/user/boost_1_65_1_install/include/boost/asio/detail/impl/epoll_reactor.ipp:438
#2  boost::asio::detail::task_io_service::do_run_one (ec=..., this_thread=..., lock=..., this=0x5572c106cad0)
    at /home/user/boost_1_65_1_install/include/boost/asio/detail/impl/task_io_service.ipp:356
#3  boost::asio::detail::task_io_service::run (ec=..., this=0x5572c106cad0)
    at /home/user/boost_1_65_1_install/include/boost/asio/detail/impl/task_io_service.ipp:149
#4  boost::asio::io_service::run (this=<optimized out>) at /home/user/boost_1_65_1_install/include/boost/asio/impl/io_service.ipp:59
#5  epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::worker_thread (this=0x5572c10736d8) at /home/user/src/bitmonero/contrib/epee/include/net/abstract_tcp_server2.inl:779
#6  0x00005572bf2a0095 in boost::_mfi::mf0<bool, epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > >::operator() (p=<optimized out>, this=<optimized out>)
    at /home/user/boost_1_65_1_install/include/boost/bind/mem_fn_template.hpp:49
#7  boost::_bi::list1<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >*> >::operator()<bool, boost::_mfi::mf0<bool, epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > >, boost::_bi::list0> (a=<synthetic pointer>..., f=..., this=<optimized out>)
    at /home/user/boost_1_65_1_install/include/boost/bind/bind.hpp:249
#8  boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > >, boost::_bi::list1<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >*> > >::operator() (this=<optimized out>)
    at /home/user/boost_1_65_1_install/include/boost/bind/bind.hpp:1294
#9  boost::detail::thread_data<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > >, boost::_bi::list1<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >*> > > >::run (this=<optimized out>)
---Type <return> to continue, or q <return> to quit---
    at /home/user/boost_1_65_1_install/include/boost/thread/detail/thread.hpp:116
#10 0x00007ccc4f0474c6 in thread_proxy () from /home/user/boost_1_65_1_install/lib/libboost_thread.so.1.65.1
#11 0x00007ccc4e06473a in start_thread () from /lib64/libpthread.so.0
#12 0x00007ccc4dd9ee7f in clone () from /lib64/libc.so.6

Thread 7 (Thread 0x7ccc452ca700 (LWP 28809)):
#0  0x00007ccc4dd92f3d in poll () from /lib64/libc.so.6
#1  0x00007ccc52dfad8a in zmq::signaler_t::wait(int) () from /lib64/libzmq.so.5
#2  0x00007ccc52ddfcf6 in zmq::mailbox_t::recv(zmq::command_t*, int) () from /lib64/libzmq.so.5
#3  0x00007ccc52dfc17a in zmq::socket_base_t::process_commands(int, bool) () from /lib64/libzmq.so.5
#4  0x00007ccc52dfc8fb in zmq::socket_base_t::recv(zmq::msg_t*, int) () from /lib64/libzmq.so.5
#5  0x00007ccc52e13049 in s_recvmsg(zmq::socket_base_t*, zmq_msg_t*, int) () from /lib64/libzmq.so.5

#6  0x00007ccc53c1a4ee in zmq::socket_t::recv (flags_=0, msg_=0x0, this=<optimized out>) at /usr/include/zmq.hpp:637
#7  cryptonote::rpc::ZmqServer::serve (this=0x7ffc56f40af0) at /home/user/src/bitmonero/src/rpc/zmq_server.cpp:63
#8  0x00007ccc53c1bc77 in boost::_mfi::mf0<void, cryptonote::rpc::ZmqServer>::operator() (p=<optimized out>, this=<optimized out>)
    at /home/user/boost_1_65_1_install/include/boost/bind/mem_fn_template.hpp:49
#9  boost::_bi::list1<boost::_bi::value<cryptonote::rpc::ZmqServer*> >::operator()<boost::_mfi::mf0<void, cryptonote::rpc::ZmqServer>, boost::_bi::list0> (a=<synthetic pointer>..., f=..., this=<optimized out>) at /home/user/boost_1_65_1_install/include/boost/bind/bind.hpp:259
#10 boost::_bi::bind_t<void, boost::_mfi::mf0<void, cryptonote::rpc::ZmqServer>, boost::_bi::list1<boost::_bi::value<cryptonote::rpc::ZmqServer*> > >::operator() (this=<optimized out>) at /home/user/boost_1_65_1_install/include/boost/bind/bind.hpp:1294
#11 boost::detail::thread_data<boost::_bi::bind_t<void, boost::_mfi::mf0<void, cryptonote::rpc::ZmqServer>, boost::_bi::list1<boost::_bi::value<cryptonote::rpc::ZmqServer*> > > >::run (this=<optimized out>)
    at /home/user/boost_1_65_1_install/include/boost/thread/detail/thread.hpp:116
#12 0x00007ccc4f0474c6 in thread_proxy () from /home/user/boost_1_65_1_install/lib/libboost_thread.so.1.65.1
#13 0x00007ccc4e06473a in start_thread () from /lib64/libpthread.so.0
#14 0x00007ccc4dd9ee7f in clone () from /lib64/libc.so.6

Thread 6 (Thread 0x7ccc478e2700 (LWP 28798)):


#0  0x00007ccc4e06a480 in pthread_cond_wait@@GLIBC_2.3.2 () from /lib64/libpthread.so.0
#1  0x00007ccc51a686dd in boost::asio::detail::posix_event::wait<boost::asio::detail::scoped_lock<boost::asio::detail::posix_mutex> > (
    lock=..., this=<optimized out>) at /home/user/boost_1_65_1_install/include/boost/asio/detail/posix_event.hpp:106
#2  boost::asio::detail::task_io_service::do_run_one (ec=..., this_thread=..., lock=..., this=0x5572c105dfa0)
    at /home/user/boost_1_65_1_install/include/boost/asio/detail/impl/task_io_service.ipp:380
#3  boost::asio::detail::task_io_service::run (ec=..., this=0x5572c105dfa0)
    at /home/user/boost_1_65_1_install/include/boost/asio/detail/impl/task_io_service.ipp:149
#4  boost::asio::io_service::run (this=<optimized out>) at /home/user/boost_1_65_1_install/include/boost/asio/impl/io_service.ipp:59
#5  0x00007ccc51a5a079 in boost::_mfi::mf0<unsigned long, boost::asio::io_service>::operator() (p=<optimized out>, this=<optimized out>)
    at /home/user/boost_1_65_1_install/include/boost/bind/mem_fn_template.hpp:49
---Type <return> to continue, or q <return> to quit---
#6  boost::_bi::list1<boost::_bi::value<boost::asio::io_service*> >::operator()<unsigned long, boost::_mfi::mf0<unsigned long, boost::asio::io_service>, boost::_bi::list0> (a=<synthetic pointer>..., f=..., this=<optimized out>)
    at /home/user/boost_1_65_1_install/include/boost/bind/bind.hpp:249
#7  boost::_bi::bind_t<unsigned long, boost::_mfi::mf0<unsigned long, boost::asio::io_service>, boost::_bi::list1<boost::_bi::value<boost::asio::io_service*> > >::operator() (this=<optimized out>) at /home/user/boost_1_65_1_install/include/boost/bind/bind.hpp:1294
#8  boost::detail::thread_data<boost::_bi::bind_t<unsigned long, boost::_mfi::mf0<unsigned long, boost::asio::io_service>, boost::_bi::list1<boost::_bi::value<boost::asio::io_service*> > > >::run (this=<optimized out>)
    at /home/user/boost_1_65_1_install/include/boost/thread/detail/thread.hpp:116
#9  0x00007ccc4f0474c6 in thread_proxy () from /home/user/boost_1_65_1_install/lib/libboost_thread.so.1.65.1
#10 0x00007ccc4e06473a in start_thread () from /lib64/libpthread.so.0
#11 0x00007ccc4dd9ee7f in clone () from /lib64/libc.so.6

Thread 5 (Thread 0x7ccbca8fb700 (LWP 28827)):
#0  0x00007ccc4e06a480 in pthread_cond_wait@@GLIBC_2.3.2 () from /lib64/libpthread.so.0
#1  0x00007ccc50515f6e in boost::condition_variable::wait (m=..., this=0x7ccc51ce80f0 <tools::threadpool::getInstance()::instance+80>)
    at /home/user/boost_1_65_1_install/include/boost/thread/pthread/condition_variable.hpp:81
#2  tools::threadpool::run (this=0x7ccc51ce80a0 <tools::threadpool::getInstance()::instance>, flush=false)
    at /home/user/src/bitmonero/src/common/threadpool.cpp:136
#3  0x00007ccc50518c36 in boost::_mfi::mf1<void, tools::threadpool, bool>::operator() (a1=<optimized out>, p=<optimized out>, 
    this=<optimized out>) at /home/user/boost_1_65_1_install/include/boost/bind/mem_fn_template.hpp:165
#4  boost::_bi::list2<boost::_bi::value<tools::threadpool*>, boost::_bi::value<bool> >::operator()<boost::_mfi::mf1<void, tools::threadpool, bool>, boost::_bi::list0> (a=<synthetic pointer>..., f=..., this=<optimized out>)
    at /home/user/boost_1_65_1_install/include/boost/bind/bind.hpp:319
#5  boost::_bi::bind_t<void, boost::_mfi::mf1<void, tools::threadpool, bool>, boost::_bi::list2<boost::_bi::value<tools::threadpool*>, boost::_bi::value<bool> > >::operator() (this=<optimized out>) at /home/user/boost_1_65_1_install/include/boost/bind/bind.hpp:1294
#6  boost::detail::thread_data<boost::_bi::bind_t<void, boost::_mfi::mf1<void, tools::threadpool, bool>, boost::_bi::list2<boost::_bi::value<tools::threadpool*>, boost::_bi::value<bool> > > >::run (this=<optimized out>)
    at /home/user/boost_1_65_1_install/include/boost/thread/detail/thread.hpp:116
#7  0x00007ccc4f0474c6 in thread_proxy () from /home/user/boost_1_65_1_install/lib/libboost_thread.so.1.65.1
#8  0x00007ccc4e06473a in start_thread () from /lib64/libpthread.so.0
#9  0x00007ccc4dd9ee7f in clone () from /lib64/libc.so.6

Thread 4 (Thread 0x7ccc45acb700 (LWP 28808)):
#0  0x00007ccc4dd9f473 in epoll_wait () from /lib64/libc.so.6
#1  0x00007ccc52dd937a in zmq::epoll_t::loop() () from /lib64/libzmq.so.5
#2  0x00007ccc52e0de8d in thread_routine () from /lib64/libzmq.so.5
#3  0x00007ccc4e06473a in start_thread () from /lib64/libpthread.so.0
#4  0x00007ccc4dd9ee7f in clone () from /lib64/libc.so.6
---Type <return> to continue, or q <return> to quit---

Thread 3 (Thread 0x7ccc462cc700 (LWP 28807)):
#0  0x00007ccc4dd9f473 in epoll_wait () from /lib64/libc.so.6
#1  0x00007ccc52dd937a in zmq::epoll_t::loop() () from /lib64/libzmq.so.5
#2  0x00007ccc52e0de8d in thread_routine () from /lib64/libzmq.so.5
#3  0x00007ccc4e06473a in start_thread () from /lib64/libpthread.so.0
#4  0x00007ccc4dd9ee7f in clone () from /lib64/libc.so.6

Thread 2 (Thread 0x7ccbc98f9700 (LWP 28825)):
#0  0x00007ccc4e06a480 in pthread_cond_wait@@GLIBC_2.3.2 () from /lib64/libpthread.so.0
#1  0x00007ccc50515f6e in boost::condition_variable::wait (m=..., this=0x7ccc51ce80f0 <tools::threadpool::getInstance()::instance+80>)
    at /home/user/boost_1_65_1_install/include/boost/thread/pthread/condition_variable.hpp:81
#2  tools::threadpool::run (this=0x7ccc51ce80a0 <tools::threadpool::getInstance()::instance>, flush=false)
    at /home/user/src/bitmonero/src/common/threadpool.cpp:136
#3  0x00007ccc50518c36 in boost::_mfi::mf1<void, tools::threadpool, bool>::operator() (a1=<optimized out>, p=<optimized out>, 
    this=<optimized out>) at /home/user/boost_1_65_1_install/include/boost/bind/mem_fn_template.hpp:165
#4  boost::_bi::list2<boost::_bi::value<tools::threadpool*>, boost::_bi::value<bool> >::operator()<boost::_mfi::mf1<void, tools::threadpool, bool>, boost::_bi::list0> (a=<synthetic pointer>..., f=..., this=<optimized out>)
    at /home/user/boost_1_65_1_install/include/boost/bind/bind.hpp:319
#5  boost::_bi::bind_t<void, boost::_mfi::mf1<void, tools::threadpool, bool>, boost::_bi::list2<boost::_bi::value<tools::threadpool*>, boost::_bi::value<bool> > >::operator() (this=<optimized out>) at /home/user/boost_1_65_1_install/include/boost/bind/bind.hpp:1294
#6  boost::detail::thread_data<boost::_bi::bind_t<void, boost::_mfi::mf1<void, tools::threadpool, bool>, boost::_bi::list2<boost::_bi::value<tools::threadpool*>, boost::_bi::value<bool> > > >::run (this=<optimized out>)
    at /home/user/boost_1_65_1_install/include/boost/thread/detail/thread.hpp:116
#7  0x00007ccc4f0474c6 in thread_proxy () from /home/user/boost_1_65_1_install/lib/libboost_thread.so.1.65.1
#8  0x00007ccc4e06473a in start_thread () from /lib64/libpthread.so.0
#9  0x00007ccc4dd9ee7f in clone () from /lib64/libc.so.6

Thread 1 (Thread 0x7ccc54627180 (LWP 28778)):
#0  0x00007ccc4dccc8df in raise () from /lib64/libc.so.6
#1  0x00007ccc4dcce4da in abort () from /lib64/libc.so.6
#2  0x00007ccc5050b178 in tools::posix_crash_handler (signal=<optimized out>) at /home/user/src/bitmonero/src/common/util.cpp:585
#3  <signal handler called>
#4  0x00007ccc4dd3c5e0 in __strcpy_sse2_unaligned () from /lib64/libc.so.6
#5  0x00007ccc52ba0d8f in rl_replace_line () from /lib64/libreadline.so.6
#6  0x00005572bf3ee5fc in remove_line_handler () at /home/user/src/bitmonero/contrib/epee/src/readline_buffer.cpp:218
#7  rdln::readline_buffer::stop (this=this@entry=0x5572c10034f8) at /home/user/src/bitmonero/contrib/epee/src/readline_buffer.cpp:67
#8  0x00005572bf2888b1 in epee::async_stdin_reader::stop (this=0x5572c10034e0)
---Type <return> to continue, or q <return> to quit---
    at /home/user/src/bitmonero/contrib/epee/include/console_handler.h:119
#9  epee::async_console_handler::stop (this=0x5572c10034e0) at /home/user/src/bitmonero/contrib/epee/include/console_handler.h:311
#10 epee::console_handlers_binder::stop_handling (this=0x5572c10034a8)
    at /home/user/src/bitmonero/contrib/epee/include/console_handler.h:540
#11 daemonize::t_command_server::stop_handling (this=0x5572c1003490) at /home/user/src/bitmonero/src/daemon/command_server.cpp:318
#12 0x00005572bf29f11e in daemonize::t_daemon::run (this=this@entry=0x7ffc56f40dc0, interactive=interactive@entry=true)
    at /home/user/src/bitmonero/src/daemon/daemon.cpp:182
#13 0x00005572bf35749c in daemonize::t_executor::run_interactive (this=<optimized out>, vm=...)
    at /home/user/src/bitmonero/src/daemon/executor.cpp:76
#14 0x00005572bf360caf in daemonizer::daemonize<daemonize::t_executor>(int, char const**, daemonize::t_executor&&, boost::program_options::variables_map const&) (argc=<optimized out>, argv=<optimized out>, 
    executor=<unknown type in /home/user/src/bitmonero/build/debug/bin/monerod, CU 0x8579f3, DIE 0x9534b4>, vm=...)
    at /home/user/src/bitmonero/src/daemonizer/posix_daemonizer.inl:104
#15 0x00005572bf35a662 in main (argc=6, argv=0x7ffc56f41c78) at /home/user/src/bitmonero/src/daemon/main.cpp:284
(gdb) 
```

# Discussion History
## hyc | 2018-05-13T13:57:06+00:00
Can you `print rl_line_buffer` 

## moneromooo-monero | 2018-05-13T14:31:53+00:00
No, I don't have the binary nor core, sorry. I'll keep it in mind if it ever happens again.

## jtgrassie | 2018-05-14T17:02:58+00:00
I don't think we _need_ to call `remove_line_handler` on exit but bypassing that call might be tricky because we do need to call it when we are suspending readline elsewhere.

## jtgrassie | 2018-05-14T17:19:15+00:00
In any case, it's odd crashing there as `rl_replace_line` just does a `strcpy` to `rl_line_buffer`. So `rl_line_buffer` must be in an unpredictable state. I guess readline must be cleaning up on exit before we have finished stopping.

## moneromooo-monero | 2018-06-06T15:17:01+00:00
Another reported by iDunk: https://paste.debian.net/hidden/f1f19aec/
Different stack trace, but if the locking is bogus, it's likely to be the same cause.

This was not on exit, but on up arrow.

## moneromooo-monero | 2019-01-10T21:46:45+00:00
Another one, this time while running:

The NULL was rl_prompt, most likely. No core generated, because ASAN disables them by default and I always forget to tell it not to :/

<pre>
2019-01-10 21:43:52.614	[SRV_MAIN]	INFO	global	src/daemon/rpc.h:78	core RPC server started ok
AddressSanitizer:DEADLYSIGNAL
=================================================================
==5967==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000000 (pc 0x5e369a45bc68 bp 0x76473fa04100 sp 0x76473fa03fe0 T3)
==5967==The signal is caused by a READ memory access.
==5967==Hint: address points to the zero page.
    #0 0x5e369a45bc67 in rdln::readline_buffer::sync() /home/user/src/bitmonero/contrib/epee/src/readline_buffer.cpp:117:17
    #1 0x764a1367ab51 in std::ostream::flush() (/lib64/libstdc++.so.6+0x117b51)
    #2 0x764a139bbbac in el::base::DefaultLogDispatchCallback::dispatch(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&&) /home/user/src/bitmonero/external/easylogging++/easylogging++.cc:2380:22
    #3 0x764a139bb376 in el::base::DefaultLogDispatchCallback::handle(el::LogDispatchData const*) /home/user/src/bitmonero/external/easylogging++/easylogging++.cc:2348:3
    #4 0x764a139bf0c8 in el::base::LogDispatcher::dispatch() /home/user/src/bitmonero/external/easylogging++/easylogging++.cc:2637:17
    #5 0x764a139c2391 in el::base::Writer::triggerDispatch() /home/user/src/bitmonero/external/easylogging++/easylogging++.cc:2789:62
    #6 0x764a139c18cd in el::base::Writer::processDispatch() /home/user/src/bitmonero/external/easylogging++/easylogging++.cc:2770:7
    #7 0x5e3699df8ef2 in el::base::Writer::~Writer() /home/user/src/bitmonero/external/easylogging++/easylogging++.h:3253:5
    #8 0x5e369a229ec9 in epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::save_dbg_log() /home/user/src/bitmonero/contrib/epee/include/net/abstract_tcp_server2.inl:286:5
    #9 0x5e369a19f01d in epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::handle_accept(boost::system::error_code const&) /home/user/src/bitmonero/contrib/epee/include/net/abstract_tcp_server2.inl:1139:13
    #10 0x5e369a22215a in boost::_mfi::mf1<void, epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&>::operator()(epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >*, boost::system::error_code const&) const /home/user/boost_1_65_1_install/include/boost/bind/mem_fn_template.hpp:165:29
    #11 0x5e369a22203f in void boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >*>, boost::arg<1> (*)()>::operator()<boost::_mfi::mf1<void, epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&>, boost::_bi::rrlist1<boost::system::error_code const&> >(boost::_bi::type<void>, boost::_mfi::mf1<void, epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&>&, boost::_bi::rrlist1<boost::system::error_code const&>&, int) /home/user/boost_1_65_1_install/include/boost/bind/bind.hpp:319:9
    #12 0x5e369a221ee0 in void boost::_bi::bind_t<void, boost::_mfi::mf1<void, epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&>, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >*>, boost::arg<1> (*)()> >::operator()<boost::system::error_code const&>(boost::system::error_code const&) /home/user/boost_1_65_1_install/include/boost/bind/bind.hpp:1306:16
    #13 0x5e369a221dae in boost::asio::detail::binder1<boost::_bi::bind_t<void, boost::_mfi::mf1<void, epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&>, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >*>, boost::arg<1> (*)()> >, boost::system::error_code>::operator()() /home/user/boost_1_65_1_install/include/boost/asio/detail/bind_handler.hpp:47:5
    #14 0x5e369a221d84 in void boost::asio::asio_handler_invoke<boost::asio::detail::binder1<boost::_bi::bind_t<void, boost::_mfi::mf1<void, epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&>, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >*>, boost::arg<1> (*)()> >, boost::system::error_code> >(boost::asio::detail::binder1<boost::_bi::bind_t<void, boost::_mfi::mf1<void, epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&>, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >*>, boost::arg<1> (*)()> >, boost::system::error_code>&, ...) /home/user/boost_1_65_1_install/include/boost/asio/handler_invoke_hook.hpp:69:3
    #15 0x5e369a221cd1 in void boost_asio_handler_invoke_helpers::invoke<boost::asio::detail::binder1<boost::_bi::bind_t<void, boost::_mfi::mf1<void, epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&>, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >*>, boost::arg<1> (*)()> >, boost::system::error_code>, boost::_bi::bind_t<void, boost::_mfi::mf1<void, epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&>, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >*>, boost::arg<1> (*)()> > >(boost::asio::detail::binder1<boost::_bi::bind_t<void, boost::_mfi::mf1<void, epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&>, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >*>, boost::arg<1> (*)()> >, boost::system::error_code>&, boost::_bi::bind_t<void, boost::_mfi::mf1<void, epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&>, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >*>, boost::arg<1> (*)()> >&) /home/user/boost_1_65_1_install/include/boost/asio/detail/handler_invoke_helpers.hpp:37:3
    #16 0x5e369a221741 in boost::asio::detail::reactive_socket_accept_op<boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >, boost::asio::ip::tcp, boost::_bi::bind_t<void, boost::_mfi::mf1<void, epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&>, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >*>, boost::arg<1> (*)()> > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) /home/user/boost_1_65_1_install/include/boost/asio/detail/reactive_socket_accept_op.hpp:123:7
    #17 0x5e369a023687 in boost::asio::detail::task_io_service_operation::complete(boost::asio::detail::task_io_service&, boost::system::error_code const&, unsigned long) /home/user/boost_1_65_1_install/include/boost/asio/detail/task_io_service_operation.hpp:38:5
    #18 0x5e369a022358 in boost::asio::detail::task_io_service::do_run_one(boost::asio::detail::scoped_lock<boost::asio::detail::posix_mutex>&, boost::asio::detail::task_io_service_thread_info&, boost::system::error_code const&) /home/user/boost_1_65_1_install/include/boost/asio/detail/impl/task_io_service.ipp:372:12
    #19 0x5e369a193392 in boost::asio::detail::task_io_service::run(boost::system::error_code&) /home/user/boost_1_65_1_install/include/boost/asio/detail/impl/task_io_service.ipp:149:10
    #20 0x5e369a192d0a in boost::asio::io_service::run() /home/user/boost_1_65_1_install/include/boost/asio/impl/io_service.ipp:59:25
    #21 0x5e369a18aeee in epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::worker_thread() /home/user/src/bitmonero/contrib/epee/include/net/abstract_tcp_server2.inl:962:34
    #22 0x5e369a197f02 in boost::_mfi::mf0<bool, epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > >::operator()(epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >*) const /home/user/boost_1_65_1_install/include/boost/bind/mem_fn_template.hpp:49:29
    #23 0x5e369a197de5 in bool boost::_bi::list1<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >*> >::operator()<bool, boost::_mfi::mf0<bool, epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > >, boost::_bi::list0>(boost::_bi::type<bool>, boost::_mfi::mf0<bool, epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > >&, boost::_bi::list0&, long) /home/user/boost_1_65_1_install/include/boost/bind/bind.hpp:249:16
    #24 0x5e369a197ce1 in boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > >, boost::_bi::list1<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >*> > >::operator()() /home/user/boost_1_65_1_install/include/boost/bind/bind.hpp:1294:16
    #25 0x5e369a197bbb in boost::detail::thread_data<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > >, boost::_bi::list1<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >*> > > >::run() /home/user/boost_1_65_1_install/include/boost/thread/detail/thread.hpp:116:17
    #26 0x764a140db954 in thread_proxy (/home/user/boost_1_65_1_install/lib/libboost_thread.so.1.65.1+0x14954)
    #27 0x764a12fb7593 in start_thread (/lib64/libpthread.so.0+0x7593)
    #28 0x764a12ad2e6e in __GI___clone (/lib64/libc.so.6+0xf9e6e)

AddressSanitizer can not provide additional info.
SUMMARY: AddressSanitizer: SEGV /home/user/src/bitmonero/contrib/epee/src/readline_buffer.cpp:117:17 in rdln::readline_buffer::sync()
Thread T3 created by T0 here:
    #0 0x5e3699d17a84 in __interceptor_pthread_create (/home/user/src/bitmonero/build/debug/bin/monerod+0x471a84)
    #1 0x764a140da2d9 in boost::thread::start_thread_noexcept(boost::thread_attributes const&) (/home/user/boost_1_65_1_install/lib/libboost_thread.so.1.65.1+0x132d9)

==5967==ABORTING
</pre>


## jtgrassie | 2019-01-12T06:57:26+00:00
Thanks @moneromooo-monero - #5065

## Gingeropolous | 2019-09-23T01:50:19+00:00
was testing randomx forknet, got this

```
    #0 0x7ffff6ea0253 in pthread_create (/usr/lib/x86_64-linux-gnu/libasan.so.2+0x36253)
    #1 0x7ffff4bf2b38 in boost::thread::start_thread_noexcept() (/usr/local/lib/libboost_thread.so.1.67.0+0x12b38)
    #2 0x555555a2d139 in epee::console_handlers_binder::start_handling(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()>) /home/fastpc/mon_rx_testnet/contrib/epee/include/console_handler.h:616
    #3 0x555555a2d139 in daemonize::t_command_server::start_handling(std::function<void ()>) /home/fastpc/mon_rx_testnet/src/daemon/command_server.cpp:341
    #4 0x555555a571b2 in daemonize::t_daemon::run(bool) /home/fastpc/mon_rx_testnet/src/daemon/daemon.cpp:169
    #5 0x555555c3e118 in daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) /home/fastpc/mon_rx_testnet/src/daemon/executor.cpp:76

SUMMARY: AddressSanitizer: heap-use-after-free /home/fastpc/mon_rx_testnet/contrib/epee/include/readline_buffer.h:18 rdln::readline_buffer::is_running() const
Shadow bytes around the buggy address:
  0x0c2e7fff97f0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c2e7fff9800: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 fa
  0x0c2e7fff9810: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c2e7fff9820: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
  0x0c2e7fff9830: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
=>0x0c2e7fff9840: fd fd fd fd fd fd[fd]fd fd fd fd fd fd fd fd fd
  0x0c2e7fff9850: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
  0x0c2e7fff9860: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
  0x0c2e7fff9870: fd fd fd fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c2e7fff9880: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c2e7fff9890: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07
  Heap left redzone:       fa
  Heap right redzone:      fb
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack partial redzone:   f4
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
==12273==ABORTING
[Thread 0x7ffd0074c700 (LWP 12299) exited]
[Thread 0x7ffd00c74700 (LWP 12298) exited]
[Thread 0x7ffd0119b700 (LWP 12297) exited]
[Thread 0x7ffd016c2700 (LWP 12296) exited]
[Thread 0x7ffd01be9700 (LWP 12295) exited]
[Thread 0x7ffd02107700 (LWP 12294) exited]
[Thread 0x7ffd05cb9700 (LWP 12283) exited]
[Thread 0x7ffd07d41700 (LWP 12279) exited]
[Thread 0x7ffd0a057700 (LWP 12275) exited]
[Thread 0x7fffeee76700 (LWP 12274) exited]
[Thread 0x7ffff7fc9800 (LWP 12273) exited]
[Inferior 1 (process 12273) exited with code 01]
```

feeling cute, didn't copy the entire thing cause screen is stupid with copy and paste

## Gingeropolous | 2019-09-23T02:01:14+00:00
okay here's the rest of it

```
2019-09-23 00:52:00.628 D [node] Stop signal sent
[Thread 0x7ffd04521700 (LWP 12287) exited]
[Thread 0x7ffd0548b700 (LWP 12284) exited]
[Thread 0x7ffd02b5e700 (LWP 12292) exited]
[Thread 0x7ffd02637700 (LWP 12293) exited]
[Thread 0x7ffd03085700 (LWP 12291) exited]
[Thread 0x7ffd03ad3700 (LWP 12289) exited]
[Thread 0x7ffd03ffa700 (LWP 12288) exited]
[Thread 0x7ffd04a4f700 (LWP 12286) exited]
[Thread 0x7ffd04f6d700 (LWP 12285) exited]
2019-09-23 00:52:00.629 I Miner thread stopped [0]
[Thread 0x7ffcd78cf700 (LWP 12831) exited]
2019-09-23 00:52:00.631 I Miner thread stopped [1]
[Thread 0x7ffc4f1fe700 (LWP 12832) exited]
[Thread 0x7ffd035ac700 (LWP 12290) exited]
2019-09-23 00:52:00.637 D JOINING all threads - almost
2019-09-23 00:52:00.637 D JOINING all threads - DONE
2019-09-23 00:52:00.637 I net_service loop stopped.
2019-09-23 00:52:00.637 I p2p net loop stopped
[Thread 0x7ffd0855f700 (LWP 12278) exited]
[Thread 0x7ffd064d7700 (LWP 12282) exited]
[Thread 0x7ffd07523700 (LWP 12280) exited]
[Thread 0x7ffd06cfd700 (LWP 12281) exited]
2019-09-23 00:52:00.639 I Stopping core RPC server...
[Thread 0x7ffd09856700 (LWP 12276) exited]
[Thread 0x7ffd09055700 (LWP 12277) exited]
2019-09-23 00:52:00.639 I Node stopped.
2019-09-23 00:52:00.729 I Mining has been stopped, 2 finished
=================================================================
==12273==ERROR: AddressSanitizer: heap-use-after-free on address 0x61700000c230 at pc 0x555556298fc2 bp 0x7ffd07d3f1e0 sp 0x7ffd07d3f1d0
READ of size 8 at 0x61700000c230 thread T6
    #0 0x555556298fc1 in rdln::readline_buffer::is_running() const /home/fastpc/mon_rx_testnet/contrib/epee/include/readline_buffer.h:18
    #1 0x555556298fc1 in rdln::suspend_readline::suspend_readline() /home/fastpc/mon_rx_testnet/contrib/epee/src/readline_buffer.cpp:27
    #2 0x555555a226ce in tools::scoped_message_writer::~scoped_message_writer() (/home/fastpc/mon_rx_testnet/build/Linux/master/debug/bin/monerod+0x4ce6ce)
2019-09-23 00:52:00.788 D Thread monitor number of peers - done
    #3 0x555555c6bec4 in daemonize::t_rpc_command_executor::stop_daemon() /home/fastpc/mon_rx_testnet/src/daemon/rpc_command_executor.cpp:1374
    #4 0x555555a06fd9 in daemonize::t_command_parser_executor::stop_daemon(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_s
tring<char, std::char_traits<char>, std::allocator<char> > > > const&) /home/fastpc/mon_rx_testnet/src/daemon/command_parser_executor.cpp:441
    #5 0x555555a40797 in bool std::_Mem_fn_base<bool (daemonize::t_command_parser_executor::*)(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<s
td::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&), true>::operator()<std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, s
td::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&, void>(daemonize::t_command_parser_executor*, std::vector<std::__cxx11::basic_string<char, std::cha
r_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&) const /usr/include/c++/5/functional:600
    #6 0x555555a40797 in bool std::_Bind<std::_Mem_fn<bool (daemonize::t_command_parser_executor::*)(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::alloc
ator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&)> (daemonize::t_command_parser_executor*, std::_Placeholder<1>)>::__call<bool, std::vector<std::__cxx11::bas
ic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&, 0ul, 1ul>(std::tuple<std::vector<
std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&>&&, std::_Index_t
uple<0ul, 1ul>) /usr/include/c++/5/functional:1074
    #7 0x555555a40797 in bool std::_Bind<std::_Mem_fn<bool (daemonize::t_command_parser_executor::*)(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::alloc
ator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&)> (daemonize::t_command_parser_executor*, std::_Placeholder<1>)>::operator()<std::vector<std::__cxx11::basic
_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&, bool>(std::vector<std::__cxx11::bas
ic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&) /usr/include/c++/5/functional:113
3
    #8 0x555555a40797 in boost::detail::function::function_obj_invoker1<std::_Bind<std::_Mem_fn<bool (daemonize::t_command_parser_executor::*)(std::vector<std::__cxx11::basic_string<char, std::char_traits
<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&)> (daemonize::t_command_parser_executor*, std::_Placeholder<1>)>, 
bool, std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&
>::invoke(boost::detail::function::function_buffer&, std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_
traits<char>, std::allocator<char> > > > const&) /usr/local/include/boost/function/function_template.hpp:138
    #9 0x555555a33805 in boost::function1<bool, std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_trait
s<char>, std::allocator<char> > > > const&>::operator()(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::ch
ar_traits<char>, std::allocator<char> > > > const&) const /usr/local/include/boost/function/function_template.hpp:769
    #10 0x555555a33805 in epee::command_handler::process_command_vec(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<
char, std::char_traits<char>, std::allocator<char> > > > const&) /home/fastpc/mon_rx_testnet/contrib/epee/include/console_handler.h:580
    #11 0x555555a42a64 in epee::command_handler::process_command_str(boost::optional<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > const&) (/home/fastpc/mon_rx_testnet/
build/Linux/master/debug/bin/monerod+0x4eea64)
    #12 0x555555a3faad in bool epee::async_console_handler::run<bool epee::async_console_handler::run<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, boost::optional<std::__cxx11::b
asic_string<char, std::char_traits<char>, std::allocator<char> > > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > > >(boost::_bi::bind_t<bool, boost::_mfi::m
f1<bool, epee::command_handler, boost::optional<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder
*>, boost::arg<1> > >, std::function<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > ()>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > co
nst&, std::function<void ()>)::{lambda(boost::optional<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > const&)#1}>(std::function<std::__cxx11::basic_string<char, std::cha
r_traits<char>, std::allocator<char> > ()>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, bool epee::async_console_handler::run<boost::_bi::bind_t<bool, boost::_m
fi::mf1<bool, epee::command_handler, boost::optional<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_b
inder*>, boost::arg<1> > > >(boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, boost::optional<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > const&
>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > >, std::function<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > ()>, std::__cxx11::
basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()>)::{lambda(boost::optional<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >
 const&)#1} const&, std::function<void ()>) (/home/fastpc/mon_rx_testnet/build/Linux/master/debug/bin/monerod+0x4ebaad)
    #13 0x555555a403e6 in epee::console_handlers_binder::run_handling(std::function<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > ()>, std::__cxx11::basic_string<char, st
d::char_traits<char>, std::allocator<char> > const&, std::function<void ()>) (/home/fastpc/mon_rx_testnet/build/Linux/master/debug/bin/monerod+0x4ec3e6)
    #14 0x555555a31256 in boost::detail::thread_data<boost::_bi::bind_t<bool, boost::_mfi::mf3<bool, epee::console_handlers_binder, std::function<std::__cxx11::basic_string<char, std::char_traits<char>, s
td::allocator<char> > ()>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()> >, boost::_bi::list4<boost::_bi::value<epee::console_handlers_bind
er*>, boost::_bi::value<std::function<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > ()> >, boost::_bi::value<std::__cxx11::basic_string<char, std::char_traits<char>, std:
:allocator<char> > >, boost::_bi::value<std::function<void ()> > > > >::run() (/home/fastpc/mon_rx_testnet/build/Linux/master/debug/bin/monerod+0x4dd256)
    #15 0x7ffff4bf3eec in thread_proxy (/usr/local/lib/libboost_thread.so.1.67.0+0x13eec)
    #16 0x7ffff41296b9 in start_thread (/lib/x86_64-linux-gnu/libpthread.so.0+0x76b9)
    #17 0x7ffff3e5f41c in clone (/lib/x86_64-linux-gnu/libc.so.6+0x10741c)

0x61700000c230 is located 304 bytes inside of 664-byte region [0x61700000c100,0x61700000c398)
freed by thread T0 here:
    #0 0x7ffff6f03b2a in operator delete(void*) (/usr/lib/x86_64-linux-gnu/libasan.so.2+0x99b2a)
    #1 0x555555a5887d in std::default_delete<daemonize::t_command_server>::operator()(daemonize::t_command_server*) const /usr/include/c++/5/bits/unique_ptr.h:76
    #2 0x555555a5887d in std::unique_ptr<daemonize::t_command_server, std::default_delete<daemonize::t_command_server> >::~unique_ptr() /usr/include/c++/5/bits/unique_ptr.h:236
    #3 0x555555a5887d in daemonize::t_daemon::run(bool) /home/fastpc/mon_rx_testnet/src/daemon/daemon.cpp:164
    #4 0x555555c3e118 in daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) /home/fastpc/mon_rx_testnet/src/daemon/executor.cpp:76

previously allocated by thread T0 here:
    #0 0x7ffff6f03532 in operator new(unsigned long) (/usr/lib/x86_64-linux-gnu/libasan.so.2+0x99532)
    #1 0x555555a56a4e in daemonize::t_daemon::run(bool) /home/fastpc/mon_rx_testnet/src/daemon/daemon.cpp:168
    #2 0x555555c3e118 in daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) /home/fastpc/mon_rx_testnet/src/daemon/executor.cpp:76

Thread T6 created by T0 here:
    #0 0x7ffff6ea0253 in pthread_create (/usr/lib/x86_64-linux-gnu/libasan.so.2+0x36253)
    #1 0x7ffff4bf2b38 in boost::thread::start_thread_noexcept() (/usr/local/lib/libboost_thread.so.1.67.0+0x12b38)
    #2 0x555555a2d139 in epee::console_handlers_binder::start_handling(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()>) /home/fastpc/mon_rx_testnet/contrib/epee/include/console_handler.h:616
    #3 0x555555a2d139 in daemonize::t_command_server::start_handling(std::function<void ()>) /home/fastpc/mon_rx_testnet/src/daemon/command_server.cpp:341
    #4 0x555555a571b2 in daemonize::t_daemon::run(bool) /home/fastpc/mon_rx_testnet/src/daemon/daemon.cpp:169
    #5 0x555555c3e118 in daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) /home/fastpc/mon_rx_testnet/src/daemon/executor.cpp:76
```


## selsta | 2020-11-03T02:45:17+00:00
Had this one while spamming sync_info. Looks similar to https://github.com/monero-project/monero/issues/3799#issuecomment-453266091
```
sync_info
2020-11-03 02:36:42.206	D Read command: sync_info
2020-11-03 02:36:42.215	D Couldn't use largePages for RandomX cache
2020-11-03 02:36:42.749	D [51.68.215.64:4238 OUT] LEVIN_PACKET_RECEIVED. [len=10, flags1, r?=1, cmd = 1003, v=1
2020-11-03 02:36:42.749	I [51.68.215.64:4238 OUT] 10 bytes received for category command-1003 initiated by peer
2020-11-03 02:36:42.749	D [51.68.215.64:4238 OUT] COMMAND_PING
2020-11-03 02:36:43.047	I [51.68.215.64:4238 OUT] 38 bytes sent for category command-1003 initiated by peer
2020-11-03 02:36:43.047	D do_send_chunk() NOW SENSD: packet=71 B
2020-11-03 02:36:43.048	D [51.68.215.64:4238 OUT] LEVIN_PACKET_SENT. [len=38, flags2, r?=0, cmd = 1003, ver=1
2020-11-03 02:36:43.440	D Couldn't use largePages for RandomX VM
2020-11-03 02:36:43.842	D Couldn't use largePages for RandomX VM
2020-11-03 02:36:44.244	D Couldn't use largePages for RandomX VM
2020-11-03 02:36:44.362	D Partial result: 11167/11388
2020-11-03 02:36:44.450	I [178.32.215.155:4993 OUT] 261 bytes sent for category command-1001 initiated by us
2020-11-03 02:36:44.450	D do_send_chunk() NOW SENSD: packet=294 B
2020-11-03 02:36:44.450	D [178.32.215.155:4993 OUT] LEVIN_PACKET_SENT. [len=261, flags1, r?=1, cmd = 1001, ver=1
2020-11-03 02:36:44.450	D [178.32.215.155:4993 OUT] anvoke_handler, timeout: 5000
Height: 2220823, target: 2222166 (99.9396%)
Downloading at 313 kB/s
5 peers
51.68.215.64:4238         f98b0700ba6ba0df  normal            0         2220823  13 kB/s, 0 blocks / 0 MB queued
91.194.84.78:18080        fd3faf5dcbd8fbc2  synchronizing     0         2222166  68 kB/s, 20 blocks / 0 MB queued
168.119.153.16:18080      fe3b45a12fd82317  synchronizing     0         2222166  89 kB/s, 20 blocks / 0 MB queued
178.32.215.155:4993       0000000000000000  before_handshake  0         0  0 kB/s, 0 blocks / 0 MB queued
95.85.162.67:18080        0d5851df19db7cb4  synchronizing     186       2222166  143 kB/s, 20 blocks / 1.25202 MB queued
3 spans, 1.25202 MB
[m..]
95.85.162.67:18080        20/186 (2220823 - 2220842, 1252 kB)  441 kB/s (1)
91.194.84.78:18080        20/186 (2220843 - 2220862)  -
168.119.153.16:18080      20/186 (2220863 - 2220882)  -
sync_info
2020-11-03 02:36:44.452	D Read command: sync_info
Height: 2220823, target: 2222166 (99.9396%)
Downloading at 313 kB/s
5 peers
51.68.215.64:4238         f98b0700ba6ba0df  normal            0         2220823  13 kB/s, 0 blocks / 0 MB queued
91.194.84.78:18080        fd3faf5dcbd8fbc2  synchronizing     0         2222166  68 kB/s, 20 blocks / 0 MB queued
168.119.153.16:18080      fe3b45a12fd82317  synchronizing     0         2222166  89 kB/s, 20 blocks / 0 MB queued
178.32.215.155:4993       0000000000000000  before_handshake  0         0  0 kB/s, 0 blocks / 0 MB queued
2020-11-03 02:36:44.453	I transaction wit95.85.162.67:18080        0d5851df19db7cb4  synchronizing     186       2222166  143 kB/s, 20 blocks / 1.25202 MB queued
Process 21308 stopped
* thread #17, stop reason = EXC_BAD_ACCESS (code=1, address=0x30)
    frame #0: 0x000000010069cea9 monerod`rdln::readline_buffer::sync() + 121
monerod`rdln::readline_buffer::sync:
->  0x10069cea9 <+121>: movq   0x30(%rbx), %rcx
    0x10069cead <+125>: cmpq   0x38(%rbx), %rcx
    0x10069ceb1 <+129>: je     0x10069cec0               ; <+144>
    0x10069ceb3 <+131>: leaq   0x1(%rcx), %rdx
Target 0: (monerod) stopped.
(lldb) bt
* thread #17, stop reason = EXC_BAD_ACCESS (code=1, address=0x30)
  * frame #0: 0x000000010069cea9 monerod`rdln::readline_buffer::sync() + 121
    frame #1: 0x00007fff696494e9 libc++.1.dylib`std::__1::basic_ostream<char, std::__1::char_traits<char> >::flush() + 65
    frame #2: 0x00000001008073ff monerod`el::base::DefaultLogDispatchCallback::handle(el::LogDispatchData const*) + 2511
    frame #3: 0x0000000100809a0a monerod`el::base::LogDispatcher::dispatch() + 330
    frame #4: 0x000000010080aa3c monerod`el::base::Writer::triggerDispatch() + 508
    frame #5: 0x000000010080a5e5 monerod`el::base::Writer::processDispatch() + 69
    frame #6: 0x00000001004b24c3 monerod`cryptonote::BlockchainLMDB::tx_exists(crypto::hash const&) const + 3267
    frame #7: 0x00000001004fb2fa monerod`cryptonote::Blockchain::have_tx(crypto::hash const&) const + 554
    frame #8: 0x000000010057334e monerod`cryptonote::core::handle_incoming_txs(epee::span<cryptonote::tx_blob_entry const>, epee::span<cryptonote::tx_verification_context>, cryptonote::relay_method, bool) + 1902
    frame #9: 0x00000001003d0584 monerod`cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::try_add_next_blocks(cryptonote::cryptonote_connection_context&) + 10836
    frame #10: 0x00000001003de858 monerod`cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_response_get_objects(int, epee::misc_utils::struct_init<cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request_t>&, cryptonote::cryptonote_connection_context&) + 13704
    frame #11: 0x0000000100098844 monerod`int epee::net_utils::buff_to_t_adapter<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, epee::misc_utils::struct_init<cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request_t>, cryptonote::cryptonote_connection_context, std::__1::__bind<int (cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::*)(int, epee::misc_utils::struct_init<cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request_t>&, cryptonote::cryptonote_connection_context&), cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*, std::__1::placeholders::__ph<1> const&, std::__1::placeholders::__ph<2> const&, std::__1::placeholders::__ph<3> const&> >(cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*, int, epee::span<unsigned char const>, std::__1::__bind<int (cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::*)(int, epee::misc_utils::struct_init<cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request_t>&, cryptonote::cryptonote_connection_context&), cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*, std::__1::placeholders::__ph<1> const&, std::__1::placeholders::__ph<2> const&, std::__1::placeholders::__ph<3> const&>, cryptonote::cryptonote_connection_context&) + 260
    frame #12: 0x00000001000366ff monerod`int cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_invoke_map<cryptonote::cryptonote_connection_context>(bool, int, epee::span<unsigned char const>, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >&, cryptonote::cryptonote_connection_context&, bool&) + 383
    frame #13: 0x0000000100033ae3 monerod`int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, epee::span<unsigned char const>, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&) + 515
    frame #14: 0x00000001003a05e6 monerod`nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::notify(int, epee::span<unsigned char const>, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&) + 86
    frame #15: 0x000000010040ee8b monerod`epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv(void const*, unsigned long) + 3915
    frame #16: 0x000000010042d22d monerod`epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_read(boost::system::error_code const&, unsigned long) + 845
    frame #17: 0x000000010043156f monerod`void boost::asio::detail::strand_service::dispatch<boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long> >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long>&) + 575
    frame #18: 0x00000001004312a6 monerod`void boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>::operator()<boost::system::error_code, unsigned long>(boost::system::error_code const&, unsigned long const&) + 102
    frame #19: 0x000000010043111f monerod`boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > >, boost::asio::io_context::basic_executor_type<std::__1::allocator<void>, 0u> >::do_complete(void*, boost::asio::detail::scheduler_operation*, boost::system::error_code const&, unsigned long) + 191
    frame #20: 0x0000000100430f49 monerod`void boost::asio::detail::strand_service::dispatch<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > >&) + 489
    frame #21: 0x0000000100430b5d monerod`void boost::asio::detail::handler_work<boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::asio::execution::any_executor<boost::asio::execution::context_as_t<boost::asio::execution_context&>, boost::asio::execution::detail::blocking::never_t<0>, boost::asio::execution::prefer_only<boost::asio::execution::detail::blocking::possibly_t<0> >, boost::asio::execution::prefer_only<boost::asio::execution::detail::outstanding_work::tracked_t<0> >, boost::asio::execution::prefer_only<boost::asio::execution::detail::outstanding_work::untracked_t<0> >, boost::asio::execution::prefer_only<boost::asio::execution::detail::relationship::fork_t<0> >, boost::asio::execution::prefer_only<boost::asio::execution::detail::relationship::continuation_t<0> > >, void>::complete<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long> >(boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>&, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>&) + 189
    frame #22: 0x00000001004308f5 monerod`boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::asio::execution::any_executor<boost::asio::execution::context_as_t<boost::asio::execution_context&>, boost::asio::execution::detail::blocking::never_t<0>, boost::asio::execution::prefer_only<boost::asio::execution::detail::blocking::possibly_t<0> >, boost::asio::execution::prefer_only<boost::asio::execution::detail::outstanding_work::tracked_t<0> >, boost::asio::execution::prefer_only<boost::asio::execution::detail::outstanding_work::untracked_t<0> >, boost::asio::execution::prefer_only<boost::asio::execution::detail::relationship::fork_t<0> >, boost::asio::execution::prefer_only<boost::asio::execution::detail::relationship::continuation_t<0> > > >::do_complete(void*, boost::asio::detail::scheduler_operation*, boost::system::error_code const&, unsigned long) + 277
    frame #23: 0x00000001000b3683 monerod`boost::asio::detail::scheduler::do_run_one(boost::asio::detail::conditionally_enabled_mutex::scoped_lock&, boost::asio::detail::scheduler_thread_info&, boost::system::error_code const&) + 739
    frame #24: 0x00000001000b3261 monerod`boost::asio::detail::scheduler::run(boost::system::error_code&) + 289
    frame #25: 0x0000000100404421 monerod`epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() + 465
    frame #26: 0x00000001017b1bf8 libboost_thread-mt.dylib`boost::(anonymous namespace)::thread_proxy(void*) + 136
    frame #27: 0x00007fff6c578109 libsystem_pthread.dylib`_pthread_start + 148
    frame #28: 0x00007fff6c573b8b libsystem_pthread.dylib`thread_start + 15
```

# Action History
- Created by: moneromooo-monero | 2018-05-13T13:17:15+00:00
- Closed at: 2020-11-29T07:55:24+00:00
