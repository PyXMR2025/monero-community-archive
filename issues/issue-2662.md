---
title: xmrig, kawpow and socks4/5
source_url: https://github.com/xmrig/xmrig/issues/2662
author: Blisk
assignees: []
labels: []
created_at: '2021-10-31T20:59:47+00:00'
updated_at: '2021-10-31T23:13:52+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Is it possible to mine kawpow over socks4 or socks5 or something like socat?
As I see it is possible to mine over tor but only monero.

# Discussion History
## Spudz76 | 2021-10-31T22:18:20+00:00
You can mine via whatever tunneling method you want as long as it can be set up transparently.

There are SOCKS5 socket-capture tools which wrap any app and force its networking to go through SOCKS5 proxy.  Similar to VPN.

## Blisk | 2021-10-31T23:02:20+00:00
Any suggestion what is most easy to use?

## Spudz76 | 2021-10-31T23:13:52+00:00
Win10 might work with [the built-in setting](https://superuser.com/questions/1528185/how-can-i-set-socks-proxy-on-windows)  There is another tool called [Sockscap](https://www.sockscap64.com/homepage/) if the built-in doesn't work.

Linux there are various tools like `shadowsocks` or others [as listed here](https://wiki.debian.org/SOCKS)

I do not know what works best because I have never needed SOCKS support.  I just spin up a real VPN with OpenVPN or something else routable by normal methods that don't need tunneling wrappers.

# Action History
- Created by: Blisk | 2021-10-31T20:59:47+00:00
