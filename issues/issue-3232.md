---
title: GUI wont open after updating Ubuntu 20.04.1
source_url: https://github.com/monero-project/monero-gui/issues/3232
author: 3ach1T3ach1
assignees: []
labels: []
created_at: '2020-11-13T09:11:18+00:00'
updated_at: '2021-04-20T23:51:40+00:00'
type: issue
status: closed
closed_at: '2021-04-20T23:51:40+00:00'
---

# Original Description
The GUI freezes when trying to open and can't be closed until killing process. Happened directly after running "sudo apt update, apt upgrade, apt full-upgrade"

Haven't been able to roll back the updates to get working yet. 

First time reporting on git here and not a professional developer etc but logistically thinking issue can be a risk security wise at worst and a bug that needs fixing none the less. No funds in account was still in process of syncing node for the first time. 

If some guidance can be provided on how to pull logs or debug etc will be appreciated and glad to contribute to fix in any small way.

Thanks in advance 

# Discussion History
## selsta | 2020-11-13T09:12:19+00:00
Which version are you using? We fixed a bug like this in v0.17.1.4

## 3ach1T3ach1 | 2020-11-13T09:14:45+00:00
@selsta It is v017.1.4 I just downloaded it, it's not the most recent?

## selsta | 2020-11-13T09:16:05+00:00
Did you download it from getmonero.org?

Can you post your terminal output when starting?

## 3ach1T3ach1 | 2020-11-13T09:26:08+00:00
Yeah from getmonero.org and the linux64 bit link under GUI.

After clicking on App the terminal opens requesting wallet code and after entering code it processes to the terminal attached with the progress ring in infinite loop.
![Screenshot from 2020-11-13 20-21-08](https://user-images.githubusercontent.com/74396332/99056410-5e54ec00-25ee-11eb-9b16-ee9415277036.png)


## selsta | 2020-11-13T09:27:07+00:00
Is this a Ledger wallet?

## 3ach1T3ach1 | 2020-11-13T09:28:08+00:00
Yes it's connected to a ledger

## selsta | 2020-11-13T09:28:43+00:00
Did you accept exporting the view key on your Ledger?

## 3ach1T3ach1 | 2020-11-13T09:31:01+00:00
It doesn't ask on the ledger now, where it did before after entering the code. Now it doesnt and likewise the terminal wouldn't freeze

## selsta | 2020-11-13T09:32:56+00:00
Did you try restarting your computer?

## 3ach1T3ach1 | 2020-11-13T09:34:43+00:00
Yes restarted multiple times. Tried running sudo apt get update to see if something was missed etc. No love :+1: 

## xiphon | 2020-11-13T09:38:09+00:00
Try to clean QML cache by removing `~/.cache/monero-project` folder.

## 3ach1T3ach1 | 2020-11-13T09:47:02+00:00
@xiphon Did that and still freezing

## xiphon | 2020-11-13T09:49:40+00:00
Run `gdb ./monero-wallet-gui`. Once it freezes, hit `CTRL+C` in terminal and post `thread apply all bt` results.

## 3ach1T3ach1 | 2020-11-13T10:07:00+00:00
Not sure I'm working it correctly this is what I get when running "gdb ./monero-wallet-gui" from the directory"

### $ gdb ./monero-wallet-gui
GNU gdb (Ubuntu 9.1-0ubuntu1) 9.1
Copyright (C) 2020 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from ./monero-wallet-gui...
(gdb) Quit



## selsta | 2020-11-13T10:07:50+00:00
Type "run" to start

## 3ach1T3ach1 | 2020-11-13T10:14:14+00:00
@selsta Thanks. 

### monero-gui-v0.17.1.4/monero-wallet-gui 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
[New Thread 0x7ffff6916700 (LWP 5493)]
2020-11-13 10:10:35.017	W Qt:5.9.9 GUI:0.17.1.4-6fce5c7 | screen: 1920x1080 - dpi: 96 - ratio:0.731364
[New Thread 0x7ffff5e90700 (LWP 5494)]
[New Thread 0x7fffee65f700 (LWP 5525)]
[New Thread 0x7fffede5e700 (LWP 5526)]
[New Thread 0x7fffed65d700 (LWP 5527)]
[New Thread 0x7fffece5c700 (LWP 5528)]
[New Thread 0x7fffe396b700 (LWP 5529)]
[New Thread 0x7fffe316a700 (LWP 5530)]
[New Thread 0x7fffe2969700 (LWP 5531)]
2020-11-13 10:10:36.018	W Logging to "/home/c/.bitmonero/monero-wallet-gui.log"
2020-11-13 10:10:36.019	W qrc:/qt-project.org/imports/QtQuick/Controls/ApplicationWindow.qml:240:9: QML ContentItem: Binding loop detected for property "implicitWidth"
[New Thread 0x7fffe08c4700 (LWP 5532)]
[New Thread 0x7fffba034700 (LWP 5533)]
[New Thread 0x7fffb9b33700 (LWP 5534)]
[New Thread 0x7fffb9632700 (LWP 5535)]
[New Thread 0x7fffb9131700 (LWP 5536)]
[New Thread 0x7fffb8c30700 (LWP 5537)]
[New Thread 0x7fffb872f700 (LWP 5538)]
[New Thread 0x7fffb822e700 (LWP 5539)]
[New Thread 0x7fffb7d2d700 (LWP 5540)]
[New Thread 0x7fffb782c700 (LWP 5541)]
[New Thread 0x7fffb732b700 (LWP 5542)]
[Thread 0x7fffe316a700 (LWP 5530) exited]
[New Thread 0x7fffe316a700 (LWP 5549)]
[New Thread 0x7fffb642a700 (LWP 5550)]
[New Thread 0x7fffb5c29700 (LWP 5551)]
^C--Type <RET> for more, q to quit, c to continue without paging--


## selsta | 2020-11-13T10:15:11+00:00
now enter

thread apply all bt

## 3ach1T3ach1 | 2020-11-13T10:19:35+00:00
I had to re-run the gdb and it came up with a different result. 

### ./monero-wallet-gui...
(gdb) start
Temporary breakpoint 1 at 0x3e0304
Starting program: /home/c/Downloads/Mining/XMR/monero-gui-linux-x64-v0.17.1 (1).4/monero-gui-v0.17.1.4/monero-wallet-gui 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Temporary breakpoint 1, 0x0000555555934304 in main ()
(gdb) 



Still enter "thread apply all bt"?



## xiphon | 2020-11-13T10:23:22+00:00
1. Run `gdb -ex run ./monero-wallet-gui`
2. Once it freezes, hit CTRL+C in terminal 
3. `thread apply all bt`

## 3ach1T3ach1 | 2020-11-13T10:31:02+00:00
Returns this

### 
Temporary breakpoint 1, 0x0000555555934304 in main ()
(gdb) gdb -ex run ./monero-wallet-gui
Undefined command: "gdb".  Try "help".
(gdb) start
The program being debugged has been started already.
Start it from the beginning? (y or n) y
Temporary breakpoint 2 at 0x555555934304
Starting program: /home/c/Downloads/Mining/XMR/monero-gui-linux-x64-v0.17.1 (1).4/monero-gui-v0.17.1.4/monero-wallet-gui 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Temporary breakpoint 2, 0x0000555555934304 in main ()
(gdb) thread apply all bt

Thread 1 (Thread 0x7ffff774dc00 (LWP 5698)):
#0  0x0000555555934304 in main ()
(gdb) 


## xiphon | 2020-11-13T10:36:48+00:00
0. Open terminal
1. Run `gdb -ex run ./monero-wallet-gui`
2. Once it freezes, hit CTRL+C in terminal
3. `thread apply all bt`



## 3ach1T3ach1 | 2020-11-13T10:41:35+00:00

$ gdb -ex run ./monero-wallet-gui
GNU gdb (Ubuntu 9.1-0ubuntu1) 9.1
Copyright (C) 2020 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from ./monero-wallet-gui...
Starting program: /home/c/Downloads/Mining/XMR/monero-gui-linux-x64-v0.17.1 (1).4/monero-gui-v0.17.1.4/monero-wallet-gui 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
[New Thread 0x7ffff6916700 (LWP 5865)]
2020-11-13 10:38:54.588	W Qt:5.9.9 GUI:0.17.1.4-6fce5c7 | screen: 1920x1080 - dpi: 96 - ratio:0.731364
[New Thread 0x7ffff5e90700 (LWP 5866)]
[New Thread 0x7fffee5f7700 (LWP 5896)]
[New Thread 0x7fffeddf6700 (LWP 5897)]
[New Thread 0x7fffed5f5700 (LWP 5898)]
[New Thread 0x7fffecdf4700 (LWP 5899)]
[New Thread 0x7fffe356b700 (LWP 5900)]
[New Thread 0x7fffe2d6a700 (LWP 5901)]
[New Thread 0x7fffe2569700 (LWP 5902)]
2020-11-13 10:38:55.396	W Logging to "/home/c/.bitmonero/monero-wallet-gui.log"
2020-11-13 10:38:55.397	W qrc:/qt-project.org/imports/QtQuick/Controls/ApplicationWindow.qml:240:9: QML ContentItem: Binding loop detected for property "implicitWidth"
[New Thread 0x7fffe0571700 (LWP 5903)]
[New Thread 0x7fffba034700 (LWP 5904)]
[New Thread 0x7fffb9b33700 (LWP 5905)]
[New Thread 0x7fffb9632700 (LWP 5906)]
[New Thread 0x7fffb9131700 (LWP 5907)]
[New Thread 0x7fffb8c30700 (LWP 5908)]
[New Thread 0x7fffb872f700 (LWP 5909)]
[New Thread 0x7fffb822e700 (LWP 5910)]
[New Thread 0x7fffb7d2d700 (LWP 5911)]
[New Thread 0x7fffb782c700 (LWP 5912)]
[New Thread 0x7fffb732b700 (LWP 5913)]
[New Thread 0x7fffb62aa700 (LWP 5916)]
--Type <RET> for more, q to quit, c to continue without paging--thread apply all bt
 
Thread 1 "monero-wallet-g" received signal SIGINT, Interrupt.
futex_wait_cancelable (private=<optimized out>, expected=0, 
    futex_word=0x55555e1f9674) at ../sysdeps/nptl/futex-internal.h:183
183	../sysdeps/nptl/futex-internal.h: No such file or directory.
(gdb) 


## xiphon | 2020-11-13T10:43:10+00:00
> 
> 
> now enter
> 
> thread apply all bt



## 3ach1T3ach1 | 2020-11-13T10:47:52+00:00


(gdb) thread apply all bt

Thread 23 (Thread 0x7fffb5aa9700 (LWP 5917)):
#0  futex_abstimed_wait_cancelable (private=<optimized out>, abstime=0x7fffb5aa8b90, clockid=<optimized out>, expected=0, futex_word=0x7fffa0004758) at ../sysdeps/nptl/futex-internal.h:320
#1  __pthread_cond_wait_common (abstime=0x7fffb5aa8b90, clockid=<optimized out>, mutex=0x7fffa0004708, cond=0x7fffa0004730) at pthread_cond_wait.c:520
#2  __pthread_cond_timedwait (cond=0x7fffa0004730, mutex=0x7fffa0004708, abstime=0x7fffb5aa8b90) at pthread_cond_wait.c:656
#3  0x00005555559ed4d0 in Monero::WalletImpl::refreshThreadFunc() ()
#4  0x0000555556022b95 in thread_proxy ()
#5  0x00007ffff7daf609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff79fc103 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 22 (Thread 0x7fffb62aa700 (LWP 5916)):
#0  0x0000555555d0dfa3 in cn_slow_hash ()
#1  0x0000555555b70b08 in crypto::generate_chacha_key(void const*, unsigned long, epee::mlocked<tools::scrubbed<std::array<unsigned char, 32ul> > >&, unsigned long) ()
#2  0x0000555555ab1122 in tools::wallet2::load_keys_buf(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, epee::wipeable_string const&, boost::optional<epee::mlocked<tools::scrubbed<std::array<unsigned char, 32ul> > > >&) ()
#3  0x0000555555abd676 in tools::wallet2::load_keys(std::__cxx11::basic_string<char------------Type <RET> for more, q to quit, c to continue without paging--



## xiphon | 2020-11-13T10:59:02+00:00
`set pagination off`
`thread apply all bt`

## 3ach1T3ach1 | 2020-11-13T11:06:41+00:00
Question is it easier to read if I screen shot the terminal with the contrasting colors or just copy paste?


## 3ach1T3ach1 | 2020-11-13T11:07:18+00:00
set pagination off
, std::char_traits<char>, std::allocator<char> > const&, epee::wipeable_string const&) ()
#4  0x0000555555b26a64 in tools::wallet2::load(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, epee::wipeable_string const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) ()
#5  0x00005555559ea47d in Monero::WalletImpl::open(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) ()
#6  0x0000555555a17364 in Monero::WalletManagerImpl::openWallet(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, Monero::NetworkType, unsigned long, Monero::WalletListener*) ()
#7  0x00005555559684de in WalletManager::openWallet(QString const&, QString const&, NetworkType::Type, unsigned long long) ()
#8  0x00005555559688ec in std::_Function_handler<void (), WalletManager::openWalletAsync(QString const&, QString const&, NetworkType::Type, unsigned long long)::{lambda()#1}>::_M_invoke(std::_Any_data const&) ()
#9  0x000055555599bd07 in QtConcurrent::RunFunctionTask<void>::run() ()
#10 0x0000555556d22d97 in QThreadPoolThread::run() ()
#11 0x0000555556d26bb9 in QThreadPrivate::start(void*) ()
#12 0x00007ffff7daf609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#13 0x00007ffff79fc103 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 21 (Thread 0x7fffb732b700 (LWP 5913)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55555addf120 <tools::threadpool::getInstance()::instance+160>) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>, cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>) at pthread_cond_wait.c:638
#3  0x0000555555cf33c3 in tools::threadpool::run(bool) ()
#4  0x0000555556022b95 in thread_proxy ()
#5  0x00007ffff7daf609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff79fc103 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 20 (Thread 0x7fffb782c700 (LWP 5912)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55555addf120 <tools::threadpool::getInstance()::instance+160>) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>, cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>) at pthread_cond_wait.c:638
#3  0x0000555555cf33c3 in tools::threadpool::run(bool) ()
#4  0x0000555556022b95 in thread_proxy ()
#5  0x00007ffff7daf609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff79fc103 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 19 (Thread 0x7fffb7d2d700 (LWP 5911)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55555addf120 <tools::threadpool::getInstance()::instance+160>) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>, cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>) at pthread_cond_wait.c:638
#3  0x0000555555cf33c3 in tools::threadpool::run(bool) ()
#4  0x0000555556022b95 in thread_proxy ()
#5  0x00007ffff7daf609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff79fc103 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 18 (Thread 0x7fffb822e700 (LWP 5910)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55555addf120 <tools::threadpool::getInstance()::instance+160>) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>, cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>) at pthread_cond_wait.c:638
#3  0x0000555555cf33c3 in tools::threadpool::run(bool) ()
#4  0x0000555556022b95 in thread_proxy ()
#5  0x00007ffff7daf609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff79fc103 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95
--Type <RET> for more, q to quit, c to continue without paging-- thread apply all bt

