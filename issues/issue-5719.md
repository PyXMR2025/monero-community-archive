---
title: failure to read passphrase when using screen.
source_url: https://github.com/monero-project/monero/issues/5719
author: trasherdk
assignees: []
labels: []
created_at: '2019-07-01T16:44:10+00:00'
updated_at: '2019-09-22T12:38:00+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Setting up a private stagenet with 2 monerod running in screen sessions. No problem.
Launching 2 wallets, also in screen sessions, with one mining on the daemon.
Wallets was created without password.

I'm constantly prompted for password, but the wallet does not wait for input.

`Monero 'Boron Butterfly' (v0.14.1.0-29a505d1c)`
```
[wallet 56Vbjc]: status
Refreshed 260/281, syncing, daemon RPC v2.6, SSL
[wallet 56Vbjc]: refresh        
Starting refresh...
Enter password (output received): Enter password (output received): Enter password (output received): Enter password (output received): Error: refresh failed: unexpected error: proxy exception in refresh thread. Blocks received: 0
Password needed (output received) - use the refresh command
Password needed (output received) - use the refresh command
Password needed (output received) - use the refresh command
Password needed (output received) - use the refresh command
[wallet 56Vbjc]:                
[wallet 56Vbjc]: wallet_info    
Filename: /home/crypto/stagenet/wallet_02.bin
Description: <Not set>
Address: 56VbjczrFCVZiLn66S3Qzv8QfmtcwkdXgM5cWGsXAPxoQeMQ79md51PLPCijvzk1iHbuHi91pws5B7iajTX9KTtJ4Z6HAo6
Type: Normal
Network type: Stagenet
[wallet 56Vbjc]:                
```
```
status 
Height: 288/288 (100.0%) on stagenet, mining at 17 H/s, net hash 16 H/s, v1 (next fork in 22.0 days), up to date, 1(out)+1(in) connections, uptime 0d 0h 38m 28s
2019-07-01 16:26:04.014     W There were 7 blocks in the last 90 minutes, there might be large hash rate changes, or we might be partitioned, cut off from the Monero network or under attack. Or it could be just sheer bad luck.
2019-07-01 16:26:31.641  I Found block <7e43974ccbe1217af29881a519ef7de9f170c8dbb3d5cb03079bb3438ec874e5> at height 288 for difficulty: 1000
2019-07-01 16:26:46.638  I Found block <64413c350fa12e5ef9c559fa036afb739ba43bb9dc51778fc246c35adb2af19d> at height 289 for difficulty: 1000
2019-07-01 16:27:05.563  I Found block <62f9594d95bab35c013252c582cb07d8d3152300f19b611ecf12af281ee518d5> at height 290 for difficulty: 1000
2019-07-01 16:27:15.483  I Found block <db0c7711c35c6239eb4a20cd6a829b25163d5b4f960fc15e975488d3c547bef9> at height 291 for difficulty: 1000
2019-07-01 16:27:34.028  W There were 11 blocks in the last 90 minutes, there might be large hash rate changes, or we might be partitioned, cut off from the Monero network or under attack. Or it could be just sheer bad luck.
status 
Height: 292/292 (100.0%) on stagenet, mining at 17 H/s, net hash 16 H/s, v1 (next fork in 22.0 days), up to date, 1(out)+1(in) connections, uptime 0d 0h 40m 39s
```


# Discussion History
## iDunk5400 | 2019-07-01T16:55:30+00:00
`set`
`help set`
`set ask-password 1`


## moneromooo-monero | 2019-07-01T17:01:11+00:00
Run with --log-level 1. If you don't see stack traces, you need either build with libunwind-dev, or run in gdb and break on exceptions ("break throw") to see what/why/where those exceptions are throwing a spanner.

## trasherdk | 2019-07-02T08:43:16+00:00
I was unable to provoke same error today. I have no clue to why.
I tried to `set ask-password never` and `set ask-password 1` but
was not prompted for password.

