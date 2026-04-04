---
title: 'readline: crash on exit when late logs are printed'
source_url: https://github.com/monero-project/monero/issues/2217
author: moneromooo-monero
assignees: []
labels: []
created_at: '2017-07-28T09:06:21+00:00'
updated_at: '2017-10-15T13:30:21+00:00'
type: issue
status: closed
closed_at: '2017-10-15T13:30:21+00:00'
---

# Original Description
I had typed "exit", and monerod was exiting:
```
ASAN:SIGSEGV
=================================================================
==29973==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000028 (pc 0x7fc8248d0bb0 bp 0x7fc7da1d5850 sp 0x7fc7da1d5840 T6)
    #0 0x7fc8248d0baf in std::basic_streambuf<char, std::char_traits<char> >::pptr() const /usr/include/c++/5/streambuf:532
    #1 0x7fc8248d0baf in std::basic_streambuf<char, std::char_traits<char> >::sputc(char) /usr/include/c++/5/streambuf:427
    #2 0x7fc8248d0baf in rdln::readline_buffer::sync() /home/moneromooo/monero/contrib/epee/src/readline_buffer.cpp:120
    #3 0x7fc823dcbe3d in std::ostream::flush() (/usr/lib/x86_64-linux-gnu/libstdc++.so.6+0x10de3d)
    #4 0x7fc824301dd7 in el::base::DefaultLogDispatchCallback::dispatch(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&&) /home/moneromooo/monero/external/easylogging++/easylogging++.cc:2222
    #5 0x7fc824301768 in el::base::DefaultLogDispatchCallback::handle(el::LogDispatchData const*) /home/moneromooo/monero/external/easylogging++/easylogging++.cc:2191
    #6 0x7fc824303522 in el::base::LogDispatcher::dispatch() /home/moneromooo/monero/external/easylogging++/easylogging++.cc:2472
    #7 0x7fc824304eb7 in el::base::Writer::triggerDispatch() /home/moneromooo/monero/external/easylogging++/easylogging++.cc:2602
    #8 0x7fc8243048b9 in el::base::Writer::processDispatch() /home/moneromooo/monero/external/easylogging++/easylogging++.cc:2585
    #9 0x5d4ab5 in cryptonote::cryptonote_connection_context::~cryptonote_connection_context() (/home/moneromooo/monero/build/debug/bin/monerod+0x5d4ab5)
    #10 0x77ee19 in epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::~connection() (/home/moneromooo/monero/build/debug/bin/monerod+0x77ee19)
    #11 0x77f07e in epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::~connection() (/home/moneromooo/monero/build/debug/bin/monerod+0x77f07e)
    #12 0x57fe71 in void boost::checked_delete<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > >(epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*) /usr/include/boost/core/checked_delete.hpp:34
    #13 0x57fe71 in boost::detail::sp_counted_impl_p<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > >::dispose() /usr/include/boost/smart_ptr/detail/sp_counted_impl.hpp:78
    #14 0x550b3f in boost::detail::sp_counted_base::release() /usr/include/boost/smart_ptr/detail/sp_counted_base_gcc_x86.hpp:146
    #15 0x5e782f in std::deque<std::pair<boost::posix_time::ptime, boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, std::allocator<std::pair<boost::posix_time::ptime, boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > > > >::_M_destroy_data_aux(std::_Deque_iterator<std::pair<boost::posix_time::ptime, boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, std::pair<boost::posix_time::ptime, boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >&, std::pair<boost::posix_time::ptime, boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >*>, std::_Deque_iterator<std::pair<boost::posix_time::ptime, boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, std::pair<boost::posix_time::ptime, boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >&, std::pair<boost::posix_time::ptime, boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >*>) (/home/moneromooo/monero/build/debug/bin/monerod+0x5e782f)
    #16 0x5e7b77 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::send_stop_signal() (/home/moneromooo/monero/build/debug/bin/monerod+0x5e7b77)
    #17 0x5e809b in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::send_stop_signal() (/home/moneromooo/monero/build/debug/bin/monerod+0x5e809b)
    #18 0x576419 in daemonize::t_daemon::stop_p2p() /home/moneromooo/monero/src/daemon/daemon.cpp:178
    #19 0x57d1c0 in std::_Function_handler<void (), std::_Bind<std::_Mem_fn<void (daemonize::t_daemon::*)()> (daemonize::t_daemon*)> >::_M_invoke(std::_Any_data const&) (/home/moneromooo/monero/build/debug/bin/monerod+0x57d1c0)
    #20 0x562a91 in std::function<void ()>::operator()() const /usr/include/c++/5/functional:2267
    #21 0x56c8fa in bool epee::async_console_handler::run<bool epee::async_console_handler::run<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > > >(boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()>)::{lambda(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)#1}>(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, bool epee::async_console_handler::run<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > > >(boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()>)::{lambda(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)#1} const&, std::function<void ()>) /home/moneromooo/monero/contrib/epee/include/console_handler.h:390
    #22 0x56cd8a in bool epee::async_console_handler::run<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > > >(boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()>) /home/moneromooo/monero/contrib/epee/include/console_handler.h:304
    #23 0x56cd8a in epee::console_handlers_binder::run_handling(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()>) /home/moneromooo/monero/contrib/epee/include/console_handler.h:533
    #24 0x560938 in boost::_mfi::mf3<bool, epee::console_handlers_binder, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()> >::operator()(epee::console_handlers_binder*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()>) const /usr/include/boost/bind/mem_fn_template.hpp:393
    #25 0x560938 in bool boost::_bi::list4<boost::_bi::value<epee::console_handlers_binder*>, boost::_bi::value<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, boost::_bi::value<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, boost::_bi::value<std::function<void ()> > >::operator()<bool, boost::_mfi::mf3<bool, epee::console_handlers_binder, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()> >, boost::_bi::list0>(boost::_bi::type<bool>, boost::_mfi::mf3<bool, epee::console_handlers_binder, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()> >&, boost::_bi::list0&, long) /usr/include/boost/bind/bind.hpp:447
    #26 0x560938 in boost::_bi::bind_t<bool, boost::_mfi::mf3<bool, epee::console_handlers_binder, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()> >, boost::_bi::list4<boost::_bi::value<epee::console_handlers_binder*>, boost::_bi::value<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, boost::_bi::value<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, boost::_bi::value<std::function<void ()> > > >::operator()() /usr/include/boost/bind/bind.hpp:893
    #27 0x560938 in boost::detail::thread_data<boost::_bi::bind_t<bool, boost::_mfi::mf3<bool, epee::console_handlers_binder, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()> >, boost::_bi::list4<boost::_bi::value<epee::console_handlers_binder*>, boost::_bi::value<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, boost::_bi::value<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, boost::_bi::value<std::function<void ()> > > > >::run() /usr/include/boost/thread/detail/thread.hpp:116
    #28 0x7fc8240515d4  (/usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0+0x115d4)
    #29 0x7fc8235896b9 in start_thread (/lib/x86_64-linux-gnu/libpthread.so.0+0x76b9)
    #30 0x7fc8232bf82c in clone (/lib/x86_64-linux-gnu/libc.so.6+0x10682c)

AddressSanitizer can not provide additional info.
SUMMARY: AddressSanitizer: SEGV /usr/include/c++/5/streambuf:532 std::basic_streambuf<char, std::char_traits<char> >::pptr() const
Thread T6 created by T0 here:
    #0 0x7fc826c05253 in pthread_create (/usr/lib/x86_64-linux-gnu/libasan.so.2+0x36253)
    #1 0x7fc8240502e8 in boost::thread::start_thread_noexcept() (/usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0+0x102e8)
    #2 0x55d1f4 in daemonize::t_command_server::start_handling(std::function<void ()>) /home/moneromooo/monero/src/daemon/command_server.cpp:282
    #3 0x8775cf  (/home/moneromooo/monero/build/debug/bin/monerod+0x8775cf)

==29973==ABORTING
```

