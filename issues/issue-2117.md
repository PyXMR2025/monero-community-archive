---
title: 'monero-wallet-cli: hang on exit in readline code'
source_url: https://github.com/monero-project/monero/issues/2117
author: moneromooo-monero
assignees: []
labels: []
created_at: '2017-06-25T14:49:45+00:00'
updated_at: '2017-09-20T21:42:22+00:00'
type: issue
status: closed
closed_at: '2017-09-20T21:00:51+00:00'
---

# Original Description
After typing exit+enter. It is rare:

Thread 4 (Thread 0x7fc825a5a700 (LWP 5206)):
#0  0x00007fc829e9f590 in pthread_cond_wait@@GLIBC_2.3.2 () from /lib64/libpthread.so.0
#1  0x0000000000d22b79 in boost::condition_variable::wait(boost::unique_lock<boost::mutex>&) ()
#2  0x0000000000d3ab07 in epee::async_stdin_reader::wait_read() ()
#3  0x0000000000d3ad03 in epee::async_stdin_reader::reader_thread_func() ()
#4  0x0000000000e50947 in void std::_Mem_fn<void (epee::async_stdin_reader::*)()>::operator()<, void>(epee::async_stdin_reader*) const ()
#5  0x0000000000e4faa2 in void std::_Bind<std::_Mem_fn<void (epee::async_stdin_reader::*)()> (epee::async_stdin_reader*)>::__call<void, , 0
#6  0x0000000000e4de16 in void std::_Bind<std::_Mem_fn<void (epee::async_stdin_reader::*)()> (epee::async_stdin_reader*)>::operator()<, voi
#7  0x0000000000e48d24 in boost::detail::thread_data<std::_Bind<std::_Mem_fn<void (epee::async_stdin_reader::*)()> (epee::async_stdin_reade
#8  0x00007fc82bd979da in thread_proxy () from /home/user/boost_1_59_install/lib/libboost_thread.so.1.59.0
#9  0x00007fc829e9a52a in start_thread () from /lib64/libpthread.so.0
#10 0x00007fc829bd622d in clone () from /lib64/libc.so.6
Thread 3 (Thread 0x7fc81ece6700 (LWP 5207)):
#0  0x00007fc829bccae3 in select () from /lib64/libc.so.6
#1  0x00000000011b040c in process_input() ()
#2  0x00000000011b025f in rdln::readline_buffer::process() ()
#3  0x0000000000d3acce in epee::async_stdin_reader::readline_thread_func() ()
#4  0x0000000000e50947 in void std::_Mem_fn<void (epee::async_stdin_reader::*)()>::operator()<, void>(epee::async_stdin_reader*) const ()
#5  0x0000000000e4faa2 in void std::_Bind<std::_Mem_fn<void (epee::async_stdin_reader::*)()> (epee::async_stdin_reader*)>::__call<void, , 0
#6  0x0000000000e4de16 in void std::_Bind<std::_Mem_fn<void (epee::async_stdin_reader::*)()> (epee::async_stdin_reader*)>::operator()<, voi
#7  0x0000000000e48d24 in boost::detail::thread_data<std::_Bind<std::_Mem_fn<void (epee::async_stdin_reader::*)()> (epee::async_stdin_reade
#8  0x00007fc82bd979da in thread_proxy () from /home/user/boost_1_59_install/lib/libboost_thread.so.1.59.0
#9  0x00007fc829e9a52a in start_thread () from /lib64/libpthread.so.0
#10 0x00007fc829bd622d in clone () from /lib64/libc.so.6
Thread 2 (Thread 0x7fc81e0d7700 (LWP 5208)):
#0  0x00007fc829e9f939 in pthread_cond_timedwait@@GLIBC_2.3.2 () from /lib64/libpthread.so.0
#1  0x0000000000d22c87 in boost::condition_variable::do_wait_until(boost::unique_lock<boost::mutex>&, timespec const&) ()
#2  0x0000000000d22607 in boost::condition_variable::wait_until(boost::unique_lock<boost::mutex>&, boost::chrono::time_point<boost::chrono:
#3  0x0000000000d501a7 in boost::cv_status boost::condition_variable::wait_for<long, boost::ratio<1l, 1l> >(boost::unique_lock<boost::mutex
#4  0x0000000000d0fd67 in cryptonote::simple_wallet::wallet_idle_thread() ()
#5  0x0000000000d0fdd3 in cryptonote::simple_wallet::run()::{lambda()#1}::operator()() const ()
#6  0x0000000000d1ed92 in boost::detail::thread_data<cryptonote::simple_wallet::run()::{lambda()#1}>::run() ()
#7  0x00007fc82bd979da in thread_proxy () from /home/user/boost_1_59_install/lib/libboost_thread.so.1.59.0
#8  0x00007fc829e9a52a in start_thread () from /lib64/libpthread.so.0
#9  0x00007fc829bd622d in clone () from /lib64/libc.so.6
Thread 1 (Thread 0x7fc82ce89840 (LWP 5205)):
#0  0x00007fc82c655480 in wcwidth@plt () from /lib64/libreadline.so.6
#1  0x00007fc82c676053 in _rl_find_next_mbchar () from /lib64/libreadline.so.6
#2  0x00007fc82c665635 in expand_prompt () from /lib64/libreadline.so.6
#3  0x00007fc82c6658f6 in rl_expand_prompt () from /lib64/libreadline.so.6
#4  0x00007fc82c6560ba in rl_set_prompt () from /lib64/libreadline.so.6
#5  0x00000000011b0232 in rdln::readline_buffer::set_prompt(std::string const&) ()
#6  0x0000000000d3af9e in epee::async_console_handler::print_prompt() ()
#7  0x0000000000d6038a in bool epee::async_console_handler::run<bool epee::async_console_handler::run<boost::_bi::bind_t<bool, boost::_mfi:
#8  0x0000000000d4a215 in bool epee::async_console_handler::run<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std:
#9  0x0000000000d3b4c4 in epee::console_handlers_binder::run_handling(std::string const&, std::string const&, std::function<void ()>) ()
#10 0x0000000000d1007b in cryptonote::simple_wallet::run() ()
#11 0x0000000000d161e4 in main ()



