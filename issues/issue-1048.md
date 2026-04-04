---
title: Monero Research Lab Meeting - Wed 31 July 2024, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1048
author: Rucknium
assignees: []
labels: []
created_at: '2024-07-31T15:01:56+00:00'
updated_at: '2024-08-13T15:22:32+00:00'
type: issue
status: closed
closed_at: '2024-08-13T15:22:32+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://web.archive.org/web/20230128130949/https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Stress testing `monerod`](https://github.com/monero-project/monero/issues/9348)

4. [Potential measures against a black marble attack](https://github.com/monero-project/research-lab/issues/119).

5. Research [Pre-Seraphis Full-Chain Membership Proofs](https://www.getmonero.org/2024/04/27/fcmps.html).

6. Any other business

7. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1044 

# Discussion History
## Rucknium | 2024-08-07T14:36:37+00:00
Logs

> __< r​ucknium:monero.social >__ Meeting time!     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< v​tnerd:monero.social >__ Hi     

> __< j​effro256:monero.social >__ howdy     

> __< rbrunner >__ Hello     

> __< o​ne-horse-wagon:monero.social >__ Hello.     

> __< 0​xfffc:monero.social >__ Hi everyone     

> __< j​berman:monero.social >__ *waves*     

> __< r​ucknium:monero.social >__ Meeting issue: https://github.com/monero-project/meta/issues/1048     

> __< k​ayabanerve:matrix.org >__ 👋     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< r​ucknium:monero.social >__ me: Comments on some tx broadcast PRs. Reading papers on gossip protocols and their privacy, bandwidth, and speed.     

> __< v​tnerd:monero.social >__ I'm working (right now) on jeffro256 pr for blockchain syncing - hopefully we can get this shipped today. Also doing LWS frontend stuff atm     

> __< 0​xfffc:monero.social >__ Reading and familiarizing myself with my broadcast mechanisms. I have started implementing this: https://github.com/monero-project/monero/issues/9334#issue-2306257939     

> __< 0​xfffc:monero.social >__ Reading and familiarizing myself with broadcast mechanisms. I have started implementing this: https://github.com/monero-project/monero/issues/9334#issue-2306257939     

> __< j​effro256:monero.social >__ Me: writing the carrot doc. Draft is here https://github.com/jeffro256/carrot/blob/master/release/carrot_0.1.md     

> __< 0​xfffc:monero.social >__ Reading the erlay paper and familiarizing myself with broadcast mechanisms. I have started implementing this: https://github.com/monero-project/monero/issues/9334#issue-2306257939     

> __< k​ayabanerve:monero.social >__ I've been preparing crates for auditing, once our current reviews wraps up.     

> __< r​ucknium:monero.social >__ 0xfffc: Looks like we are looking at a similar area     

> __< j​berman:monero.social >__ me: working on adding fcmp++'s to the cryptonote::transaction class     

> __< r​ucknium:monero.social >__ 3) Stress testing monerod https://github.com/monero-project/monero/issues/9348     

> __< s​gp_:monero.social >__ Hello     

> __< r​ucknium:monero.social >__ spackle created a new release version for stressnet. It pulled in everything that is in the new monero master plus the invalid blocks fix and jeffro256 's PR to reduce tx writes from 2 to 1.     

> __< r​ucknium:monero.social >__ Things seem to be running smoothly with the new release so far     

> __< r​ucknium:monero.social >__ Any more comments on stressnet?     

> __< o​ne-horse-wagon:monero.social >__ Rucknium: Is there any projected date as to when stressnet will end?     

> __< r​ucknium:monero.social >__ That's still being discussed.     

> __< o​ne-horse-wagon:monero.social >__ My feelings are to keep it going until every stress idea has been exhausted.     

> __< 0​xfffc:monero.social >__ Around August 8,9 spackle will leave stressnet, and me Rucknium will maintain the repo. We expect to continue stress-net but with much less nodes.     

> __< 0​xfffc:monero.social >__ ( spackle did a great job so far. So hats off to his work )     

> __< r​ucknium:monero.social >__ Yes that's the loose plan now     

> __< r​ucknium:monero.social >__ 4) Potential measures against a black marble attack. https://github.com/monero-project/research-lab/issues/119     

> __< r​ucknium:monero.social >__ A group claimed responsibility for the suspected spam transactions earlier this year: https://antidark.net/board/viewtopic.php?t=10     

> __< r​ucknium:monero.social >__ They said that their objective was not to launch an anti-privacy black marble attack, but to congest the txpool to try to exploit some mechanisms in some services' withdrawal logic.     

> __< r​ucknium:monero.social >__ Anyone want to share opinions about this?     

> __< k​ayabanerve:matrix.org >__ When I first read it, there was no evidence of their claims, and it didn't completely make sense. I wouldn't care too much about it. I'm unsure if they've added more detail though to justify their story.     

