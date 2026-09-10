---
title: Monero Research Lab Meeting - Wed 02 September 2026, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1451
author: Rucknium
assignees: []
labels: []
created_at: '2026-09-02T14:52:23+00:00'
updated_at: '2026-09-08T18:15:56+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Live log: https://libera.monerologs.net/monero-research-lab

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. FCMP++ to-do list status. [Programming tasks](https://github.com/seraphis-migration/monero/issues/53). [Reviews and audits](https://cryptpad.fr/sheet/#/2/sheet/view/yPVIUywwA9-deE9VF6GYm9bXbPdCerdST3UDEEfBxcM/embed/). [FCMP++ Integration Audit Overview](https://github.com/seraphis-migration/monero/issues/294). [Network upgrade schedule Gantt chart](https://html-preview.github.io/?url=https://github.com/jeffro256/fcmp-carrot-plan/blob/master/fcmp%2B%2B-carrot.html).

4. [Relative locks with FCMP++](https://github.com/monero-project/research-lab/issues/161).

5. [FCMP beta stressnet](https://github.com/seraphis-migration/monero/releases/). [Version 3 launch checklist](https://github.com/seraphis-migration/monero/pull/415).

6. Any other business

7. Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs: #1448 

# Discussion History
## Rucknium | 2026-09-08T18:15:56+00:00
Logs

> __< rucknium >__ Meeting time! https://github.com/monero-project/meta/issues/1451     

> __< rucknium >__ 1. Greetings     

> __< slowbeardigger:matrix.org >__ hello     

> __< ravfx:xmr.mx >__ o/     

> __< rbrunner >__ Hello     

> __< jpk68:matrix.org >__ Hello     

> __< articmine >__ Hi     

> __< vtnerd >__ hi     

> __< boog900 >__ hi     

> __< ack-j:matrix.org >__ Hi     

> __< jberman >__ waves     

> __< jeffro256 >__ Howdy      

> __< rucknium >__ 2. Updates. What is everyone working on?     

> __< jeffro256 >__ me: carrot_core reviews, Carot spec changes, and hot-cold PR https://github.com/seraphis-migration/monero/pull/52. Did a lot of big changes to that PR      

> __< jberman >__ some upstream PR review, and have started up again working on Serai     

> __< vtnerd >__ me: finally making a lws signed 1.0 release in the next couple of days (hopefully the last bug fix was just pushed); working on monerod serialization; reviews     

> __< jpk68:matrix.org >__ Me: worked on replacing GNU Readline, updating and reviewing PRs, doing some hardware wallet testing     

> __< rucknium >__ me: Wrote a draft of methodology for using monerism to estimate the effectiveness of spy node adversaries: https://gist.github.com/Rucknium/ba230a2bab8a446d0997b7b002bf3af6     

> __< rucknium >__ 3. FCMP++ to-do list status. Programming tasks (https://github.com/seraphis-migration/monero/issues/53). Reviews and audits (https://cryptpad.fr/sheet/#/2/sheet/view/yPVIUywwA9-deE9VF6GYm9bXbPdCerdST3UDEEfBxcM/embed/). FCMP++ Integration Audit Overview (https://github.com/seraphis-migration/monero/issues/294). Network upgrade  [... too long, see https://mrelay.p2pool.observer/e/-cPd5KYLLTJvdW5y ]     

> __< ack-j:matrix.org >__ MAGIC: set up an automated security review of monero PRs     

> __< ack-j:matrix.org >__ https://github.com/xmrack/monero-review/issues     

> __< gingeropolous >__ me: server maintenance. spinny 40TB lives on. optane drives FTW. contemplating another CCS. Fixing / improving monerosim.     

> __< vtnerd >__ ack-j:matrix.orgthese are automated AI reviews? will need to bookmark this     

> __< jberman >__ boog900:monero.social reviewed and approved the tx relay v2 major changes over here https://github.com/seraphis-migration/monero/pull/450 (I still need to respond to that last comment there, but minor point). So that one is cleared for beta stressnet v3     

> __< gingeropolous >__ me: contemplating if a ccs could cover a tesla powerwall (or equivalent) so we can stop having these damn outages ....     

> __< ack-j:matrix.org >__ vtnerd:monero.social: yes. I have opus-5 scan a new pr from a queue every 30 minutes. Each time the pr’s hash changes it gets back inline for the queue     

> __< jberman >__ jeffro256:monero.social made good progress on hot/cold wallets looks like, which we want in before stressnet v3 as well     

> __< slowbeardigger:matrix.org >__ ack-j:matrix.org: Is it there any consideration of switching AI models?     

> __< slowbeardigger:matrix.org >__ Claude models got a little bit “worse”     

> __< jberman >__ Re: Research Tasks. The current remaining major task is having circuit + gadgets impl re-audited, and the fcmp-plus-plus audited. We're currently fielding quotes and talking to candidates answering questions etc.     

> __< jeffro256 >__ I don't have much to add except that review and upstreaming is ongoing      

> __< rucknium >__ Anything more on this topic?     

> __< rucknium >__ 4. Relative locks with FCMP++ (https://github.com/monero-project/research-lab/issues/161).     

> __< rucknium >__ After the meeting, loop.ster:matrix.org said:     

> __< rucknium >__ > Don't get me wrong, I am interested in pursuing this, it's about how much time I can spend on it. If it's completely pro bono -- my working assumption --, it's like 10% of my time, tops, and I'll be using AI to help accelerate things. So I can't commit to some deadline of "produce a spec by XX date or else timelocks don't get merged".     

> __< rucknium >__ > What's encouraging is that there wasn't anyone against merging the time locks from what I could tell, so that's a very positive indicator.[... more lines follow, see mrelay.p2pool.observer/e/ur6U6qQLdzdNQXVF ]     

> __< rucknium >__ And that mrelay link is a 404 for me now. Can anyone else see it?     

> __< slowbeardigger:matrix.org >__ 404 for me as well     

> __< rucknium >__ Ah, I can find the old Matrix chat room:     

> __< rucknium >__ > Basically what I can offer is that if there's a general understanding that I am working on a spec, as time permits, along with the idea that relative locks probably do get merged -- that could work. That way we're not stuck at point 0, and in a month or so, we can compare notes again and maybe we're at a point where things can solidify a bit.     

> __< jberman >__ One point I was kind of getting at: I think even work on this spec would potentially be a solid candidate for a CCS proposal. It would be helpful Research to help solidify adding features to Monero's consensus     

> __< loop.ster:matrix.org >__ oh I see. I read it as, write the spec and then maybe..     

> __< jberman >__ nay, sorry I was unclear     

> __< loop.ster:matrix.org >__ cool, well I suspect I'll have some cycles next week to work on grease. I didn't move anything fwd this week     

> __< jberman >__ my main point being I think that continuing on the path of exploring working with that feature would be appreciated     

> __< rucknium >__ Any more discussion of this topic?     

> __< loop.ster:matrix.org >__ nothing from me     

> __< jberman >__ same, thank you loop.ster:matrix.org     

> __< rucknium >__ 5. FCMP beta stressnet (https://github.com/seraphis-migration/monero/releases/). Version 3 launch checklist (https://github.com/seraphis-migration/monero/pull/415).     

> __< jberman >__ It's just hot/cold wallet stuff now, we're working on it     

> __< jeffro256 >__ Al the major changes from j-berman's review are done AFAICT, just renamings left      

> __< rucknium >__ Thanks, jberman:monero.social and jeffro256:monero.social .     

> __< rucknium >__ Looks like this is going to be a short meeting.     

> __< rucknium >__ We can end the meeting here. Thanks everyone.     

> __< articmine >__ Thanks      


# Action History
- Created by: Rucknium | 2026-09-02T14:52:23+00:00