# Discussion History
## jtgrassie | 2017-06-25T15:00:59+00:00
Have you tried with #2112 ? Reason I ask is this has a process lock.

## moneromooo-monero | 2017-06-25T15:06:56+00:00
No, I have just what's on master right now. It may well be the reason, thanks.

## jtgrassie | 2017-06-25T15:08:54+00:00
Yes I'm sure thats it. #2112 fixes.

## moneromooo-monero | 2017-06-26T04:47:47+00:00
I'm seeing a similar non fatal hang with 2112 applied. It's pretty often, and happens when I'm being asked for a password (when starting, when doing any command which requires one). The hang is only temporary though, but can last a minute. It *looks* like if I go to another shell to run pstack to see where it's at, this will get it unstuck and it displays its password prompt, but not always (and this is when I can get the stack trace below).

Thread 4 (Thread 0x7f7a7bd99700 (LWP 5362)):
#0  0x00007f7a801de590 in pthread_cond_wait@@GLIBC_2.3.2 () from /lib64/libpthread.so.0
#1  0x0000000000d22c5d in boost::condition_variable::wait(boost::unique_lock<boost::mutex>&) ()
#2  0x0000000000d3abeb in epee::async_stdin_reader::wait_read() ()
#3  0x0000000000d3ade7 in epee::async_stdin_reader::reader_thread_func() ()
#4  0x0000000000e50a2b in void std::_Mem_fn<void (epee::async_stdin_reader::*)()>::operator()<, void>(epee::async_stdin_reader*) const ()
#5  0x0000000000e4fb86 in void std::_Bind<std::_Mem_fn<void (epee::async_stdin_reader::*)()> (epee::async_stdin_reader*)>::__call<void, , 0
#6  0x0000000000e4defa in void std::_Bind<std::_Mem_fn<void (epee::async_stdin_reader::*)()> (epee::async_stdin_reader*)>::operator()<, voi
#7  0x0000000000e48e08 in boost::detail::thread_data<std::_Bind<std::_Mem_fn<void (epee::async_stdin_reader::*)()> (epee::async_stdin_reade
#8  0x00007f7a820d69da in thread_proxy () from /home/user/boost_1_59_install/lib/libboost_thread.so.1.59.0
#9  0x00007f7a801d952a in start_thread () from /lib64/libpthread.so.0
#10 0x00007f7a7ff1522d in clone () from /lib64/libc.so.6
Thread 3 (Thread 0x7f7a75025700 (LWP 5363)):
#0  0x00007f7a7ff0bae3 in select () from /lib64/libc.so.6
#1  0x00000000011b0a7c in process_input() ()
#2  0x00000000011b089f in rdln::readline_buffer::process() ()
#3  0x0000000000d3adb2 in epee::async_stdin_reader::readline_thread_func() ()
#4  0x0000000000e50a2b in void std::_Mem_fn<void (epee::async_stdin_reader::*)()>::operator()<, void>(epee::async_stdin_reader*) const ()
#5  0x0000000000e4fb86 in void std::_Bind<std::_Mem_fn<void (epee::async_stdin_reader::*)()> (epee::async_stdin_reader*)>::__call<void, , 0
#6  0x0000000000e4defa in void std::_Bind<std::_Mem_fn<void (epee::async_stdin_reader::*)()> (epee::async_stdin_reader*)>::operator()<, voi
#7  0x0000000000e48e08 in boost::detail::thread_data<std::_Bind<std::_Mem_fn<void (epee::async_stdin_reader::*)()> (epee::async_stdin_reade
#8  0x00007f7a820d69da in thread_proxy () from /home/user/boost_1_59_install/lib/libboost_thread.so.1.59.0
#9  0x00007f7a801d952a in start_thread () from /lib64/libpthread.so.0
#10 0x00007f7a7ff1522d in clone () from /lib64/libc.so.6
Thread 2 (Thread 0x7f7a74416700 (LWP 5381)):
#0  0x00007f7a801de939 in pthread_cond_timedwait@@GLIBC_2.3.2 () from /lib64/libpthread.so.0
#1  0x0000000000d22d6b in boost::condition_variable::do_wait_until(boost::unique_lock<boost::mutex>&, timespec const&) ()
#2  0x0000000000d226eb in boost::condition_variable::wait_until(boost::unique_lock<boost::mutex>&, boost::chrono::time_point<boost::chrono:
#3  0x0000000000d5028b in boost::cv_status boost::condition_variable::wait_for<long, boost::ratio<1l, 1l> >(boost::unique_lock<boost::mutex
#4  0x0000000000d0fe4b in cryptonote::simple_wallet::wallet_idle_thread() ()
#5  0x0000000000d0feb7 in cryptonote::simple_wallet::run()::{lambda()#1}::operator()() const ()
#6  0x0000000000d1ee76 in boost::detail::thread_data<cryptonote::simple_wallet::run()::{lambda()#1}>::run() ()
#7  0x00007f7a820d69da in thread_proxy () from /home/user/boost_1_59_install/lib/libboost_thread.so.1.59.0
#8  0x00007f7a801d952a in start_thread () from /lib64/libpthread.so.0
#9  0x00007f7a7ff1522d in clone () from /lib64/libc.so.6
Thread 1 (Thread 0x7f7a831c8840 (LWP 5361)):
#0  0x00007f7a801e0f1d in __lll_lock_wait () from /lib64/libpthread.so.0
#1  0x00007f7a801db89d in pthread_mutex_lock () from /lib64/libpthread.so.0
#2  0x00000000011b054d in __gthread_mutex_lock ()
#3  0x00000000011b0d66 in std::mutex::lock() ()
#4  0x00000000011b0e87 in std::unique_lock<std::mutex>::lock() ()
#5  0x00000000011b0e0f in std::unique_lock<std::mutex>::unique_lock(std::mutex&) ()
#6  0x00000000011b0734 in rdln::readline_buffer::stop() ()
#7  0x00000000011b05f4 in rdln::suspend_readline::suspend_readline() ()
#8  0x0000000000fb9a46 in tools::password_container::prompt(bool, char const*) ()
#9  0x0000000000e57c8c in tools::wallet2::password_prompt(bool) ()
#10 0x0000000000cf6a17 in cryptonote::simple_wallet::get_and_verify_password() const ()
#11 0x0000000000ce4c4f in cryptonote::simple_wallet::make_multisig(std::vector<std::string, std::allocator<std::string> > const&) ()
#12 0x0000000000dad2b8 in boost::_mfi::mf1<bool, cryptonote::simple_wallet, std::vector<std::string, std::allocator<std::string> > const&>:
#13 0x0000000000da28c8 in bool boost::_bi::list2<boost::_bi::value<cryptonote::simple_wallet*>, boost::arg<1> >::operator()<bool, boost::_m
#14 0x0000000000d95ea6 in bool boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, cryptonote::simple_wallet, std::vector<std::string, std::all
#15 0x0000000000d86c4a in boost::detail::function::function_obj_invoker1<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, cryptonote::simple
#16 0x0000000000d49eb4 in boost::function1<bool, std::vector<std::string, std::allocator<std::string> > const&>::operator()(std::vector<std
#17 0x0000000000d3b3e2 in epee::command_handler::process_command_vec(std::vector<std::string, std::allocator<std::string> > const&) ()
#18 0x0000000000d3b496 in epee::command_handler::process_command_str(std::string const&) ()
#19 0x0000000000d937a6 in bool boost::_mfi::mf1<bool, epee::command_handler, std::string const&>::call<epee::console_handlers_binder*, std:
#20 0x0000000000d84e7c in bool boost::_mfi::mf1<bool, epee::command_handler, std::string const&>::operator()<epee::console_handlers_binder*
#21 0x0000000000d73fdc in bool boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> >::operator()<bool, boost
#22 0x0000000000d603da in bool boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::string const&>, boost::_bi::list
#23 0x0000000000d4a2a4 in bool epee::async_console_handler::run<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std:
#24 0x0000000000d60623 in bool epee::async_console_handler::run<bool epee::async_console_handler::run<boost::_bi::bind_t<bool, boost::_mfi:
#25 0x0000000000d4a2f9 in bool epee::async_console_handler::run<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std:
#26 0x0000000000d3b5a8 in epee::console_handlers_binder::run_handling(std::string const&, std::string const&, std::function<void ()>) ()
#27 0x0000000000d1015f in cryptonote::simple_wallet::run() ()
#28 0x0000000000d162c8 in main ()


