---
title: possible error with priority node connection
source_url: https://github.com/monero-project/monero/issues/9068
author: Gingeropolous
assignees: []
labels: []
created_at: '2023-11-15T02:57:10+00:00'
updated_at: '2023-11-26T23:01:45+00:00'
type: issue
status: closed
closed_at: '2023-11-25T15:17:12+00:00'
---

# Original Description
So I try to connect my node A to the xmrchain node B as a priority node. 

```
bitmonero.log-2023-11-12-16-40-40-2023-11-12 15:52:05.461	[P2P6]	INFO	net.p2p	src/p2p/net_node.inl:2675	[176.9.0.187:18080 3738d72d-86df-4722-8017-0e5badb645b2 OUT] NEW CONNECTION
bitmonero.log-2023-11-12-16-40-40-2023-11-12 15:52:05.461	[P2P6]	INFO	net.p2p.traffic	contrib/epee/include/net/levin_protocol_handler_async.h:57	[176.9.0.187:18080 OUT] 274 bytes sent for category command-1001 initiated by us
bitmonero.log-2023-11-12-16-40-40-2023-11-12 15:52:05.567	[P2P8]	INFO	net	contrib/epee/include/storages/levin_abstract_invoke2.h:74	Failed to invoke command 1001 return code -3
bitmonero.log-2023-11-12-16-40-40-2023-11-12 15:52:05.567	[P2P8]	WARNING	net.p2p	src/p2p/net_node.inl:1160	[176.9.0.187:18080 OUT] COMMAND_HANDSHAKE invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
bitmonero.log-2023-11-12-16-40-40-2023-11-12 15:52:05.568	[P2P6]	WARNING	net.p2p	src/p2p/net_node.inl:1219	[176.9.0.187:18080 OUT] COMMAND_HANDSHAKE Failed
bitmonero.log-2023-11-12-16-40-40-2023-11-12 15:52:05.568	[P2P6]	INFO	net.p2p	src/p2p/net_node.inl:1412	[176.9.0.187:18080 OUT] [priority]Failed to HANDSHAKE with peer 176.9.0.187:18080
bitmonero.log-2023-11-12-16-40-40:2023-11-12 15:52:05.568	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: boost::exception_detail::clone_impl<boost::exception_detail::error_info_injector<boost::bad_weak_ptr> >
bitmonero.log-2023-11-12-16-40-40-2023-11-12 15:52:05.568	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
bitmonero.log-2023-11-12-16-40-40-2023-11-12 15:52:05.568	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0x107) [0x562d78f40ed7]:__cxa_throw+0x107) [0x562d78f40ed7]
bitmonero.log-2023-11-12-16-40-40-2023-11-12 15:52:05.568	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] /bin/monerod(+0xbeffc) [0x562d78b1fffc] 
bitmonero.log-2023-11-12-16-40-40-2023-11-12 15:52:05.568	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3] /bin/monerod(+0x3507d7) [0x562d78db17d7] 
bitmonero.log-2023-11-12-16-40-40-2023-11-12 15:52:05.568	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4] /bin/monerod(+0x363f84) [0x562d78dc4f84] 
bitmonero.log-2023-11-12-16-40-40-2023-11-12 15:52:05.568	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5] /bin/monerod(+0x37358b) [0x562d78dd458b] 
bitmonero.log-2023-11-12-16-40-40-2023-11-12 15:52:05.568	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6] /bin/monerod(+0x3736c9) [0x562d78dd46c9] 
bitmonero.log-2023-11-12-16-40-40-2023-11-12 15:52:05.568	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7] /bin/monerod(+0x3d6a1f) [0x562d78e37a1f] 
bitmonero.log-2023-11-12-16-40-40-2023-11-12 15:52:05.568	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8] /bin/monerod(+0x34ed63) [0x562d78dafd63] 
bitmonero.log-2023-11-12-16-40-40-2023-11-12 15:52:05.568	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9] /bin/monerod(+0x3816f9) [0x562d78de26f9] 
bitmonero.log-2023-11-12-16-40-40-2023-11-12 15:52:05.568	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10] /bin/monerod(+0x3506a5) [0x562d78db16a5] 
bitmonero.log-2023-11-12-16-40-40-2023-11-12 15:52:05.568	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11] /bin/monerod(+0xc0986) [0x562d78b21986] 
bitmonero.log-2023-11-12-16-40-40-2023-11-12 15:52:05.568	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12] /bin/monerod(+0x36fb01) [0x562d78dd0b01] 
bitmonero.log-2023-11-12-16-40-40-2023-11-12 15:52:05.568	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [13]  0x11bcd) [0x7f2efe96dbcd]:_64-linux-gnu/libboost_thread.so.1.65.1(+0x11bcd) [0x7f2efe96dbcd]
bitmonero.log-2023-11-12-16-40-40-2023-11-12 15:52:05.568	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [14]  0x76db) [0x7f2efd8dd6db]:_64-linux-gnu/libpthread.so.0(+0x76db) [0x7f2efd8dd6db]
bitmonero.log-2023-11-12-16-40-40-2023-11-12 15:52:05.568	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [15]  0x3f) [0x7f2efd60661f]:_64-linux-gnu/libc.so.6(clone+0x3f) [0x7f2efd60661f]
bitmonero.log-2023-11-12-16-40-40-2023-11-12 15:52:05.568	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	
bitmonero.log-2023-11-12-16-40-40-2023-11-12 15:52:05.568	[P2P6]	ERROR	net	contrib/epee/include/net/levin_protocol_handler_async.h:340	[176.9.0.187:18080 OUT] [levin_protocol] -->> start_outer_call failed
bitmonero.log-2023-11-12-16-40-40-2023-11-12 15:52:05.569	[P2P8]	INFO	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2953	[176.9.0.187:18080 OUT] [0] state: closed in state before_handshake
bitmonero.log-2023-11-12-16-40-40-2023-11-12 15:52:05.570	[P2P8]	INFO	net.p2p	src/p2p/net_node.inl:2694	[176.9.0.187:18080 3738d72d-86df-4722-8017-0e5badb645b2 OUT] CLOSE CONNECTION
--
```

