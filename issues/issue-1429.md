---
title: 'Monero Community Workgroup Meeting: Sat, 2026-07-25 16:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1429
author: nahuhh
assignees: []
labels: []
created_at: '2026-07-24T18:05:04+00:00'
updated_at: '2026-08-07T22:52:05+00:00'
type: issue
status: closed
closed_at: '2026-08-07T22:52:05+00:00'
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
  a. jeffro256 - [2026 q2, full time development](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/688)  
  b. [MRL] Dennis Trautwein - [ProbeLab P2P Network Metrics Proposal](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/667)    
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

[Previous meeting including logs](https://github.com/monero-project/meta/issues/1418)

# Discussion History
## nahuhh | 2026-08-07T22:51:29+00:00
Logs 
    
> **\<ofrnxmr\>** Meeting time. https://github.com/monero-project/meta/issues/1429     
    
> **\<plowsof\>** hello     
    
> **\<slowbeardigger:matrix.org\>** hi     
    
> **\<DataHoarder\>** 👀     
    
> **\<nioc\>** meow     
    
> **\<ofrnxmr\>** Just a few of us here today, so lets just have a short meeting, since the last one was 2.5hrs     
    
> **\<ofrnxmr\>** We can come back next week     
    
> **\<ofrnxmr\>** 3. Community highlights     
    
> **\<slowbeardigger:matrix.org\>** Let’s wait like 5-10 more mins if that’s ok     
    
> **\<slowbeardigger:matrix.org\>** maybe more people will join     
    
> **\<ofrnxmr\>** After a 3 months break, https://revuo-xmr.com/ posted a new issue     
    
> **\<sgp_\>** https://magicgrants.org/2026/07/20/Skylight-Wallet-in-F-Droid     
    
> **\<sgp_\>** Skylight Wallet is now on the official F-Droid store, with reproducible builds (including for monero_c)     
    
> **\<ofrnxmr\>** BasicSwapDEX was hit with an exploit on the refund path. Known loss = 0.66 BTC (total known 0.661 BTC total losses across 2 exploits)     
    
> **\<plowsof\>** DataHoarders transaction scanning suite propels a closed source 7 second full chain scanner which sech1 has seen first hand working     
    
> **\<sgp_\>** Zero “anti features.” The option for local scanning with a node (like other Monero wallets) is coming soon^tm     
    
> **\<DataHoarder\>** plowsof: I pointed out from there, it's different codebases :D     
    
> **\<mrcyjanek0:matrix.org\>** Does skylight plan to contribute changes back?     
    
> **\<ofrnxmr\>** I can confirm skylight is a reproducible build, as fdroid happily updated my local skylight (same signing key)     
    
> **\<DataHoarder\>** again I did not develop that other one besides making that Tari bruteforcer :)     
    
> **\<plowsof\>** bootstraps, inspires? :D     
    
> **\<sgp_\>** @mrcyjanek0:matrix.org: It’s all MIT so take what you want     
    
> **\<plowsof\>** codeberg says no to cryptocurrency projects - not sure where this leaves wownero cc jwinterm     
    
> **\<mrcyjanek0:matrix.org\>** LGPL*     
    
> **\<jpk68:matrix.org\>** Hello     
    
> **\<ofrnxmr\>** Wownero ia movonf to git.suchwow (or whatever the address is) with an already existing github mirror     
    
> **\<ofrnxmr\>** monfluo and moneroswap are looking for new homes as well     
    
> **\<jpk68:matrix.org\>** I have moved my Monero-related project(s) off of Codeberg for the time being. Also investigating self-hosting Forgejo     
    
> **\<DataHoarder\>** remember you can always have your own forge that auto-pushes/syncs onto github/codeberg/whatever else you have out there (I do this myself with a bunch of my projects that I run on my gitea/forgejo instance)     
    
> **\<sgp_\>** @mrcyjanek0:matrix.org  https://github.com/MAGICGrants/skylight-wallet/blob/main/scripts/reproducible.patch     
    
> **\<DataHoarder\>** I'd recommend self-hosting forgejo. Self-contained and quite compatible API     
    
> **\<sgp_\>** Otherwise it just pulls from vtnerd’s fork     
    
> **\<mrcyjanek0:matrix.org\>** ah okay, thanks!     
    
> **\<sgp_\>** If anything is unclear of how you can use it, let me know and I’d be happy to help     
    
> **\<mrcyjanek0:matrix.org\>** Appreciate it! Looks straightforward ^^     
    
> **\<ofrnxmr\>** If that's all for news, we can move on to the CCS proposals     
    
> **\<ofrnxmr\>** a. jeffro256 - 2026 q2, full time development https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/688     
    
