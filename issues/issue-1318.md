---
title: Monero Research Lab Meeting - Wed 31 December 2025, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1318
author: Rucknium
assignees: []
labels: []
created_at: '2025-12-31T14:12:57+00:00'
updated_at: '2026-01-12T22:34:41+00:00'
type: issue
status: closed
closed_at: '2026-01-12T22:34:41+00:00'
---

# Original Description

Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Spy nodes](https://github.com/monero-project/meta/issues/1124).

4. Post-FCMP scaling concepts.

5. [FCMP alpha stressnet](https://monero.town/post/6763165).

6. Any other business

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1313 

# Discussion History
## Rucknium | 2026-01-06T21:24:24+00:00
Log

> __< rucknium >__ Meeting time! https://github.com/monero-project/meta/issues/1318     

> __< rucknium >__ 1. Greetings     

> __< vtnerd >__ Hi!     

> __< rbrunner >__ Hello     

> __< articmine >__ Hi     

> __< ArticMine >__ hi via IRC     

> __< rucknium >__ 2. Updates. What is everyone working on?     

> __< rucknium >__ me: Working on some updates to https://moneronet.info/ to properly display new spy node behavior.     

> __< rbrunner >__ In the middle of the biggest review I have ever done: sneedlewoods' switching `simplewallet` from directly using `wallet2` to using the Wallet API     

> __< articmine >__ I updated the scaling documents to fix the wallet scaling to 1.2 on the long-term median.     

> __< articmine >__ Also attended the 39c3      

> __< rbrunner >__ Oh!     

> __< vtnerd >__ Me: debugging an otherwise finished fcmp++ tx construction in lwsf     

> __< rucknium >__ 3. Spy nodes (https://github.com/monero-project/meta/issues/1124).     

> __< rucknium >__ I have been working on a few improvements to https://moneronet.info/ . In the current version, a node is only counted as spy if it behaves like a spy node in the daily scan. But I want to change that to also include nodes on the (new) MRL ban list. There are many spy nodes on Hetzner and Digital Ocean that stopped having the spy node fingerprint, but are probably still spy nodes.     

> __< rucknium >__ The webapp is showing a decline in the number of honest nodes, but I think it's a false reading.     

> __< rbrunner >__ What's your theory how you get it wrong now?     

> __< rucknium >__ I think a problem with database locking.     

> __< rbrunner >__ So just some problem inside your app?     

> __< rucknium >__ I don't know why it's causing a noticeable problem now and not before.     

> __< rucknium >__ Yes. I think so. I ran boog900:monero.social 's simpler scanner and it picked up the expected, larger, number of nodes.     

> __< rbrunner >__ No visible decline because of the holidays? I would expect at least some decline.     

> __< rucknium >__ My scanner also saves peer lists and I think everything else a node sends when it reponds to a Levin handshake.     

> __< rucknium >__ So I need a database for it instead of just writing to a flat file like the original scanner did.     

> __< rucknium >__ Well, that trend, if it exists, is the victim of lost data 😬     

> __< rucknium >__ I want to have this ready for a social media announcement of the new version of the MRL ban list next week.     

> __< rucknium >__ IMHO, not a good idea to announce it during this week.     

> __< rbrunner >__ Yes, too quiet     

> __< rucknium >__ I plan to have two lines for the count of the nodes that have the MRL ban list. One for version 1 and one for version 2.     

> __< articmine >__ Yes very quiet      

> __< rucknium >__ selsta also asked rbrunner and me if we think the ASmap is worth deploying: https://github.com/monero-project/monero/pull/7935#issuecomment-3666660926     

> __< rucknium >__ I plan to reply no because subnets are much less risky to use as a basis for selecting peers.     

> __< rbrunner >__ No idea about that "ASmap" stuff, never looked into it     

> __< rucknium >__ Subnets always have the same number of possible IP addresses. ASNs do not.     

> __< rucknium >__ ASNs are more easily manipulated by adversaries. According to boog900:monero.social , the ASN that the spy nodes are now using, instead of LionLink, is only one year old. Nodes would have to constantly update the ASN database or they would be victimized by such an adversary, IMHO.     

> __< rbrunner >__ Some easy automated lookup is not possible, or at least complicated?     

> __< rucknium >__ I have a game theory model that shows pretty rigorously the conditions where having subnet deduplication is better than not having it. It's based on knowing the subnet size, i.e. number of IP addresses in eash. ASN size can be tiny or huge.     

> __< rbrunner >__ Anyway, it would probably complicate things even more, for unclear gain, or hard-to-prove gain     

> __< rucknium >__ Game theory models don't map perfectly onto reality, of course, but at least it does inform about worst case scenarios IMHO.     

> __< vtnerd >__ generating the map is automated but is reliant on your view of the ip peering protocols     

> __< rucknium >__ Game theory model is here: https://github.com/Rucknium/misc-research/blob/main/Monero-Peer-Subnet-Deduplication/pdf/monero-peer-subnet-deduplication.pdf     

> __< vtnerd >__ https://asmap.org/sourcing-data/     

> __< rucknium >__ Not very complicated IMHO. Two-player  zero-sum game with two possible pure strategies each.     

> __< vtnerd >__ I’ve never liked it because the db changes how the connections work, and the db itself is hard to review     

> __< rucknium >__ Isn't the proposed BTC implementation a static database that ships with the node binary?     

> __< vtnerd >__ yes. its just that you’ve got to more or less trust how the db was made. or I guess you could review all of that generation code and then attempt to rebuild the db yourself     

> __< vtnerd >__ the process just seemed to opaque for more liking, but other people in btc seemed to disagree     

> __< rucknium >__ It's not merged in bitcoind yet, right?     

> __< rucknium >__ AFAIK, the purpose of the bitcoin implementation is a little different, or different emphasis. Their emphasis is anti-censorship and network resilience, not really privacy AFAIK.     

> __< rucknium >__ Anything more on spy nodes?     

> __< vtnerd >__ not sure of the merge status, looks like some portion of it may have been merged (the code but not the db)     

> __< rucknium >__ Is preland:monero.social  here?     

> __< vtnerd >__ yes they are more concerned with eclipse attacks, etc     

> __< rbrunner >__ Much more money involved. Imagine you could cut of some important miner, for even a few hours ...     

> __< rucknium >__ I will skip the "Post-FCMP scaling concepts" item this meeting since preland isn't here.     

> __< rucknium >__ 5. FCMP alpha stressnet (https://monero.town/post/6763165).     

> __< rucknium >__ Bugs are still being reported and squashed     

> __< rbrunner >__ Running already for 3 months, if the date of the post is correct. Time flies.     

> __< rucknium >__ This alpha stressnet has continued longer than I expected, but it's continuing to be useful     

> __< articmine >__ How big is the block weight?     

> __< rucknium >__ I remember telling untraceable:monero.social   that the stressnet blockchain would go to about 50GB. I don't know how big an unpruned node is now since I pruned all my nodes. But it's above 150GB AFAIK :D     

> __< rbrunner >__ Uh, and just now SSDs prices will probably explode :)     

> __< articmine >__ What about ML?     

> __< articmine >__ MP?     

> __< DataHoarder >__ due to orphan forks the long term weight wasn't increased that much afaik     

> __< DataHoarder >__ and stuff breaking down after 15-18 MiB and nodes falling out of sync -> making their own empty blocks, then merging later down the line     

> __< articmine >__ Sorry MN the former MS      

> __< articmine >__ So MN resets     

> __< rucknium >__ I will try a get_info query to see if the long-term median has increased yet.     

> __< articmine >__ It takes over 2 months      

> __< articmine >__ To change MaL     

> __< articmine >__ ML*     

> __< rucknium >__ Anything more on stressnet?     

> __< rucknium >__ We can end the meeting here. Thanks everyone.     

> __< articmine >__ Thanks      

> __< rbrunner >__ There won't be any better meeting this year still, ever :)     

> __< rucknium >__ This one lasted only 50 minutes. That's a good meeting ;)     

> __< articmine >__ Well my first meeting from an airplane, over northern Canada      

> __< DataHoarder >__ I won't be able to attend any further meetings until next year     

> __< rucknium >__ Can you sync 1GB blocks from that airplane yet? Hahaha     

> __< articmine >__ I did sync the Monero blockchain      

> __< rbrunner >__ Well, some of them use StarLink now, and if not too many people on board use the connection, I think speed is pretty decent     

> __< bikrambiswas:matrix.org >__ Can I Download it ? Is it safe ? Just asking > <niyid:matrix.org> Hi everyone 👋     

> __< rbrunner7 >__ Well, Google still gives a download count of 0. Might be nobody downloaded to actually test. Zero downloads after a few days for a new wallet is brutal, but it is like it is ...     



# Action History
- Created by: Rucknium | 2025-12-31T14:12:57+00:00
- Closed at: 2026-01-12T22:34:41+00:00
