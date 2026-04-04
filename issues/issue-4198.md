---
title: monero-wallet-cli frozen after typing password for a transfer
source_url: https://github.com/monero-project/monero/issues/4198
author: moneroISlove
assignees: []
labels:
- invalid
created_at: '2018-07-30T20:02:38+00:00'
updated_at: '2018-09-14T12:08:58+00:00'
type: issue
status: closed
closed_at: '2018-09-14T12:08:58+00:00'
---

# Original Description
Version used : v0.12.3.0-release and v0.12.2.0-release
OS: Arch Linux
Internet: 14ms / 100Mbit
Nodes: remote nodes (moneroworld) and myown deamon via SSH (portforwarding)

Tried 15-20 times with many remotenodes and myown daemon but always freeze :/

Found an older one : https://github.com/monero-project/monero/issues/3813



# Discussion History
## moneromooo-monero | 2018-07-30T20:41:56+00:00
Get an all thread stack trace:

gdb /path/to/monero-wallet-cli '`pidof monero-wallet-cli\`
thread apply all bt


Then paste the (multi page) output here or fpaste.org or pastebin.mozilla.org.

## moneroISlove | 2018-07-30T22:34:27+00:00
Thread 2 (Thread 0x7fa725b90700 (LWP 10860)):
#0  0x00007fa728dd5ffc in pthread_cond_wait@@GLIBC_2.3.2 () from /usr/lib/libpthread.so.0
No symbol table info available.
#1  0x0000564fa81e8108 in boost::condition_variable::wait(boost::unique_lock<boost::mutex>&) ()
No symbol table info available.
#2  0x0000564fa81e8491 in epee::async_stdin_reader::reader_thread_func() ()
No symbol table info available.
#3  0x00007fa72b2b17bf in ?? () from /usr/lib/libboost_thread.so.1.66.0
No symbol table info available.
#4  0x00007fa728dd0075 in start_thread () from /usr/lib/libpthread.so.0
No symbol table info available.
#5  0x00007fa728b0553f in clone () from /usr/lib/libc.so.6
No symbol table info available.

Thread 1 (Thread 0x7fa72bd5ac00 (LWP 10851)):
#0  0x00007fa728af6934 in read () from /usr/lib/libc.so.6
No symbol table info available.
#1  0x00007fa728a88788 in __GI__IO_file_underflow () from /usr/lib/libc.so.6
No symbol table info available.
#2  0x00007fa728a898a2 in __GI__IO_default_uflow () from /usr/lib/libc.so.6
No symbol table info available.
#3  0x00007fa728a841f0 in getc () from /usr/lib/libc.so.6
No symbol table info available.
#4  0x00007fa72967ffde in __gnu_cxx::stdio_sync_filebuf<char, std::char_traits<char> >::syncgetc (this=0x7fa729919ce0 <__gnu_internal::buf_cin_sync>)
    at /build/gcc/src/gcc-build/x86_64-pc-linux-gnu/libstdc++-v3/include/ext/stdio_sync_filebuf.h:225
No locals.
#5  __gnu_cxx::stdio_sync_filebuf<char, std::char_traits<char> >::underflow (this=0x7fa729919ce0 <__gnu_internal::buf_cin_sync>)
    at /build/gcc/src/gcc-build/x86_64-pc-linux-gnu/libstdc++-v3/include/ext/stdio_sync_filebuf.h:133
        __c = <optimized out>
#6  0x00007fa72963d249 in std::basic_streambuf<char, std::char_traits<char> >::sgetc (this=0x7fa729919ce0 <__gnu_internal::buf_cin_sync>)
    at /build/gcc/src/gcc/libstdc++-v3/src/c++98/istream-string.cc:197
        __ret = <optimized out>
        this = 0x7fa729919ce0 <__gnu_internal::buf_cin_sync>
        __ret = <optimized out>
        __ret = <optimized out>
        __ret = <optimized out>