# Discussion History
## moneromooo-monero | 2017-07-28T09:09:32+00:00
Note: this is when logging something in the cryptonote_connection_context, which happens late I guess. That log is just a raw string, so no accessing bad data.

With stock code, it also happens when running with --log-level *:DEBUG, making it impossible to debug leaks with non trivial debug traces.

As a stopgap, a simple (if (m_cout_buf = NULL) break; avoids the crash so I can debug.

## jtgrassie | 2017-07-28T12:19:49+00:00
I _think_ what maybe happening is that `readline_buffer::stop` is being called while there is a `readline_buffer::sync` happening. Not yet found how / where this is able to happen as they should be on the same thread and the stack trace isn't showing this.

## moneromooo-monero | 2017-07-28T16:30:24+00:00
BTW, there's a race bug in console_handler itself, which I will fix. It might be that the readline stuff is being a secondary victim to this.

## moneromooo-monero | 2017-07-28T18:20:20+00:00
Doesn't seem to be related. I can't reproduce that console_handler race.

## jtgrassie | 2017-07-28T18:32:49+00:00
So I'm thinking of putting an extra mutex & lock on stop and sync but my concern is this may block exiting in a timely manner if there's a lot of logging occurring when trying to stop and exit. 


## moneromooo-monero | 2017-07-29T17:28:35+00:00
If you build with tsan (-fsanitize=thread), the readline code lights up. Should help see what's racy.

## moneromooo-monero | 2017-08-07T23:32:06+00:00
With current master, valgrind finds this:
```
==10458== Thread 10:
==10458== Invalid read of size 8
==10458==    at 0x994BEB0: std::basic_streambuf<char, std::char_traits<char> >::sputc(char) (in /usr/lib64/libstdc++.so.6.0.22)
==10458==    by 0x8974E46: rdln::readline_buffer::sync() (readline_buffer.cpp:120)
==10458==    by 0x993ABCD: std::ostream::flush() (in /usr/lib64/libstdc++.so.6.0.22)
==10458==    by 0x8EB0718: el::base::DefaultLogDispatchCallback::dispatch(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&&) (easylogging++.cc:2222)
==10458==    by 0x8EB03ED: el::base::DefaultLogDispatchCallback::handle(el::LogDispatchData const*) (easylogging++.cc:2191)
==10458==    by 0x8EB18AA: el::base::LogDispatcher::dispatch() (easylogging++.cc:2472)
==10458==    by 0x8EB25FB: el::base::Writer::triggerDispatch() (easylogging++.cc:2602)
==10458==    by 0x8EB23C7: el::base::Writer::processDispatch() (easylogging++.cc:2585)
==10458==    by 0xA00BBF: el::base::Writer::~Writer() (easylogging++.h:3265)
==10458==    by 0xB3D9D1: epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::~connection() (abstract_tcp_server2.inl:98)
==10458==    by 0xB3DC19: epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::~connection() (abstract_tcp_server2.inl:99)
==10458==    by 0xB3634E: void boost::checked_delete<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > >(epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*) (checked_delete.hpp:34)
==10458==  Address 0x28 is not stack'd, malloc'd or (recently) free'd
==10458== 
==10458== 
==10458== Process terminating with default action of signal 11 (SIGSEGV): dumping core
==10458==  Access not within mapped region at address 0x28
==10458==    at 0x994BEB0: std::basic_streambuf<char, std::char_traits<char> >::sputc(char) (in /usr/lib64/libstdc++.so.6.0.22)
==10458==    by 0x8974E46: rdln::readline_buffer::sync() (readline_buffer.cpp:120)
==10458==    by 0x993ABCD: std::ostream::flush() (in /usr/lib64/libstdc++.so.6.0.22)
==10458==    by 0x8EB0718: el::base::DefaultLogDispatchCallback::dispatch(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&&) (easylogging++.cc:2222)
==10458==    by 0x8EB03ED: el::base::DefaultLogDispatchCallback::handle(el::LogDispatchData const*) (easylogging++.cc:2191)
==10458==    by 0x8EB18AA: el::base::LogDispatcher::dispatch() (easylogging++.cc:2472)
==10458==    by 0x8EB25FB: el::base::Writer::triggerDispatch() (easylogging++.cc:2602)
==10458==    by 0x8EB23C7: el::base::Writer::processDispatch() (easylogging++.cc:2585)
==10458==    by 0xA00BBF: el::base::Writer::~Writer() (easylogging++.h:3265)
==10458==    by 0xB3D9D1: epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::~connection() (abstract_tcp_server2.inl:98)
==10458==    by 0xB3DC19: epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::~connection() (abstract_tcp_server2.inl:99)
==10458==    by 0xB3634E: void boost::checked_delete<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > >(epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*) (checked_delete.hpp:34)
==10458==  If you believe this happened as a result of a stack
==10458==  overflow in your program's main thread (unlikely but
==10458==  possible), you can try to increase the size of the
==10458==  main thread stack using the --main-stacksize= flag.
==10458==  The main thread stack size used in this run was 8388608.
```

## jtgrassie | 2017-08-16T13:41:39+00:00
#2301 should fix this

## moneromooo-monero | 2017-10-15T13:21:44+00:00
I've not seen that for a long time now.

+resolved

# Action History
- Created by: moneromooo-monero | 2017-07-28T09:06:21+00:00
- Closed at: 2017-10-15T13:30:21+00:00
