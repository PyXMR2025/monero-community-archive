---
title: monerod bus error
source_url: https://github.com/monero-project/monero/issues/7424
author: voidzero
assignees: []
labels: []
created_at: '2021-03-04T12:33:21+00:00'
updated_at: '2021-03-05T12:27:07+00:00'
type: issue
status: closed
closed_at: '2021-03-05T12:27:07+00:00'
---

# Original Description
On Linux x86, I'm getting a bus error with Monero v0.17.1.9.

Here's the backtrace:

```
Program terminated with signal SIGBUS, Bus error.
#0  0x00007f8a061430c1 in ?? () from /lib/libc.so.6
(gdb) bt
#0  0x00007f8a061430c1 in ?? () from /lib/libc.so.6
#1  0x000055c5d40a3626 in mdb_page_touch.lto_priv ()
#2  0x000055c5d40a3ae0 in mdb_page_search.lto_priv ()
#3  0x000055c5d40a696b in mdb_txn_commit ()
#4  0x000055c5d40e9327 in cryptonote::mdb_txn_safe::commit(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) ()
#5  0x000055c5d40e19a9 in cryptonote::BlockchainLMDB::open(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, int) ()
#6  0x000055c5d41e9b7a in cryptonote::core::init(boost::program_options::variables_map const&, cryptonote::test_options const*, std::function<epee::span<unsigned char const> const (cryptonote::network_type)> const&) ()
#7  0x000055c5d447b256 in daemonize::t_internals::t_internals(boost::program_options::variables_map const&) ()
#8  0x000055c5d43d046a in daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) ()
#9  0x000055c5d3f13ee6 in main ()
```

# Discussion History
## hyc | 2021-03-04T13:59:50+00:00
Unfortunately, this most likely means your blockchain file is corrupted. You probably had an unclean shutdown of your PC recently.

## voidzero | 2021-03-04T14:03:59+00:00
Oh. That sucks. I have a backup of my monero dir though. Is it enough to just copy the lmdb dir? I can see if that will help.

## hyc | 2021-03-04T14:13:46+00:00
Yes, you can just copy over the lmdb/data.mdb file. If the same problem happens again after that, possibly the backup was already corrupted, or you have bad sectors on your storage device.

## voidzero | 2021-03-04T14:54:45+00:00
that would suck, it's an NVME :-)
I'll copy the file over and keep you posted on the outcome. Thanks so far for your help.

## voidzero | 2021-03-05T12:27:07+00:00
Ok. Seems that a resync fixed the issue. Thanks again @hyc, problem solved.

# Action History
- Created by: voidzero | 2021-03-04T12:33:21+00:00
- Closed at: 2021-03-05T12:27:07+00:00