I believe I have all dependencies in place.
```
monero-v0.14.1.0$ ldd monerod 
        linux-vdso.so.1 (0x00007ffcd6d93000)
        librt.so.1 => /lib64/librt.so.1 (0x00007f6b0724a000)
        libdl.so.2 => /lib64/libdl.so.2 (0x00007f6b07046000)
        libboost_chrono.so.1.59.0 => /usr/lib64/libboost_chrono.so.1.59.0 (0x00007f6b06e40000)
        libboost_filesystem.so.1.59.0 => /usr/lib64/libboost_filesystem.so.1.59.0 (0x00007f6b06c29000)
        libboost_program_options.so.1.59.0 => /usr/lib64/libboost_program_options.so.1.59.0 (0x00007f6b069b0000)
        libboost_regex.so.1.59.0 => /usr/lib64/libboost_regex.so.1.59.0 (0x00007f6b066af000)
        libboost_system.so.1.59.0 => /usr/lib64/libboost_system.so.1.59.0 (0x00007f6b064ac000)
        libzmq.so.5 => /usr/lib64/libzmq.so.5 (0x00007f6b0622b000)
        libsodium.so.23 => /usr/lib64/libsodium.so.23 (0x00007f6b05fd5000)
        libreadline.so.6 => /usr/lib64/libreadline.so.6 (0x00007f6b05d8c000)
        libtermcap.so.2 => /lib64/libtermcap.so.2 (0x00007f6b05b89000)
        libunbound.so.2 => /usr/lib64/libunbound.so.2 (0x00007f6b058e0000)
        libboost_date_time.so.1.59.0 => /usr/lib64/libboost_date_time.so.1.59.0 (0x00007f6b056cf000)
        libssl.so.1 => /lib64/libssl.so.1 (0x00007f6b0545c000)
        libcrypto.so.1 => /lib64/libcrypto.so.1 (0x00007f6b05003000)
        libboost_serialization.so.1.59.0 => /usr/lib64/libboost_serialization.so.1.59.0 (0x00007f6b04dc8000)
        libboost_thread.so.1.59.0 => /usr/lib64/libboost_thread.so.1.59.0 (0x00007f6b04ba2000)
        libstdc++.so.6 => /usr/lib64/libstdc++.so.6 (0x00007f6b04826000)
        libm.so.6 => /lib64/libm.so.6 (0x00007f6b0451d000)
        libgcc_s.so.1 => /usr/lib64/libgcc_s.so.1 (0x00007f6b04306000)
        libpthread.so.0 => /lib64/libpthread.so.0 (0x00007f6b040e9000)
        libc.so.6 => /lib64/libc.so.6 (0x00007f6b03d20000)
        /lib64/ld-linux-x86-64.so.2 (0x00007f6b080bc000)
        libicudata.so.56 => /usr/lib64/libicudata.so.56 (0x00007f6b0233d000)
        libicui18n.so.56 => /usr/lib64/libicui18n.so.56 (0x00007f6b01eac000)
        libicuuc.so.56 => /usr/lib64/libicuuc.so.56 (0x00007f6b01b14000)
        libunwind.so.8 => /usr/lib64/libunwind.so.8 (0x00007f6b018fa000)
        libevent-2.0.so.5 => /usr/lib64/libevent-2.0.so.5 (0x00007f6b016b2000)
        liblzma.so.5 => /lib64/liblzma.so.5 (0x00007f6b0148d000)
```


## trasherdk | 2019-07-12T00:03:15+00:00
I just got that `Enter password` thing again:
```
Enter password (output received): Enter password (output received): Enter password (output received): Enter password (output received): Error: refresh failed: unexpected error: proxy exception in refresh thread. Blocks received: 0
Password needed (output received) - use the refresh command
Password needed (output received) - use the refresh command
Password needed (output received) - use the refresh command
Password needed (output received) - use the refresh command
```
I appears when starting `monero-wallet-cli` from a bash script, in a detached screen session:
```
#!/bin/sh
do_stuff
do_more
screen -S 'miner' -d -m ./monero-stratum-ss/monero-wallet-cli --testnet --password '' --wallet-file data/testnet/miner-wallet
```
then, after some time, reattaching `screen -r miner`, and the `Enter password` occur (sometimes).

What do I need to set, to get rid of:
```
2019-07-11 23:17:06.944  E Error locking page at 0x7fa7a4038000: Cannot allocate memory, subsequent mlock errors will be silenced
```
from `monero-wallet-rcp` ?

BTW. I'm on testnet at the moment.

## moneromooo-monero | 2019-07-12T11:20:39+00:00
See man bash, ulimit, "-l     The maximum size that may be locked into memory".

## moneromooo-monero | 2019-09-06T13:57:59+00:00
Would you mind editing the title to something like "failure to read passphrase when using screen" or something similar which matches the bug please ? Helps when reading the bug list,

# Action History
- Created by: trasherdk | 2019-07-01T16:44:10+00:00