> **\<nioc\>** merge please     
    
> **\<jpk68:matrix.org\>** +1     
    
> **\<slowbeardigger:matrix.org\>** +1     
    
> **\<mrcyjanek0:matrix.org\>** +1     
    
> **\<nioc\>** a great mixture of talent and motivation     
    
> **\<ofrnxmr\>** b. [MRL] Dennis Trautwein - ProbeLab P2P Network Metrics Proposal https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/667     
    
> **\<slowbeardigger:matrix.org\>** -1     
    
> **\<ofrnxmr\>** this still has unaddressed comments, not sure if they maybe just havent seen them and need a ping?     
    
> **\<nioc\>** I am clueless and will leave this to MRL     
    
> **\<jpk68:matrix.org\>** No opinion on this one     
    
> **\<ofrnxmr\>** MRL helped shape the new proposal scope, which is why it is still open. but pending comments being addressed     
    
> **\<ofrnxmr\>** c. jpk68 - full-time work (3 months) https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/689     
    
> **\<slowbeardigger:matrix.org\>** +1     
    
> **\<ofrnxmr:xmr.mx\>** i havent yet commented on the proposal, only read through it once, and my first takeaway is that, if merged,  it should not be funded using i2p bounty     
    
> **\<mrcyjanek0:matrix.org\>** +1 love the i2p stuff!     
    
> **\<slowbeardigger:matrix.org\>** @mrcyjanek0:matrix.org: right????     
    
> **\<ofrnxmr:xmr.mx\>** i2p was a different ccs @mrcyjanek0:matrix.org     
    
> **\<jpk68:matrix.org\>** @ofrnxmr:xmr.mx: Fair point. It's just a preference, however :)     
    
> **\<ofrnxmr:xmr.mx\>** if the work was specifically to add torcontrol support, you could argue for the funding from the bounty     
    
> **\<mrcyjanek0:matrix.org\>** @ofrnxmr:xmr.mx: I know, just mentioning that I like it     
    
> **\<jpk68:matrix.org\>** If the work was just for Tor Control, I would be sitting around like 70% of the time     
    
> **\<jpk68:matrix.org\>** Might as well make myself useful in the meantime ;)     
    
> **\<ofrnxmr:xmr.mx\>** bounty money is already supposed to be for a specific purpose. putting it towards misc tasks would be misappropriation     
    
> **\<jpk68:matrix.org\>** Since Gingeropolous is/was the creator of that bounty, I would like to hear what he thinks about this. If he or the majority of people don't like it, I'll remove it     
    
> **\<ofrnxmr:xmr.mx\>** if there was a specific milestone for torcontol, you could argue for that amount etc. this is just my opinion, particularly because we are already outside of the norm by using bounty money for ccs proposals     
    
> **\<ofrnxmr:xmr.mx\>** its not gingers money.     
    
> **\<ofrnxmr:xmr.mx\>** i think the proper path to requesting those funds, would be a specific torcontrol milestone and that amount to be requested     
    
> **\<jpk68:matrix.org\>** Fair. I will consider removing the bounty-related paragraph in that case, as another milestone-based proposal would not be convenient     
    
> **\<ofrnxmr:xmr.mx\>** imo, i dont think specific feature add (torcontrol) in the ccs would be accepted unless it is milestoned     
    
> **\<rottenwheel:unredacted.org\>** @jpk68:matrix.org: your CCS idea has been shared via @MoneroSpace on X. https://x.com/MoneroSpace/status/2081056411925225587 // nitter: https://xcancel.com/MoneroSpace/status/2081056411925225587     
    
> **\<nioc\>** are we talking about adding a tor control milestone into the proposal ?     
    
> **\<ofrnxmr:xmr.mx\>** yes, nioc     
    
> **\<ofrnxmr:xmr.mx\>** its mentioned in the proposal, but there are no milestones     
    
> **\<jpk68:matrix.org\>** I don't see how that would make any difference. The proposal is to work 40 hours per week on things, including Tor Control     
    
> **\<nioc\>** rules  :D     
    
> **\<ofrnxmr:xmr.mx\>** and if you dont finish torcontrol?     
    
> **\<slowbeardigger:matrix.org\>** "For this CCS, I plan to work on the following areas:     
    
> **\<slowbeardigger:matrix.org\>** Begin work on support for the Tor Control protocol in monerod, specifically for automatically configuring onion services     
    
> **\<slowbeardigger:matrix.org\>** Look into integrating the existing I2P SAM implementation into 'core' wallet code for use with remote nodes     
    
