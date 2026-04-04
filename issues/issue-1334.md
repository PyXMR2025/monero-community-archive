---
title: 'Monero Community Workgroup Meeting: Jan 31st 16:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1334
author: plowsof
assignees: []
labels: []
created_at: '2026-01-31T11:24:42+00:00'
updated_at: '2026-03-25T09:48:53+00:00'
type: issue
status: closed
closed_at: '2026-03-25T09:48:53+00:00'
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
    - not shared at the meeting TODO https://github.com/monero-project/meta/issues/1326
    - RandomX v2 https://github.com/tevador/RandomX/pull/317
News: [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/) - [This Week In Monero](https://cyphergoat.com/this-week-in-monero) - [Monero Moon](https://www.themoneromoon.com/)    
4. [CCS updates](https://ccs.getmonero.org/)    
  a. [39C3 Support](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/622)    
  b. [Open-source Monero browser extension wallet](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/636)    
  c. [Monero News App and Monero Magazine: Build a Community Media Platform for Monero](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/639)    
5. Workgroup reports    
  a. Dev workgroup
  b. Localization workgroup
  c. Outreach workgroup
  d. Events workgroup 
  e. Website workgroup
  f. Policy workgroup
  g. Research workgroup
  h. [FCMP++ Stressnet](https://github.com/seraphis-migration)
6. Open ideas time    
7. Confirm next meeting date/time    

[Previous meeting including logs](https://github.com/monero-project/meta/issues/1323)    

Meeting logs will be posted here afterwards.    

# Discussion History
## plowsof | 2026-03-25T09:48:48+00:00
Logs 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
> **\<plowsof\>** meeting time https://github.com/monero-project/meta/issues/1334     
    
> **\<hbs:matrix.org\>** <hbs:matrix.org> hello     
    
> **\<plowsof\>** sorry for being late , greetings     
    
> **\<syntheticbird\>** <syntheticbird> hello     
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> hello     
    
> **\<plowsof\>** a message from our cuprate sponsors: boog900's recent CCS update https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/611#note_33930 and hintos https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/591#note_34171     
    
> **\<plowsof\>** hbs also shared a progress update / completion, can discuss that now also      
    
> **\<plowsof\>** alot of progress with -sites weblate now redsh4de , translations finally      
    
> **\<plowsof\>** Electrum wallets coming to basicswapDeX soon ofrnxmr      
    
> **\<ofrnxmr\>** <ofrnxmr> Not soonTM anymore     
    
> **\<ofrnxmr\>** <ofrnxmr> Up and running afaik just a single bug left before it can be merged     
    
> **\<plowsof\>** Ruckniums ASN map of spy nodes and more https://moneronet.info/     
    
> **\<plowsof\>** nice     
    
> **\<ofrnxmr\>** <ofrnxmr> (bug if failing swap due to fee too low to be relayed)     
    
> **\<plowsof\>** DataHoarder has been working 24/7 responding to OVK questions for whats seems like just another day after day      
    
> **\<ofrnxmr\>** <ofrnxmr> Only happens on electrum, server rejects too low fee rate. Small bug but it causes swaps to fail occasionally so obv needs to be fixed before release     
    
> **\<DataHoarder\>** night after night*     
    
> **\<ofrnxmr\>** <ofrnxmr> Nono, only 21/7     
    
> **\<ofrnxmr\>** <ofrnxmr> The other 3 are harassing ai slop artists     
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> Website updates from me: Pretty much feature complete now, so what i have been working on have been mainly developer UX improvements.     
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> Two biggest changes:     
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> * introducing native CSS nesting for better readability: https://caniuse.com/css-nesting[... more lines follow, see https://mrelay.p2pool.observer/e/4pXD8uEKTk8zYjRo ]     
    
> **\<plowsof\>** would be good to see the footprint of an actual light client of basicswapdex, monero, wownero, btc, ltc using remote/electrum.. when bch electrum D:      
    
> **\<DataHoarder\>** but mostly been testing RandomX v2 on exotic devices, with my own go-randomx (and got the prefetch tweak on v2!)     
    
> **\<plowsof\>** 💪     
    
> **\<ofrnxmr\>** <ofrnxmr> plowsof: About 3gb if wownero is also remote node     
    
> **\<syntheticbird\>** <syntheticbird> @redsh4de:matrix.org: CSS nesting     
    
> **\<syntheticbird\>** <syntheticbird> we needed it for so long     
    
> **\<syntheticbird\>** <syntheticbird> I'm so glad this has been standardized everywhere     
    
> **\<plowsof\>** ccs nesting 👁️     
    
> **\<michael\>** <michael> Oops late, hello saluton.     
    
> **\<plowsof\>** i mean css nesting 😠     
    
> **\<syntheticbird\>** <syntheticbird> plowsof: new exploit just dropped     
    
> **\<plowsof\>** lol     
    
> **\<plowsof\>** hello michael i was 5 blocks late, no worries     
    
> **\<plowsof\>** DataHoarder have bitmain bothered to read the release notes are still checking their email inbox xD     
    
> **\<DataHoarder\>** no idea     
    
> **\<plowsof\>** or are they*     
    
> **\<DataHoarder\>** there were no further updates on that in #monero-pow so maybe ask hyc     
    
> **\<plowsof\>** thanks     
    
> **\<plowsof\>** roight     
    
> **\<plowsof\>** can share the CCS ideas unless anything else to bring up     
    
> **\<DataHoarder\>** RandomX V2 initial support was added into xmrig dev branch too, which can be used for benchmarks on devices with fun NUMA localities https://github.com/xmrig/xmrig/pull/3769 (xmrig --bench=1M --algo=rx/v2).      
    
> **\<DataHoarder\>** The current RandomX V2 changes are "finalized" see a description on https://github.com/SChernykh/RandomX/blob/v2/doc/design_v2.md  (+ commitments, but these already exist in code)     
    
> **\<DataHoarder\>** and ofc, the main PR for it on the repo https://github.com/tevador/RandomX/pull/317     
    
> **\<plowsof\>** nice sech1, and thx for the invaluable testing DH     
    
> **\<DataHoarder\>** I have effectively "burned" two 128G LRDIMM DDR4 sticks @ 3200MHz while doing so ... one got replaced, other is a loss     
    
> **\<plowsof\>** :(     
    
> **\<DataHoarder\>** (I used randomx as memory stress test)     
    
> **\<DataHoarder\>** I have nothing else on that, but if you want to submit benchmarks see https://gist.github.com/SChernykh/6058ecf01c929883b9d19c7eeadc8809     
    
> **\<plowsof\>** 👍     
    
> **\<DataHoarder\>** or you can drop by #monero-pow with your benchmarks as well     
    
> **\<DataHoarder\>** if you have EPYC/Threadripper machines use xmrig, as otherwise NUMA locality is not taken into account     
    
> **\<plowsof\>** active news letter [This Week In Monero](https://cyphergoat.com/this-week-in-monero)     
    
> **\<plowsof\>**   a. [39C3 Support](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/622)         
    
> **\<plowsof\>** no updates for this afaict      
    
> **\<plowsof\>** can circle back if necessary      
    
> **\<plowsof\>**   b. [Open-source Monero browser extension wallet](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/636)         
    
> **\<plowsof\>** Expiration date would be: February 7th, 2026     
    
> **\<plowsof\>** has not responded to a comment to share previous work     
    
> **\<plowsof\>** maybe spirobel could comment when they see it     
    
> **\<nioc\>** is that expiration date for funding or completion?      
    
> **\<plowsof\>** i vote for it to be closure      
    
> **\<plowsof\>** date     
    
> **\<nioc\>** oh wait, I thought that was for spirobel  o_0     
    
> **\<plowsof\>** ah sorry for the confusion     
    
> **\<nioc\>** me too  lol     
    
> **\<plowsof\>** not spirobels proposal     
    
> **\<plowsof\>** another proposal not showing on the ideas page or i notes: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/638     
    
> **\<plowsof\>** from Ciphernerd     
    
> **\<plowsof\>** close immediately!     
    
> **\<plowsof\>** the website , a wordpress page, leads to https://ciphernerd-com.l.ink/ now      
    
> **\<ofrnxmr\>** <ofrnxmr> Left my feedback on the proposal     
    
> **\<plowsof\>** there are open source news letter blog things people can pick up e.g. Revuo      
    
> **\<plowsof\>** this is low effort with zero prev contributions , close     
    
> **\<plowsof\>** monero_magazine here?     
    
> **\<plowsof\>** thanks for feedback ofrnxmr      
    
> **\<plowsof\>** and those who have up/down dooted on gitlab     
    
> **\<plowsof\>**   c. [Monero News App and Monero Magazine: Build a Community Media Platform for Monero](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/639)         
    
> **\<plowsof\>** has comments and was also shared on matrix/irc      
    
> **\<ofrnxmr\>** <ofrnxmr> Some of the initial nits are things like referring to stealthex as a dex and no kyc     
    
> **\<ofrnxmr\>** <ofrnxmr> Which are real basic falsehoods or hallucinations     
    
> **\<plowsof\>** red flag when the proposer is claiming to be from the community, and collaborating with devs      
    
> **\<ofrnxmr\>** <ofrnxmr> And yet nobody knows em     
    
> **\<syntheticbird\>** <syntheticbird> plowsof: lmao     
    
> **\<syntheticbird\>** <syntheticbird> "My CCS has been approved by Monero CEO"     
    
> **\<plowsof\>** videos of flicking through magazines should not 'wow' you, anyone can go to a 'create a magazine' and ctrl+v a buncha stuff and get it to your door / act as a proxy seller     
    
> **\<ofrnxmr\>** <ofrnxmr> I still (from long ago) believe that magazines should strive to be self-sufficient     
    
> **\<plowsof\>** they are followed by beldex on twitter 💪     
    
> **\<ofrnxmr\>** <ofrnxmr> Beldex would probably fund them if asked 🤷‍♂️     
    
> **\<plowsof\>** yeah     
    
> **\<ofrnxmr\>** <ofrnxmr> Better a beldex ad placement than spreading falsehoods about swappers being dexes     
    
> **\<plowsof\>** https://x.com/Monero_Magazine/verified_followers     
    
> **\<plowsof\>** merge?     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> nay     
    
> **\<plowsof\>** any other business? 👀     
    
> **\<plowsof\>** syntheticbird the CEO of monero has found a wallet which i am a benifactor of, they contacted me on discord about it     
    
> **\<hbs:matrix.org\>** <hbs:matrix.org> do you mind sharing the OVK for that wallet?     
    
> **\<syntheticbird\>** <syntheticbird> I mind     
    
> **\<plowsof\>** its a legacy one i never upgraded because post quantum is a myth i tells ya     
    
> **\<syntheticbird\>** <syntheticbird> This is one step towards the total deanonymization of Monero and the destruction of the cryptocurrency landscape as we know it     
    
> **\<syntheticbird\>** <syntheticbird> # /s     
    
> **\<plowsof\>**  hbs' update and ccs completed  https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/597#note_34183     
    
> **\<hbs:matrix.org\>** <hbs:matrix.org> Available to answer questions     
    
> **\<plowsof\>** <spirobel:kernal.eu> can we just close bs like this. they didnt even take the time to engage in "vibe coding" or plagiarism  > <plowsof> maybe spirobel could comment when they see it     
    
> **\<spirobel:kernal.eu\>** <spirobel:kernal.eu> https://mrelay.p2pool.observer/m/kernal.eu/jkIiktbeWqYNUCjViXzpjKZK.png (image.png)     
    
> **\<plowsof\>** 👍     
    
> **\<plowsof\>** feel bad for wasting peoples times linking to those proposal ideas, sorry      
    
> **\<spirobel:kernal.eu\>** <spirobel:kernal.eu> https://github.com/Waterboard-Subject2?tab=following  https://github.com/fatassbunny https://github.com/surprise     
    
> **\<spirobel:kernal.eu\>** <spirobel:kernal.eu> https://github.com/Coopyy     
    
> **\<plowsof\>** hbs you also have a dedicated room which people can follow up in and receive hands on support while testing thing     
    
> **\<spirobel:kernal.eu\>** <spirobel:kernal.eu> look at followers and following      
    
> **\<spirobel:kernal.eu\>** <spirobel:kernal.eu> https://github.com/ClairvoyantSolutions     
    
> **\<plowsof\>** 😆     
    
> **\<plowsof\>** i hear it has raving reviews on a monero forum somehwere     
    
> **\<plowsof\>** thinks for looking further into this spirobel     
    
> **\<plowsof\>** <hbs:matrix.org> yep, happy to interact there as well > <plowsof> hbs you also have a dedicated room which people can follow up in and receive hands on support while testing thing     
    
> **\<nioc\>** the MoneroSwap room by hbs  #moneroswap:matrix.org     
    
> **\<plowsof\>** thanks nioc, matrix isnt wanting to load right now      
    
> **\<nioc\>** IRC seems fine      
    
> **\<plowsof\>** always     
    
> **\<nioc\>** ( ͡° ͜ʖ ͡°)     
    
> **\<plowsof\>** will link prev MRL meetings for the OVK discussions soon     
    
> **\<michael\>** <michael> Good meeting and moderation, thanks everyone and dankon.     
    
> **\<plowsof\>** thanks all for attending !     
    
> **\<hbs:matrix.org\>** <hbs:matrix.org> Thanks all, have a nice week-end     
    
> **\<monero_magazine:matrix.org\>** <monero_magazine:matrix.org> Thank you for taking the time to review my application. I understand the rejection.     
    
> **\<monero_magazine:matrix.org\>** <monero_magazine:matrix.org> Polwsof, I would like to tell you that it's not very nice to be spat on as if I did nothing, and on my work and even my past work. I understand being rejected, but I would appreciate a little respect for my work. I am trying to build something here. We are not machines. Try to say things with a little more tact. I think it is your aversion to AI that has made you a little tense towards me.     
    
> **\<monero_magazine:matrix.org\>** <monero_magazine:matrix.org> In any case, I'll stay alert to what's going on here. I didn't know the group. Have a good evening, everyone 🙂     
    
> **\<plowsof\>** glad you found the room after 6 years it's never too late to get involved      
    
> **\<plowsof\>** when you prompt LLM for responses you gotta provide full context      
    
> **\<plowsof\>** and plowsof is dead inside and highly resistant to appeals to emotional from LLM models trained up until mid 2025     
    
> **\<plowsof\>** happy monday everyone, lets get working      

Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: plowsof | 2026-01-31T11:24:42+00:00
- Closed at: 2026-03-25T09:48:53+00:00
