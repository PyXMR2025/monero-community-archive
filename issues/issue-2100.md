---
title: crash on monero-wallet-cli --testnet --generate-new-wallet FOO
source_url: https://github.com/monero-project/monero/issues/2100
author: moneromooo-monero
assignees: []
labels: []
created_at: '2017-06-21T13:45:36+00:00'
updated_at: '2017-07-12T11:30:02+00:00'
type: issue
status: closed
closed_at: '2017-07-12T11:30:02+00:00'
---

# Original Description
Introduced by the readline patch.

# Discussion History
## jtgrassie | 2017-06-21T14:02:23+00:00
You got a crash log?

## jtgrassie | 2017-06-21T14:19:05+00:00
@moneromooo-monero I cannot replicate on OS X or Ubuntu. I need details of the crash to investigate further.

## moneromooo-monero | 2017-06-21T15:49:36+00:00
#0  0x00007f4575af7953 in std::basic_ostream<char, std::char_traits<char> >& std::__ostream_insert<char, std::char_traits<char> >(std::basic_ostream<char, std::char_traits<char> >&, char const*, long) () from /lib64/libstdc++.so.6
#1  0x0000000000c03df8 in operator<< <std::char_traits<char> > (__out=..., __s=0xf05388 "Enter new wallet password")
    at /usr/include/c++/4.9.2/ostream:535
#2  read_from_tty (pass2=..., pass1=..., message=<optimized out>, verify=<optimized out>)
    at /home/user/src/bitmonero/src/common/password.cpp:180
#3  tools::password_container::prompt (verify=true, message=0xf05388 "Enter new wallet password")
    at /home/user/src/bitmonero/src/common/password.cpp:250
#4  0x00000000008d159e in tools::wallet2::password_prompt (new_password=new_password@entry=true)
    at /home/user/src/bitmonero/src/wallet/wallet2.cpp:461
#5  0x00000000008e736c in (anonymous namespace)::get_password (vm=..., opts=..., verify=verify@entry=true)
    at /home/user/src/bitmonero/src/wallet/wallet2.cpp:213
#6  0x00000000008fa508 in tools::wallet2::make_new (vm=...) at /home/user/src/bitmonero/src/wallet/wallet2.cpp:495
#7  0x000000000064e90b in cryptonote::simple_wallet::new_wallet (this=this@entry=0x7ffdbb711030, vm=..., recovery_key=..., 
    recover=<optimized out>, two_random=<optimized out>, old_language="")
    at /home/user/src/bitmonero/src/simplewallet/simplewallet.cpp:1330
#8  0x000000000065e3bb in cryptonote::simple_wallet::init (this=this@entry=0x7ffdbb711030, vm=...)
    at /home/user/src/bitmonero/src/simplewallet/simplewallet.cpp:1117
#9  0x00000000005cb68f in main (argc=<optimized out>, argv=0x7ffdbb711628)
    at /home/user/src/bitmonero/src/simplewallet/simplewallet.cpp:4390
#10 0x00007f4574f85fe0 in __libc_start_main () from /lib64/libc.so.6
#11 0x00000000005f0c69 in _start ()


## moneromooo-monero | 2017-06-21T15:51:13+00:00
It is in a very weird place to be crashing. However, this is likely secondary damage, since valgrind complains too (and taking out the readline patches make it work again):

