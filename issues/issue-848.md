---
title: connections not limited to node specified in --add-exclusive-node
source_url: https://github.com/monero-project/monero/issues/848
author: radfish
assignees: []
labels: []
created_at: '2016-05-19T22:30:52+00:00'
updated_at: '2017-09-25T01:42:19+00:00'
type: issue
status: closed
closed_at: '2016-05-21T01:20:29+00:00'
---

# Original Description
The daemon connects to other nodes besides the exclusive one.

Also, tried with --hide-my-port: same behavior.
Also, tried rm p2pstate.bin, same behavior.

Expected behavior: there is only one connection made from or to bitmonerod when --add-exclusive-node is specified.


# Discussion History
## osensei | 2016-05-20T06:19:20+00:00
Currently, what --add-exclusive-node does is instruct the daemon to only make outgoing connections to the exclusive nodes. That doesn't prevent other peers from connecting to your node.

What --hide-my-port does is tell the daemon to not announce itself to other nodes as a peer candidate.

BUT.... if your node has previously announced itself to the network and you launch it with "--hide-my-port --add-exclusive-daemon xxx.xxx.xxx.xxx:18080" other peers will already know about your node and they may still try to connect to it (and succeed).

In this case, to accomplish the behavior you are expecting, you should run your node in a port that you haven't used before on your current IP, that is... using the parameter --p2p-bind-port. Or, if you are behind a NAT router, using --no-igd will prevent your router from automatically forwarding port 18080 to your node and that would be enough to prevent other nodes from connecting to you (as long as that port is not already forwarded on your router).

In summary, if other nodes know about the existence of your node, they may still connect to you despite using --add-exclusive-node, so what you need to do is to ensure no other node will reach yours.

EDIT TO ADD:

I'm not saying that this behavior is OK nor wrong. I'm just saying that's the way it works.

Edit again to add the complete example just for clarity:

```
./bitmonerod --hide-my-port --p2p-bind-port <new_port_never_used_before> --add-exclusive-node <ip:port> --no-igd
```

That should do the trick.

Aaanndddd... one more edit:
All that being said, I don't think it's polite to use exclusive nodes if you don't own them, as you would be generating around 3GB of traffic to that particular node when syncing from scratch, so please have that in mind.


## radfish | 2016-05-21T01:20:29+00:00
Thanks for the detailed explanation. This all makes sense.


## iamsmooth | 2017-09-25T01:36:42+00:00
This is an old issue which I just noticed but a better workaround than a new port (which could still in theory accept a connection if someone found it and firewall allowed) is `--p2p-bind-ip 127.0.0.1`. That makes it impossible for any outside connections since the p2p listener is bound to the loopback.



# Action History
- Created by: radfish | 2016-05-19T22:30:52+00:00
- Closed at: 2016-05-21T01:20:29+00:00
