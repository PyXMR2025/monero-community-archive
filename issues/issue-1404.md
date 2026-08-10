---
title: 'Monero Community Workgroup Meeting: Sat, 2026-06-13 16:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1404
author: nahuhh
assignees: []
labels: []
created_at: '2026-06-13T07:49:35+00:00'
updated_at: '2026-08-07T22:46:58+00:00'
type: issue
status: closed
closed_at: '2026-08-07T22:46:58+00:00'
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
    - MoneroKon finished.  
    - [P2Pool critical upgrade **TODAY**](https://www.reddit.com/r/Monero/comments/1u1tt1p/psa_critical_p2pool_security_update/)! Download [here](https://github.com/SChernykh/p2pool/releases)  
4. CCS proposals  
  a. Koe - [Research and Development, hardfork](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/681)  
  b. [MRL] Dennis Trautwein - [ProbeLab P2P Network Metrics Proposal](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/667)    
  c. Marko Pohlo - [Cuprate Consensus-Rule Differential Fuzzing](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/676)    
  d. r4v3r23 - [ANONERO Continued development](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/671)  
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

[Previous meeting including logs](https://github.com/monero-project/meta/issues/1398)

# Discussion History
## michaesc | 2026-06-13T15:15:40+00:00
@nahuhh please correct the date of this ticket, as the title states Saturday and 14 June.

## nahuhh | 2026-06-13T18:54:32+00:00
Sorry about that. Done

## nahuhh | 2026-08-07T22:31:15+00:00
Logs 
    
> **\<ofrnxmr\>** Meeting time: https://github.com/monero-project/meta/issues/1404     
    
> **\<jpk68:matrix.org\>** Hello     
    
> **\<redsh4de:matrix.org\>** Hello     
    
> **\<msvb-lab\>** Hello.     
    
> **\<plowsof:matrix.org\>** hi     
    
> **\<ofrnxmr\>** Welcome     
    
> **\<ofrnxmr\>** 3. Community highlights     
    
> **\<moneromavrick:matrix.org\>** Yo     
    
> **\<ofrnxmr\>** Monerokon was last weekend. I heard it went well     
    
> **\<ofrnxmr\>** This weekend we have a critical p2pool update https://github.com/SChernykh/p2pool/releases     
    
> **\<DataHoarder\>** I keep monitoring updated and non-updated nodes to find any incidence of exploitation.     
    
> **\<hbs:matrix.org\>** (late) hello     
    
> **\<ofrnxmr\>** An explot was found in BasicSwapDEX (unrelated to monero swaps) which also had a critical release: https://github.com/basicswap/basicswap/releases/tag/v0.16.4     
    
> **\<ofrnxmr\>** Any other business / community highlights?     
    
> **\<ofrnxmr\>** Plugging the newsletters: [Revuo Monero](https://revuo-xmr.com/) &  [This week in Monero TWIM](https://cyphergoat.com/this-week-in-monero)     
    
> **\<ofrnxmr\>** If nothing else, lets move on to the CCS proposals     
    
> **\<ofrnxmr\>** 4. CCS proposals     
    
> **\<ofrnxmr\>** <4rkal> CypherGoat’s MoneroKon scavenger hunt wrapped up successfully in Warsaw, with $800 in prizes distributed. Hunt details: https://cyphergoat.com/monerokon2026 > <ofrnxmr> Any other business / community highlights?     
    
> **\<ofrnxmr\>** Nice     
    
> **\<ofrnxmr\>** a. Koe - [Research and Development, hardfork](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/681)     
    
> **\<jpk68:matrix.org\>** +1     
    
> **\<ofrnxmr\>** Koe came back a while ago and completed his prior ccs     
    
> **\<ofrnxmr\>** New one continues work on fcmp/carrot     
    
> **\<redsh4de:matrix.org\>** +1     
    
> **\<tobtoht\>** +1     
    
> **\<ofrnxmr:xmr.mx\>** +1     
    
> **\<ofrnxmr\>** b. Dennis Trautwein - [ProbeLab P2P Network Metrics Proposal](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/667)     
    
> **\<plowsof\>** i left a comment regarding rates https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/667#note_36602     
    
> **\<ofrnxmr\>** Aside from that, i believe MRL has given their blessing on the deliverables     
    
> **\<ofrnxmr\>** c. Marko Pohlo - [Cuprate Consensus-Rule Differential Fuzzing](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/676)     
    
> **\<jpk68:matrix.org\>** This proposal seems pretty interesting, however Cuprate devs have mentioned the timing isn't very opportune     
    
> **\<ofrnxmr:xmr.mx\>** i tend to agree with boogs comment, along the lines of "its too early for this"     
    
> **\<jpk68:matrix.org\>** IMO something like this would be really nice/useful eventually, for consensus and client diversity reasons     
    
> **\<ofrnxmr:xmr.mx\>** imo should revisit once cuprate is feature complete etc     
    
> **\<plowsof\>** in the meantime, a 2nd round for fuzzing monero core / fcmp++ remains unfunded here https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/667#note_36602     
    
> **\<plowsof\>** clipboard hijacked sorry     
    
> **\<plowsof\>** https://donate.magicgrants.org/monero/projects/fuzzing-monero-2     
    
> **\<jpk68:matrix.org\>** 100% in favour of this one ^     
    
> **\<plowsof\>** note  the price, 3 months for 3 devs, 50k, probelabs 1.5 person months 40k     
    
> **\<plowsof\>** unrelated but interesting none the less     
    
> **\<ofrnxmr:xmr.mx\>** 1/3 of the devs is the top contributrow to oss-fuzz as well     
    
> **\<ofrnxmr:xmr.mx\>** er. or "a" top, not "the"     
    
> **\<ofrnxmr:xmr.mx\>** anyway, my vote is close &  revisit later     
    
> **\<ofrnxmr:xmr.mx\>** anyone else? logs cant see emojis     
    
> **\<ofrnxmr\>** d. r4v3r23 - [ANONERO Continued development](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/671)     
    
> **\<ofrnxmr:xmr.mx\>** I intended to comment on this proposal directly, but never got around to it. i was in favor of the 1st and 2nd revisions (which were 12 and 6 months, respectively)     
    
> **\<ofrnxmr:xmr.mx\>** My concern is that the dev is not the proposer, and is a dev-for-hire, and limiting the timeframe leaves question about what happens after the 3 months?     
    
> **\<ofrnxmr:xmr.mx\>** for the initial anonero, and the 1.0 release, they both had different devs, and this is a third. the rate difference from 1.0 to this proposal is essentially a 4x increase (if we assume that this only lasts 3 months) -- and even a potential 4x increase from the initial version of the proposal     
    
> **\<ofrnxmr:xmr.mx\>** all things being equal (the same amount of hours on each revision, ie 40hrs/week for 3 months, 20hrs for 6 months, and 10hrs for 12 months) the dollar rate remains the same. but my main concern is "where will the dev be in 4-12 months?"     
    
> **\<ofrnxmr:xmr.mx\>** i prefer revision 1 and 2 for that reason. id be more comfortable knowing  that the project still has a dev to solve issues 10 months from now     
    
> **\<jpk68:matrix.org\>** I have the same concern, but I am tempted to be somewhat in support of this proposal overall. More development for Android wallets is good for the ecosystem     
    
> **\<jpk68:matrix.org\>** To be honest, I am pretty skeptical that this dev will stay for long, based on what's happened previously     
    
> **\<ofrnxmr:xmr.mx\>** @jpk68:matrix.org: to echo some of plowsofs initial feedback -- the wallet has undergone a major rewrite already, and is a different dev each time     
    
> **\<ofrnxmr:xmr.mx\>** so paying the dev for 3 months doesnt seem ideal. yes, wallet dev is good for ecosystem. but not having a dev is not     
    
> **\<ofrnxmr:xmr.mx\>** acx, for example, maintains monfluo for ~40xmr per year     
    
> **\<ofrnxmr:xmr.mx\>** anoneros rev. 1  proposal was 66xmr for the year     
    
> **\<ofrnxmr:xmr.mx\>** acx is available all year. anonero's dev is free to leave in 3 months     
    
> **\<ofrnxmr:xmr.mx\>** (after collecting a years pay)     
    
> **\<ofrnxmr:xmr.mx\>** anyway, thats the feedback that i planned to leave on the merge request. i'm in favor if its 6 or 12 months, but not 3 months     
    
> **\<plowsof\>** double the asking amount then? or are we literally forcing a dev to work less / week?     
    
> **\<plowsof\>** where will they be in 13 months     
    
> **\<ofrnxmr:xmr.mx\>** the initial revision was 66xmr per year     
    
> **\<ofrnxmr:xmr.mx\>** then was 66 per 6 months, now is 109 for 3 months     
    
> **\<plowsof\>** priced in fiat and the $  value moved. iirc it was 69 xmr     
    
> **\<plowsof\>** +10% buffer     
    
> **\<ofrnxmr:xmr.mx\>** yeah, i know fiat adjusted the number, but it still changed from 69 to 88 w/o fiat jump     
    
> **\<ofrnxmr:xmr.mx\>** dev rates went from 45 to 60/hr     
    
> **\<plowsof\>** 69.9*     
    
> **\<ofrnxmr:xmr.mx\>** :P mr specific     
    
> **\<ofrnxmr:xmr.mx\>** if other have no issue, then thats fine. just leaving my feedback that id prefer the proposal undo the latest change     
    
> **\<plowsof\>** whats a +15$ an hour raise between friends     
    
> **\<ofrnxmr:xmr.mx\>** it was said that the rate changed because the dev is working full time now and needs 33% more for that.     
    
> **\<ofrnxmr:xmr.mx\>** id prefer part time w/ longer availability, is my position     
    
> **\<ofrnxmr:xmr.mx\>** im not counting the dollars, my main concern is that the wallet will be unmaintained in 3.1 months     
    
> **\<ofrnxmr:xmr.mx\>** from the looks of the repo, after 1.0 release 9 months ago, there have only been 8 commits http://git.anonero5wmhraxqsvzq2ncgptq6gq45qoto6fnkfwughfl4gbt44swad.onion/ANONERO/ANONERO/compare/v1.0.0...v1.0.1     
    
> **\<plowsof\>** Monerujo feeling nervous rn     
    
> **\<ofrnxmr:xmr.mx\>** (so the other dev worked out their contract and left, it seems). == i prefer longer part-time contract vs shorter full-time     
    
> **\<ofrnxmr:xmr.mx\>** anyway, enough of my rambling     
    
> **\<ofrnxmr:xmr.mx\>** thats the final CCS on the agenda today.     
    
> **\<ofrnxmr:xmr.mx\>** again, big reminder to update your p2pool https://github.com/SChernykh/p2pool/releases, and to share with everybody cc @  @moneromavrick:matrix.org     
    
> **\<plowsof\>** the dev is sending patches to raver @ 40 hours a week (can you imagine?) - they should probably make pull requests instead. on that note , the codeberg for bridge that jpk68 was using, should be switched over to becoming a github app + webhooks to hopefully avoid being nuked     
    
> **\<ofrnxmr:xmr.mx\>** nuking seems related to sending PRs to p2pool     
    
> **\<plowsof\>** @tomdooley brainchainz !     
    
> **\<plowsof\>** lol yes, avoiding p2pool also     
    
> **\<ofrnxmr:xmr.mx\>** Next meeting Sat June 27, 2026, 1600 UTC     
    
> **\<ofrnxmr:xmr.mx\>** Thanks everyone for attending     
    
> **\<plowsof\>** thanks for hosting 👍     
    
> **\<ofrnxmr:xmr.mx\>** please leave feedback on the open proposals, either thumbs up/down or comment     
    
> **\<michael\>** Good meeting, dankon.     
    
> **\<plowsof\>** <r4v3r23> you know how easy it is to apply patches? > <plowsof> the dev is sending patches to raver @ 40 hours a week (can you imagine?) - they should probably make pull requests instead. on that note , the codeberg for bridge that jpk68 was using, should be switched over to becoming a github app + webhooks to hopefully avoid being nuked     
    
> **\<@ofrnxmr:xmr.mx\>** <r4v3r23> you guys are confusing being maintained/supported with the work thats being done > <@ofrnxmr:xmr.mx> im not counting the dollars, my main concern is that the wallet will be unmaintained in 3.1 months     
    
> **\<r4v3r23\>** the wallet has always been maintained and supported from the very first release     
    
> **\<plowsof\>** would you not prefer him to make pull requests?     
    
> **\<r4v3r23\>** plowsof: its a non issue. he could easily do that     
    
> **\<r4v3r23\>** same as applying patches. the only difference is what account it would be under     
    
> **\<@ofrnxmr:xmr.mx\>** <r4v3r23> > <@ofrnxmr:xmr.mx> My concern is that the dev is not the proposer, and is a dev-for-hire, and limiting the timeframe leaves question about what happens after the 3 months?     
    
> **\<r4v3r23\>** ill say this: ive never been more confident in the future of the project than now. this dev is reliable, professional, iterates fast and is always available. that said, this round of work is essentially to bring ANONERO to "feature complete/stable" status - this isnt a project that needs constant CCSs for low level maintence/dev work     
    
> **\<r4v3r23\>** there is 0 risk of the wallet being unmaintained after 3 months, just like it was never unmaintained at any point in the wallets history     
    
> **\<r4v3r23\>** since 3 months was brought up at first meeting, thats now the proposal, and literally the only thing holding up the work is the funding. all the features are designed and ready for implementation     
    
> **\<r4v3r23\>** ANONERO will be maintained and supported indefinitely. this CCS is to finally bring advanced stealth features and give it the fresh UI it deserves     
    
> **\<plowsof\>** any design examples of the new ui?     
    
> **\<r4v3r23\>** "Any unclaimed milestones after 3 months can have funds allocated to FCMP++ work." - this alone should speak to how confident i am in this proposal     
    
> **\<plowsof\>** "CCS will expire one year from date of first payout and funds can be send to the General Fund." you are now 4x more confident, nice to see, promising     
    
> **\<r4v3r23\>** plowsof: correct     
    
> **\<r4v3r23\>** this is an independent project that respect user privacy and has innovated more than any other mobile wallet. benefit of the doubt wouldnt hurt     
    
> **\<plowsof\>** do any other wallets in the ecosystem function on patches? it seems really unique, i would definitely consider moving to pull requests     
    
> **\<r4v3r23\>** plowsof: the patches was just so that the code is "owned" by the ANONERO user/project     
    
> **\<r4v3r23\>** literally instead of dev doing git push, its git patch and send     
    
> **\<r4v3r23\>** its the exact same thing     
    
> **\<r4v3r23\>** if its a deal breaker, than dev can just push commits...     
    
> **\<r4v3r23\>** the 3 month proposal is the best way to guarantee the delivery timing, and ensure future support. the "continued support" part of the CCS isnt limited to 3 months (it was there in the original proposal), the time line is strictly for the feature milestones     
    
> **\<@ofrnxmr:xmr.mx\>** <r4v3r23> a wallet needs constant commits to be maintained....? > <@ofrnxmr:xmr.mx> from the looks of the repo, after 1.0 release 9 months ago, there have only been 8 commits http://git.anonero5wmhraxqsvzq2ncgptq6gq45qoto6fnkfwughfl4gbt44swad.onion/ANONERO/ANONERO/compare/v1.0.0...v1.0.1     
    
> **\<r4v3r23\>** you realize the entire point of the 1.0 rewrite is to be stable and NOT need so many updates?     
    
> **\<r4v3r23\>** feathers last release was in April 2025 - are you gonna accuse feather also of being unmaintained?     
    
> **\<r4v3r23\>** or would you rather ANONERO create busy work to justify constant 3 month proposals?     
    
> **\<r4v3r23\>** the goal is a solid, stable, feature complete wallet that needs minimum maintanence     
    
> **\<r4v3r23\>** btw, ANONERO (with new dev) was the first wallet to update to v0.18.5     
    
> **\<r4v3r23\>** so unless there are any real objections, lets get this to funding     

Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: nahuhh | 2026-06-13T07:49:35+00:00
- Closed at: 2026-08-07T22:46:58+00:00
