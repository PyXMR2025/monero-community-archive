---
title: Program received signal SIGSEGV, Segmentation fault
source_url: https://github.com/monero-project/monero/issues/279
author: Gingeropolous
assignees: []
labels: []
created_at: '2015-05-06T10:36:52+00:00'
updated_at: '2015-11-24T14:53:02+00:00'
type: issue
status: closed
closed_at: '2015-11-24T14:53:02+00:00'
---

# Original Description
bitmonero v0.8.8.7-41f0a8f
Is this normal behavior now? When I exit, I get a segfault. Set_log 2 and gdb:

2015-May-06 06:31:34.637172 [SRV_MAIN]Deinitializing core...
2015-May-06 06:31:34.637406 [SRV_MAIN]Mining has been stopped, 0 finished
2015-May-06 06:31:34.755137 [SRV_MAIN]Mining has been stopped, 0 finished
2015-May-06 06:31:34.755763 [SRV_MAIN]Deinitializing cryptonote_protocol...

Program received signal SIGSEGV, Segmentation fault.
0x00000000006a48b4 in nOT::nUtils::cLogger::Thread2Number(std::thread::id) ()
(gdb) tb 20
Temporary breakpoint 1 at 0x7ffff7bc2f50: file events.c, line 20.
(gdb) bt 20
#0  0x00000000006a48b4 in nOT::nUtils::cLogger::Thread2Number(std::thread::id) ()
#1  0x000000000074b3d5 in nOT::nUtils::cLogger::write_stream(int, std::string const&) [clone .constprop.912]()
#2  0x0000000000665eaf in epee::net_utils::data_logger::~data_logger() ()
#3  0x00000000006cf551 in std::unique_ptr<epee::net_utils::data_logger, std::default_delete<epee::net_utils::data_logger> >::~unique_ptr() ()
#4  0x00007ffff7833259 in __run_exit_handlers (status=1, listp=0x7ffff7bb56c8 <__exit_funcs>, run_list_atexit=run_list_atexit@entry=true) at exit.c:82
#5  0x00007ffff78332a5 in __GI_exit (status=<optimized out>) at exit.c:104
#6  0x00007ffff7818ecc in __libc_start_main (main=0x47b540 <main>, argc=1, argv=0x7fffffffe098, init=<optimized out>, fini=<optimized out>, rtld_fini=<optimized out>,

```
stack_end=0x7fffffffe088) at libc-start.c:321
```
#7  0x000000000048d52c in _start ()


# Discussion History
## fluffypony | 2015-11-24T14:53:02+00:00
Fixed


# Action History
- Created by: Gingeropolous | 2015-05-06T10:36:52+00:00
- Closed at: 2015-11-24T14:53:02+00:00