Thread 17 (Thread 0x7fffb872f700 (LWP 5909)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55555addf120 <tools::threadpool::getInstance()::instance+160>) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>, cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>) at pthread_cond_wait.c:638
#3  0x0000555555cf33c3 in tools::threadpool::run(bool) ()
#4  0x0000555556022b95 in thread_proxy ()
#5  0x00007ffff7daf609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff79fc103 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 16 (Thread 0x7fffb8c30700 (LWP 5908)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55555addf120 <tools::threadpool::getInstance()::instance+160>) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>, cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>) at pthread_cond_wait.c:638
#3  0x0000555555cf33c3 in tools::threadpool::run(bool) ()
#4  0x0000555556022b95 in thread_proxy ()
#5  0x00007ffff7daf609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff79fc103 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 15 (Thread 0x7fffb9131700 (LWP 5907)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55555addf120 <tools::threadpool::getInstance()::instance+160>) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>, cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>) at pthread_cond_wait.c:638
#3  0x0000555555cf33c3 in tools::threadpool::run(bool) ()
#4  0x0000555556022b95 in thread_proxy ()
#5  0x00007ffff7daf609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff79fc103 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 14 (Thread 0x7fffb9632700 (LWP 5906)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55555addf124 <tools::threadpool::getInstance()::instance+164>) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>, cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>) at pthread_cond_wait.c:638
#3  0x0000555555cf33c3 in tools::threadpool::run(bool) ()
#4  0x0000555556022b95 in thread_proxy ()
#5  0x00007ffff7daf609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff79fc103 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 13 (Thread 0x7fffb9b33700 (LWP 5905)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55555addf124 <tools::threadpool::getInstance()::instance+164>) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>, cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>) at pthread_cond_wait.c:638
#3  0x0000555555cf33c3 in tools::threadpool::run(bool) ()
#4  0x0000555556022b95 in thread_proxy ()
#5  0x00007ffff7daf609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff79fc103 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 12 (Thread 0x7fffba034700 (LWP 5904)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55555addf124 <tools::threadpool::getInstance()::instance+164>) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>, cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>) at pthread_cond_wait.c:508
--Type <RET> for more, q to quit, c to continue without paging--



## xiphon | 2020-11-13T11:26:26+00:00
Please copy-paste the complete output.