It turns out I also have the xmrchain node B set to connect to A as a priority node, because node A has xmrchain as an INC connection

```
user@user-ProLiant-DL325-Gen10:~/.bitmonero$ monerod --rpc-bind-port 12345 print_cn | grep 176.9.0.187
INC 176.9.0.187:50792        IPv4 
```

probably nothing, but i don't understand why its throwing the stacktrace thing. I thought that was for when things are borkt. 

though if you run two nodes, it would make sense to have them set to make each other a priority to connect to. But I guess you only need to tell one of them to make it a priority? 

# Discussion History
## vtnerd | 2023-11-15T17:05:28+00:00
This is identical to #8132 . I think my PR #7345 could fix the issue, but I have not heard back from the reporter in the other thread (and I have not seen this on my local node). Listing it as a priority node should be a red herring, but cannot say for certain until the problem is found.

## Gingeropolous | 2023-11-16T00:50:10+00:00
aight, running #7345 . i'll check the logs in a day to see if they are full of those stacktrace 

## Gingeropolous | 2023-11-17T22:39:41+00:00
looking good so far

Wednesday?
user@user-ProLiant-DL325-Gen10:~/.bitmonero$ grep stacktrace bitmonero.log* | wc -l
6106

Thu Nov 16 15:54:05 EST 2023
user@user-ProLiant-DL325-Gen10:~/.bitmonero$ grep stacktrace bitmonero.log* | wc -l
5143

Fri Nov 17 06:08:20 EST 2023
user@user-ProLiant-DL325-Gen10:~/.bitmonero$ grep stacktrace bitmonero.log* | wc -l
3767

Fri Nov 17 17:24:03 EST 2023
user@user-ProLiant-DL325-Gen10:~/.bitmonero$ grep stacktrace bitmonero.log* | wc -l
2376


## Gingeropolous | 2023-11-19T13:17:24+00:00
Sat Nov 18 06:57:30 EST 2023
user@user-ProLiant-DL325-Gen10:~/.bitmonero$ grep stacktrace bitmonero.log* | wc -l
1272

Sun Nov 19 08:10:57 EST 2023
user@user-ProLiant-DL325-Gen10:~/.bitmonero$ grep stacktrace bitmonero.log* | wc -l
202

Running the same command on the xmrchain box:
xmrchain@Ubuntu-1804-bionic-64-minimal:~/.bitmonero$ grep stacktrace bitmonero.log* | wc -l
213102

