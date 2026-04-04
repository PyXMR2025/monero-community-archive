---
title: All SSL RPC requests to daemon running on FreeBSD 11.3 fail (after 15 second
  wait)
source_url: https://github.com/monero-project/monero/issues/6009
author: ndorf
assignees: []
labels: []
created_at: '2019-10-22T21:32:55+00:00'
updated_at: '2019-10-22T22:30:38+00:00'
type: issue
status: closed
closed_at: '2019-10-22T22:30:38+00:00'
---

# Original Description
This issue occurs when the daemon is recent master running on FreeBSD 11.3, which comes with openssl version "1.0.2s-freebsd." The same versions work fine on a nearby Linux system, which happens to use openssl "1.1.0l-1." It doesn't matter which client is used (they both work with the Linux daemon and fail with the FreeBSD one).

The same server is also running two `release-v0.14` daemons (stagenet and mainnet), which work without issues, SSL included. They all use the same libssl.

Basically, requests to the daemon from `monero-wallet-cli` and `monerod <daemon_command>` always fail, after a 15 second delay: 

```
% fgrep Daemonise /monero/data/testnet/bitmonero.log | tail -1                  
2019-10-22 20:28:56.435	     0x806e16000	WARNING	daemon	src/daemon/executor.cpp:61	Monero 'Boron Butterfly' (v0.14.1.2-441ed9f2f) Daemonised
% fgrep Synced /monero/data/testnet/bitmonero.log | tail -1
2019-10-22 20:30:21.655	[P2P4]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1454	Synced 1326346/1326346 (0.300349 sec, 13.317840 blocks/sec), 0.000000 MB queued in 0 spans, stripe 0 -> 0: []
% time ./build/FreeBSD/master/release/bin/monerod --log-level=4 --testnet status   
2019-10-22 20:40:21.795	I Monero 'Boron Butterfly' (v0.14.1.2-441ed9f2f)
2019-10-22 20:40:21.816	I Generating SSL certificate
2019-10-22 20:40:22.026	W SSL peer has not been verified
2019-10-22 20:40:22.026	W SSL peer has not been verified
2019-10-22 20:40:22.031	D SSL handshake success
2019-10-22 20:40:37.042	T READ ENDS: Connection err_code 335544539
2019-10-22 20:40:37.042	D Problems at read: short read
2019-10-22 20:40:37.042	E Unexpected recv fail
2019-10-22 20:40:37.042	T Returning false because of wrong state machine. state: 5
2019-10-22 20:40:37.042	I Failed to invoke http request to  /getinfo
Error: Problem fetching info-- rpc_request: 
2019-10-22 20:40:37.047	D Problems at shutdown: Socket is not connected
./build/FreeBSD/master/release/bin/monerod --log-level=4 --testnet status  0.15s user 0.60s system 4% cpu 16.443 total
% time curl --insecure https://localhost:28081/getinfo 
curl: (52) Empty reply from server
curl --insecure https://localhost:28081/getinfo  0.01s user 0.11s system 0% cpu 15.227 total
%
```

The same requests work fine when using curl with plain HTTP instead of HTTPS.

I've installed a more recent OpenSSL (1.1.1d) from the FreeBSD packages, but I don't know how to get the Monero build to find it under `/usr/local`. I found a CMake variable named `OpenSSL_DIR` but setting that didn't seem to do anything. Does anyone know how that works?

# Discussion History
## selsta | 2019-10-22T21:35:46+00:00
Did you try latest master? I think https://github.com/monero-project/monero/pull/5996 fixed this.

## ndorf | 2019-10-22T22:30:35+00:00
Yup, fixed. Thanks

# Action History
- Created by: ndorf | 2019-10-22T21:32:55+00:00
- Closed at: 2019-10-22T22:30:38+00:00
