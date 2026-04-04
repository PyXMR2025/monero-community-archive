---
title: Impossible to send transaction with latest cli version
source_url: https://github.com/monero-project/monero/issues/3571
author: xmr-karnal
assignees: []
labels: []
created_at: '2018-04-06T15:45:56+00:00'
updated_at: '2018-06-25T22:41:01+00:00'
type: issue
status: closed
closed_at: '2018-06-25T22:41:01+00:00'
---

# Original Description
Was using a remote node and running into all sorts of (unfortunately, not saved) errors, and launched a local node. Synchronized after several hours.

But it still does not work, different error however:

> [wallet xxxxx]: transfer xxx yyy
> Wallet password: 
> Error: no connection to daemon. Please make sure daemon is running.

And yet..

> [wallet xxxx]: refresh
> Starting refresh...
> Refresh done, blocks received: 0                     

Re-attempting the transaction at this point yields the same error.

Clearly the daemon is running on localhost - it's there on tmux to see, and the refresh command does not complain of the daemon being absent.

But attempting a transaction invariably results in the claim that the daemon is not running.                                         


# Discussion History
## moneromooo-monero | 2018-04-06T17:21:58+00:00
Bump logs to 1 on daemon and wallet, and see what errors you get. Also make sure you're running 0.12.0.0 for both.

## xmr-karnal | 2018-04-06T18:02:01+00:00
I tried changing the logging level in both; no useful information logged.

I have a packet capture started before hitting return on the transfer command, and up to the transaction failing with the same error.

Not sure how much information pasting that here would reveal, but I'm going to guess quite some?

Could send you the encrypted log..

Only thing I could imagine is that I compiled the wallet myself (as always), or that this is somehow related to the ongoing difficulty adjustment situation, although I am inclined to believe that should that be the case, a lot more people would be complaining right now.

## moneromooo-monero | 2018-04-06T19:42:00+00:00
Then do two things:
- on the daemon side, use logs 1,perf:DEBUG
- on the wallet side, double check you're pointing to the right IP:port

perf:DEBUG will log every RPC called, so if it doesn't log anything, you're likely not actually querying the dameon in the first place.


## xmr-karnal | 2018-04-07T09:04:41+00:00
@moneromooo-monero:

Re wallet, of course it is the correct ip (localhost): the wallet connects and refreshes, but then come transfer time, after a timeout of many seconds, decides to conclude that there is no daemon connection.

Every single time.

Connections to localhost tearing down alone.. now that's a novel thing!

Re daemon, assuming what you asked was: set_log 1,perf:DEBUG - on the daemon, it produced the following, from right before hitting return on the transfer command, to right after the wallet failing with:

> Error: no connection to daemon. Please make sure daemon is running.

>  [RPC1]  DEBUG   perf    src/common/perf_timer.cpp:104   PERF             ----------
> [RPC1]  DEBUG   perf    src/common/perf_timer.cpp:128   PERF        5    on_get_version
> [RPC0]  DEBUG   perf    src/common/perf_timer.cpp:104   PERF             ----------
> [RPC0]  DEBUG   perf    src/common/perf_timer.cpp:128   PERF        0    on_get_height
>  [RPC1]  DEBUG   perf    src/common/perf_timer.cpp:104   PERF             ----------
> [RPC1]  DEBUG   perf    src/common/perf_timer.cpp:128   PERF      318    on_get_output_histogram
> [RPC0]  DEBUG   perf    src/common/perf_timer.cpp:128   PERF       10    on_get_version
> [RPC1]  DEBUG   perf    src/common/perf_timer.cpp:104   PERF             ----------
> [RPC1]  DEBUG   perf    src/common/perf_timer.cpp:128   PERF        1    on_get_blocks
>  [RPC1]  DEBUG   perf    src/common/perf_timer.cpp:104   PERF             ----------
> [RPC1]  DEBUG   perf    src/common/perf_timer.cpp:128   PERF        2    on_get_blocks
> [RPC0]  DEBUG   perf    src/common/perf_timer.cpp:104   PERF             ----------
> [RPC0]  DEBUG   perf    src/common/perf_timer.cpp:128   PERF        0    on_get_transaction_pool_hashes

This obvious discrepancy got me thinking, so here's a tcpdump on the loopback interface, in two stages:

After inputting password for transfer command, but before accepting the no payment ID:
> 00:00:00:00:00:00 > 00:00:00:00:00:00, ethertype IPv4 (0x0800), length 54: 127.0.0.1.18081 > 127.0.0.1.58950: Flags [.], ack 304, win 2789, length 0
> 00:00:00:00:00:00 > 00:00:00:00:00:00, ethertype IPv4 (0x0800), length 141: 127.0.0.1.58950 > 127.0.0.1.18081: Flags [P.], seq 304:391, ack 1116, win 25619, length 87
> 00:00:00:00:00:00 > 00:00:00:00:00:00, ethertype IPv4 (0x0800), length 54: 127.0.0.1.18081 > 127.0.0.1.58950: Flags [.], ack 391, win 2789, length 0
> 00:00:00:00:00:00 > 00:00:00:00:00:00, ethertype IPv4 (0x0800), length 214: 127.0.0.1.18081 > 127.0.0.1.58950: Flags [P.], seq 1116:1276, ack 391, win 2789, length 160
> 00:00:00:00:00:00 > 00:00:00:00:00:00, ethertype IPv4 (0x0800), length 181: 127.0.0.1.18081 > 127.0.0.1.58950: Flags [P.], seq 1276:1403, ack 391, win 2789, length 127
> 00:00:00:00:00:00 > 00:00:00:00:00:00, ethertype IPv4 (0x0800), length 54: 127.0.0.1.58950 > 127.0.0.1.18081: Flags [.], ack 1403, win 25616, length 0 