> __< j​effro256:monero.social >__ Agreed: As of yet it is unverified. Might be a mistake to assume that a black marble attack did not occur because some rando on a forum said so     

> __< r​ucknium:monero.social >__ I basically concur. But they did say something that a person who prepared spam txs would know: wallet2 does not perform well when 200,000 accounts are created.     

> __< j​effro256:monero.social >__ This looks to be a followup (maybe): https://antidark.net/board/viewtopic.php?t=15     

> __< b​asses:matrix.org >__ There are some discussion from antidark members https://monero.town/post/3785880     

> __< b​asses:matrix.org >__ yes     

> __< r​ucknium:monero.social >__ In the followup they answer a comment about why won't they release the spam wallet(s) view keys. They said that they would not release it.     

> __< r​ucknium:monero.social >__ It would be bad for user privacy if the suspected spammer actually released the spam wallet(s) view key(s).     

> __< r​ucknium:monero.social >__ Releasing the view keys would prove that they actually were responsible for the spam (or at least that the entity that was responsible gave them the view keys.     

> __< rbrunner >__ I guess it doesn't change much for us overall whether it really was this group or not.     

> __< k​ayabanerve:matrix.org >__ I'd rather such a theoretical view key not float around.     

> __< r​ucknium:monero.social >__ 5) Research Pre-Seraphis Full-Chain Membership Proofs. https://www.getmonero.org/2024/04/27/fcmps.html     

> __< k​ayabanerve:matrix.org >__ I don't have much more to say than my initial comment. Veridise is moving forward with the R1CS gadget for evaluating this week, and there's preliminary opinions on the GBP proof review.     

> __< r​ucknium:monero.social >__ I saw this paper: https://distributedlab.com/whitepaper/Bulletproofs-Construction-and-Examples.pdf  "This document introduces some clarification and corrections to Bulletproofs++ [Eag+23] paper."     

> __< r​ucknium:monero.social >__ The paper probably isn't very relevant for Monero right now since BP++ is not going forward in the Monero protocol AFAIK.     

> __< k​ayabanerve:matrix.org >__ I saw the note it existed. I wouldn't change the perception of BP++, as Aaron reviewed it, at this time.     

> __< k​ayabanerve:matrix.org >__ If this leads to a new revision of BP++, then that may be eligible for rereview, but...     

> __< r​ucknium:monero.social >__ Any more topics anyone wants to discuss?     

> __< j​effro256:monero.social >__ Who would be some good auditors for the new addressing protocol ?     

> __< j​effro256:monero.social >__ Whether that be Jamtis or Carrot or something else     

> __< a​aron:cypherstack.com >__ FYI the Cypher Stack review of the Veridise report should be released to kayabanerve today as an initial draft for comment     

> __< a​aron:cypherstack.com >__ Very curious on the GBP opinion :D     

> __< k​ayabanerve:monero.social >__ :D     

> __< r​ucknium:monero.social >__ That reminds me that Cypher Stack reviewed a protocol that seemed to add return addresses to Monero-like txs, which has been on getmonero.org's roadmap for a while: https://github.com/cypherstack/salvium-review/releases/download/final/final.pdf     

> __< a​aron:cypherstack.com >__ We did that review, yes     

> __< k​ayabanerve:monero.social >__ jeffro256: You'd need to define the desired properties.     

> __< k​ayabanerve:monero.social >__ Presumably, a variety of indistinguishability properties.     

> __< j​effro256:monero.social >__ I have a list of informal security and indistinguishability properties that I plan to add later. Also working on writing a condensed abstraction of FCMP++ requirements for Carrot (i.e. O = x G = y T, C = z G + a H, 0 <= a < 2**64, L = x Hp(O), sender needs knowledge of x, y, z, a, outgoing view wallet needs knowledge of x, etc)     

> __< j​effro256:monero.social >__ Is this the right path?     

> __< j​effro256:monero.social >__ *O = x G + y T     

> __< r​ucknium:monero.social >__ kayabanerve: What do you think ^ ?     

> __< rbrunner >__ Seems to me if Cypher Stack reviews something like this Salvium, they are in a good spot to review our "stuff" as well. Looks pretty ambitious, by the way, that Salvium project.     

> __< a​aron:cypherstack.com >__ I can't speak for Cypher Stack, but I would certainly advocate that the company put in a bid for such a review (for the addressing, I mean)     

> __< k​ayabanerve:matrix.org >__ I'd have to see the document to properly comment, sorry.     

> __< j​effro256:monero.social >__ Aaron Feickert: thanks !     

> __< j​effro256:monero.social >__ kayabanerve: fair enough, will try to do later today     

> __< r​ucknium:monero.social >__ I think we can end the meeting here. Thanks all.     

> __< j​effro256:monero.social >__ Thanks everyone !     


# Action History
- Created by: Rucknium | 2024-07-31T15:01:56+00:00
- Closed at: 2024-08-13T15:22:32+00:00
