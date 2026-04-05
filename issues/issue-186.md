---
title: xmrig through proxy
source_url: https://github.com/xmrig/xmrig/issues/186
author: ridera7
assignees: []
labels:
- enhancement
created_at: '2017-11-03T15:33:55+00:00'
updated_at: '2018-11-05T07:01:14+00:00'
type: issue
status: closed
closed_at: '2018-11-05T07:01:14+00:00'
---

# Original Description
Hi. Can you tell me what should I do to make xmrig working through proxy?
Here is the situation: My main computer is sit behind corporate proxy and has Win10 onboard and Proxifier to connect ANY application through corporative proxy. There is installed some proxy-server for receiving requests from other computer (witn Linux Mint18.2 onboard).
I configured main settings on it to connect through main machine (so browsers, apt, synaptic works fine with internet). But xmrig always tells me "[pool] DNS error: temporary failure". I think it can't work through my improvized tunnel?
I can't find any settings for work with proxy in xmrig. Does it able to work with proxy?
May be exist some things like proxifier for linux?
(Sorry for my bad english)

# Discussion History
## ridera7 | 2017-11-07T06:19:03+00:00
Now I using xmrig-proxy to mine on some monero pool but not on nicehash.


## ght3d | 2017-11-07T16:37:55+00:00
A http or socks4/5 proxy feature like in cpuminer-opt would be really great. Xmrig would've worked on nicehash and would've mined other coins properly. As for now, using xmrig with xmrig proxy doesnt work when mining other cryptonight coins like bytecoin and electroneum. Also an internal http proxy feature would allow users to overcome problems like firewalls (in case there's a separate gateway with internet and outside the firewall in the same network). 

Dev, please consider adding and http or socks proxy feature into xmrig, it would make xmrig the best miner of all (xmrig speed is much more superior to other mining software).

## dagmoller | 2017-11-09T19:06:39+00:00
I agree, socks proxy would be great...

## xmrig | 2017-11-10T02:55:57+00:00
I agree, but it need more complicated, all cpuminer-* use libcurl and this lib has proxy support out of box, just need wrap it, but libuv not support proxy, it need be implemented by self (or maybe someone else already did it).
Thank you.


## ghost | 2017-12-16T15:36:21+00:00
Please let me know if you find a way to make it work through a proxy server. Just wonder any third party program can help the job.

## dreamlant | 2017-12-17T10:08:55+00:00
please add xmrig through socks proxy

## enwillyado | 2018-01-14T21:07:52+00:00
I have implemented afunction to allow _parent proxy_ (Outbound over "CONNECT" command of HTTP) in the "xmrig-proxy" project. It works! Would someone be interested to see it?

## 2010phenix | 2018-01-17T13:53:28+00:00
enwillyado, yes Thx.

## enwillyado | 2018-01-18T21:55:30+00:00
@2010phenix See the poll request. @xmrig, this funtionality is already contained in the roadmap https://github.com/xmrig/xmrig/issues/106.

## direngley | 2018-04-09T04:48:08+00:00
plz. update HTTP/SOCKS proxy support #186

## moralrebuild | 2018-04-18T03:38:55+00:00
When can we have this functionality? 

## enwillyado | 2018-04-18T06:06:54+00:00
@moralrebuild @direngley You can use my last fork version: https://github.com/enwillyado/xmrig/releases

# Action History
- Created by: ridera7 | 2017-11-03T15:33:55+00:00
- Closed at: 2018-11-05T07:01:14+00:00