After accepting the payment id, up to the point where the wallet claims there is no daemon connection:


> 00:00:00:00:00:00 > 00:00:00:00:00:00, ethertype IPv4 (0x0800), length 164: 127.0.0.1.58950 > 127.0.0.1.18081: Flags [P.], seq 391:501, ack 1403, win 25619, length 110
> 00:00:00:00:00:00 > 00:00:00:00:00:00, ethertype IPv4 (0x0800), length 54: 127.0.0.1.18081 > 127.0.0.1.58950: Flags [.], ack 501, win 2789, length 0
> 00:00:00:00:00:00 > 00:00:00:00:00:00, ethertype IPv4 (0x0800), length 58: 127.0.0.1.58950 > 127.0.0.1.18081: Flags [P.], seq 501:505, ack 1403, win 25619, length 4 
> 00:00:00:00:00:00 > 00:00:00:00:00:00, ethertype IPv4 (0x0800), length 54: 127.0.0.1.18081 > 127.0.0.1.58950: Flags [.], ack 505, win 2789, length 0
> 00:00:00:00:00:00 > 00:00:00:00:00:00, ethertype IPv4 (0x0800), length 213: 127.0.0.1.18081 > 127.0.0.1.58950: Flags [P.], seq 1403:1562, ack 505, win 2789, length 159
> 00:00:00:00:00:00 > 00:00:00:00:00:00, ethertype IPv4 (0x0800), length 54: 127.0.0.1.58950 > 127.0.0.1.18081: Flags [.], ack 1562, win 25617, length 0 
> 00:00:00:00:00:00 > 00:00:00:00:00:00, ethertype IPv4 (0x0800), length 121: 127.0.0.1.18081 > 127.0.0.1.58950: Flags [P.], seq 1562:1629, ack 505, win 2789, length 67 
> 00:00:00:00:00:00 > 00:00:00:00:00:00, ethertype IPv4 (0x0800), length 54: 127.0.0.1.58950 > 127.0.0.1.18081: Flags [.], ack 1629, win 25616, length 0 
> 00:00:00:00:00:00 > 00:00:00:00:00:00, ethertype IPv4 (0x0800), length 165: 127.0.0.1.58950 > 127.0.0.1.18081: Flags [P.], seq 505:616, ack 1629, win 25619, length 111
> 00:00:00:00:00:00 > 00:00:00:00:00:00, ethertype IPv4 (0x0800), length 54: 127.0.0.1.18081 > 127.0.0.1.58950: Flags [.], ack 616, win 2789, length 0
> 00:00:00:00:00:00 > 00:00:00:00:00:00, ethertype IPv4 (0x0800), length 269: 127.0.0.1.58950 > 127.0.0.1.18081: Flags [P.], seq 616:831, ack 1629, win 25619, length 215
> 00:00:00:00:00:00 > 00:00:00:00:00:00, ethertype IPv4 (0x0800), length 54: 127.0.0.1.18081 > 127.0.0.1.58950: Flags [.], ack 831, win 2816, length 0
> 00:00:00:00:00:00 > 00:00:00:00:00:00, ethertype IPv4 (0x0800), length 214: 127.0.0.1.18081 > 127.0.0.1.58950: Flags [P.], seq 1629:1789, ack 831, win 2816, length 160
> 00:00:00:00:00:00 > 00:00:00:00:00:00, ethertype IPv4 (0x0800), length 54: 127.0.0.1.58950 > 127.0.0.1.18081: Flags [.], ack 1789, win 25617, length 0 
> 00:00:00:00:00:00 > 00:00:00:00:00:00, ethertype IPv4 (0x0800), length 314: 127.0.0.1.18081 > 127.0.0.1.58950: Flags [P.], seq 1789:2049, ack 831, win 2816, length 260
> 00:00:00:00:00:00 > 00:00:00:00:00:00, ethertype IPv4 (0x0800), length 54: 127.0.0.1.58950 > 127.0.0.1.18081: Flags [.], ack 2049, win 25613, length 0 
> 00:00:00:00:00:00 > 00:00:00:00:00:00, ethertype IPv4 (0x0800), length 165: 127.0.0.1.58950 > 127.0.0.1.18081: Flags [P.], seq 831:942, ack 2049, win 25619, length 111
> 00:00:00:00:00:00 > 00:00:00:00:00:00, ethertype IPv4 (0x0800), length 54: 127.0.0.1.18081 > 127.0.0.1.58950: Flags [.], ack 942, win 2816, length 0
> 00:00:00:00:00:00 > 00:00:00:00:00:00, ethertype IPv4 (0x0800), length 221: 127.0.0.1.58950 > 127.0.0.1.18081: Flags [P.], seq 942:1109, ack 2049, win 25619, length 167
> 00:00:00:00:00:00 > 00:00:00:00:00:00, ethertype IPv4 (0x0800), length 54: 127.0.0.1.18081 > 127.0.0.1.58950: Flags [.], ack 1109, win 2842, length 0
> 00:00:00:00:00:00 > 00:00:00:00:00:00, ethertype IPv4 (0x0800), length 208: 127.0.0.1.18081 > 127.0.0.1.58950: Flags [P.], seq 2049:2203, ack 1109, win 2842, length 154
> 00:00:00:00:00:00 > 00:00:00:00:00:00, ethertype IPv4 (0x0800), length 54: 127.0.0.1.58950 > 127.0.0.1.18081: Flags [.], ack 2203, win 25619, length 0 
> 00:00:00:00:00:00 > 00:00:00:00:00:00, ethertype IPv4 (0x0800), length 168: 127.0.0.1.18081 > 127.0.0.1.58950: Flags [P.], seq 2203:2317, ack 1109, win 2842, length 114
> 00:00:00:00:00:00 > 00:00:00:00:00:00, ethertype IPv4 (0x0800), length 54: 127.0.0.1.58950 > 127.0.0.1.18081: Flags [.], ack 2317, win 25618, length 0 
> 00:00:00:00:00:00 > 00:00:00:00:00:00, ethertype IPv4 (0x0800), length 164: 127.0.0.1.58950 > 127.0.0.1.18081: Flags [P.], seq 1109:1219, ack 2317, win 25619, length 110
> 00:00:00:00:00:00 > 00:00:00:00:00:00, ethertype IPv4 (0x0800), length 54: 127.0.0.1.18081 > 127.0.0.1.58950: Flags [.], ack 1219, win 2842, length 0
> 00:00:00:00:00:00 > 00:00:00:00:00:00, ethertype IPv4 (0x0800), length 138: 127.0.0.1.58950 > 127.0.0.1.18081: Flags [P.], seq 1219:1303, ack 2317, win 25619, length 84
> 00:00:00:00:00:00 > 00:00:00:00:00:00, ethertype IPv4 (0x0800), length 54: 127.0.0.1.18081 > 127.0.0.1.58950: Flags [.], ack 1303, win 2842, length 0
> 00:00:00:00:00:00 > 00:00:00:00:00:00, ethertype IPv4 (0x0800), length 214: 127.0.0.1.18081 > 127.0.0.1.58950: Flags [P.], seq 2317:2477, ack 1303, win 2842, length 160
> 00:00:00:00:00:00 > 00:00:00:00:00:00, ethertype IPv4 (0x0800), length 54: 127.0.0.1.58950 > 127.0.0.1.18081: Flags [.], ack 2477, win 25619, length 0 
> 00:00:00:00:00:00 > 00:00:00:00:00:00, ethertype IPv4 (0x0800), length 1009: 127.0.0.1.18081 > 127.0.0.1.58950: Flags [P.], seq 2477:3432, ack 1303, win 2842, length 955
> 00:00:00:00:00:00 > 00:00:00:00:00:00, ethertype IPv4 (0x0800), length 54: 127.0.0.1.58950 > 127.0.0.1.18081: Flags [.], ack 3432, win 25605, length 0 

