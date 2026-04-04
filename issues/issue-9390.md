---
title: Tor proxy does not work with IPv6 destination
source_url: https://github.com/monero-project/monero/issues/9390
author: woodser
assignees: []
labels:
- request
created_at: '2024-06-30T12:47:18+00:00'
updated_at: '2024-10-08T12:49:52+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Seems monero-wallet-rpc/cli does not work through Tor proxy to an IPv6 destination (IPv4 is ok).

Prerequisites:

- check ipv6 is supported with ping -6 [feder8.me](http://feder8.me/)
- have tor daemon running

Tests:

1. start monero-wallet-rpc connecting to IPv4 node ([node3.monerodevs.org:18089](http://node3.monerodevs.org:18089/))
2. start monero-wallet-rpc connecting to IPv4 node ([node3.monerodevs.org:18089](http://node3.monerodevs.org:18089/)) through SOCKS5 proxy
3. start monero-wallet-rpc connecting to IPv6 node ([feder8.me:18089](http://feder8.me:18089/))
4. start monero-wallet-rpc connecting to IPv6 node ([feder8.me:18089](http://feder8.me:18089/)) through SOCKS5 proxy
5. start monero-wallet-rpc connecting to IPv6 node ([2a0b:f4c2:2::63]:18081)
6. start monero-wallet-rpc connecting to IPv6 node ([2a0b:f4c2:2::63]:18081) through SOCKS5 proxy

Tests 4 and 6 fail with the error message is "no_connection_to_daemon".

See original issue and comment from @fa2a5qj3: https://github.com/haveno-dex/haveno/issues/1076#issuecomment-2198550173

There is a [2 XMR bounty](https://github.com/haveno-dex/haveno/issues/1076) on this issue.

# Discussion History
## shortwavesurfer2009 | 2024-06-30T12:54:06+00:00
Did you change SOCKS5 proxy to [::1]:9050 or whatever? When tor starts it should open SOCKS5 proxies on both 127.0.0.1:9050 (v4 traffic) and [::1]:9050 (v6 traffic). Using 127.0.0.1 for v6 traffic will fail

## vtnerd | 2024-06-30T17:03:19+00:00
Internally we use socks4 which only supports IPv4. So this will never work with IPv6 currently. I will put Socks5+IPv6 support in my next CCS proposal (hopefully I will have time for it).

## boldsuck | 2024-06-30T23:21:29+00:00
Default system tor `SocksPort 9050` & haveno's torrc `SOCKSPort auto` only listens on IPv4.
\+ `SocksPort [::1]:9050` or `SocksPort [::1]:auto` on IPv4 + IPv6

I don't know if SocksPolicy is useful if we have `DisableNetwork 1` in haveno's torrc, but it doesn't hurt.
```
SocksPolicy accept 127.0.0.1
SocksPolicy accept6 [::1]
SocksPolicy reject *
```
[EDIT:]
Just for info: I tested Haveno with torrc settings:
SocksPort auto
SocksPort [::1]:auto

Then Haveno aborts starting. But this should be fixed [now](https://github.com/haveno-dex/haveno/commit/856faafd1ce45aead9648d000d133048298f216e)

## woodser | 2024-10-08T12:22:15+00:00
There is a 2 XMR [bounty](https://github.com/haveno-dex/haveno/issues/1076) on this issue.

# Action History
- Created by: woodser | 2024-06-30T12:47:18+00:00