## 3ach1T3ach1 | 2020-11-13T11:34:52+00:00
$ gdb -ex run ./monero-wallet-gui
GNU gdb (Ubuntu 9.1-0ubuntu1) 9.1
Copyright (C) 2020 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from ./monero-wallet-gui...
Starting program: /home/c/Downloads/Mining/XMR/monero-gui-linux-x64-v0.17.1 (1).4/monero-gui-v0.17.1.4/monero-wallet-gui 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
[New Thread 0x7ffff6916700 (LWP 5865)]
2020-11-13 10:38:54.588	W Qt:5.9.9 GUI:0.17.1.4-6fce5c7 | screen: 1920x1080 - dpi: 96 - ratio:0.731364
[New Thread 0x7ffff5e90700 (LWP 5866)]
[New Thread 0x7fffee5f7700 (LWP 5896)]
[New Thread 0x7fffeddf6700 (LWP 5897)]
[New Thread 0x7fffed5f5700 (LWP 5898)]
[New Thread 0x7fffecdf4700 (LWP 5899)]
[New Thread 0x7fffe356b700 (LWP 5900)]
[New Thread 0x7fffe2d6a700 (LWP 5901)]
[New Thread 0x7fffe2569700 (LWP 5902)]
2020-11-13 10:38:55.396	W Logging to "/home/c/.bitmonero/monero-wallet-gui.log"
2020-11-13 10:38:55.397	W qrc:/qt-project.org/imports/QtQuick/Controls/ApplicationWindow.qml:240:9: QML ContentItem: Binding loop detected for property "implicitWidth"
[New Thread 0x7fffe0571700 (LWP 5903)]
[New Thread 0x7fffba034700 (LWP 5904)]
[New Thread 0x7fffb9b33700 (LWP 5905)]
[New Thread 0x7fffb9632700 (LWP 5906)]
[New Thread 0x7fffb9131700 (LWP 5907)]
[New Thread 0x7fffb8c30700 (LWP 5908)]
[New Thread 0x7fffb872f700 (LWP 5909)]
[New Thread 0x7fffb822e700 (LWP 5910)]
[New Thread 0x7fffb7d2d700 (LWP 5911)]
[New Thread 0x7fffb782c700 (LWP 5912)]
[New Thread 0x7fffb732b700 (LWP 5913)]
[New Thread 0x7fffb62aa700 (LWP 5916)]
--Type <RET> for more, q to quit, c to continue without paging--thread apply all bt
 
Thread 1 "monero-wallet-g" received signal SIGINT, Interrupt.
futex_wait_cancelable (private=<optimized out>, expected=0, 
    futex_word=0x55555e1f9674) at ../sysdeps/nptl/futex-internal.h:183
183	../sysdeps/nptl/futex-internal.h: No such file or directory.
(gdb) thread apply all bt

Thread 23 (Thread 0x7fffb5aa9700 (LWP 5917)):
#0  futex_abstimed_wait_cancelable (private=<optimized out>, abstime=0x7fffb5aa8b90, clockid=<optimized out>, expected=0, futex_word=0x7fffa0004758) at ../sysdeps/nptl/futex-internal.h:320
#1  __pthread_cond_wait_common (abstime=0x7fffb5aa8b90, clockid=<optimized out>, mutex=0x7fffa0004708, cond=0x7fffa0004730) at pthread_cond_wait.c:520
#2  __pthread_cond_timedwait (cond=0x7fffa0004730, mutex=0x7fffa0004708, abstime=0x7fffb5aa8b90) at pthread_cond_wait.c:656
#3  0x00005555559ed4d0 in Monero::WalletImpl::refreshThreadFunc() ()
#4  0x0000555556022b95 in thread_proxy ()
#5  0x00007ffff7daf609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff79fc103 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 22 (Thread 0x7fffb62aa700 (LWP 5916)):
#0  0x0000555555d0dfa3 in cn_slow_hash ()
#1  0x0000555555b70b08 in crypto::generate_chacha_key(void const*, unsigned long, epee::mlocked<tools::scrubbed<std::array<unsigned char, 32ul> > >&, unsigned long) ()
#2  0x0000555555ab1122 in tools::wallet2::load_keys_buf(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, epee::wipeable_string const&, boost::optional<epee::mlocked<tools::scrubbed<std::array<unsigned char, 32ul> > > >&) ()
#3  0x0000555555abd676 in tools::wallet2::load_keys(std::__cxx11::basic_string<char------------T--Type <--Type <RE--Type <RET> --Type <RET> for --Type <RET--Type------T-------Ty--Ty--Ty---T----T--Type <RE--Type <RET> for more, q to quit, c to continue without paging--set pagination off
, std::char_traits<char>, std::allocator<char> > const&, epee::wipeable_string const&) ()
#4  0x0000555555b26a64 in tools::wallet2::load(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, epee::wipeable_string const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) ()
#5  0x00005555559ea47d in Monero::WalletImpl::open(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) ()
#6  0x0000555555a17364 in Monero::WalletManagerImpl::openWallet(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, Monero::NetworkType, unsigned long, Monero::WalletListener*) ()
#7  0x00005555559684de in WalletManager::openWallet(QString const&, QString const&, NetworkType::Type, unsigned long long) ()
#8  0x00005555559688ec in std::_Function_handler<void (), WalletManager::openWalletAsync(QString const&, QString const&, NetworkType::Type, unsigned long long)::{lambda()#1}>::_M_invoke(std::_Any_data const&) ()
#9  0x000055555599bd07 in QtConcurrent::RunFunctionTask<void>::run() ()
#10 0x0000555556d22d97 in QThreadPoolThread::run() ()
#11 0x0000555556d26bb9 in QThreadPrivate::start(void*) ()
#12 0x00007ffff7daf609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#13 0x00007ffff79fc103 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 21 (Thread 0x7fffb732b700 (LWP 5913)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55555addf120 <tools::threadpool::getInstance()::instance+160>) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>, cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>) at pthread_cond_wait.c:638
#3  0x0000555555cf33c3 in tools::threadpool::run(bool) ()
#4  0x0000555556022b95 in thread_proxy ()
#5  0x00007ffff7daf609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff79fc103 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 20 (Thread 0x7fffb782c700 (LWP 5912)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55555addf120 <tools::threadpool::getInstance()::instance+160>) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>, cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>) at pthread_cond_wait.c:638
#3  0x0000555555cf33c3 in tools::threadpool::run(bool) ()
#4  0x0000555556022b95 in thread_proxy ()
#5  0x00007ffff7daf609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff79fc103 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 19 (Thread 0x7fffb7d2d700 (LWP 5911)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55555addf120 <tools::threadpool::getInstance()::instance+160>) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>, cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>) at pthread_cond_wait.c:638
#3  0x0000555555cf33c3 in tools::threadpool::run(bool) ()
#4  0x0000555556022b95 in thread_proxy ()
#5  0x00007ffff7daf609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff79fc103 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 18 (Thread 0x7fffb822e700 (LWP 5910)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55555addf120 <tools::threadpool::getInstance()::instance+160>) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>, cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>) at pthread_cond_wait.c:638
#3  0x0000555555cf33c3 in tools::threadpool::run(bool) ()
#4  0x0000555556022b95 in thread_proxy ()
#5  0x00007ffff7daf609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff79fc103 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95
--Type <RET> for more, q to quit, c to continue without paging-- thread apply all bt

Thread 17 (Thread 0x7fffb872f700 (LWP 5909)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55555addf120 <tools::threadpool::getInstance()::instance+160>) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>, cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>) at pthread_cond_wait.c:638
#3  0x0000555555cf33c3 in tools::threadpool::run(bool) ()
#4  0x0000555556022b95 in thread_proxy ()
#5  0x00007ffff7daf609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff79fc103 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 16 (Thread 0x7fffb8c30700 (LWP 5908)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55555addf120 <tools::threadpool::getInstance()::instance+160>) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>, cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>) at pthread_cond_wait.c:638
#3  0x0000555555cf33c3 in tools::threadpool::run(bool) ()
#4  0x0000555556022b95 in thread_proxy ()
#5  0x00007ffff7daf609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff79fc103 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 15 (Thread 0x7fffb9131700 (LWP 5907)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55555addf120 <tools::threadpool::getInstance()::instance+160>) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>, cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>) at pthread_cond_wait.c:638
#3  0x0000555555cf33c3 in tools::threadpool::run(bool) ()
#4  0x0000555556022b95 in thread_proxy ()
#5  0x00007ffff7daf609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff79fc103 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 14 (Thread 0x7fffb9632700 (LWP 5906)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55555addf124 <tools::threadpool::getInstance()::instance+164>) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>, cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>) at pthread_cond_wait.c:638
#3  0x0000555555cf33c3 in tools::threadpool::run(bool) ()
#4  0x0000555556022b95 in thread_proxy ()
#5  0x00007ffff7daf609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff79fc103 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 13 (Thread 0x7fffb9b33700 (LWP 5905)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55555addf124 <tools::threadpool::getInstance()::instance+164>) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>, cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>) at pthread_cond_wait.c:638
#3  0x0000555555cf33c3 in tools::threadpool::run(bool) ()
#4  0x0000555556022b95 in thread_proxy ()
#5  0x00007ffff7daf609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff79fc103 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 12 (Thread 0x7fffba034700 (LWP 5904)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55555addf124 <tools::threadpool::getInstance()::instance+164>) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>, cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>) at pthread_cond_wait.c:508
--Type <RET> for more, q to quit, c to continue without paging--


## selsta | 2020-11-13T11:43:33+00:00
if you press "c" it should show you all the text, please copy it here, almost done :)

