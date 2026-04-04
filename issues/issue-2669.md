---
title: Bus error on loading blockchain
source_url: https://github.com/monero-project/monero/issues/2669
author: avfedorov
assignees: []
labels: []
created_at: '2017-10-16T12:38:29+00:00'
updated_at: '2019-12-01T16:02:45+00:00'
type: issue
status: open
closed_at: null
---

# Original Description

gdb /usr/local/bin/monerod
GNU gdb (GDB) Red Hat Enterprise Linux 7.6.1-94.el7
Copyright (C) 2013 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-redhat-linux-gnu".
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>...
Reading symbols from /usr/local/bin/monerod...done.
(gdb) set args --config-file /home/monero/etc/monerod.conf
(gdb) run
Starting program: /usr/local/bin/monerod --config-file /home/monero/etc/monerod.conf
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib64/libthread_db.so.1".
2017-10-16 12:34:16.631     7ffff7fe4780        INFO    global  src/daemon/main.cpp:279 Monero 'Helium Hydra' (v0.11.0.0-release)
2017-10-16 12:34:16.631     7ffff7fe4780        INFO    global  src/daemon/protocol.h:55        Initializing cryptonote protocol...
2017-10-16 12:34:16.631     7ffff7fe4780        INFO    global  src/daemon/protocol.h:60        Cryptonote protocol initialized OK
[New Thread 0x7ffff72f9700 (LWP 4770)]
[New Thread 0x7ffff6df8700 (LWP 4771)]
[New Thread 0x7ffff68f7700 (LWP 4772)]
[New Thread 0x7ffff63f6700 (LWP 4773)]
[New Thread 0x7ffff5ef5700 (LWP 4774)]
[New Thread 0x7ffff59f4700 (LWP 4775)]
[New Thread 0x7ffff54f3700 (LWP 4776)]
[New Thread 0x7ffff4ff2700 (LWP 4777)]
[New Thread 0x7ffff4af1700 (LWP 4778)]
[New Thread 0x7ffff45f0700 (LWP 4779)]
[New Thread 0x7ffff40ef700 (LWP 4780)]
[New Thread 0x7ffff3bee700 (LWP 4781)]
[New Thread 0x7ffff36ed700 (LWP 4782)]
[New Thread 0x7ffff31ec700 (LWP 4783)]
[New Thread 0x7ffff2ceb700 (LWP 4784)]
[New Thread 0x7ffff27ea700 (LWP 4785)]
[New Thread 0x7ffff22e9700 (LWP 4786)]
[New Thread 0x7ffff1de8700 (LWP 4787)]
[New Thread 0x7ffff18e7700 (LWP 4788)]
[New Thread 0x7ffff13e6700 (LWP 4789)]
[New Thread 0x7ffff0ee5700 (LWP 4790)]
[New Thread 0x7ffff09e4700 (LWP 4791)]
[New Thread 0x7ffff04e3700 (LWP 4792)]
[New Thread 0x7fffeffe2700 (LWP 4793)]
[New Thread 0x7fffefae1700 (LWP 4794)]
[New Thread 0x7fffef5e0700 (LWP 4795)]
[New Thread 0x7fffef0df700 (LWP 4796)]
[New Thread 0x7fffeebde700 (LWP 4797)]
[New Thread 0x7fffee6dd700 (LWP 4798)]
[New Thread 0x7fffee1dc700 (LWP 4799)]
[New Thread 0x7fffedcdb700 (LWP 4800)]
2017-10-16 12:34:16.652     7ffff7fe4780        INFO    global  src/daemon/p2p.h:63     Initializing p2p server...
[New Thread 0x7fffed7da700 (LWP 4801)]
[New Thread 0x7fffecfd9700 (LWP 4802)]
[New Thread 0x7fffe7fff700 (LWP 4803)]
[New Thread 0x7fffe77fe700 (LWP 4804)]
[1508157256] libunbound[4766:0] info: warning: unsupported algorithm for trust anchor . DS IN
[1508157256] libunbound[4766:0] warning: trust anchor . has no supported algorithms, the anchor is ignored (check if you need to upgrade unbound and openssl)
[Thread 0x7fffe7fff700 (LWP 4803) exited]
[Thread 0x7fffecfd9700 (LWP 4802) exited]
[Thread 0x7fffed7da700 (LWP 4801) exited]
[Thread 0x7fffe77fe700 (LWP 4804) exited]
2017-10-16 12:34:20.696     7ffff7fe4780        INFO    global  src/daemon/p2p.h:68     P2p server initialized OK
2017-10-16 12:34:20.696     7ffff7fe4780        INFO    global  src/daemon/rpc.h:58     Initializing core rpc server...
2017-10-16 12:34:20.696     7ffff7fe4780        INFO    global  contrib/epee/include/net/http_server_impl_base.h:70     Binding on 127.0.0.1:18081
2017-10-16 12:34:20.696     7ffff7fe4780        INFO    global  src/daemon/rpc.h:63     Core rpc server initialized OK on port: 18081
2017-10-16 12:34:20.696     7ffff7fe4780        INFO    global  src/daemon/core.h:73    Initializing core...
2017-10-16 12:34:20.697     7ffff7fe4780        INFO    global  src/cryptonote_core/cryptonote_core.cpp:323     Loading blockchain from folder /home/monero/data/lmdb ...
[New Thread 0x7fffe77fe700 (LWP 4805)]

