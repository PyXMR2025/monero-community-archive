---
title: Daemon crashes (SIGSEGV) after last batch of PRs
source_url: https://github.com/monero-project/monero/issues/5337
author: moneroexamples
assignees: []
labels: []
created_at: '2019-03-23T11:10:28+00:00'
updated_at: '2019-03-23T21:29:15+00:00'
type: issue
status: closed
closed_at: '2019-03-23T21:29:14+00:00'
---

# Original Description
on Arch Linux. I checked on two PCs running Arch.

Backtrace
```
Thread 2 "monerod" received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0x7ffff4c8f700 (LWP 7789)]
0x0000555555b5cdfa in tools::dns_utils::parse_dns_public[abi:cxx11](char const*) ()
(gdb) where
#0  0x0000555555b5cdfa in tools::dns_utils::parse_dns_public[abi:cxx11](char const*) ()
#1  0x0000555555b5e29a in tools::DNSResolver::DNSResolver() ()
#2  0x0000555555b5eadc in tools::DNSResolver::instance() ()
#3  0x0000555555a02d03 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::init(boost::program_options::variables_map const&)::{lambda()#1}::operator()() const
    ()
#4  0x00007ffff737eb72 in ?? () from /usr/lib/libboost_thread.so.1.69.0
#5  0x00007ffff7025a9d in start_thread () from /usr/lib/libpthread.so.0
#6  0x00007ffff6f55b23 in clone () from /usr/lib/libc.so.6
```



# Discussion History
## moneromooo-monero | 2019-03-23T14:21:45+00:00
https://github.com/monero-project/monero/pull/5324

## vtnerd | 2019-03-23T17:17:46+00:00
Why would that PR prevent a segfault from occurring?

## moneromooo-monero | 2019-03-23T18:34:27+00:00
Because DNS_PUBLIC is NULL when parsed.

## moneroexamples | 2019-03-23T21:29:14+00:00
The #5324 fixes the issue. Thank you!

# Action History
- Created by: moneroexamples | 2019-03-23T11:10:28+00:00
- Closed at: 2019-03-23T21:29:14+00:00