#7  std::basic_istream<char, std::char_traits<char> >& std::getline<char, std::char_traits<char>, std::allocator<char> >(std::basic_istream<char, std::char_traits<char> >&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, char) ()
    at /build/gcc/src/gcc/libstdc++-v3/src/c++98/istream-string.cc:145
        __idelim = 10
        __eof = -1
        __sb = 0x7fa729919ce0 <__gnu_internal::buf_cin_sync>
        __c = <optimized out>
        __extracted = 0
        __err = std::_S_goodbit
        __cerb = {_M_ok = true}
#8  0x0000564fa8189caf in ?? ()
No symbol table info available.
#9  0x0000564fa81928ab in cryptonote::simple_wallet::ask_wallet_create_if_needed() ()
No symbol table info available.
#10 0x0000564fa81b44c9 in cryptonote::simple_wallet::init(boost::program_options::variables_map const&) ()
No symbol table info available.
#11 0x0000564fa817b8ad in main ()
No symbol table info available.
Continuing.
[New Thread 0x7fa724629700 (LWP 11058)]
[New Thread 0x7fa724128700 (LWP 11059)]
[New Thread 0x7fa723c27700 (LWP 11060)]
[New Thread 0x7fa723726700 (LWP 11061)]
[New Thread 0x7fa723225700 (LWP 11090)]
[New Thread 0x7fa722a24700 (LWP 11160)]
[New Thread 0x7fa722223700 (LWP 11161)]
[New Thread 0x7fa721a22700 (LWP 11162)]
[New Thread 0x7fa721221700 (LWP 11163)]
[Thread 0x7fa721a22700 (LWP 11162) exited]
[Thread 0x7fa722223700 (LWP 11161) exited]
[Thread 0x7fa721221700 (LWP 11163) exited]

Thread 1 "monero-wallet-c" received signal SIGINT, Interrupt.
0x00007fa728dd5ffc in pthread_cond_wait@@GLIBC_2.3.2 () from /usr/lib/libpthread.so.0

## moneromooo-monero | 2018-07-31T08:25:54+00:00
That trace looks like it's asking for a wallet to use, which happens at startup.
Maybe gdb is getting confused, or the binary changed since it started running.
What is the command you were running when you got that wedge ?

## moneroISlove | 2018-07-31T18:47:04+00:00
gdb --pid=10851

(gdb) set logging file trace.log
(gdb) set logging on
(gdb) thread apply all bt full
(gdb) set logging off
(gdb) quit


## moneromooo-monero | 2018-07-31T18:59:09+00:00
 What is the monero-wallet-cli command you were running when you got that wedge ?

## moneroISlove | 2018-07-31T19:04:30+00:00
transfer 4AWN6NgEQJr1rDdWP4BP2cJ9PkkHyL1z4hbmWPTgfiMucUYrPfoxB71bSeE6qNaXzT7wfqBzUsCJb52763zhdtVS6TGSCB2 1

Password: blabla

--> freeze


## moneromooo-monero | 2018-07-31T19:24:57+00:00
Can you try a debug build ? This might give better trace info.

## moneroISlove | 2018-07-31T23:40:23+00:00
make debug
Current version : Monero 'Lithium Luna' (v0.12.3.0-master-0dddfeac)

seems the same : https://paste.fedoraproject.org/paste/Dnw6w~9qlJJ-PWfF34pGsw/raw

## moneroISlove | 2018-08-01T01:10:06+00:00
I did a OS update, than i have to rebuild monero because of libboost issues. Now it works but still a bit slow.

## jonathancross | 2018-08-27T12:50:40+00:00
@moneroISlove Does this mean the issue can be closed?

## moneromooo-monero | 2018-09-14T12:03:56+00:00
I'll close it then, since one off and not reproducible. Reopen if you do reproduce it.

+invalid

# Action History
- Created by: moneroISlove | 2018-07-30T20:02:38+00:00
- Closed at: 2018-09-14T12:08:58+00:00
