---
title: 'Monero Community Workgroup Meeting: Dec 6th 16:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1305
author: plowsof
assignees: []
labels: []
created_at: '2025-12-02T13:28:07+00:00'
updated_at: '2025-12-08T22:15:03+00:00'
type: issue
status: closed
closed_at: '2025-12-08T22:15:03+00:00'
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
    - https://libera.monerologs.net/ is alive again, thank you anon
    - https://github.com/gupax-io/gupax/issues/137
    - tevadors take on Blockchain Scaling https://github.com/monero-project/research-lab/issues/155 
    - Blocksize mis(information) wars
    - [MAGIC fundraiser for fuzzing round 2](https://donate.magicgrants.org/monero/projects/fuzzing-monero-2)
    - Rucknium adds improvements to https://github.com/Rucknium/xmrspammer , in use on stressnet
    - Monero Blocks https://blocks.p2pool.observer/pools DataHoarder
    - https://github.com/xmrig/xmrig/pull/3736 sech1
    - Eigen Wallet upcoming release https://eigenwallet.org/changelog.html
News: [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/) - [This week in Monero](https://cyphergoat.com/this-week-in-monero)
4. [CCS updates](https://ccs.getmonero.org/)    
  a. [39C3 Support](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/622)    
  b. [emsczkp research Bulletproofs*](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/626)    
  c. [j-berman full-time part 12 (4 months)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/628)    
  d. [selsta part-time monero development (3 months) (19)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/629)    
  e. [vtnerd 2025 q4 (full-time) proposal](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/630)    
5. Workgroup reports    
  a. Dev workgroup
  b. Localization workgroup
  c. Outreach workgroup
  d. Events workgroup - [MoneroKon 2026](https://MoneroKon.org)
  e. Website workgroup https://github.com/redsh4de/monero-site
  f. Policy workgroup
  g. Research workgroup
  h. [FCMP++ Stressnet updates](https://github.com/seraphis-migration)
6. Open ideas time    
7. Confirm next meeting date/time    

[Previous meeting including logs](https://github.com/monero-project/meta/issues/1301)    

Meeting logs will be posted here afterwards.    

# Discussion History
## michaesc | 2025-12-06T15:08:04+00:00
Would you please @plowsof  add to today's agenda an entry for discussion about **Changelly** to decide or consider their new ideas for more Monero inclusion? If my entry request is granted the topic could be called:

- Changelly outreach

...but I'm not sure where it belongs, because it's not part of a workgroup or CCS. Maybe make it part of **Community highlights**? The reason I'm requesting this is from meetings I've had with them, to hear if anyone has information about whether outreach or inclusion would be good or bad.

## plowsof | 2025-12-06T15:35:09+00:00
Sure thing 👍 during Community Highlights seems sane, afaict changenow are present in several popular wallets and swap aggregation services

## plowsof | 2025-12-07T00:38:03+00:00
Logs 
    
    
    
    
    
    
    
    
    
    
> **\<plowsof\>** Meeting time https://github.com/monero-project/meta/issues/1305     
    
> **\<ofrnxmr\>** <ofrnxmr> GM. Be back in 5min     
    
> **\<plowsof\>** greetings, the Blocksize (mis)information wars appear to be in full effect 😬     
    
> **\<msvb-lab\>** Hello.     
    
> **\<hinto\>** <hinto> hello     
    
> **\<plowsof\>** thankfully https://libera.monerologs.net/ is alive again, thank you anon. #monero-research-lounge has alot of this being discussed recently      
    
> **\<plowsof\>** https://github.com/gupax-io/gupax/issues/137 hello hinto      
    
> **\<emsczkp:matrix.org\>** <emsczkp:matrix.org> Hello     
    
> **\<plowsof\>** is the transfer going well?     
    
> **\<0xfffc\>** <0xfffc> Hi everyone     
    
> **\<plowsof\>** i can confirm the signed pgp statement comes from hinto      
    
> **\<hbs:matrix.org\>** <hbs:matrix.org> hello     
    
> **\<plowsof\>** msvb-lab does ChangeNOW want to seek feedback on some outreach?     
    
> **\<hinto\>** <hinto> I've transferred Gupax to @lm:matrix.baermail.fr and they are currently in the process of porting Gupaxx to gupax-io/gupax, they should also have ownership of the gupax.io domain in a few days (takes a bit of time to transfer apparently)     
    
> **\<ofrnxmr\>** <ofrnxmr> plowsof: yeah, the comment on agenda was confusing     
    
> **\<msvb-lab\>** Yes, let me explain.     
    
> **\<hinto\>** <hinto> @datahoarder:monero.social: reminder that the "by hinto-janai" on p2pool.observer should be updated :)     
    
> **\<msvb-lab\>** First of all, I wrote the topic wrong because it's Changelly not ChangeNOW.     
    
> **\<msvb-lab\>** Sorry for making that very dumb mistake.     
    
> **\<ofrnxmr\>** <ofrnxmr> msvb-lab: Oh, nack     
    
> **\<msvb-lab\>** I've had some on line and in person meetings to respond to different Changelly people trying to serve Monero users more.     
    
> **\<plowsof\>** thank you for GUPAX hinto , nice to see it thriving      
    
> **\<ofrnxmr\>** <ofrnxmr> But lets play devils advocate. Whats the gist     
    
> **\<plowsof\>** changelly is , ,, , mission abort     
    
> **\<msvb-lab\>** The purpose of this meeting agenda item is to ask us all, do you have an opinion about Changelly and is it positive or negative?     
    
> **\<ofrnxmr\>** <ofrnxmr> Negative     
    
> **\<msvb-lab\>** Is there an easy way to understand why Changelly is not well received, and is the problem limited to past actions of several years ago?     
    
> **\<plowsof\>** changelly is listed as a scam wallet on the r/monero subreddit      
    
> **\<msvb-lab\>** I don't feel like searching the internet in five places to inform myself, and meetings with them imply to me that their wishes are normal ones. To serve Monero users more or better.     
    
> **\<plowsof\>** i think it stems from their shotgun-KYC , and constant stories of people claiming to go through the KYC steps and have funds not returned (anecdotal)      
    
> **\<msvb-lab\>** I don't have a well developed opinion on the matter, and I see some things that they did wrongly were far in the past.     
    
> **\<ofrnxmr\>** <ofrnxmr> msvb-lab: whats stopping them from serving monero users? We're not going to promote a service that has a history of stealing funds on bogus shotgun kyc     
    
> **\<plowsof\>** changelly do not appear on kycnot.me      
    
> **\<ofrnxmr\>** <ofrnxmr> Nor orangefren or trocador     
    
> **\<ofrnxmr\>** <ofrnxmr> Nobody wants to associate with them     
    
> **\<msvb-lab\>** Does Shapeshift (old) and Majesic (also old) appear in any of the places for groups abusing KYC? I mean, is it true that Changelly is more abusive than other groups during this and last (2024) year?     
    
> **\<ofrnxmr\>** <ofrnxmr> Majestic has probably never requested kyc     
    
> **\<ofrnxmr\>** <ofrnxmr> Some services like FixedFloat will request SoF etc when they receive dirty funds, and will return the funds or process the swap if the sender can confirm that they arent the thief     
    
> **\<msvb-lab\>** Majestic had problems with complaints by users when their transactions failed and were left without funds that should have been returned, but as with all services this was usually due to slow work that later was corrected. That's why I put them on the complaints list.     
    
> **\<ofrnxmr\>** <ofrnxmr> afaik, they cleared up any issues when they came to light, but yes majestic also had a spotty history with rates not matching etc     
    
> **\<ofrnxmr\>** <ofrnxmr> But majestic doesnt exist anymore, so is irrelevant     
    
> **\<msvb-lab\>** Is it true that Monero community places promote groups using KYC, but doing so responsibly? Or are the places that ban Changelly doing so because all KYC using sservices there get banned?     
    
> **\<ofrnxmr\>** <ofrnxmr> The former     
    
> **\<msvb-lab\>** Okay, I'm just trying to understand this now. Still no well developed opinion.     
    
> **\<msvb-lab\>** So if we understand that Changelly is using KYC in a responsible manner and has not abused KYC for several years, then it would mean that we the community want to help them serve Monero users. Is that right?     
    
> **\<ofrnxmr\>** <ofrnxmr> trocador and orangefren both list services that will perform aml checks on incoming funds and will request kyc if they fail the checks. But they also have kyc-free services listed     
    
> **\<ofrnxmr\>** <ofrnxmr> msvb-lab: No. I think they should do whatever they need to do on their own     
    
> **\<ofrnxmr\>** <ofrnxmr> "Fool me once? You fooled me. Fool me twice? ...i won't be fooled twice" - george w bush     
    
> **\<msvb-lab\>** Trocador and Orangefren do not list Changelly as a reputable service, right?     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> i dont think they list them at all      
    
> **\<msvb-lab\>** We can close this topic soon, but I plan to bring it back a couple times unless more than two people are informed about the situtation. I'm also planning to talk to Orangefren and Cake people, to find out what the truth is.     
    
> **\<orangefren\>** <orangefren> @plowsof:matrix.org: We do not     
    
> **\<msvb-lab\>** If nobody else has an opinion about Changelly, then we can move on to the next agenda item plowsof.     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> their public image is tarnished , no one has any reason to align themselves with them unless for a quick $     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> they need to fix their public image first     
    
> **\<ofrnxmr\>** <ofrnxmr> @plowsof:matrix.org: Coin Wallet aligns themselves with changelly 😂     
    
> **\<msvb-lab\>** Hi orangefren, cool. I think they are very aware that they need to fix their public image and are working (finally) to do so.     
    
> **\<msvb-lab\>** The question is if Changelly's recent efforts come from true intentions to do the right things and have really departed from the abuse in past years.     
    
> **\<ofrnxmr\>** <ofrnxmr> Actions speak louder than words. I don't think any dialog is going to change anything     
    
> **\<orangefren\>** <orangefren> They never seemed to care about their reputation as far as I can tell. For instance they never reached out to us     
    
> **\<msvb-lab\>** Because if they are permanently starting to do the right thing now and behave as well as most other groups, it would not make sense to punish them.     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> plowsofLLC would advise them to start a new shell company under a new name and figure it out from there     
    
> **\<msvb-lab\>** I still don't know about this, but let's please move on because the topic is taking too much time. I'll come back with another round in a month after researching a bit more.     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> thanks for bringing them up msvb-lab      
    
> **\<hbs:matrix.org\>** <hbs:matrix.org> @plowsof:matrix.org: They can call it Changedlly....     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> Orange Pi RV2 owners, rejoice, sech1 is making huge advancements for you and your mining farms      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> https://github.com/xmrig/xmrig/pull/3736 and https://github.com/xmrig/xmrig/pull/3740     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> Monero Blocks https://blocks.p2pool.observer/pools DataHoarder. beautiful      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> Rucknium is in the nginx/cert box config file trenches migrating moneroresearch.info to a new host and released some nice updates to the xmrspammer for stressnet https://github.com/Rucknium/xmrspammer     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> MAGIC 2nd funding round for fuzzing (and MAGIC committee applications begin) https://donate.magicgrants.org/monero/projects/fuzzing-monero-2      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> upcoming EigenWallet release from @binarybaron:matrix.org and @einliterflasche2:matrix.org  https://eigenwallet.org/changelog.html     
    
> **\<rucknium\>** <rucknium> Thanks especially to people using xmrspammer and reporting problems. Should be much more reliable for the beta stressnet.     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> how much starting capital did you put into your 9 wallets you brought online recently?      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> in sXMR     
    
> **\<ofrnxmr\>** <ofrnxmr> Upcoming basicswapdex release should have electrum support for btc-like wallets. No reliance to run nodes for every coin     
    
> **\<rucknium\>** <rucknium> 50 sXMR each. Much more than needed, but I have a few thousand sXMR to burn anyway.     
    
> **\<ofrnxmr\>** <ofrnxmr> https://mrelay.p2pool.observer/m/monero.social/kxqUrtRKArVnAjtldUCJZfxX.png (1765038548587581745232277023269.png)     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> UI looks very nice      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> displaying the electrum node/full node depending      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> anything else to touch on ( the blocksize war is on-going )     
    
> **\<ofrnxmr\>** <ofrnxmr> Lots of fud on twitter. Pretty annoying     
    
> **\<ofrnxmr\>** <ofrnxmr> Fwiw, zano and other cryptonote coins inherited the same 100mb packet size limit     
    
> **\<ofrnxmr\>** <ofrnxmr> And zcash has a 2mb(?) block size limit     
    
> **\<ofrnxmr\>** <ofrnxmr> i think i need to retract my opposition to sech1's max_weight mining param, as this is probably a cleaner way to add the limit w/o requiring a hard fork to remove it     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> can follow this via #monero-research-lounge:monero.social  #monero-research-lab:monero.social , lets cover the open CCS ideas     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> a. 39C3 Support (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/622)     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> this left off at the budget being shared https://repo.getmonero.org/-/project/54/uploads/756dd76bbdf11bf755ee30e67c907003/2025_Budget_CDC_39C3__rev2__-_main_2_.pdf     
    
> **\<plowsof\>** was discussed last meeting https://libera.monerologs.net/monero-community/20251122#c615861      
    
> **\<plowsof\>** open for feedback      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> moving on to cover the rest in the hour, do share feedback if you have any though     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> b. emsczkp research Bulletproofs* (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/626)     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> consensus from MRL to have this merged 👀     
    
> **\<rucknium\>** <rucknium> This was discussed at the last two MRL meetings     
    
> **\<emsczkp:matrix.org\>** <emsczkp:matrix.org> Hi, I’m the proposer of the Bulletproofs* research. Thank you all for giving me this slot.     
    
> **\<emsczkp:matrix.org\>** <emsczkp:matrix.org> just wanted to let the community know that this proposal has already been discussed in previous MRL meetings, and last meeting (on 3 December), it received strong consensus by the core team. I’m now waiting for the proposal to move to the next step.     
    
> **\<emsczkp:matrix.org\>** <emsczkp:matrix.org> https://libera.monerologs.net/monero-research-lab/20251203     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> thanks for clarifying , should then be merged at the next opportunity, not much else to discuss here then     
    
> **\<syntheticbird\>** <syntheticbird> i was in the back of the class, so i didn't know about this proposal. MERGE IT NOW OR I'LL STUFF A PUMPKIN IN PLOWSOF COMPUTER     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> thanks for joining      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> c. j-berman full-time part 12 (4 months) (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/628)     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> d. selsta part-time monero development (3 months) (19) (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/629)     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> e. vtnerd 2025 q4 (full-time) proposal (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/630)     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> ✅️ emojis have been left under jberman, selsta, and vtnerds proposals 😄     
    
> **\<syntheticbird\>** <syntheticbird> 6 emojis     
    
> **\<syntheticbird\>** <syntheticbird> per person     
    
> **\<@rottenwheel:unredacted.org\>** <plowsof:matrix.org> AOB: MAGIC Grants elections are live ^ > <@rottenwheel:unredacted.org> MAGIC Grants Monero Fund Committee elections are live! Nominate yourself, cast your votes away, if you feel like - https://github.com/MAGICGrants/Monero-Fund-Elections     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> 6 - 6 - 6 :(     
    
> **\<syntheticbird\>** <syntheticbird> 7 now     
    
> **\<syntheticbird\>** <syntheticbird> good job     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> would anyone like to bring some other business up?     
    
> **\<hbs:matrix.org\>** <hbs:matrix.org> I've published a report for the EVM-XMR Atomic Swap UI CCS     
    
> **\<hbs:matrix.org\>** <hbs:matrix.org> milestone 1 is done, on track to finalize milestone 2 by the end of the year/early Q1 2026.     
    
> **\<hbs:matrix.org\>** <hbs:matrix.org> and worked on a maker bot which should be testable around Xmas     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/597#note_33358     
    
> **\<nioc\>** "Given the recent price appreciation of Monero, I've decided to spend some time building a maker bot without filing a separate proposal as was initially planned."     
    
> **\<nioc\>** w0w     
    
> **\<ofrnxmr\>** <ofrnxmr> redsh4de also lowered the xmr amount on their funding req due to price appreciation     
    
> **\<ofrnxmr\>** <ofrnxmr> Some honorable / admirable actions from both     
    
> **\<nioc\>** was that b4 funding?     
    
> **\<ofrnxmr\>** <ofrnxmr> Nope     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/627/diffs     
    
> **\<ofrnxmr\>** <ofrnxmr> its not funded yet, but was already up for funding when the amount was lowered     
    
> **\<nioc\>** https://ccs.getmonero.org/funding-required/     
    
> **\<sneedlewoods_xmr:matrix.org\>** <sneedlewoods_xmr:matrix.org> question: Is there a rule that prevents having 2 CCS proposals?     
    
> **\<msvb-lab\>** What is the status of organising Monerokon in Turkiye? Does anybody have an opinion about this?     
    
> **\<sneedlewoods_xmr:matrix.org\>** <sneedlewoods_xmr:matrix.org> I have this WIP proposal https://ccs.getmonero.org/proposals/SNeedlewoods-02_part-time-dev-work.html for which I recently made pull requests and I'm waiting for reviews.     
    
> **\<sneedlewoods_xmr:matrix.org\>** <sneedlewoods_xmr:matrix.org> I'd like to make a new proposal starting in January to continue dev work, but my WIP wont be finished by then, so I would make sure I have enough time for work on review comments     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> the xmr-xmr precedent allows this      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> mj-xmr*     
    
> **\<syntheticbird\>** <syntheticbird> @sneedlewoods_xmr:matrix.org: no rule prohibit this, it's more a pr problem     
    
> **\<syntheticbird\>** <syntheticbird> aka "do public consider that you can fight on both front"     
    
> **\<ofrnxmr\>** <ofrnxmr> msvb-lab: @orangefren:monero.social  may be interested in organizing a monerokon     
    
> **\<sneedlewoods_xmr:matrix.org\>** <sneedlewoods_xmr:matrix.org> alright, will write a proposal then and see what the feedback is, thanks     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> sneedlewoods so you have to wait for reviews to continue?      
    
> **\<sneedlewoods_xmr:matrix.org\>** <sneedlewoods_xmr:matrix.org> btw nice to see you're alive SyntheticBird      
    
> **\<syntheticbird\>** <syntheticbird> @sneedlewoods_xmr:matrix.org: thx you very much. but I'm actually undead     
    
> **\<msvb-lab\>** It seems some (maybe many) people don't like Turkiye in general, for good reasons that unfortunately apply to 90% of other countries as well.     
    
> **\<orangefren\>** <orangefren> @ofrnxmr: Briefly:     
    
> **\<orangefren\>** <orangefren> Following a failure to secure a venue in Belgrade we reached out to a venue we previously used for a meetup in Turkey. They are interested in hosting and capable of doing so. We are ironing out the details. Our team hasn't decided on pursing this yet, but if we reach consensus internally and don't run into any deal breakers with the venue then we intend on organising it     
    
> **\<sneedlewoods_xmr:matrix.org\>** <sneedlewoods_xmr:matrix.org> @plowsof:matrix.org: the way I phrased it, the milestone for the CCS is completed "when the code is merged into monero project", which in hindsight was not the wisest decision     
    
> **\<ofrnxmr\>** <ofrnxmr> msvb-lab: The food?     
    
> **\<orangefren\>** <orangefren> @ofrnxmr: The food is amazing     
    
> **\<ajs_\>** <ajs_> Turkey is a great place, been living there for years, but it is currently not the safest place for developers working on privacy tech     
    
> **\<ofrnxmr\>** <ofrnxmr> @sneedlewoods_xmr:matrix.org: Merge shouldnt be a req before moving on. There are prs that dont get merged for yrs, and yours is rather large     
    
> **\<syntheticbird\>** <syntheticbird> I got once in Turkey, and there was a sniper rifle in the front glass of a shop     
    
> **\<syntheticbird\>** <syntheticbird> that's a hell of place     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> an open end to the meeting here, thanks all for attending      
    
> **\<syntheticbird\>** <syntheticbird> thanks plowsof     
    
> **\<plowsof\>** this meeting was sponsored by the Universal Time Constant and the holiday spirit      

Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

continued:
```
17:07:35 <br-m> <rottenwheel:unredacted.org> Maybe kernal.eu (XMR ATM and MoneroPay) people might be able to chime in. I think they went to/from Turkey often. Temporary residency, whatever. 🤔
17:07:35 <br-m> <rottenwheel:unredacted.org> RIP one of MoneroKon's directors...
17:07:57 <msvb-lab> Thanks for a good meeting and thanks plowsof for the good moderation.
17:11:34 <br-m> <orangefren> nioc: Is there a place that openly welcomes privacy devs? I don't know of one
17:12:17 <br-m> <hbs:matrix.org> @orangefren: Theses days seems mainly court houses and prisons
17:12:48 <nioc> I am cluleess, was just sharing an opinion of someone with experience 
17:13:21 <nioc> the usa should be safe if we donate to the ballroom  :D
17:14:02 <br-m> <redsh4de:matrix.org> Hello everyone!
17:14:02 <br-m> <redsh4de:matrix.org> Updates from my side on the website redesign project:
17:14:02 <br-m> <redsh4de:matrix.org> * The blog is live, with pagination and a RSS feed![... more lines follow, see https://mrelay.p2pool.observer/e/tJCd8c8KRm9pZUVR ]
17:14:22 <nioc> fund this person  ^^
18:04:44 <DataHoarder> Yep hinto, I have been holding up from doing observe updates and I have been doing major v5 changes to go consensus
```

# Action History
- Created by: plowsof | 2025-12-02T13:28:07+00:00
- Closed at: 2025-12-08T22:15:03+00:00
