---
title: 'Monero Community Workgroup Meeting: Sat, 2026-06-27 16:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1411
author: nahuhh
assignees: []
labels: []
created_at: '2026-06-27T11:20:56+00:00'
updated_at: '2026-08-07T22:47:05+00:00'
type: issue
status: closed
closed_at: '2026-08-07T22:47:05+00:00'
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
    - [MoneroKon Planning Meeting today @ 17:00 UTC](https://github.com/monero-project/meta/issues/1406) - Vote on venue.  
4. CCS proposals  
  a. Koe - [Research and Development, hardfork](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/681)  
  b. [MRL] Dennis Trautwein - [ProbeLab P2P Network Metrics Proposal](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/667)    
  c. Marko Pohlo - [Cuprate Consensus-Rule Differential Fuzzing](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/676)    
  d. v1docq47 - [monero konferenco 2026 voice-over and working on xmr.ru](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/683)  
  e. r4v3r23 - [ANONERO Continued development](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/671)  
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

[Previous meeting including logs](https://github.com/monero-project/meta/issues/1404)

# Discussion History
## nahuhh | 2026-08-07T22:46:02+00:00
Logs 
    
> **\<ofrnxmr\>** Meeting time. https://github.com/monero-project/meta/issues/1411     
    
> **\<ofrnxmr\>** Greetings     
    
> **\<user2570:unredacted.org\>** hello     
    
> **\<parasew:matrix.org\>** hi!     
    
> **\<sneedlewoods_xmr:matrix.org\>** alo     
    
> **\<ofrnxmr\>** Good morning everyone. I forgot to bring donuts     
    
> **\<plowsof\>** hi     
    
> **\<ofrnxmr\>** 3. Community highlights     
    
> **\<michael\>** Hello.     
    
> **\<sneedlewoods_xmr:matrix.org\>** @ofrnxmr: I'd like to say thanks to tobtoht, selsta, plowsof and everyone else who helped to reduce the open PR count from (IIRC well above) 300 to ~270     
    
> **\<ofrnxmr\>** I'm working on increasing that count 🙏, jk     
    
> **\<ofrnxmr\>** +1, but also nice that there are a number of new contributors fixing some long-standing issues     
    
> **\<selsta\>** still lots of work to with older issues / PRs     
    
> **\<ofrnxmr\>** Following this meeting, there is a MoneroKon Planning Meeting today @ 17:00 UTC (shttps://github.com/monero-project/meta/issues/1406). They will hold a vote on venue     
    
> **\<plowsof\>** sgp_ announced Skylight will be adding (in an upcoming release)  " support [for] non-lightweight Monero wallets as well (node + sync). Ty vtnerd for making it easy to support both"     
    
> **\<ofrnxmr\>** seems matrix swallowed the hyperlink to monerokon agenda? https://github.com/monero-project/meta/issues/1406     
    
> **\<ofrnxmr\>** Not monero related, but cyphergoat.com (by @4rkal:monero.social ) noted that binance is delisting europe     
    
> **\<parasew:matrix.org\>** @ofrnxmr: this is unconfirmed, and they can still get their mica licence via another country than greece     
    
> **\<ofrnxmr\>** They sent out emails to some users. A user here confirmed (shared their email screenshot)     
    
> **\<plowsof:matrix.org\>** ANONERO finally opened their forgejo (tor only) instance to manual registrations 💪     
    
> **\<ofrnxmr\>** Revuo seems to have joined monero observer on a vacation. https://cyphergoat.com/this-week-in-monero is still pumpibg out weekly issues     
    
> **\<hbs:matrix.org\>** Hello (late again...)     
    
> **\<ofrnxmr\>** if no further community highlights, we can move on to the proposals. Will try to ensure we finish early so interested parties have time to make it over to MK'27 meeting     
    
> **\<ofrnxmr\>** 4. CCS proposals     
    
> **\<ofrnxmr\>** a. Koe - Research and Development, hardfork (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/681)     
    
> **\<ofrnxmr:xmr.mx\>** +1     
    
> **\<sneedlewoods_xmr:matrix.org\>** +1     
    
> **\<ofrnxmr\>** b. [MRL] Dennis Trautwein - ProbeLab P2P Network Metrics Proposal (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/667)     
    
> **\<ofrnxmr\>** MRL ack'd the general idea, but there are some unaddressed comments since the last meeting     
    
> **\<ofrnxmr\>** c. Marko Pohlo - Cuprate Consensus-Rule Differential Fuzzing (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/676)     
    
> **\<ofrnxmr:xmr.mx\>** my take on the cuprate fuzzing proposal is that it is too early for this proposal, and should be revisited when cuprate matures     
    
> **\<ofrnxmr:xmr.mx\>** my vote is to close this one     
    
> **\<nioc\>** +1 for koe     
    
> **\<ofrnxmr\>** Thanks n1oc2     
    
> **\<nioc\>** as for Marko Pohlo I defer to boog     
    
> **\<ofrnxmr:xmr.mx\>** i think (need to scroll up) that boog liked my comment about closing until maturity at the prior meeting     
    
> **\<ofrnxmr:xmr.mx\>** https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/676#note_36585 << boogs comment     
    
> **\<@ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> boog liked this comment https://libera.monerologs.net/monero-community/20260613#c684779 nioc > <@ofrnxmr:xmr.mx> imo should revisit once cuprate is feature complete etc     
    
> **\<nioc\>** speaking of which..... https://ccs.getmonero.org/funding-required/     
    
> **\<ofrnxmr\>** speaking of monerkon. The 2026 monerkon videos are available on youtube     
    
> **\<nioc\>** 1 of which is for a cuprate dev and the CCS work is being done by someone working on cuprate without compensation     
    
> **\<ofrnxmr\>** Monerokon*     
    
> **\<ofrnxmr:xmr.mx\>** looks like jberrman is overfunded     
    
> **\<plowsof:matrix.org\>** https://ccs.getmonero.org/funding-required/     
    
> **\<plowsof:matrix.org\>** thnx nioc, failed to quote     
    
> **\<ofrnxmr\>** d. v1docq47 - monero konferenco 2026 voice-over and working on xmr.ru (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/683)     
    
> **\<ofrnxmr\>** Proposal is relatively new, but its a regular proposer and proposal. Has been doing this work for years     
    
> **\<plowsof:matrix.org\>** ill drop it in #xmr.ru:matrix.org with my universal " 👋 🫵 🤏 ⏲️? 😊   👍️ 👎️ ->  https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/683 "     
    
> **\<ofrnxmr\>** raver wont be here for the last proposal on the agenda > e. r4v3r23 - ANONERO Continued development (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/671)     
    
> **\<@ofrnxmr\>** <sneedlewoods_xmr:matrix.org> (I think Yiannis Psarras from ProbeLab had a good talk: "Mapping Spy Node Dominance in the Monero P2P Network") > <@ofrnxmr> speaking of monerkon. The 2026 monerkon videos are available on youtube     
    
> **\<ofrnxmr:xmr.mx\>** https://www.youtube.com/watch?v=luLy5-56blM     
    
> **\<ofrnxmr:xmr.mx\>** https://www.youtube.com/@MoneroCommunityWorkgroup     
    
> **\<ofrnxmr\>** If theres nothing else, we can end the meeting here.     
    
> **\<sneedlewoods_xmr:matrix.org\>** thanks everyone     
    
> **\<ofrnxmr\>** Next meeting in 2 weeks. Saturday July 11 @ 1600 UTC     
    
> **\<plowsof:matrix.org\>** thanks ofrnxmr , lurkers and none lurkers 👋     
    
> **\<michael\>** Good meeting, dankon.     

Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: nahuhh | 2026-06-27T11:20:56+00:00
- Closed at: 2026-08-07T22:47:05+00:00
