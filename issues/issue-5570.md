---
title: OpenBSD memory leak? Corruption? Readline?
source_url: https://github.com/monero-project/monero/issues/5570
author: mrme0w
assignees: []
labels: []
created_at: '2019-05-24T00:56:54+00:00'
updated_at: '2025-12-28T22:33:49+00:00'
type: issue
status: closed
closed_at: '2025-12-28T22:33:49+00:00'
---

# Original Description
[wallet 4AsDPc (no daemon)]: save
��������������������������������@XI�bWallet data saved
[wallet 4AsDPc (no daemon)]: save
��������������������������������Wallet data saved
[wallet 4AsDPc (no daemon)]: save
���������������������������������7�aWallet data saved
[wallet 4AsDPc (no daemon)]: save
[wallet 4AsDPc (no daemon)]: Segmentation fault (core dumped)


# Discussion History
## mrme0w | 2019-05-24T00:57:28+00:00
(Notice the strange artifacts that change after all of the question marks)

Next post is a gdb backtrace

## mrme0w | 2019-05-24T00:58:12+00:00
(gdb) bt
#0  strrchr () at /usr/src/lib/libc/arch/amd64/string/strrchr.S:51
#1  0x0000006249a96a86 in rl_redisplay () at /usr/src/gnu/lib/libreadline/display.c:454
#2  0x0000005f98ff1747 in rdln::suspend_readline::suspend_readline () from /home/mrme0w/monero/build/OpenBSD/master/release/bin/monero-wallet-cli
#3  0x0000005f98bcb759 in tools::scoped_message_writer::~scoped_message_writer () from /home/mrme0w/monero/build/OpenBSD/master/release/bin/monero-wallet-cli
#4  0x0000005f98b4c16f in cryptonote::simple_wallet::save () from /home/mrme0w/monero/build/OpenBSD/master/release/bin/monero-wallet-cli
#5  0x0000005f98bd0568 in epee::command_handler::process_command_vec () from /home/mrme0w/monero/build/OpenBSD/master/release/bin/monero-wallet-cli
#6  0x0000005f98be5957 in epee::command_handler::process_command_str () from /home/mrme0w/monero/build/OpenBSD/master/release/bin/monero-wallet-cli
#7  0x0000005f98be637c in _ZN4epee21async_console_handler3runIZNS0_3runIN5boost3_bi6bind_tIbNS3_4_mfi3mf1IbNS_15command_handlerERKNSt3__112basic_stringIcNS9_11char_traitsIcEENS9_9allocatorIcEEEEEENS4_5list2INS4_5valueIPNS_23console_handlers_binderEEENS3_3argILi1EEEEEEEEEbT_NS9_8functionIFSF_vEEESH_NST_IFvvEEEEUlSH_E_EEbSV_SH_RKSS_SX_ () from /home/mrme0w/monero/build/OpenBSD/master/release/bin/monero-wallet-cli
#8  0x0000005f98be57ea in epee::async_console_handler::run<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > > > () from /home/mrme0w/monero/build/OpenBSD/master/release/bin/monero-wallet-cli
#9  0x0000005f98bd0267 in epee::console_handlers_binder::run_handling () from /home/mrme0w/monero/build/OpenBSD/master/release/bin/monero-wallet-cli
#10 0x0000005f98baa8d1 in cryptonote::simple_wallet::run () from /home/mrme0w/monero/build/OpenBSD/master/release/bin/monero-wallet-cli
#11 0x0000005f98bae2af in main () from /home/mrme0w/monero/build/OpenBSD/master/release/bin/monero-wallet-cli
Current language:  auto; currently asm
(gdb)

## mrme0w | 2019-05-24T01:00:24+00:00
These strange console artifacts happen on monerod too, but mostly after commands such as "save" or "exit".

## mrme0w | 2019-05-24T01:28:10+00:00
OK, so compiling with readline disabled on OpenBSD fixes the garbled output and crashes.

Any suggestions on how to fix this?

## moneromooo-monero | 2019-05-24T07:59:13+00:00
Any chance you can rn with asan (add -D SANITIZE=ON to the cmake command line) ?

## offshoremonero | 2022-11-24T01:37:57+00:00
Pull request #8596 fixes this issue for now.

# Action History
- Created by: mrme0w | 2019-05-24T00:56:54+00:00
- Closed at: 2025-12-28T22:33:49+00:00
