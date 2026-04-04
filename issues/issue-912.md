---
title: 'Monero Community Workgroup Meeting: Saturday 28th October 2023 @ 15:00 UTC'
source_url: https://github.com/monero-project/meta/issues/912
author: plowsof
assignees: []
labels: []
created_at: '2023-10-21T13:40:57+00:00'
updated_at: '2023-11-05T18:47:23+00:00'
type: issue
status: closed
closed_at: '2023-11-05T18:47:23+00:00'
---

# Original Description
Location: [Libera.chat, #monero-community](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-community:monero.social?via=matrix.org&via=monero.social)

[Instructions for joining the monero.social Matrix server.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time
15:00 UTC [Check your timezone](https://www.timeanddate.com/worldclock/converter.html)

Moderator: plowsof

Please reach out in advance of the meeting if you would like to propose an agenda item.

Proposed Meeting Items:

1. Introduction
2. Greetings
3. Community highlights 
    - [RISC-V binaries](https://github.com/monero-project/monero/pull/9029#pullrequestreview-1691266562). selsta is currently working on the gitian build process for them. tobtoht and others testing/helping.   
    - selsta discovered an issue some time ago which prevented M1/M2 Mac users from using the Monero-GUI to manage a local daemon. A patch fixing this issue (which reduced hash rate/performance for GUI Mac users) has been reverted: https://github.com/monero-project/monero-gui/pull/4229 after sech1 found the root cause [#monero-pow logs](https://libera.monerologs.net/monero-pow/20231019#c290842)
    - Just a week after Exodus wallet privacy fix, the number of Monero transactions with the nonstandard fee has been cut in half [@ Monero.town](https://monero.town/post/842460) - https://rucknium.me/donate/
    - Monerokon videos uploaded [yewtu.be](https://yewtu.be/watch?v=clCcuAIaAz4&list=PLsSYUeVwrHBm1m7IaU3JiDVb5EC7cn0KG&index=0) - ajs
    - [Seraphis 1 year development report ](https://www.reddit.com/r/Monero/comments/17duyvo/seraphis_wallet_development_1_year_report/) rbrunner
    - [Monero-lws PoC](https://lws.lzahq.tech/) proof of concept project with lws packaged with monerod, mymonero-js web app, and a custom flask app lza_menace wrote to be an admin panel for the lws backend https://git.cloud.lzahq.tech/nerodev/monero-lw - lza_menace
    - [BasicSwap now has a Windows installer](https://www.reddit.com/r/Monero/comments/17ho9r9/basicswap_installer_monero_atomic_swaps/)
    - [background sync with view only wallet](https://github.com/monero-project/monero/pull/8617) ready for review/testing - jberman . [bounty for this](https://bounties.monero.social/posts/41/10-503m-implement-viewkey-based-background-refresh-to-significantly-reduce-wallet-sync-time)
    - News: [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/) - [The Monero Standard](https://localmonero.co/the-monero-standard) - [Monero Moon](https://www.themoneromoon.com/)    
5. [CCS updates](https://ccs.getmonero.org/)    
  a. [Add retroactive funding proposal for FCMPs](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/403)    to be merged
  b. [dangerousfreedom - wallet work](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/409)    
  c. [Core Monero Concepts](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/412)    
  d. [escapethe3RA Monero Observer maintenance (2023 Q4)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/414)    
  e. [Incorporate LLC for MoneroKon](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/415)    
  f. [erc: ccs for getmonero and weblate](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/416)    
  g. [Monero Selfhosted View-only Web Wallet (with received transaction Telegram/Email/SMS/Discord/Webhook alerts)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/417)    
  h. [CCS Coordinator](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/418) 
  i. [v1docq47 - monerotopia 2023 (part 2) and monerokon 2023 voiceovers and working on xmr.ru](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/420)    
  j. [Rent ad space on r/CryptoCurrency to promote MoneroKon 2024](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/419) expired / closed
  k. [jeffro256 full-time dev 2023Q4](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/421)    
6. Workgroup reports    
  a. Dev workgroup
  b. Localization workgroup
  c. Outreach workgroup
  d. Events workgroup - [MoneroKon 2023](https://github.com/MoneroKon/)
  e. Website workgroup
  f. Policy workgroup
  g. Research workgroup
  h. [Seraphis Migration workgroup](https://github.com/seraphis-migration)
7. Open ideas time    
8. Confirm next meeting date/time    

[Previous meeting including logs](https://github.com/monero-project/meta/issues/906)    

Meeting logs will be posted here afterwards.    

# Discussion History
## plowsof | 2023-10-30T22:22:04+00:00
Logs 
> __< p​lowsof:matrix.org >__ Meeting today in 3hrs12mins~ https://github.com/monero-project/meta/issues/912     

> __< nioc >__ ofrn's last message is a link which asks me the following question "Choose an app to continue"       

> __< nioc >__ maybe one day we will have a proper babel fish      

> __< c​trej:matrix.org >__ All but one of the CCS issues are spam: https://repo.getmonero.org/monero-project/ccs-proposals/-/issues     

> __< c​trej:matrix.org >__ Do you have the rights to remove those plowsof?     

> __< p​lowsof:matrix.org >__ no, but i poke luigi1111 when there is *looks* yes thats enough to get cleaned lol     

> __< o​frnxmr:monero.social >__ nioc:  is Monero Support  available on mrelay? Too lazy to check :D     

> __< nioc >__ yes     

> __< p​lowsof:matrix.org >__ Meeting time https://github.com/monero-project/meta/issues/912     

> __< plowsof >__ greetings!     

> __< s​needlewoods_xmr:matrix.org >__ hi frens     

> __< c​trej:matrix.org >__ hello     

> __< msvb-lab >__ Hello.     

> __< a​js_:matrix.org >__ hello     

> __< h​into.janaiyo:matrix.org >__ hi     

> __< p​lowsof:matrix.org >__ lets discuss some recent news while people arrive 👋     

> __< p​lowsof:matrix.org >__ [RISC-V binaries](https://github.com/monero-project/monero/pull/9029#pullrequestreview-1691266562) PR from selsta. tobtoht and others testing/helping. and it looks to be complete 👍️     

> __< r​afaelrsanches:monero.social >__ Greetings!     

> __< p​lowsof:matrix.org >__ selsta discovered an issue some time ago which prevented M1/M2 Mac users from using the Monero-GUI to manage a local daemon. A patch fixing this issue (which reduced hash rate/performance for GUI Mac users) has been reverted: https://github.com/monero-project/monero-gui/pull/4229 after sech1 found the root cause [#monero-pow logs](https://libera.monerologs.net/monero-pow/20231019#<clipped message>     

> __< selsta >__ tevador and tobtoht did most of the work     

> __< p​lowsof:matrix.org >__ c290842) . sech1 is also working on adding merge mining into p2pool, links to the repo can be found in the bounty that will reward this effort https://bounties.monero.social/posts/96/1-100m-add-merge-mining-to-p2pool     

> __< p​lowsof:matrix.org >__ tyvm tevador and tobtoht 🫡     

> __< p​lowsof:matrix.org >__ more details of this can be discussed with the professionals in #monero-pow 😄     

> __< p​lowsof:matrix.org >__ Rucknium has been busy.. after detecting a privacy leak from Exodus, proving that it had been fixed: https://monero.town/post/842460 he "counted the number of non-RingCT rings and outputs created between block height 2689608 (v16 fork on 2022-08-14) and 3003871 (2023-10-25)." to aid with the privacy impacts of "Treating pre-RingCT outputs like coinbase outputs" https://github.com/<clipped message>     

> __< p​lowsof:matrix.org >__ monero-project/research-lab/issues/59#issuecomment-1783237506     

> __< p​lowsof:matrix.org >__ all Monerokon videos have been uploaded by ajs_ Monerokon videos https://yewtu.be/watch?v=clCcuAIaAz4&list=PLsSYUeVwrHBm1m7IaU3JiDVb5EC7cn0KG&index=0 .. a talk by BasicSwap dex can be found there. who have this week released a Gui for Windows     

> __< msvb-lab >__ The videos are very good.     

> __< a​js_:matrix.org >__ i need to redo two (noot and midipoet's) as the stream didn't get part of the intro     

> __< o​frnxmr:monero.social >__ I think its more than a GUI, but an exe installer 👀 (basicswapdex windows update)     

> __< a​js_:matrix.org >__ I'll be repairing the videos from locally recorded backups     

> __< a​js_:matrix.org >__ there is also a remote presentation missing on monero standard book     

> __< a​js_:matrix.org >__ will upload soon     

> __< p​lowsof:matrix.org >__ Jberman who will be appearing soon in a chicago meetup sponsored by cakewallet has been finishing [background sync with view only wallet](https://github.com/monero-project/monero/pull/8617) ready for review/testing -  [bounty for this here](https://bounties.monero.social/posts/41/) rbrunner has been testing and providing actionable feedback/issues ... rbrunner also posted the [Ser<clipped message>     

> __< p​lowsof:matrix.org >__ aphis 1 year development report ](https://www.reddit.com/r/Monero/comments/17duyvo/seraphis_wallet_development_1_year_report/)     

> __< o​frnxmr:monero.social >__ vik (Cake):     

> __< p​lowsof:matrix.org >__ Hinto who i notice being here today... released a new GUPAX version recently. their CCS maintenance period is up/due for payout at the end of December, thanks for your support     

> __< r​afaelrsanches:monero.social >__ when this book will be released?     

> __< a​js_:matrix.org >__ there was a recent announcement from their twitter account     

> __< p​lowsof:matrix.org >__ any other items to discuss? all our newsletters have been active: News: [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/) - [The Monero Standard](https://localmonero.co/the-monero-standard) - [Monero Moon](https://www.themoneromoon.com/)     

> __< o​frnxmr:monero.social >__ Cake wallet meetup in chicago in a couple days     

> __< o​frnxmr:monero.social >__ Featuring jberman:  and kayabanerve:  iirc     

> __< o​frnxmr:monero.social >__ Thats.. nov 2 i think. Nit sure exact details     

> __< h​into.janaiyo:matrix.org >__ boog900 finished their 1st milestone, awaiting payment https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/405     

> __< p​lowsof:matrix.org >__ more info on that here https://www.meetup.com/monero-chicago/events/295349648/ hosted by sgp     

> __< o​frnxmr:monero.social >__ Payments will come soon tm     

> __< p​lowsof:matrix.org >__ we#re keeping track of those awaiting payouts, apologies for the delays, everyone should be listed in my update comment here https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/385#note_22625     

> __< p​lowsof:matrix.org >__ valldrac has also posted an update of his milestone 1 nearing completion https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/388#note_22758     

> __< p​lowsof:matrix.org >__ lets try and tackle the ideas list     

> __< p​lowsof:matrix.org >__ https://ccs.getmonero.org/ideas/     

> __< p​lowsof:matrix.org >__ skipping   a. [Add retroactive funding proposal for FCMPs](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/403)    as its waiting to be merged     

> __< p​lowsof:matrix.org >__ b. [dangerousfreedom - wallet work](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/409)     

> __< o​frnxmr:monero.social >__ One thing - website needs to be updated     

> __< o​frnxmr:monero.social >__ It still shows loveras ccs as requires funding     

> __< p​lowsof:matrix.org >__ true     

> __< r​afaelrsanches:monero.social >__ I am already using this wip lib to develop my monero wallet, it it currently in a private repo, but I'll open source it when it is done. You can check some simple demo videos here:     

> __< r​afaelrsanches:monero.social >__ https://drive.proton.me/urls/SRA0MVB4HG#zNrGiHiiWXCI     

> __< r​afaelrsanches:monero.social >__ Password: rafaelrsanches     

> __< r​afaelrsanches:monero.social >__ I am already using this wip lib to develop my monero wallet, it is currently in a private repo, but I'll open source it when it is done. You can check some simple demo videos here:     

> __< r​afaelrsanches:monero.social >__ https://drive.proton.me/urls/SRA0MVB4HG#zNrGiHiiWXCI     

> __< r​afaelrsanches:monero.social >__ Password: rafaelrsanches     

> __< p​lowsof:matrix.org >__ dangerousfreedoms proposal was discussed last week, positive vibes all round. and since then rbrunner along with the no wallet left behind workgroup are providing reviews of their previous work, so this is progressing     

> __< p​lowsof:matrix.org >__ not much else to say really     

> __< o​frnxmr:monero.social >__ The good thing? Even if we voted to merge, we'd still be waiting     

> __< p​lowsof:matrix.org >__ this is true     

> __< nioc >__ up vote for whenever it's ready     

> __< o​frnxmr:monero.social >__ hopefully roads converge and it makes the merge queue in time     

> __< p​lowsof:matrix.org >__ moving on?     

> __< s​needlewoods_xmr:matrix.org >__ +1 for dangerousfreedom     

> __< p​lowsof:matrix.org >__ c. [Core Monero Concepts](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/412)     

> __< p​lowsof:matrix.org >__ in its current form, it would absorb the remaining funds from savandras proposal, and go to funding requiring 1 XMR     

> __< p​lowsof:matrix.org >__ 2 videos are planned. RandomX and Nodes. i shared concerns about nodes perhaps being boring/generic and xenu explained their concept for the video     

> __< o​frnxmr:monero.social >__ Imo nodes and randomx are 1 video     

> __< c​trej:matrix.org >__ What where the other 2 future topics planned?     

> __< c​trej:matrix.org >__ found it     

> __< c​trej:matrix.org >__ •	Random X: Understanding the significance of ASIC resistance     

> __< c​trej:matrix.org >__ •	Breaking down the how-to and the rationale for P2Pool.     

> __< c​trej:matrix.org >__ •	Nodes: Why every Monero enthusiast should consider running one.     

> __< c​trej:matrix.org >__ •	Fungibility: Explaining its essence in the context of Monero.     

> __< p​lowsof:matrix.org >__ thanks, was swimming through my tabs     

> __< c​trej:matrix.org >__ Yeah i think RandomX and Nodes are good picks to do first     

> __< c​trej:matrix.org >__ and yes i think they should be separate videos     

> __< p​lowsof:matrix.org >__ this would be a test then to make a Monero-centric video about nodes, and not just about http / a series of pipes on a decentralised networks 1 node 1 vote     

> __< nioc >__ also think that they should be separate      

> __< p​lowsof:matrix.org >__ cryptocurrency/internet^ not Monero     

> __< c​trej:matrix.org >__ xenu did a good job with the script last time, and I will proof read it too     

> __< c​trej:matrix.org >__ I'm pretty certain it will work out well     

> __< p​lowsof:matrix.org >__ thanks ceetee     

> __< r​ecanman:agoradesk.com >__ Hello, apologizes for being late     

> __< p​lowsof:matrix.org >__ merging this team to produce 2 videos, requiring only 1XMR + remaining funds from savandras has my vote     

> __< c​trej:matrix.org >__ +1     

> __< p​lowsof:matrix.org >__ hi recanman !     

> __< p​lowsof:matrix.org >__ 1 vote is make it 1 video, 2 votes for merge as is, 1 vote for 'meh nods could be boring but i see you will help to make sure its not'     

> __< p​lowsof:matrix.org >__ moving on?     

> __< h​into.janaiyo:matrix.org >__ +1 merge as is     

> __< c​trej:matrix.org >__ cant find the proposal for last vid, was that also 18XMR     

> __< c​trej:matrix.org >__ cant find the proposal for last vid, was that also 18XMR?     

> __< p​lowsof:matrix.org >__ previous was 9xmr for 1 video     

> __< c​trej:matrix.org >__ okey, why do we now have such a jump in price?     

> __< p​lowsof:matrix.org >__ theyve cornered the market / the previous one was at a heavily discounted rate     

> __< p​lowsof:matrix.org >__ im not certain though, vostoemisio can clarify     

> __< p​lowsof:matrix.org >__ iirc the 'real' price vosto's team charges commercial entities for this work is greater than 18xmr / video     

> __< o​frnxmr:monero.social >__ Were not a commercial entity     

> __< p​lowsof:matrix.org >__ expect a clarification on the jump soon 🙏     

> __< r​ecanman:agoradesk.com >__ It seems a bit expensive     

> __< p​lowsof:matrix.org >__ ok lets move on     

> __< p​lowsof:matrix.org >__ e. [Incorporate LLC for MoneroKon](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/415)     

> __< a​js_:matrix.org >__ hi     

> __< p​lowsof:matrix.org >__ hello, i think -events still need to fine tune this idea?     

> __< a​js_:matrix.org >__ so, planning for MoneroKon 2024 has been on hold until the entity issue has been been resolved     

> __< a​js_:matrix.org >__ there has been concerns expressed regarding the number of directors vs the need for decentralization, that an LLC is technically "for profit" vs alignment with Monero ethos, and why even have an entity when invoicing could be outsourced and there is no need for banks since everything should be paid in XMR     

> __< a​js_:matrix.org >__ I understand these concerns     

> __< a​js_:matrix.org >__ on the other hand, the perfect could become an enemy of the good     

> __< o​frnxmr:monero.social >__ https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/415#note_22771     

> __< o​frnxmr:monero.social >__ I'm about to thumb up this comment     

> __< a​js_:matrix.org >__ as no one "owns" MoneroKon and MoneroKon is a community lead initiativ     

> __< a​js_:matrix.org >__ your input on the future direction we take is extremely important     

> __< o​frnxmr:monero.social >__ you cant register a legal entity, with 1 shareholder, and claim no one owns it     

> __< o​frnxmr:monero.social >__ Fantasia     

> __< r​ecanman:agoradesk.com >__ Independent option will be discussed more at the meeting in hour hour     

> __< o​frnxmr:monero.social >__ The latter (no entity) means yes, no one owns it     

> __< r​ecanman:agoradesk.com >__ Independent option will be discussed more at the meeting in one hour     

> __< r​ecanman:agoradesk.com >__ I'm not sure how it would work though     

> __< o​frnxmr:monero.social >__ And everybody is responsible for their own actions     

> __< p​lowsof:matrix.org >__ i think the structure of this LLC has changed (monerobull has decided not to move forward) and other things have been suggested, may need some edits/further discussion?     

> __< a​js_:matrix.org >__ if it is independent option, I would have to step away for the project since I am a known person and have been KYCed     

> __< o​frnxmr:monero.social >__ Why dont YOU open an llc ON YOUR OWN?     

> __< o​frnxmr:monero.social >__ And head it as ceo, yourself     

> __< a​js_:matrix.org >__ yes, we need to work on it more     

> __< o​frnxmr:monero.social >__ Super comfortable if _someone else_ does it, right?     

> __< p​lowsof:matrix.org >__ thats not good as ajs has been heavily involved/crucial to all the monterokons (someone who has attended one can attest)     

> __< a​js_:matrix.org >__ we are open to comments, suggestions     

> __< r​ucknium:monero.social >__ Does it have to be EU-based? What were the reasons that MAGIC was ruled out earlier?     

> __< r​ecanman:agoradesk.com >__ Tax stuff     

> __< o​frnxmr:monero.social >__ Aside from that "i wouldnt touch this project with a 10 foot pole" sounds like a funng thjng to say, after nominating your friend     

> __< r​ecanman:agoradesk.com >__ And KYC afaik     

> __< p​lowsof:matrix.org >__ Monerokon state side would be ok with MAGIC i assume     

> __< o​frnxmr:monero.social >__ usa based     

> __< o​frnxmr:monero.social >__ sgp:     

> __< p​lowsof:matrix.org >__ is there an events meeting today?     

> __< r​ecanman:agoradesk.com >__ Yes     

> __< r​ecanman:agoradesk.com >__ In one hour and 10 minutes     

> __< r​ucknium:monero.social >__ Why is USA-based a barrier?     

> __< o​frnxmr:monero.social >__ Good question     

> __< a​js_:matrix.org >__ someone in US needs to organize it     

> __< r​ucknium:monero.social >__ Since the issue is being reconsidered     

> __< msvb-lab >__ Yes plowsof, there is a events meeting today.     

> __< o​frnxmr:monero.social >__ Thanks recanman     

> __< msvb-lab >__ I think it's in about one hour.     

> __< o​frnxmr:monero.social >__ Someone has recan on ignore?     

> __< r​ucknium:monero.social >__ Anyway, I just wanted to make sure people didn't forget that MAGIC is an option.     

> __< p​lowsof:matrix.org >__ thanks, i think its best to dedicate more time to this proposal in the #monero-events:monero.social meeting     

> __< r​ecanman:agoradesk.com >__ Oh no     

> __< a​js_:matrix.org >__ okay     

> __< a​js_:matrix.org >__ we can move on     

> __< p​lowsof:matrix.org >__ thank you for attending ajs_     

> __< c​trej:matrix.org >__ for one person this chat must be half-empty, lol     

> __< p​lowsof:matrix.org >__ f. [erc: ccs for getmonero and weblate](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/416)     

> __< o​frnxmr:monero.social >__ I upvoted.      

> __< o​frnxmr:monero.social >__ He needs help over there anyway     

> __< r​ecanman:agoradesk.com >__ There are many issues with getmonero website in terms of localization     

> __< p​lowsof:matrix.org >__ ceetee left a nice comment, noticed some typo and made sane suggestions about minimum availability / disclaimers     

> __< o​frnxmr:monero.social >__ hardenedsteel: ,  plowsof hinto @hinto.janaiyo:matrix.org:       

> __< o​frnxmr:monero.social >__ help out     

> __< s​needlewoods_xmr:matrix.org >__ I'd like to see weblate work again     

> __< o​frnxmr:monero.social >__ Id like to see some people contribute ❤️     

> __< p​lowsof:matrix.org >__ erc has access to the vps / pings back end staff about it and performs maintenance tasks himself. weblate should be coming back online soon(tm)     

> __< c​trej:matrix.org >__ After plowsof's answer I'd say 1 hour availability/week is fine. I just want to make sure that there is someone to contact if/when thinks break     

> __< r​ecanman:agoradesk.com >__ Depending on how large it is, I could do arabic     

> __< o​frnxmr:monero.social >__ erc is available everyday most times     

> __< o​frnxmr:monero.social >__ Monero Website     

> __< p​lowsof:matrix.org >__ erc has to at least correct the typo ceetee spotted and respond to the comments     

> __< p​lowsof:matrix.org >__ work in progress list will show a catalogue of pain and suffering dating back ~4 year of website contirbutions     

> __< p​lowsof:matrix.org >__ completed list*     

> __< p​lowsof:matrix.org >__ there are reasons to dislike the proposer, but those reasons do not prevent work on site being done     

> __< p​lowsof:matrix.org >__ i think we can move on awaiting response/edit     

> __< p​lowsof:matrix.org >__ we need to discuss the most important one!     

> __< p​lowsof:matrix.org >__ g. [Monero Selfhosted View-only Web Wallet (with received transaction Telegram/Email/SMS/Discord/Webhook alerts)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/417)     

> __< r​ecanman:agoradesk.com >__ -1     

> __< s​needlewoods_xmr:matrix.org >__ lol     

> __< o​frnxmr:monero.social >__ News folks: its the first view only wallet     

> __< p​lowsof:matrix.org >__ i did not alert the proposer about this community meeting, because hteyve been in the shadows for 3 years following all news     

> __< p​lowsof:matrix.org >__ im sure they are here right now, so let them know how you feel     

> __< o​frnxmr:monero.social >__ rafaelrsanches:  that upvote is sus     

> __< o​frnxmr:monero.social >__ Im watching you 👁️     

> __< r​ecanman:agoradesk.com >__ I don't feel that it is worth 10k     

> __< r​ecanman:agoradesk.com >__ It could make good use of monero-lws     

> __< o​frnxmr:monero.social >__ wallet dev that agrees with that trash hesp ccs for a wallet,     

> __< o​frnxmr:monero.social >__ okieeee     

> __< p​lowsof:matrix.org >__ im still waiting for them to name some wallets other than Touche     

> __< r​afaelrsanches:monero.social >__ Is that a upvote? Sorry, it is just to tag that I read it     

> __< o​frnxmr:monero.social >__ And what do you think of the things they wrote?     

> __< p​lowsof:matrix.org >__ no point to discuss it , until it at least changes to be 'monero-lws' centric / proves their ability / responds to comments     

> __< o​frnxmr:monero.social >__ They follow all community news, but dont know of any wallets that support biew-only     

> __< o​frnxmr:monero.social >__ and dont know about lws     

> __< o​frnxmr:monero.social >__ Or mymonero     

> __< r​ecanman:agoradesk.com >__ The proposer said that it was simple, but was asking for $10K+. I mentioned that, then he responded with a quote from someone:     

> __< r​ecanman:agoradesk.com >__ >Actually, making something simpler for the user is even harder.     

> __< r​ecanman:agoradesk.com >__ >“Simplicity is the ultimate sophistication” (Leonardo Da Vinci)     

> __< o​frnxmr:monero.social >__ anyway     

> __< o​frnxmr:monero.social >__ Close this garbage. Wasting my tine     

> __< p​lowsof:matrix.org >__ downdooting!     

> __< p​lowsof:matrix.org >__ have my enemies left yet? we can discuss my own proposal     

> __< p​lowsof:matrix.org >__ h. [CCS Coordinator](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/418)     

> __< o​frnxmr:monero.social >__ proposer needs to go read 3yrs of monero.observer or revuo or moon etc, then come back without being a bold faced liar who thinks were a bunch of apes who automerge anything     

> __< c​trej:matrix.org >__ no need to discuss     

> __< s​needlewoods_xmr:matrix.org >__ I didn't vote the last one so I have two votes for this ... +2     

> __< o​frnxmr:monero.social >__ Er.. my comment is about wallet, not plowsof lol     

> __< r​ecanman:agoradesk.com >__ I was very surprised, thanks for the clarification     

> __< o​frnxmr:monero.social >__ I just need to check that you didnt lower your rates or something     

> __< nioc >__ plowsof should also read     

> __< o​frnxmr:monero.social >__ 69. Good     

> __< o​frnxmr:monero.social >__ merge     

> __< r​ecanman:agoradesk.com >__ It's always been 69 xmr, no difference     

> __< r​ecanman:agoradesk.com >__ +merge     

> __< o​frnxmr:monero.social >__ 🦧     

> __< o​frnxmr:monero.social >__ Merge     

> __< c​trej:matrix.org >__ Also same hours, no shrinkflation happening here ^^     

> __< c​trej:matrix.org >__ + merge     

> __< c​trej:matrix.org >__ +merge     

> __< o​frnxmr:monero.social >__ Brb, got to log onto my alts     

> __< endogenic >__ my new lws client code handles view only fwiw     

> __< p​lowsof:matrix.org >__ i vote to merge plowsofs proposal, stand up guy     

> __< o​frnxmr:monero.social >__ Tw endogenic. So i take it you dont like this ccs either? Your input matters     

> __< r​ecanman:agoradesk.com >__ endogenic, could you show me where?     

> __< endogenic >__ and is mega advanced in terms of handling issues that arent super obvious. i'd have released it but i'm working on this annoying bug in wasm still     

> __< o​frnxmr:monero.social >__ "plowsof is only allowed to stand up for washroom breaks"     

> __< p​lowsof:matrix.org >__ thank you for the kind comments here/on the proposal <3     

> __< endogenic >__ just saying - my work is done already basically, just this wasm bug and the finished writeup -     

> __< r​ecanman:agoradesk.com >__ Please let me know when you release it endogenic, I'd like to use it     

> __< endogenic >__ ok     

> __< p​lowsof:matrix.org >__ thanks for the update endogenic, does woodser know about this wasm bug? maybe they can help?     

> __< endogenic >__ i doubt it     

> __< p​lowsof:matrix.org >__ last not not least we have   i. [v1docq47 - monerotopia 2023 (part 2) and monerokon 2023 voiceovers and working on xmr.ru](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/420)     

> __< o​frnxmr:monero.social >__ endogenic: ping plowsof if you need a hand/extra eyes, and we'll get you one/some, ya?     

> __< o​frnxmr:monero.social >__ Alt     

> __< o​frnxmr:monero.social >__ > thanks for the update endogenic, does woodser know about this wasm bug? maybe they can help?     

> __< o​frnxmr:monero.social >__ Meant to quote this     

> __< o​frnxmr:monero.social >__ How did last ccs go?     

> __< p​lowsof:matrix.org >__ i have shared this proposal in the #xmr.ru:matrix.org yesterday and await feedback, ajs mentioned the other day about considering using software / ai to handle some things     

> __< p​lowsof:matrix.org >__ Lovera speaks russian and could also leave some feedback     

> __< o​frnxmr:monero.social >__ He usually gets his funding     

> __< o​frnxmr:monero.social >__ and does the work as describes afaik     

> __< o​frnxmr:monero.social >__ And the funding, i assume, comes from his supporters / locals     

> __< c​trej:matrix.org >__ Feedback from someone in here that speaks russian would be appreciated     

> __< c​trej:matrix.org >__ The two people how commented are not familiar to me     

> __< o​frnxmr:monero.social >__ I voted merge last time for these reason, but perhaps wait 2 weeks for feedback     

> __< c​trej:matrix.org >__ *who commented     

> __< p​lowsof:matrix.org >__ indeed, we just await feedback on this one, v1docq47 has been contributing for years     

> __< p​lowsof:matrix.org >__ sorry for going over the hour, and i have some bad news regarding MOONS... the proposal expired   j. [Rent ad space on r/CryptoCurrency to promote MoneroKon 2024](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/419) expired / closed     

> __< r​ucknium:monero.social >__ Not going to discuss jeffro256's proposal?     

> __< p​lowsof:matrix.org >__ checks notes     

> __< p​lowsof:matrix.org >__ https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/421     

> __< p​lowsof:matrix.org >__ the MOONS proposal was not removed/replaced, my bad     

> __< o​frnxmr:monero.social >__ Who? Jk     

> __< r​ucknium:monero.social >__ One of the tasks that jeffro256 did for his last CCS was to develop (finally!) a description of wallet2's decoy selection algorithm. I read it. It is very clear documentation IMHO. Then I used it to create a closed-form mathematical formula of the decoy selection algorithm.     

> __< s​needlewoods_xmr:matrix.org >__ +1     

> __< p​lowsof:matrix.org >__ previous proposal https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/390 / helping Rucknium with consensus rules / decoy selection , bettering the entire ecosystem to name but a few things he has been doing     

> __< c​trej:matrix.org >__ merge jeffro     

> __< r​ucknium:monero.social >__ A paper released earlier this year complained that there wasn't a mathematical formula. So those researchers should be satisfied customers now!     

> __< o​frnxmr:monero.social >__ jeffro256:  does this "full-time" work ob jamtis etc, imply the work on coinbase is paused, or still "ready when we are" / WIP     

> __< r​ucknium:monero.social >__ More importantly, the mathematical formula is necessary to develop improvements to the decoy selection algorithm.     

> __< r​ucknium:monero.social >__ And it can be used by wallets that do not use wallet2 to check that their decoy selection algorithm does not deviate from the standard. If it does deviate, then privacy is worse for their users.     

> __< p​lowsof:matrix.org >__ perfect     

> __< p​lowsof:matrix.org >__ can we introduce any fake delays on this one to distract from merge delays?     

> __< p​lowsof:matrix.org >__ i  cant think of any     

> __< r​ucknium:monero.social >__ Here are the docs that jeffro wrote: https://github.com/jeffro256/monero/blob/decoy_selection_md/docs/DECOY_SELECTION.md     

> __< p​lowsof:matrix.org >__ semi-related: Rucknium is isthmus' proposed work in their closed ccs proposal still required?     

> __< r​ucknium:monero.social >__ Here's my draft of the mathematical formula based on the docs: https://www.overleaf.com/read/ndbtkwrbrdjq     

> __< p​lowsof:matrix.org >__ jeffro has also helped/helping boog900 with their work on consensus rules     

> __< r​ucknium:monero.social >__ isthmus has given me some of what he said he would do. Some of the nonstandard txs that he was looking for     

> __< r​ucknium:monero.social >__ We both planned to look for nonstandard txs. The Exodus Desktop wallet issue that I found was one of the results from that.     

> __< o​frnxmr:monero.social >__ ✌️ thanks plowsof     

> __< p​lowsof:matrix.org >__ thanks all for attending! hopefully we can discuss a CCS proposal from Rucknium soon 🙏     

> __< msvb-lab >__ Dankon for a good meeting everyone.     

> __< r​ecanman:agoradesk.com >__ Goodbyee     

> __< r​ecanman:agoradesk.com >__ Goodbye     

> __< r​ucknium:monero.social >__ You you want a statistical Monero problem to be researched, let me know. There are a lot of things to work on. The community can help set priorities.     

> __< r​ucknium:monero.social >__ If you *     

> __< r​ucknium:monero.social >__ Some people want PocketChange privacy to be researched, for example.     

> __< j​effro256:monero.social >__ On that Coinbase decoy selection PR ?     

> __< j​effro256:monero.social >__ You’ll have to convince people that it’s a net benefit to privacy     

> __< r​ucknium:monero.social >__ IMHO, it may be paused until we figure out the privacy cost-benefit to making large changes to the wallet2 decoy selection algorithm between hard forks.     

> __< r​ucknium:monero.social >__ My research discussion note "Formula for Accuracy of Guessing Monero Real Spends Using Fungibility Defects" is a step toward figuring that out: https://github.com/Rucknium/misc-research/tree/main/Monero-Fungibility-Defect-Classifier/pdf     

> __< r​ucknium:monero.social >__ I think there is a large privacy benefit with few downsides if it is implemented at a hard fork. All wallets would have to upgrade, so there would not be multiple wallet2 decoy selection algorithms being used by users.     

> __< p​lowsof:matrix.org >__ i missed   d. [escapethe3RA Monero Observer maintenance (2023 Q4)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/414)    - please forgive me , i am half blind and there where alot of proposals     

> __< p​lowsof:matrix.org >__ the community messages on monero.observer are very handy, one reminded me that there is a total of 19.5XMR available for contributing to the passport Monero wallet https://monero.observer/legalcomment-2/     


Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

## plowsof | 2023-10-30T22:23:48+00:00
```
21:10:08 <m-relay> <v​ostoemisio:matrix.org> Doubled length, 2 min instead of 1 per vid. Our first proposam and video was planned and budgeted to be 1 min but we noticed we couldn't fit a solid script within that timeframe. Anyway, we went beyond and it came out to about 2min 15 sec or so iirc
21:11:06 <m-relay> <v​ostoemisio:matrix.org> > <@ctrej:matrix.org> okey, why do we now have such a jump in price?
21:11:07 <m-relay> <v​ostoemisio:matrix.org> In reply to @ctrej:matrix.org
21:11:07 <m-relay> <v​ostoemisio:matrix.org> okey, why do we now have such a jump in price?
21:11:08 <m-relay> <v​ostoemisio:matrix.org> Doubled length, 2 min instead of 1 per vid. Our first proposal and video was planned and budgeted to be 1 min but we noticed we couldn't fit a solid script within that timeframe. Anyway, we went beyond and it came out to about 2min 15 sec or so iirc
22:09:26 <m-relay> <c​trej:matrix.org> >So, I propose that we create an animation series featuring short (**1 min or so**), ELI5-style explainer videos that break down the key concepts of how Monero works in a simple and digestible way that could easily be shared every time we, the community, face misleading comments. 
22:09:26 <m-relay> <c​trej:matrix.org> https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/387#note_21253
22:11:43 <m-relay> <c​trej:matrix.org> Claim checks out. I didn't even realized that we got more then what what we paid for initially.
```

# Action History
- Created by: plowsof | 2023-10-21T13:40:57+00:00
- Closed at: 2023-11-05T18:47:23+00:00
