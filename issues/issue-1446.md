---
title: 'Monero Community Workgroup Meeting: Sat, 2026-08-22 16:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1446
author: nahuhh
assignees: []
labels: []
created_at: '2026-08-21T16:22:49+00:00'
updated_at: '2026-08-22T20:30:01+00:00'
type: issue
status: closed
closed_at: '2026-08-22T20:30:01+00:00'
---

# Original Description
Location: [Libera.chat, #monero-community](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-community:monero.social?via=matrix.org&via=monero.social)

[Instructions for joining the monero.social Matrix server.](https://www.getmonero.org/resources/user-guides/join-monero-matrix.html)

Time
16:00 UTC [Check your timezone](https://www.timeanddate.com/worldclock/converter.html)

Moderator: ofrnxmr

Please reach out in advance of the meeting if you would like to propose an agenda item.


Proposed Meeting Items:

1. Introduction
2. Greetings
3. Community highlights    
News: [Monero Observer](https://monero.observer)
4. CCS proposals  
  a. [MRL] Dennis Trautwein - [ProbeLab P2P Network Metrics Proposal](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/667)    
  b. acx - [part-time monfluo](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/690)  
  c. panagot12 [Monero LWS Observatory — Public LWS Health](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/686)  
  d. Boog900 - [Cuprate FCMP++ support](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/691)  
  e. v1docq47 - [monero konferenco 2026 voice-over and working on xmr.ru](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/683)  
  f. r4v3r23 - [ANONERO Continued development](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/671)  
5. Workgroup reports    
  a. Dev workgroup  
  b. Localization workgroup  
  c. Outreach workgroup  
  d. Events workgroup  
  e. Website workgroup  
  f. Policy workgroup  
  g. Research workgroup  
  h. [FCMP++ stressnet](https://github.com/seraphis-migration)
6. Open ideas time    
7. Confirm next meeting date/time    

[Previous meeting including logs](https://github.com/monero-project/meta/issues/1439)

# Discussion History
## nahuhh | 2026-08-22T20:29:16+00:00
Logs 
    
> **\<ofrnxmr\>** Meeting time: https://github.com/monero-project/meta/issues/1446     
    
> **\<hbs:matrix.org\>** Hello     
    
> **\<slowbeardigger:matrix.org\>** Hello hello     
    
> **\<boog900\>** Hi     
    
> **\<jpk68:matrix.org\>** Hello     
    
> **\<ofrnxmr\>** lets get into the community highlights     
    
> **\<ofrnxmr\>** https://monero.observer is back     
    
> **\<plowsof\>** welcome back escaprethe3ra     
    
> **\<ofrnxmr\>** multiple gpu wallet scanners in the wild, able to scan the chain from a local or precomputed cache in seconds     
    
> **\<plowsof\>** escapethe3ra*     
    
> **\<hbs:matrix.org\>** Published two videos explaining how MoneroSwap works     
    
> **\<ofrnxmr:xmr.mx\>** #moneroswap:matrix.org     
    
> **\<ofrnxmr\>** nothing else exciting going on?     
    
> **\<ofrnxmr\>** serai had another audit completed     
    
> **\<ofrnxmr\>** jberman reports that the phase 1 audit is completed, and all items related to it have been reviewed and merged into monero master     
    
> **\<ofrnxmr\>** phase of of the integration audit*     
    
> **\<ofrnxmr\>** ok, lets get into the CCS proposals     
    
> **\<ofrnxmr\>** note that ccs.getmonero.org is broken atm. ideas page shows nothing and funding page isnt updating     
    
> **\<ofrnxmr\>** should hopefully be back up in a few days. I'm not sure which part of the stack is broken, but iiuc ccs.getmonero.org is on a separate box than repo.getmonero.org     
    
> **\<ofrnxmr\>** repo was updated a few days ago, and seems ccs went haywire at that time, so maybe ccs just needs some services restarted - but i have no idea     
    
> **\<ofrnxmr\>** a. [MRL] Dennis Trautwein - ProbeLab P2P Network Metrics Proposal https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/667     
    
> **\<ofrnxmr\>** Dennis left a new comment https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/667#note_37195     
    
> **\<ofrnxmr\>** "I see this proposal has been stuck here. What needs to happen in order to merge this and move the proposal from "Ideas" to "Fundraising"? Is there any sticking point, given it moved off of MRL? Let us know how we can be of help to move things forward."     
    
> **\<ofrnxmr:xmr.mx\>** (jokes on him - its not on the ideas page anymore :D hha jkjk)     
    
> **\<slowbeardigger:matrix.org\>** lol     
    
> **\<plowsof\>** the volunteer said they would be able to check this weekend what went wrong on the ccs , not heard from them yet     
    
> **\<ofrnxmr\>** i spoke to them and they said they would be unavailable     
    
> **\<ofrnxmr\>** but they dont have access to the ccs box, just repo afaik     
    
> **\<ofrnxmr\>** ccs is diego box     
    
> **\<ofrnxmr\>** so its possible that the issue isnt on repo (iiuc..)     
    
> **\<diego:cypherstack.com\>** is it?     
    
> **\<ofrnxmr\>** ya     
    
> **\<ofrnxmr\>** thats what pigeons said some time ago     
    
> **\<plowsof\>** ive told CS to hold back in case its a gitlab issue that will be resolved this weekend     
    
> **\<plowsof\>** that helps knowing it wont be resolved this weekend     
    
> **\<ofrnxmr\>** still worth looking at ccs if some service there is just stuck     
    
> **\<plowsof\>** a restart will fix it as my mirror runs fine with the current gitlab     
    
> **\<plowsof\>** my concern was restart and then someting is done again today , but nvm     
    
> **\<ofrnxmr\>** thats what i mean - if gitlab isfi ne, then the issue is probably something stuck on ccs     
    
> **\<jpk68:matrix.org\>** Can there not be, like, a scheduled cron job to restart the server?     
    
> **\<ofrnxmr\>** but yeah, the update of repo isnt done, so probably more hiccups to go     
    
> **\<ofrnxmr:xmr.mx\>** jpk, we only restart during a power failure (thats what i do)     
    
> **\<plowsof\>** all signs point to lack of timeouts inside a try/catch i added that solved another problem, but i have to see it break first     
    
> **\<ofrnxmr:xmr.mx\>** cant see it break if its already broken :P     
    
> **\<plowsof\>** fix it then break it again :D     
    
> **\<ofrnxmr:xmr.mx\>** anyway, id ask that diego / cs check the ccs website to see if its on their end     
    
> **\<ofrnxmr:xmr.mx\>** if it breaks again, we can watch it     
    
> **\<ofrnxmr:xmr.mx\>** but for now, funding and ideas is fkd up     
    
> **\<slowbeardigger:matrix.org\>** So, what do we think of the ProbeLab CCS proposal?     
    
> **\<ofrnxmr:xmr.mx\>** i dont have much of an opinion on it, but i dont think the data is overly helpful     
    
> **\<slowbeardigger:matrix.org\>** -1     
    
> **\<ofrnxmr:xmr.mx\>** there have been past studies done showing that there are large nodes (1000+ connections) that essentially handle 80% of the network traffic. i dont think it takes too much work to figure that out     
    
> **\<slowbeardigger:matrix.org\>** no bueno     
    
> **\<ofrnxmr:xmr.mx\>** you have monero.fail doing reverse lookups across the whole network to discover every node monero.fail/map     
    
> **\<ofrnxmr:xmr.mx\>** i dont know what such data buys us, it seems more informative     
    
> **\<ofrnxmr:xmr.mx\>** and again, i feel like its just funding blockchain surveillance. but hey, that all just my opinion     
    
> **\<slowbeardigger:matrix.org\>** It does feel that way     
    
> **\<yiannisbot:matrix.org\>** Hi folks, Yiannis from ProveLab here to answer questions and see if this can move forward.     
    
> **\<slowbeardigger:matrix.org\>** Hello     
    
> **\<ravfx:xmr.mx\>** -1     
    
> **\<yiannisbot:matrix.org\>** We want the study to be as helpful and valuable as possible for the community. We gathered feedback that indeed it is going to be. But we’ve also asked several times if there’s something we should add to make it more impactful.     
    
> **\<ofrnxmr:xmr.mx\>** > A report about metrics on unreachable nodes in the Monero network published on ProbeLab’s blog. The report will include the outcome of our research study and will include heuristics that make better judgements of whether a node is a spy node or not. If budget allows we will also collect these metrics continuously and have them live on probelab.io.     
    
> **\<ofrnxmr:xmr.mx\>** im not sure knowing whether a node is a spy is ultimately helpful. as discoveries are made, they can jsut change their behavior     
    
> **\<slowbeardigger:matrix.org\>** @ofrnxmr:xmr.mx: x2     
    
> **\<ofrnxmr:xmr.mx\>** so the way a user runs a node should simply be defensive - to always assume that every peer is malicious     
    
> **\<yiannisbot:matrix.org\>** The point of the study is to try and identify better heuristics to identify spy nodes and also make it harder for spy nodes to exist in the network.     
    
> **\<ofrnxmr:xmr.mx\>** the latter doesnt seem possible     
    
> **\<ofrnxmr:xmr.mx\>** the same spynodes on monero exist on i2p, bitcoin, etc     
    
> **\<slowbeardigger:matrix.org\>** I am not convinced this proposal should be funded…     
    
> **\<slowbeardigger:matrix.org\>** the core issue isn’t just the cost or the closed source nature of Nebula…     
    
> **\<slowbeardigger:matrix.org\>** it is that the fundamental activity ProbeLab is proposing, a large scale crawling of the Monero p2p network,  is itself the same class of activity that spy nodes perform[... more lines follow, see https://mrelay.p2pool.observer/e/l8janqMLbF9HRUFt ]     
    
> **\<ravfx:xmr.mx\>** The more we detect the more they will evolve to evade detection     
    
> **\<jpk68:matrix.org\>** I would say -1 from me as well, especially considering the work is not fully FOSS     
    
> **\<ofrnxmr:xmr.mx\>** like, we know that large quantity of nodes on btc, i2p, and monero are spy nodes, yet the only "solutions" for any of them are blocking, asmap, reducing clusters     
    
> **\<yiannisbot:matrix.org\>** Regarding the closed source: we’ve revised the proposal and this was amended.     
    
> **\<jpk68:matrix.org\>** IMO, something more useful would be looking into actual mitigations, such as an ASmap like Bitcoin Core uses, or preventing heuristic leakage through anonymity networks.     
    
> **\<ofrnxmr:xmr.mx\>** or improving block sync throughput and sybil resistance on anonymity networks     
    
> **\<ofrnxmr:xmr.mx\>** but these things dont require monitoring the adversaries, they defend against all adversaries     
    
> **\<ofrnxmr:xmr.mx\>** so it would make it not realistic for spied to participate at all, since they cant learn anything     
    
> **\<yiannisbot:matrix.org\>** Ok, that’s useful. I’m wondering why such suggestions come several months after the proposal was submitted.     
    
> **\<yiannisbot:matrix.org\>** If you can add these comments in the proposal itself, we can continue the discussion and see if we have a methodology to propose that would make it valuable.     
    
> **\<ofrnxmr:xmr.mx\>** some more interesting proposals need more interesting input. we can apologize for not having better ideas earlier, but its not easy to think of what to do     
    
> **\<yiannisbot:matrix.org\>** Otherwise messages just get lost in this channel.     
    
> **\<boog900\>** I think I did say something like that in the monero labs meetings IIRC     
    
> **\<ofrnxmr:xmr.mx\>** ok, 10mins left, lets get to the other propsals quickly     
    
> **\<ofrnxmr:xmr.mx\>** again, note that the website isnt working so funding isnt working atm     
    
> **\<jpk68:matrix.org\>** @boog900: Yes, myself as well.     
    
> **\<ofrnxmr\>** b. acx - part-time monfluo https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/690     
    
> **\<ofrnxmr\>** @plowsof is this in merge queue?     
    
> **\<jpk68:matrix.org\>** Easy +1     
    
> **\<slowbeardigger:matrix.org\>** +1     
    
> **\<ravfx:xmr.mx\>** +1     
    
> **\<ofrnxmr\>** c. panagot12 Monero LWS Observatory — Public LWS Health https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/686     
    
> **\<yiannisbot:matrix.org\>** In all, I’m hearing that there’s limited interest for the proposal. We’ll leave it to that from our side and let us know if appetite shifts. We’ll also dive a little more on Dandelion+ to see any space for optimization there.     
    
> **\<jpk68:matrix.org\>** ofrnxmr: -1     
    
> **\<ravfx:xmr.mx\>** -1     
    
> **\<slowbeardigger:matrix.org\>** ofrnxmr: -1     
    
> **\<pw:xmr.mx\>** ofrnxmr: +1     
    
> **\<pw:xmr.mx\>** been having a nap     
    
> **\<ofrnxmr:xmr.mx\>** id -1 as well,if nothing else, because there arent many public lws servers atm     
    
> **\<ofrnxmr:xmr.mx\>** a kuno would probably do well here, also since this is vibe coded     
    
> **\<pw:xmr.mx\>** ofrnxmr: *     
    
> **\<plowsof\>** acx yes ofrnxmr     
    
> **\<ofrnxmr:xmr.mx\>** d. Boog900 - Cuprate FCMP++ support https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/691     
    
> **\<pw:xmr.mx\>** +1     
    
> **\<ravfx:xmr.mx\>** +1     
    
> **\<slowbeardigger:matrix.org\>** +1     
    
> **\<ofrnxmr\>** e. v1docq47 - monero konferenco 2026 voice-over and working on xmr.ru https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/683     
    
> **\<pw:xmr.mx\>** -1 not urgent     
    
> **\<slowbeardigger:matrix.org\>** -1     
    
> **\<ravfx:xmr.mx\>** -1     
    
> **\<ofrnxmr:xmr.mx\>** racists     
    
> **\<ofrnxmr:xmr.mx\>** i thought this was a "merge, but not right now" :D hah     
    
> **\<ofrnxmr:xmr.mx\>** v1docq47 has been funded for all of his prior proposals (except 1) and has been doing this work for years. i wouldnt want to merge during a slow-funding period, but im not against merging it since the audience is entirely different than our usual     
    
> **\<ofrnxmr:xmr.mx\>** so my person vote is "postpone"     
    
> **\<ofrnxmr:xmr.mx\>** personal*     
    
> **\<ofrnxmr:xmr.mx\>** (not close)     
    
> **\<slowbeardigger:matrix.org\>** +1 to postpone     
    
> **\<pw:xmr.mx\>** well could always hold off i guess, ya     
    
> **\<ofrnxmr\>** f. r4v3r23 - ANONERO Continued development https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/671     
    
> **\<pw:xmr.mx\>** repo page is no longer loading for me.     
    
> **\<pw:xmr.mx\>** has any milestones been met yet or does it still seem like a bit.of a mess     
    
> **\<ravfx:xmr.mx\>** +1     
    
> **\<pw:xmr.mx\>** in regards to F – anonero     
    
> **\<ofrnxmr:xmr.mx\>** patchwork, milestones for anonero? no     
    
> **\<slowbeardigger:matrix.org\>** Shall we postpone this one as well?     
    
> **\<slowbeardigger:matrix.org\>** there are some points that haven’t been clarified     
    
> **\<ofrnxmr:xmr.mx\>** their repo loads for me     
    
> **\<ofrnxmr:xmr.mx\>** http://git.anonero5wmhraxqsvzq2ncgptq6gq45qoto6fnkfwughfl4gbt44swad.onion/ANONERO/ANONERO/commits/branch/main     
    
> **\<slowbeardigger:matrix.org\>** @ofrnxmr:xmr.mx: took me a few secs but it did     
    
> **\<pw:xmr.mx\>** everything just seemed to have gone tits up since a couple meetings ago and time scales were reduced, adding pressure to r4v3r23/anonero     
    
> **\<ofrnxmr:xmr.mx\>** there have been more comments in both directions since the last meeting     
    
> **\<pw:xmr.mx\>** after the last meeting r4v3r managed to pop in and replied 'devs are ready'     
    
> **\<pw:xmr.mx\>** any progress made since then?     
    
> **\<pw:xmr.mx\>** I'm not against anonero but it seems all over the place     
    
> **\<ofrnxmr:xmr.mx\>** well, the only updates on the app have been translations, so idk whats going on     
    
> **\<pw:xmr.mx\>** would be fantastic to see progress  and peoples suggestions taken on board for taking it further, rather then be shot down and dismissed.     
    
> **\<ravfx:xmr.mx\>** Oh, that update, been a while     
    
> **\<pw:xmr.mx\>** + pospone     
    
> **\<slowbeardigger:matrix.org\>** +1 postpone until things get clear     
    
> **\<plowsof\>** we dont care about seeing concepts for the new ui right? example: new CCS ui , we expected to see mockups     
    
> **\<plowsof\>** the milestones have been planned and decided - jut need funding now     
    
> **\<pw:xmr.mx\>** he shouldn't of reduced the time scales adding pressure to himself/dev and not deliver in those reduced times.     
    
> **\<ravfx:xmr.mx\>** Imo ui is fine. Just fix the bug and add a network killswitch on anon     
    
> **\<plowsof\>** ravfx new ui is the first milestone     
    
> **\<ofrnxmr:xmr.mx\>** network kill switch isnt in the milestones, but i personally think the way the apps are is mixed up     
    
> **\<slowbeardigger:matrix.org\>** “Milestone 1: New UI (23.1725 XMR)”     
    
> **\<ofrnxmr:xmr.mx\>** both of the apps are online - nero = view only, anon = signing and spend     
    
> **\<ravfx:xmr.mx\>** Yeah, reverse anon and nero, would make more sence     
    
> **\<ofrnxmr:xmr.mx\>** anon should be online view and spend, nero should be offline sign only     
    
> **\<pw:xmr.mx\>** plowsof: I still say +1 to postpone, till see things moving further.     
    
> **\<pw:xmr.mx\>** no offence intended. it would be great to see anonero flying     
    
> **\<ofrnxmr:xmr.mx\>** ok, what are we waiting for with the postpone?     
    
> **\<ofrnxmr:xmr.mx\>** what do we want answered or to see before merge?     
    
> **\<ofrnxmr:xmr.mx\>** mockup for ui? bugs being fixed / activity on repo from dev? prs from contributors instead of patches being submit and git author credit taken by anonero account?     
    
> **\<pw:xmr.mx\>** peoples bug reporting like @ravfx:xmr.mx findings,  being taken on board - rather then him being shot down and called a clown     
    
> **\<pw:xmr.mx\>** @ofrnxmr:xmr.mx: all of the above IMO     
    
> **\<ofrnxmr:xmr.mx\>** http://git.anonero5wmhraxqsvzq2ncgptq6gq45qoto6fnkfwughfl4gbt44swad.onion/ANONERO/ANONERO/commit/2ae2f0fdbfa51f3565f7db4d532f5c9ec856f8f7 example - this was done by @udenix:4d2.org  but author is anonero     
    
> **\<plowsof\>** plenty of bugs have been identified     
    
> **\<pw:xmr.mx\>** I've noticed peoples bug findings just being met with hostility, attitude and denial     
    
> **\<plowsof\>** would be nice for udenix to explain why he didnt spot the 3+ year old dependencies in the wallet after contirbuting for months     
    
> **\<ofrnxmr:xmr.mx\>** UDENIX was contributing for months? how can you tell :D     
    
> **\<plowsof\>** raver said anyone who built from source would get them - which is wrong , provably     
    
> **\<pw:xmr.mx\>** I'm all for it succeeding BTW.     
    
> **\<plowsof\>** udenix is the kotlin dev?     
    
> **\<ofrnxmr:xmr.mx\>** i thought he was jsut the guy who did the transaltions     
    
> **\<plowsof\>** oh we dont care about the anon dev, i forgot     
    
> **\<ofrnxmr:xmr.mx\>** the spanish translation*     
    
> **\<plowsof\>** ignore     
    
> **\<plowsof\>** what is ofrnxmr waiting for to vote on the proposal?     
    
> **\<pw:xmr.mx\>** votes.     
    
> **\<ofrnxmr:xmr.mx\>** twas a joke     
    
> **\<pw:xmr.mx\>** ohz hehehuhuhahaha     
    
> **\<ofrnxmr:xmr.mx\>** seems were still at a crossroads and over the limit. lets see if activity picks up or any concerns addressed before next meeting     
    
> **\<ofrnxmr:xmr.mx\>** thanks folks     
    
> **\<slowbeardigger:matrix.org\>** take care ppl     
    
> **\<ofrnxmr\>** Next meeting Sat Sept 5, 2026 @ 1600 UTC     

Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: nahuhh | 2026-08-21T16:22:49+00:00
- Closed at: 2026-08-22T20:30:01+00:00