uptime for my local box
uptime 3d 12h 27m 53s

I'll give this a week for stability, and then test it on xmrchain

## Gingeropolous | 2023-11-19T13:22:24+00:00
Of course i realize now i should be grepping for weak_ptr

xmrchain@Ubuntu-1804-bionic-64-minimal:~/.bitmonero$ grep weak_ptr bitmonero.log* | wc -l
9055

user@user-ProLiant-DL325-Gen10:~/.bitmonero$ grep weak_ptr bitmonero.log* | wc -l
9

and the ones on proliant are all from 11/16, which was before I added this PR. 

## vtnerd | 2023-11-20T17:31:40+00:00
@Gingeropolous so does this appear to help? Because the grep is still returning results (old logs?).

## Gingeropolous | 2023-11-21T02:31:53+00:00
yeah, its old logs. It looks like its helping the situation. 

yep, currently there are 0 instances

Mon Nov 20 21:32:12 EST 2023
user@user-ProLiant-DL325-Gen10:~/.bitmonero$ grep weak_ptr bitmonero.log* | wc -l
0


## Gingeropolous | 2023-11-23T10:34:58+00:00
on homebox,
uptime 7d 9h 44m 18s

patch considered stable on homebox

Now testing on xmrchain

Prior to pulling in 7345:

All logs

Thu Nov 23 11:30:53 AM CET 2023
xmrchain@Ubuntu-1804-bionic-64-minimal:~/.bitmonero$ grep weak_ptr bitmonero.log* | wc -l
12749

Recent Logs

xmrchain@Ubuntu-1804-bionic-64-minimal:~/.bitmonero$ grep weak_ptr bitmonero.log | wc -l
2162



## vtnerd | 2023-11-23T23:42:09+00:00
> Recent Logs
>
> xmrchain@Ubuntu-1804-bionic-64-minimal:~/.bitmonero$ grep weak_ptr bitmonero.log | wc -l
2162

So it's still happening? Unfortunately I am not seeing this on my local box. Does it require a higher log level than default?

## vtnerd | 2023-11-23T23:58:38+00:00
>> Recent Logs
>>
>> xmrchain@Ubuntu-1804-bionic-64-minimal:~/.bitmonero$ grep weak_ptr bitmonero.log | wc -l
2162
>>
> So it's still happening? Unfortunately I am not seeing this on my local box. Does it require a higher log level than default?

Answered my own question (forgot the log prints level)

## Gingeropolous | 2023-11-24T02:43:58+00:00
sorry im making this confusing. Those were the recent logs before the patch were applied.

as far as I can tell, its not happening. The recent log (bitmonero.log) shows there are no new instances, and the total log (bitmonero.log* , which includes all the logrotated logs) is showing a decreasing number compared to before the patch was applied
```
Height: 3024783/3024783 (100.0%) on mainnet, not mining, net hash 2.41 GH/s, v16, 127(out)+113(in) connections, uptime 0d 16h 10m 34s
xmrchain@Ubuntu-1804-bionic-64-minimal:~/.bitmonero$ date
Fri Nov 24 03:42:24 AM CET 2023
xmrchain@Ubuntu-1804-bionic-64-minimal:~/.bitmonero$ grep weak_ptr bitmonero.log | wc -l
0
xmrchain@Ubuntu-1804-bionic-64-minimal:~/.bitmonero$ grep weak_ptr bitmonero.log* | wc -l
6792
```

The patch seems successful 

## Gingeropolous | 2023-11-24T12:26:07+00:00
and yeah, I run log-level 1

## vtnerd | 2023-11-24T20:05:16+00:00
Ok, sounds like this patch fixes the issue. The problem is _probably_ a race-condition to the destructor of the connection object. I'm not aware of another fix, besides using a `weak_ptr` to stop the abuse of `shared_ptr` (which is what my PR does).

## Gingeropolous | 2023-11-25T15:17:12+00:00
fixed by #7345 

## vtnerd | 2023-11-26T23:01:44+00:00
Now I just have to get reviewers ;)

# Action History
- Created by: Gingeropolous | 2023-11-15T02:57:10+00:00
- Closed at: 2023-11-25T15:17:12+00:00
