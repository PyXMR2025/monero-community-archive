---
title: Exception at server worker thread, what=map::at
source_url: https://github.com/monero-project/monero/issues/701
author: FlailingBorg
assignees: []
labels: []
created_at: '2016-03-05T12:48:48+00:00'
updated_at: '2016-12-15T17:59:24+00:00'
type: issue
status: closed
closed_at: '2016-12-15T17:59:24+00:00'
---

# Original Description
For quite a while I've been getting this error every once in a while, running bitmonerod in a 64bit Linux VM, built from source, both the last tagged release and almost current (Feb 18, 1889c0e) master branch.

```
ERROR   {2} {p1} 2016-03-03 20:32:10.560373 [abstract_tcp_server2.inl+763 ::worker_thread] Exception at server worker thread, what=map::at
```

After this, at some point the block height stops increasing if I check with `print_height`, but it still responds to commands. I tried increasing the log level but didn't get anything useful out of it. It usually takes a few days to happen. Any suggestions on how to fix this or get more info?


# Discussion History
## FlailingBorg | 2016-03-06T15:58:41+00:00
Okay, so lately it seems to happen every couple of hours rather than every couple of days.

```
2016-Mar-06 15:51:16.727559 [P2P4][***.***.***.***:18080 OUT]Synced 985718/985718
2016-Mar-06 15:51:16.728043 [P2P4][***.***.***.***:18080 OUT] SYNCHRONIZED OK
2016-Mar-06 15:51:16.728052 [P2P5][***.***.**.***:18080 OUT] SYNCHRONIZED OK
ERROR   {2} {p1} 2016-03-06 15:51:33.014146 [abstract_tcp_server2.inl+763 ::worker_thread] Exception at server worker thread, what=map::at
print_cn
Remote Host                   Peer id             Recv/Sent (inactive,sec)      State                    Livetime(sec)       Down (kB/s) Down(now)     Up (kB/s) Up(now)      

print_height
985732
save
Blockchain saved
exit
2016-Mar-06 16:55:57.298031 [node] Stop signal sent
Stop signal sent
2016-Mar-06 16:55:57.690574 [SRV_MAIN]net_service loop stopped.
2016-Mar-06 16:55:57.690734 [SRV_MAIN]p2p net loop stopped
2016-Mar-06 16:55:57.699169 [node] Stop signal sent
2016-Mar-06 16:55:57.699201 [SRV_MAIN]Stopping core rpc server...
2016-Mar-06 16:55:57.699770 [SRV_MAIN]Node stopped.
2016-Mar-06 16:55:57.699916 [SRV_MAIN]Deinitializing rpc server...
2016-Mar-06 16:55:57.700350 [SRV_MAIN]Deinitializing p2p...
2016-Mar-06 16:55:57.765315 [SRV_MAIN]Deinitializing core...
2016-Mar-06 16:55:57.785537 [SRV_MAIN]Closing IO Service.
2016-Mar-06 16:55:57.822704 [SRV_MAIN]Deinitializing cryptonote_protocol...
```


## moneromooo-monero | 2016-03-29T17:06:02+00:00
If you can repeat the problem while having the two patches at https://github.com/monero-project/bitmonero/pull/775, we should see where that exception is coming from now.


## FlailingBorg | 2016-03-31T19:40:29+00:00
Thanks, I'll rebuild including that commit and see what happens. Oddly enough the exception hasn't occurred at all lately.


## moneromooo-monero | 2016-09-24T16:45:14+00:00
Any luck ?


## luigi1111 | 2016-12-15T17:59:24+00:00
@FlailingBorg Please reopen if this reoccurs.

# Action History
- Created by: FlailingBorg | 2016-03-05T12:48:48+00:00
- Closed at: 2016-12-15T17:59:24+00:00
