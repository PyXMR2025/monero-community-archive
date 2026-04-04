---
title: '[Idea] Lessening privacy leak when using public node by using multiple nodes'
source_url: https://github.com/monero-project/monero/issues/1524
author: kenshi84
assignees: []
labels: []
created_at: '2017-01-04T11:24:00+00:00'
updated_at: '2017-01-04T13:23:14+00:00'
type: issue
status: closed
closed_at: '2017-01-04T13:23:14+00:00'
---

# Original Description
As I understand it, when using a remote public node, privacy leak happens in the following way: let's say I want to create one ring signature for the amount of 0.1 XMR with mixin of 4. My wallet has one unspent output key of 0.1 XMR, so I ask the public node to send me 4 other output keys of 0.1 XMR to mix with. By creating the ring signature consisting of 4+1=5 keys and submitting it to the network (regardless of which node to use for submission), the said public node will know which index in the ring is real by finding the very same 4 keys that it provided earlier.

My idea is to reduce the privacy leak by connecting to multiple independent public nodes and collect small bits of information from each of them. Specifically, in the above scenario, the wallet would connect to 4 different public nodes and ask for only one output key of 0.1 XMR each. Among 5 keys in the resulting ring signature, each used public node will know only one index that is fake, but won't be able to tell which index is real (assuming the nodes are really independent and not colluding together). Admittedly this might require more time connecting to multiple nodes than connecting to just one single node, but better privacy may be worth longer waiting for some users.

PS: Is this the right place to post this kind of open-ended ideas? Are other platforms (e.g. Reddit, StackExchange, forum.getmonero.org) better suited? Thanks!

# Discussion History
## Jaqueeee | 2017-01-04T11:53:16+00:00
I like the idea. It's somewhat related to an idea i had for the GUI, in particular the mobile version of it. If we could provide an official list of remote nodes, the wallet could choose one or multiple random nodes every time. This would further improve the privacy and also improve performance and load balancing compared to the today existing round-robin dns solution. Rouge and unreachable nodes could automatically be removed from the list and they could also be sorted by continent or similar.

## moneromooo-monero | 2017-01-04T12:10:00+00:00
The wallet now asks for all the outputs it needs, including the one the wallet owns.

This system might be useful for other things though.

## kenshi84 | 2017-01-04T12:14:29+00:00
@moneromooo-monero Aha, I didn't know that, and such a simple solution! I'm embarrassed :)
So, is there still privacy leak with the current method, or is it as private as running one's own node?

## Jaqueeee | 2017-01-04T12:31:54+00:00
The daemon still knows that one of the outputs is yours. With high mixin the privacy leak is minimal as far as i can tell. 
@kenshi84 more info here:
http://monero.stackexchange.com/a/84/736


## moneromooo-monero | 2017-01-04T12:39:09+00:00
The daemon always knows one of the inputs in a ring is the one that's being spent, if the signature checks out. Unless you're talking about mapping IP address to tx ? In which case it doesn't matter where/how you got the  fake outs (unless you're saying make the daemon believe you're just relaying it, but that'll be fixed by kovri).

## kenshi84 | 2017-01-04T13:23:13+00:00
Thank you for answering! Closing.

# Action History
- Created by: kenshi84 | 2017-01-04T11:24:00+00:00
- Closed at: 2017-01-04T13:23:14+00:00