So there *is* a connection to the daemon, and to make matters worse, it's not even closed at the end (TCP level); the wallet's claim that there is no connection is not even true because due to some hiccup the TCP connection itself was teared down (by hypothetical accident) in the end.

What would you recommend as the next step? I could offer to send the data from the packet capture PGP-encrypted if you think that would help.

## moneromooo-monero | 2018-04-07T11:23:23+00:00
"No connection" for the wallet means "the other side did not return my data", not "there is no TCP connection". Next step is to take an all thread stack trace in monerod and monero-wallet-cli while this timeout is happening: gdb /path/to/binary pid-of-that-binary, then while in gdb: thread apply all bt.


## xmr-karnal | 2018-04-07T13:30:25+00:00
Hey, so this is a bit of new territory to me, hope the following helps.

I started monerod again, let it synchronize.
I started cli wallet, went through refresh, paste the transfer command, go through the no payment id prompt, wait about 1 second and as quickly as I could, switched tmux pane and run the gdb command.

![](https://s7.pixxxels.cc/yauv8osuz/monerod-debug.png)

**Daemon**:
```
(gdb) thread apply all bt                                                                                                                                                                                                            [160/372]

Thread 21 (Thread 0x7022ec533700 (LWP 3275)):
#0  0x0000703624607480 in pthread_cond_wait@@GLIBC_2.3.2 () from /lib64/libpthread.so.0
#1  0x00005c4985eaf677 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#2  0x00007036250d2146 in thread_proxy () from /lib64/libboost_thread.so.1.60.0
#3  0x000070362460173a in start_thread () from /lib64/libpthread.so.0
#4  0x000070362433be7f in clone () from /lib64/libc.so.6

Thread 20 (Thread 0x7022eca34700 (LWP 3274)):
#0  0x0000703624607480 in pthread_cond_wait@@GLIBC_2.3.2 () from /lib64/libpthread.so.0
#1  0x00005c4985eaf677 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#2  0x00007036250d2146 in thread_proxy () from /lib64/libboost_thread.so.1.60.0
#3  0x000070362460173a in start_thread () from /lib64/libpthread.so.0
#4  0x000070362433be7f in clone () from /lib64/libc.so.6

Thread 19 (Thread 0x7022ecf35700 (LWP 3273)):
#0  0x0000703624607480 in pthread_cond_wait@@GLIBC_2.3.2 () from /lib64/libpthread.so.0
#1  0x00005c4985eaf677 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#2  0x00007036250d2146 in thread_proxy () from /lib64/libboost_thread.so.1.60.0
#3  0x000070362460173a in start_thread () from /lib64/libpthread.so.0
---Type <return> to continue, or q <return> to quit---
#4  0x000070362433be7f in clone () from /lib64/libc.so.6

Thread 18 (Thread 0x70360c9f6700 (LWP 3272)):
#0  0x0000703624607480 in pthread_cond_wait@@GLIBC_2.3.2 () from /lib64/libpthread.so.0
#1  0x00005c4985eaf677 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#2  0x00007036250d2146 in thread_proxy () from /lib64/libboost_thread.so.1.60.0
#3  0x000070362460173a in start_thread () from /lib64/libpthread.so.0
#4  0x000070362433be7f in clone () from /lib64/libc.so.6

Thread 17 (Thread 0x70360cef7700 (LWP 3271)):
#0  0x0000703624607480 in pthread_cond_wait@@GLIBC_2.3.2 () from /lib64/libpthread.so.0
#1  0x00005c4985eaf677 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#2  0x00007036250d2146 in thread_proxy () from /lib64/libboost_thread.so.1.60.0
#3  0x000070362460173a in start_thread () from /lib64/libpthread.so.0
#4  0x000070362433be7f in clone () from /lib64/libc.so.6

Thread 16 (Thread 0x70360d3f8700 (LWP 3270)):
#0  0x0000703624607480 in pthread_cond_wait@@GLIBC_2.3.2 () from /lib64/libpthread.so.0
#1  0x00005c4985eaf677 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#2  0x00007036250d2146 in thread_proxy () from /lib64/libboost_thread.so.1.60.0
#3  0x000070362460173a in start_thread () from /lib64/libpthread.so.0
#4  0x000070362433be7f in clone () from /lib64/libc.so.6

Thread 15 (Thread 0x70360d8f9700 (LWP 3269)):
#0  0x0000703624607480 in pthread_cond_wait@@GLIBC_2.3.2 () from /lib64/libpthread.so.0
#1  0x00005c4985eaf677 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#2  0x00007036250d2146 in thread_proxy () from /lib64/libboost_thread.so.1.60.0
#3  0x000070362460173a in start_thread () from /lib64/libpthread.so.0
#4  0x000070362433be7f in clone () from /lib64/libc.so.6

Thread 14 (Thread 0x70360ddfa700 (LWP 3268)):
#0  0x0000703624607480 in pthread_cond_wait@@GLIBC_2.3.2 () from /lib64/libpthread.so.0
#1  0x00005c4985eaf677 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#2  0x00007036250d2146 in thread_proxy () from /lib64/libboost_thread.so.1.60.0
#3  0x000070362460173a in start_thread () from /lib64/libpthread.so.0
#4  0x000070362433be7f in clone () from /lib64/libc.so.6

Thread 13 (Thread 0x70360e2fb700 (LWP 3267)):
#0  0x0000703624607480 in pthread_cond_wait@@GLIBC_2.3.2 () from /lib64/libpthread.so.0                                                                                                                                              [100/372]
#1  0x00005c4985eaf677 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#2  0x00007036250d2146 in thread_proxy () from /lib64/libboost_thread.so.1.60.0
#3  0x000070362460173a in start_thread () from /lib64/libpthread.so.0
#4  0x000070362433be7f in clone () from /lib64/libc.so.6

Thread 12 (Thread 0x70360e7fc700 (LWP 3266)):
#0  0x000070362433c473 in epoll_wait () from /lib64/libc.so.6
#1  0x00005c4985eaf228 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#2  0x00007036250d2146 in thread_proxy () from /lib64/libboost_thread.so.1.60.0
#3  0x000070362460173a in start_thread () from /lib64/libpthread.so.0
#4  0x000070362433be7f in clone () from /lib64/libc.so.6

Thread 11 (Thread 0x70360effd700 (LWP 3265)):
#0  0x0000703624607829 in pthread_cond_timedwait@@GLIBC_2.3.2 () from /lib64/libpthread.so.0
#1  0x00007036250d3f71 in boost::this_thread::hiden::sleep_for(timespec const&) () from /lib64/libboost_thread.so.1.60.0
#2  0x00005c4985ea05b0 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::run()::{lambda()#1}::operator()() const ()
#3  0x00007036250d2146 in thread_proxy () from /lib64/libboost_thread.so.1.60.0
#4  0x000070362460173a in start_thread () from /lib64/libpthread.so.0
#5  0x000070362433be7f in clone () from /lib64/libc.so.6

Thread 10 (Thread 0x70360f7fe700 (LWP 3264)):
---Type <return> to continue, or q <return> to quit---
#0  0x000070362432ff3d in poll () from /lib64/libc.so.6
#1  0x0000703626816d8a in zmq::signaler_t::wait(int) () from /lib64/libzmq.so.5
#2  0x00007036267fbcf6 in zmq::mailbox_t::recv(zmq::command_t*, int) () from /lib64/libzmq.so.5
#3  0x000070362681817a in zmq::socket_base_t::process_commands(int, bool) () from /lib64/libzmq.so.5
#4  0x00007036268188fb in zmq::socket_base_t::recv(zmq::msg_t*, int) () from /lib64/libzmq.so.5
#5  0x000070362682f049 in s_recvmsg(zmq::socket_base_t*, zmq_msg_t*, int) () from /lib64/libzmq.so.5
#6  0x00005c4985ff5647 in cryptonote::rpc::ZmqServer::serve() ()
#7  0x00007036250d2146 in thread_proxy () from /lib64/libboost_thread.so.1.60.0
#8  0x000070362460173a in start_thread () from /lib64/libpthread.so.0
#9  0x000070362433be7f in clone () from /lib64/libc.so.6

Thread 9 (Thread 0x70360ffff700 (LWP 3263)):
#0  0x000070362433c473 in epoll_wait () from /lib64/libc.so.6
#1  0x00007036267f537a in zmq::epoll_t::loop() () from /lib64/libzmq.so.5
#2  0x0000703626829e8d in thread_routine () from /lib64/libzmq.so.5
#3  0x000070362460173a in start_thread () from /lib64/libpthread.so.0
#4  0x000070362433be7f in clone () from /lib64/libc.so.6

Thread 8 (Thread 0x70361ca32700 (LWP 3262)):
#0  0x000070362433c473 in epoll_wait () from /lib64/libc.so.6
#1  0x00007036267f537a in zmq::epoll_t::loop() () from /lib64/libzmq.so.5
#2  0x0000703626829e8d in thread_routine () from /lib64/libzmq.so.5
#3  0x000070362460173a in start_thread () from /lib64/libpthread.so.0
#4  0x000070362433be7f in clone () from /lib64/libc.so.6

Thread 7 (Thread 0x70361e648700 (LWP 3261)):                                                                                                                                                                                          [52/372]
#0  0x0000703624607480 in pthread_cond_wait@@GLIBC_2.3.2 () from /lib64/libpthread.so.0
#1  0x00005c4985cc98e3 in bool epee::async_console_handler::run<bool epee::async_console_handler::run<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::__cxx11::basic_string<char, std::char_traits<char>, std::all
ocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > > >(boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::__cxx11::basic_string<char, std::char_traits<char
>, std::allocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > >, std::function<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > ()>, std::__cxx11::ba
sic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()>)::{lambda(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)#1}>(std::function<std::__cxx11::basic_string<
char, std::char_traits<char>, std::allocator<char> > ()>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, bool epee::async_console_handler::run<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::
command_handler, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > > >(boost::_bi::bind_t<bool, boost::_mfi::mf1<b
ool, epee::command_handler, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > >, std::function<std::__cxx11::basic
_string<char, std::char_traits<char>, std::allocator<char> > ()>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()>)::{lambda(std::__cxx11::basic_string<char, std::char_traits<c
har>, std::allocator<char> > const&)#1} const&, std::function<void ()>) ()
#2  0x00005c4985cca65e in epee::console_handlers_binder::run_handling(std::function<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > ()>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocat
or<char> > const&, std::function<void ()>) ()
#3  0x00005c4985cc5d7f in boost::detail::thread_data<boost::_bi::bind_t<bool, boost::_mfi::mf3<bool, epee::console_handlers_binder, std::function<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > ()>, std::__
cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()> >, boost::_bi::list4<boost::_bi::value<epee::console_handlers_binder*>, boost::_bi::value<std::function<std::__cxx11::basic_string<cha
r, std::char_traits<char>, std::allocator<char> > ()> >, boost::_bi::value<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, boost::_bi::value<std::function<void ()> > > > >::run() ()
#4  0x00007036250d2146 in thread_proxy () from /lib64/libboost_thread.so.1.60.0
#5  0x000070362460173a in start_thread () from /lib64/libpthread.so.0
#6  0x000070362433be7f in clone () from /lib64/libc.so.6

Thread 6 (Thread 0x70361ee49700 (LWP 3260)):
#0  0x0000703624331c93 in select () from /lib64/libc.so.6
#1  0x00005c4985cc8772 in epee::async_stdin_reader::reader_thread_func() ()
#2  0x00007036250d2146 in thread_proxy () from /lib64/libboost_thread.so.1.60.0
#3  0x000070362460173a in start_thread () from /lib64/libpthread.so.0
#4  0x000070362433be7f in clone () from /lib64/libc.so.6

Thread 5 (Thread 0x70361f64a700 (LWP 3259)):
#0  0x00005c498604ccb4 in mdb_page_search_root ()
#1  0x00005c498604ce4b in mdb_page_search ()
#2  0x00005c498604edd5 in mdb_cursor_set ()
#3  0x00005c498604f13e in mdb_cursor_set ()
#4  0x00005c498604bdd8 in mdb_cursor_get ()
#5  0x00005c4985f182dd in cryptonote::BlockchainLMDB::get_tx_block_height(crypto::hash const&) const ()
#6  0x00005c4985f3203b in cryptonote::BlockchainLMDB::get_output_histogram(std::vector<unsigned long, std::allocator<unsigned long> > const&, bool, unsigned long) const ()
---Type <return> to continue, or q <return> to quit---
#7  0x00005c4985f3bfd7 in cryptonote::Blockchain::get_output_histogram(std::vector<unsigned long, std::allocator<unsigned long> > const&, bool, unsigned long) const ()
#8  0x00005c4985e223b6 in cryptonote::core_rpc_server::on_get_output_histogram(cryptonote::COMMAND_RPC_GET_OUTPUT_HISTOGRAM::request const&, cryptonote::COMMAND_RPC_GET_OUTPUT_HISTOGRAM::response&, epee::json_rpc::error&) ()
#9  0x00005c4985d7e7cb in bool cryptonote::core_rpc_server::handle_http_request_map<epee::net_utils::connection_context_base>(epee::net_utils::http::http_request_info const&, epee::net_utils::http::http_response_info&, epee::net_utils::co
nnection_context_base&) ()
#10 0x00005c4985d837e9 in cryptonote::core_rpc_server::handle_http_request(epee::net_utils::http::http_request_info const&, epee::net_utils::http::http_response_info&, epee::net_utils::connection_context_base&) ()
#11 0x00005c4985d4eded in epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base>::handle_request(epee::net_utils::http::http_request_info const&, epee::net_utils::http::http_response_info&) ()
#12 0x00005c4985d1006e in epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_request_and_send_response(epee::net_utils::http::http_request_info const&) ()
#13 0x00005c4985d10456 in epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_retriving_query_body() ()
#14 0x00005c4985d87ff8 in epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_buff_in(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&) ()
#15 0x00005c4985d8849d in epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_recv(void const*, unsigned long) ()
#16 0x00005c4985d887b8 in epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::handle_read(boost::system::error_code const&, unsigned long) ()
#17 0x00005c4985d439ca in void boost::asio::detail::strand_service::dispatch<boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_uti
ls::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_con
text_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long> >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, ep
ee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::con
nection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long>&) ()
#18 0x00005c4985d43d58 in boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_m
fi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee
::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, 
unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_
bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(boost::asio
::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#19 0x00005c4985d441d6 in void boost::asio::detail::strand_service::dispatch<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void
, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shar
ed_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::e
rror_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long
>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >(boost::asio::
detail::strand_service::strand_impl*&, boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_uti
ls::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epe
e::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi:
:bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value
<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > >&) ()
#20 0x00005c4985d444f0 in boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::
connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::n
et_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(boost::asio::detail::task_io_service*, boost
::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#21 0x00005c4985cdcbfc in boost::asio::detail::epoll_reactor::descriptor_state::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#22 0x00005c4985cf2ff2 in epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::worker_thread() ()
#23 0x00007036250d2146 in thread_proxy () from /lib64/libboost_thread.so.1.60.0
#24 0x000070362460173a in start_thread () from /lib64/libpthread.so.0
#25 0x000070362433be7f in clone () from /lib64/libc.so.6

Thread 4 (Thread 0x70361d445700 (LWP 3258)):
#0  0x000070362433c473 in epoll_wait () from /lib64/libc.so.6
#1  0x00005c4985cf2b19 in epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::worker_thread() ()
#2  0x00007036250d2146 in thread_proxy () from /lib64/libboost_thread.so.1.60.0
#3  0x000070362460173a in start_thread () from /lib64/libpthread.so.0
#4  0x000070362433be7f in clone () from /lib64/libc.so.6

Thread 3 (Thread 0x70361de47700 (LWP 3253)):
#0  0x0000703624607480 in pthread_cond_wait@@GLIBC_2.3.2 () from /lib64/libpthread.so.0
#1  0x00005c4985f692f8 in boost::asio::io_service::run() ()
#2  0x00007036250d2146 in thread_proxy () from /lib64/libboost_thread.so.1.60.0
#3  0x000070362460173a in start_thread () from /lib64/libpthread.so.0
#4  0x000070362433be7f in clone () from /lib64/libc.so.6

Thread 2 (Thread 0x70361fb4b700 (LWP 3209)):
#0  0x0000703624607480 in pthread_cond_wait@@GLIBC_2.3.2 () from /lib64/libpthread.so.0
#1  0x00005c4985fdcc63 in tools::threadpool::run() ()
#2  0x00007036250d2146 in thread_proxy () from /lib64/libboost_thread.so.1.60.0
---Type <return> to continue, or q <return> to quit---
#3  0x000070362460173a in start_thread () from /lib64/libpthread.so.0
#4  0x000070362433be7f in clone () from /lib64/libc.so.6

Thread 1 (Thread 0x703627bdfd00 (LWP 3208)):
#0  0x0000703624607480 in pthread_cond_wait@@GLIBC_2.3.2 () from /lib64/libpthread.so.0
#1  0x00007036250d4dc3 in boost::thread::join_noexcept() () from /lib64/libboost_thread.so.1.60.0
#2  0x00005c4985ef210e in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::run_server(unsigned long, bool, boost::thread_attributes 
const&) ()
#3  0x00005c4985ef3b12 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::run() ()
#4  0x00005c4985cdf974 in daemonize::t_p2p::run() ()
#5  0x00005c4985cd66d8 in daemonize::t_daemon::run(bool) ()
#6  0x00005c4985d8980e in daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) ()
#7  0x00005c4985d907fe in bool daemonizer::daemonize<daemonize::t_executor>(int, char const**, daemonize::t_executor&&, boost::program_options::variables_map const&) ()
#8  0x00005c4985ca7c4d in main ()
(gdb) 

```

**Wallet**:

```
(gdb) thread apply all bt                                                                                                                                                                                                              [2/140]

Thread 4 (Thread 0x74e771d40700 (LWP 3411)):
#0  0x000074e77e552829 in pthread_cond_timedwait@@GLIBC_2.3.2 () from /lib64/libpthread.so.0
#1  0x00005ecf8fd60532 in cryptonote::simple_wallet::wallet_idle_thread() ()
#2  0x000074e780599146 in thread_proxy () from /lib64/libboost_thread.so.1.60.0
#3  0x000074e77e54c73a in start_thread () from /lib64/libpthread.so.0
#4  0x000074e77e286e7f in clone () from /lib64/libc.so.6

Thread 3 (Thread 0x74e772241700 (LWP 3320)):
#0  0x000074e77e552480 in pthread_cond_wait@@GLIBC_2.3.2 () from /lib64/libpthread.so.0
#1  0x00005ecf8ffeaf83 in tools::threadpool::run() ()
#2  0x000074e780599146 in thread_proxy () from /lib64/libboost_thread.so.1.60.0
#3  0x000074e77e54c73a in start_thread () from /lib64/libpthread.so.0
#4  0x000074e77e286e7f in clone () from /lib64/libc.so.6

Thread 2 (Thread 0x74e773144700 (LWP 3319)):
#0  0x000074e77e552480 in pthread_cond_wait@@GLIBC_2.3.2 () from /lib64/libpthread.so.0
#1  0x00005ecf8fda31f3 in epee::async_stdin_reader::reader_thread_func() ()
#2  0x000074e780599146 in thread_proxy () from /lib64/libboost_thread.so.1.60.0
#3  0x000074e77e54c73a in start_thread () from /lib64/libpthread.so.0
#4  0x000074e77e286e7f in clone () from /lib64/libc.so.6

Thread 1 (Thread 0x74e7814380c0 (LWP 3318)):
#0  0x000074e77e287473 in epoll_wait () from /lib64/libc.so.6
#1  0x00005ecf8fdd0dc1 in epee::net_utils::blocked_mode_client::recv(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, std::chrono::duration<long, std::ratio<1l, 1000l> >) ()
#2  0x00005ecf8fe21ea5 in epee::net_utils::http::http_simple_client_template<epee::net_utils::blocked_mode_client>::handle_reciev(std::chrono::duration<long, std::ratio<1l, 1000l> >) ()
---Type <return> to continue, or q <return> to quit---
#3  0x00005ecf8fe2312f in epee::net_utils::http::http_simple_client_template<epee::net_utils::blocked_mode_client>::invoke(boost::basic_string_ref<char, std::char_traits<char> >, boost::basic_string_ref<char, std::char_traits<char> >, st$::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::chrono::duration<long, std::ratio<1l, 1000l> >, epee::net_utils::http::http_response_info const**, std::__cxx11::list<std::pair<std::__cxx11::basic$string<char, std::char_traits<char>, std::allocator<char> >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::alloca$or<char> >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > > const&) ()
#4  0x00005ecf8ff700d1 in bool epee::net_utils::invoke_http_json<epee::json_rpc::request<cryptonote::COMMAND_RPC_GET_OUTPUT_HISTOGRAM::request>, epee::json_rpc::response<cryptonote::COMMAND_RPC_GET_OUTPUT_HISTOGRAM::response, epee::json_$pc::error>, epee::net_utils::http::http_simple_client_template<epee::net_utils::blocked_mode_client> >(boost::basic_string_ref<char, std::char_traits<char> >, epee::json_rpc::request<cryptonote::COMMAND_RPC_GET_OUTPUT_HISTOGRAM::request> const&, epee::json_rpc::response<cryptonote::COMMAND_RPC_GET_OUTPUT_HISTOGRAM::response, epee::json_rpc::error>&, epee::net_utils::http::http_simple_client_template<epee::net_utils::blocked_mode_client>&, std::chrono::duration<long, std:$ratio<1l, 1000l> >, boost::basic_string_ref<char, std::char_traits<char> >) ()
#5  0x00005ecf8ff70c88 in bool epee::net_utils::invoke_http_json_rpc<cryptonote::COMMAND_RPC_GET_OUTPUT_HISTOGRAM::request, cryptonote::COMMAND_RPC_GET_OUTPUT_HISTOGRAM::response, epee::net_utils::http::http_simple_client_template<epee::$et_utils::blocked_mode_client> >(boost::basic_string_ref<char, std::char_traits<char> >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, cryptonote::COMMAND_RPC_GET_OUTPUT_HISTOGRAM::request const&, crypt$note::COMMAND_RPC_GET_OUTPUT_HISTOGRAM::response&, epee::net_utils::http::http_simple_client_template<epee::net_utils::blocked_mode_client>&, std::chrono::duration<long, std::ratio<1l, 1000l> >, boost::basic_string_ref<char, std::char_tr$its<char> >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) ()
#6  0x00005ecf8fe91cf0 in tools::wallet2::get_outs(std::vector<std::vector<std::tuple<unsigned long, crypto::public_key, rct::key>, std::allocator<std::tuple<unsigned long, crypto::public_key, rct::key> > >, std::allocator<std::vector<st$::tuple<unsigned long, crypto::public_key, rct::key>, std::allocator<std::tuple<unsigned long, crypto::public_key, rct::key> > > > >&, std::vector<unsigned long, std::allocator<unsigned long> > const&, unsigned long) ()
#7  0x00005ecf8fec727a in tools::wallet2::transfer_selected_rct(std::vector<cryptonote::tx_destination_entry, std::allocator<cryptonote::tx_destination_entry> >, std::vector<unsigned long, std::allocator<unsigned long> > const&, unsigned long, std::vector<std::vector<std::tuple<unsigned long, crypto::public_key, rct::key>, std::allocator<std::tuple<unsigned long, crypto::public_key, rct::key> > >, std::allocator<std::vector<std::tuple<unsigned long, crypto::public_key, r$t::key>, std::allocator<std::tuple<unsigned long, crypto::public_key, rct::key> > > > >&, unsigned long, unsigned long, std::vector<unsigned char, std::allocator<unsigned char> > const&, cryptonote::transaction&, tools::wallet2::pending_tx&, bool) ()
#8  0x00005ecf8fecd208 in tools::wallet2::create_transactions_2(std::vector<cryptonote::tx_destination_entry, std::allocator<cryptonote::tx_destination_entry> >, unsigned long, unsigned long, unsigned int, std::vector<unsigned char, std::
allocator<unsigned char> > const&, unsigned int, std::set<unsigned int, std::less<unsigned int>, std::allocator<unsigned int> >, bool) ()
#9  0x00005ecf8fd80f01 in cryptonote::simple_wallet::transfer_main(int, std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, s
td::allocator<char> > > > const&) ()
#10 0x00005ecf8fddb9cd in epee::command_handler::process_command_str(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) ()
#11 0x00005ecf8fdb2e50 in bool epee::async_console_handler::run<bool epee::async_console_handler::run<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::__cxx11::basic_string<char, std::char_traits<char>, std::all
ocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > > >(boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::__cxx11::basic_string<char, std::char_traits<char
>, std::allocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > >, std::function<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > ()>, std::__cxx11::ba
sic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()>)::{lambda(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)#1}>(std::function<std::__cxx11::basic_string<
char, std::char_traits<char>, std::allocator<char> > ()>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, bool epee::async_console_handler::run<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::
command_handler, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > > >(boost::_bi::bind_t<bool, boost::_mfi::mf1<b
ool, epee::command_handler, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > >, std::function<std::__cxx11::basic
_string<char, std::char_traits<char>, std::allocator<char> > ()>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()>)::{lambda(std::__cxx11::basic_string<char, std::char_traits<c
har>, std::allocator<char> > const&)#1} const&, std::function<void ()>) ()
#12 0x00005ecf8fd68b28 in cryptonote::simple_wallet::run() ()
#13 0x00005ecf8fd32061 in main ()
```

## moneromooo-monero | 2018-04-07T13:40:16+00:00
The wallet is getting an output histogram, and the daemon is gathering it.
Try adding --trusted-daemon. It should be default, but you never know, this code changed recently.


## moneromooo-monero | 2018-04-07T13:42:09+00:00
Or bump the timeout in src/wallet/wallet2.cpp:5871:

    bool r = net_utils::invoke_http_json_rpc("/json_rpc", "get_output_histogram", req_t, resp_t, m_http_client, rpc_timeout);

Set this to rpc_timeout * 1000 or the like.

## xmr-karnal | 2018-04-07T15:19:32+00:00
Followed your suggestion; Below is the result:


```
diff --git a/src/wallet/wallet2.cpp b/src/wallet/wallet2.cpp
index 4b7e6dd..260d354 100644
--- a/src/wallet/wallet2.cpp
+++ b/src/wallet/wallet2.cpp
@@ -8036,7 +8036,7 @@ std::vector<size_t> wallet2::select_available_outputs_from_histogram(uint64_t co
   req_t.min_count = count;
   req_t.max_count = 0;
   req_t.unlocked = unlocked;
-  bool r = net_utils::invoke_http_json_rpc("/json_rpc", "get_output_histogram", req_t, resp_t, m_http_client, rpc_timeout);
+  bool r = net_utils::invoke_http_json_rpc("/json_rpc", "get_output_histogram", req_t, resp_t, m_http_client, rpc_timeout * 1000);
   m_daemon_rpc_mutex.unlock();
   THROW_WALLET_EXCEPTION_IF(!r, error::no_connection_to_daemon, "select_available_outputs_from_histogram");
   THROW_WALLET_EXCEPTION_IF(resp_t.status == CORE_RPC_STATUS_BUSY, error::daemon_busy, "get_output_histogram");
```

```
monero-wallet-cli --log-file /dev/null --wallet-file pathToWalletDataDir/myWallet --daemon-address=127.0.0.1:18081 --trusted-daemon

monerod --restricted-rpc --rpc-bind-port 18081 --rpc-bind-ip 127.0.0.1
```

Still the same:

> Error: no connection to daemon. Please make sure daemon is running.


## moneromooo-monero | 2018-04-07T15:44:39+00:00
And it timed out after... a lot of time ?

## xmr-karnal | 2018-04-07T18:58:35+00:00
Didn't check, left it to run while tending to other stuff.

Should I repeat the test and pay attention to the timeout this time?

I will try in a bit the following to try to eliminate some possibilities:

* Use my locally-compiled binary with a couple of different wallets (I've been attempting the same transaction on the same wallet this whole time) to eliminate the possibility of it being some obscure bug that's manifesting with my particular wallet state.

* Download the official cli wallet and attempt the same transfer, see if the same thing happens - that should eliminate some weirdness from using ccache or not updating a submodule or god knows what else.

Sounds like a plan?

## moneromooo-monero | 2018-04-07T19:19:29+00:00
The timestamps in the wallet log should reflect the timeout delay.

Let's get some more info: start the wallet with --log-level 2, then paste the log from the last line with "transfer: starting with fee " to end. Either on github, or paste.debian.net or fpaste.org.

## xmr-karnal | 2018-04-08T10:32:29+00:00
Afraid my wallet log file is /dev/null.

I'll try to have a look at this tonight or tomorrow again, presently a bit strapped for time. Hope we can get to the bottom of it, but I think it must be something very specific, or dozens of others would be complaining, no?

## moneromooo-monero | 2018-04-09T11:19:31+00:00
Try with 3550 and 3574.

## Haafingar | 2018-04-12T05:10:39+00:00
Tested with 3550, 3574 and 3584 

Still reports that it can't connect to the daemon upon using the `transfer` command

## Haafingar | 2018-04-12T06:31:56+00:00
Will do, also new error message `Error: transaction cancelled.` has started showing up too

## moneromooo-monero | 2018-04-12T07:53:42+00:00
> Tested with 3550, 3574 and 3584
> 
> Still reports that it can't connect to the daemon upon using the transfer command

I need actual messages, please, from wallet and daemon (level 2 log preferably).


## kingsley22 | 2018-04-12T19:09:56+00:00
I reduced the TESTNET_SEGREGATION_FORK_HEIGHT closer to the actual block height.

Don't know what other ramifications it might have however.

## Haafingar | 2018-04-13T02:06:06+00:00
Latest master pull seems to be working

## moneromooo-monero | 2018-06-25T22:01:02+00:00
+resolved

# Action History
- Created by: xmr-karnal | 2018-04-06T15:45:56+00:00
- Closed at: 2018-06-25T22:41:01+00:00