## 3ach1T3ach1 | 2020-11-13T11:47:02+00:00
$ gdb -ex run ./monero-wallet-gui
GNU gdb (Ubuntu 9.1-0ubuntu1) 9.1
Copyright (C) 2020 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from ./monero-wallet-gui...
Starting program: /home/c/Downloads/Mining/XMR/monero-gui-linux-x64-v0.17.1 (1).4/monero-gui-v0.17.1.4/monero-wallet-gui 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
[New Thread 0x7ffff6916700 (LWP 5865)]
2020-11-13 10:38:54.588	W Qt:5.9.9 GUI:0.17.1.4-6fce5c7 | screen: 1920x1080 - dpi: 96 - ratio:0.731364
[New Thread 0x7ffff5e90700 (LWP 5866)]
[New Thread 0x7fffee5f7700 (LWP 5896)]
[New Thread 0x7fffeddf6700 (LWP 5897)]
[New Thread 0x7fffed5f5700 (LWP 5898)]
[New Thread 0x7fffecdf4700 (LWP 5899)]
[New Thread 0x7fffe356b700 (LWP 5900)]
[New Thread 0x7fffe2d6a700 (LWP 5901)]
[New Thread 0x7fffe2569700 (LWP 5902)]
2020-11-13 10:38:55.396	W Logging to "/home/c/.bitmonero/monero-wallet-gui.log"
2020-11-13 10:38:55.397	W qrc:/qt-project.org/imports/QtQuick/Controls/ApplicationWindow.qml:240:9: QML ContentItem: Binding loop detected for property "implicitWidth"
[New Thread 0x7fffe0571700 (LWP 5903)]
[New Thread 0x7fffba034700 (LWP 5904)]
[New Thread 0x7fffb9b33700 (LWP 5905)]
[New Thread 0x7fffb9632700 (LWP 5906)]
[New Thread 0x7fffb9131700 (LWP 5907)]
[New Thread 0x7fffb8c30700 (LWP 5908)]
[New Thread 0x7fffb872f700 (LWP 5909)]
[New Thread 0x7fffb822e700 (LWP 5910)]
[New Thread 0x7fffb7d2d700 (LWP 5911)]
[New Thread 0x7fffb782c700 (LWP 5912)]
[New Thread 0x7fffb732b700 (LWP 5913)]
[New Thread 0x7fffb62aa700 (LWP 5916)]
--Type <RET> for more, q to quit, c to continue without paging--thread apply all bt
 
Thread 1 "monero-wallet-g" received signal SIGINT, Interrupt.
futex_wait_cancelable (private=<optimized out>, expected=0, 
    futex_word=0x55555e1f9674) at ../sysdeps/nptl/futex-internal.h:183
183	../sysdeps/nptl/futex-internal.h: No such file or directory.
(gdb) thread apply all bt

Thread 23 (Thread 0x7fffb5aa9700 (LWP 5917)):
#0  futex_abstimed_wait_cancelable (private=<optimized out>, abstime=0x7fffb5aa8b90, clockid=<optimized out>, expected=0, futex_word=0x7fffa0004758) at ../sysdeps/nptl/futex-internal.h:320
#1  __pthread_cond_wait_common (abstime=0x7fffb5aa8b90, clockid=<optimized out>, mutex=0x7fffa0004708, cond=0x7fffa0004730) at pthread_cond_wait.c:520
#2  __pthread_cond_timedwait (cond=0x7fffa0004730, mutex=0x7fffa0004708, abstime=0x7fffb5aa8b90) at pthread_cond_wait.c:656
#3  0x00005555559ed4d0 in Monero::WalletImpl::refreshThreadFunc() ()
#4  0x0000555556022b95 in thread_proxy ()
#5  0x00007ffff7daf609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff79fc103 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 22 (Thread 0x7fffb62aa700 (LWP 5916)):
#0  0x0000555555d0dfa3 in cn_slow_hash ()
#1  0x0000555555b70b08 in crypto::generate_chacha_key(void const*, unsigned long, epee::mlocked<tools::scrubbed<std::array<unsigned char, 32ul> > >&, unsigned long) ()
#2  0x0000555555ab1122 in tools::wallet2::load_keys_buf(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, epee::wipeable_string const&, boost::optional<epee::mlocked<tools::scrubbed<std::array<unsigned char, 32ul> > > >&) ()
#3  0x0000555555abd676 in tools::wallet2::load_keys(std::__cxx11::basic_string<char------------T--Type <--Type <RE--Type <RET> --Type <RET> for --Type <RET--Type------T-------Ty--Ty--Ty---T----T--Type <RE--Type <RET> for more, q to quit, c to continue without paging--set pagination off
, std::char_traits<char>, std::allocator<char> > const&, epee::wipeable_string const&) ()
#4  0x0000555555b26a64 in tools::wallet2::load(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, epee::wipeable_string const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) ()
#5  0x00005555559ea47d in Monero::WalletImpl::open(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) ()
#6  0x0000555555a17364 in Monero::WalletManagerImpl::openWallet(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, Monero::NetworkType, unsigned long, Monero::WalletListener*) ()
#7  0x00005555559684de in WalletManager::openWallet(QString const&, QString const&, NetworkType::Type, unsigned long long) ()
#8  0x00005555559688ec in std::_Function_handler<void (), WalletManager::openWalletAsync(QString const&, QString const&, NetworkType::Type, unsigned long long)::{lambda()#1}>::_M_invoke(std::_Any_data const&) ()
#9  0x000055555599bd07 in QtConcurrent::RunFunctionTask<void>::run() ()
#10 0x0000555556d22d97 in QThreadPoolThread::run() ()
#11 0x0000555556d26bb9 in QThreadPrivate::start(void*) ()
#12 0x00007ffff7daf609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#13 0x00007ffff79fc103 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 21 (Thread 0x7fffb732b700 (LWP 5913)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55555addf120 <tools::threadpool::getInstance()::instance+160>) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>, cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>) at pthread_cond_wait.c:638
#3  0x0000555555cf33c3 in tools::threadpool::run(bool) ()
#4  0x0000555556022b95 in thread_proxy ()
#5  0x00007ffff7daf609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff79fc103 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 20 (Thread 0x7fffb782c700 (LWP 5912)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55555addf120 <tools::threadpool::getInstance()::instance+160>) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>, cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>) at pthread_cond_wait.c:638
#3  0x0000555555cf33c3 in tools::threadpool::run(bool) ()
#4  0x0000555556022b95 in thread_proxy ()
#5  0x00007ffff7daf609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff79fc103 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 19 (Thread 0x7fffb7d2d700 (LWP 5911)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55555addf120 <tools::threadpool::getInstance()::instance+160>) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>, cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>) at pthread_cond_wait.c:638
#3  0x0000555555cf33c3 in tools::threadpool::run(bool) ()
#4  0x0000555556022b95 in thread_proxy ()
#5  0x00007ffff7daf609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff79fc103 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 18 (Thread 0x7fffb822e700 (LWP 5910)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55555addf120 <tools::threadpool::getInstance()::instance+160>) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>, cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>) at pthread_cond_wait.c:638
#3  0x0000555555cf33c3 in tools::threadpool::run(bool) ()
#4  0x0000555556022b95 in thread_proxy ()
#5  0x00007ffff7daf609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff79fc103 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95
--Type <RET> for more, q to quit, c to continue without paging-- thread apply all bt