> **\<slowbeardigger:matrix.org\>** Continue to improve the usability, scope, and feature parity of the Monero GUI[... more lines follow, see https://mrelay.p2pool.observer/e/3pyWnZoLZnRackRN ]     
    
> **\<jpk68:matrix.org\>** I believe I have had quite a good track record in terms of being productive, and making good use of time. It's not like I'm going to purposely drag my feet and be lazy just to get funding without doing anything     
    
> **\<ofrnxmr:xmr.mx\>** thats not the point. you requested bounty funds for a feature that you may  or may not complete     
    
> **\<slowbeardigger:matrix.org\>** @ofrnxmr:xmr.mx: Maybe defining this properly in the ccs?     
    
> **\<jpk68:matrix.org\>** @ofrnxmr:xmr.mx: As I said, that can be removed.     
    
> **\<ofrnxmr:xmr.mx\>** @slowbeardigger:matrix.org: thats the request for milestones     
    
> **\<jpk68:matrix.org\>** All of my contributions so far, excluding I2P SAM work, have been unpaid     
    
> **\<ofrnxmr:xmr.mx\>** that has nothing to do with anything?     
    
> **\<jpk68:matrix.org\>** @ofrnxmr:xmr.mx: My point is that I don't understand the concern of not making good use of time, and therefore I don't agree with the milestone proposal except from the standpoint of receiving bounty funding.     
    
> **\<ofrnxmr:xmr.mx\>** its not a concern of making good use of time     
    
> **\<ofrnxmr:xmr.mx\>** right. if you arent requesting bounty funds, then the milestones arent as important     
    
> **\<jpk68:matrix.org\>** I understand, and have said I will consider removing the bounty note.     
    
> **\<jpk68:matrix.org\>** I appreciate your concern /srs     
    
> **\<ofrnxmr:xmr.mx\>** but deliverables do matter, and if torcontrol is one of them, then then it would be nice to see it completed instead of rolled into 9 months of proposals (not saying tha tyou will, but look at current funding efforts)     
    
> **\<ofrnxmr:xmr.mx\>** bounty funds = milestone = no issue getting funding. no bounty funds = it might not be funded if vaguely written with no promises or guarantees     
    
> **\<ofrnxmr:xmr.mx\>** synthethic has been a largely unpaid contributor for like, 3 years now     
    
> **\<ofrnxmr:xmr.mx\>** its not just about getting it merged, its about giving it the best chance of being funded     
    
> **\<ofrnxmr:xmr.mx\>** need to think about it from the perspective of donors. you have a "hack" where you can bypass the trouble and potentially get the money directly from the bounty. but that requires a torcontrol milestone. essentially a tor version of your last proposal. otherwise, you need to do some marketing etc to try to gather donors, since its appears to be a drought     
    
> **\<ofrnxmr:xmr.mx\>** "dont set yourself up for failure"     
    
> **\<ofrnxmr:xmr.mx\>** just something to think about. also, we will be branching soomTM, and getting i2p merged before that should be a priority, otherwise none of your i2p prs will hit release until fcmp     
    
> **\<ofrnxmr\>** we can come back to this, i'll leave comment on proposal if necessary     
    
> **\<ofrnxmr\>** (8 mins left)     
    
> **\<ofrnxmr\>** d. panagot12 Monero LWS Observatory — Public LWS Health https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/686     
    
> **\<slowbeardigger:matrix.org\>** ofrnxmr: https://github.com/panagot/Monero-LWS-Observatory not working, or down.     
    
> **\<slowbeardigger:matrix.org\>** maybe ping the person?     
    
> **\<ofrnxmr:xmr.mx\>** probably banned for being bot-like     
    
> **\<slowbeardigger:matrix.org\>** tons of AI sounding text too     
    
> **\<plowsof\>** https://github.com/panagot     
    
> **\<slowbeardigger:matrix.org\>** @slowbeardigger:matrix.org: not a bad thing, but the repo is down     
    
> **\<ofrnxmr:xmr.mx\>** i looked at the vercel deployment of this, and while it looks like a typical slop website, but does seem like a viable idea. similat to monero.fail and ditatompel, but yeah. idk if i like it.     
    
> **\<ofrnxmr:xmr.mx\>** will need to find out what happened to the repo before moving forward, in ant case     
    
> **\<ofrnxmr:xmr.mx\>** any*     
    
> **\<slowbeardigger:matrix.org\>** agreed     
    
> **\<ofrnxmr:xmr.mx\>** not foss = instaclose     
    
> **\<ofrnxmr\>** e. v1docq47 - monero konferenco 2026 voice-over and working on xmr.ru https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/683     
    
> **\<slowbeardigger:matrix.org\>** ofrnxmr: +1     
    
> **\<ofrnxmr:xmr.mx\>** i think id like to ask him if he's in a rush. if not, id like to wait to merge until  the more urgent proposals are funded     
    
> **\<ofrnxmr:xmr.mx\>** he had trouble getting funded once before, and it doesnt look great to have multiple proposals awaiting funding for extended periods of time     
    
> **\<ofrnxmr:xmr.mx\>** otherwise, im a +1 since he's been doing this for years and all-but-1 times, hes been funded     
    
> **\<ofrnxmr\>** f. r4v3r23 - ANONERO Continued development https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/671     
    
> **\<slowbeardigger:matrix.org\>** -1     
    
> **\<nioc\>** ofrnxmr agree re v1docq47     
    
> **\<nioc\>** *agree with your thoughts     
    
> **\<ofrnxmr:xmr.mx\>** i have not checked to see if the repo is accepting registrations, issues, or prs. i think it would be a lot more approachable if it was available for community members to contribute to     
    
> **\<slowbeardigger:matrix.org\>** in the last meeting there was an issue i believe, that there wasn’t all the code or some code open sourced?     
    
> **\<slowbeardigger:matrix.org\>** Correct me if i am wrong     
    
> **\<ofrnxmr:xmr.mx\>** the code is open source, but the repo registrations were closed, so users like plowsof could not open issues     
    
> **\<ofrnxmr:xmr.mx\>** which lead to an anonero-fork that had the issues fixed     
    
> **\<slowbeardigger:matrix.org\>** @ofrnxmr:xmr.mx: Thanks for the correction, this is a big turn off for me     
    
> **\<ofrnxmr:xmr.mx\>** (and also implemented the majority, or all, of the proposed  featured from the ccs, and then added a few on top)     
    
> **\<ofrnxmr:xmr.mx\>** the repo is on a tor-only self-hosted forgejo http://git.anonero5wmhraxqsvzq2ncgptq6gq45qoto6fnkfwughfl4gbt44swad.onion/ANONERO/ANONERO     
    
> **\<ofrnxmr:xmr.mx\>** id like to see: plowsof register on the instance, open issues, submit pr fixes, and those fixes be reviewed and merged (if valid)     
    
> **\<plowsof\>** the issues found on anonero are being raised upstream + getting fixed e.g. https://github.com/monero-project/monero/pull/10937/changes     
    
> **\<plowsof\>** they have since opened registration on their git but you reap what you sow , years being closed off - dev(s) who have issues with the project lead have come forward - compare to another monerujo fork, monfluo - even the name was community voted on and has surpassed anonero in features - and contributors, just missing the bc-ur cold signing     
    
> **\<ofrnxmr\>** and background sync*     
    
> **\<plowsof\>** apparently the features of anonero have been planned / decided already, i dont know where that took place     
    
> **\<slowbeardigger:matrix.org\>** ofrnxmr: -1, but feels like there is no people commenting here, or at least enough     
    
> **\<slowbeardigger:matrix.org\>** Should we leave the CCS for next week? idk     
    
> **\<ofrnxmr\>** yeah, just looking for something quickly     
    
> **\<ofrnxmr\>** cant find it. next time     
    
> **\<ofrnxmr\>** we can end the meeting here. thanks everyone for attending. Next meeting August 8 2026, same place     
    
> **\<plowsof\>** 👋 thanks     
    
> **\<slowbeardigger:matrix.org\>** ty     
    
> **\<slowbeardigger:matrix.org\>** take care yall     
    
> **\<DataHoarder\>** better highlight tbh plowsof, I used the Go scanning/code suite to find, get secret scalars, then make, prove, sign, and send a 1-in-2-out  (not using wallet rpc, just the monerod decoys endpoint + send raw tx) a CLSAG + BP+ transaction spending from the zero-key wallet and got some "free range" XMR :)     
    
> **\<DataHoarder\>** (this is what triggered sech1 to build the efficient scanner)     
    
> **\<ofrnxmr:xmr.mx\>** what i s"free range xmr"     
    
> **\<DataHoarder\>** XMR that appeared on known public seeds     
    
> **\<plowsof\>** the abb(ey)? wallet     
    
> **\<DataHoarder\>** yep, the zero-scalar secret spend key     
    
> **\<jpk68:matrix.org\>** Left a comment regarding bounty funding:     
    
> **\<jpk68:matrix.org\>** https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/689#note_36994     
    
> **\<sech1\>** The scanner is not 7 second, it's 8 seconds on RTX 5070 :D And I did it just to see how fast can it go, and to maybe implement GPU-accelerated wallet scanning for mobile GPUs (smartphones) - where it's needed the most.     

Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: nahuhh | 2026-07-24T18:05:04+00:00
- Closed at: 2026-08-07T22:52:05+00:00
