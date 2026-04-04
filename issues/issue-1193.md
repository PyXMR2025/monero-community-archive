---
title: 'Monero Community Workgroup Meeting: April 26th 16:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1193
author: plowsof
assignees: []
labels: []
created_at: '2025-04-25T09:31:39+00:00'
updated_at: '2025-05-21T07:14:42+00:00'
type: issue
status: closed
closed_at: '2025-05-21T07:14:42+00:00'
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
  a. [Btcpayserver plugin](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/538)    
  b. [Monero Browser Wallet](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/555)    
  c. [Haveno iOS and Android App](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/570)    
  e. [Add jeffro256-full-time-2025Q2](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/578)    
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
    -   d. [OPENENET-MS01-MoneroSpace-Decentralized-Satellite-Network](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/577)    
8. Confirm next meeting date/time    
[Previous meeting including logs](https://github.com/monero-project/meta/issues/)    

Meeting logs will be posted here afterwards.    


# Discussion History
## spirobel | 2025-04-26T10:13:17+00:00
General recommendations:

1. Move the CCS discussions to the front, the banter to the back. 
2. Pepare the CCS conversations thoroughly. Outline under which circumstances merge or close is recommended. Prevent people from introducing new contentious points that have not been clearly articulated beforehand in the gitlab comments. This prevents derailing / prolonging the conversation endlessly. 
3. communicate clearly, don't use irony outside of the banter section at the end.

The expectation stated was that CCS discussions are resolved in 1 month.

Example CCS proposal dialogue preperation:

### a. [Btcpayserver plugin](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/538) 3 months overdue
from the discussion in the BtcPay matrix channel:

sgp_:napoly: I don't want to park it under MAGIC anymore
sgp_:Anyway, I'm sorry for any past animosity and I just want to help ensure the plugin remains supported, and my preference is for this proposal to be the means that accomplishes that
**-> so sgps comment to be considered resolved. (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/538#note_29062)**

**conditions for merge / close:**

resolve comment raised by ofrnxmr:

> i have np with lws support, but if the ccs dropped lws stuff, imo its essentially limited to my proposed m1 (below). Whether that is a good or bad thing, is uo for debate
> 
> M1: Finish GUI for remote node configuration [started here](https://github.com/btcpayserver/btcpayserver/pull/6239).. making sure to address [this comment](https://github.com/btcpayserver/btcpayserver/pull/6239#issuecomment-2481847461)
> 
> M2: multi-wallet support via LWS and/or wallet-rpc + adapt M1 and M2 for lws (probably 70% of the ccs). + "wallet setup interface (create*, import, export*, update*)" for lws
> M3: setup (new users) and migration (existing users) documentation
> 
> re m2. Might be a bad idea for spend keys to touch the server, so might should Not create wallets(rpc), and be import(view wallet) only.
> i don't know where export-wallet would make sense? Or what update-wallet means(change wallet?)?
> anyway, sounds like duplicate of "Onboarding redesign to support both wallet-rpc and lws"

src: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/538#note_29353
	
**do these changes made by deverickapollo cover that?**

> The changes made further refined the milestones and goals to more accurately represent the work planned for the proposal:
> 
> Considered community feedback and prioritized existing maintenance and feature requests related to daemon and wallet management
> 
> Milestone 1:
> 
> Adding Unit Testing and Code Coverage provides a layer of sanity needed to manage releases over time. This comes with an expectation that new code include unit testing
> 
> 
> Milestone 2/3
> 
> Prioritize daemon/wallet UI configuration improvements for 2 and consolidate all lws development into milestone 3
> Add release as deliverable
> 
> 
> Milestone 4
> 
> Push review of remote note implementation until after lws development to ensure alignment
> 
> 
> 
> 
> Confirm expectations following [@NicolasDorier](https://github.com/NicolasDorier) initial port of the plugin
> Added CoinCards as the sponsor of our initial research at MoneroTopia 2024
> Emphasized the expectation from the BTCPay team to ensure everyone understands BTCPay would like us to host all components of this integration
> Created [org](https://github.com/btcpay-monero) to host plugin following migration
> Highlight the value of an open source payment processing solution to enable third-party hosting
> Increase timeline to ensure we're not rushing the deliverable
> 
> For meetings, [@napoly](https://github.com/napoly) and I have discussed implementation details with vtnerd regarding milestone 3 with monero-lws. Over the past few weeks, I've also been discussing the availability of monero-integrations for a home but serhack has been too busy to continue.

https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/538#note_29346
	
there has been some discussion about that in the btcpay matrix chat as well: https://matrix.to/#/#btcpay-monero:matrix.org
participants deverickapollo, ofrnxmr, plowsof should report if they consider this resolved (and if not why + what would need to happen to resolve it from their point of view)
	
### b. [Monero Browser Wallet](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/555) 1 month overdue
**updates:** 
since the last meeting there have been more upvotes and a supportive comment by anhdres:

> "I don't see the downside of @spirobel developing this, even if it's not as secure as a standalone hardcore Monero wallet, it could untap a new batch of users if speedy/easy integration with web services are needed.
> Regarding the amount of XMR requested, I don't have the technical background to be able to judge if it's expensive or cheap, but my position when it comes to the CCS is that if the proposal is serious we should set it live and let the donors decide if it's worth funding or not." 

https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/555#note_29654

**no open questions left to discuss**
### c. [Haveno iOS and Android App](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/570) due

conditions for merge / close:
The stated goal of the CCS is: "decouple Haveno users from desktop computer and **allow trading on the go.**"

At the same time the CCS proposer acknowledges this comment with a thumbs up: **"This is not standalone and standalone mobile support itself is not really feasible."**

This logical inconsistency needs to be resolved to move forward with this proposal.

### e. [Add jeffro256-full-time-2025Q2](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/578) on time
   uncontroversial merge given the contributors prior CCS track record and the urgency+importance of work on Carrot/FCMP

## NorrinRadd | 2025-04-26T14:37:27+00:00
> conditions for merge / close: The stated goal of the CCS is: "decouple Haveno users from desktop computer and **allow trading on the go.**"

This is accomplished. 

## spirobel | 2025-04-26T15:18:03+00:00
@NorrinRadd  
> This is accomplished.

How is it accomplished? Will there be an issue if a trade is in progress and the user is disconnected from their haveno node running on their desktop / laptop

## NorrinRadd | 2025-04-26T15:23:45+00:00

> [@NorrinRadd](https://github.com/NorrinRadd)
> 
> > This is accomplished.
> 
> How is it accomplished? Will there be an issue if a trade is in progress and the user is disconnected from their haveno node running on their desktop / laptop

Functionality is available away from the computer. Trades can be performed from anywhere (this is tested working). Trades continue if connectivity is lost as well. 

## plowsof | 2025-05-21T07:13:51+00:00
Logs 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
> **\<plowsof\>** Meeting time https://github.com/monero-project/meta/issues/1193     
    
> **\<plowsof\>** greetings!     
    
> **\<msvb-lab\>** Hello.     
    
> **\<plowsof\>** have any recent events highlights to bring up? please share     
    
> **\<plowsof\>** "alpha stressnet for FCMP++ is scheduled to be ready by May 21st, so get ready!" via jeffro256      
    
> **\<j​effro256:monero.social\>** Howdy     
    
> **\<s​pirobel:kernal.eu\>** hi     
    
> **\<s​pirobel:kernal.eu\>** lets share at the end. 12am here. lets go through the proposals and banter afterwards     
    
> **\<plowsof\>** repo link for atsamd21's haveno app https://github.com/atsamd21/Haveno-app      
    
> **\<s​pirobel:kernal.eu\>** https://github.com/monero-project/meta/issues/1193#issuecomment-2832012597     
    
> **\<plowsof\>** your local time does not dictate the meeting agenda      
    
> **\<ofrnxmr\>** greeting and updates first     
    
> **\<s​yntheticbird:monero.social\>** hi     
    
> **\<plowsof\>** unless of course you are the moderator (also possible)     
    
> **\<c​t:xmr.mx\>** hello :)     
    
> **\<plowsof\>** nor does your lack of sleep bring urgency what so ever     
    
> **\<s​pirobel:kernal.eu\>** https://x.com/rottenwheel1/status/1812412616146297197     
    
> **\<plowsof\>** 👋     
    
> **\<s​pirobel:kernal.eu\>** is it this one? https://x.com/rottenwheel1/status/1812412616146297197     
    
> **\<plowsof\>** 👀     
    
> **\<s​pirobel:kernal.eu\>** unstructured meetings just waste everyones time.     
    
> **\<a​tsamd21:matrix.org\>** No im working on a new one     
    
> **\<NorrinRadd\>** Hi      
    
> **\<plowsof\>** you are unhappy with the structure, they are not unstructured. you are free to moderate you own communiyt meeting at a suitable local time , or the same time should people want that      
    
> **\<plowsof\>** the community meetings are majority 'ccs proposals', people have voiced their concerns about this too      
    
> **\<s​pirobel:kernal.eu\>** cool. Would be interested to hear your take on the haveno proposal     
    
> **\<nioc\>** 5xmr for 129GBP, how is that real     
    
> **\<plowsof\>** stagenet are cheaper to mine      
    
> **\<nioc\>** oh     
    
> **\<plowsof\>** https://www.monerokon.org/ , get ya tickets if you wish to attend      
    
> **\<plowsof\>** anyone have anything else to highlight?     
    
> **\<ofrnxmr\>** update your monerods     
    
> **\<j​effro256:monero.social\>** The XMR/GBP rate is "correct" in the trade on the top, and than 10x lower in the bottom trade. Almost like someone forgot to move a decimal place, lol. But yeah it's fake XMR and fake GBP at the end of the day on stagenet     
    
> **\<j​effro256:monero.social\>** Cool if true, I know people have been waiting a long time for a mobile Haveno application     
    
> **\<plowsof\>** lets move on to the ccs proposals , starting with the easiest      
    
> **\<plowsof\>**   e. [Add jeffro256-full-time-2025Q2](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/578)         
    
> **\<ofrnxmr\>** Merge     
    
> **\<nioc\>** +1     
    
> **\<d​everickapollo:matrix.org\>** Good move     
    
> **\<s​yntheticbird:monero.social\>** monero.social is dyin     
    
> **\<s​pirobel:kernal.eu\>** merge     
    
> **\<s​yntheticbird:monero.social\>** +1     
    
> **\<d​everickapollo:matrix.org\>** also merge     
    
> **\<plowsof\>** pigeons : any issues with the matrix server?      
    
> **\<plowsof\>** thanks for feedback     
    
> **\<ofrnxmr\>** Yeah its dying     
    
> **\<plowsof\>**   a. [Btcpayserver plugin](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/538)         
    
> **\<ofrnxmr\>** Very slow     
    
> **\<plowsof\>** https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/538#note_29756 recent update here     
    
> **\<ofrnxmr\>** My issues with btcpay have been resolved for the most part, retracted my nack     
    
> **\<d​everickapollo:matrix.org\>** Changes from feedback merged. Should be good to go     
    
> **\<s​pirobel:kernal.eu\>** nice so we can merge     
    
> **\<s​pirobel:kernal.eu\>** sgp also retracted     
    
> **\<s​pirobel:kernal.eu\>** saw that in the btcpay matrix     
    
> **\<plowsof\>** thanks for the changes      
    
> **\<s​yntheticbird:monero.social\>** no i disagree, dont merge, but i don't have any reason     
    
> **\<s​yntheticbird:monero.social\>** 👍️     
    
> **\<s​yntheticbird:monero.social\>** /s     
    
> **\<s​yntheticbird:monero.social\>** /jk     
    
> **\<d​everickapollo:matrix.org\>** ya all bounty funds were directed to this CCS     
    
> **\<s​pirobel:kernal.eu\>** 👍️     
    
> **\<ofrnxmr\>** the bounty funds are TBD still, i think     
    
> **\<j​effro256:monero.social\>** Curious: have any business directly relying on this plugin pledged to donate any amount of XMR to this CCS?     
    
> **\<plowsof\>** transferal of the bounty amounts could be rough to time      
    
> **\<ofrnxmr\>** the bounties were closed (so nobody tries to claim them), but probably still need to ensure that the funds are properly appropriated as to not set precedent of rugging donors by change the goals     
    
> **\<pigeons\>** plowsof: out now, will check later, what are the symptoms?     
    
> **\<ofrnxmr\>** Pigeons, just started to be very slow     
    
> **\<plowsof\>** apparently "slow" but functional*     
    
> **\<plowsof\>** usual stuff     
    
> **\<s​yntheticbird:monero.social\>** got disconnected briefly     
    
> **\<ofrnxmr\>** Seems to be back speedy now     
    
> **\<s​yntheticbird:monero.social\>** i couldn't do my joke     
    
> **\<d​everickapollo:matrix.org\>** I'll be campaigning for funding once we get to that stage.     
    
> **\<j​effro256:monero.social\>** I know I should have brought this up 3 months ago, so don't view this as a blocker, but would be nice to see some corporate support from interested parties before merging since this directly benefits for-profit companies (Coin Cards, Cake Pay, et al) while going through a crowdfunding avenue.     
    
> **\<j​effro256:monero.social\>** Tbc, it's a great initiative and definitely needs to get done.     
    
> **\<ofrnxmr\>** coincards commented on the proposal     
    
> **\<d​everickapollo:matrix.org\>** Coincards has voiced intentions and I've been in contact with Vik. No concerns there. There are several more we should be communicating with.     
    
> **\<ofrnxmr\>** Some people are complaining about btcpay breaking when they update to 2.1. I havent tried a direct upgrade, but i assume this needs to be fixed     
    
> **\<plowsof\>** alright thanks for feedback. will try and get confirmation on whats happening with _all_ the bounties funds. payouts are slow so might not be possible to donate them while the proposal is in funding.     
    
> **\<plowsof\>** seth made a series of tweets for the v2.1 fix for people using the docker method. an env variable and restart iirc      
    
> **\<plowsof\>** thanks for feedback      
    
> **\<ofrnxmr\>** Yea, but needs to point to the new repo(?)     
    
> **\<j​effro256:monero.social\>** Thanks!     
    
> **\<plowsof\>**   b. [Monero Browser Wallet](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/555)         
    
> **\<s​yntheticbird:monero.social\>** where r4v3r23 ?     
    
> **\<s​yntheticbird:monero.social\>** where is the popcorn     
    
> **\<plowsof\>** spirobel      
    
> **\<ofrnxmr\>** Just want to confirm that once this ccs is complete (or once m2 is complete), we will have a fully functional browser wallet?     
    
> **\<s​pirobel:kernal.eu\>** yes     
    
> **\<plowsof\>** https://bounties.monero.social/posts/11/1-216m-authentication-token-proxy , this seems completed pending review, just wanted to share the "http 402 payment required" thingy - have you already accomplished pay walled content via monero payment in browser? if yes can you fit it to this standard please? not sure if this is related to your current     
    
> **\<plowsof\>** proposal or future work     
    
> **\<s​pirobel:kernal.eu\>** this is similar to the POC I built 2 years ago.     
    
> **\<ofrnxmr\>** Meaning send, receive, subaddreses, seed backup(?), all that good stuff that we would expect from a wallet? (coin control?)     
    
> **\<s​pirobel:kernal.eu\>** I also published the POC as open source recently     
    
> **\<s​pirobel:kernal.eu\>** yes     
    
> **\<plowsof\>** indeed, l402 . net is that POC' but fitting to the standard      
    
> **\<plowsof\>** for example if gingeropolous wanted to enable his api for wordpress shops     
    
> **\<clipped message\>** I think the milestone conditions could be a clarified. "Monero Browser Wallet" as a milestone without further qualification is not clear what is actually being delivered and will inevitably result in drama down the road when people disagree on what a "monero browser wallet" is. What browsers are targeted? What are the actual features outline for this specific payout? What kind of <clipped message>     
    
> **\<j​effro256:monero.social\>** UI are you going for?     
    
> **\<plowsof\>** he could add a proxy infront of the back end api      
    
> **\<plowsof\>** then the grifters can pay , but slightly offtopic      
    
> **\<ofrnxmr\>** jeffro, its (aiui) a browser extension like metamask     
    
> **\<plowsof\>** web wallet vs browser wallet big difference     
    
> **\<ofrnxmr\>** Not sure if the same ux like metamask / brave wallet     
    
> **\<plowsof\>** one advantage of this wallet , it behaves like moneor-wallet-cli running on your machine. no need to find a node with CORS enabled      
    
> **\<j​effro256:monero.social\>** Yes, I understand the general concept of a browser wallet, but the proposal needs way more details attached to specific milestones so the community knows what it's funding, and what it will receive at specific milestones     
    
> **\<s​pirobel:kernal.eu\>** I will rewrite the POC as an MV2 extension to get it published on the chrome store. the ui will contain everything you expect from a browser wallet like meta mask.     
    
> **\<j​effro256:monero.social\>** Because I want to avoid drama again where the proposer and the CCS participants misunderstand each other on which point the funds are released     
    
> **\<plowsof\>** the 3 deliverables under What jeffro256 https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/555#what should be clarified?     
    
> **\<s​pirobel:kernal.eu\>** In my view it is clarified enough because I also published the PoC source code. It is clear from that what a browser wallet is from my understanding     
    
> **\<s​pirobel:kernal.eu\>** I can go ahead and do wireframes and spec everything out in detail, but that itself is a large chunk of work. And it will lead to inflexibility     
    
> **\<s​pirobel:kernal.eu\>** sometimes a design needs to  be adapted  and iterated on     
    
> **\<ofrnxmr\>** "What browsers are targeted? What are the actual features outline for this specific payout? What kind of UI are you going for?"<< probably clarify these in the proposal      
    
> **\<plowsof\>** yeah seems sane      
    
> **\<j​effro256:monero.social\>** The "Implementation" section https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/555#implementation is pretty decent at listing discrete tasks, perhaps this could be organized by milestone to delineate what is the "API" tasks vs what is the "browser wallet" tasks vs what is the "companion app" tasks?     
    
> **\<plowsof\>** Chrome store spirobel mentioned and tor browser      
    
> **\<ofrnxmr\>** Tor browser is firefox, so i assume chrome and firefox(?)     
    
> **\<s​pirobel:kernal.eu\>** it is but the markdown rendering messes it up.     
    
> **\<s​pirobel:kernal.eu\>** there are two browser extension stores: chrome and firefox. I will publish to both     
    
> **\<s​pirobel:kernal.eu\>** that is the second milestone.     
    
> **\<j​effro256:monero.social\>** Cool, could you put that it the proposal, please?     
    
> **\<s​pirobel:kernal.eu\>** yes     
    
> **\<plowsof\>** +1 thanks for feedback      
    
> **\<plowsof\>** i did not, and i will not invite Jackie to this meeting, i don't want to bring this proposal up      
    
> **\<plowsof\>** d. [OPENENET-MS01-MoneroSpace-Decentralized-Satellite-Network](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/577)         
    
> **\<ofrnxmr\>** Merge     
    
> **\<plowsof\>** Lol     
    
> **\<ofrnxmr\>** Once funding fails, we can use the funds raised to blackhole it into the generalfund /s     
    
> **\<ofrnxmr\>** Im jk. NACK     
    
> **\<plowsof\>** the funding amout was reduced, so its not even good for that anymore      
    
> **\<j​effro256:monero.social\>** I see we moved down from 30,000 XMR to 550 XMR     
    
> **\<plowsof\>** another 550 to go     
    
> **\<ofrnxmr\>** Oh wtf. What a scam. If its not 30kxmr then its not worth discussing     
    
> **\<plowsof\>** Jackie should claim this bounty after appearing on monerotalk to promote the proposal https://bounties.monero.social/posts/186/0-420m-help-promote-monerospace yes?     
    
> **\<ofrnxmr\>** no     
    
> **\<s​yntheticbird:monero.social\>** we will crush the dream of a 12y kid and we will be happy     
    
> **\<plowsof\>** but the donors will be rugged     
    
> **\<ofrnxmr\>** they deserve it in this case      
    
> **\<ofrnxmr\>** Lol 😬. Need that approved tag     
    
> **\<plowsof\>** closing monerospace and banning Jackies account . thoughts?     
    
> **\<ofrnxmr\>** Maybe send it to doug     
    
> **\<s​yntheticbird:monero.social\>** plowsof dont ban jackies     
    
> **\<plowsof\>** right, good idea, yes     
    
> **\<s​pirobel:kernal.eu\>** i added the sentence "The extension will be published to the Chrome Web Store and the Firefox extension store." to the second milestone.     
    
> **\<j​effro256:monero.social\>** Why ban Jackie     
    
> **\<s​yntheticbird:monero.social\>** CHICKEN JACKIE     
    
> **\<ofrnxmr\>** Yes close, and warn first     
    
> **\<plowsof\>** he spams my notifications, emails (no bounties) and hides payout requests and actual updates     
    
> **\<plowsof\>** s/no/now     
    
> **\<plowsof\>** and uses alts on bounties site* lol ok just close it     
    
> **\<plowsof\>** closing monerospace      
    
> **\<s​yntheticbird:monero.social\>** plowsof give me your account credentials and i'll mute him for you promise promise promise i swear i wont would never ever do anything else with it     
    
> **\<plowsof\>** "chicken jackie"      
    
> **\<plowsof\>** 👍     
    
> **\<n1oc\>** [CCS Proposals] plowsoff closed merge request #577: OPENENET-MS01-MoneroSpace-Decentralized-Satellite-Network https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/577     
    
> **\<plowsof\>**   c. [Haveno iOS and Android App](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/570)         
    
> **\<NorrinRadd\>** quick update, milestones 1 and 2 are done, 3 and 4 are almost done.      
    
> **\<s​yntheticbird:monero.social\>** cooking fr 🔥🔥     
    
> **\<plowsof\>** so there are currently three? people working on this separately (at least one of which is accused of being AI) - are there any advantages of your project vs theirs? or would you need time to compare/contrast      
    
> **\<NorrinRadd\>** well one advantage is that the sdk is cross platform, instead of Windows dependent.     
    
> **\<NorrinRadd\>** Due to that, it is likely that others will be able to maintain & contribute easier.      
    
> **\<NorrinRadd\>** + review     
    
> **\<plowsof\>** LootSpam (i think this is kewbit with a better LLM) https://bounties.monero.social/posts/126/37-175m-building-an-open-source-android-app-for-haveno-dex      
    
> **\<plowsof\>** and atsamd21 https://github.com/atsamd21/Haveno-app     
    
> **\<ofrnxmr\>** I think it would be easier to consider this proposal if it is ineligible to claim old-haveno funds (even if funding fails)     
    
> **\<plowsof\>** and we would need people responsible to review the work     
    
> **\<ofrnxmr\>** Atsamd21's doesnt require a desktop      
    
> **\<plowsof\>** not people who give bad endorsements and have nothing to lose     
    
> **\<ofrnxmr\>** I think norrinradd's does?     
    
> **\<NorrinRadd\>** ofrnxmr two comments: to your first statement first, what's the reasoning behind it being ineligible?      
    
> **\<ofrnxmr\>** After wasting the funds repeatedly, they should only be eligible for retroactively completed works.      
    
> **\<ofrnxmr\>** Not paying for milestones that may or may not lead to completing the project     
    
> **\<ofrnxmr\>** A major point of ccs is that you raise your own funds      
    
> **\<ofrnxmr\>** being unable to raise the funds means that there isnt anyone who wants to fund the work     
    
> **\<NorrinRadd\>** secondly, what is the feasibility of keeping an app running 24/7? Haveno is a DEX, and as such, means that each participant runs a web service. Is that something that people are going to be doing in mass on phones? In my experience, my offers usually take 4 days to be taken on Haveno (and I always intentionally price to be the cheapest option).  Will a good number of people be able to     
    
> **\<NorrinRadd\>** keep an app running for 4 days continually on a phone?     
    
> **\<ofrnxmr\>** Those funds arent for a haveno app, but for a new desktop UI     
    
> **\<plowsof\>** im not sure of the similarity / resources but monero wallets are open 24/7 while background scanning      
    
> **\<NorrinRadd\>** "they should only be eligible for retroactively completed works" -- if i understand that correctly, I agree.  As statement, this milestones are already in progress and nearly completion.     
    
> **\<plowsof\>** have you been tracking your hours?     
    
> **\<s​pirobel:kernal.eu\>** is the goal that people run the haveno node on their desktop / laptop and then connect to that from their phone?     
    
> **\<NorrinRadd\>** "but for a new desktop UI" -- I was going to mention that. This works on desktop as well.     
    
> **\<s​pirobel:kernal.eu\>** how does that enable "trading on the go" ?     
    
> **\<ofrnxmr\>** well if the ccs is completed before funded, we can come back to discuss using haveno ui funds to top off the ccs funding required     
    
> **\<j​effro256:monero.social\>** spirobel: run Haveno daemon on computer, copy Tor hidden service link to phone, access daemon from phone     
    
> **\<NorrinRadd\>** plowsof i'll have to check how that background scanning works. I doubt that. I believe the app wakes to scan, and then closes.      
    
> **\<ofrnxmr\>** monfluo runs 24/7     
    
> **\<ofrnxmr\>** Using a foreground service. It doesnt run periodically     
    
> **\<NorrinRadd\>** spirobel the app works from anywhere     
    
> **\<ofrnxmr\>** Cake runs periodically. Anonero also runs 24/7     
    
> **\<s​pirobel:kernal.eu\>** seems like a mission for  a webfrontend. + additional functionality in the daemon     
    
> **\<s​pirobel:kernal.eu\>** the app seems like another extra step     
    
> **\<ofrnxmr\>** Yea. Its seems like pretty much just an interface to the api      
    
> **\<ofrnxmr\>** wrapped in an "app" instead of a webapp     
    
> **\<ofrnxmr\>** 🤷‍♂️     
    
> **\<ofrnxmr\>** Anyway, i think it needs more upvotes to consider merging     
    
> **\<j​effro256:monero.social\>** Yeah we could squash all these frontend development efforts (except for Native android/iOS Haveno daemon) into one by just making it a web frontend     
    
> **\<s​yntheticbird:monero.social\>** m-relay <s​yntheticbird:monero.social> is saying in the corner of the room: "Please dont make it Electron. Please dont make it Electron. Please dont make it Electron..."     
    
> **\<j​effro256:monero.social\>** And I don't even really think that a native haveno daemon on a mobile device is something that should be pursued anyways     
    
> **\<NorrinRadd\>** so strangely enough, this compiles to web as well      
    
> **\<NorrinRadd\>** I personally wouldn't use it that way, but it does      
    
> **\<ofrnxmr\>** Jeffro256, review please https://github.com/monero-project/monero/pull/9914 /s     
    
> **\<plowsof\>** nack 9914 without squashing     
    
> **\<plowsof\>** alright we have went over the hour, thanks all for attending and providing feedback      
    
> **\<NorrinRadd\>** jeffro256 i doubt the usefulness also, but as I've discussed with someone else, it could be the next step afterward      
    
> **\<s​pirobel:kernal.eu\>** thanks     
    
> **\<j​effro256:monero.social\>** ofnrxmr: https://github.com/FuneroBlockchain/Funero/blob/1712e2a19e5bf1517f2be8392e5d0280d41ec8bc/src/cryptonote_config.h#L58 revolutionary idea     
    
> **\<ofrnxmr\>** Cheers     
    
> **\<s​pirobel:kernal.eu\>** this was a good session     
    
> **\<ofrnxmr\>** Lololol HF every 250k blocks lololololol     
    
> **\<ofrnxmr\>** "Genesis Block Reward: 50,000 FNRO" "Initial block reward: 7 FNRO"     
    
> **\<ofrnxmr\>** "P2P Port: 38080     
    
> **\<ofrnxmr\>** RPC Port: 38081     
    
> **\<ofrnxmr\>** " jerkoff couldnt even find his own port range     
    
> **\<s​yntheticbird:monero.social\>** i read jeffrok couldn't even find his own port range     
    
> **\<j​effro256:monero.social\>** I don't like this new nickname     
    
> **\<j​effro256:monero.social\>** Btw thanks everyone ! Good meeting     
    
> **\<s​yntheticbird:monero.social\>** reasonably so 👍️     
    
> **\<msvb-lab\>** Good meeting, by bye.     
    
> **\<NorrinRadd\>** "Anyway, i think it needs more upvotes to consider merging" -- how many are required?      
    
> **\<s​yntheticbird:monero.social\>** 90     
    
> **\<s​yntheticbird:monero.social\>** +0.5XM     

Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: plowsof | 2025-04-25T09:31:39+00:00
- Closed at: 2025-05-21T07:14:42+00:00
