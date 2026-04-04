---
title: 'monero-wallet-cli: crash in readline code'
source_url: https://github.com/monero-project/monero/issues/2118
author: moneromooo-monero
assignees: []
labels: []
created_at: '2017-06-25T15:02:34+00:00'
updated_at: '2017-06-26T05:06:20+00:00'
type: issue
status: closed
closed_at: '2017-06-26T05:06:20+00:00'
---

# Original Description
I am in my multisig branch, rebased on top of today's master, but none of that extra code touches anything near input code. I had just loaded the wallet, and was starting to type a command. It crashed as I was started typing (possibly on a keypress, I'm not quite sure, got surprised by the crash).

#0  0x0000000000000000 in ?? ()
#1  0x00007f7000a6c67e in rl_callback_read_char () from /lib64/libreadline.so.6
#2  0x00000000011b041f in process_input() ()
#3  0x00000000011b025f in rdln::readline_buffer::process() ()
#4  0x0000000000d3acce in epee::async_stdin_reader::readline_thread_func() ()
#5  0x0000000000e50947 in void std::_Mem_fn<void (epee::async_stdin_reader::*)()>::operator()<, void>(epee::async_stdin_reader*) const ()
#6  0x0000000000e4faa2 in void std::_Bind<std::_Mem_fn<void (epee::async_stdin_reader::*)()> (epee::async_stdin_reader*)>::__call<void, , 0ul>(std::tuple<>&&, std::_Index_tuple<0ul>) ()
#7  0x0000000000e4de16 in void std::_Bind<std::_Mem_fn<void (epee::async_stdin_reader::*)()> (epee::async_stdin_reader*)>::operator()<, void>() ()
#8  0x0000000000e48d24 in boost::detail::thread_data<std::_Bind<std::_Mem_fn<void (epee::async_stdin_reader::*)()> (epee::async_stdin_reader*)> >::run() ()
#9  0x00007f70001969da in thread_proxy () from /home/user/boost_1_59_install/lib/libboost_thread.so.1.59.0
#10 0x00007f6ffe29952a in start_thread () from /lib64/libpthread.so.0
#11 0x00007f6ffdfd522d in clone () from /lib64/libc.so.6


# Discussion History
## jtgrassie | 2017-06-25T15:05:16+00:00
As with #2117, have you tried with #2112? This has a process lock that should resolve this.

## moneromooo-monero | 2017-06-25T15:07:11+00:00
No, I have just what's on master right now. It may well be the reason, thanks.

## moneromooo-monero | 2017-06-26T05:06:20+00:00
I've not seen this again, seems fixed by 2112.

# Action History
- Created by: moneromooo-monero | 2017-06-25T15:02:34+00:00
- Closed at: 2017-06-26T05:06:20+00:00