Program received signal SIGBUS, Bus error.
0x00007ffff7443295 in __memcpy_ssse3_back () from /lib64/libc.so.6
Missing separate debuginfos, use: debuginfo-install glibc-2.17-157.el7_3.2.x86_64
(gdb) bt
#0  0x00007ffff7443295 in __memcpy_ssse3_back () from /lib64/libc.so.6
#1  0x0000000000c25abf in std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::_M_mutate(unsigned long, unsigned long, char const*, unsigned long) ()
#2  0x0000000000c2678b in std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::_M_replace(unsigned long, unsigned long, char const*, unsigned long) ()
#3  0x00000000007d7ad2 in cryptonote::BlockchainLMDB::for_all_txpool_txes(std::function<bool (crypto::hash const&, cryptonote::txpool_tx_meta_t const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const*)>, bool) const ()
#4  0x000000000080526c in cryptonote::Blockchain::for_all_txpool_txes(std::function<bool (crypto::hash const&, cryptonote::txpool_tx_meta_t const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const*)>, bool) const ()
#5  0x000000000084b6b5 in cryptonote::tx_memory_pool::init() ()
#6  0x00000000008410c1 in cryptonote::core::init(boost::program_options::variables_map const&, cryptonote::test_options const*) ()
#7  0x0000000000649ed0 in daemonize::t_daemon::run(bool) ()
#8  0x000000000074ca0a in daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) ()
#9  0x000000000074ee3c in bool daemonizer::daemonize<daemonize::t_executor>(int, char const**, daemonize::t_executor&&, boost::program_options::variables_map const&) ()
#10 0x000000000061ed87 in main ()
(gdb)


# Discussion History
## moneromooo-monero | 2017-10-16T13:15:51+00:00
Can you post on fpaste.org (or pastebin.mozilla.org) the output of these two commands, please:

mdb_dump -s txpool_meta ~/.bitmonero/lmdb
mdb_dump -s txpool_blob ~/.bitmonero/lmdb

Thanks


## avfedorov | 2017-10-16T22:28:38+00:00
https://paste.fedoraproject.org/paste/L9oX7Cm-rTljDbf6Gh3JSw

## hyc | 2017-10-17T12:28:44+00:00
Check in your kernel log (or dmesg output) when these Bus errors happen, is there any other error message around the same time?

Are you able to physically copy the data.mdb file to another drive, or does that also fail? This is looking more like a hardware failure than anything else.

## avfedorov | 2017-10-17T13:01:39+00:00
No any other messages in logs or dmesg.
data.mdb copied to another place without any problem.
Before this server was turned off incorrectly by power failure.
Perhaps this resulted in data corruption, if you see inconsistencies in mdb.
In this case, the data storage engine is not good, if it can not recover after such simple failures.

## hyc | 2017-10-17T14:09:48+00:00
You can try starting monerod with `--db-salvage` in that case. You hadn't mentioned you had a power failure.

## madranet | 2018-01-02T16:59:13+00:00
I'm getting this too on OSX with `Version: 0.11.1.0 Helium Hydra`

If I run the GUI wallet, I get an error, after a few minutes, saying the `monerod` daemon has crashed:

![2018-01-02_16-51-11](https://user-images.githubusercontent.com/669658/34491885-32d4572c-efdd-11e7-9b3f-4ea887c8183b.png)

However, if I start `monerod` on its own from the command line, it syncs properly:

```
./monerod --data-dir /path/to/external/drive/Monero

<snip>

2018-01-02 16:45:02.668	[P2P9]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:305	[67.160.127.187:18080 OUT] Sync data returned a new top block candidate: 1478449 -> 1478450 [Your node is 1 blocks (0 days) behind]
SYNCHRONIZATION started
2018-01-02 16:45:07.059	[P2P2]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[92.255.182.137:18080 OUT]  Synced 1478450/1478450
2018-01-02 16:45:07.059	[P2P3]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1521	SYNCHRONIZED OK
2018-01-02 16:45:07.059	[P2P2]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1521	SYNCHRONIZED OK
2018-01-02 16:45:07.059	[P2P3]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1543
**********************************************************************
You are now synchronized with the network. You may now start monero-wallet-cli.

Use the "help" command to see the list of available commands.
**********************************************************************
```

Then, if I either start `monero-wallet-cli` from the command line or run the GUI application, `monerod` crashes again, after a couple of minutes, with `monero-wallet-cli` reporting the following error:

```
Monero 'Helium Hydra' (v0.11.1.0-release)
Logging to ./monero-wallet-cli.log
Wallet password: **********
Opened wallet: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
**********************************************************************
Use "help" command to see the list of available commands.
**********************************************************************
Starting refresh...
Error: refresh failed: no connection to daemon. Please make sure daemon is running.. Blocks received: 0
Background refresh thread started
````

...and `monerod` reporting a bus error:

```
[1]    19400 bus error  ./monerod --data-dir /path/to/external/drive/Monero
```


EDIT: just to iterate; no power outages or hardware problems at my end.  My Monero datadir is on an external drive, but it synchronises without issue when the daemon is run by itself. It's only when the GUI or CLI wallets are run that the daemon crashes.

## moneromooo-monero | 2018-01-04T13:20:31+00:00
A DB fix was merged in #3019

## 78bash | 2018-04-07T17:40:19+00:00
This happened with me when I tried to run monerod after moving data.mdb from another location but the transfer was incomplete due to insufficient drive capacity. After resolving that issue, I reran monerod and my blockchain fully synced. I didn't need to flag --db-salvage. I did specify --data-dir. Hope this helps.

## ytrezq | 2019-11-28T20:55:11+00:00
Got the same problem. But in my case no unclean shutdown. I only have a rotating drive so I synced on a remote server then downloaded the database to a different location which is how the error is triggered.

Though in my case, `mdb_dump` fails too with the same error.

## moneromooo-monero | 2019-12-01T16:02:45+00:00
Did you copy the blockchain while monerod was running ? Do the two computers have the same endianness ?

# Action History
- Created by: avfedorov | 2017-10-16T12:38:29+00:00
