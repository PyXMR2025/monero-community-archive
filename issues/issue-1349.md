---
title: Segmentation fault issue
source_url: https://github.com/monero-project/monero/issues/1349
author: will22
assignees: []
labels: []
created_at: '2016-11-17T00:52:38+00:00'
updated_at: '2017-10-19T13:45:05+00:00'
type: issue
status: closed
closed_at: '2017-09-19T23:36:21+00:00'
---

# Original Description
I am running a 32 bit linux version (v0-10-0-0) of monerod in a whonix virtual machine. 

The first time I ran monerod in whonix, everything worked perfectly. But every time after that, when I try to start it up, everything looks normal (green line read: NET service bound to ...)(second green line read: core rpc server initialized OK on port ...), but then (after 5 more white lines of stuff) I get Segmentation fault and everything stops. 

Also, I notice my monero folder on my base OS has a monero-wallet-cli.log but on my whonix instance my monero folder never makes one of those that I see at least (it is the 32 bit version on whonix, but 64 bit version on my base OS)

According to [this](https://unix.stackexchange.com/questions/132192/running-application-ends-with-segmentation-fault), it (the segmentation fault) seems like it's a bug in monerod. How can I fix this problem?
 

# Discussion History
## vtnerd | 2016-11-17T13:08:23+00:00
This is definitely a bug in monero - I've seen it on Gentoo. Everytime the first two runs after boot result in segmentation fault, and the third time it runs.

@will22 What distribution as you using?


## will22 | 2016-11-17T15:35:31+00:00
I am using Ubuntu 16.04. Mine only worked the first time, and hasn't worked since.


## moneromooo-monero | 2016-11-17T20:26:50+00:00
Do you have a stack trace ? If you're not familiar with getting one:

ulimit -c
ulimit -c unlimited
gdb /path/to/monerod /path/to/core
bt

Then you can run ulimit -c XXX, replacing XXX with whatever the first ulimit -c command returned (if it already said unlimited, you can leave it).


## ghost | 2016-11-17T21:05:02+00:00
Side issue - @moneromooo-monero maybe add those instructions to the readme/elsewhere for people wanting to do debugging? I keep having to come back to old issues just to see the (very good) instructions you've given me in the past


## moneromooo-monero | 2016-11-17T21:42:34+00:00
Yes, good idea, since there are many Linux users who don't know much about Linux nowadays.
Please file a bug asking for such a HOWTO and I'll write one at some point.


## will22 | 2016-11-18T02:19:58+00:00
@moneromooo-monero I followed the directions in the [link](https://unix.stackexchange.com/questions/132192/running-application-ends-with-segmentation-fault) I posted above because I didn't understand what you were telling me to do. 

(I ran "sudo apt-get install gdb) I switched to the directory monerod was in, and instead of typing "./monerod" like usual to start the program, I typed "gdb monerod". Licensing stuff popped up and at the end a prompt appeared "(gdp)_ ".  I typed "run". It for the most part looked like the program monerod was starting up like normal, then it ran into the segmentation fault. I then typed "bt" in the (gdp)_ prompt. I received:

[Program received signal SIGSEGV, Segmentation fault.
0x0850c535 in mdb_cmp_long ()
(gdb) bt
#0  0x0850c535 in mdb_cmp_long ()
#1  0x0850c7cd in mdb_node_search ()
#2  0x085126db in mdb_cursor_set ()
#3  0x08514e9f in mdb_cursor_put.part ()
#4  0x08518fed in mdb_txn_commit ()
#5  0x082f39f4 in cryptonote::mdb_txn_safe::commit(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) ()
#6  0x082fe918 in cryptonote::BlockchainLMDB::open(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, int) ()
#7  0x08292d89 in cryptonote::core::init(boost::program_options::variables_map const&, cryptonote::test_options const*) ()
#8  0x08222490 in daemonize::t_daemon::run(bool) ()
#9  0x083b2865 in daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) ()
#10 0x081a004c in main ()
(gdb) ]

Question:
Did I file this bug report in the proper place and format? Following [this](https://github.com/adobe/brackets/wiki/How-to-Report-an-Issue) it seemed like I was supposed to put the lines I pasted from my terminal in brakets, so I did.

Does the person who fixes a bug generally notify the question asker? About how long would somthing like this take (I only ask because if its going to be a few days, I need to figure out a work around somehow)

Lastly, here is what happened when I followed the steps you wrote"

[Type: "whonix" <enter> for help.
user@host:~$ cd ~/**************************
user@host:~/*************************_$ ulimit -c
0
user@host:~/**_**********************_$ ulimit -c unlimited
user@host:~/**_***********************$ gdb monerod
GNU gdb (Debian 7.7.1+dfsg-5) 7.7.1
Copyright (C) 2014 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later http://gnu.org/licenses/gpl.html
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "i586-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
http://www.gnu.org/software/gdb/bugs/.
Find the GDB manual and other documentation resources online at:
http://www.gnu.org/software/gdb/documentation/.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from monerod...done.
(gdb) bt
No stack.
(gdb) ulimit -c 0
Undefined command: "ulimit".  Try "help".
(gdb) ]

Although I believe, I got what you wanted from the other directions I followed, I would like to know if I misunderstood your steps.

Thanks

EDIT: This post automatically put a few things in italics and bold that I didn't tell it to. Dont know why.
EDIT: Ok this: "(gdp)_ " in the secon paragraph caused everything to be italicized, so I added a space between the underscore and the quote to get rid of it. 


## moneromooo-monero | 2016-11-18T12:47:31+00:00
Thanks, the stack trace in the middle is what I was interested in. It shows a crash in liblmdb. I suspect this is due to 32 bits, rather than Whonix. I'll ping hyc, who's the expert at that.


## ghost | 2016-11-21T23:58:04+00:00
I think you may have forgotten to ping @hyc :)

## hyc | 2016-11-22T02:15:56+00:00
How big is the data.mdb file at this point? Might want to get a copy of it to dissect it.

## abelboldu | 2016-11-22T10:01:05+00:00
Hi,

I'm experiencing this on a RPi node also.


After some long time syncing, I stopped it with a ^C, and now it segfaults when starts to sync again.


Backtrace:
```
Program terminated with signal SIGSEGV, Segmentation fault.
#0  0x004739fe in std::_Rb_tree_rebalance_for_erase(std::_Rb_tree_node_base*, std::_Rb_tree_node_base&) ()
[Current thread is 1 (LWP 19981)]
```
```
Thread 19 "monerod" received signal SIGSEGV, Segmentation fault.
[Switching to LWP 20040]
0x004739fe in std::_Rb_tree_rebalance_for_erase(std::_Rb_tree_node_base*, std::_Rb_tree_node_base&) ()
(gdb) bt
#0  0x004739fe in std::_Rb_tree_rebalance_for_erase(std::_Rb_tree_node_base*, std::_Rb_tree_node_base&) ()
#1  0x00249120 in std::_Rb_tree<unsigned int, std::pair<unsigned int const, long>, std::_Select1st<std::pair<unsigned int const, long> >, std::less<unsigned int>, std::allocator<std::pair<unsigned int const, long> > >::_M_erase_aux(std::_Rb_tree_const_iterator<std::pair<unsigned int const, long> >) ()
#2  0x00252286 in cryptonote::tx_memory_pool::take_tx(crypto::hash const&, cryptonote::transaction&, unsigned int&, unsigned long long&, bool&) ()
#3  0x001fee54 in cryptonote::Blockchain::handle_block_to_main_chain(cryptonote::block const&, crypto::hash const&, cryptonote::block_verification_context&) ()
#4  0x0020049e in cryptonote::Blockchain::add_new_block(cryptonote::block const&, cryptonote::block_verification_context&) ()
#5  0x001ec846 in cryptonote::core::handle_incoming_block(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, cryptonote::block_verification_context&, bool) ()
#6  0x002356fe in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_response_get_objects(int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&) ()
#7  0x00332c20 in int epee::net_utils::buff_to_t_adapter<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, cryptonote::NOTIFY_RESPONSE_G
ET_OBJECTS::request, cryptonote::cryptonote_connection_context, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > > >(cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > >, cryptonote::cryptonote_connection_context&) [clone .constprop.483] ()
#8  0x0033477c in int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&) [clone .constprop.448] ()
#9  0x001c1d02 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::notify(int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&) ()
#10 0x001a39de in epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv(void const*, unsigned int) ()
#11 0x001a7df4 in epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_read(boost::system::error_code const&, unsigned int) ()
#12 0x00207a52 in boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned int>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned int>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned int>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context---Type <return> to continue, or q <return> to quit---
_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned int) ()
#13 0x002083b2 in boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned int>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned int) ()
#14 0x0027ae50 in boost::asio::detail::task_io_service::run(boost::system::error_code&) [clone .constprop.1093] ()
#15 0x0018f420 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#16 0x0038bd0e in thread_proxy ()
#17 0x76f1af40 in ?? ()
Backtrace stopped: previous frame identical to this frame (corrupt stack?)
```

## hyc | 2016-11-22T12:47:33+00:00
@abelboldu that's unrelated to the DB. Sounds like your poolstate.bin is corrupted. You can just delete that and restart.

## abelboldu | 2016-11-22T13:29:55+00:00
@hyc thanks

## ghost | 2016-11-24T13:26:02+00:00
Hi @hyc, is there any simple way for people to determine this file has become corrupted in the future?

## ghost | 2016-11-24T13:26:26+00:00
I can add the details to the Readme under debugging

## hyc | 2016-11-24T14:05:04+00:00
Not at present. We've never needed such a feature before. I suppose running mdb_dump -a > /dev/null would tell you.

## kellrobinson | 2016-12-11T20:18:55+00:00
I got the segmentation fault error.  I looked and there is no poolstate.bin file in the .bitmonero folder.  I'm using ARMv7 monero 10.0.0 on an android phone.  I imported the blockchain from a raw file.  I have not been able to sync up any blocks, beyond what I imported.

## pvl1 | 2017-03-19T00:53:04+00:00
confirmed on another arm board, no poolstate.bin file. running ubuntu

## vdo | 2017-08-11T19:15:40+00:00
Another segmentation fault, on a PINE64 board, removed poolstate.bin first:
```
dietpi@dietxmr:~$ gdb monero/monerod
GNU gdb (Debian 7.7.1+dfsg-5) 7.7.1
Copyright (C) 2014 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "aarch64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from monero/monerod...(no debugging symbols found)...done.
(gdb) run
Starting program: /home/dietpi/monero-v0.10.3.1/monerod
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/aarch64-linux-gnu/libthread_db.so.1".
2017-08-11 20:13:30.493         INFO    global  contrib/epee/src/mlog.cpp:145  N
ew log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,ve
rify:FATAL,stacktrace:INFO
2017-08-11 20:13:30.495         INFO    global  src/daemon/main.cpp:282 Monero '
Wolfram Warptangent' (v0.10.3.1-release)
2017-08-11 20:13:30.497         INFO    global  src/daemon/protocol.h:55       I
nitializing cryptonote protocol...
2017-08-11 20:13:30.497         INFO    global  src/daemon/protocol.h:60       C
ryptonote protocol initialized OK
2017-08-11 20:13:30.499         INFO    global  src/daemon/p2p.h:63     Initiali
zing p2p server...
[New Thread 0x7fb7d871e0 (LWP 2422)]
[New Thread 0x7fb75871e0 (LWP 2423)]
[New Thread 0x7fb6c951e0 (LWP 2424)]
[New Thread 0x7fb64951e0 (LWP 2425)]
[Thread 0x7fb6c951e0 (LWP 2424) exited]
[Thread 0x7fb7d871e0 (LWP 2422) exited]
[Thread 0x7fb64951e0 (LWP 2425) exited]
[Thread 0x7fb75871e0 (LWP 2423) exited]
2017-08-11 20:13:35.281         INFO    global  src/daemon/p2p.h:68     P2p serv
er initialized OK
2017-08-11 20:13:35.282         INFO    global  src/daemon/rpc.h:58     Initiali
zing core rpc server...
2017-08-11 20:13:35.282         INFO    global  contrib/epee/include/net/http_se
rver_impl_base.h:70     Binding on 127.0.0.1:18081
2017-08-11 20:13:35.282         INFO    global  src/daemon/rpc.h:63     Core rpc
 server initialized OK on port: 18081
2017-08-11 20:13:35.283         INFO    global  src/daemon/core.h:73    Initializing core...
2017-08-11 20:13:35.285         INFO    global  src/cryptonote_core/cryptonote_core.cpp:326     Loading blockchain from folder /home/dietpi/.bitmonero/lmdb ...

Program received signal SIGSEGV, Segmentation fault.
memmove () at ../ports/sysdeps/aarch64/memmove.S:156
156     ../ports/sysdeps/aarch64/memmove.S: No such file or directory.
(gdb) bt
#0  memmove () at ../ports/sysdeps/aarch64/memmove.S:156
#1  0x00000000009a77e0 in mdb_node_add ()
#2  0x00000000009a3558 in mdb_cursor_put ()
#3  0x00000000009a2748 in mdb_txn_commit ()
#4  0x000000000096b05c in cryptonote::mdb_txn_safe::commit(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) ()
#5  0x0000000000978b80 in cryptonote::BlockchainLMDB::open(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, int) ()
#6  0x00000000008a7804 in cryptonote::core::init(boost::program_options::variables_map const&, cryptonote::test_options const*) ()
#7  0x00000000006f9c1c in daemonize::t_core::run() ()
#8  0x00000000006f8fc0 in daemonize::t_daemon::run(bool) ()
#9  0x00000000007b23b4 in daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) ()
#10 0x00000000007b4b34 in main ()
(gdb)
```


## hyc | 2017-08-12T02:08:17+00:00
@vdo looks like a corrupted DB. What are you using for storage on that pine64? Has it crashed/shutdown uncleanly before?


## vdo | 2017-08-12T08:13:29+00:00
@hyc Yes, I suffered several power cuts this week actually, and the node daemon starts automatically with supervidord, so it has to be the case.
Is there any way to fix the corrupted db? If not I will just rsync it from another place...

## hyc | 2017-08-12T09:36:33+00:00
At present there's no convenient way to recover it. If you're comfortable with a binary/hex file editor I can give you manual steps to try.

## vdo | 2017-08-15T10:04:09+00:00
Thanks @hyc , sounds like an interesting exercise but I don't have the time to put my hands on a hex editor atm :)
I will just rsync the data.lmdb from my desktop machine.

Feature request: put 'checkpoints' in the database sync to recover it in the case of a  ungraceful shutdown.

## hyc | 2017-08-15T10:50:32+00:00
PR #2288 will add a recovery feature.

## vdo | 2017-09-12T22:31:02+00:00
Still having similar issues with de new --db-salvage  option:

```
dietpi@dietxmr:~/monero$ ./monerod --db-salvage
2017-09-12 22:25:26.147	      7f9c212000	INFO 	global	src/daemon/main.cpp:279	Monero 'Helium Hydra' (v0.11.0.0-02e5dcd2)
2017-09-12 22:25:26.148	      7f9c212000	INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2017-09-12 22:25:26.149	      7f9c212000	INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
2017-09-12 22:25:26.151	      7f9c212000	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2017-09-12 22:25:30.752	      7f9c212000	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2017-09-12 22:25:30.752	      7f9c212000	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
2017-09-12 22:25:30.752	      7f9c212000	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:70	Binding on 127.0.0.1:18081
2017-09-12 22:25:30.753	      7f9c212000	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2017-09-12 22:25:30.753	      7f9c212000	INFO 	global	src/daemon/core.h:73	Initializing core...
2017-09-12 22:25:30.755	      7f9c212000	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:319	Loading blockchain from folder /home/dietpi/.bitmonero/lmdb ...
Segmentation fault
dietpi@dietxmr:~/monero$ ls
dummy  dummy.address.txt  dummy.keys  monero-blockchain-export	monero-blockchain-import  monerod  monero-utils-deserialize  monero-wallet-cli	monero-wallet-cli.log  monero-wallet-rpc  terminfo.txt
dietpi@dietxmr:~/monero$ gdb monerod core 
GNU gdb (Debian 7.7.1+dfsg-5) 7.7.1
Copyright (C) 2014 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "aarch64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from monerod...(no debugging symbols found)...done.

warning: core file may not match specified executable file.
[New LWP 13744]
[New LWP 13746]
[New LWP 13747]
[New LWP 13745]
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/aarch64-linux-gnu/libthread_db.so.1".
Core was generated by `'.
Program terminated with signal SIGSEGV, Segmentation fault.
#0  memmove () at ../ports/sysdeps/aarch64/memmove.S:156
156	../ports/sysdeps/aarch64/memmove.S: No such file or directory.
(gdb) bt
#0  memmove () at ../ports/sysdeps/aarch64/memmove.S:156
#1  0x000000556b005c10 in mdb_node_add ()
#2  0x000000556b0088ac in mdb_cursor_put.part ()
#3  0x000000556b00a0e4 in mdb_txn_commit ()
#4  0x000000556af09d54 in cryptonote::mdb_txn_safe::commit(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) ()
#5  0x000000556af29cf0 in cryptonote::BlockchainLMDB::open(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, int) ()
#6  0x000000556af61ee4 in cryptonote::core::init(boost::program_options::variables_map const&, cryptonote::test_options const*) ()
#7  0x000000556adb47d0 in daemonize::t_daemon::run(bool) ()
#8  0x000000556ae4e52c in daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) ()
#9  0x000000556ae504bc in bool daemonizer::daemonize<daemonize::t_executor>(int, char const**, daemonize::t_executor&&, boost::program_options::variables_map const&) ()
#10 0x000000556ad8e224 in main ()


```

## hyc | 2017-09-12T22:33:42+00:00
Unfortunate. Then you're just going to have to resync from scratch. Use `--db-sync-mode safe` from now on, too.

## vdo | 2017-09-12T22:42:27+00:00
OK, will do and try again with synced data.

Prior to this error, monerod was literally 'killing' my board even with ` --db-sync-mode safe`(no logs, no coredumps) so I had to restart it powering off.
Sadly I couldn't grab any more information about that issue which I suspect is a different one.

maybe a x64 board would be a better alternative?


## hyc | 2017-09-12T23:03:07+00:00
I was having a lot of problems due to unstable power supply with my Pine64 early on too. Buying a beefier USB cable helped, as well as a high-output USB power supply.

## hyc | 2017-09-12T23:03:58+00:00
At this point I don't think there's anything more we can do with this issue. Unstable hardware can't be fixed with software. Close it?

## vdo | 2017-09-12T23:17:27+00:00
ok for me

## jonathancross | 2017-09-19T23:22:20+00:00
This seems to be resolved.  Anyone disagree with closing?

## hyc | 2017-09-19T23:31:30+00:00
+resolved

## Titan-C | 2017-10-18T09:24:45+00:00
I'm experiencing a segmentation fault too.
I use archlinux. Installed monero 0.11.0.0 from archlinux aur, and compiled from source.

```bash
gdb --args monerod --data-dir=/scratch/monero          
GNU gdb (GDB) 8.0.1
Copyright (C) 2017 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-pc-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from monerod...(no debugging symbols found)...done.
(gdb) run
Starting program: /usr/bin/monerod --data-dir=/scratch/monero
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/usr/lib/libthread_db.so.1".
2017-10-18 09:23:16.526	    7ffff7fb5780	INFO 	global	src/daemon/main.cpp:279	Monero 'Helium Hydra' (v0.11.0.0-release)
2017-10-18 09:23:16.527	    7ffff7fb5780	INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2017-10-18 09:23:16.527	    7ffff7fb5780	INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
[New Thread 0x7ffff24ff700 (LWP 29654)]
[New Thread 0x7ffff1ffe700 (LWP 29655)]
[New Thread 0x7ffff1afd700 (LWP 29656)]
[New Thread 0x7ffff15fc700 (LWP 29657)]
[New Thread 0x7ffff10fb700 (LWP 29658)]
[New Thread 0x7ffff0bfa700 (LWP 29659)]
[New Thread 0x7ffff06f9700 (LWP 29660)]
[New Thread 0x7ffff01f8700 (LWP 29661)]
[New Thread 0x7fffefcf7700 (LWP 29662)]
[New Thread 0x7fffef7f6700 (LWP 29663)]
[New Thread 0x7fffef2f5700 (LWP 29664)]
2017-10-18 09:23:16.529	    7ffff7fb5780	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
[New Thread 0x7fffeedf4700 (LWP 29665)]
[New Thread 0x7fffee5f3700 (LWP 29666)]
[New Thread 0x7fffeddf2700 (LWP 29667)]
[New Thread 0x7fffed5f1700 (LWP 29668)]
[Thread 0x7fffed5f1700 (LWP 29668) exited]
[Thread 0x7fffeddf2700 (LWP 29667) exited]
[Thread 0x7fffeedf4700 (LWP 29665) exited]
[Thread 0x7fffee5f3700 (LWP 29666) exited]
2017-10-18 09:23:21.146	    7ffff7fb5780	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2017-10-18 09:23:21.146	    7ffff7fb5780	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
2017-10-18 09:23:21.147	    7ffff7fb5780	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:70	Binding on 127.0.0.1:18081
2017-10-18 09:23:21.147	    7ffff7fb5780	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2017-10-18 09:23:21.147	    7ffff7fb5780	INFO 	global	src/daemon/core.h:73	Initializing core...
2017-10-18 09:23:21.147	    7ffff7fb5780	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:323	Loading blockchain from folder /scratch/monero/lmdb ...
[New Thread 0x7fffed5f1700 (LWP 29676)]
2017-10-18 09:23:21.471	    7ffff7fb5780	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:421	Loading checkpoints
2017-10-18 09:23:21.544	    7ffff7fb5780	INFO 	global	src/daemon/core.h:78	Core initialized OK
2017-10-18 09:23:21.544	    7ffff7fb5780	INFO 	global	src/daemon/rpc.h:68	Starting core rpc server...
[New Thread 0x7fffeddf2700 (LWP 29677)]
[New Thread 0x7fffee5f3700 (LWP 29678)]
2017-10-18 09:23:21.545	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:73	Core rpc server started ok
[New Thread 0x7fffeedf4700 (LWP 29679)]
[New Thread 0x7fffeca54700 (LWP 29680)]
2017-10-18 09:23:21.547	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:78	Starting p2p net loop...
[New Thread 0x7fffdffff700 (LWP 29681)]
[New Thread 0x7fffdf7fe700 (LWP 29682)]
[New Thread 0x7fffdf2fd700 (LWP 29683)]
[New Thread 0x7fffdedfc700 (LWP 29684)]
[New Thread 0x7fffde8fb700 (LWP 29685)]
[New Thread 0x7fffde3fa700 (LWP 29686)]
[New Thread 0x7fffddef9700 (LWP 29687)]
[New Thread 0x7fffdd9f8700 (LWP 29688)]
[New Thread 0x7fffdd4f7700 (LWP 29689)]
[New Thread 0x7fffdcff6700 (LWP 29690)]
[New Thread 0x7fffdcaf5700 (LWP 29691)]
2017-10-18 09:23:22.548	[P2P1]	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:1231	
**********************************************************************
The daemon will start synchronizing with the network. This may take a long time to complete.

You can set the level of process detailization* through "set_log <level|categories>" command*,
where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING)

Use the "help" command to see the list of available commands.
**********************************************************************

2017-10-18 09:23:24.971	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1543	
**********************************************************************
You are now synchronized with the network. You may now start monero-wallet-cli.

Use the "help" command to see the list of available commands.
**********************************************************************
2017-10-18 09:23:25.952	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:305	[73.200.76.71:18080 OUT] Sync data returned a new top block candidate: 1288623 -> 1377932 [Your node is 89309 blocks (124 days) behind] 
SYNCHRONIZATION started
2017-10-18 09:23:26.000	[P2P1]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:305	[139.59.145.83:18080 OUT] Sync data returned a new top block candidate: 1288623 -> 1423258 [Your node is 134635 blocks (186 days) behind] 
SYNCHRONIZATION started

Thread 25 "monerod" received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0x7fffdedfc700 (LWP 29684)]
0x00005555558abcab in cryptonote::Blockchain::handle_block_to_main_chain(cryptonote::block const&, crypto::hash const&, cryptonote::block_verification_context&) ()
(gdb) bt
#0  0x00005555558abcab in cryptonote::Blockchain::handle_block_to_main_chain(cryptonote::block const&, crypto::hash const&, cryptonote::block_verification_context&) ()
#1  0x00005555558b20ee in cryptonote::Blockchain::add_new_block(cryptonote::block const&, cryptonote::block_verification_context&) ()
#2  0x00005555558c78b4 in cryptonote::core::handle_incoming_block(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, cryptonote::block_verification_context&, bool) ()
#3  0x00005555557745a5 in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::try_add_next_blocks(cryptonote::cryptonote_connection_context&) ()
#4  0x00005555557775d9 in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_response_get_objects(int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&) ()
#5  0x0000555555762f20 in int epee::net_utils::buff_to_t_adapter<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request, cryptonote::cryptonote_connection_context, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > > >(cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > >, cryptonote::cryptonote_connection_context&) ()
#6  0x0000555555765a67 in int cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_invoke_map<cryptonote::cryptonote_connection_context>(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, cryptonote::cryptonote_connection_context&, bool&) ()
#7  0x000055555577d15a in int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&) ()
#8  0x000055555577d3b0 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::notify(int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&) ()
#9  0x000055555577d8bf in epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote---Type <return> to continue, or q <return> to quit---
_connection_context> >::handle_recv(void const*, unsigned long) ()
#10 0x000055555578382d in epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_read(boost::system::error_code const&, unsigned long) ()
#11 0x0000555555740f9e in void boost::asio::detail::strand_service::dispatch<boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long> >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long>&) ()
#12 0x00005555557412b5 in boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#13 0x0000555555741628 in void boost::asio::detail::strand_service::dispatch<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boos---Type <return> to continue, or q <return> to quit---
t::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > >&) ()
#14 0x00005555557418f5 in boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#15 0x00005555557002a0 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#16 0x00007ffff650944f in ?? () from /usr/lib/libboost_thread.so.1.65.1
#17 0x00007ffff532808a in start_thread () from /usr/lib/libpthread.so.0
#18 0x00007ffff506024f in clone () from /usr/lib/libc.so.6
(gdb) 
```

## radfish | 2017-10-18T17:34:36+00:00
On Wed, Oct 18, 2017 at 02:24:56AM -0700, Óscar Nájera wrote:
> I'm experiencing a segmentation fault too.
> I use archlinux. Installed monero 0.11.0.0 from archlinux aur, and compiled from source.

Try monero-git AUR pkg, there have been fixes to sync since the release.


## Titan-C | 2017-10-18T22:31:22+00:00
> Try monero-git AUR pkg, there have been fixes to sync since the release.

monero-git does not even compile. I can't install it.


## radfish | 2017-10-19T02:24:38+00:00
On Wed, Oct 18, 2017 at 03:31:25PM -0700, Óscar Nájera wrote:
> > Try monero-git AUR pkg, there have been fixes to sync since the release.
> 
> monero-git does not even compile. I can't install it.

Builds fine for me. What's the error?


## Titan-C | 2017-10-19T13:45:04+00:00
> Builds fine for me. What's the error?

I don't get a very useful info from pacaur.

:: Synchronizing package databases...
 core is up to date
 extra                                        1658.2 KiB  8.66M/s 00:00 [########################################] 100%
 community                                       4.1 MiB  6.68M/s 00:01 [########################################] 100%
:: Starting AUR upgrade...
:: resolving dependencies...
:: looking for inter-conflicts...

AUR Packages  (1)  Old Version  New Version

aur/monero-git                  latest

:: Proceed with installation? [Y/n]

:: Retrieving package(s)...
:: monero-git build files are up-to-date -- skipping
:: Checking monero-git integrity...
==> Making package: monero-git 0.11.0.0-1 (Thu Oct 19 15:51:31 CEST 2017)
==> Retrieving sources...
  -> Updating monero git repo...
Fetching origin
remote: Counting objects: 171, done.
remote: Compressing objects: 100% (37/37), done.
remote: Total 171 (delta 130), reused 154 (delta 127), pack-reused 7
Receiving objects: 100% (171/171), 69.91 KiB | 6.99 MiB/s, done.
Resolving deltas: 100% (133/133), completed with 44 local objects.
From https://github.com/monero-project/monero
 + 82bf0245...75af2b76 refs/pull/2134/head  -> refs/pull/2134/head  (forced update)
 + baa26c53...ee0a7931 refs/pull/2134/merge -> refs/pull/2134/merge  (forced update)
 * [new ref]           refs/pull/2681/head  -> refs/pull/2681/head
 * [new ref]           refs/pull/2681/merge -> refs/pull/2681/merge
 * [new ref]           refs/pull/2682/head  -> refs/pull/2682/head
 * [new ref]           refs/pull/2682/merge -> refs/pull/2682/merge
 * [new ref]           refs/pull/2683/head  -> refs/pull/2683/head
 * [new ref]           refs/pull/2683/merge -> refs/pull/2683/merge
 * [new ref]           refs/pull/2684/head  -> refs/pull/2684/head
 * [new ref]           refs/pull/2684/merge -> refs/pull/2684/merge
==> Validating source files with md5sums...
    monero ... Skipped
:: Building monero-git package(s)...
==> Making package: monero-git 0.11.0.0.r4797.4b228dd3-1 (Thu Oct 19 15:51:38 CEST 2017)
==> Checking runtime dependencies...
==> Checking buildtime dependencies...
==> WARNING: Using existing $srcdir/ tree
==> Starting pkgver()...
==> Removing existing $pkgdir/ directory...
==> Starting build()...
-- The C compiler identification is GNU 7.2.0
-- The CXX compiler identification is GNU 7.2.0
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Building without build tag
-- Could not find DEVELOPER_LOCAL_TOOLS in env (not required)
-- BOOST_IGNORE_SYSTEM_PATHS defaults to OFF
-- Could not find DEVELOPER_LIBUNBOUND_OLD in env (not required)
-- Building for a 64-bit system
-- Building internal libraries as static
-- Could not find DATABASE in env (not required unless you want to change database type from default: lmdb)
-- Using LMDB as default DB type
-- Stack trace on exception enabled (using easylogging++)
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Looking for pthread_create
-- Looking for pthread_create - not found
-- Check if compiler accepts -pthread
-- Check if compiler accepts -pthread - yes
-- Found Threads: TRUE
-- Found OpenSSL: /usr/lib/libcrypto.so (found version "1.1.0f")
-- Using OpenSSL include dir at /usr/include
-- Found MiniUPnPc: /usr/include/miniupnpc
-- Found miniupnpc API version 16
-- Using shared miniupnpc found at /usr/include/miniupnpc
-- Looking for libunbound
-- Found libunbound include (unbound.h) in /usr/include
-- Found libunbound shared library
-- Using 64-bit LMDB from source tree
-- Building on x86_64 for native
-- AES support enabled
-- Found Boost Version: 106501
-- Found Readline: /usr/include
-- Performing Test GNU_READLINE_FOUND
-- Performing Test GNU_READLINE_FOUND - Success
-- Found readline library at: /usr
-- Found Git: /usr/bin/git
-- Found Doxygen: /usr/bin/doxygen (found version "1.8.13") found components:  doxygen dot
-- Configuring done
-- Generating done
-- Build files have been written to: /home/oscar/.cache/pacaur/monero-git/src/monero/build
Scanning dependencies of target genversion
Scanning dependencies of target lmdb
Scanning dependencies of target easylogging
Scanning dependencies of target obj_version
Scanning dependencies of target obj_cncrypto
Scanning dependencies of target obj_checkpoints
Scanning dependencies of target obj_cryptonote_basic
Scanning dependencies of target obj_cryptonote_core
[  1%] Generating testnet_blocks.o
Scanning dependencies of target obj_ringct
Scanning dependencies of target obj_blockchain_db
make[2]: *** No rule to make target 'version.cpp', needed by 'src/CMakeFiles/obj_version.dir/__/version.cpp.o'.  Stop.
make[1]: *** [CMakeFiles/Makefile2:451: src/CMakeFiles/obj_version.dir/all] Error 2
make[1]: *** Waiting for unfinished jobs....
Scanning dependencies of target obj_common
[  2%] Building CXX object external/easylogging++/CMakeFiles/easylogging.dir/easylogging++.cc.o
[  3%] Generating blocks.o
-- You are currently on commit 4b228dd3
[  4%] Building C object external/db_drivers/liblmdb/CMakeFiles/lmdb.dir/midl.c.o
[  5%] Building C object external/db_drivers/liblmdb/CMakeFiles/lmdb.dir/mdb.c.o
[  6%] Building CXX object src/checkpoints/CMakeFiles/obj_checkpoints.dir/checkpoints.cpp.o
-- The most recent tag was at fda88c8d
-- You are ahead of or behind a tagged release
[  6%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/aesb.c.o
[  7%] Building CXX object src/ringct/CMakeFiles/obj_ringct.dir/rctOps.cpp.o
[  8%] Building CXX object src/blockchain_db/CMakeFiles/obj_blockchain_db.dir/blockchain_db.cpp.o
[  9%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/account.cpp.o
Scanning dependencies of target blocks
[  9%] Built target genversion
[ 10%] Building CXX object src/common/CMakeFiles/obj_common.dir/base58.cpp.o
[ 11%] Building C object src/blocks/CMakeFiles/blocks.dir/blockexports.c.o
[ 12%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/blake256.c.o
[ 12%] Building CXX object src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/blockchain.cpp.o
[ 12%] Linking C static library libblocks.a
[ 13%] Building CXX object src/ringct/CMakeFiles/obj_ringct.dir/rctSigs.cpp.o
[ 14%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/chacha8.c.o
[ 14%] Built target blocks
[ 15%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/cryptonote_basic_impl.cpp.o
[ 16%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/crypto-ops-data.c.o
[ 17%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/crypto-ops.c.o
[ 17%] Building CXX object src/crypto/CMakeFiles/obj_cncrypto.dir/crypto.cpp.o
[ 18%] Building CXX object src/common/CMakeFiles/obj_common.dir/command_line.cpp.o
[ 19%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/groestl.c.o
[ 20%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash-extra-blake.c.o
[ 21%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash-extra-groestl.c.o
[ 21%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash-extra-jh.c.o
[ 22%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash-extra-skein.c.o
[ 23%] Building CXX object src/blockchain_db/CMakeFiles/obj_blockchain_db.dir/lmdb/db_lmdb.cpp.o
[ 24%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash.c.o
[ 25%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/jh.c.o
[ 26%] Linking C static library liblmdb.a
[ 27%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/keccak.c.o
[ 27%] Built target lmdb
[ 28%] Building CXX object src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/cryptonote_core.cpp.o
[ 28%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/oaes_lib.c.o
[ 29%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/random.c.o
[ 30%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/skein.c.o
[ 31%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/slow-hash.c.o
[ 31%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/tree-hash.c.o
[ 31%] Built target obj_cncrypto
[ 32%] Building CXX object src/ringct/CMakeFiles/obj_ringct.dir/rctTypes.cpp.o
[ 32%] Building C object src/ringct/CMakeFiles/obj_ringct.dir/rctCryptoOps.c.o
[ 32%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/cryptonote_format_utils.cpp.o
[ 33%] Linking CXX static library libeasylogging.a
[ 33%] Built target easylogging
[ 34%] Building CXX object src/common/CMakeFiles/obj_common.dir/dns_utils.cpp.o
[ 35%] Building CXX object src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/tx_pool.cpp.o
[ 36%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/difficulty.cpp.o
[ 37%] Building CXX object src/common/CMakeFiles/obj_common.dir/download.cpp.o
[ 38%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/hardfork.cpp.o
[ 39%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/miner.cpp.o
[ 40%] Building CXX object src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/cryptonote_tx_utils.cpp.o
[ 40%] Built target obj_ringct
[ 40%] Building CXX object src/common/CMakeFiles/obj_common.dir/util.cpp.o
[ 41%] Building CXX object src/common/CMakeFiles/obj_common.dir/i18n.cpp.o
[ 42%] Building CXX object src/common/CMakeFiles/obj_common.dir/password.cpp.o
[ 43%] Building CXX object src/common/CMakeFiles/obj_common.dir/perf_timer.cpp.o
[ 43%] Building CXX object src/common/CMakeFiles/obj_common.dir/threadpool.cpp.o
[ 43%] Built target obj_blockchain_db
[ 44%] Building CXX object src/common/CMakeFiles/obj_common.dir/updates.cpp.o
[ 44%] Built target obj_checkpoints
[ 45%] Building CXX object src/common/CMakeFiles/obj_common.dir/stack_trace.cpp.o
[ 45%] Built target obj_cryptonote_core
[ 45%] Built target obj_common
[ 45%] Built target obj_cryptonote_basic
make: *** [Makefile:141: all] Error 2
==> ERROR: A failure occurred in build().
    Aborting...
:: failed to build monero-git package(s)


# Action History
- Created by: will22 | 2016-11-17T00:52:38+00:00
- Closed at: 2017-09-19T23:36:21+00:00