## moneromooo-monero | 2017-06-26T05:00:16+00:00
It also happens at random places, for instance, a long pause on new wallet creation between the display of languages and the "Enter the number corresponding to the language of your choice: " prompt.

## moneromooo-monero | 2017-06-26T06:27:45+00:00
1:20 pause here, from the log timestamps. I'll just disable it for now, it's infuriating when debugging stuff.

## jtgrassie | 2017-06-26T10:38:12+00:00
Do you have your `select` PR applied too?

## moneromooo-monero | 2017-06-26T12:21:01+00:00
You mean the one to avoid the busy loop ? Yes, it's in master, and it's in the tree I was testing.

## jtgrassie | 2017-06-26T12:27:25+00:00
Yes #2111. Just checking before I did into it. It's tough as I cannot replicate. Will try some other systems. 

## moneromooo-monero | 2017-06-26T12:38:12+00:00
Very odd. It's pretty much all the time here. Fedora on Xen, x86_64.

## jtgrassie | 2017-06-26T13:07:46+00:00
Reason I thought maybe #2111 fixed it was because of seeing this in your stack:
```
Thread 3 (Thread 0x7f7a75025700 (LWP 5363)):
#0 0x00007f7a7ff0bae3 in select () from /lib64/libc.so.6
#1 0x00000000011b0a7c in process_input() ()
#2 0x00000000011b089f in rdln::readline_buffer::process() ()
```

