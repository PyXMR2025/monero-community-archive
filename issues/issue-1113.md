---
title: 'Monero Community Workgroup Meeting: November 23rd 16:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1113
author: plowsof
assignees: []
labels: []
created_at: '2024-11-20T16:20:54+00:00'
updated_at: '2024-12-08T07:55:52+00:00'
type: issue
status: closed
closed_at: '2024-12-08T07:55:52+00:00'
---

# Original Description
Location: [Libera.chat, #monero-community](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-community:monero.social?via=matrix.org&via=monero.social)

[Instructions for joining the monero.social Matrix server.](https://www.getmonero.org/resources/user-guides/join-monero-matrix.html)

Time
16:00 UTC [Check your timezone](https://www.timeanddate.com/worldclock/converter.html)

Moderator: plowsof

Please reach out in advance of the meeting if you would like to propose an agenda item.

Proposed Meeting Items:

1. Introduction
2. Greetings
3. Community highlights    
News: [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/)
4. [CCS updates](https://ccs.getmonero.org/)    
  a. [Carrot animated video](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/506)    close
  b. [CryptoCheckout WordPress plugin (for WooCommerce) & Shopify app](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/514)    close
  c. [Monerotopia 2024 Marketing and Publicity](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/515)    pre-approved pending invoice
  d. [Gingeropolous 1TB MRC upgrade](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/516)    
  e. [v1docq47 - monerotopia 2024 voiceovers and working on xmr.ru](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/517)    
  f. [Add monero-[serai, wallet] audit](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/518)    
5. Workgroup reports    
  a. Dev workgroup
  b. Localization workgroup
  c. Outreach workgroup
  d. Events workgroup - [MoneroKon 2025](https://monerokon.org)
  e. Website workgroup
  f. Policy workgroup
  g. Research workgroup
  h. [Seraphis Migration workgroup](https://github.com/seraphis-migration)
6. Open ideas time    
7. Confirm next meeting date/time    

[Previous meeting including logs](https://github.com/monero-project/meta/issues/1106)    

Meeting logs will be posted here afterwards.    

# Discussion History
## plowsof | 2024-12-08T07:55:28+00:00
Logs 
> __< plowsof >__ Meeting in 1 hr https://github.com/monero-project/meta/issues/1113     

> __< r​ottenwheel:kernal.eu >__ As long as you let one decide between persistent and stateless, I'm game. vthor     

> __< r​ottenwheel:kernal.eu >__ Good luck figuring out how to do persistent though lol, will be interesting to see.     

> __< vthor >__ rottenwheel: I don't like really the thought to safe the seeds on the same microSD card - although it is probably the cheapest option, it is not the best. On my research for NFC payment on weak hardware I found cheap SPI secure elements and SPI flash, which could be sourced in quantities of 100 for below $5.     

> __< r​ottenwheel:kernal.eu >__ vthor the more you talk about ways to implement persistent state for XMRSigner, the less I like the idea, and I already oppose and disagree with it 100% as-is...     

> __< vthor >__ rottenwheel, It will result in two different build, I don't like incactive code in the image. Could even be happen to go to 3 version (but not sure, need some time to think and thinkering about and analyze different threat models - and best would be to get some actual user input, why they want to have certain version)     

> __< r​ottenwheel:kernal.eu >__ Beyond my bias, sounds stupid, for lack of a better word, to add more components, as that would effectively bar current SeedSigner users and owners from trying XMRSigner in the first place...     

> __< r​ottenwheel:kernal.eu >__ Don't break the stateless concept. What the other two individuals claim to be a UX hurdle, is the main selling point of the SeedSigner project.     

> __< r​ottenwheel:kernal.eu >__ I find it hard to understand how instead of looking at it from the security perspective, they latch on the UI/UX inconvenience...     

> __< r​ottenwheel:kernal.eu >__ Cool, yeah, all WIP. I've said my piece. Congrats on getting fully funded, sir. 😊     

> __< vthor >__ No, the stateless version will be always 100% staeless, not even microSD storing. And a version with microSD storing, need to see... And discous with actual user.     

> __< vthor >__ rottenwheel, thank you very much! Hopen to see you in CDMX, but missed you.     

> __< vthor >__ Need to walk the white monster before he pees on my feets. afk.     

> __< plowsof >__ Meeting time https://github.com/monero-project/meta/issues/1113      

> __< plowsof >__ greetings!     

> __< o​frnxmr:monero.social >__ howdy     

> __< plowsof >__ whats been going on since the last meeting? Monerotpia happened https://monerotopia.com/      

> __< 0​xfffc:monero.social >__ Hello everyone     

> __< plowsof >__ MKC3 call for workshops/presentations up https://x.com/MoneroKon/status/1860321346380533986 - ajs      

> __< plowsof >__ 0xfff made a PR making some improvements to --no-initial-sync and wallet-rpc?     

> __< plowsof >__ kewbit teased a CCS update for the haveno-gui... the monero -serai/wallet ccs proposal from kayabanerve has been merged https://ccs.getmonero.org/funding-required/     

> __< o​frnxmr:monero.social >__ Make wallet-rpc great for the first time since bytecoin     

> __< msvb-lab >__ Hello.     

> __< plowsof >__ in my recent ccs update, i tallied up the funds we've repurposed or donated to the general fund from abandonned ccs proposals. 384.06 repurposed. 161.85 returned to the general fund https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/503#note_27312     

> __< vthor >__ Hi!     

> __< 0​xfffc:monero.social >__ https://github.com/monero-project/monero/pull/9579     

> __< o​frnxmr:monero.social >__ Boooo 👎     

> __< plowsof >__ i look forward to testing this 0xfffc thank you     

> __< o​frnxmr:monero.social >__ We should instead repurpose the old gemeralfund btc and xmr addresses funds from black hole to transparency report     

> __< 0​xfffc:monero.social >__ ( You’re welcome. My pleasure. )     

> __< ofrnxmr >__ https://github.com/monero-project/monero/pull/9579 one of @0xfffc's fixes     

> __< plowsof >__ thanks     

> __< plowsof >__ XMRSigner from vthor originating from repurposed funds :) but now his own work has been funded (was discussed today here)      

> __< plowsof >__ ofrnxmr did you mention wallet-rpc using insane bandwidth amounts if left running 24/7?     

> __< plowsof >__ ive never ran it at home so wouldn't notice      

> __< 0​xfffc:monero.social >__ I believe this should alleviate the problem: https://github.com/monero-project/monero/pull/9574     

> __< plowsof >__ News: [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/)     

> __< plowsof >__ oh, another PR      

> __< o​frnxmr:monero.social >__ Yes     

> __< plowsof >__ Siren/Stnby of digilol/moneropay are probably effected , as well as alot of merchants/swappers then      

> __< o​frnxmr:monero.social >__ Like gb's per hr if a service utilizes close_wallet inbeteren open_wallet calls     

> __< plowsof >__ good catch      

> __< 0​xfffc:monero.social >__ Yes. It was basically days (or even months of? of computation wasted overall.     

> __< o​frnxmr:monero.social >__ leads to very very much increased time to respond the longer the service is running     

> __< o​frnxmr:monero.social >__ Resyncs the same blocks over and over.. and over again     

> __< vthor >__ 0xfffc: but this will only avoid long opening time on open a wallet, would it be easy to quick fix the also the restore wallet from seed? (I suspect the long time on weak hardware comes from generating addresses on restore)     

> __< plowsof >__ perhaps this is when i need to kill the process by grabbing its pid      

> __< o​frnxmr:monero.social >__ I think there still may be an off-by-1 issue, as it syncs 2 blocks everytime it receives 1 more now     

> __< 0​xfffc:monero.social >__ Great catch. I will try to fix it. Will dm you about it. 🙏🏻     

> __< s​tnby:kernal.eu >__ Huh?     

> __< plowsof >__ "if a service utilizes close_wallet inbeteren open_wallet calls" - ofrnxmr above. if moneropay does this then could be suffering from delays/bandwidth usage      

> __< o​frnxmr:monero.social >__ tldr: these wallet-rpc issues should help projects, like moneropay, to function better     

> __< o​frnxmr:monero.social >__ It also doesnt seem to refresh at open like its supposed to. Takes 20secs     

> __< s​iren:kernal.eu >__ Yeah the resync thing is very annoying     

> __< plowsof >__ nice     

> __< plowsof >__ anything else to bring up? else we can move on to the ccs ideas      

> __< plowsof >__ articmine shared thoughts on FCMP in MRL today which raised further discussion https://libera.monerologs.net/monero-research-lab/20241123      

> __< plowsof >__ specifically the "post on  FCMP++ costs and transaction sizes"     

> __< plowsof >__ MRL can weigh in on this further.. now then      

> __< plowsof >__ moving on, ccs ideas:     

> __< plowsof >__   a. [Carrot animated video](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/506)         

> __< plowsof >__ close/merge?      

> __< plowsof >__ not enough positive engagement around this, looks like it will be closed      

> __< dEBRUYNE >__ plowsof: As a side note, was the FCMP++ video officially released, or not yet?      

> __< o​frnxmr:monero.social >__ I think this is a close, no engagement from proposer     

> __< plowsof >__ vostoemissio released a video , yes, thanks      

> __< o​frnxmr:monero.social >__ Not yet, xenu and vost redoing some of the script     

> __< o​frnxmr:monero.social >__ The video they released was a pre-release, and kaya commented some inaccuracies     

> __< o​frnxmr:monero.social >__ So theyre going to fix up and rerelease     

> __< plowsof >__ thanks debruyne, here is vostos comment, open for feedback as above https://libera.monerologs.net/monero-community/20241121#c462513     

> __< plowsof >__ closing Carrot animated video      

> __< plowsof >__   b. [CryptoCheckout WordPress plugin (for WooCommerce) & Shopify app](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/514)         

> __< plowsof >__ close/merge?     

> __< o​frnxmr:monero.social >__ Close     

> __< o​frnxmr:monero.social >__ Oh, for community news     

> __< o​frnxmr:monero.social >__ Haveno Development  and #haveno:development are the new homes for haveno dev on matrix and irc     

> __< plowsof >__ a close from me. also special thanks for mrnaif from bitcart.io for sharing his insight regarding getting on to the shopify app store and such      

> __< plowsof >__ the proposer of the above didnt even know how it was done and dropped the premise immediately      

> __< plowsof >__ closing cryptocheckout      

> __< plowsof >__   c. [Monerotopia 2024 Marketing and Publicity](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/515)         

> __< plowsof >__ this was pre-approved, pending the upcoming update from geonic , we can move on unless that is on hand      

> __< plowsof >__ at hand*     

> __< o​frnxmr:monero.social >__ +1 plowsof     

> __< dEBRUYNE >__ plowsof: ty     

> __< o​frnxmr:monero.social >__ Seems the event went well though. Congrats     

> __< plowsof >__ 👏     

> __< plowsof >__   d. [Gingeropolous 1TB MRC upgrade](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/516)         

> __< o​frnxmr:monero.social >__ Mrl i think liked this, but i again have mt reservations about continuously trusting folks who are irresponsible with our security and privacy     

> __< o​frnxmr:monero.social >__ I think someone else should run the mrl lab pcs     

> __< plowsof >__ 20 xmr, ram for MRL who expressed a need for it , and with positive updoots      

> __< o​frnxmr:monero.social >__ Ginger refused to share the ips that he was forwarding to, and it took community whitehats to pry the info from internet logging or nslookup     

> __< o​frnxmr:monero.social >__ And he deleted ips and still refused to share     

> __< r​ucknium:monero.social >__ Maybe gingeropolous can do a sysadmin security short course :)     

> __< r​ucknium:monero.social >__ I wouldn't mind doing one myself     

> __< o​frnxmr:monero.social >__ Dodges any questions about the subject     

> __< o​frnxmr:monero.social >__ i dont think it eas irresponsible due to being uneducated, but simply due to negligence     

> __< o​frnxmr:monero.social >__ then tried to cover it up     

> __< o​frnxmr:monero.social >__ And still pretends like nothing happened     

> __< h​into:monero.social >__ hello     

> __< l​ordx3nu:matrix.org >__ Re fcmp video: revisions made just waiting for Luke     

> __< l​ordx3nu:matrix.org >__ Re carrot: vosto and I have expressed interest for doing an animated vid for this though not sure if there is enough interest     

> __< plowsof >__ Rucknium is one of the main consumers of ram, if i could click my heels then Rucknium would be setting the hardware up in house for other MRL members     

> __< l​ordx3nu:matrix.org >__ Waiting for Luke to sign off*     

> __< plowsof >__ blame kayabanerve for any issues moving forward, noted      

> __< l​ordx3nu:matrix.org >__ Thanks     

> __< plowsof >__ thanks for sharing the update Xenu 💪     

> __< l​ordx3nu:matrix.org >__ 😁     

> __< r​ucknium:monero.social >__ Most of the expense of the MRC hardware was covered by gingeropolous. The implicit deal, I think, is that ging provides most of the hardware free-of-charge since he's mining Monero on it when the CPU threads are free. I hope that ging gives a fuller explanation for what happened with node.moneroworld.com , but consider that getting greenfield owned or rented hardware would be expe<clipped message>     

> __< r​ucknium:monero.social >__ nsive for the CCS.     

> __< r​ucknium:monero.social >__ Even with this proposal, ging is paying for the machine. The CCS is just for the RAM (which isn't really needed for mining)     

> __< o​frnxmr:monero.social >__ Yeah, lets just keep funding his mining operation. I think that's messed up     

> __< plowsof >__ merging gingeropolous - we could fund sech1 to purchase expensive monero mining equipment and let MRL use it upon request too      

> __< o​frnxmr:monero.social >__ Didnt we pay for the rigs with prior ccs' too? I might be mistaken here     

> __< r​ucknium:monero.social >__ No, he doesn't need this RAM for mining     

> __< plowsof >__ ah ok     

> __< o​frnxmr:monero.social >__ Why not just let ruck buy the ram for himself     

> __< r​ucknium:monero.social >__ With a prior CCS, large SSDs were purchased. Again, that's what research needs, not mining     

> __< nioCat >__ we are not funding his mining operation, his mining operation is being used by MRL     

> __< r​ucknium:monero.social >__ nioCat has it right     

> __< o​frnxmr:monero.social >__ thank niocat     

> __< plowsof >__ thanks mbull      

> __< plowsof >__ moving on     

> __< h​into:monero.social >__ Rucknium: curious, what is the setup for storing the DB in ram?     

> __< o​frnxmr:monero.social >__ thanks mbll     

> __< r​ucknium:monero.social >__ In an R `data.table`     

> __< r​ucknium:monero.social >__ You want the columns?     

> __< h​into:monero.social >__ are those stored/reusable by other programs?     

> __< r​ucknium:monero.social >__ Basically no. It's for statistical analysis. You cannot run the blockchain from this, if that's what you are asking.     

> __< plowsof >__   e. [v1docq47 - monerotopia 2024 voiceovers and working on xmr.ru](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/517)         

> __< plowsof >__ i've shared this proposal in the xmr.ru matrix room, continued positive support that gets him merged is coming in      

> __< o​frnxmr:monero.social >__ Voting merge on account of successful history and always getting funding     

> __< r​ucknium:monero.social >__ An R `data.table` is extremely fast for statistical analysis, especially for data that has a hierarchical structure like Monero: block -> tx -> ring -> ring member     

> __< r​ucknium:monero.social >__ https://h2oai.github.io/db-benchmark/     

> __< r​ucknium:monero.social >__ The downside is that it keeps the data in RAM, so if you have lots of data, you need lots of RAM.     

> __< plowsof >__ looks like v1docq47 will be merged shuld the trend in feedback continue after its sat for a bit longer     

> __< plowsof >__ Any other business?      

> __< plowsof >__ Are we all waiting for a general fund transparency report?     

> __< o​frnxmr:monero.social >__ Generalfund 0 1 2 3 4 and 5     

> __< h​into:monero.social >__ does each program that needs `data.table` map LMDB data to a `data.table` on startup before continuing?     

> __< plowsof >__ we can end the meeting here then. thank you all for attending      


Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: plowsof | 2024-11-20T16:20:54+00:00
- Closed at: 2024-12-08T07:55:52+00:00
