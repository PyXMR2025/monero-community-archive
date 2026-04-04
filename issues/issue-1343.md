---
title: Monero Research Lab Meeting - Wed 18 February 2026, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1343
author: Rucknium
assignees: []
labels: []
created_at: '2026-02-18T16:53:21+00:00'
updated_at: '2026-03-04T16:04:16+00:00'
type: issue
status: closed
closed_at: '2026-03-04T16:04:16+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Live log: https://libera.monerologs.net/monero-research-lab

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [FCMP code integration audit overview](https://github.com/seraphis-migration/monero/issues/294).

4. [`carrot-core` implementation audit](https://github.com/cypherstack/carrot_core-audit).

5. [FCMP alpha stressnet](https://monero.town/post/6763165).

6. Any other business

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1340 

# Discussion History
## Rucknium | 2026-02-25T16:20:51+00:00
Log


> __< jberman >__ In advance of the meeting today (I unfortunately won't be able to attend today), here is the latest proposed audit plan for the FCMP++ integration: https://github.com/seraphis-migration/monero/issues/294     

> __< jberman >__ After discussions with jeffro256 , we decided to open all crypto PR's upstream to the Monero master branch, and then we'd have those PR's audited. I'm currently finalizing those PR's, then will reach out to audit firms once ready (likely Cypher Stack)     

> __< jberman >__ Re: alpha stressnet, all looks good for beta     

> __< jberman >__ Re: beta stressnet, we're working through outstanding tasks still     

> __< sgp_ >__ No update from me other than money pls (re divisors)     

> __< plowsof >__ ack      

> __< rucknium >__ MRL meeting in this room in two hours.     

> __< jeffro256 >__ Unfortunately I am traveling today , so I also won't be able to make the meeting , but Cyperstack completed their audit of carrot_core! https://github.com/cypherstack/carrot_core-audit     

> __< rucknium >__ Meeting time! https://github.com/monero-project/meta/issues/1343     

> __< rucknium >__ 1. Greetings     

> __< rucknium >__ ( jberman:monero.social  and jeffro256:monero.social  said they cannot attend the meeting today.)     

> __< rbrunner >__ Hello     

> __< plowsof >__ 👋     

> __< rucknium >__ This may be a short meeting 😄     

> __< rucknium >__ 2. Updates. What is everyone working on?     

> __< rbrunner >__ Looking further into Polyseed implementations, with slow speed     

> __< rucknium >__ me: For the next couple of weeks at least I won't have work updates. I need to reset, recharge, and return to my projects with fresher eyes. I will still chair MRL meetings, if that is ok with everyone.     

> __< rbrunner >__ I would be very surprised if not :)     

> __< nioc >__ rucknium please do  <3     

> __< rucknium >__ Sounds good :)     

> __< rucknium >__ 3. FCMP code integration audit overview (https://github.com/seraphis-migration/monero/issues/294).     

> __< rucknium >__ I will quote jberman:monero.social  from before the meeting:     

> __< rucknium >__ > In advance of the meeting today (I unfortunately won't be able to attend today), here is the latest proposed audit plan for the FCMP++ integration: https://github.com/seraphis-migration/monero/issues/294     

> __< rucknium >__ > After discussions with jeffro256 , we decided to open all crypto PR's upstream to the Monero master branch, and then we'd have those PR's audited. I'm currently finalizing those PR's, then will reach out to audit firms once ready (likely Cypher Stack)     

> __< rucknium >__ Any comments on this plan?     

> __< rbrunner >__ Looking from the outside, sounds reasonable, and personally I trust the persons involved to find a good path forward     

> __< rucknium >__ 4. carrot-core implementation audit (https://github.com/cypherstack/carrot_core-audit).     

> __< rucknium >__ This was posted just yesterday. AFAIK, jbabb:cypherstack.com  was the lead person on this.     

> __< rbrunner >__ 5 pages? Well, maybe that all it needs ...     

> __< rucknium >__ DataHoarder[m]  might find the report interesting because DataHoarder has re-implemented a lot of CARROT in Go. I think.     

> __< rbrunner >__ Well yes, if the audit compares code with the spec, and code is ok, the result really is a quite short report. No problem :)     

> __< rbrunner >__ Does not mean at all of course that this comparison was only little work.     

> __< rucknium >__ Any more comments on the audit report for now? It was just posted, so everyone can have time to digest and bring up opinions later if desired.     

> __< rucknium >__ 5. FCMP alpha stressnet (https://monero.town/post/6763165).     

> __< rucknium >__ Quoting jberman:monero.social :     

> __< rucknium >__ > Re: alpha stressnet, all looks good for beta     

> __< rucknium >__ > Re: beta stressnet, we're working through outstanding tasks still     

> __< rbrunner >__ Can't comment, don't take part     

> __< rbrunner >__ People seem to have fun however, judging from the talk in the room     

> __< rucknium >__ I have the alpha stressnet blockchain size at 226 GB, unpruned . I will be glad when it's reset for beta stressnet 😁     

> __< rucknium >__ Anything more on stressnet?     

> __< rucknium >__ We can end the meeting here. Thanks everyone.     

> __< plowsof >__ thanks Rucknium!     

> __< rbrunner >__ +1     

> __< DataHoarder >__ yeah. I think I have a few specifics missing but most is there. I'll read when I have some time     

> __< DataHoarder >__ ^ I had to cleanup and stopped running it, will be back for beta     

> __< DataHoarder >__ randomx v2 is merged upstream, beta had an item for having commitments     

> __< DataHoarder >__ would that also now also include v2 testing (if commitments make it to beta stressnet?)     

> __< jeffro256 >__ That's not a bad idea at all      

> __< jeffro256 >__ I imagine it would break p2pool, XMRIG , etc, though      

> __< jeffro256 >__ Doesn't sech1 also maintain xmrig ? Is there a planned deadline for xmrig support ?     

> __< sech1 >__ v2 code is already in xmrig dev branch     

> __< sech1 >__ P2Pool also updated RandomX repo     

> __< jeffro256 >__ Perfect, I'll work on v2 support for beta stressnet then      

> __< sech1 >__ for v2 commitments, you'll also need to define where in the block template to put them, and add them to the "submit_block" RPC     

> __< sech1 >__ not block template, but the block itself. Commitment is not a part of block template/block hashing blob     

> __< DataHoarder >__ > I imagine it would break p2pool     

> __< DataHoarder >__ ^ the one that can mine in stressnet is go-p2pool not main P2Pool yet :)     

> __< DataHoarder >__ and I do have go-randomx supporting V2 (and would support RandomX new release if one comes too)     

> __< DataHoarder >__ sech1 would swoop in later when carrot/targets have more or less stabilized, as also all the carrot stuff has to make it in onto p2pool     

> __< DataHoarder >__ block header, yeah    


# Action History
- Created by: Rucknium | 2026-02-18T16:53:21+00:00
- Closed at: 2026-03-04T16:04:16+00:00