But now I'm thinking maybe some kind of race.

I've been testing on OS X 10.11.6 and Ubuntu 16 (Under VirtualBox).

## jtgrassie | 2017-06-26T13:22:22+00:00
So a password prompt is correctly suspending readline processing:

```
Thread 1 (Thread 0x7f7a831c8840 (LWP 5361)):
#0 0x00007f7a801e0f1d in __lll_lock_wait () from /lib64/libpthread.so.0
#1 0x00007f7a801db89d in pthread_mutex_lock () from /lib64/libpthread.so.0
#2 0x00000000011b054d in __gthread_mutex_lock ()
#3 0x00000000011b0d66 in std::mutex::lock() ()
#4 0x00000000011b0e87 in std::unique_lockstd::mutex::lock() ()
#5 0x00000000011b0e0f in std::unique_lockstd::mutex::unique_lock(std::mutex&) ()
#6 0x00000000011b0734 in rdln::readline_buffer::stop() ()
#7 0x00000000011b05f4 in rdln::suspend_readline::suspend_readline() ()
#8 0x0000000000fb9a46 in tools::password_container::prompt(bool, char const) ()
```
So why is thread 3 at `select`?
```
Thread 3 (Thread 0x7f7a75025700 (LWP 5363)):
#0 0x00007f7a7ff0bae3 in select () from /lib64/libc.so.6
#1 0x00000000011b0a7c in process_input() ()
#2 0x00000000011b089f in rdln::readline_buffer::process() ()
```
What I see from this is that `rdln::readline_buffer::stop()` is waiting on the lock from `rdln::readline_buffer::process()` which is stuck at `select`. As your patch #2111 should have stopped `select` blocking for long, that should in theory mean the lock gets released and readline_buffer manages to stop. That it's stuck on `select` is troubling.


## jtgrassie | 2017-06-26T13:33:22+00:00
But then looking at your two stacktraces, is the first issue of exit, enter, fixed by #2122?
There look to be a lot of other waiting locks unrelated to readline in the second stacktrace.

## moneromooo-monero | 2017-06-27T08:50:40+00:00
I did not see the exit hang again, but then I had seen it only once before.

## moneromooo-monero | 2017-06-27T08:55:20+00:00
Looking at the code right now, it looks like it could be that the stop thread never gets the lock, since the caller for select is:

      while (m_run.load(std::memory_order_relaxed))
      {
        m_readline_buffer.process();
      }

So the thread never gets to enter any kind of wait while outside the lock. To reliably get rid of this, you need a condition variable in addition to the mutex.


## moneromooo-monero | 2017-06-27T09:02:44+00:00
And by never, I mean for a long time. It'd also neatly explain the random seeming delays, and also why it often got "unstuck" when I ran pstack on it to see where it was...

## jtgrassie | 2017-06-27T10:44:07+00:00
> Looking at the code right now, it looks like it could be that the stop thread never gets the lock

But in your backtrace `readline_buffer::stop` is getting the lock so I'm not sure about this. `readline_buffer::process` (where the select is) is protected by the lock so the only way it should only be at select if it entered this method before the stop acquired the lock and and it should return quickly and on next call be stopped before reaching select as stop has the lock.