Thread 17 (Thread 0x7fffb872f700 (LWP 5909)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55555addf120 <tools::threadpool::getInstance()::instance+160>) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>, cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>) at pthread_cond_wait.c:638
#3  0x0000555555cf33c3 in tools::threadpool::run(bool) ()
#4  0x0000555556022b95 in thread_proxy ()
#5  0x00007ffff7daf609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff79fc103 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 16 (Thread 0x7fffb8c30700 (LWP 5908)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55555addf120 <tools::threadpool::getInstance()::instance+160>) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>, cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>) at pthread_cond_wait.c:638
#3  0x0000555555cf33c3 in tools::threadpool::run(bool) ()
#4  0x0000555556022b95 in thread_proxy ()
#5  0x00007ffff7daf609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff79fc103 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 15 (Thread 0x7fffb9131700 (LWP 5907)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55555addf120 <tools::threadpool::getInstance()::instance+160>) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>, cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>) at pthread_cond_wait.c:638
#3  0x0000555555cf33c3 in tools::threadpool::run(bool) ()
#4  0x0000555556022b95 in thread_proxy ()
#5  0x00007ffff7daf609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff79fc103 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 14 (Thread 0x7fffb9632700 (LWP 5906)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55555addf124 <tools::threadpool::getInstance()::instance+164>) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>, cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>) at pthread_cond_wait.c:638
#3  0x0000555555cf33c3 in tools::threadpool::run(bool) ()
#4  0x0000555556022b95 in thread_proxy ()
#5  0x00007ffff7daf609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff79fc103 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 13 (Thread 0x7fffb9b33700 (LWP 5905)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55555addf124 <tools::threadpool::getInstance()::instance+164>) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>, cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>) at pthread_cond_wait.c:638
#3  0x0000555555cf33c3 in tools::threadpool::run(bool) ()
#4  0x0000555556022b95 in thread_proxy ()
#5  0x00007ffff7daf609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff79fc103 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 12 (Thread 0x7fffba034700 (LWP 5904)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55555addf124 <tools::threadpool::getInstance()::instance+164>) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>, cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>) at pthread_cond_wait.c:508
--Type <RET> for more, q to quit, c to continue without paging--c
#2  __pthread_cond_wait (cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>) at pthread_cond_wait.c:638
#3  0x0000555555cf33c3 in tools::threadpool::run(bool) ()
#4  0x0000555556022b95 in thread_proxy ()
#5  0x00007ffff7daf609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff79fc103 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 11 (Thread 0x7fffe0571700 (LWP 5903)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55555addf124 <tools::threadpool::getInstance()::instance+164>) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>, cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>) at pthread_cond_wait.c:638
#3  0x0000555555cf33c3 in tools::threadpool::run(bool) ()
#4  0x0000555556022b95 in thread_proxy ()
#5  0x00007ffff7daf609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff79fc103 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 10 (Thread 0x7fffe2569700 (LWP 5902)):
#0  0x00007ffff79ef96f in __GI___poll (fds=0x7fffc80029e0, nfds=1, timeout=9992) at ../sysdeps/unix/sysv/linux/poll.c:29
#1  0x00007ffff7e1b1ae in ?? () from /lib/x86_64-linux-gnu/libglib-2.0.so.0
#2  0x00007ffff7e1b2e3 in g_main_context_iteration () from /lib/x86_64-linux-gnu/libglib-2.0.so.0
#3  0x0000555556f4f7cf in QEventDispatcherGlib::processEvents(QFlags<QEventLoop::ProcessEventsFlag>) ()
#4  0x0000555556ef5935 in QEventLoop::exec(QFlags<QEventLoop::ProcessEventsFlag>) ()
#5  0x0000555556d21854 in QThread::run() ()
#6  0x0000555556d26bb9 in QThreadPrivate::start(void*) ()
#7  0x00007ffff7daf609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#8  0x00007ffff79fc103 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 9 (Thread 0x7fffe2d6a700 (LWP 5901)):
#0  0x00005555561b7b98 in bn_mul_add_words ()
#1  0x00005555560e2d98 in bn_from_montgomery_word ()
#2  0x00005555560e2c1c in bn_mul_mont_fixed_top ()
#3  0x00005555561ca6fc in BN_mod_exp_mont_consttime ()
#4  0x00005555561c951f in BN_mod_exp_mont ()
#5  0x00005555561d1178 in witness ()
#6  0x00005555561d1098 in BN_is_prime_fasttest_ex ()
#7  0x00005555561d0b58 in BN_generate_prime_ex ()
#8  0x0000555556152a6f in rsa_builtin_keygen ()
#9  0x00005555561524bf in RSA_generate_multi_prime_key ()
#10 0x0000555556152416 in RSA_generate_key_ex ()
#11 0x0000555555f2e32a in epee::net_utils::create_rsa_ssl_certificate(evp_pkey_st*&, x509_st*&) ()
#12 0x0000555555f30dc0 in epee::net_utils::ssl_options_t::create_context() const ()
#13 0x00005555559af9df in epee::net_utils::http::http_simple_client_template<epee::net_utils::blocked_mode_client>::set_server(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, boost::optional<epee::net_utils::http::login>, epee::net_utils::ssl_options_t) ()
#14 0x0000555555f11b1b in epee::net_utils::http::abstract_http_client::set_server(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, boost::optional<epee::net_utils::http::login>, epee::net_utils::ssl_options_t) ()
#15 0x0000555555a14702 in Monero::WalletManagerImpl::setDaemonAddress(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) ()
#16 0x000055555596762a in std::_Function_handler<void (), WalletManager::setDaemonAddressAsync(QString const&)::{lambda()#1}>::_M_invoke(std::_Any_data const&) ()
#17 0x000055555599bd07 in QtConcurrent::RunFunctionTask<void>::run() ()
#18 0x0000555556d22d97 in QThreadPoolThread::run() ()
#19 0x0000555556d26bb9 in QThreadPrivate::start(void*) ()
#20 0x00007ffff7daf609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#21 0x00007ffff79fc103 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 8 (Thread 0x7fffe356b700 (LWP 5900)):
#0  0x00007ffff79ef96f in __GI___poll (fds=0x7fffd0004a20, nfds=1, timeout=-1) at ../sysdeps/unix/sysv/linux/poll.c:29
#1  0x00007ffff7e1b1ae in ?? () from /lib/x86_64-linux-gnu/libglib-2.0.so.0
#2  0x00007ffff7e1b2e3 in g_main_context_iteration () from /lib/x86_64-linux-gnu/libglib-2.0.so.0
#3  0x0000555556f4f7cf in QEventDispatcherGlib::processEvents(QFlags<QEventLoop::ProcessEventsFlag>) ()
#4  0x0000555556ef5935 in QEventLoop::exec(QFlags<QEventLoop::ProcessEventsFlag>) ()
#5  0x0000555556d21724 in QThread::exec() ()
#6  0x00005555563211f5 in QQuickXmlQueryEngine::run() ()
#7  0x0000555556d26bb9 in QThreadPrivate::start(void*) ()
#8  0x00007ffff7daf609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#9  0x00007ffff79fc103 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 7 (Thread 0x7fffecdf4700 (LWP 5899)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55555af6cd28) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x55555af6ccd8, cond=0x55555af6cd00) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x55555af6cd00, mutex=0x55555af6ccd8) at pthread_cond_wait.c:638
#3  0x00007fffeedfe62b in ?? () from /usr/lib/x86_64-linux-gnu/dri/nouveau_dri.so
#4  0x00007fffeedfe23b in ?? () from /usr/lib/x86_64-linux-gnu/dri/nouveau_dri.so
#5  0x00007ffff7daf609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff79fc103 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 6 (Thread 0x7fffed5f5700 (LWP 5898)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55555af6cd28) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x55555af6ccd8, cond=0x55555af6cd00) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x55555af6cd00, mutex=0x55555af6ccd8) at pthread_cond_wait.c:638
#3  0x00007fffeedfe62b in ?? () from /usr/lib/x86_64-linux-gnu/dri/nouveau_dri.so
#4  0x00007fffeedfe23b in ?? () from /usr/lib/x86_64-linux-gnu/dri/nouveau_dri.so
#5  0x00007ffff7daf609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff79fc103 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 5 (Thread 0x7fffeddf6700 (LWP 5897)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55555af6cd28) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x55555af6ccd8, cond=0x55555af6cd00) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x55555af6cd00, mutex=0x55555af6ccd8) at pthread_cond_wait.c:638
#3  0x00007fffeedfe62b in ?? () from /usr/lib/x86_64-linux-gnu/dri/nouveau_dri.so
#4  0x00007fffeedfe23b in ?? () from /usr/lib/x86_64-linux-gnu/dri/nouveau_dri.so
#5  0x00007ffff7daf609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff79fc103 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 4 (Thread 0x7fffee5f7700 (LWP 5896)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55555af6cd28) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x55555af6ccd8, cond=0x55555af6cd00) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x55555af6cd00, mutex=0x55555af6ccd8) at pthread_cond_wait.c:638
#3  0x00007fffeedfe62b in ?? () from /usr/lib/x86_64-linux-gnu/dri/nouveau_dri.so
#4  0x00007fffeedfe23b in ?? () from /usr/lib/x86_64-linux-gnu/dri/nouveau_dri.so
#5  0x00007ffff7daf609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff79fc103 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 3 (Thread 0x7ffff5e90700 (LWP 5866)):
#0  0x00007ffff79ef96f in __GI___poll (fds=0x7fffe80029e0, nfds=1, timeout=-1) at ../sysdeps/unix/sysv/linux/poll.c:29
#1  0x00007ffff7e1b1ae in ?? () from /lib/x86_64-linux-gnu/libglib-2.0.so.0
#2  0x00007ffff7e1b2e3 in g_main_context_iteration () from /lib/x86_64-linux-gnu/libglib-2.0.so.0
#3  0x0000555556f4f7cf in QEventDispatcherGlib::processEvents(QFlags<QEventLoop::ProcessEventsFlag>) ()
#4  0x0000555556ef5935 in QEventLoop::exec(QFlags<QEventLoop::ProcessEventsFlag>) ()
#5  0x0000555556d21724 in QThread::exec() ()
#6  0x0000555556b0b0d5 in QQmlThreadPrivate::run() ()
#7  0x0000555556d26bb9 in QThreadPrivate::start(void*) ()
#8  0x00007ffff7daf609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#9  0x00007ffff79fc103 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 2 (Thread 0x7ffff6916700 (LWP 5865)):
#0  0x00007ffff79ef96f in __GI___poll (fds=0x7ffff6915ce8, nfds=1, timeout=-1) at ../sysdeps/unix/sysv/linux/poll.c:29
#1  0x00007ffff7ad7c1a in ?? () from /lib/x86_64-linux-gnu/libxcb.so.1
#2  0x00007ffff7ad990a in xcb_wait_for_event () from /lib/x86_64-linux-gnu/libxcb.so.1
#3  0x00005555577f27f9 in QXcbEventReader::run() ()
#4  0x0000555556d26bb9 in QThreadPrivate::start(void*) ()
#5  0x00007ffff7daf609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff79fc103 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 1 (Thread 0x7ffff774dc00 (LWP 5861)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55555e1f9674) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x55555aeef158, cond=0x55555e1f9648) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x55555e1f9648, mutex=0x55555aeef158) at pthread_cond_wait.c:638
#3  0x00007ffff7ad7df0 in ?? () from /lib/x86_64-linux-gnu/libxcb.so.1
#4  0x00007ffff7ad9a02 in xcb_wait_for_special_event () from /lib/x86_64-linux-gnu/libxcb.so.1
#5  0x00007ffff44d841e in glPrimitiveBoundingBox () from /lib/x86_64-linux-gnu/libGLX_mesa.so.0
#6  0x00007ffff44d8588 in glPrimitiveBoundingBox () from /lib/x86_64-linux-gnu/libGLX_mesa.so.0
#7  0x00007ffff44d974e in glPrimitiveBoundingBox () from /lib/x86_64-linux-gnu/libGLX_mesa.so.0
#8  0x00007ffff44da6ac in glPrimitiveBoundingBox () from /lib/x86_64-linux-gnu/libGLX_mesa.so.0
#9  0x00007fffeea876b3 in ?? () from /usr/lib/x86_64-linux-gnu/dri/nouveau_dri.so
#10 0x00007fffeea897f4 in ?? () from /usr/lib/x86_64-linux-gnu/dri/nouveau_dri.so
#11 0x00007fffeea9591c in ?? () from /usr/lib/x86_64-linux-gnu/dri/nouveau_dri.so
#12 0x00007fffeea95f90 in ?? () from /usr/lib/x86_64-linux-gnu/dri/nouveau_dri.so
#13 0x00007fffeeab9b85 in ?? () from /usr/lib/x86_64-linux-gnu/dri/nouveau_dri.so
#14 0x00007fffeeabe706 in ?? () from /usr/lib/x86_64-linux-gnu/dri/nouveau_dri.so
#15 0x00005555565ac6da in QSGBatchRenderer::Renderer::renderBatches() ()
#16 0x00005555565b2214 in QSGBatchRenderer::Renderer::render() ()
#17 0x00005555564aed42 in QSGRenderer::renderScene(QSGBindable const&) ()
#18 0x00005555564af21b in QSGRenderer::renderScene(unsigned int) ()
#19 0x00005555564cbf5e in QSGDefaultRenderContext::renderNextFrame(QSGRenderer*, unsigned int) ()
#20 0x00005555563c6062 in QQuickWindowPrivate::renderSceneGraph(QSize const&) ()
#21 0x00005555564c1720 in QSGGuiThreadRenderLoop::renderWindow(QQuickWindow*) ()
#22 0x00005555563d0527 in QQuickWindow::event(QEvent*) ()
#23 0x000055555720d2cc in QApplicationPrivate::notify_helper(QObject*, QEvent*) ()
#24 0x00005555572148cc in QApplication::notify(QObject*, QEvent*) ()
#25 0x0000555556ef7ab8 in QCoreApplication::notifyInternal2(QObject*, QEvent*) ()
#26 0x0000555556601846 in QWindow::event(QEvent*) ()
#27 0x00005555563d04d5 in QQuickWindow::event(QEvent*) ()
#28 0x000055555720d2cc in QApplicationPrivate::notify_helper(QObject*, QEvent*) ()
#29 0x00005555572148cc in QApplication::notify(QObject*, QEvent*) ()
#30 0x0000555556ef7ab8 in QCoreApplication::notifyInternal2(QObject*, QEvent*) ()
#31 0x0000555556f4ea4e in QTimerInfoList::activateTimers() ()
#32 0x0000555556f4f429 in idleTimerSourceDispatch(_GSource*, int (*)(void*), void*) ()
#33 0x00007ffff7e1afbd in g_main_context_dispatch () from /lib/x86_64-linux-gnu/libglib-2.0.so.0
#34 0x00007ffff7e1b240 in ?? () from /lib/x86_64-linux-gnu/libglib-2.0.so.0
#35 0x00007ffff7e1b2e3 in g_main_context_iteration () from /lib/x86_64-linux-gnu/libglib-2.0.so.0
#36 0x0000555556f4f7cf in QEventDispatcherGlib::processEvents(QFlags<QEventLoop::ProcessEventsFlag>) ()
#37 0x0000555556ef5935 in QEventLoop::exec(QFlags<QEventLoop::ProcessEventsFlag>) ()
#38 0x0000555556eff298 in QCoreApplication::exec() ()
#39 0x00005555559367ef in main ()
(gdb) 


