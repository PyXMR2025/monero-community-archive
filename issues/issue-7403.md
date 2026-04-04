---
title: outgoing RPC bandwidth drops after a while, node becomes unconnectable via
  RPC
source_url: https://github.com/monero-project/monero/issues/7403
author: Gingeropolous
assignees: []
labels: []
created_at: '2021-02-26T03:37:25+00:00'
updated_at: '2021-04-01T02:47:01+00:00'
type: issue
status: closed
closed_at: '2021-03-31T03:15:16+00:00'
---

# Original Description
I've noticed this with my high load public RPC servers. I monitor bandwidth with nload. Basically, when I start monerod, the outgoing bandwidth is high - for instance, right now I'm seeing ~100 Mbits / sec, and right now I have 53 RPC connections which I check with netstat -anp |grep 18089 |wc -l

 If it runs long enough, eventually nload will report that my outgoing bandwidth is maybe 200 kbits / second, and usually when this happens the RPC connection count is up to 100+. 

In these cases, when I restart monerod, the outgoing shoots right back on up to 100 Mbits / second.

I've also noticed that in these cases, if I try to connect to the node, my GUI can't make a connection. But once i restart the node, the GUI can connect. 

I've "solving" the problem currently with a cronjob, but... yeah. 

# Discussion History
## Gingeropolous | 2021-03-31T03:15:15+00:00
was the same thing as #7482 

issue resolves by disabling rpc-ssl, so bug probably in that.  



## vtnerd | 2021-03-31T13:21:30+00:00
This seems like another issue entirely. SSL uses additional CPU load, so I wonder if this box is hitting that limit. Part of the issue will be CPU cache being hit much harder, causing a slowdown in everything.

An argument for max number of RPC clients may need to be added.

## hyc | 2021-03-31T17:55:52+00:00
Agreed, a setting for max number of RPC clients has been needed anyway, just to control server load.

## Gingeropolous | 2021-04-01T02:47:01+00:00
@vtnerd , 
> This seems like another issue entirely. SSL uses additional CPU load, so I wonder if this box is hitting that limit. 

The box is a 48 thread epyc with 64 GB ram, so I would hope thats not the case. Granted, its mining in the background with nice 19 , but i'm not sure if the other node operators that experienced this issue are *also* mining. And granted, I haven't tested if disabling mining makes the phenomenon go away. 

I'm pretty sure its the same issue as the SSL thing. When I posted this issue, I hadn't really started to dive into the problem. It's only when I started diving into the netstat output did I notice the CLOSE_WAIT state. 

but yeah, a max number of RPC clients would be good. Would be nice if the wallet / daemon had a handshake or whatever where if the daemon says it can't handle it, to get the wallet to re-request information from the DNS entry or whatever. I guess just initiate a new connection. 

# Action History
- Created by: Gingeropolous | 2021-02-26T03:37:25+00:00
- Closed at: 2021-03-31T03:15:16+00:00
