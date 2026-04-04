---
title: Monerod periodically crashes on sync (Assertion failed)
source_url: https://github.com/monero-project/monero/issues/8897
author: alexhooketh
assignees: []
labels:
- bug
- reproduction needed
created_at: '2023-06-09T06:48:57+00:00'
updated_at: '2023-12-09T06:05:03+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I'm on 82% sync now and I've noticed that sometimes monerod crashes with errors like this

```
2023-06-09 04:20:24.204 I Synced 2406260/2904072 (82%, 497812 left)
2023-06-09 04:20:24.723 I Synced 2406280/2904072 (82%, 497792 left)
2023-06-09 04:20:24.811 I Synced 2406300/2904072 (82%, 497772 left)
2023-06-09 04:20:24.875 I Synced 2406320/2904072 (82%, 497752 left)
Assertion failed: nbytes == sizeof (dummy) (src/signaler.cpp:395)
Assertion failed: nbytes == sizeof (dummy) (src/signaler.cpp:395)
Assertion failed: nbytes == sizeof (dummy) (src/signaler.cpp:395)
2023-06-09 04:20:25.402 I Synced 2406340/2904072 (82%, 497732 left)

0:\Secret\Path\123\Monero>
```

It's not really critical for me as I just restart daemon and it continues syncing as usual, but I thought that maybe you will need this info. [According to google it's assertions from libzmq](https://github.com/zeromq/libzmq/issues/1930)

I'm using windows 11 22H2, syncing on an external ssd. Command: `monerod --p2p-bind-port=30311 --data-dir=D:\monerodata`

# Discussion History
## selsta | 2023-06-09T07:31:41+00:00
We can try to update libzmq and see if the issue goes away. Would you run a test monerod with updated dependency?

## alexhooketh | 2023-06-09T09:53:28+00:00
> We can try to update libzmq and see if the issue goes away. Would you run a test monerod with updated dependency?

Sure!

## selsta | 2023-06-09T15:00:14+00:00
Seems we already use the latest version, so that can't be it.

## alexhooketh | 2023-06-09T15:42:50+00:00
> Seems we already use the latest version, so that can't be it.

Its behaviour is interesting. It crashes at random but without database corruption or anything that could say it crashed. I just run a node again and it works as always. I even made a python script that automatically reloads it when it crashes :P 
I don't use any antiviruses, so I think there's something with libzmq itself

## moneromooo-monero | 2023-06-10T10:19:51+00:00
It looks like the crash comes some time later after the assertions. It may well be related though.

## alexhooketh | 2023-06-10T10:36:12+00:00
> It looks like the crash comes some time later after the assertions. It may well be related though.

Actually it crashes almost instantly after assertion failed messages, it's just sync messages running too fast that they have time to print before closing

## alexhooketh | 2023-06-14T09:54:24+00:00
> It looks like the crash comes some time later after the assertions. It may well be related though.

Tried ubuntu 22.04. The same thing. Downloaded both binaries from github, checksums match.

## selsta | 2023-06-14T09:55:39+00:00
@41rjordan same PC or a different one? same network?

## alexhooketh | 2023-06-14T10:52:02+00:00
> @41rjordan same PC or a different one? same network?

Windows is on my personal PC on my home network. Ubuntu is on dedicated server in another country. Both 16GB ram, 8 cores Intel CPU

## selsta | 2023-06-14T10:52:54+00:00
And both have the same libzmq assertion?

## alexhooketh | 2023-06-14T10:58:13+00:00
> And both have the same libzmq assertion?

Didn't see error on Ubuntu. Started it again, i'll write error here when it'll crash again.
I've also noticed that after sync monerod crashes every 2 hours +-5 minutes, but I'm not sure if it's not coincidence 

## gituser | 2023-08-15T21:03:17+00:00
I'm getting similar issue on testnet with latest monero release `v0.18.2.2`, monerod crashes, wallets are hanging with timeouts:

```
2023-08-15 20:53:20.010	[P2P9]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1687	Synced 2305966/2305966
2023-08-15 20:53:24.586	[P2P1]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2490	
2023-08-15 20:53:24.586	[P2P1]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2490	**********************************************************************
2023-08-15 20:53:24.586	[P2P1]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2490	You are now synchronized with the network. You may now start monero-wallet-cli.
2023-08-15 20:53:24.586	[P2P1]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2490	
2023-08-15 20:53:24.586	[P2P1]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2490	Use the "help" command to see the list of available commands.
2023-08-15 20:53:24.586	[P2P1]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2490	**********************************************************************
2023-08-15 20:59:57.421	[P2P6]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:409	[44.212.30.239:28080 OUT] Sync data returned a new top block candidate: 2305966 -> 2305972 [Your node is 6 blocks (12.0 minutes) behind] 
2023-08-15 20:59:57.421	[P2P6]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:409	SYNCHRONIZATION started
2023-08-15 21:01:42.655	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::bad_alloc
2023-08-15 21:01:42.655	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2023-08-15 21:01:42.655	    7fc3b12f5700	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::bad_alloc
2023-08-15 21:01:42.655	    7fc3b12f5700	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2023-08-15 21:01:42.655	    7fc3af4ef700	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::bad_alloc
2023-08-15 21:01:42.655	    7fc3af4ef700	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2023-08-15 21:01:42.655	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1] /home/monero/monerod(+0x5313ad) [0x562211b313ad] 
2023-08-15 21:01:42.655	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] /home/monero/monerod(+0x88ca31) [0x562211e8ca31] 
2023-08-15 21:01:42.655	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3] /home/monero/monerod(+0x882c61) [0x562211e82c61] 
2023-08-15 21:01:42.655	    7fc3b12f5700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1] /home/monero/monerod(+0x5313ad) [0x562211b313ad] 
2023-08-15 21:01:42.655	    7fc3b12f5700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] /home/monero/monerod(+0x88ca31) [0x562211e8ca31] 
2023-08-15 21:01:42.655	    7fc3b12f5700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3] /home/monero/monerod(+0x882c61) [0x562211e82c61] 
2023-08-15 21:01:42.655	    7fc3b12f5700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4] /home/monero/monerod(+0x87ff93) [0x562211e7ff93] 
2023-08-15 21:01:42.655	    7fc3b12f5700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5] /home/monero/monerod(+0x4e1c62) [0x562211ae1c62] 
2023-08-15 21:01:42.655	    7fc3b12f5700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6] /home/monero/monerod(+0x4e2b5c) [0x562211ae2b5c] 
2023-08-15 21:01:42.655	    7fc3b12f5700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7] /home/monero/monerod(+0x4c8301) [0x562211ac8301] 
2023-08-15 21:01:42.655	    7fc3b12f5700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8] /home/monero/monerod(+0x4c84a6) [0x562211ac84a6] 
2023-08-15 21:01:42.655	    7fc3b12f5700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9] /home/monero/monerod(+0x4c854d) [0x562211ac854d] 
2023-08-15 21:01:42.655	    7fc3b12f5700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10] /home/monero/monerod(+0x46306c) [0x562211a6306c] 
2023-08-15 21:01:42.655	    7fc3b12f5700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11] /home/monero/monerod(+0x528f89) [0x562211b28f89] 
2023-08-15 21:01:42.656	    7fc3b12f5700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12] /home/monero/monerod(+0xb6908d) [0x56221216908d] 
2023-08-15 21:01:42.656	    7fc3b12f5700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [13]  0x76db) [0x7fc8301726db]:_64-linux-gnu/libpthread.so.0(+0x76db) [0x7fc8301726db]
2023-08-15 21:01:42.656	    7fc3b12f5700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [14]  0x3f) [0x7fc82fe9b61f]:_64-linux-gnu/libc.so.6(clone+0x3f) [0x7fc82fe9b61f]
2023-08-15 21:01:42.656	    7fc3b12f5700	INFO	stacktrace	src/common/stack_trace.cpp:172	
2023-08-15 21:01:42.656	    7fc3b26f9700	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::bad_alloc
2023-08-15 21:01:42.656	    7fc3b26f9700	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2023-08-15 21:01:42.656	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4] /home/monero/monerod(+0x87ff93) [0x562211e7ff93] 
2023-08-15 21:01:42.656	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5] /home/monero/monerod(+0x4e1c62) [0x562211ae1c62] 
2023-08-15 21:01:42.656	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6] /home/monero/monerod(+0x4e2b5c) [0x562211ae2b5c] 
2023-08-15 21:01:42.656	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7] /home/monero/monerod(+0x4c8301) [0x562211ac8301] 
2023-08-15 21:01:42.656	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8] /home/monero/monerod(+0x4c84a6) [0x562211ac84a6] 
2023-08-15 21:01:42.656	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9] /home/monero/monerod(+0x4c854d) [0x562211ac854d] 
2023-08-15 21:01:42.656	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10] /home/monero/monerod(+0x46306c) [0x562211a6306c] 
2023-08-15 21:01:42.656	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11] /home/monero/monerod(+0x528f89) [0x562211b28f89] 
2023-08-15 21:01:42.656	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12] /home/monero/monerod(+0x529b58) [0x562211b29b58] 
2023-08-15 21:01:42.656	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [13] /home/monero/monerod(+0x4742a6) [0x562211a742a6] 
2023-08-15 21:01:42.656	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [14] /home/monero/monerod(+0x49626b) [0x562211a9626b] 
2023-08-15 21:01:42.656	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [15] /home/monero/monerod(+0x43b466) [0x562211a3b466] 
2023-08-15 21:01:42.656	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [16] /home/monero/monerod(+0x441b98) [0x562211a41b98] 
2023-08-15 21:01:42.656	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [17] /home/monero/monerod(+0x192d0b) [0x562211792d0b] 
2023-08-15 21:01:42.656	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [18] /home/monero/monerod(+0x194638) [0x562211794638] 
2023-08-15 21:01:42.656	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [19] /home/monero/monerod(+0x194cab) [0x562211794cab] 
2023-08-15 21:01:42.656	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [20] /home/monero/monerod(+0x195001) [0x562211795001] 
2023-08-15 21:01:42.656	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [21] /home/monero/monerod(+0x3fa242) [0x5622119fa242] 
2023-08-15 21:01:42.656	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [22] /home/monero/monerod(+0x3fbd1e) [0x5622119fbd1e] 
2023-08-15 21:01:42.656	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [23] /home/monero/monerod(+0x1301b5) [0x5622117301b5] 
2023-08-15 21:01:42.656	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [24] /home/monero/monerod(+0x130b90) [0x562211730b90] 
2023-08-15 21:01:42.656	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [25] /home/monero/monerod(+0x3c8f39) [0x5622119c8f39] 
2023-08-15 21:01:42.656	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [26] /home/monero/monerod(+0xb6908d) [0x56221216908d] 
2023-08-15 21:01:42.656	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [27]  0x76db) [0x7fc8301726db]:_64-linux-gnu/libpthread.so.0(+0x76db) [0x7fc8301726db]
2023-08-15 21:01:42.656	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [28]  0x3f) [0x7fc82fe9b61f]:_64-linux-gnu/libc.so.6(clone+0x3f) [0x7fc82fe9b61f]
2023-08-15 21:01:42.656	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	
2023-08-15 21:01:42.656	    7fc3b26f9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1] /home/monero/monerod(+0x5313ad) [0x562211b313ad] 
2023-08-15 21:01:42.656	    7fc3b26f9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] /home/monero/monerod(+0x88ca31) [0x562211e8ca31] 
2023-08-15 21:01:42.656	    7fc3b26f9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3] /home/monero/monerod(+0x882c61) [0x562211e82c61] 
2023-08-15 21:01:42.656	    7fc3b26f9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4] /home/monero/monerod(+0x87ff93) [0x562211e7ff93] 
2023-08-15 21:01:42.656	    7fc3b26f9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5] /home/monero/monerod(+0x4e1c62) [0x562211ae1c62] 
2023-08-15 21:01:42.656	    7fc3b26f9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6] /home/monero/monerod(+0x4e2b5c) [0x562211ae2b5c] 
2023-08-15 21:01:42.656	    7fc3b26f9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7] /home/monero/monerod(+0x4c8301) [0x562211ac8301] 
2023-08-15 21:01:42.656	    7fc3b26f9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8] /home/monero/monerod(+0x4c84a6) [0x562211ac84a6] 
2023-08-15 21:01:42.656	    7fc3b26f9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9] /home/monero/monerod(+0x4c854d) [0x562211ac854d] 
2023-08-15 21:01:42.656	    7fc3b26f9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10] /home/monero/monerod(+0x46306c) [0x562211a6306c] 
2023-08-15 21:01:42.656	    7fc3b26f9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11] /home/monero/monerod(+0x528f89) [0x562211b28f89] 
2023-08-15 21:01:42.656	    7fc3b26f9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12] /home/monero/monerod(+0xb6908d) [0x56221216908d] 
2023-08-15 21:01:42.656	    7fc3b26f9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [13]  0x76db) [0x7fc8301726db]:_64-linux-gnu/libpthread.so.0(+0x76db) [0x7fc8301726db]
2023-08-15 21:01:42.656	    7fc3b26f9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [14]  0x3f) [0x7fc82fe9b61f]:_64-linux-gnu/libc.so.6(clone+0x3f) [0x7fc82fe9b61f]
2023-08-15 21:01:42.656	    7fc3b26f9700	INFO	stacktrace	src/common/stack_trace.cpp:172	
2023-08-15 21:01:42.656	    7fc3af4ef700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1] /home/monero/monerod(+0x5313ad) [0x562211b313ad] 
2023-08-15 21:01:42.656	    7fc3af4ef700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] /home/monero/monerod(+0x88ca31) [0x562211e8ca31] 
2023-08-15 21:01:42.656	    7fc3af4ef700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3] /home/monero/monerod(+0x882c61) [0x562211e82c61] 
2023-08-15 21:01:42.656	    7fc3af4ef700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4] /home/monero/monerod(+0x87ff93) [0x562211e7ff93] 
2023-08-15 21:01:42.656	    7fc3af4ef700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5] /home/monero/monerod(+0x4e1c62) [0x562211ae1c62] 
2023-08-15 21:01:42.656	    7fc3af4ef700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6] /home/monero/monerod(+0x4e2b5c) [0x562211ae2b5c] 
2023-08-15 21:01:42.656	    7fc3af4ef700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7] /home/monero/monerod(+0x4c8301) [0x562211ac8301] 
2023-08-15 21:01:42.656	    7fc3af4ef700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8] /home/monero/monerod(+0x4c84a6) [0x562211ac84a6] 
2023-08-15 21:01:42.656	    7fc3af4ef700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9] /home/monero/monerod(+0x4c854d) [0x562211ac854d] 
2023-08-15 21:01:42.656	    7fc3af4ef700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10] /home/monero/monerod(+0x46306c) [0x562211a6306c] 
2023-08-15 21:01:42.656	    7fc3af4ef700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11] /home/monero/monerod(+0x528f89) [0x562211b28f89] 
2023-08-15 21:01:42.656	    7fc3af4ef700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12] /home/monero/monerod(+0xb6908d) [0x56221216908d] 
2023-08-15 21:01:42.656	    7fc3af4ef700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [13]  0x76db) [0x7fc8301726db]:_64-linux-gnu/libpthread.so.0(+0x76db) [0x7fc8301726db]
2023-08-15 21:01:42.656	    7fc3af4ef700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [14]  0x3f) [0x7fc82fe9b61f]:_64-linux-gnu/libc.so.6(clone+0x3f) [0x7fc82fe9b61f]
2023-08-15 21:01:42.656	    7fc3af4ef700	INFO	stacktrace	src/common/stack_trace.cpp:172	
2023-08-15 21:01:57.896	[P2P6]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1687	Synced 2305972/2305972
```

## selsta | 2023-08-15T21:04:59+00:00
@gituser the log you posted does not show any crash

## gituser | 2023-08-15T21:11:08+00:00
> @gituser the log you posted does not show any crash

ok, so the stacktrace is perfectly normal?

and

```
2023-08-15 21:01:42.656	    7fc3b26f9700	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::bad_alloc
2023-08-15 21:01:42.656	    7fc3b26f9700	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:```

## gituser | 2023-08-15T21:13:27+00:00
@selsta in wallet log I get entries like: 

```
2023-08-15 20:53:38.565	[RPC0]	WARNING	wallet.wallet2	src/wallet/wallet2.cpp:3274	Expected 100 out of 8967 tx(es), got 97
```

and sometimes if I try to query wallet via RPC it just timeouts, any idea what might be the reason?

## selsta | 2023-08-15T22:43:44+00:00
bad_alloc means you don't have huge pages enabled on your system, but it should not cause any issues: https://github.com/monero-project/monero/issues/8790#issuecomment-1498511918

> query wallet via RPC

How do you do that?

## gituser | 2023-08-15T22:59:12+00:00
@selsta 
mostly I query height by using `get_height` RPC method and I'm getting occasionally timeouts even though there is a timeout set to 3 minutes for each request.

Here is an example request:

```
curl http://127.0.0.1:28085/json_rpc -d '{"jsonrpc":"2.0","method":"get_height"}' -H 'Content-Type: application/json'
```

## selsta | 2023-08-15T23:02:31+00:00
Which OS are you using, what kind of hardware do you have? It seems you custom compiled monero, or used a package manager?

## gituser | 2023-08-15T23:04:42+00:00
@selsta I'm using `Ubuntu 18.04.6 LTS` with latest updates, monero is compiled from source (latest release `v0.18.2.2-release`, no custom patches). This is a testnet and data resides on HDD, 8GB memory.

## selsta | 2023-08-15T23:07:08+00:00
It might be related to HDD, is it a local disk, USB attached, network drive?

## gituser | 2023-08-15T23:08:14+00:00
@selsta this is a local HDD drive (SATA3 interface I believe).

## selsta | 2023-08-15T23:15:21+00:00
That might explain worse performance but should not cause any minute long timeouts.

## gituser | 2023-08-16T10:08:36+00:00
@selsta storage isn't an issue here.
I've moved whole VM to the SSD, but still getting such errors. I think the issue here is either monerod connectivity (no peers, I have my outside port closed, running with --no-igd, --hide-my-port) or something to do with the wallets.

Also getting these entries in monerod log:
```
2023-08-16 10:08:47.084	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: boost::exception_detail::clone_impl<boost::exception_detail::error_info_injector<boost::bad_weak_ptr> >
2023-08-16 10:08:47.084	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2023-08-16 10:08:47.084	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1] /home/monero/monerod(+0x5313ad) [0x558f9f5313ad] 
2023-08-16 10:08:47.084	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] /home/monero/monerod(+0x12f4fc) [0x558f9f12f4fc] 
2023-08-16 10:08:47.084	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3] /home/monero/monerod(+0x3aa8e7) [0x558f9f3aa8e7] 
2023-08-16 10:08:47.084	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4] /home/monero/monerod(+0x3be227) [0x558f9f3be227] 
2023-08-16 10:08:47.084	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5] /home/monero/monerod(+0x3cd55b) [0x558f9f3cd55b] 
2023-08-16 10:08:47.084	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6] /home/monero/monerod(+0x3cd5fc) [0x558f9f3cd5fc] 
2023-08-16 10:08:47.084	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7] /home/monero/monerod(+0x42cdc5) [0x558f9f42cdc5] 
2023-08-16 10:08:47.084	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8] /home/monero/monerod(+0x3a8fb3) [0x558f9f3a8fb3] 
2023-08-16 10:08:47.084	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9] /home/monero/monerod(+0x3c9949) [0x558f9f3c9949] 
2023-08-16 10:08:47.084	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10] /home/monero/monerod(+0x3aa603) [0x558f9f3aa603] 
2023-08-16 10:08:47.084	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11] /home/monero/monerod(+0x130b90) [0x558f9f130b90] 
2023-08-16 10:08:47.084	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12] /home/monero/monerod(+0x3c8f39) [0x558f9f3c8f39] 
2023-08-16 10:08:47.084	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [13] /home/monero/monerod(+0xb6908d) [0x558f9fb6908d] 
2023-08-16 10:08:47.084	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [14]  0x76db) [0x7f2b119526db]:_64-linux-gnu/libpthread.so.0(+0x76db) [0x7f2b119526db]
2023-08-16 10:08:47.084	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [15]  0x3f) [0x7f2b1167b61f]:_64-linux-gnu/libc.so.6(clone+0x3f) [0x7f2b1167b61f]
```

Is it caused by hugepages disabled?

## gituser | 2023-08-16T13:18:22+00:00
It seems the issue is from the old wallets format and/or something to do with that, I've recreated all wallets from seeds and restarted `monero-wallet-rpc` there are no longer timeout errors for now.. I still have old wallet files in case to reproduce the issue somehow.

## selsta | 2023-08-16T23:50:24+00:00
> Is it caused by hugepages disabled?

No, but it doesn't appear to be related to any issues you are having.

## gituser | 2023-08-17T13:47:14+00:00
@selsta if you give me instructions on how to debug this issue I can try to pinpoint it, most likely it's in `monero-wallet-rpc`

# Action History
- Created by: alexhooketh | 2023-06-09T06:48:57+00:00