$ valgrind ./build/fuzz/bin/monero-wallet-cli --testnet --generate-new-wallet fuzztest
==12305== Memcheck, a memory error detector
==12305== Copyright (C) 2002-2013, and GNU GPL'd, by Julian Seward et al.
==12305== Using Valgrind-3.10.1 and LibVEX; rerun with -h for copyright info
==12305== Command: ./build/fuzz/bin/monero-wallet-cli --testnet --generate-new-wallet fuzztest
==12305== 
Monero 'Wolfram Warptangent' (v0.10.3.1-ae8841f)
Logging to ./build/fuzz/bin/monero-wallet-cli.log
==12305== Conditional jump or move depends on uninitialised value(s)
==12305==    at 0xE0D24D: rdln::readline_buffer::start() (readline_buffer.cpp:49)
==12305==    by 0x70FFEE: epee::async_stdin_reader::async_stdin_reader() (console_handler.h:57)
==12305==    by 0x643679: async_console_handler (console_handler.h:292)
==12305==    by 0x643679: console_handlers_binder (console_handler.h:502)
==12305==    by 0x643679: cryptonote::simple_wallet::simple_wallet() (simplewallet.cpp:685)
==12305==    by 0x5CB62B: main (simplewallet.cpp:4389)
==12305== 
==12305== Conditional jump or move depends on uninitialised value(s)
==12305==    at 0xE0CF05: rdln::suspend_readline::suspend_readline() (readline_buffer.cpp:29)
==12305==    by 0xC03620: tools::password_container::prompt(bool, char const*) (password.cpp:246)
==12305==    by 0x8D159D: tools::wallet2::password_prompt(bool) (wallet2.cpp:461)
==12305==    by 0x8E736B: (anonymous namespace)::get_password(boost::program_options::variables_map const&, (anonymous namespace)::options const&, bool) (wallet2.cpp:213)
==12305==    by 0x8FA507: tools::wallet2::make_new(boost::program_options::variables_map const&) (wallet2.cpp:495)
==12305==    by 0x64E90A: cryptonote::simple_wallet::new_wallet(boost::program_options::variables_map const&, crypto::secret_key const&, bool, bool, std::string const&) (simplewallet.cpp:1330)
==12305==    by 0x65E3BA: cryptonote::simple_wallet::init(boost::program_options::variables_map const&) (simplewallet.cpp:1117)
==12305==    by 0x5CB68E: main (simplewallet.cpp:4390)
==12305== 
==12305== Conditional jump or move depends on uninitialised value(s)
==12305==    at 0xE0CF87: stop (readline_buffer.cpp:58)
==12305==    by 0xE0CF87: rdln::suspend_readline::suspend_readline() (readline_buffer.cpp:30)
==12305==    by 0xC03620: tools::password_container::prompt(bool, char const*) (password.cpp:246)
==12305==    by 0x8D159D: tools::wallet2::password_prompt(bool) (wallet2.cpp:461)
==12305==    by 0x8E736B: (anonymous namespace)::get_password(boost::program_options::variables_map const&, (anonymous namespace)::options const&, bool) (wallet2.cpp:213)
==12305==    by 0x8FA507: tools::wallet2::make_new(boost::program_options::variables_map const&) (wallet2.cpp:495)
==12305==    by 0x64E90A: cryptonote::simple_wallet::new_wallet(boost::program_options::variables_map const&, crypto::secret_key const&, bool, bool, std::string const&) (simplewallet.cpp:1330)
==12305==    by 0x65E3BA: cryptonote::simple_wallet::init(boost::program_options::variables_map const&) (simplewallet.cpp:1117)
==12305==    by 0x5CB68E: main (simplewallet.cpp:4390)
==12305== 
==12305== Conditional jump or move depends on uninitialised value(s)
==12305==    at 0x726BB68: std::basic_ios<char, std::char_traits<char> >::clear(std::_Ios_Iostate) (in /usr/lib64/libstdc++.so.6.0.20)
==12305==    by 0x726BC55: std::basic_ios<char, std::char_traits<char> >::rdbuf(std::basic_streambuf<char, std::char_traits<char> >*) (in /usr/lib64/libstdc++.so.6.0.20)
==12305==    by 0xE0CFD1: stop (readline_buffer.cpp:60)
==12305==    by 0xE0CFD1: rdln::suspend_readline::suspend_readline() (readline_buffer.cpp:30)
==12305==    by 0xC03620: tools::password_container::prompt(bool, char const*) (password.cpp:246)
==12305==    by 0x8D159D: tools::wallet2::password_prompt(bool) (wallet2.cpp:461)
==12305==    by 0x8E736B: (anonymous namespace)::get_password(boost::program_options::variables_map const&, (anonymous namespace)::options const&, bool) (wallet2.cpp:213)
==12305==    by 0x8FA507: tools::wallet2::make_new(boost::program_options::variables_map const&) (wallet2.cpp:495)
==12305==    by 0x64E90A: cryptonote::simple_wallet::new_wallet(boost::program_options::variables_map const&, crypto::secret_key const&, bool, bool, std::string const&) (simplewallet.cpp:1330)
==12305==    by 0x65E3BA: cryptonote::simple_wallet::init(boost::program_options::variables_map const&) (simplewallet.cpp:1117)
==12305==    by 0x5CB68E: main (simplewallet.cpp:4390)
==12305== 
==12305== Use of uninitialised value of size 8
==12305==    at 0x7287950: std::basic_ostream<char, std::char_traits<char> >& std::__ostream_insert<char, std::char_traits<char> >(std::basic_ostream<char, std::char_traits<char> >&, char const*, long) (in /usr/lib64/libstdc++.so.6.0.20)
==12305==    by 0xC03DF7: operator<< <std::char_traits<char> > (ostream:535)
==12305==    by 0xC03DF7: read_from_tty (password.cpp:180)
==12305==    by 0xC03DF7: tools::password_container::prompt(bool, char const*) (password.cpp:250)
==12305==    by 0x8D159D: tools::wallet2::password_prompt(bool) (wallet2.cpp:461)
==12305==    by 0x8E736B: (anonymous namespace)::get_password(boost::program_options::variables_map const&, (anonymous namespace)::options const&, bool) (wallet2.cpp:213)
==12305==    by 0x8FA507: tools::wallet2::make_new(boost::program_options::variables_map const&) (wallet2.cpp:495)
==12305==    by 0x64E90A: cryptonote::simple_wallet::new_wallet(boost::program_options::variables_map const&, crypto::secret_key const&, bool, bool, std::string const&) (simplewallet.cpp:1330)
==12305==    by 0x65E3BA: cryptonote::simple_wallet::init(boost::program_options::variables_map const&) (simplewallet.cpp:1117)
==12305==    by 0x5CB68E: main (simplewallet.cpp:4390)
==12305== 
==12305== Invalid read of size 8
==12305==    at 0x7287950: std::basic_ostream<char, std::char_traits<char> >& std::__ostream_insert<char, std::char_traits<char> >(std::basic_ostream<char, std::char_traits<char> >&, char const*, long) (in /usr/lib64/libstdc++.so.6.0.20)
==12305==    by 0xC03DF7: operator<< <std::char_traits<char> > (ostream:535)
==12305==    by 0xC03DF7: read_from_tty (password.cpp:180)
==12305==    by 0xC03DF7: tools::password_container::prompt(bool, char const*) (password.cpp:250)
==12305==    by 0x8D159D: tools::wallet2::password_prompt(bool) (wallet2.cpp:461)
==12305==    by 0x8E736B: (anonymous namespace)::get_password(boost::program_options::variables_map const&, (anonymous namespace)::options const&, bool) (wallet2.cpp:213)
==12305==    by 0x8FA507: tools::wallet2::make_new(boost::program_options::variables_map const&) (wallet2.cpp:495)
==12305==    by 0x64E90A: cryptonote::simple_wallet::new_wallet(boost::program_options::variables_map const&, crypto::secret_key const&, bool, bool, std::string const&) (simplewallet.cpp:1330)
==12305==    by 0x65E3BA: cryptonote::simple_wallet::init(boost::program_options::variables_map const&) (simplewallet.cpp:1117)
==12305==    by 0x5CB68E: main (simplewallet.cpp:4390)
==12305==  Address 0xc08ea70 is 256 bytes inside a block of size 544 free'd
==12305==    at 0x4C2B183: operator delete(void*) (in /usr/lib64/valgrind/vgpreload_memcheck-amd64-linux.so)
==12305==    by 0xE64E81: ~TypedConfigurations (easylogging++.h:1971)
==12305==    by 0xE64E81: safeDelete<el::base::TypedConfigurations> (easylogging++.h:912)
==12305==    by 0xE64E81: el::Logger::configure(el::Configurations const&) (easylogging++.cc:600)
==12305==    by 0xE6828F: reconfigureLogger (easylogging++.cc:2931)
==12305==    by 0xE6828F: reconfigureAllLoggers (easylogging++.cc:2953)
==12305==    by 0xE6828F: el::Loggers::setDefaultConfigurations(el::Configurations const&, bool) (easylogging++.cc:2970)
==12305==    by 0xE07721: mlog_configure(std::string const&, bool) (mlog.cpp:125)
==12305==    by 0x5E4201: wallet_args::main(int, char**, char const*, boost::program_options::options_description, boost::program_options::positional_options_description const&, char const*, bool) (wallet_args.cpp:144)
==12305==    by 0x5CB52C: main (simplewallet.cpp:4382)
==12305== 
==12305== Invalid read of size 8
==12305==    at 0x7287953: std::basic_ostream<char, std::char_traits<char> >& std::__ostream_insert<char, std::char_traits<char> >(std::basic_ostream<char, std::char_traits<char> >&, char const*, long) (in /usr/lib64/libstdc++.so.6.0.20)
==12305==    by 0xC03DF7: operator<< <std::char_traits<char> > (ostream:535)
==12305==    by 0xC03DF7: read_from_tty (password.cpp:180)
==12305==    by 0xC03DF7: tools::password_container::prompt(bool, char const*) (password.cpp:250)
==12305==    by 0x8D159D: tools::wallet2::password_prompt(bool) (wallet2.cpp:461)
==12305==    by 0x8E736B: (anonymous namespace)::get_password(boost::program_options::variables_map const&, (anonymous namespace)::options const&, bool) (wallet2.cpp:213)
==12305==    by 0x8FA507: tools::wallet2::make_new(boost::program_options::variables_map const&) (wallet2.cpp:495)
==12305==    by 0x64E90A: cryptonote::simple_wallet::new_wallet(boost::program_options::variables_map const&, crypto::secret_key const&, bool, bool, std::string const&) (simplewallet.cpp:1330)
==12305==    by 0x65E3BA: cryptonote::simple_wallet::init(boost::program_options::variables_map const&) (simplewallet.cpp:1117)
==12305==    by 0x5CB68E: main (simplewallet.cpp:4390)
==12305==  Address 0x60 is not stack'd, malloc'd or (recently) free'd
==12305== 
==12305== 
==12305== Process terminating with default action of signal 11 (SIGSEGV): dumping core
==12305==  Access not within mapped region at address 0x60
==12305==    at 0x7287953: std::basic_ostream<char, std::char_traits<char> >& std::__ostream_insert<char, std::char_traits<char> >(std::basic_ostream<char, std::char_traits<char> >&, char const*, long) (in /usr/lib64/libstdc++.so.6.0.20)
==12305==    by 0xC03DF7: operator<< <std::char_traits<char> > (ostream:535)
==12305==    by 0xC03DF7: read_from_tty (password.cpp:180)
==12305==    by 0xC03DF7: tools::password_container::prompt(bool, char const*) (password.cpp:250)
==12305==    by 0x8D159D: tools::wallet2::password_prompt(bool) (wallet2.cpp:461)
==12305==    by 0x8E736B: (anonymous namespace)::get_password(boost::program_options::variables_map const&, (anonymous namespace)::options const&, bool) (wallet2.cpp:213)
==12305==    by 0x8FA507: tools::wallet2::make_new(boost::program_options::variables_map const&) (wallet2.cpp:495)
==12305==    by 0x64E90A: cryptonote::simple_wallet::new_wallet(boost::program_options::variables_map const&, crypto::secret_key const&, bool, bool, std::string const&) (simplewallet.cpp:1330)
==12305==    by 0x65E3BA: cryptonote::simple_wallet::init(boost::program_options::variables_map const&) (simplewallet.cpp:1117)
==12305==    by 0x5CB68E: main (simplewallet.cpp:4390)
==12305==  If you believe this happened as a result of a stack
==12305==  overflow in your program's main thread (unlikely but
==12305==  possible), you can try to increase the size of the
==12305==  main thread stack using the --main-stacksize= flag.
==12305==  The main thread stack size used in this run was 8388608.
==12305== 
==12305== HEAP SUMMARY:
==12305==     in use at exit: 109,537 bytes in 1,482 blocks
==12305==   total heap usage: 3,957 allocs, 2,475 frees, 239,800 bytes allocated
==12305== 
==12305== LEAK SUMMARY:
==12305==    definitely lost: 0 bytes in 0 blocks
==12305==    indirectly lost: 0 bytes in 0 blocks
==12305==      possibly lost: 32,254 bytes in 448 blocks
==12305==    still reachable: 77,283 bytes in 1,034 blocks
==12305==         suppressed: 0 bytes in 0 blocks
==12305== Rerun with --leak-check=full to see details of leaked memory
==12305== 
==12305== For counts of detected and suppressed errors, rerun with: -v
==12305== Use --track-origins=yes to see where uninitialised values come from
==12305== ERROR SUMMARY: 7 errors from 7 contexts (suppressed: 0 from 0)
Killed


