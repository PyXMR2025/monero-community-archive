---
title: Starting wallet RPC server - stuck
source_url: https://github.com/monero-project/monero/issues/8243
author: martinoshub
assignees: []
labels: []
created_at: '2022-04-07T03:48:18+00:00'
updated_at: '2022-04-07T11:14:12+00:00'
type: issue
status: closed
closed_at: '2022-04-07T10:57:07+00:00'
---

# Original Description
My monero RPC server gets stuck on "starting wallet RPC server". When I add more logging, it's stuck at "joining all threads".

If I start this with monero-wallet-cli instead of monero-wallet-rpc and give it a wallet, it works just fine. It can sync, it can see incoming coins and everything. But when I start the RPC instead, it's stuck.

Help would be appreciated.

$ ./monero-wallet-rpc --rpc-login x:y --rpc-bind-ip 127.0.0.1 --rpc-bind-port 18050 --daemon-address 127.0.0.1:18081 --trusted-daemon --wallet-dir ~/.bitmonero/wallet --log-level=2
This is the RPC monero wallet. It needs to connect to a monero
daemon to work correctly.

Monero 'Oxygen Orion' (v0.17.3.0-release)
2022-04-07 03:43:50.564 I Setting log level = 2
2022-04-07 03:43:50.564 I Logging to: ./monero-wallet-rpc.log
Logging to ./monero-wallet-rpc.log
2022-04-07 03:43:50.564 I Set server type to: 1 from name: RPC, prefix_name = RPC
2022-04-07 03:43:50.565 I Binding on 127.0.0.1 (IPv4):18050
2022-04-07 03:43:50.565 I Generating SSL certificate
2022-04-07 03:43:51.346 D start accept (IPv4)
2022-04-07 03:43:51.346 D Spawned connection #0 to 0.0.0.0 currently we have sockets count:1
2022-04-07 03:43:51.346 D test, connection constructor set m_connection_type=1
2022-04-07 03:43:51.346 W Starting wallet RPC server
2022-04-07 03:43:51.346 I Run net_service loop( 1 threads)...
2022-04-07 03:43:51.346 D Run server thread name: RPC
2022-04-07 03:43:51.347 D JOINING all threads



# Discussion History
## selsta | 2022-04-07T07:17:25+00:00
Do you know how to compile monero? If yes, can you compile `release-v0.17` branch + #7759 applied?

I likely won't help but it's worth a try.

## martinoshub | 2022-04-07T10:17:11+00:00
> I likely won't help but it's worth a try.

$ ./monero-wallet-rpc --version
Monero 'Oxygen Orion' (v0.17.0.0-f49fc9b48)
$ ./monero-wallet-rpc --rpc-login x:y --rpc-bind-ip 127.0.0.1 --rpc-bind-port 18050 --daemon-address 127.0.0.1:18081 --wallet-dir ~/.bitmonero/wallet --log-level=2
This is the RPC monero wallet. It needs to connect to a monero
daemon to work correctly.

Monero 'Oxygen Orion' (v0.17.0.0-f49fc9b48)
2022-04-07 10:06:59.539 I Setting log level = 2
2022-04-07 10:06:59.539 I Logging to: ./monero-wallet-rpc.log
Logging to ./monero-wallet-rpc.log
2022-04-07 10:06:59.539 I Set server type to: 1 from name: RPC, prefix_name = RPC
2022-04-07 10:06:59.539 I Binding on 127.0.0.1 (IPv4):18050
2022-04-07 10:06:59.540 I Generating SSL certificate
2022-04-07 10:07:01.423 D start accept (IPv4)
2022-04-07 10:07:01.423 D Spawned connection #0 to 0.0.0.0 currently we have sockets count:1
2022-04-07 10:07:01.424 D test, connection constructor set m_connection_type=1
2022-04-07 10:07:01.424 W Starting wallet RPC server
2022-04-07 10:07:01.424 I Run net_service loop( 1 threads)...
2022-04-07 10:07:01.424 D Run server thread name: RPC
2022-04-07 10:07:01.424 D JOINING all threads

In this stage, the RPC port is already open, but sending it any line results in the connection being closed.

Not sure if this helps anything, but I wondered what it was doing, so I did an strace. This stuff below is a snippet from the never-ending work it's doing (it's not flooding the strace logs, just a couple of lines a second).

541165 epoll_wait(5, [{EPOLLIN, {u32=4176776052, u64=94111205198708}}], 128, -1) = 1
541165 timerfd_settime(6, 0, {it_interval={tv_sec=0, tv_nsec=0}, it_value={tv_sec=0, tv_nsec=493959000}}, {it_interval={tv_sec=0, tv_nsec=0}, it_value={tv_sec=0, tv_nsec=0}}) = 0
541165 epoll_wait(5, [{EPOLLIN, {u32=4176776052, u64=94111205198708}}], 128, -1) = 1
541165 timerfd_settime(6, 0, {it_interval={tv_sec=0, tv_nsec=0}, it_value={tv_sec=0, tv_nsec=5830000}}, {it_interval={tv_sec=0, tv_nsec=0}, it_value={tv_sec=0, tv_nsec=0}}) = 0
541165 epoll_wait(5, [{EPOLLIN, {u32=4176776052, u64=94111205198708}}], 128, -1) = 1
541165 timerfd_settime(6, 0, {it_interval={tv_sec=0, tv_nsec=0}, it_value={tv_sec=0, tv_nsec=993891000}}, {it_interval={tv_sec=0, tv_nsec=0}, it_value={tv_sec=0, tv_nsec=0}}) = 0
541165 timerfd_settime(6, 0, {it_interval={tv_sec=0, tv_nsec=0}, it_value={tv_sec=0, tv_nsec=499997000}}, {it_interval={tv_sec=0, tv_nsec=0}, it_value={tv_sec=0, tv_nsec=993730868}}) = 0


## moneromooo-monero | 2022-04-07T10:47:12+00:00
Are you sure you're using the right auth ? It's not basic, it's... I forget, it's the other main http one. You can use --disable-rpc-login to test if this is auth that's tripping you.

## martinoshub | 2022-04-07T10:57:04+00:00
So... I'll leave this here for the next potential doofus who runs into this "problem" (incorrectly perceived by me).

Turns out that "stuck" message is the last thing shown before everything starts working. It wasn't actually stuck, just waiting for connections. It's a bit confusing that it doesn't say something to signal it's ready, but whatever. The blame is on me.

The reason why it "didn't work" (that wonderful expression we all love when we try to debug other people's problems) is that I tried to communicate without SSL, so the connection just closed, so I figured it was still starting up. It wasn't the case. I simply just had to https:// instead of http://. Yes, d'oh.

Anyway, sorry for any potential time wasted. I hope this post can make up for it by helping the next person who makes the same mistake.

ps. An "Init done, server ready" or something to that effect in the startup log messages would be nice.

# Action History
- Created by: martinoshub | 2022-04-07T03:48:18+00:00
- Closed at: 2022-04-07T10:57:07+00:00
