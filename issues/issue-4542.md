---
title: 'segffault on android '
source_url: https://github.com/monero-project/monero/issues/4542
author: twiuglufosfa
assignees: []
labels: []
created_at: '2018-10-09T17:41:53+00:00'
updated_at: '2018-12-01T09:11:56+00:00'
type: issue
status: closed
closed_at: '2018-12-01T09:11:56+00:00'
---

# Original Description
i compiled and try to run on termux but not possible because of segfault

https://pastebin.com/zUAeMdZ0

# Discussion History
## moneromooo-monero | 2018-10-09T18:07:47+00:00
Do you have a stack trace (gdb bninary core, bt) ?

## twiuglufosfa | 2018-11-27T11:30:55+00:00
is enough this or u need smth more 

"Starting program: /data/data/com.termux/files/home/monerod
warning: Unable to determine the number of hardware watchpoints available.
warning: Unable to determine the number of hardware breakpoints available.

Program received signal SIGSEGV, Segmentation fault.
0x00000055556269e0 in std::__ndk1::basic_ostream<char, std::__ndk1::char_traits<char> >& std::__ndk1::__put_character_sequence<char, std::__ndk1::char_traits<char> >(std::__ndk1::basic_ostream<char, std::__ndk1::char_traits<char> >&, char const*, unsigned long) ()
"

## moneromooo-monero | 2018-11-27T12:24:42+00:00
When you're at this step, run this command:

bt

This should give you the stack trace.

## twiuglufosfa | 2018-11-27T14:34:40+00:00
#10x0000005555ac4440 in el::base::DefaultLogDispatchCallback::dispatch(std::__ndk1::basic_string<char, std::__ndk1::char_traits<char>, std::__ndk1::allocator<char> >&&) ()
#2  0x0000005555ac3ff4 in el::base::DefaultLogDispatchCallback::handle(el::LogDispatchData const*) ()
#3  0x0000005555ac5c1c in el::base::LogDispatcher::dispatch() ()
#4  0x0000005555ac6d8c in el::base::Writer::triggerDispatch() ()
#5  0x000000555562330c in el::base::Writer::~Writer() ()
#6  0x0000005555aad390 in epee::mlocker::get_page_size() ()
#7  0x0000005555aad4e0 in epee::mlocker::lock(void*, unsigned long) ()
#8  0x000000555561ad44 in _GLOBAL__sub_I_crypto.c
unsigned long) ()
#8  0x000000555561ad44 in _GLOBAL__sub_I_crypto.c--Type <RET> for more, q to quit, c to continue without paging--
pp ()
#9  0x0000007fb7f583b8 in __dl__ZN6soinfo10call_arrayEPKcPPFvvEmb () from /system/bin/linker64
#10 0x0000007fb7f5bf8c in __dl__ZL29__linker_init_post_relocationR19KernelArgumentBlocky ()
   from /system/bin/linker64
#11 0x0000007fb7f5ada8 in __dl___linker_init ()
   from /system/bin/linker64
#12 0x0000007fb7f52c7c in __dl__start ()
   from /system/bin/linker64
Backtrace stopped: previous frame identical to this frame (corrupt stack?)

## twiuglufosfa | 2018-11-28T12:51:30+00:00
i checked and i found that apk insert stripped version of libmonero.

maybe this dont help on debugging?

## moneromooo-monero | 2018-11-29T16:00:01+00:00
There is not much info here. Maybe the output stream code in your libstdc++ relies on globally allocated objects which aren't yet initiualized. That's a guess though.

## twiuglufosfa | 2018-11-29T16:02:34+00:00
what to do?

i download latest code and error is exactly same!
maybe smth else with dbg?


## moneromooo-monero | 2018-11-29T16:07:14+00:00
Can you build your own ?

## twiuglufosfa | 2018-11-29T17:27:51+00:00
build is successful but wont run because of seg fault 

## moneromooo-monero | 2018-11-30T01:10:24+00:00
In contrib/epee/src/mlocker.cpp, comment out the line with "MINFO" (or remove it).


## twiuglufosfa | 2018-11-30T10:58:30+00:00
works!!
what that line did?

## moneromooo-monero | 2018-11-30T16:51:59+00:00
That line logs something very early. Apparently before libstdc++ is fully initialized.

## moneromooo-monero | 2018-11-30T16:54:53+00:00
https://github.com/monero-project/monero/pull/4925

## twiuglufosfa | 2018-12-01T09:11:56+00:00
solved!

happy that i helped on this.

# Action History
- Created by: twiuglufosfa | 2018-10-09T17:41:53+00:00
- Closed at: 2018-12-01T09:11:56+00:00
