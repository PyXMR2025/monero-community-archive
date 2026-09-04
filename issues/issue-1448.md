---
title: Monero Research Lab Meeting - Wed 26 August 2026, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1448
author: Rucknium
assignees: []
labels: []
created_at: '2026-08-26T13:40:02+00:00'
updated_at: '2026-09-02T14:49:43+00:00'
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

6. Validating key images. https://github.com/monero-project/monero/pull/11155 and https://github.com/monero-project/monero/pull/11152

7. Any other business

8. Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs: #1443 

# Discussion History
## Rucknium | 2026-09-02T14:49:43+00:00
Logs

> __< rucknium >__ Meeting time! https://github.com/monero-project/meta/issues/1448     

> __< jeffro256 >__ Howdy     

> __< rucknium >__ 1. Greetings     

> __< sech1 >__ Hello     

> __< tevador >__ Hi     

> __< jpk68:matrix.org >__ Hello     

> __< vtnerd >__ Hi     

> __< rbrunner >__ Hello     

> __< rucknium >__ 2. Updates. What is everyone working on?     

> __< tevador >__ mx25519 and polyseed maintenance/updates     

> __< sech1 >__ I'm working on adding Carrot math to P2Pool - I'll be likely done in 1-2 weeks, after that P2Pool will be ready for stressnet testing     

> __< jberman >__ waves     

> __< rucknium >__ me: Updated the IP package to work with the latest version of R: https://github.com/Rucknium/IP . It has been accepted to go back onto the Comprehensive R Archive Network (CRAN). Also working with monerosim. (Thanks to gingeropolous:monero.social  for fixing the issues I found so far https://github.com/Fountain5405/monerosim/issues ).     

> __< vtnerd >__ Me: tracked down a regression in lws, updated several monerod prs with serialization almost ready to push, and another zmq thing with yet more serialization changes      

> __< tevador >__ FYI: mx25519 optimizations from the past week made the amd64x implementation about 20% faster (98k cycles per scalar mult on Zen2).     

> __< jberman >__ PR reviews mostly, and started back working on Serai     

> __< jeffro256 >__ me: working on people's reports for Carrot, updating the Carrot spec for tevador's suggested changes, and working on j-berman's hot-cold feedback      

> __< jeffro256 >__ And upstream shtuff      

> __< jpk68:matrix.org >__ Me: reviews, fixing some bugs, beginning work on Tor Control integration     

> __< rucknium >__ 3. FCMP++ to-do list status. Programming tasks (https://github.com/seraphis-migration/monero/issues/53). Reviews and audits (https://cryptpad.fr/sheet/#/2/sheet/view/yPVIUywwA9-deE9VF6GYm9bXbPdCerdST3UDEEfBxcM/embed/). FCMP++ Integration Audit Overview (https://github.com/seraphis-migration/monero/issues/294). Network upgrade  [... too long, see https://mrelay.p2pool.observer/e/pt6mxKQLWXJsNVVj ]     

> __< jberman >__ On Research Task audits: Request for quotes on circuits + gadget + fcmp-plus-plus lib has gone out, we've gotten some responses but nothing major to report yet     

> __< rucknium >__ Another thing: I plan to upgrade the Matrix room version of this room to version 12 after the end of the meeting. If anyone thinks I shouldn't do that, speak now.     

> __< jberman >__ On tasks: next major item is hot/cold wallet integration jeffro256:monero.social mentioned above, in the final cycles now on that task     

> __< jberman >__ Here's the latest upstream PR for FCMP++ integration: github.com/monero-project/monero/pull/10361       

> __< rucknium >__ Thanks, jberman:monero.social . Anything more on this item?     

> __< rucknium >__ Come to think of it, I should probably coordinate with DataHoarder[m]  on the Matrix room upgrade since we will have to switch the IRC-Matrix bridge bot to the next version room.     

> __< DataHoarder >__ do it anytime.     

> __< rucknium >__ DataHoarder: Sounds good. Thanks.     

> __< DataHoarder >__ I automated that part and it'll follow the tombstone with all IRC puppets and relay.     

> __< rucknium >__ Well you are ahead of me :)     

> __< UkoeHB >__ me: reviews, pending_tx sanity checker nonsense     