## jtgrassie | 2017-06-27T10:58:41+00:00
When `select` is done, `process_input` returns so `readline_buffer::process` gives up the lock and the waiting `readline_buffer::stop` then continues and stops `readline_buffer`.

## jtgrassie | 2017-06-27T11:02:38+00:00
Ah ha. But yes the converse makes sense! The stop/exit thread can be blocked/waiting for a suspended readline_buffer. 

## jtgrassie | 2017-06-27T11:41:43+00:00
But then this state can only ever be present if readline is suspended, which is only when password prompting or in a multiline output message command. 
As I cannot yet replicate, do you mind testing something? Basically changing:
```cpp
int rdln::readline_buffer::process()
{
  std::unique_lock<std::mutex> lock(process_mutex);
  if(m_cout_buf == NULL)
    return 0;
  return process_input();
}
```
to:
```cpp
int rdln::readline_buffer::process()
{
  if(!process_mutex.try_lock())
    return 0;
  if(m_cout_buf == NULL)
    return 0;
  int count = process_input();
  process_mutex.unlock();
  return count;
}
```
This way, process() never blocks when RL is suspended.

## moneromooo-monero | 2017-06-27T14:18:48+00:00
Did not help (I also added an unlock on the early return so it's not a deadlock due to that).
I'll add a cond var then, I'm pretty sure it's that.

## moneromooo-monero | 2017-06-27T14:42:48+00:00
If I add a yield() at the end of process, it's a lot better, though it can still wait a bit, so not 100% good.

## moneromooo-monero | 2017-06-27T14:50:23+00:00
Hmm. Reading the code, rdln::readline_buffer::sync uses m_cout_buf, but does not seem to lock process_mutex, which protects m_cout_buf in start/stop.

## moneromooo-monero | 2017-06-27T14:58:37+00:00
It's annoying. With a 1 millisecond sleep at the end of process (after unlock), it works reliably. Not sure why a yield isn't always enough, since it should let the start/stop lock the lock before the thread is scheduled again. Using a cond var does not work since it'd need to be locked already. Would you be fine with a sleep like this ?

## moneromooo-monero | 2017-06-27T15:09:20+00:00
Or maybe a better solution is to remove that process_lock and find a more granular way to fix the previous problem ?

## moneromooo-monero | 2017-06-27T15:10:22+00:00
This is the patch which fixes the bug here:
```
commit e0ce6556c97d5838a29748a4f81f5d6c09464683
Author: moneromooo-monero <moneromooo-monero@users.noreply.github.com>
Date:   Tue Jun 27 16:04:44 2017 +0100

    readline_buffer: fix start/stop threads being starved by process
    
    process could run for quite some time re-acquiring the process
    lock, leaving start/stop starving. Yielding after unlock in
    process is much better but doesn't seem to be enough to reliably
    yield, so we sleep for a millisecond, which should be transparent
    for user input anyway.

diff --git a/contrib/epee/src/readline_buffer.cpp b/contrib/epee/src/readline_buffer.cpp
index 67eec13..c959bf5 100644
--- a/contrib/epee/src/readline_buffer.cpp
+++ b/contrib/epee/src/readline_buffer.cpp
@@ -5,6 +5,7 @@
 #include <unistd.h>
 #include <mutex>
 #include <condition_variable>
+#include <boost/thread.hpp>
 
 static int process_input();
 static void install_line_handler();
@@ -83,10 +84,17 @@ void rdln::readline_buffer::set_prompt(const std::string& prompt)
 
 int rdln::readline_buffer::process()
 {
-  std::unique_lock<std::mutex> lock(process_mutex);
+  process_mutex.lock();
   if(m_cout_buf == NULL)
+  {
+    process_mutex.unlock();
+    boost::this_thread::sleep_for(boost::chrono::milliseconds( 1 ));
     return 0;
-  return process_input();
+  }
+  int count = process_input();
+  process_mutex.unlock();
+  boost::this_thread::sleep_for(boost::chrono::milliseconds( 1 ));
+  return count;
 }
 
 int rdln::readline_buffer::sync()

```

## moneromooo-monero | 2017-06-27T15:12:12+00:00
Also a bit of cleanup I found while looking at it:

```
commit 16d4ea96aecc83edfbad21cb0d23894cc78146aa
Author: moneromooo-monero <moneromooo-monero@users.noreply.github.com>
Date:   Tue Jun 27 16:04:14 2017 +0100

    readline_buffer: move a local to local scope
    
    Also limit the select fd limit to what we use

diff --git a/contrib/epee/src/readline_buffer.cpp b/contrib/epee/src/readline_buffer.cpp
index 3865b56..67eec13 100644
--- a/contrib/epee/src/readline_buffer.cpp
+++ b/contrib/epee/src/readline_buffer.cpp
@@ -118,19 +118,18 @@ int rdln::readline_buffer::sync()
   return 0;
 }
 
-static fd_set fds;
-
 static int process_input()
 {
   int count;
   struct timeval t;
+  fd_set fds;
   
   t.tv_sec = 0;
   t.tv_usec = 1000;
   
   FD_ZERO(&fds);
   FD_SET(STDIN_FILENO, &fds);
-  count = select(FD_SETSIZE, &fds, NULL, NULL, &t);
+  count = select(STDIN_FILENO + 1, &fds, NULL, NULL, &t);
   if (count < 1)
   {
     return count;


```

They're based on a branch with your process_lock patch, so don't apply to master.

## jtgrassie | 2017-06-27T15:21:33+00:00
Great. Got there in the end it seems!
Do you want me add these to the PR with the process_lock?

## moneromooo-monero | 2017-06-27T16:45:50+00:00
I guess. That'd lose my GPG signature, but those are small patches so should be fine to re-review once merged.

## jtgrassie | 2017-06-27T22:17:19+00:00
@moneromooo-monero OK I added to #2112 and tested on OS X and Ubuntu quickly.
As I never managed to replicate, can you do a final test of this PR please?

## moneromooo-monero | 2017-06-28T12:34:04+00:00
This now seems all fixed with the recent patches, closing.

## moneromooo-monero | 2017-07-05T14:20:14+00:00
This has now happened again:

Thread 6 (Thread 0x7f0577488700 (LWP 20037)):
#0  0x00007f05bc12a590 in pthread_cond_wait@@GLIBC_2.3.2 () from /lib64/libpthread.so.0
#1  0x00007f05bfaac659 in wait<boost::asio::detail::scoped_lock<boost::asio::detail::posix_mutex> > (lock=..., this=0x4bd93a8) at /home/use
#2  do_run_one (ec=..., this_thread=..., lock=..., this=<optimized out>) at /home/user/boost_1_59_0/boost/asio/detail/impl/task_io_service.
#3  boost::asio::detail::task_io_service::run (this=0x4bd9350, ec=...) at /home/user/boost_1_59_0/boost/asio/detail/impl/task_io_service.ip
#4  0x00007f05bfab15bb in boost::asio::io_service::run (this=0x4bd80a0) at /home/user/boost_1_59_0/boost/asio/impl/io_service.ipp:59
#5  0x00007f05bfaa84a0 in operator() (p=<optimized out>, this=<optimized out>) at /home/user/boost_1_59_0/boost/bind/mem_fn_template.hpp:49
#6  operator()<long unsigned int, boost::_mfi::mf0<long unsigned int, boost::asio::io_service>, boost::_bi::list0> (a=<synthetic pointer>, 
#7  operator() (this=<optimized out>) at /home/user/boost_1_59_0/boost/bind/bind.hpp:895
#8  boost::detail::thread_data<boost::_bi::bind_t<unsigned long, boost::_mfi::mf0<unsigned long, boost::asio::io_service>, boost::_bi::list
#9  0x00007f05bcb799da in thread_proxy () from /home/user/boost_1_59_install/lib/libboost_thread.so.1.59.0
#10 0x00007f05bc12552a in start_thread () from /lib64/libpthread.so.0
#11 0x00007f05bbe6122d in clone () from /lib64/libc.so.6
Thread 5 (Thread 0x7f0576c87700 (LWP 20038)):
#0  0x00007f05bbe61833 in epoll_wait () from /lib64/libc.so.6
#1  0x000000000056bce6 in boost::asio::detail::epoll_reactor::run (this=0x4be9be0, block=block@entry=true, ops=...) at /home/user/boost_1_5
#2  0x000000000056d3f4 in boost::asio::detail::task_io_service::do_run_one (this=this@entry=0x4be9b00, lock=..., this_thread=..., ec=...) a
#3  0x000000000058ba77 in run (ec=..., this=0x4be9b00) at /home/user/boost_1_59_0/boost/asio/detail/impl/task_io_service.ipp:149
#4  run (this=<optimized out>) at /home/user/boost_1_59_0/boost/asio/impl/io_service.ipp:59
#5  epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::worker_thre
#6  0x0000000000564d8a in operator() (p=<optimized out>, this=<optimized out>) at /home/user/boost_1_59_0/boost/bind/mem_fn_template.hpp:49
#7  operator()<bool, boost::_mfi::mf0<bool, epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<> > >, boost::_b
#8  operator() (this=<optimized out>) at /home/user/boost_1_59_0/boost/bind/bind.hpp:895
#9  boost::detail::thread_data<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, epee::net_utils::boosted_tcp_server<epee::net_utils::http::h
#10 0x00007f05bcb799da in thread_proxy () from /home/user/boost_1_59_install/lib/libboost_thread.so.1.59.0
#11 0x00007f05bc12552a in start_thread () from /lib64/libpthread.so.0
#12 0x00007f05bbe6122d in clone () from /lib64/libc.so.6
Thread 4 (Thread 0x7f0576486700 (LWP 20039)):
#0  0x00007f05bc12a590 in pthread_cond_wait@@GLIBC_2.3.2 () from /lib64/libpthread.so.0
#1  0x000000000056d59c in wait<boost::asio::detail::scoped_lock<boost::asio::detail::posix_mutex> > (lock=..., this=0x4be9b58) at /home/use
#2  boost::asio::detail::task_io_service::do_run_one (this=this@entry=0x4be9b00, lock=..., this_thread=..., ec=...) at /home/user/boost_1_5
#3  0x000000000058ba77 in run (ec=..., this=0x4be9b00) at /home/user/boost_1_59_0/boost/asio/detail/impl/task_io_service.ipp:149
#4  run (this=<optimized out>) at /home/user/boost_1_59_0/boost/asio/impl/io_service.ipp:59
#5  epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::worker_thre
#6  0x0000000000564d8a in operator() (p=<optimized out>, this=<optimized out>) at /home/user/boost_1_59_0/boost/bind/mem_fn_template.hpp:49
#7  operator()<bool, boost::_mfi::mf0<bool, epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<> > >, boost::_b
#8  operator() (this=<optimized out>) at /home/user/boost_1_59_0/boost/bind/bind.hpp:895
#9  boost::detail::thread_data<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, epee::net_utils::boosted_tcp_server<epee::net_utils::http::h
#10 0x00007f05bcb799da in thread_proxy () from /home/user/boost_1_59_install/lib/libboost_thread.so.1.59.0
#11 0x00007f05bc12552a in start_thread () from /lib64/libpthread.so.0
#12 0x00007f05bbe6122d in clone () from /lib64/libc.so.6
Thread 3 (Thread 0x7f0575c85700 (LWP 20040)):
#0  0x00007f05bc12a590 in pthread_cond_wait@@GLIBC_2.3.2 () from /lib64/libpthread.so.0
#1  0x00007f05bc90fd5c in std::condition_variable::wait(std::unique_lock<std::mutex>&) () from /lib64/libstdc++.so.6
#2  0x00007f05bd7f17dd in rdln::readline_buffer::get_line (this=this@entry=0x4c02588, line="") at /home/user/src/bitmonero/contrib/epee/src
#3  0x000000000054e910 in epee::async_stdin_reader::reader_thread_func (this=0x4c02560) at /home/user/src/bitmonero/contrib/epee/include/co
#4  0x000000000054bfba in operator()<, void> (__object=<optimized out>, this=<optimized out>) at /usr/include/c++/4.9.2/functional:569
#5  __call<void, 0ul> (__args=<optimized out>, this=<optimized out>) at /usr/include/c++/4.9.2/functional:1264
#6  operator()<, void> (this=<optimized out>) at /usr/include/c++/4.9.2/functional:1323
#7  boost::detail::thread_data<std::_Bind<std::_Mem_fn<void (epee::async_stdin_reader::*)()> (epee::async_stdin_reader*)> >::run() (this=<o
#8  0x00007f05bcb799da in thread_proxy () from /home/user/boost_1_59_install/lib/libboost_thread.so.1.59.0
#9  0x00007f05bc12552a in start_thread () from /lib64/libpthread.so.0
#10 0x00007f05bbe6122d in clone () from /lib64/libc.so.6
Thread 2 (Thread 0x7f0574c83700 (LWP 20042)):
#0  0x00007f05bc12a590 in pthread_cond_wait@@GLIBC_2.3.2 () from /lib64/libpthread.so.0
#1  0x000000000054e6f8 in boost::condition_variable::wait (this=this@entry=0x4c02698, m=...) at /home/user/boost_1_59_0/boost/thread/pthrea
#2  0x0000000000550e1c in get_line (line="", this=0x4c02560) at /home/user/src/bitmonero/contrib/epee/include/console_handler.h:86
#3  epee::async_console_handler::run<bool epee::async_console_handler::run<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_ha
#4  0x0000000000551570 in run<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::basic_string<char> const&>, boost
#5  epee::console_handlers_binder::run_handling(std::string const&, std::string const&, std::function<void ()>) (this=0x4c02528, prompt="",
#6  0x000000000054d4ab in operator() (a3=..., a2="Monero 'Wolfram Warptangent' (v0.10.3.1-694470f)\nCommands: \n  alt_chain_info          P
#7  operator()<bool, boost::_mfi::mf3<bool, epee::console_handlers_binder, const std::basic_string<char>&, const std::basic_string<char>&, 
#8  operator() (this=0x4c24088) at /home/user/boost_1_59_0/boost/bind/bind.hpp:895
#9  boost::detail::thread_data<boost::_bi::bind_t<bool, boost::_mfi::mf3<bool, epee::console_handlers_binder, std::string const&, std::stri
#10 0x00007f05bcb799da in thread_proxy () from /home/user/boost_1_59_install/lib/libboost_thread.so.1.59.0
#11 0x00007f05bc12552a in start_thread () from /lib64/libpthread.so.0
#12 0x00007f05bbe6122d in clone () from /lib64/libc.so.6
Thread 1 (Thread 0x7f05c0902880 (LWP 20036)):
#0  0x00007f05bc12a590 in pthread_cond_wait@@GLIBC_2.3.2 () from /lib64/libpthread.so.0
#1  0x000000000054e6f8 in boost::condition_variable::wait (this=0x4c02768, m=...) at /home/user/boost_1_59_0/boost/thread/pthread/condition
#2  0x00007f05bcb7a41c in boost::thread::join_noexcept() () from /home/user/boost_1_59_install/lib/libboost_thread.so.1.59.0
#3  0x0000000000547da1 in join (this=0x4c02560) at /home/user/boost_1_59_0/boost/thread/detail/thread.hpp:767
#4  stop (this=0x4c02560) at /home/user/src/bitmonero/contrib/epee/include/console_handler.h:115
#5  stop (this=0x4c02560) at /home/user/src/bitmonero/contrib/epee/include/console_handler.h:310
#6  stop_handling (this=0x4c02528) at /home/user/src/bitmonero/contrib/epee/include/console_handler.h:518
#7  daemonize::t_command_server::stop_handling (this=0x4c02510) at /home/user/src/bitmonero/src/daemon/command_server.cpp:291
#8  0x000000000056312a in daemonize::t_daemon::run (this=this@entry=0x7ffdbb3e2ce0, interactive=interactive@entry=true) at /home/user/src/b
#9  0x000000000065e778 in daemonize::t_executor::run_interactive (this=this@entry=0x7ffdbb3e36d7, vm=...) at /home/user/src/bitmonero/src/d
#10 0x00000000006624d0 in daemonizer::daemonize<daemonize::t_executor>(int, char const**, daemonize::t_executor&&, boost::program_options::
#11 0x00000000006606fd in main (argc=3, argv=0x7ffdbb3e3848) at /home/user/src/bitmonero/src/daemon/main.cpp:286

A quick look around shows line_mutex is used at only one location (to lock get_line), which looks very suspect.


## jtgrassie | 2017-07-05T14:40:52+00:00
> A quick look around shows line_mutex is used at only one location (to lock get_line), which looks very suspect.

It is notified from code in `handle_enter`.

## moneromooo-monero | 2017-07-05T17:01:29+00:00
I'm assuming you mean have_line, not line_mutex. line_mutex is used only in get_line (but it might be there to ensure only one thread can read a line at once ?)


## jtgrassie | 2017-07-05T17:45:24+00:00
Thats correct. The mutex is there for thread safety and the condition_variable is used to block till we have a line of input.

## jtgrassie | 2017-07-06T13:22:03+00:00
@moneromooo-monero is this also confirmed to be readline related? Asking because I have seen these exit hangs in the wallet without readline.

## moneromooo-monero | 2017-07-06T14:10:57+00:00
The stack trace shows a thread waiting in readline::get_line. I also never had that happen before the readline patches (though it did happen in windows in the past).

## jtgrassie | 2017-07-07T12:08:48+00:00
Can you try this patch please before I create a PR? It should deal with a waiting get_line while trying to stop. 
```diff
diff --git a/contrib/epee/src/readline_buffer.cpp b/contrib/epee/src/readline_buffer.cpp
index c846641b..53261132 100644
--- a/contrib/epee/src/readline_buffer.cpp
+++ b/contrib/epee/src/readline_buffer.cpp
@@ -59,6 +59,7 @@ void rdln::readline_buffer::start()
 void rdln::readline_buffer::stop()
 {
   std::unique_lock<std::mutex> lock(process_mutex);
+  have_line.notify_all();
   if(m_cout_buf == NULL)
     return;
   std::cout.rdbuf(m_cout_buf);
```

## moneromooo-monero | 2017-07-07T14:41:44+00:00
I will, but at first glance, this is racy since get_line does not lock process_mutex, therefore might start just after that notify_all.

## jtgrassie | 2017-07-07T14:50:17+00:00
get_line doesn't need to lock process_mutex though as it serves a separate purpose.

## moneromooo-monero | 2017-07-07T18:40:26+00:00
I have tried the patch, and, unsurprisingly (since the hang occured just once after your previous patch), exiting works fine.

## moneromooo-monero | 2017-08-16T12:14:58+00:00
I've just had it again with latest master. One thread waiting for readline_buffer::get_line to end, and it doesn't,

## moneromooo-monero | 2017-09-20T21:00:51+00:00
I've not seen this since hyc's threading simplification.

+resolved

# Action History
- Created by: moneromooo-monero | 2017-06-25T14:49:45+00:00
- Closed at: 2017-09-20T21:00:51+00:00
