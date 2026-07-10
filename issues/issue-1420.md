---
title: Monero Research Lab Meeting - Wed 08 July 2026, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1420
author: Rucknium
assignees: []
labels: []
created_at: '2026-07-07T19:40:44+00:00'
updated_at: '2026-07-09T19:23:50+00:00'
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

3. [Post-quantum encryption](https://github.com/monero-project/research-lab/issues/151#issuecomment-4412416686). [Jamtis](https://gist.github.com/tevador/639d083c994c1ef9401832c08e2b7832#appendix-c-instant-sync-protocol).

4. [FCMP beta stressnet](https://github.com/seraphis-migration/monero/releases/).

5. [`monerosim`](https://github.com/Fountain5405/monerosim).

6. Any other business

7. Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs: #1415 

# Discussion History
## Rucknium | 2026-07-09T19:23:50+00:00
Logs

> __< vtnerd >__ Schedule conflict during the meeting so I'll give my updates now: finished fixing small bugs in lws and lwsf (Claude Report/review). Now working on updating all the serialization prs - there's been one review in particular that needs attention      

> __< gingeropolous >__ dunno what i'll be doing at the time, my update - cluster work. stupid hardware being stupid     

> __< sgp_ >__ My only update is that the Helios/Selene review kicked off and will be returned later this month     

> __< sgp_ >__ The reviewer is Least Authority     

> __< rucknium >__ Meeting time! https://github.com/monero-project/meta/issues/1420     

> __< rucknium >__ 1. Greetings     

> __< articmine >__ Hi     

> __< jpk68 >__ Hello     

> __< rbrunner >__ Hello     

> __< boog900 >__ Hi     

> __< jberman >__ waves     

> __< rucknium >__ 2. Updates. What is everyone working on?     

> __< rbrunner >__ Still Polyseed, but now with the code ready for re-review     

> __< jpk68 >__ Me: I2P GUI integration, writing docs     

> __< rucknium >__ me: Keeping stressnet stressed and some HackerOne work.     

> __< rucknium >__ There were some updates posted right before the meeting.     

> __< jberman >__ me: continuing with finalizing the audited FCMP++ integration PR's (we're approaching 1k lines of integration crypto code merged including tests), and more stressnet investigating     

> __< rucknium >__ 3. Post-quantum encryption (https://github.com/monero-project/research-lab/issues/151#issuecomment-4412416686). Jamtis (https://gist.github.com/tevador/639d083c994c1ef9401832c08e2b7832#appendix-c-instant-sync-protocol).     

> __< rucknium >__ Any discussion on this topic?     

> __< rucknium >__ 4. FCMP beta stressnet (https://github.com/seraphis-migration/monero/releases/).     

> __< rucknium >__ The main machine I use to send tx spam has had some stability issues. gingeropolous:monero.social  referenced them in his update before the meeting.     

> __< rucknium >__ But other users are spamming from their machines. Thank you!     

> __< rucknium >__ Block sizes have gone back to being small because tx spam isn't enough to keep them large.     

> __< jberman >__ Looking to get v2.1 out in the next day (solves windows GUI crash, marginally improves wallet refresh, and will hopefully solve those double spend errors for good)     

> __< rucknium >__ I added a few new features to my xmrspammer package https://github.com/Rucknium/xmrspammer . With get.view.keys(), a user can get the view keys of their spamming wallets. Useful for seeing which of your spam wallets are getting txs confirmed if you submit your view keys to https://stressnet.p2pool.observer/payments     

> __< rucknium >__ And kill.wallet.processes() will kill the monero-wallet-rpc processes associated with a set of wallets. Useful in case you don't want to kill all of the wallet RPC processes running on your machine.     

> __< rucknium >__ Anything else on stressnet?     

> __< jberman >__ Nothing from me, other than that seems like remaining hiccups seem to be uncommon upstream edge cases     

> __< jberman >__ and FCMP++ / Carrot specific code seems to be holding up well     

> __< rucknium >__ jberman:monero.social: Glad to hear it. (I will ping you about something at the end of the meeting.)     

> __< rucknium >__ 5. monerosim (https://github.com/Fountain5405/monerosim).     

> __< rucknium >__ gingeropolous:monero.social said he is working on some hardware issues in the Monero Research Computing Cluster. Thanks, gingeropolous:monero.social ! Probably there is no further update on monerosim for this meeting.     

> __< rucknium >__ 6. Any other business     

> __< rucknium >__ I want to check in on status of the last FCMP++ items needed before deployment.     

> __< rucknium >__ jberman:monero.social: Do these reflect the current remaining items: https://github.com/seraphis-migration/monero/issues/53 https://cryptpad.fr/sheet/#/2/sheet/view/yPVIUywwA9-deE9VF6GYm9bXbPdCerdST3UDEEfBxcM/embed/     

> __< rucknium >__ Is there another list we should be looking at, too?     

> __< rucknium >__ Or anyone else can comment on the to-do list, too.     

> __< jberman >__ Sorry, computer connection is spotty rn. Switching to mobile     

> __< jberman >__ The remaining major blockers include:     

> __< jberman >__ 1. Beta stressnet     

> __< jberman >__ 2. Research Audit tasks     

> __< jberman >__ 3. Multisig[... more lines follow, see https://mrelay.p2pool.observer/e/tOqe4pQLM3VoaHhN ]     

> __< jberman >__ That list reflects Research audit tasks. In addition to what's there, we've been discussing having another round of audits done on the circuit and gadgets impl (the equivalent area where Zcash had a hidden inflation bug)     

> __< rucknium >__ The counterfeiting bugs & flaws in other coins make me nervous, personally.     

> __< rucknium >__ They have always made me nervous, but there are more of them now. And more recent.     

> __< jberman >__ I would say that if beta stressnet continues running the way it's been running, that beta has demonstrably served its purpose     

> __< jberman >__ Koe is nearly complete with multisig     

> __< jberman >__ Jeffro is nearly complete with hot/cold impl, which I've also reviewed in depth thus far     

> __< jberman >__ Hardware wallets are probably the biggest question mark on the impl front at the moment. Not that we won't be able to complete it. But we've been waiting on the vendors to indicate they have the capacity to do it asap     

> __< ofrnxmr >__ jberman: plowsof should test the cold signing airgap stuff for fcmp++ (and mobile eallet migration in general)     

> __< jberman >__ And then on merging code: we're making incremental progress on that front. Crypto building blocks are making their way in. That's been/will be my first priority at this point     

> __< plowsof:matrix.org >__ creating an unsigned tx set + signing (if thats possible now, it will be great to try)     

> __< ofrnxmr >__ I think an impotant step on the way, is for mobile wallet to be tested on stressnet     

> __< jberman >__ Cake mentioned they're going to prepare a build for the beta stressnet, so that'll be nice     

> __< ofrnxmr >__ Cake said theyd thibk abt it in public, maybe confirmed it elsewhere>     

> __< ofrnxmr >__ Acx said he couldnt get monfluo to build for master, and monerujo didnt respond yet     

> __< rucknium >__ Should I create a general FCMP update item on future agendas, or is there no need?     

> __< jberman >__ plowsof:matrix.org: AFAIK jeffro256:monero.social  is still finalizing the PR from my review comments, but once that PR is fully ready, will be able to test it (will link the PR in a sec)     

> __< jberman >__ rucknium: Sgtm     

> __< jberman >__ This is the development branch PR for hot/cold wallets: https://github.com/seraphis-migration/monero/pull/52     

> __< rucknium >__ jberman: I will do it.     

> __< jberman >__ And then that'll get pulled into beta once it's ready here: https://github.com/seraphis-migration/monero/pull/358     

> __< jeffro256 >__ Hi, sorry I'm late      

> __< jeffro256 >__ Yeah, I recently made a big change to the carrot_core lib here: https://github.com/seraphis-migration/monero/pull/424. Now the hot-cold PR, and the knowledge proofs PR depend on it      

> __< jeffro256 >__ Today I'm refactoring all the doc strings in my Carrot code so they can be parsed by Doxygen, and I'm reviewing Ukoe's review of carrot_impl      

> __< rucknium >__ jberman:monero.social: Thanks for explaining the FCMP to-do list!     

> __< rucknium >__ Anything else anyone wants to bring up?     

> __< jeffro256 >__ j-berman Should we mention blocking tasks for v2.1?     

> __< jberman >__ Sure, blocking task is me looking into rucknium:monero.social 's latest logs showing another double spend error running code that solves a bug that was contributing to the issue, but apparently there is still another bug causing it and needs further investigation     

> __< jberman >__ I haven't had the chance to dig into those logs yet     

> __< rucknium >__ How important is it to fully resolve the double-spend error? It is extremely rare.     

> __< rucknium >__ In terms of priorities     

> __< jberman >__ Not very, I'm not prioritizing it highly at this point (and have also had somewhat limited availability this past week), which is why I haven't gotten to it     

> __< jpk68:matrix.org >__ I contacted Trezor on Twitter, trying to give them contact info. They responded and said their devs were already in contact, which seems to be... not true > <jberman> Hardware wallets are probably the biggest question mark on the impl front at the moment. Not that we won't be able to complete it. But we've been waiting on the vendors to indicate they have the capacity to do it asap     

> __< rucknium >__ (Note to readers: "double-spend error" does not mean that the blockchain accepts a double-spend. The error occurs because the wallet software forgets that it spent a coin and then tries to spend the coin again. The node rejects the transaction with a double-spend error.)     

> __< plowsof:matrix.org >__ ideally the wallet would self correct, the outputs marked as double spent in the tx are then marked as such and the next attempt does not include them. is this not happening?     

> __< ofrnxmr >__ Its not     

> __< rucknium >__ We can end the meeting here. Thanks everyone!     

> __< jberman >__ The more pressing concern with the issue ATM is that the node isn't relaying the tx in the first place, so tx gets stuck in the node un-relayed. That's the core thing that needs to be fixed here     




# Action History
- Created by: Rucknium | 2026-07-07T19:40:44+00:00
