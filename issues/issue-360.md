---
title: got a back trace on the segfault on exit
source_url: https://github.com/monero-project/monero/issues/360
author: Gingeropolous
assignees: []
labels: []
created_at: '2015-08-05T01:13:57+00:00'
updated_at: '2015-11-24T14:56:14+00:00'
type: issue
status: closed
closed_at: '2015-11-24T14:56:14+00:00'
---

# Original Description
# define MONERO_VERSION_TAG "1737fec"
# define MONERO_VERSION "0.8.8.7"
# define MONERO_VERSION_FULL MONERO_VERSION "-" MONERO_VERSION_TAG

Lubuntu 14.04

(gdb) bt 80
#0  0x0000000000759074 in nOT::nUtils::cLogger::Thread2Number(std::thread::id) ()
#1  0x0000000000767235 in nOT::nUtils::cLogger::write_stream(int, std::string const&) [clone .constprop.941]()
#2  0x00000000006aea0f in epee::net_utils::data_logger::~data_logger() ()
#3  0x00000000006e3b01 in std::unique_ptr<epee::net_utils::data_logger, std::default_delete<epee::net_utils::data_logger> >::~unique_ptr() ()
#4  0x00007ffff7833259 in __run_exit_handlers (status=1, listp=0x7ffff7bb56c8 <__exit_funcs>, run_list_atexit=run_list_atexit@entry=true) at exit.c:82
#5  0x00007ffff78332a5 in __GI_exit (status=<optimized out>) at exit.c:104
#6  0x00007ffff7818ecc in __libc_start_main (main=0x47d1b0 <main>, argc=1, argv=0x7fffffffe088, init=<optimized out>, fini=<optimized out>, rtld_fini=<optimized out>,

```
stack_end=0x7fffffffe078) at libc-start.c:321
```
#7  0x000000000049016c in _start ()

(gdb)


# Discussion History
## Gingeropolous | 2015-09-11T00:03:45+00:00
and another

(gdb) bt 40
#0  0x000000000071084c in nOT::nUtils::cLogger::Thread2Number(std::thread::id)
    ()
#1  0x000000000070f65f in nOT::nUtils::cLogger::write_stream(int, std::string const&) [clone .constprop.9112]()
#2  0x00000000007282e4 in epee::net_utils::data_logger::~data_logger() ()
#3  0x00000000006cca39 in std::unique_ptr<epee::net_utils::data_logger, std::default_delete<epee::net_utils::data_logger> >::~unique_ptr() ()
#4  0x00007ffff7833259 in __run_exit_handlers (status=1,
    listp=0x7ffff7bb56c8 <__exit_funcs>,
    run_list_atexit=run_list_atexit@entry=true) at exit.c:82
#5  0x00007ffff78332a5 in __GI_exit (status=<optimized out>) at exit.c:104
#6  0x00007ffff7818ecc in __libc_start_main (main=0x4a9190 <main>, argc=3,
    argv=0x7fffffffdea8, init=<optimized out>, fini=<optimized out>,
    rtld_fini=<optimized out>, stack_end=0x7fffffffde98) at libc-start.c:321
#7  0x00000000004ae72c in _start ()


## fluffypony | 2015-11-24T14:56:14+00:00
Fixed


# Action History
- Created by: Gingeropolous | 2015-08-05T01:13:57+00:00
- Closed at: 2015-11-24T14:56:14+00:00