## jtgrassie | 2017-06-21T15:57:45+00:00
@moneromooo-monero Thanks. And what OS and hardware was this on?

## moneromooo-monero | 2017-06-21T15:59:41+00:00
Fedora, x86_64

## jtgrassie | 2017-06-21T16:17:57+00:00
@moneromooo-monero very odd. The only thing I can think of is a threading / race issue, though not found one yet. Whenever there is a password prompt, I suspend the readline stuff.

## jtgrassie | 2017-06-21T16:23:09+00:00
@moneromooo-monero can you try adding: 
```cpp
#ifdef HAVE_READLINE
    rdln::suspend_readline pause_readline;
#endif
```
on line 257 of `src/common/password.cpp` as that might require this too please.

## moneromooo-monero | 2017-06-21T16:26:06+00:00
No change.

## moneromooo-monero | 2017-06-21T16:28:20+00:00
m_cout_buff doesn't seem to be initialized.

## jtgrassie | 2017-06-21T16:31:46+00:00
@moneromooo-monero good spot, but is that the culprit? Can you initialize to null on `readline_buffer` constructor to test please?


## moneromooo-monero | 2017-06-21T16:32:36+00:00
That's fixed it. I'll make a patch.

## jtgrassie | 2017-06-21T16:33:35+00:00
@moneromooo-monero Rockstar. Thanks.

## moneromooo-monero | 2017-06-21T16:36:04+00:00
https://github.com/monero-project/monero/pull/2103

## moneromooo-monero | 2017-07-12T11:30:02+00:00
merged

# Action History
- Created by: moneromooo-monero | 2017-06-21T13:45:36+00:00
- Closed at: 2017-07-12T11:30:02+00:00
