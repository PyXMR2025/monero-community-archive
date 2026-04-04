---
title: On a bytecoin fork, seed nodes cannot be connected to
source_url: https://github.com/monero-project/monero/issues/226
author: xpbcreator
assignees: []
labels: []
created_at: '2015-02-16T20:57:05+00:00'
updated_at: '2015-02-16T21:11:09+00:00'
type: issue
status: closed
closed_at: '2015-02-16T21:02:25+00:00'
---

# Original Description
Hi Monero devs,

I'm the creator of [Pebblecoin](https://bitcointalk.org/index.php?topic=909624.0).  I have an issue with the hardcoded seed nodes and I was wondering if you have had any similar issues or could help point me to a fix.  As it is now, the 5 seed nodes cannot be connected to.  From the client side, I get timeouts: 

```
COMMAND_HANDSHAKE invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
```

I tried upping the timeout to 60 seconds yet it still times out.  From the seed node side, I get these potentially relevant error messages:

```
[sock 32] Some problems at write: Broken pipe:32
```

and

```
[P2P7]Failed to get remote endpoint: Transport endpoint is not connected:107
[P2P7]ERROR ../../contrib/epee/include/net/abstract_tcp_server2.inl:638 [sock 54] Failed to start connection, connections_count = 61
```

and

```
[P2P5]Failed to invoke command 1002 return code -3
[P2P5][69.60.113.27:52699 INC]COMMAND_TIMED_SYNC invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
```

Any idea what may be causing the issues?  I ask because I didn't change the networking code.  I added a new type of command, but that only comes in after the handshake process is done already.  The issue happens on any node that has more than a few connections to it.

Thanks,
xpbcreator


# Discussion History
## fluffypony | 2015-02-16T21:02:25+00:00
Closing this as not related to Monero, but we can still talk on this thread:)

I tried to connect to 69.60.113.27:52699 using netcat (well, ncat, but same diff) and it appeared to be inaccessible from here. Is it possible that your seed nodes are genuinely inaccessible because they aren't bound to 0.0.0.0 / their external IP? Or maybe a firewall is blocking some/all of them?


## xpbcreator | 2015-02-16T21:03:27+00:00
Thanks!  

That's a non-seed node and 52699 is an outgoing port - try connecting to 69.60.113.24:6180, which is a seed node on the P2P port.


## fluffypony | 2015-02-16T21:06:14+00:00
Ok that definitely works, so the port is open and accessible. Hmmmm. Did this stop working when you added your new type of command? Could be a bug in that, then, maybe not on the incoming side but on the outgoing side (I'm guessing, though)


## xpbcreator | 2015-02-16T21:08:57+00:00
The new command was there on release, and it was working fine at that point.  The issue came up more recently, without a change in the networking code.  It seems to be an issue only when more nodes are connected.  The bug was probably there from the start but it only manifested recently.  It could have to do with the new command but I doubt it at this point since the command is only relevant once the nodes are connected.  As it is now, the seed nodes for some reason are not completing the handshake.  If the monero devs have never experienced this then it probably is something I may have changed in the networking code.. 


## fluffypony | 2015-02-16T21:10:44+00:00
It's a tough one; because we have so many seed nodes (especially with DNS seeds) it's entirely possible that this has occurred before but hasn't been noticed/reported because it just steps to the next available node for seeds. Sorry I couldn't be more useful!


## xpbcreator | 2015-02-16T21:11:09+00:00
That's alright, thanks for taking the time!


# Action History
- Created by: xpbcreator | 2015-02-16T20:57:05+00:00
- Closed at: 2015-02-16T21:02:25+00:00