## 3ach1T3ach1 | 2020-11-14T09:59:16+00:00
Any idea on a fix? @xiphon @selsta 

## selsta | 2020-11-14T10:00:58+00:00
@xiphon will have to take a look at the logs. 

Can you open non Ledger wallets fine?

## 3ach1T3ach1 | 2020-11-14T10:52:24+00:00
Yes I can open the ledger GUI it's just the monero-gui.Appimage that I cant


## xiphon | 2020-11-14T12:02:52+00:00
Now, let it run for a while and collect the stack trace.

0. Open terminal
1. Run `gdb -ex run ./monero-wallet-gui`
2. Let it run for 5 minutes
3. Hit CTRL+C in terminal
4. `thread apply all bt`


## 3ach1T3ach1 | 2020-11-14T15:31:40+00:00
@xiphon 

$ gdb -ex run ./monero-wallet-gui
GNU gdb (Ubuntu 9.2-0ubuntu1~20.04) 9.2
Copyright (C) 2020 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from ./monero-wallet-gui...
Starting program: /home/c/Downloads/Mining/XMR/monero-gui-linux-x64-v0.17.1 (1).4/monero-gui-v0.17.1.4/monero-wallet-gui 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
[New Thread 0x7ffff7183700 (LWP 22068)]
2020-11-14 15:23:17.215	W Qt:5.9.9 GUI:0.17.1.4-6fce5c7 | screen: 1920x1080 - dpi: 96 - ratio:0.731364
[New Thread 0x7ffff66fd700 (LWP 22071)]
[New Thread 0x7fffee981700 (LWP 22097)]
[New Thread 0x7fffee180700 (LWP 22098)]
[New Thread 0x7fffed97f700 (LWP 22099)]
[New Thread 0x7fffed17e700 (LWP 22100)]
[New Thread 0x7fffe396b700 (LWP 22101)]
[New Thread 0x7fffe316a700 (LWP 22102)]
[New Thread 0x7fffe2969700 (LWP 22103)]
2020-11-14 15:23:18.200	W Logging to "/home/c/.bitmonero/monero-wallet-gui.log"
2020-11-14 15:23:18.201	W qrc:/qt-project.org/imports/QtQuick/Controls/ApplicationWindow.qml:240:9: QML ContentItem: Binding loop detected for property "implicitWidth"
[New Thread 0x7fffe0d71700 (LWP 22104)]
[New Thread 0x7fffe0870700 (LWP 22105)]
[New Thread 0x7fffba034700 (LWP 22106)]
[New Thread 0x7fffb9b33700 (LWP 22107)]
[New Thread 0x7fffb9632700 (LWP 22108)]
[New Thread 0x7fffb9131700 (LWP 22109)]
[New Thread 0x7fffb8c30700 (LWP 22110)]
[New Thread 0x7fffb872f700 (LWP 22111)]
[New Thread 0x7fffb822e700 (LWP 22112)]
[New Thread 0x7fffb7d2d700 (LWP 22113)]
[New Thread 0x7fffb782c700 (LWP 22114)]
[Thread 0x7fffe316a700 (LWP 22102) exited]
[New Thread 0x7fffe316a700 (LWP 22135)]
[New Thread 0x7fffb692b700 (LWP 22136)]
[New Thread 0x7fffb612a700 (LWP 22137)]
[Thread 0x7fffe316a700 (LWP 22135) exited]
^C--Type <RET> for more, q to quit, c to continue without paging--c

Thread 1 "monero-wallet-g" received signal SIGINT, Interrupt.
futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55555e1d4a40) at ../sysdeps/nptl/futex-internal.h:183
183	../sysdeps/nptl/futex-internal.h: No such file or directory.
(gdb) 


## xiphon | 2020-11-14T15:59:45+00:00
`thread apply all bt`

## 3ach1T3ach1 | 2020-11-14T17:23:17+00:00
@xiphon 

gdb -ex run ./monero-wallet-gui
GNU gdb (Ubuntu 9.2-0ubuntu1~20.04) 9.2
Copyright (C) 2020 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from ./monero-wallet-gui...
Starting program: /home/c/Downloads/Mining/XMR/monero-gui-linux-x64-v0.17.1 (1).4/monero-gui-v0.17.1.4/monero-wallet-gui 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
[New Thread 0x7ffff7183700 (LWP 26621)]
2020-11-14 17:12:48.403	W Qt:5.9.9 GUI:0.17.1.4-6fce5c7 | screen: 1920x1080 - dpi: 96 - ratio:0.731364
[New Thread 0x7ffff66fd700 (LWP 26622)]
[New Thread 0x7fffee981700 (LWP 26649)]
[New Thread 0x7fffee180700 (LWP 26650)]
[New Thread 0x7fffed97f700 (LWP 26651)]
[New Thread 0x7fffed17e700 (LWP 26652)]
[New Thread 0x7fffe396b700 (LWP 26653)]
[New Thread 0x7fffe316a700 (LWP 26654)]
[New Thread 0x7fffe2969700 (LWP 26655)]
2020-11-14 17:12:49.239	W Logging to "/home/c/.bitmonero/monero-wallet-gui.log"
2020-11-14 17:12:49.240	W qrc:/qt-project.org/imports/QtQuick/Controls/ApplicationWindow.qml:240:9: QML ContentItem: Binding loop detected for property "implicitWidth"
[New Thread 0x7fffe0d71700 (LWP 26656)]
[New Thread 0x7fffe0870700 (LWP 26657)]
[New Thread 0x7fffba034700 (LWP 26658)]
[New Thread 0x7fffb9b33700 (LWP 26659)]
[New Thread 0x7fffb9632700 (LWP 26660)]
[New Thread 0x7fffb9131700 (LWP 26661)]
[New Thread 0x7fffb8c30700 (LWP 26662)]
[New Thread 0x7fffb872f700 (LWP 26663)]
[New Thread 0x7fffb822e700 (LWP 26664)]
[New Thread 0x7fffb7d2d700 (LWP 26665)]
[New Thread 0x7fffb782c700 (LWP 26666)]
[New Thread 0x7fffb692b700 (LWP 26670)]
[New Thread 0x7fffb612a700 (LWP 26671)]
[Thread 0x7fffe316a700 (LWP 26654) exited]
^C--Type <RET> for more, q to quit, c to continue without paging--thread apply all bt

