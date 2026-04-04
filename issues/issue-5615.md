---
title: 'Enhancement: Geographically spread out seed nodes'
source_url: https://github.com/monero-project/monero/issues/5615
author: sanderfoobar
assignees: []
labels: []
created_at: '2019-06-08T18:26:39+00:00'
updated_at: '2019-06-08T21:08:01+00:00'
type: issue
status: closed
closed_at: '2019-06-08T21:08:01+00:00'
---

# Original Description
'Core peers' (seed nodes) are the backbone of the Monero network. 

https://github.com/monero-project/monero/blob/ebb1c03e8cace02ebcc87c92f372e413a26c6406/src/p2p/net_node.inl#L467-L474

whois'ing to for country info:

```
dsc@fastbox:~# for line in 107.152.130.98 212.83.175.67 5.9.100.248 163.172.182.165 161.67.132.39 198.74.231.92 195.154.123.123 212.83.172.165; do echo "> $line" && whois "$line" | grep "country"; done

> 107.152.130.98
> 212.83.175.67
country:        FR
> 5.9.100.248
country:        DE
> 163.172.182.165
country:        FR
> 161.67.132.39
country:        ES
> 198.74.231.92
> 195.154.123.123
country:        FR
> 212.83.172.165
country:        FR
```

Currently they are all EU hosted which makes them unnecessarily more vulnerable to shutdown/raids (due to being in roughly the same jurisdiction), thereby posing a challenge from a risk management standpoint. 

I suggest one or more seed nodes to join the list that are hosted in Russia, Africa, middle east, Asia, etc.

In addition, these seed nodes should not be registered to just one person. I don't know the current situation, but if the hosting is all in fluffy's name... non-optimal situation.

# Discussion History
## umma08 | 2019-06-08T18:36:01+00:00
seed nodes are just full nodes that have opened their ports to the network to accept incoming connections, correct? 

by default is the port 18180?

edit. the port seems to be 18080

## sanderfoobar | 2019-06-08T18:41:12+00:00
> seed nodes are just full nodes that have opened their ports to the network to accept incoming connections, correct?
> 
> by default is the port 18180?

Seed nodes are essentially full nodes with 2 differences:

- Hosted and managed by the Monero core team.
- First 'point of contact' for people that are starting to sync and have not obtained any peer lists yet. A list of seed nodes is embedded/hardcoded inside `monerod`.

Other than above, they're regular full nodes that expose port `18080`.

## umma08 | 2019-06-08T18:49:19+00:00
> > seed nodes are just full nodes that have opened their ports to the network to accept incoming connections, correct?
> > by default is the port 18180?
> 
> Seed nodes are essentially full nodes with 2 differences:
> 
> * Hosted and managed by the Monero core team.
> * First 'point of contact' for people that are starting to sync and have not obtained any peer lists yet. A list of seed nodes is embedded/hardcoded inside `monerod`.
> 
> Other than above, they're regular full nodes that expose port `18080`.

ah i understand now. did not know this. thank you for explaining. 

## fluffypony | 2019-06-08T19:34:14+00:00
@xmrdsc they're not hosted by me. I have one in that list. I had an open call for trusted volunteers to run seed nodes a few years back. The list *will not change* at this juncture, especially as hard-coded seed nodes are rarely used and are the fallback. The primary seeding mechanism is DNS seeds, hard-coded seed nodes are what your node uses when it fails DNS resolution (unlikely).

## sanderfoobar | 2019-06-08T21:08:01+00:00
@fluffypony Oh I see. I miss-understood, thanks for clarification.

# Action History
- Created by: sanderfoobar | 2019-06-08T18:26:39+00:00
- Closed at: 2019-06-08T21:08:01+00:00
