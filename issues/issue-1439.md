---
title: 'Monero Community Workgroup Meeting: Sat, 2026-08-08 16:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1439
author: nahuhh
assignees: []
labels: []
created_at: '2026-08-07T21:48:43+00:00'
updated_at: '2026-08-09T08:21:03+00:00'
type: issue
status: closed
closed_at: '2026-08-09T08:21:03+00:00'
---

# Original Description
Location: [Libera.chat, #monero-community](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-community:monero.social?via=matrix.org&via=monero.social)

[Instructions for joining the monero.social Matrix server.](https://www.getmonero.org/resources/user-guides/join-monero-matrix.html)

Time
16:00 UTC [Check your timezone](https://www.timeanddate.com/worldclock/converter.html)

Moderator: ofrnxmr

Please reach out in advance of the meeting if you would like to propose an agenda item.


Proposed Meeting Items:

1. Introduction
2. Greetings
3. Community highlights    
News: [Revuo Monero](https://revuo-xmr.com/) - [This week in Monero TWIM](https://cyphergoat.com/this-week-in-monero)  
4. CCS proposals  
  a. [MRL] Dennis Trautwein - [ProbeLab P2P Network Metrics Proposal](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/667)    
  b. acx - [part-time monfluo](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/690)  
  c. jpk68 - [full-time work (3 months)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/689)  
  d. panagot12 [Monero LWS Observatory — Public LWS Health](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/686)  
  e. v1docq47 - [monero konferenco 2026 voice-over and working on xmr.ru](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/683)  
  f. r4v3r23 - [ANONERO Continued development](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/671)  
5. Workgroup reports    
  a. Dev workgroup  
  b. Localization workgroup  
  c. Outreach workgroup  
  d. Events workgroup  
  e. Website workgroup  
  f. Policy workgroup  
  g. Research workgroup  
  h. [FCMP++ stressnet](https://github.com/seraphis-migration)
6. Open ideas time    
7. Confirm next meeting date/time    

[Previous meeting including logs](https://github.com/monero-project/meta/issues/1429)

# Discussion History
## nahuhh | 2026-08-08T17:02:02+00:00
Logs 
    
> **\<ofrnxmr\>** Meeting time: https://github.com/monero-project/meta/issues/1439     
    
> **\<ofrnxmr\>** Hello all     
    
> **\<syntheticbird\>** End of meeting     
    
> **\<syntheticbird\>** Hello     
    
> **\<jpk68:matrix.org\>** Hello     
    
> **\<pw:xmr.mx\>** hello     
    
> **\<slowbeardigger:matrix.org\>** hola/hello     
    
> **\<sneedlewoods_xmr:matrix.org\>** hi     
    
> **\<ofrnxmr\>** while waiting for people to arrive, lets get into the highlights over the past 2 weeks     
    
> **\<ofrnxmr\>** @syntheticbird     
    
> **\<syntheticbird\>** CUPRATE KESTERITE HAS BEEN RELEASED     
    
> **\<syntheticbird\>** DOWNLOAD NOW     
    
> **\<syntheticbird\>** ITS VERY FAST     
    
> **\<jpk68:matrix.org\>** Speaking of fast, some effort was also put into speeding up wallet sync in monerod (the graphs were a powerful motivator)     
    
> **\<ofrnxmr\>** Don't count those chickens yet, monerod might catch up :P     
    
> **\<jpk68:matrix.org\>** https://mrelay.p2pool.observer/m/matrix.org/ofvrHSrhiWSJAaeTPOJxoYPU.png (clipboard.png)     
    
> **\<jpk68:matrix.org\>** h/t @boog900:monero.social     
    
> **\<plowsof\>** Hi     
    
> **\<nioc\>** syntheticbird thx 4 the motivation  :)     
    
> **\<syntheticbird\>** 🫶.     
    
> **\<nioc\>** is it too early to shill for more motivation?     
    
> **\<jpk68:matrix.org\>** We attempted to decrease the lock contention during hot paths, which resulted in a ~2.85x throughput increase when syncing 16 wallets at once     
    
> **\<nioc\>** https://ccs.getmonero.org/proposals/syntheticbird_cuprate_scs_ab_3_months.html     
    
> **\<slowbeardigger:matrix.org\>** havent had coffee, so yes.     
    
> **\<slowbeardigger:matrix.org\>** kiddin'     
    
> **\<ofrnxmr\>** no other highlights?     
    
> **\<ofrnxmr\>** i feel like im forgetting something     
    
> **\<syntheticbird\>** there is something COLD that happened but that doesnt' concern monero     
    
> **\<nioc\>** yes, koe was OVER FUNDED  :P     
    
> **\<syntheticbird\>** oh right     
    
> **\<syntheticbird\>** 🎉     
    
> **\<pw:xmr.mx\>** wtf since when did confetti fill the screen     
    
> **\<syntheticbird\>** bro its beenn 10 years     
    
> **\<syntheticbird\>** back when matrix was called Riot     
    
> **\<syntheticbird\>** there is also     
    
> **\<thomasbuilds:matrix.org\>** hello guys     
    
> **\<pw:xmr.mx\>** maybe update I done other day has changed something in setting's then. never seen that happen before     
    
> **\<slowbeardigger:matrix.org\>** hallo     
    
> **\<ofrnxmr\>** News: Revuo Monero - This week in Monero TWIM << no news since the last meeting     
    
> **\<pw:xmr.mx\>** not weekly thenm     
    
> **\<thomasbuilds:matrix.org\>** syntheticbird can you run ci for https://github.com/Cuprate/cuprate/pull/668 :)     
    
> **\<hbs:matrix.org\>** aloha     
    
> **\<ofrnxmr:xmr.mx\>** revuo is quarterly /s     
    
> **\<syntheticbird\>** sure thomas     
    
> **\<ofrnxmr\>** 4. CCS proposals     
    
> **\<ofrnxmr\>** a. [MRL] Dennis Trautwein - ProbeLab P2P Network Metrics Proposal     
    
> **\<ofrnxmr\>** not sure whats going on with this one, no activity, havent heard anything from the proposer(s) in over a month     
    
> **\<ofrnxmr:xmr.mx\>** guess will need to ping them again - if no response, probably close it?     
    
> **\<plowsof\>** they are around. they want to know the next steps.     
    
> **\<ofrnxmr:xmr.mx\>** okok     
    
> **\<ofrnxmr:xmr.mx\>** well, they can respond to the comments on the proposal (i missed mrl meeting, must be where they are)     
    
> **\<plowsof\>** $40k for 1.5 person months -> "let the donors decide" / and i think im the only one who mentioned that on the CCS comment so must not be a big concern     
    
> **\<nioc\>** did not notice them at the last MRL meeting     
    
> **\<syntheticbird\>** bold of you plowsof to assume we all donors can read     
    
> **\<ofrnxmr\>** he didnt, which is why he has to ask the proposer     
    
> **\<plowsof\>** https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/667#note_36602     
    
> **\<pw:xmr.mx\>** plowsof: $40k for what?     
    
> **\<ofrnxmr\>** for the proposal that he just linked     
    
> **\<syntheticbird\>** * thumbs up to plowsof *     
    
> **\<ofrnxmr\>** ohh, thanks plowsof. i forgot to post the link :')     
    
> **\<syntheticbird\>** anyway that'll be a -1 for me     
    
> **\<ofrnxmr:xmr.mx\>** personally, im not a fan of the proposal. it started off very corporate, and was a paid service     
    
> **\<ofrnxmr:xmr.mx\>** felt to me like we were funding blockchain surveillance     
    
> **\<jpk68:matrix.org\>** It's also not fully open-source, I don't think     
    
> **\<syntheticbird\>** i am all for blockchain surveillance as long as its open source     
    
> **\<ofrnxmr:xmr.mx\>** since they will ofc sell their services to whoever     
    
> **\<ofrnxmr:xmr.mx\>** im not for funding for-profit BS     
    
> **\<slowbeardigger:matrix.org\>** -1     
    
> **\<ofrnxmr:xmr.mx\>** if its free, and available to mrl for free, forever, i have np with it     
    
> **\<ofrnxmr:xmr.mx\>** if we pay to build it, then have to pay to access it, thats not cool     
    
> **\<ofrnxmr:xmr.mx\>** lol     
    
> **\<ofrnxmr:xmr.mx\>** dont quote me - the proposal has changed since the early iterations where this was the case     
    
> **\<ofrnxmr:xmr.mx\>** i still am not a fan. MRL ack'd the reduced scope, but a few downvotes here, so we're at a crossroads     
    
> **\<hbs:matrix.org\>** If it's their business, why should the community fund any of it?     
    
> **\<plowsof\>** because     
    
> **\<hbs:matrix.org\>** plowsof: oh ok, makes sense     
    
> **\<plowsof\>** lol     
    
> **\<ofrnxmr:xmr.mx\>** plowsof: "because that why, you see?"     
    
> **\<ofrnxmr\>** ok, moving on     
    
> **\<ofrnxmr\>** b. acx - part-time monfluo https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/690     
    
> **\<ofrnxmr\>** i didnt forget the link this time     
    
> **\<jpk68:matrix.org\>** +1     
    
> **\<syntheticbird\>** +1     
    
> **\<slowbeardigger:matrix.org\>** +1     
    
> **\<sneedlewoods_xmr:matrix.org\>** +1     
    
> **\<pw:xmr.mx\>** +1     
    
> **\<ofrnxmr\>** c. jpk68 - full-time work (3 months) https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/689     
    
> **\<plowsof\>** will be nice to see how their monero-oxide stuff alleviates the monero dependency problems mobile devs encounter     
    
> **\<slowbeardigger:matrix.org\>** ofrnxmr: The funding stuff has been resolved since the last meeting?     
    
> **\<syntheticbird\>** press +1 if you are a bad person     
    
> **\<sneedlewoods_xmr:matrix.org\>** +1, also left a comment     
    
> **\<pw:xmr.mx\>** c +1     
    
> **\<jpk68:matrix.org\>** Thank you for your support, everyone <3     
    
> **\<syntheticbird\>** +1     
    
> **\<jpk68:matrix.org\>** Regarding funding: I contacted Gingeropolous and he said he would comment on the proposal within two weeks     
    
> **\<slowbeardigger:matrix.org\>** +1     
    
> **\<jpk68:matrix.org\>** I still believe the proposal qualifies as "future work", but again, it's not a hard requirement     
    
> **\<ofrnxmr\>** d. panagot12 Monero LWS Observatory — Public LWS Health https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/686     
    
> **\<ofrnxmr\>** lolwtf?     
    
> **\<jpk68:matrix.org\>** Not sure why this hasn't been closed yet :|     
    
> **\<syntheticbird\>** me when ping cloudflare.com     
    
> **\<slowbeardigger:matrix.org\>** still 404 the repo     
    
> **\<ofrnxmr\>** they made the repo public, and dm'd me on twitter (i think, dont remember) about it     
    
> **\<jpk68:matrix.org\>** NACK     
    
> **\<ofrnxmr\>** now it 404s again     
    
> **\<ofrnxmr\>** hard close for breaking the rules     
    
> **\<slowbeardigger:matrix.org\>** you can’t have a proposal on the ccs and have the repo like that, or can you?     
    
> **\<ofrnxmr\>** @jpk, not closed because we give everyone a fair chance     
    
> **\<ofrnxmr\>** you can not, correct     
    
> **\<plowsof\>** thomas builds can complete this on a random sunday afternoon     
    
> **\<syntheticbird\>** lmao     
    
> **\<slowbeardigger:matrix.org\>** ofrnxmr: So will be closed?     
    
> **\<slowbeardigger:matrix.org\>** -1 anyways     
    
> **\<ofrnxmr\>** i am voting for it to be closed     
    
> **\<syntheticbird\>** i am voting for author to be tortured     
    
> **\<slowbeardigger:matrix.org\>** ofrnxmr: +1 to be closed     
    
> **\<slowbeardigger:matrix.org\>** @syntheticbird: feathers involved?     
    
> **\<plowsof\>** seriously though if LWS can't be trusted to just not work, sometimes, id rather see pull requests upstream to make it more stable if thats the case     
    
> **\<syntheticbird\>** @slowbeardigger:matrix.org: as a bird? yes     
    
> **\<slowbeardigger:matrix.org\>** good\     
    
> **\<ofrnxmr:xmr.mx\>** speaking of LWS, this is a bit off topic, but @plowsof i dont think we should be listing that lws csharp lib on getmonero     
    
> **\<syntheticbird\>** reasoning?     
    
> **\<plowsof\>** from btcpayserver monero devs?     
    
> **\<ofrnxmr:xmr.mx\>** its under a year old, about 5 commits for the whole repo, hasnt been touched in 5 months, and lws is a moving target     
    
> **\<ofrnxmr:xmr.mx\>** yes     
    
> **\<syntheticbird\>** +1 to remove     
    
> **\<ofrnxmr:xmr.mx\>** its not listed yet, but there is a new pr to add it     
    
> **\<syntheticbird\>** +1 to close it     
    
> **\<ofrnxmr:xmr.mx\>** i forgot to comment about it, and just wanted to say something     
    
> **\<ofrnxmr\>** e. v1docq47 - monero konferenco 2026 voice-over and working on xmr.ru https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/683     
    
> **\<slowbeardigger:matrix.org\>** +1     
    
> **\<ofrnxmr:xmr.mx\>** Im still a +1 here, but still want to wait for other proposals to be funded since this likely isnt urgent     
    
> **\<slowbeardigger:matrix.org\>** @ofrnxmr:xmr.mx: agreed     
    
> **\<ofrnxmr:xmr.mx\>** https://ccs.getmonero.org/funding-required/     
    
> **\<ofrnxmr\>** and last, but not least     
    
> **\<ofrnxmr\>** f. r4v3r23 - ANONERO Continued development https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/671     
    
> **\<slowbeardigger:matrix.org\>** -1     
    
> **\<slowbeardigger:matrix.org\>** tbh i see Anonero a bit redundant     
    
> **\<ravfx:xmr.mx\>** +1 for Anonero     
    
> **\<syntheticbird\>** +1     
    
> **\<plowsof\>** latest update on this was a support comment from vik / cake wallet https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/671#note_37062 "While @r4v3r23 hasn't been kind to me, Cake Wallet, or our team historically, but that shouldn't stop us from supporting independent builders"     
    
> **\<plowsof\>** for this current proposal we have a kotlin dev that didn;t notice the deps where >3 years old since anoneros inception     
    
> **\<ofrnxmr:xmr.mx\>** the longer this frags on, the more i wonder about the longevity -- plowsof pointed out some serious vulns that have yet to be fixed     
    
> **\<plowsof\>** freeze/thaw , pay to many, and account support exist already in monfluo which is also a fork of monerujo     
    
> **\<ofrnxmr:xmr.mx\>** http://git.anonero5wmhraxqsvzq2ncgptq6gq45qoto6fnkfwughfl4gbt44swad.onion/ANONERO/ANONERO/commits/branch/main     
    
> **\<ofrnxmr:xmr.mx\>** some / at least 1     
    
> **\<ofrnxmr:xmr.mx\>** which has already been fixed on a fork, and iirc on feather     
    
> **\<plowsof\>** has the community had any input on the new UI?     
    
> **\<ofrnxmr:xmr.mx\>** s/frags/drags     
    
> **\<plowsof\>** are they going to rely on AI to complete the milestones? https://git.disroot.org/iuanv9/anonero-fork/pulls     
    
> **\<ofrnxmr:xmr.mx\>** the cost, the features, etc. i dont really have a problem with any of that. just that the current dev seems not willing to maintain it unless the money is on the table, so how does that play out in the long run?     
    
> **\<syntheticbird\>** it doesn't     
    
> **\<plowsof\>** syntheticbird have you used anonero wallet?     
    
> **\<syntheticbird\>** during a short period of time     
    
> **\<syntheticbird\>** a year ago     
    
> **\<syntheticbird\>** does that count ?     
    
> **\<plowsof\>** i guess so     
    
> **\<plowsof\>** a fresh wallet for one time use / testing?     
    
> **\<syntheticbird\>** just testing since cake wallet syncing over tor was duper slow and I wanted to test out other monero only wallets     
    
> **\<ofrnxmr:xmr.mx\>** i have it installed but never use it because of the tor requirement. i dont remember if it bypasses tor to allow local/lan nodes     
    
> **\<ravfx:xmr.mx\>** I did a second test run for that one, And actually it's the better option (cupcake UI is "laggy" on my old motorola), Monerujo still permacrash after importing the view key from it's airgap companion app     
    
> **\<ofrnxmr:xmr.mx\>** and dont use it as air-gapped, because anon has internet permissions     
    
> **\<plowsof\>** (release attempts openssl handshakes even on tor but thats upstream) and anonero is also slow on tor - but the ui will freeze while syncing an old wallet or just crash     
    
> **\<ravfx:xmr.mx\>** Yeah, I wish he would have a "airgap" mode that remove node syncing and all that shit (because it's kind of anoying to see the thing sync full time when you open it     
    
> **\<ofrnxmr:xmr.mx\>** anon is the airgap / offline signer half     
    
> **\<plowsof\>** during set up you select a node (for your air gapped wallet)     
    
> **\<plowsof\>** and your airgapped wallet begins to sync from that node     
    
> **\<ravfx:xmr.mx\>** Yeah, it's just the anoyance of the "offline signer" trying to sync all the time on a phone without internet     
    
> **\<ravfx:xmr.mx\>** Even without node configured     
    
> **\<ravfx:xmr.mx\>** A few fixes but at the end it could be a good option     
    
> **\<ravfx:xmr.mx\>** Also Anon don't seam to LOCK itself if you don't "exit" it once your done     
    
> **\<ofrnxmr:xmr.mx\>** it also loads the ui before the lockscreen     
    
> **\<ravfx:xmr.mx\>** like you unlock phone  a few hours later and your right in the wallet, no unlock needed     
    
> **\<ofrnxmr:xmr.mx\>** this is what i mean about maintenance     
    
> **\<ofrnxmr:xmr.mx\>** the last dev just seems to have up and left once the funds ran out     
    
> **\<plowsof\>** so we have more upvotes than down to merge ANONERO as is     
    
> **\<ofrnxmr:xmr.mx\>** im not against merging it     
    
> **\<pw:xmr.mx\>** @ofrnxmr:xmr.mx: i thought there was new devs ready to go flat out on it and if milestones were not met (after reducing the time scales a month ago) he was happy for funding to go else where ?     
    
> **\<ofrnxmr:xmr.mx\>** but i guess it might be a good idea to confirm that the dev is still availale     
    
> **\<pw:xmr.mx\>** it seems all over the place imho     
    
> **\<ofrnxmr:xmr.mx\>** @pw:xmr.mx: the devs last commit was updating dependencies 2 months ago     
    
> **\<pw:xmr.mx\>** you did say don't reduce the time scales, keep it long and it's ok to finish early     
    
> **\<pw:xmr.mx\>** -1     
    
> **\<ofrnxmr:xmr.mx\>** thats what i said, yes. raver said that the dev would stay on for a year regardless     
    
> **\<ofrnxmr:xmr.mx\>** "Update: Guaranteed 40 hours per week. Milestones 1-3 will be completed within 3 months of funding, with Milestone 4 estimated to take ~1 month. Support/maintenance commitment for 1 year."     
    
> **\<plowsof\>** if the dev deosnt come back for 100 odd monero im sure someone else can audition to do the work     
    
> **\<ofrnxmr:xmr.mx\>** fair     
    
> **\<plowsof\>** kotlin devs that are willing to make merges outside of core that are reviewed by themselves     
    
> **\<ofrnxmr\>** btw, i skipped jeffro since im assuming that is just awaiting merge     
    
> **\<plowsof\>** yes (with 1 milestone already completed)     
    
> **\<ofrnxmr\>** ok, thats all folks. need to get back into my research into defeating syntheticbird and the evil cuprate kestrintueisdes     
    
> **\<ofrnxmr\>** Next meeting Sat Aug 22, 2026, 1600 UTC     
    
> **\<sneedlewoods_xmr:matrix.org\>** thanks everyone     
    
> **\<syntheticbird\>** thanks     
    
> **\<plowsof\>** thnx     
    
> **\<slowbeardigger:matrix.org\>** take care ppl     

Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: nahuhh | 2026-08-07T21:48:43+00:00
- Closed at: 2026-08-09T08:21:03+00:00