> __< rucknium >__ 4. Relative locks with FCMP++ (https://github.com/monero-project/research-lab/issues/161).     

> __< jberman >__ u/CjS77 expressed hesitation in building with them until the feature would be confirmed included in Monero     

> __< jberman >__ > I guess I'd like to take the temperature on the level of support before committing to anything.     

> __< jeffro256 >__ What about its viability as it relates to Grease?     

> __< jberman >__ I responded that I have a hard time seeing significant resistance to the feature if the protocol is fully specced + there's a developemnt path to utilizing the feature     

> __< jberman >__ https://github.com/monero-project/research-lab/issues/161#issuecomment-5396778447     

> __< jberman >__ Sounds like it would be a major change to their protocol     

> __< tevador >__ Classic chicken-egg, but shipping the consensus code for the lock is probably way less work than designing the actual PC protocol.     

> __< jberman >__ If someone was actually interested in designing the actual PC protocol, then I think it would make sense to seek funding for that design, rather than funding for a protocol that relies on trust     

> __< jberman >__ Doesn't make sense to me that they wouldn't be interested in that work personally     

> __< jberman >__ I mean, I guess it's not a major risk to include that change to consensus either way, but it would be nice to have a concrete path to using it established first     

> __< tevador >__ One thing that's still TBD is the lock length since we can only ship one value. 1 week would have some advantages for PCs compared to 1 day, but maybe 3 days is a good compromise.     

> __< rucknium >__ Does anyone have a way to contact fiatdemise:matrix.org ? IMHO, XMRChat.com is the most obvious first use case for payment channels. Maybe that could get some momentum behind the payment channels idea.     

> __< rucknium >__ Maybe I will try to email the XMRChat support email address.     

> __< jberman >__ Another thing u/CjS77 raised in that issue is the issue of requiring O(n) state growth for channel updates, and UkoeHB sketched a potential way to avoid it? I know bitcoin would need a consensus change to achieve it on their end (eltoo), so seems like another open area to consider     

> __< fiatdemise:matrix.org >__ Hi, I'm not familiar with payment channels or their benefit, but I'll take a look at an email with more info.     

> __< UkoeHB >__ I sketched some requirements for one way to avoid it, and Cjs77 pointed out the speculative/experimental VCOF from greese v1 aims at the same problem. But no guaranteed solve.     

> __< rucknium >__ fiatdemise:matrix.org: Hi! If users are getting frustrated with the 10 block lock, payment channels could solve that, at the cost of more complexity. I will email you later.     

> __< tevador >__ I think O(n) channels are acceptable. One state is maybe 300 bytes?     

> __< rucknium >__ The BTC Lightning Network is based on aggregating many payment channels     

> __< jberman >__ > Not an issue for moderately active channels (n < 1000), but for some of the applications that I would love to see for channels that involve many thousands of updates (fine-grained streaming content for example)     

> __< jberman >__ I think that was a solid point     

> __< tevador >__ Let's aim for incremental improvements     

> __< UkoeHB >__ Don't we need a perfect design for payment channels to be useful     

> __< rucknium >__ Anyone aware of BTC Lightning being used for fine-grained streaming content?     

> __< UkoeHB >__ Don't think*     

> __< tevador >__ It's better to have non-perfect relative locks with non-perfect (but working) payment channels than nothing.     

> __< jberman >__ point remains it would be nice to have a fully developed protocol prior to shipping a consensus change that has these sort of kinks ironed out and understood (and provably functioning payment channels)     

> __< tevador >__ Then we're back to the chicken egg problem     

> __< rbrunner >__ Didn't tevador post a sketch of such a protocol? And if yes, isn't that at least a starting point?     

> __< jberman >__ Ya, I really don't think u/CjS77 would have an easier time getting funding after this change is merged versus before, so I really don't think this is actually a chicken egg problem      

> __< selsta >__ can we add one more point to the agenda? is https://github.com/monero-project/monero/pull/11155 or https://github.com/monero-project/monero/pull/11152 preferred? or both? we need to decide for the next release. maybe jeffro can explain.     

> __< rucknium >__ selsta: Yes. I can add it at the end.     

> __< rucknium >__ More discussion on relative locks for now?     

> __< jberman >__ In any case, I don't think the change needs to be held back. I think it's ok. At the same time, I'd like to see a concrete development path for it     

> __< UkoeHB >__ Re: relative locks I propose we keep pushing forward with PR to add the basic rule. So far there seem no strong/direct objections, just jberman preferring a protocol be more fleshed out.     

> __< UkoeHB >__ It seems the Greese team isn't prepare to flesh that out, so idk if any progress will be made on that front.     

> __< jberman >__ we can share this convo with them and see what happens on that front     

> __< rucknium >__ Maybe one of the authors of those Monero payment channel papers can write a new paper with relative locks :)     

> __< rucknium >__ I mean, maybe they could be contacted. Could be worth a shot. But probably a 9 month wait on something like that.     

> __< jberman >__ ya I wouldn't veto this change pending a 9 month wait, I personally do think it's ok     

> __< UkoeHB >__ If we are 9mo out from hf, that would be good timing for a paper for someone to pick up and implement.     

> __< rucknium >__ 5. FCMP beta stressnet (https://github.com/seraphis-migration/monero/releases/). Version 3 launch checklist (https://github.com/seraphis-migration/monero/pull/415).     

> __< DataHoarder >__ as mentioned before, I assume this also brings up the changes from the fcmp staging branch onto v3?     

> __< jberman >__ Hot/cold PR is the major lingering item (I haven't updated that checklist)     

> __< jberman >__ DataHoarder: yes, and latest master     

> __< DataHoarder >__ 👍     

> __< jeffro256 >__ I'm working on responding to some reports, and then I'll be on top of finishing hot/cold      

> __< rucknium >__ 6. Validating key images. https://github.com/monero-project/monero/pull/11155 https://github.com/monero-project/monero/pull/11152     

> __< selsta >__ yes, does it make sense for the release to just merge 11152 while 11155 being merged to master?     

> __< jeffro256 >__ SGTM      

> __< jberman >__ both look fine     

> __< rucknium >__ Any more discussion on this topic?     

> __< rucknium >__ We can end the meeting here. Thanks everyone.   


# Action History
- Created by: Rucknium | 2026-08-26T13:40:02+00:00