Thread 1 "monero-wallet-g" received signal SIGINT, Interrupt.
futex_wait_cancelable (private=<optimized out>, expected=0, 
    futex_word=0x55555e1ee250) at ../sysdeps/nptl/futex-internal.h:183
183	../sysdeps/nptl/futex-internal.h: No such file or directory.
(gdb) thread apply all bt

Thread 23 (Thread 0x7fffb612a700 (LWP 26671)):
#0  futex_abstimed_wait_cancelable (private=<optimized out>, abstime=0x7fffb6129b90, clockid=<optimized out>, expected=0, futex_word=0x7fffa4004758) at ../sysdeps/nptl/futex-internal.h:320
#1  __pthread_cond_wait_common (abstime=0x7fffb6129b90, clockid=<optimized out>, mutex=0x7fffa4004708, cond=0x7fffa4004730) at pthread_cond_wait.c:520
#2  __pthread_cond_timedwait (cond=0x7fffa4004730, mutex=0x7fffa4004708, abstime=0x7fffb6129b90) at pthread_cond_wait.c:656
#3  0x00005555559ed4d0 in Monero::WalletImpl::refreshThreadFunc() ()
#4  0x0000555556022b95 in thread_proxy ()
#5  0x00007ffff7dae609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff79fb293 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 22 (Thread 0x7fffb692b700 (LWP 26670)):
#0  0x0000555555d0e41f in cn_slow_hash ()
#1  0x0000555555b70b08 in crypto::generate_chacha_key(void const*, unsigned long, epee::mlocked<tools::scrubbed<std::array<unsigned char, 32ul> > >&, unsigned long) ()
#2  0x0000555555ab1122 in tools::wallet2::load_keys_buf(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, epee::wipeable_s--Type <RET> for more, q to quit, c to continue without paging--c
tring const&, boost::optional<epee::mlocked<tools::scrubbed<std::array<unsigned char, 32ul> > > >&) ()
#3  0x0000555555abd676 in tools::wallet2::load_keys(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, epee::wipeable_string const&) ()
#4  0x0000555555b26a64 in tools::wallet2::load(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, epee::wipeable_string const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) ()
#5  0x00005555559ea47d in Monero::WalletImpl::open(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) ()
#6  0x0000555555a17364 in Monero::WalletManagerImpl::openWallet(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, Monero::NetworkType, unsigned long, Monero::WalletListener*) ()
#7  0x00005555559684de in WalletManager::openWallet(QString const&, QString const&, NetworkType::Type, unsigned long long) ()
#8  0x00005555559688ec in std::_Function_handler<void (), WalletManager::openWalletAsync(QString const&, QString const&, NetworkType::Type, unsigned long long)::{lambda()#1}>::_M_invoke(std::_Any_data const&) ()
#9  0x000055555599bd07 in QtConcurrent::RunFunctionTask<void>::run() ()
#10 0x0000555556d22d97 in QThreadPoolThread::run() ()
#11 0x0000555556d26bb9 in QThreadPrivate::start(void*) ()
#12 0x00007ffff7dae609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#13 0x00007ffff79fb293 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 21 (Thread 0x7fffb782c700 (LWP 26666)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55555addf120 <tools::threadpool::getInstance()::instance+160>) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>, cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>) at pthread_cond_wait.c:638
#3  0x0000555555cf33c3 in tools::threadpool::run(bool) ()
#4  0x0000555556022b95 in thread_proxy ()
#5  0x00007ffff7dae609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff79fb293 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 20 (Thread 0x7fffb7d2d700 (LWP 26665)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55555addf120 <tools::threadpool::getInstance()::instance+160>) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>, cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>) at pthread_cond_wait.c:638
#3  0x0000555555cf33c3 in tools::threadpool::run(bool) ()
#4  0x0000555556022b95 in thread_proxy ()
#5  0x00007ffff7dae609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff79fb293 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 19 (Thread 0x7fffb822e700 (LWP 26664)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55555addf120 <tools::threadpool::getInstance()::instance+160>) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>, cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>) at pthread_cond_wait.c:638
#3  0x0000555555cf33c3 in tools::threadpool::run(bool) ()
#4  0x0000555556022b95 in thread_proxy ()
#5  0x00007ffff7dae609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff79fb293 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 18 (Thread 0x7fffb872f700 (LWP 26663)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55555addf120 <tools::threadpool::getInstance()::instance+160>) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>, cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>) at pthread_cond_wait.c:638
#3  0x0000555555cf33c3 in tools::threadpool::run(bool) ()
#4  0x0000555556022b95 in thread_proxy ()
#5  0x00007ffff7dae609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff79fb293 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 17 (Thread 0x7fffb8c30700 (LWP 26662)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55555addf120 <tools::threadpool::getInstance()::instance+160>) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>, cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>) at pthread_cond_wait.c:638
#3  0x0000555555cf33c3 in tools::threadpool::run(bool) ()
#4  0x0000555556022b95 in thread_proxy ()
#5  0x00007ffff7dae609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff79fb293 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 16 (Thread 0x7fffb9131700 (LWP 26661)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55555addf120 <tools::threadpool::getInstance()::instance+160>) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>, cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>) at pthread_cond_wait.c:638
#3  0x0000555555cf33c3 in tools::threadpool::run(bool) ()
#4  0x0000555556022b95 in thread_proxy ()
#5  0x00007ffff7dae609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff79fb293 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 15 (Thread 0x7fffb9632700 (LWP 26660)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55555addf120 <tools::threadpool::getInstance()::instance+160>) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>, cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>) at pthread_cond_wait.c:638
#3  0x0000555555cf33c3 in tools::threadpool::run(bool) ()
#4  0x0000555556022b95 in thread_proxy ()
#5  0x00007ffff7dae609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff79fb293 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 14 (Thread 0x7fffb9b33700 (LWP 26659)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55555addf120 <tools::threadpool::getInstance()::instance+160>) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>, cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>) at pthread_cond_wait.c:638
#3  0x0000555555cf33c3 in tools::threadpool::run(bool) ()
#4  0x0000555556022b95 in thread_proxy ()
#5  0x00007ffff7dae609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff79fb293 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 13 (Thread 0x7fffba034700 (LWP 26658)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55555addf120 <tools::threadpool::getInstance()::instance+160>) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>, cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>) at pthread_cond_wait.c:638
#3  0x0000555555cf33c3 in tools::threadpool::run(bool) ()
#4  0x0000555556022b95 in thread_proxy ()
#5  0x00007ffff7dae609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff79fb293 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 12 (Thread 0x7fffe0870700 (LWP 26657)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55555addf120 <tools::threadpool::getInstance()::instance+160>) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>, cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>) at pthread_cond_wait.c:638
#3  0x0000555555cf33c3 in tools::threadpool::run(bool) ()
#4  0x0000555556022b95 in thread_proxy ()
#5  0x00007ffff7dae609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff79fb293 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 11 (Thread 0x7fffe0d71700 (LWP 26656)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55555addf120 <tools::threadpool::getInstance()::instance+160>) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>, cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x55555addf0f8 <tools::threadpool::getInstance()::instance+120>, mutex=0x55555addf0d0 <tools::threadpool::getInstance()::instance+80>) at pthread_cond_wait.c:638
#3  0x0000555555cf33c3 in tools::threadpool::run(bool) ()
#4  0x0000555556022b95 in thread_proxy ()
#5  0x00007ffff7dae609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff79fb293 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 10 (Thread 0x7fffe2969700 (LWP 26655)):
#0  0x00007ffff79eeaff in __GI___poll (fds=0x7fffc80029e0, nfds=1, timeout=9990) at ../sysdeps/unix/sysv/linux/poll.c:29
#1  0x00007ffff7e1a1ae in ?? () from /lib/x86_64-linux-gnu/libglib-2.0.so.0
#2  0x00007ffff7e1a2e3 in g_main_context_iteration () from /lib/x86_64-linux-gnu/libglib-2.0.so.0
#3  0x0000555556f4f7cf in QEventDispatcherGlib::processEvents(QFlags<QEventLoop::ProcessEventsFlag>) ()
#4  0x0000555556ef5935 in QEventLoop::exec(QFlags<QEventLoop::ProcessEventsFlag>) ()
#5  0x0000555556d21854 in QThread::run() ()
#6  0x0000555556d26bb9 in QThreadPrivate::start(void*) ()
#7  0x00007ffff7dae609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#8  0x00007ffff79fb293 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 8 (Thread 0x7fffe396b700 (LWP 26653)):
#0  0x00007ffff79eeaff in __GI___poll (fds=0x7fffd0004a20, nfds=1, timeout=-1) at ../sysdeps/unix/sysv/linux/poll.c:29
#1  0x00007ffff7e1a1ae in ?? () from /lib/x86_64-linux-gnu/libglib-2.0.so.0
#2  0x00007ffff7e1a2e3 in g_main_context_iteration () from /lib/x86_64-linux-gnu/libglib-2.0.so.0
#3  0x0000555556f4f7cf in QEventDispatcherGlib::processEvents(QFlags<QEventLoop::ProcessEventsFlag>) ()
#4  0x0000555556ef5935 in QEventLoop::exec(QFlags<QEventLoop::ProcessEventsFlag>) ()
#5  0x0000555556d21724 in QThread::exec() ()
#6  0x00005555563211f5 in QQuickXmlQueryEngine::run() ()
#7  0x0000555556d26bb9 in QThreadPrivate::start(void*) ()
#8  0x00007ffff7dae609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#9  0x00007ffff79fb293 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 7 (Thread 0x7fffed17e700 (LWP 26652)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55555af6d728) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x55555af6d6d8, cond=0x55555af6d700) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x55555af6d700, mutex=0x55555af6d6d8) at pthread_cond_wait.c:638
#3  0x00007fffeedfe62b in ?? () from /usr/lib/x86_64-linux-gnu/dri/nouveau_dri.so
#4  0x00007fffeedfe23b in ?? () from /usr/lib/x86_64-linux-gnu/dri/nouveau_dri.so
#5  0x00007ffff7dae609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff79fb293 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 6 (Thread 0x7fffed97f700 (LWP 26651)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55555af6d728) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x55555af6d6d8, cond=0x55555af6d700) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x55555af6d700, mutex=0x55555af6d6d8) at pthread_cond_wait.c:638
#3  0x00007fffeedfe62b in ?? () from /usr/lib/x86_64-linux-gnu/dri/nouveau_dri.so
#4  0x00007fffeedfe23b in ?? () from /usr/lib/x86_64-linux-gnu/dri/nouveau_dri.so
#5  0x00007ffff7dae609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff79fb293 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 5 (Thread 0x7fffee180700 (LWP 26650)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55555af6d728) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x55555af6d6d8, cond=0x55555af6d700) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x55555af6d700, mutex=0x55555af6d6d8) at pthread_cond_wait.c:638
#3  0x00007fffeedfe62b in ?? () from /usr/lib/x86_64-linux-gnu/dri/nouveau_dri.so
#4  0x00007fffeedfe23b in ?? () from /usr/lib/x86_64-linux-gnu/dri/nouveau_dri.so
#5  0x00007ffff7dae609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff79fb293 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 4 (Thread 0x7fffee981700 (LWP 26649)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55555af6d728) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x55555af6d6d8, cond=0x55555af6d700) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x55555af6d700, mutex=0x55555af6d6d8) at pthread_cond_wait.c:638
#3  0x00007fffeedfe62b in ?? () from /usr/lib/x86_64-linux-gnu/dri/nouveau_dri.so
#4  0x00007fffeedfe23b in ?? () from /usr/lib/x86_64-linux-gnu/dri/nouveau_dri.so
#5  0x00007ffff7dae609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff79fb293 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 3 (Thread 0x7ffff66fd700 (LWP 26622)):
#0  0x00007ffff79eeaff in __GI___poll (fds=0x7fffe80029e0, nfds=1, timeout=-1) at ../sysdeps/unix/sysv/linux/poll.c:29
#1  0x00007ffff7e1a1ae in ?? () from /lib/x86_64-linux-gnu/libglib-2.0.so.0
#2  0x00007ffff7e1a2e3 in g_main_context_iteration () from /lib/x86_64-linux-gnu/libglib-2.0.so.0
#3  0x0000555556f4f7cf in QEventDispatcherGlib::processEvents(QFlags<QEventLoop::ProcessEventsFlag>) ()
#4  0x0000555556ef5935 in QEventLoop::exec(QFlags<QEventLoop::ProcessEventsFlag>) ()
#5  0x0000555556d21724 in QThread::exec() ()
#6  0x0000555556b0b0d5 in QQmlThreadPrivate::run() ()
#7  0x0000555556d26bb9 in QThreadPrivate::start(void*) ()
#8  0x00007ffff7dae609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#9  0x00007ffff79fb293 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 2 (Thread 0x7ffff7183700 (LWP 26621)):
#0  0x00007ffff79eeaff in __GI___poll (fds=0x7ffff7182ce8, nfds=1, timeout=-1) at ../sysdeps/unix/sysv/linux/poll.c:29
#1  0x00007ffff7ad6c1a in ?? () from /lib/x86_64-linux-gnu/libxcb.so.1
#2  0x00007ffff7ad890a in xcb_wait_for_event () from /lib/x86_64-linux-gnu/libxcb.so.1
#3  0x00005555577f27f9 in QXcbEventReader::run() ()
#4  0x0000555556d26bb9 in QThreadPrivate::start(void*) ()
#5  0x00007ffff7dae609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff79fb293 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 1 (Thread 0x7ffff774cc00 (LWP 26603)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x55555e1ee250) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x55555aeef158, cond=0x55555e1ee228) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x55555e1ee228, mutex=0x55555aeef158) at pthread_cond_wait.c:638
#3  0x00007ffff7ad6df0 in ?? () from /lib/x86_64-linux-gnu/libxcb.so.1
#4  0x00007ffff7ad8a02 in xcb_wait_for_special_event () from /lib/x86_64-linux-gnu/libxcb.so.1
#5  0x00007ffff4d4541e in glPrimitiveBoundingBox () from /lib/x86_64-linux-gnu/libGLX_mesa.so.0
#6  0x00007ffff4d45588 in glPrimitiveBoundingBox () from /lib/x86_64-linux-gnu/libGLX_mesa.so.0
#7  0x00007ffff4d4674e in glPrimitiveBoundingBox () from /lib/x86_64-linux-gnu/libGLX_mesa.so.0
#8  0x00007ffff4d476ac in glPrimitiveBoundingBox () from /lib/x86_64-linux-gnu/libGLX_mesa.so.0
#9  0x00007fffeea876b3 in ?? () from /usr/lib/x86_64-linux-gnu/dri/nouveau_dri.so
#10 0x00007fffeea897f4 in ?? () from /usr/lib/x86_64-linux-gnu/dri/nouveau_dri.so
#11 0x00007fffeea9591c in ?? () from /usr/lib/x86_64-linux-gnu/dri/nouveau_dri.so
#12 0x00007fffeea95f90 in ?? () from /usr/lib/x86_64-linux-gnu/dri/nouveau_dri.so
#13 0x00007fffeeab9b85 in ?? () from /usr/lib/x86_64-linux-gnu/dri/nouveau_dri.so
#14 0x00007fffeeabe706 in ?? () from /usr/lib/x86_64-linux-gnu/dri/nouveau_dri.so
#15 0x00005555565ac6da in QSGBatchRenderer::Renderer::renderBatches() ()
#16 0x00005555565b2214 in QSGBatchRenderer::Renderer::render() ()
#17 0x00005555564aed42 in QSGRenderer::renderScene(QSGBindable const&) ()
#18 0x00005555564af21b in QSGRenderer::renderScene(unsigned int) ()
#19 0x00005555564cbf5e in QSGDefaultRenderContext::renderNextFrame(QSGRenderer*, unsigned int) ()
#20 0x00005555563c6062 in QQuickWindowPrivate::renderSceneGraph(QSize const&) ()
#21 0x00005555564c1720 in QSGGuiThreadRenderLoop::renderWindow(QQuickWindow*) ()
#22 0x00005555563d0527 in QQuickWindow::event(QEvent*) ()
#23 0x000055555720d2cc in QApplicationPrivate::notify_helper(QObject*, QEvent*) ()
#24 0x00005555572148cc in QApplication::notify(QObject*, QEvent*) ()
#25 0x0000555556ef7ab8 in QCoreApplication::notifyInternal2(QObject*, QEvent*) ()
#26 0x0000555556601846 in QWindow::event(QEvent*) ()
#27 0x00005555563d04d5 in QQuickWindow::event(QEvent*) ()
#28 0x000055555720d2cc in QApplicationPrivate::notify_helper(QObject*, QEvent*) ()
#29 0x00005555572148cc in QApplication::notify(QObject*, QEvent*) ()
#30 0x0000555556ef7ab8 in QCoreApplication::notifyInternal2(QObject*, QEvent*) ()
#31 0x0000555556f4ea4e in QTimerInfoList::activateTimers() ()
#32 0x0000555556f4f429 in idleTimerSourceDispatch(_GSource*, int (*)(void*), void*) ()
#33 0x00007ffff7e19fbd in g_main_context_dispatch () from /lib/x86_64-linux-gnu/libglib-2.0.so.0
#34 0x00007ffff7e1a240 in ?? () from /lib/x86_64-linux-gnu/libglib-2.0.so.0
#35 0x00007ffff7e1a2e3 in g_main_context_iteration () from /lib/x86_64-linux-gnu/libglib-2.0.so.0
#36 0x0000555556f4f7cf in QEventDispatcherGlib::processEvents(QFlags<QEventLoop::ProcessEventsFlag>) ()
#37 0x0000555556ef5935 in QEventLoop::exec(QFlags<QEventLoop::ProcessEventsFlag>) ()
#38 0x0000555556eff298 in QCoreApplication::exec() ()
#39 0x00005555559367ef in main ()
(gdb) 



## xiphon | 2020-11-15T20:33:24+00:00
Would you like to test the recent Github Workflows CI build? `docker-linux-static` artifact at https://github.com/monero-project/monero-gui/actions/runs/359757921. Note it's built on the Github servers, so for testing purposes only.

PS: You better wait for the next release in a few weeks.

## 3ach1T3ach1 | 2020-11-19T14:41:12+00:00
@xiphon  So not need or use for me to test just wait for next release? 

## xiphon | 2021-04-20T23:51:40+00:00
Should be resolved in v0.17.1.5 and onwards.

# Action History
- Created by: 3ach1T3ach1 | 2020-11-13T09:11:18+00:00
- Closed at: 2021-04-20T23:51:40+00:00
