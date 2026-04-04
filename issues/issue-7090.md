---
title: Per-AS connection limit
source_url: https://github.com/monero-project/monero/issues/7090
author: keffnet
assignees: []
labels: []
created_at: '2020-12-07T05:36:59+00:00'
updated_at: '2023-09-02T12:18:04+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
When spinning up my monerod I get these 26 connections split between inc/out.

OVH - 22
Suddenlink - 1
Digitalocean - 1
Centurylink - 1
Contabo - 1

This is very disconcerting for me. 85% of nodes on my newly spun up monerod is behind OVH. 
For all I know it's all run by the same entity. One can also assume that there's a high probably of there being 
hundreds of nodes behind OVH if I randomly got 22 instantly.

Has there been any thoughts of implementing the same per-AS limit that now exists in Bitcoin Core?

Even if I don't think many node operators are using it it's a good way of spreading connections among ISPs in a world where
I can spin up a vps with 100 ips for like $25. And it would be really easy to implement.




# Discussion History
## moneromooo-monero | 2020-12-07T15:30:55+00:00
Yes. Patches welcome.

## keffnet | 2020-12-07T16:52:00+00:00
Why did i know you were going to answer like this :D ok. Patch incoming.

## selsta | 2020-12-07T17:09:50+00:00
FYI, there is a list of known malicious peers, mostly hosted on OVH: https://gui.xmr.pm/files/block.txt

You can apply the list as a ban list using `--ban-list /path/to/block`, v0.17.1.6 also has some improvements against them.

Per-AS connection limit would still be nice in the future.

## keffnet | 2020-12-07T17:30:23+00:00
> FYI, there is a list of known malicious peers, mostly hosted on OVH: https://gui.xmr.pm/files/block.txt
> 
> You can apply the list as a ban list using `--ban-list /path/to/block`, v0.17.1.6 also has some improvements against them.
> 
> Per-AS connection limit would still be nice in the future.

I just blocked all ovh. But it's still a bad workaround. Will send a asn-limit patch soon.

## moneromooo-monero | 2020-12-07T17:34:36+00:00
Note that there's currently a preference for peers not in the same /16 range. It would be nice to use the system, so you end up still connecting to the same AS if there are no other peers (ie, testing).

## keffnet | 2020-12-07T18:14:06+00:00
That would only occur in testnet? Since 1 peer per AS should be enough in normal scenarios. Bitcoins /16 limit (i assume monero inherited) was flawed from the beginning. Most likely it was used since it required no external sources to separete isps. But it's bad to use it today.

## vtnerd | 2020-12-07T18:26:25+00:00
@shyrwall what is the technique you plan to use? This isn't as trivial as /16 lookup because it should require some external database. This is primarily why I stopped cold after looking into it - I wasn't sure how someone could independently verify the information.

The experimental Bitcoin Core method is even worse with regards to verification. They are trying to identify every AS that a connection flows through to select peers. It helps with eclipse and mitm attacks, but its based on this database of routing information that some external authority publishes.

## keffnet | 2020-12-07T18:29:46+00:00
2 solutions. One is to dump the prefixes from the RIR dbs. Or to dump from the real bgp table. I will do the last since its reality.

Ofc this means it will have to be updated regularly but thats a non issue since it will be so much better than a dumb /16 drop.

## moneromooo-monero | 2020-12-30T21:34:46+00:00
Any chance you might have started looking at this yet ? :)

## moneromooo-monero | 2021-01-09T20:12:41+00:00
pingy pingitty ping, that would be a really nice patch ^_^


## keffnet | 2021-01-10T10:21:39+00:00
Hi

Sorry. Just came back from NY holiday. I'll try to have time to look at it again. I just plan on trying to copy Bitcoin Cores code since they have a good ""compression"" algo for the as table.

But keep in mind i'm CPP illiterate. Someone else can probably knock this out in a few hours :P

## moneromooo-monero | 2021-01-10T15:38:06+00:00
Ah. Well, I'm C++ literate but BGP illiterate :D Is the bitcoin core code under a suitable licence as a first prerequisite ?

## jonathancross | 2021-01-28T17:19:54+00:00
Friendly ping @shyrwall 

## keffnet | 2021-01-28T20:10:26+00:00
> 
> 
> Friendly ping @shyrwall

I discussed it with moneromoo on irc. I can assist with the part of getting the AS,IP data since i'm a networking guy but learning the code would take too much time since i suck at C :)

## moneromooo-monero | 2021-01-30T21:06:13+00:00
I think if you can get me a data structure with information on what it means, I can do the rest.

## keffnet | 2021-01-31T03:32:03+00:00
I assume your C-eyes can see the structure from,

https://github.com/bitcoin/bitcoin/blob/master/src/util/asmap.cpp
https://github.com/bitcoin/bitcoin/pull/16702/commits/ec45646de9e62b3d42c85716bfeb06d8f2b507dc
https://github.com/sipa/bitcoin/blob/202004_asmap_tool/src/bitcoin-asmap.cpp

The best way to generate the file I guess can be discussed later. I got an example at https://github.com/shyrwall/asmap .
Resulting file is currently about 1.1MB.



## plowsof | 2023-09-02T12:15:35+00:00
A bounty for this issue has been created by ydvim (currently at 1.21 XMR) https://bounties.monero.social/posts/93

PR that needs review / closes this issue #7935

# Action History
- Created by: keffnet | 2020-12-07T05:36:59+00:00
