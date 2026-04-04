---
title: Rare race on exit in console_handler
source_url: https://github.com/monero-project/monero/issues/2296
author: moneromooo-monero
assignees: []
labels:
- bug
created_at: '2017-08-15T15:24:13+00:00'
updated_at: '2020-01-17T01:32:42+00:00'
type: issue
status: closed
closed_at: '2020-01-17T01:32:42+00:00'
---

# Original Description
Note the odd location of both threads 1 and 6 in src/daemon/daemon.cpp:127.
```
(gdb) thread apply all bt

Thread 6 (Thread 0x7fc705810700 (LWP 21060)):
#0  0x00007fc74e960460 in pthread_cond_wait@@GLIBC_2.3.2 () from /lib64/libpthread.so.0
#1  0x0000000000a6423c in boost::condition_variable::wait (this=0x3b48128, m=...)
    at /home/user/boost_1_59_0/boost/thread/pthread/condition_variable.hpp:73
#2  0x0000000000a64b23 in epee::async_stdin_reader::get_line (this=0x3b47fc0, line="")
    at /home/user/src/bitmonero/contrib/epee/include/console_handler.h:86
#3  0x0000000000a69f2c in epee::async_console_handler::run<bool epee::async_console_handler::run<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > > >(boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()>)::{lambda(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)#1}>(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, bool epee::async_console_handler::run<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > > >(boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()>)::{lambda(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)#1} const&, std::function<void ()>) (this=0x3b47fc0, 
    prompt="", 
    usage="Monero 'Wolfram Warptangent' (v0.10.3.1-14ec6ed)\nCommands: \n  alt_chain_info          Print information about alternative chains\n  ban", ' ' <repeats 21 times>, "Ban a given IP for a time\n  bans", ' ' <repeats 13 times>..., cmd_handler=..., exit_handler=...)
    at /home/user/src/bitmonero/contrib/epee/include/console_handler.h:351
#4  0x0000000000a678a9 in epee::async_console_handler::run<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > > >(boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()>) (this=0x3b47fc0, ch_handler=..., prompt="", 
    usage="Monero 'Wolfram Warptangent' (v0.10.3.1-14ec6ed)\nCommands: \n  alt_chain_info          Print information about alternative chains\n  ban", ' ' <repeats 21 times>, "Ban a given IP for a time\n  bans", ' ' <repeats 13 times>..., exit_handler=...)
    at /home/user/src/bitmonero/contrib/epee/include/console_handler.h:304
#5  0x0000000000a65a2c in epee::console_handlers_binder::run_handling(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()>) (
    this=0x3b47f88, prompt="", 
    usage_string="Monero 'Wolfram Warptangent' (v0.10.3.1-14ec6ed)\nCommands: \n  alt_chain_info          Print information about alternativ---Type <return> to continue, or q <return> to quit---
e chains\n  ban", ' ' <repeats 21 times>, "Ban a given IP for a time\n  bans", ' ' <repeats 13 times>..., exit_handler=...)
    at /home/user/src/bitmonero/contrib/epee/include/console_handler.h:533
#6  0x0000000000a77810 in boost::_mfi::mf3<bool, epee::console_handlers_binder, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()> >::operator()(epee::console_handlers_binder*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()>) const (this=0x3b69358, 
    p=0x3b47f88, a1="", 
    a2="Monero 'Wolfram Warptangent' (v0.10.3.1-14ec6ed)\nCommands: \n  alt_chain_info          Print information about alternative chains\n  ban", ' ' <repeats 21 times>, "Ban a given IP for a time\n  bans", ' ' <repeats 13 times>..., a3=...)
    at /home/user/boost_1_59_0/boost/bind/mem_fn_template.hpp:393
#7  0x0000000000a7765d in boost::_bi::list4<boost::_bi::value<epee::console_handlers_binder*>, boost::_bi::value<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, boost::_bi::value<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, boost::_bi::value<std::function<void ()> > >::operator()<bool, boost::_mfi::mf3<bool, epee::console_handlers_binder, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()> >, boost::_bi::list0>(boost::_bi::type<bool>, boost::_mfi::mf3<bool, epee::console_handlers_binder, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()> >&, boost::_bi::list0&, long) (this=0x3b69368, f=..., a=...)
    at /home/user/boost_1_59_0/boost/bind/bind.hpp:449
#8  0x0000000000a7730d in boost::_bi::bind_t<bool, boost::_mfi::mf3<bool, epee::console_handlers_binder, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()> >, boost::_bi::list4<boost::_bi::value<epee::console_handlers_binder*>, boost::_bi::value<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, boost::_bi::value<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, boost::_bi::value<std::function<void ()> > > >::operator()() (this=0x3b69358)
    at /home/user/boost_1_59_0/boost/bind/bind.hpp:895
#9  0x0000000000a76fec in boost::detail::thread_data<boost::_bi::bind_t<bool, boost::_mfi::mf3<bool, epee::console_handlers_binder, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()> >, boost::_bi::list4<boost::_bi::value<epee::console_handlers_binder*>, boost::_bi::value<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, boost::_bi::value<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, boost::_bi::value<std::function<void ()> > > > >::run() (this=0x3b691a0)
    at /home/user/boost_1_59_0/boost/thread/detail/thread.hpp:116
#10 0x00007fc74f429adf in thread_proxy () from /home/user/boost_1_59_install/lib/libboost_thread.so.1.59.0
#11 0x00007fc74e95a73a in start_thread () from /lib64/libpthread.so.0
#12 0x00007fc74e694e0f in clone () from /lib64/libc.so.6

Thread 5 (Thread 0x7fc708015700 (LWP 21055)):
#0  0x00007fc74e960460 in pthread_cond_wait@@GLIBC_2.3.2 () from /lib64/libpthread.so.0
#1  0x0000000000aa06ad in boost::asio::detail::posix_event::wait<boost::asio::detail::scoped_lock<boost::asio::detail::posix_mutex> > (
    this=0x3b19f58, lock=...) at /home/user/boost_1_59_0/boost/asio/detail/posix_event.hpp:106
---Type <return> to continue, or q <return> to quit---
#2  0x0000000000a8c049 in boost::asio::detail::task_io_service::do_run_one (this=0x3b19f00, lock=..., this_thread=..., ec=...)
    at /home/user/boost_1_59_0/boost/asio/detail/impl/task_io_service.ipp:380
#3  0x0000000000a8b848 in boost::asio::detail::task_io_service::run (this=0x3b19f00, ec=...)
    at /home/user/boost_1_59_0/boost/asio/detail/impl/task_io_service.ipp:149
#4  0x0000000000a8c4f9 in boost::asio::io_service::run (this=0x3b18908) at /home/user/boost_1_59_0/boost/asio/impl/io_service.ipp:59
#5  0x00007fc752c09c8d in boost::_mfi::mf0<unsigned long, boost::asio::io_service>::operator() (this=0x3b43578, p=0x3b18908)
    at /home/user/boost_1_59_0/boost/bind/mem_fn_template.hpp:49
#6  0x00007fc752c09b2b in boost::_bi::list1<boost::_bi::value<boost::asio::io_service*> >::operator()<unsigned long, boost::_mfi::mf0<unsigned long, boost::asio::io_service>, boost::_bi::list0> (this=0x3b43588, f=..., a=...) at /home/user/boost_1_59_0/boost/bind/bind.hpp:245
#7  0x00007fc752c09157 in boost::_bi::bind_t<unsigned long, boost::_mfi::mf0<unsigned long, boost::asio::io_service>, boost::_bi::list1<boost::_bi::value<boost::asio::io_service*> > >::operator() (this=0x3b43578) at /home/user/boost_1_59_0/boost/bind/bind.hpp:895
#8  0x00007fc752c085a6 in boost::detail::thread_data<boost::_bi::bind_t<unsigned long, boost::_mfi::mf0<unsigned long, boost::asio::io_service>, boost::_bi::list1<boost::_bi::value<boost::asio::io_service*> > > >::run (this=0x3b433c0)
    at /home/user/boost_1_59_0/boost/thread/detail/thread.hpp:116
#9  0x00007fc74f429adf in thread_proxy () from /home/user/boost_1_59_install/lib/libboost_thread.so.1.59.0
#10 0x00007fc74e95a73a in start_thread () from /lib64/libpthread.so.0
#11 0x00007fc74e694e0f in clone () from /lib64/libc.so.6

Thread 4 (Thread 0x7fc748a17700 (LWP 21054)):
#0  0x00007fc74e960460 in pthread_cond_wait@@GLIBC_2.3.2 () from /lib64/libpthread.so.0
#1  0x0000000000a6423c in boost::condition_variable::wait (this=0x3b19200, m=...)
    at /home/user/boost_1_59_0/boost/thread/pthread/condition_variable.hpp:73
#2  0x00007fc750260740 in boost::condition_variable::wait<tools::thread_group::data::run()::<lambda()> >(boost::unique_lock<boost::mutex> &, tools::thread_group::data::<lambda()>) (this=0x3b19200, m=..., pred=...)
    at /home/user/boost_1_59_0/boost/thread/pthread/condition_variable_fwd.hpp:94
#3  0x00007fc750260489 in tools::thread_group::data::run (this=0x3b191d8) at /home/user/src/bitmonero/src/common/thread_group.cpp:125
#4  0x00007fc7502627f9 in boost::_mfi::mf0<void, tools::thread_group::data>::operator() (this=0x3b1dfa8, p=0x3b191d8)
    at /home/user/boost_1_59_0/boost/bind/mem_fn_template.hpp:49
#5  0x00007fc75026275c in boost::_bi::list1<boost::_bi::value<tools::thread_group::data*> >::operator()<boost::_mfi::mf0<void, tools::thread_group::data>, boost::_bi::list0> (this=0x3b1dfb8, f=..., a=...) at /home/user/boost_1_59_0/boost/bind/bind.hpp:255
#6  0x00007fc750262707 in boost::_bi::bind_t<void, boost::_mfi::mf0<void, tools::thread_group::data>, boost::_bi::list1<boost::_bi::value<tools::thread_group::data*> > >::operator() (this=0x3b1dfa8) at /home/user/boost_1_59_0/boost/bind/bind.hpp:895
#7  0x00007fc7502626c8 in boost::detail::thread_data<boost::_bi::bind_t<void, boost::_mfi::mf0<void, tools::thread_group::data>, boost::_bi::list1<boost::_bi::value<tools::thread_group::data*> > > >::run (this=0x3b1ddf0)
    at /home/user/boost_1_59_0/boost/thread/detail/thread.hpp:116
#8  0x00007fc74f429adf in thread_proxy () from /home/user/boost_1_59_install/lib/libboost_thread.so.1.59.0
#9  0x00007fc74e95a73a in start_thread () from /lib64/libpthread.so.0
#10 0x00007fc74e694e0f in clone () from /lib64/libc.so.6
---Type <return> to continue, or q <return> to quit---

Thread 3 (Thread 0x7fc749218700 (LWP 21053)):
#0  0x00007fc74e960460 in pthread_cond_wait@@GLIBC_2.3.2 () from /lib64/libpthread.so.0
#1  0x0000000000a6423c in boost::condition_variable::wait (this=0x3b19200, m=...)
    at /home/user/boost_1_59_0/boost/thread/pthread/condition_variable.hpp:73
#2  0x00007fc750260740 in boost::condition_variable::wait<tools::thread_group::data::run()::<lambda()> >(boost::unique_lock<boost::mutex> &, tools::thread_group::data::<lambda()>) (this=0x3b19200, m=..., pred=...)
    at /home/user/boost_1_59_0/boost/thread/pthread/condition_variable_fwd.hpp:94
#3  0x00007fc750260489 in tools::thread_group::data::run (this=0x3b191d8) at /home/user/src/bitmonero/src/common/thread_group.cpp:125
#4  0x00007fc7502627f9 in boost::_mfi::mf0<void, tools::thread_group::data>::operator() (this=0x3b1dbf8, p=0x3b191d8)
    at /home/user/boost_1_59_0/boost/bind/mem_fn_template.hpp:49
#5  0x00007fc75026275c in boost::_bi::list1<boost::_bi::value<tools::thread_group::data*> >::operator()<boost::_mfi::mf0<void, tools::thread_group::data>, boost::_bi::list0> (this=0x3b1dc08, f=..., a=...) at /home/user/boost_1_59_0/boost/bind/bind.hpp:255
#6  0x00007fc750262707 in boost::_bi::bind_t<void, boost::_mfi::mf0<void, tools::thread_group::data>, boost::_bi::list1<boost::_bi::value<tools::thread_group::data*> > >::operator() (this=0x3b1dbf8) at /home/user/boost_1_59_0/boost/bind/bind.hpp:895
#7  0x00007fc7502626c8 in boost::detail::thread_data<boost::_bi::bind_t<void, boost::_mfi::mf0<void, tools::thread_group::data>, boost::_bi::list1<boost::_bi::value<tools::thread_group::data*> > > >::run (this=0x3b1da40)
    at /home/user/boost_1_59_0/boost/thread/detail/thread.hpp:116
#8  0x00007fc74f429adf in thread_proxy () from /home/user/boost_1_59_install/lib/libboost_thread.so.1.59.0
#9  0x00007fc74e95a73a in start_thread () from /lib64/libpthread.so.0
#10 0x00007fc74e694e0f in clone () from /lib64/libc.so.6

Thread 2 (Thread 0x7fc749a19700 (LWP 21052)):
#0  0x00007fc74e960460 in pthread_cond_wait@@GLIBC_2.3.2 () from /lib64/libpthread.so.0
#1  0x0000000000a6423c in boost::condition_variable::wait (this=0x3b19200, m=...)
    at /home/user/boost_1_59_0/boost/thread/pthread/condition_variable.hpp:73
#2  0x00007fc750260740 in boost::condition_variable::wait<tools::thread_group::data::run()::<lambda()> >(boost::unique_lock<boost::mutex> &, tools::thread_group::data::<lambda()>) (this=0x3b19200, m=..., pred=...)
    at /home/user/boost_1_59_0/boost/thread/pthread/condition_variable_fwd.hpp:94
#3  0x00007fc750260489 in tools::thread_group::data::run (this=0x3b191d8) at /home/user/src/bitmonero/src/common/thread_group.cpp:125
#4  0x00007fc7502627f9 in boost::_mfi::mf0<void, tools::thread_group::data>::operator() (this=0x3b1d868, p=0x3b191d8)
    at /home/user/boost_1_59_0/boost/bind/mem_fn_template.hpp:49
#5  0x00007fc75026275c in boost::_bi::list1<boost::_bi::value<tools::thread_group::data*> >::operator()<boost::_mfi::mf0<void, tools::thread_group::data>, boost::_bi::list0> (this=0x3b1d878, f=..., a=...) at /home/user/boost_1_59_0/boost/bind/bind.hpp:255
#6  0x00007fc750262707 in boost::_bi::bind_t<void, boost::_mfi::mf0<void, tools::thread_group::data>, boost::_bi::list1<boost::_bi::value<tools::thread_group::data*> > >::operator() (this=0x3b1d868) at /home/user/boost_1_59_0/boost/bind/bind.hpp:895
#7  0x00007fc7502626c8 in boost::detail::thread_data<boost::_bi::bind_t<void, boost::_mfi::mf0<void, tools::thread_group::data>, boost::_bi::list1<boost::_bi::value<tools::thread_group::data*> > > >::run (this=0x3b1d6b0)
---Type <return> to continue, or q <return> to quit---
    at /home/user/boost_1_59_0/boost/thread/detail/thread.hpp:116
#8  0x00007fc74f429adf in thread_proxy () from /home/user/boost_1_59_install/lib/libboost_thread.so.1.59.0
#9  0x00007fc74e95a73a in start_thread () from /lib64/libpthread.so.0
#10 0x00007fc74e694e0f in clone () from /lib64/libc.so.6

Thread 1 (Thread 0x7fc753ff6880 (LWP 21051)):
#0  0x00007fc74e5c28df in raise () from /lib64/libc.so.6
#1  0x00007fc74e5c44da in abort () from /lib64/libc.so.6
#2  0x00007fc74e5bad67 in __assert_fail_base () from /lib64/libc.so.6
#3  0x00007fc74e5bae12 in __assert_fail () from /lib64/libc.so.6
#4  0x0000000000a63c96 in boost::condition_variable::~condition_variable (this=0x3b48128, __in_chrg=<optimized out>)
    at /home/user/boost_1_59_0/boost/thread/pthread/condition_variable_fwd.hpp:81
#5  0x0000000000a64a10 in epee::async_stdin_reader::~async_stdin_reader (this=0x3b47fc0, __in_chrg=<optimized out>)
    at /home/user/src/bitmonero/contrib/epee/include/console_handler.h:63
#6  0x0000000000a65bd4 in epee::async_console_handler::~async_console_handler (this=0x3b47fc0, __in_chrg=<optimized out>)
    at /home/user/src/bitmonero/contrib/epee/include/console_handler.h:288
#7  0x0000000000a65c60 in epee::console_handlers_binder::~console_handlers_binder (this=0x3b47f88, __in_chrg=<optimized out>)
    at /home/user/src/bitmonero/contrib/epee/include/console_handler.h:512
#8  0x0000000000ad9fea in daemonize::t_command_server::~t_command_server (this=0x3b47f70, __in_chrg=<optimized out>)
    at /home/user/src/bitmonero/src/daemon/command_server.h:49
#9  0x0000000000ada01c in std::default_delete<daemonize::t_command_server>::operator() (this=0x7ffc82f902e0, __ptr=0x3b47f70)
    at /usr/include/c++/6.3.1/bits/unique_ptr.h:76
#10 0x0000000000abce67 in std::unique_ptr<daemonize::t_command_server, std::default_delete<daemonize::t_command_server> >::~unique_ptr (
    this=0x7ffc82f902e0, __in_chrg=<optimized out>) at /usr/include/c++/6.3.1/bits/unique_ptr.h:239
#11 0x0000000000a78118 in daemonize::t_daemon::run (this=0x7ffc82f90570, interactive=true)
    at /home/user/src/bitmonero/src/daemon/daemon.cpp:127
#12 0x0000000000bd50cb in daemonize::t_executor::run_interactive (this=0x7ffc82f91587, vm=...)
    at /home/user/src/bitmonero/src/daemon/executor.cpp:77
#13 0x0000000000be2be0 in daemonizer::daemonize<daemonize::t_executor>(int, char const**, daemonize::t_executor&&, boost::program_options::variables_map const&) (argc=17, argv=0x7ffc82f917a8, 
    executor=<unknown type in /home/user/src/bitmonero/build/debug/bin/monerod, CU 0x6f9634, DIE 0x875023>, vm=...)
    at /home/user/src/bitmonero/src/daemonizer/posix_daemonizer.inl:104
#14 0x0000000000bd6d75 in main (argc=17, argv=0x7ffc82f917a8) at /home/user/src/bitmonero/src/daemon/main.cpp:286
```

# Discussion History
## dEBRUYNE-1 | 2018-01-08T12:30:53+00:00
+bug

## moneromooo-monero | 2019-11-12T11:07:29+00:00
I got another crash on exit in the readline handler. I did not keep the stack trace but it was one I'd seen before.

# Action History
- Created by: moneromooo-monero | 2017-08-15T15:24:13+00:00
- Closed at: 2020-01-17T01:32:42+00:00
