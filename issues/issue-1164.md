---
title: 'Monero Community Workgroup Meeting: March 1st 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1164
author: plowsof
assignees: []
labels: []
created_at: '2025-02-27T14:17:54+00:00'
updated_at: '2025-03-26T23:57:33+00:00'
type: issue
status: closed
closed_at: '2025-03-26T23:57:33+00:00'
---

# Original Description
Location: [Libera.chat, #monero-community](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-community:monero.social?via=matrix.org&via=monero.social)

[Instructions for joining the monero.social Matrix server.](https://www.getmonero.org/resources/user-guides/join-monero-matrix.html)

Time
18:00 UTC [Check your timezone](https://www.timeanddate.com/worldclock/converter.html)

Moderator: plowsof

Please reach out in advance of the meeting if you would like to propose an agenda item.

Proposed Meeting Items:

1. Introduction
2. Greetings
3. Community highlights    
News: [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/) - [Monero Moon](https://www.themoneromoon.com/)    
    - [OSPEAD](https://github.com/Rucknium/OSPEAD) "since the August 2022 hard fork [...] an effective ring size of 4.2" - Rucknium [related reddit thread](https://www.reddit.com/r/Monero/comments/1ivnef8/rucknium_has_published_ospead_findings_showing/) xenu
    - cuprated fast sync entire blockchain in under 2 hours (fast sync is the default sync method of monerod) [related tweet](https://nitter.net/KevinoTech/status/1895772875086520336) rottenwheel
4. [CCS updates](https://ccs.getmonero.org/)    
  a. [Funding Proposal for Unstoppable Wallet: Enabling Native Monero Integration on iOS & Android](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/532)    
  b. [Btcpayserver plugin](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/538)    
  c. [Initial commit of MoneroKon 2025 CCS proposal](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/554)    
  d. [Monero Browser Wallet](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/555)    
  e. [Walletverse monero integration](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/556)    
  f. [acx Monfluo maintenance and further development (3 months)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/557)    
  g. [Revuo Monero Maintenance (2025 Q2)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/559)    
  h. [plowsof CCS Coordinator](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/560)   
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

[Previous meeting including logs](https://github.com/monero-project/meta/issues/)    

Meeting logs will be posted here afterwards.    


# Discussion History
## Rucknium | 2025-02-28T21:14:48+00:00
Please add to the agenda [MAGIC Proposal: Metronero Development](https://github.com/MAGICGrants/Monero-Fund/issues/41)

@sausagenoods

## plowsof | 2025-03-26T23:56:15+00:00
> __< b​usyboredom:tchncs.de >__ I'm moving this weekend so won't make it to the meeting, but my update for AcceptXMR is:     

> __< b​usyboredom:tchncs.de >__ Had a fun side quest packaging the WordPress plugin for nixos-based WordPress installations. Slow progress on the currency conversion work, should make faster progress next two weeks since I'll be done moving.     

> __< plowsof >__ Thanks for the update busyboredom 💪     

> __< o​frnxmr:xmr.mx >__ i prefer the old time (1600utc)     

> __< o​frnxmr:xmr.mx >__ The later it gets, the more it lands in the middle of stuff     

> __< plowsof >__ Meeting time https://github.com/monero-project/meta/issues/1164      

> __< plowsof >__ first time at 18:00 , maybe 20:00? or back to 16:00 we can play it by ear      

> __< s​pirobel:kernal.eu >__ 16 pls 20 would be 4am for me     

> __< plowsof >__ right... ok lets get through the major  recent events      

> __< plowsof >__  [OSPEAD](https://github.com/Rucknium/OSPEAD) "since the August 2022 hard fork [...] an effective ring size of 4.2" - Rucknium [related reddit thread](https://www.reddit.com/r/Monero/comments/1ivnef8/rucknium_has_published_ospead_findings_showing/) xenu      

> __< m​ichael:monero.social >__ Hello.     

> __< plowsof >__ hello     

> __< plowsof >__ im wondering if any chainalysis have been using this already, or, if they can show the effects on existing research , e.g. moonstoneresearch / sgp_ report on the CCS hack https://moonstoneresearch.com/2023/11/03/Postmortem-of-Monero-CCS-Hack.html      

> __< plowsof >__ cuprated fast sync entire blockchain in under 2 hours (fast sync is the default sync method of monerod*) [related tweet](https://nitter.net/KevinoTech/status/1895772875086520336) rottenwheel     

> __< plowsof >__ 2.5x faster according to #cuprate syntheticbird      

> __< plowsof >__ https://ccs.getmonero.org/funding-required/ 🙏      

> __< ofrnxmr >__ Looks like cuprate optimized randomx syncing     

> __< ofrnxmr >__ Previously it was seconds per batch, now it looks to be about as fast as pre-randomx      

> __< plowsof >__ ofrnxmr yo umentioned 're writing monerod in c++ would yield improvements also' which i found funny      

> __< ofrnxmr >__ 😆😆 yeah. Starting from scratch w/o all of the inherited deficiencies       

> __< plowsof >__ j-berman has developed / given presentation on faster syncing for clients IIRC wonder if cuprate could adopt this in the future (i assume this would be for a cli rather than the daemon, i could be wrong)     

> __< s​pirobel:kernal.eu >__ link?     

> __< ofrnxmr >__ -dev needs to not-ignore what cuprate is doing. Clearly the 2x*2 speedup should be possible to be duplicated on monerod     

> __< plowsof >__ for berman? ill have to find it / confirm - i vividly remember a presentation perhaps at a cake sponsored event where the async style sync was mentioned      

> __< ofrnxmr >__ Cuprate was one-upon-a-time slower tobsync the first 100k blocks than monerod, and ~same speed to sync the full chain. I dont think the optimizations are voodoo     

> __< ofrnxmr >__ One of them was simply the sync-mode      

> __< ofrnxmr >__ cc hinto boog900     

> __< plowsof >__ can move on to ccs ideas in the mean time      

> __< plowsof >__ meantime*      

> __< o​frnxmr:xmr.mx >__ Yea     

> __< plowsof >__ just to mention tat vtnerd was merged to funding , but feedback is welcome (what to focus his time on etc) https://ccs.getmonero.org/proposals/vtnerd-2025-q1.html      

> __< plowsof >__   a. [Funding Proposal for Unstoppable Wallet: Enabling Native Monero Integration on iOS & Android](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/532)         

> __< plowsof >__ j0j0xmr had linked  a commit, removing something from their paid tier , however the concerns in the proposal comments remain unaddressed      

> __< ofrnxmr >__ Close / reopen if they ever feel like responding     

> __< n1oc >__ [CCS Proposals] plowsoff closed merge request #532: Funding Proposal for Unstoppable Wallet: Enabling Native Monero Integration on iOS & Android https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/532     

> __< plowsof >__ i agree, oops, moving on     

> __< plowsof >__   b. [Btcpayserver plugin](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/538)         

> __< plowsof >__ a new comment from Deverick https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/538#note_28917     

> __< s​pirobel:kernal.eu >__ and this one https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/538#note_28920     

> __< plowsof >__ also wondered what the emoji meant lol     

> __< ofrnxmr >__ I dont understand deverick, napoly and skunkwheel thumb downing my comment that btcpayserver 2.1 will launch with monero support. The ccs proposal doesnt asknowledge that and needs to be redefined imo     

> __< plowsof >__ sgp_ had intended for the btcpayserver plugin to be on the MAGIC repo but : https://libera.monerologs.net/monero-community/20250227#c502452     

> __< r​ucknium:monero.social >__ A little relevant: Siren and Stnby  have submitted a funding proposal for further Metronero development to the MAGIC Monero Fund: https://github.com/MAGICGrants/Monero-Fund/issues/41     

> __< r​ucknium:monero.social >__ Metronero is a "BTCPayServer alternative using MoneroPay."     

> __< plowsof >__ thanks for sharing Rucknium , relevant      

> __< r​ucknium:monero.social >__ I'm not longer on the committee, so I don't know if it will get approved or not. But it probably will     

> __< s​pirobel:kernal.eu >__ I want to mention, that the first milestone of my proposal is also relevant     

> __< s​pirobel:kernal.eu >__ similar feature set, but different goals / target audiences     

> __< ofrnxmr >__ "During our work on open bounties and 2 for the Monero community, we identified the need to realign our efforts on the plugin migration to ensure continued support for Monero within BTCPay Server."     

> __< plowsof >__ i do not agree that "Multiwallet support: This is a critical feature that aligns monero with the rest of the BTCPay ecosystem." - FCMP++ .. quantum resistance.. would be critical.  don;t tell me that "merchants like Cake Pay, Concords, Shopinbit, and many more." will cease to exist if multi wallet support isn't added      

> __< plowsof >__ bitcart.io has multi wallet support / easier to setup imo than btcpayserver , where are the third party hosters pushing monero? (for free)? marketing issue?      

> __< plowsof >__ Metronero adds a (at least from what i remember) method of third party hosting with a fee model      

> __< plowsof >__ will the repo be on monero-project repo? Deverick should be drumming up support for his own proposal as per rules and pushing this along      

> __< plowsof >__ and napoly      

> __< ofrnxmr >__ theyre instead just playing the drum of "the world will end if we dont use lws with remote nodes oxymoron"      

> __< s​gp_:monero.social >__ I'm talking with deverick about options to maintain this going forward. I think this CCS can be tabled until further notice, imo     

> __< plowsof >__ but 8 people thumbed it up and 1 down this is typical CCS conspiracy      

> __< s​gp_:monero.social >__ LWS support will mostly benefit btcpayserver hosting companies, so I want to work with deverick/napoly to reach out to these companies with a proposal and have them cover the majority/all of the costs. At least as Plan A     

> __< s​pirobel:kernal.eu >__ plan B is normal CCS?     

> __< plowsof >__ sgp_ thank you for drumming up support for their proposal      

> __< s​gp_:monero.social >__ No, that's probably plan F     

> __< s​gp_:monero.social >__ Again, just my opinion     

> __< plowsof >__ i agree with it      

> __< s​pirobel:kernal.eu >__ we all agree nice     

> __< plowsof >__ +1 for Metronero Siren Stnby      

> __< r​ucknium:monero.social >__ Did they say how exactly they intend to enable multi-wallet support?     

> __< s​pirobel:kernal.eu >__ also +1     

> __< s​pirobel:kernal.eu >__ by using lws     

> __< s​gp_:monero.social >__ Metronero proposal for MAGIC Grants uses one wallet seed only for their multiple stores feature     

> __< s​gp_:monero.social >__ It's shared     

> __< plowsof >__ benefit being a fee model for the hosting company , or, open source self host right?     

> __< plowsof >__ bitcart.ai / mrnaif uses some Rust magic for third party hosting of multiple monero wallets      

> __< ofrnxmr >__ +1 for metronero     

> __< plowsof >__ we can move on i thinks? thanks for the feedback     

> __< ofrnxmr >__ Yes, but also on metronero, it uses moneropay      

> __< ofrnxmr >__ And includes further development on moneropay     

> __< r​ucknium:monero.social >__ It makes sense to me that this proposal should revise its scope and cost once NicolasDorier finished the 2.1 plugin. So that the proposers know what architecture they would be building on top of.     

> __< plowsof >__ will make sure Deverick napoly see this meeting log , thank you      

> __< plowsof >__   c. [Initial commit of MoneroKon 2025 CCS proposal](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/554)         

> __< ofrnxmr >__ they made a profit last yr, i dont understand why they need ccs this year?     

> __< ofrnxmr >__ + a 10% buffer even tho theyre going to market sell it into a stablecoin     

> __< plowsof >__ there was an issue with the front end UI of the Safe wallet, but hbs and fancisscom clarified "funds are safe, the only issue is that Safe hasn't restored the UI to interact with the multi sig safe on polygon yet, so any interaction would require direct smart contract calls, doable but not ideal"      

> __< s​gp_:monero.social >__ I read it as basically them needing a loan to cover the initial costs     

> __< ofrnxmr >__ Are they repaying it?     

> __< s​gp_:monero.social >__ Not in this case, though arguably them continuing to invest in the community event is reasonable (imo)     

> __< ofrnxmr >__ I read it like that too, but i dont see anything about where the surplus goes      

> __< plowsof >__ the smiles on attendees faces shall be payment in full      

> __< s​tnby:kernal.eu >__ Thanks for bringing our toy up     

> __< h​bs:matrix.org >__ The surplus, if any, will be used to finance future editions of MoneroKon     

> __< plowsof >__ do note that the general fund has a history of contributing to monerokon proposals      

> __< s​gp_:monero.social >__ Ideally you should aim to have a surplus to avoid this next year. I'm not against this proposal if the goal is still sustainability     

> __< nioc >__ They are not selling all to stable coin and the 10% volatility has already beeb     

> __< ofrnxmr >__ hbs, how about using surplus up to the amount of the ccs, used to improve this years experience      

> __< nioc >__ Already been hit     

> __< ofrnxmr >__ Niocat, xmr is 220     

> __< nioc >__ Was 235 wen proposal was made     

> __< ofrnxmr >__ It was priced at 223     

> __< h​bs:matrix.org >__ it was decided to go with a CCS because we have not filled all sponsors slots, so CCS is seen as a way to ensure the event can take place     

> __< ofrnxmr >__ nvm 223 eur     

> __< h​bs:matrix.org >__ as specified in the proposal, we will seek a new venue for future editions to reduce the total budget, so if things go as planned we should not require a CCS in the future     

> __< ofrnxmr >__ i think the 223 includes 10% buffer, @hbs?     

> __< h​bs:matrix.org >__ the exchange rate used was the EMA50, we divided 20k by that rate then added the 10% to the number of XMR     

> __< h​bs:matrix.org >__ leading to 99     

> __< ofrnxmr >__ 223 does include the 10%     

> __< ofrnxmr >__ So ~200eur + 10%      

> __< ofrnxmr >__ 223*99=22k     

> __< plowsof >__ maths are confusing, we can confirm the amounts shortly sirs      

> __< plowsof >__ thanks for the feedback so far, i think we can move on      

> __< plowsof >__   d. [Monero Browser Wallet](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/555)         

> __< plowsof >__ spirobel there has been some feedback that mentioned the amount , but you clarified that it is a bargain      

> __< ofrnxmr >__ I'm doing math backwards, sorry plow. Real rate is 202eur/xmr (209usd/xmr)     

> __< s​pirobel:kernal.eu >__ lets go through the deliverables there was also some critique that mentioned it should be split up, but I disagree with that     

> __< s​pirobel:kernal.eu >__ it should not be split up     

> __< plowsof >__ ok thanks for confirming, this is your proposal, as is - no changes required      

> __< r​ucknium:monero.social >__ > Currently Monero shoppers have to copy and paste addresses from the tor browser into their wallets. This can be made more convenient and secure by a browser wallet.     

> __< s​gp_:monero.social >__ No qr codes?     

> __< r​ucknium:monero.social >__ But the Tor Project discourages installing extensions in the Tor Browser https://tb-manual.torproject.org/plugins/     

> __< r​ucknium:monero.social >__ > However, the only add-ons that have been tested for use with Tor Browser are those included by default. Installing any other browser add-ons may break functionality in Tor Browser or cause more serious problems that affect your privacy and security. It is strongly discouraged to install additional add-ons, and the Tor Project will not offer support for these configurations.     

> __< ofrnxmr >__ Or uris?     

> __< plowsof >__ open in wallet button href="monero:"     

> __< s​pirobel:kernal.eu >__ yes for good reason     

> __< s​pirobel:kernal.eu >__ you mean deeplinks right? It means that often when you click an x.link on a mobile browser suddenly the x app opens     

> __< s​gp_:monero.social >__ Danger: You should never install any additional extensions on Tor Browser or edit about:config settings, including the ones we suggest for Firefox. Browser extensions and non-standard settings make you stand out from others on the Tor network, thus making your browser easier to fingerprint.     

> __< s​gp_:monero.social >__ https://www.privacyguides.org/en/tor/     

> __< s​pirobel:kernal.eu >__ yeah very good point. Most random extensions shouldnt be installed.     

> __< s​pirobel:kernal.eu >__ but this is an exception     

> __< s​pirobel:kernal.eu >__ anyway lets go through the deliverables and address this first     

> __< s​gp_:monero.social >__ I just wanted to note the goal of an extension with Tor browser is fundamentally incompatible. Extensions can be used in other cases     

> __< s​pirobel:kernal.eu >__ blanket statement     

> __< plowsof >__ as we're over the hour we have to touch on the other proposals, thank you for the feedback so far and apologies      

> __< s​pirobel:kernal.eu >__ yeah its 3am here     

> __< plowsof >__ thank you for attending      

> __< plowsof >__   e. [Walletverse monero integration](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/556)         

> __< plowsof >__ has recently been rejected by MAGIC, so we can skip this one for now as we're over time but open for feedback none the less     

> __< plowsof >__   f. [acx Monfluo maintenance and further development (3 months)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/557)         

> __< plowsof >__ low asking amount of 14 xmr to add features to a MySu fork      

> __< plowsof >__   g. [Revuo Monero Maintenance (2025 Q2)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/559)         

> __< plowsof >__   h. [plowsof CCS Coordinator](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/560)        

> __< ofrnxmr >__ +1 acx, revuo and plowsof dont start til april so no big rush. But +1 plowsof      

> __< s​iren:kernal.eu >__ I see value in a browser wallet from an UI/UX perspective. Especially if it improves the multisig experience.     

> __< s​pirobel:kernal.eu >__ https://matrix.monero.social/_matrix/media/v1/download/kernal.eu/ywzqHFIZQgFMupWQtVhGWuQo     

> __< ofrnxmr >__ Multisig is changing wirh fcmp     

> __< plowsof >__ thank you for the feedback and updoots on mine and other proposals :)      

> __< s​pirobel:kernal.eu >__ tor browser has no script pre installed. It is not as black and white     

> __< plowsof >__ v1do has been up for funding for some time      

> __< ofrnxmr >__ Yeah, i'm not against merging em     

> __< ofrnxmr >__ Payouts for those dont come til end of April or-so, but no harm in getting a head start     

> __< ofrnxmr >__ Well, luigi has been taking 4 weeks to do payouts, so payouts will come end of may :D     

> __< ofrnxmr >__ (i'm voting merge acx and plow)     

> __< s​pirobel:kernal.eu >__ alright good night everyone. If you have any questions about the browser wallet, library, etc abstract or concrete. pls ask 🙏     

> __< ofrnxmr >__ Spirobel, you recently closed out (successfully) the previous ccs, right?     

> __< plowsof >__ good night thanks for joining . and all who have attended. yes spirobels prev porposal has been paid out and completed      

> __< s​pirobel:kernal.eu >__ yes. It was the preliminary work for all of this     

> __< v1docq47[x] >__ as an option, im considering a reduction in the amount     

> __< plowsof >__ kewbits proposal has been terminated i am delighted to share      

> __< v1docq47[x] >__ funding is going very hard...     

> __< plowsof >__ v1docq47 there are also approx 1~xmr available from your previous proposals (overfunding) which is also another option to help      

> __< ofrnxmr >__ V1d     

> __< v1docq47[x] >__ lets see for another month, then ill think about it      

> __< ofrnxmr >__ You have some overpayment from previous ccs'     

> __< ofrnxmr >__ So we can probably vote to apply the funds if the fundraising is unsuccessful      

> __< ofrnxmr >__ Plowsof. 1xmr or 10?     

> __< plowsof >__ it would be a shame to see this happen as v1do has been completing ccs proposals for years      

> __< plowsof >__ closer to 1      

> __< v1docq47[x] >__ i wouldnt want to have to resort to that      

> __< plowsof >__ ofrnxmr closer to 10***** yes https://github.com/plowsof/scrape_ccs_fr/tree/ccs1     

> __< plowsof >__ apologies. 10 is substantial      

> __< v1docq47[x] >__ theres still 3 months of work ahead, so theres no rush :)     

> __< plowsof >__ thanks for joining us and good luck with funding     

> __< plowsof >__ i think we can end the meeting here, thanks all for attending      

> __< v1docq47[x] >__ tnx     

> __< ofrnxmr >__ you can still request payouts before funding is completed, if needed (according to the rules)     

> __< plowsof >__ currently this is not preferred      

> __< ofrnxmr >__ Rule 6 "Your work on the project can begin before the proposal is fully funded, and milestones may (at times) be paid out before the proposal is fully funded."     

> __< v1docq47[x] >__ luigi said he wanted to wait until the proposal was fully funded     

> __< plowsof >__ we'll have to yell at him, getting overfunded amounts approved is a positive step      

> __< ofrnxmr >__ ofc you cant request funds that havent been donated, but i dont think it hurts anything to request funds that have been     

> __< ofrnxmr >__ Yeah. We can give it another 4 weeks if v1d is ok with that     

> __< v1docq47[x] >__ i wrote to him a month ago about the payment for dec+jan     

> __< ofrnxmr >__ did you post request on the proposal?     

> __< ofrnxmr >__ A month ago a lot of ppl requested payouts and it took him a month to pay them. So dont worry, he's just on a boat right now     

> __< v1docq47[x] >__ yup, i wrote him and plowsof after the two month works report     

> __< b​oog900:monero.social >__ yeah I think that was a wallet thing     

> __< plowsof >__ I will make my false memory true soon, thanks boog900     


Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: plowsof | 2025-02-27T14:17:54+00:00
- Closed at: 2025-03-26T23:57:33+00:00
