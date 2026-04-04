---
title: 'Monero Community Workgroup Meeting: Dec 20th 16:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1314
author: plowsof
assignees: []
labels: []
created_at: '2025-12-17T14:38:22+00:00'
updated_at: '2026-01-02T01:44:27+00:00'
type: issue
status: closed
closed_at: '2026-01-02T01:44:27+00:00'
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
    - Expect updates to the Spy Nodes [mrl-banlist](https://moneronet.info/) - see Ruckniums https://moneronet.info/ and discussion in https://github.com/monero-project/meta/issues/1310
    - Qubics "selfish mining under performed honest mining due to poor fork resolution and a conservative strategy. As many know, they never held a stable majority." [full paper](https://arxiv.org/abs/2512.01437) - via authors [X](https://x.com/iam_suhyeon) account
    - Blocksize Scaling discussions continue (see MRL meetings) - https://github.com/ArticMine/Monero-Documents
    - DataHoarder adds Bounties / CCS + more to https://blocks.p2pool.observer/payments
    - Tech. difficulties with the bounties bot, https://github.com/monerobot/monerobot/issues/12 and I've audited the address balances and found some discrepancies @ [bounties-mismatches](https://github.com/plowsof/check-monero-bounties-subad/blob/main/bounty-mismatches.csv) , HennyH is going to debug and fix the issues.
    - CCS slow to update funding amounts contributing to needless [overfunding](https://github.com/plowsof/scrape_ccs_fr)? the CCS _can_ be updated every minute. (Adding 'Unconfirmed balance' will require some dockerising and development/debug work - i've made a start on dockerising at least)
News: [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/) - [This Week In Monero](https://cyphergoat.com/this-week-in-monero) - [Monero Moon](https://www.themoneromoon.com/)    
4. [CCS updates](https://ccs.getmonero.org/)    
  a. [39C3 Support](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/622)    
  b. [Sneedlewoods-03_part-time_dev_work-Q1-26](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/634)
5. Workgroup reports    
  a. Dev workgroup
  b. Localization workgroup
  c. Outreach workgroup
  d. Events workgroup - [MoneroKon 2026](https://monerokon.org) - a venue for 2026 is still being discussed
  e. Website workgroup - redsh4de working on https://beta.monerodevs.org who posts regularupdates in [#monero-site](https://libera.monerologs.net/monero-site/20251216) 
  f. Policy workgroup
  g. Research workgroup https://github.com/monero-project/meta/issues/1313
  h. [FCMP++ Stressnet](https://github.com/seraphis-migration) https://stressnet.p2pool.observer/
    - "Ruckniums 1.4 release is using 107gb of ram compared to 1.5-prerelease using 14gb" via ofrnxmr
6. Open ideas time    
7. Confirm next meeting date/time    

[Previous meeting including logs](https://github.com/monero-project/meta/issues/1305)    

Meeting logs will be posted here afterwards.    


# Discussion History
## plowsof | 2026-01-02T01:44:08+00:00
Logs 
    
    
    
    
    
    
    
    
    
    
    
> **\<plowsof\>** meeting time https://github.com/monero-project/meta/issues/1314      
    
> **\<lm:matrix.baermail.fr\>** <lm:matrix.baermail.fr> 👋     
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> 👋     
    
> **\<michael\>** <michael> Hello.     
    
> **\<plowsof\>** greetings !     
    
> **\<ohchase:envs.net\>** <ohchase:envs.net> 👋     
    
> **\<plowsof\>** Ruckniums network scan tool : https://moneronet.info/  👀 boog900 shared in the last MRL meeting an update to the ban list @ https://github.com/Boog900/monero-ban-list/pull/10  meeting logs: https://github.com/monero-project/meta/issues/1310     
    
> **\<plowsof\>** how is site coming along redsh4de? 👋     
    
> **\<plowsof\>** https://beta.monerodevs.org/     
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> paragraphs incoming from me     
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> Soo, over the past 2 weeks, worked on adding three new pages to the website, some docs about how to add/modify/extend relevant content and use some utilities i made, and general improvements in various areas of the codebase - with a focus on making CSS more compact, weighing out a potential migration for SCSS due to it's support for nesting and general features that improve maintainability     
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> First, what's new since the last update     
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> 1. "What is Monero?" page at https://beta.monerodevs.org/get-started/what-is-monero/     
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> The design is meant to follow a sectioned pitch deck style that tells a kind of a story (problem -> solution -> use cases), with a call to action section leading the user to either download a wallet or purchase Monero.     
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> Thought it also fitting to add a Learn More section with Dr. Daniel Kim's presentation about Monero (with subtitle options), as i think it really covers most questions people might have about what Monero is and why it matters. As always, all text on the current page can be considered a placeholder and is only for presentation purposes     
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> https://mrelay.p2pool.observer/m/matrix.org/kseRprcJsuNGyedaoGcbYydP.png (image.png)     
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> 2. Exchanges page with eyecandy! https://beta.monerodevs.org/get-started/exchanges/     
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> Added a responsive exchanges page, with the options organized as such: Decentralized Exchanges, Aggregators, and CEXes - effectively sorted in a descending order by which ones are the most optimal for privacy.     
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> To avoid overwhelming users, made a filter sidebar/drawer to help newcomers quickly highlight the options that fit their situation - hopefully solving the common complaint that its difficult to buy Monero, which stems more from a bad presentation and discoverability of options rather than a lack of them[... more lines follow, see https://mrelay.p2pool.observer/e/joOFsNQKMWd6ajR3 ]     
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> Desktop view:     
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> https://mrelay.p2pool.observer/m/matrix.org/MUwFDEbGPOkakiNpYJoOBdUR.png (image.png)     
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> Mobile view:     
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> https://mrelay.p2pool.observer/m/matrix.org/AHrYnLgavROuzCKSRwwFQwNq.png (image.png)     
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> 3. Merchants at https://beta.monerodevs.org/get-started/merchants/     
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> List of merchant directories for now - four options listed as of today     
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> https://mrelay.p2pool.observer/m/matrix.org/gjzTcMzbvopdLfapYCLVlpdY.png (image.png)     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Looks good and loads real fast     
    
> **\<plowsof\>** nice progress redsh4de 💪images brought to us by the power of DataHoarders bridge.  proposals currently open for funding -> https://ccs.getmonero.org/funding-required/     
    
> **\<plowsof\>** has GUPAXX made the migration to the gupax-io repo? https://github.com/gupax-io/gupax     
    
> **\<lm:matrix.baermail.fr\>** <lm:matrix.baermail.fr> plowsof: Gupax.io is up,     
    
> **\<lm:matrix.baermail.fr\>** <lm:matrix.baermail.fr> Codebase is merged, but I want to finish some code refactor before releasing gupax v2     
    
> **\<plowsof\>** i can share a small update about my attempt at tweaking some things on the CCS backend after feedback. i should be able to put a testnet instance showing unconfirmed amounts next week     
    
> **\<nioc\>** meow     
    
> **\<plowsof\>** aot of small tweaks needed that prevented ccs from seeing pool transactions at all - hidden in the depths of php     
    
> **\<plowsof\>** other requests such as 'red banner to tell people that overfunding likely wont go to the proposer*) ... and a KISS "external funding" - where the FR page would just link people to an external fund raiser, this was requested a while ago, might not be so useful now but its a possibility      
    
> **\<plowsof\>** nice lm 💪 pumping the p2pool hashrate : https://blocks.p2pool.observer/pools     
    
> **\<lm:matrix.baermail.fr\>** <lm:matrix.baermail.fr> Very impressed @redsh4de:matrix.org !     
    
> **\<lm:matrix.baermail.fr\>** <lm:matrix.baermail.fr> Did you planned for localization support ?     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> @lm:matrix.baermail.fr: Yes     
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> planned? ;)     
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> already live     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Go check out the rtl arabic version     
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> https://beta.monerodevs.org/ar/     
    
> **\<plowsof\>** i hear the blockscaling wars may have ended?   "(see MRL meetings) - https://github.com/ArticMine/Monero-Documents "      
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Nope     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Our twitter friends are unhappy     
    
> **\<lm:matrix.baermail.fr\>** <lm:matrix.baermail.fr> I see it now, perfect !     
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> @lm:matrix.baermail.fr: wrote a lot of utilities to simplify localization for strings, more info about how it all works here: https://github.com/redsh4de/monero-site/blob/main/docs/how-to-add-localization-to-a-page.md     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> @ofrnxmr:xmr.mx: "After the recent backlash against a hard cap on the block size, it seems like the Monero developers have decided to cripple the scaling factors instead."     
    
> **\<plowsof\>** these monero developers sound really mean if true!     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Theyre racist bigots     
    
> **\<plowsof\>** so the people who are of the opinion that monero is going to be crippled are aware of the current technical limitations that put caps on sizes of certain things      
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> So you're a racist too? Noted.     
    
> **\<nioc\>** they were promised infinite block size      
    
> **\<plowsof\>** 😭     
    
> **\<plowsof\>** Noted and *ignored*     
    
> **\<nioc\>** website funding https://ccs.getmonero.org/proposals/redsh4de-getmonero-redesign.html     
    
> **\<nioc\>** general fund has donated      
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> nioc: Been spending a lot of time on the project, if anyone would like to support my work, do consider contributing <3     
    
> **\<plowsof\>** oh ' should the date displayed on the funding required page - be the date which it was put to funding ' to stop teitter from shaming us      
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> +1     
    
> **\<plowsof\>** its currently the date at which the porposer placed there to say 'i will begin from this date or intend to'     
    
> **\<nioc\>** put all the dates     
    
> **\<plowsof\>** yes     
    
> **\<plowsof\>** anything else anyone would like to mention?     
    
> **\<plowsof\>** News: [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/) - [This Week In Monero](https://cyphergoat.com/this-week-in-monero) (Oberver still on his 2nd break in 4 years)     
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> plowsof: in the list of proposals, i think the date shown must be the one on which the proposal went live     
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> same thing in the proposal view, with the proposal creation date being shown under it like a secondary item     
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> or in the body, like "Proposal created on XYZ"     
    
> **\<plowsof\>** yep , we can probably show all the dates clearly, and they can be ordered on the publish date - rather than the 'i intend to begin @' date      
    
> **\<plowsof\>** any feedback on the open ccs ideas?      
    
> **\<plowsof\>**   a. [39C3 Support](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/622)         
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> supporting a presence as 39C3 is very +EV imo, im for it. planning to visit the congress myself     
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> s/as/at     
    
> **\<plowsof\>**   b. [Sneedlewoods-03_part-time_dev_work-Q1-26](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/634)     
    
> **\<plowsof\>** has been brought up in no-wallet-left-behind meetings with positive feedback      
    
> **\<nioc\>** ++1     
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> +1     
    
> **\<plowsof\>** thanks for feedback. and speaking of events:     
    
> **\<plowsof\>**   d. Events workgroup - [MoneroKon 2026](https://monerokon.org) - a venue for 2026 is still being discussed     
    
> **\<plowsof\>** <lm:matrix.baermail.fr> 27-30 december is very close, is it an issue to have it funded after the event ? > <plowsof> a. [39C3 Support](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/622)     
    
> **\<plowsof\>** <ofrnxmr:xmr.mx> Usually ppl put the date as the current date that they opened entered the idea stage > <plowsof> yep , we can probably show all the dates clearly, and they can be ordered on the publish date - rather than the 'i intend to begin @' date     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> It should probably be changed to match the merge date     
    
> **\<plowsof\>** #monero-events to follow along i i hear the bitcoin film festival are open to sharing the venue in Warsaw      
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> can also maybe add extra fields for idea -> funding -> wip     
    
> **\<nioc\>** I believe questions were brought up last meeting about the 39C3 proposal.  Were they addressed?      
    
> **\<plowsof\>** most discussion happened here https://libera.monerologs.net/monero-community/20251122#c615861     
    
> **\<plowsof\>** if they are addresses people can give a thumbs up otherwise no     
    
> **\<plowsof\>** " although with C3 getting close, would be nice to get this approved or denied so we can know whether to go elsewhere for money if needed"     
    
> **\<plowsof\>** "that said, given the slow donations of current proposals in FR I don't foresee it getting funded quickly even if merged"     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> plowsof: this is my immediate thought     
    
> **\<lm:matrix.baermail.fr\>** <lm:matrix.baermail.fr> They could always sed 2025 2026 😐     
    
> **\<plowsof\>** any more feedbacks     
    
> **\<plowsof\>** because   h. [FCMP++ Stressnet](https://github.com/seraphis-migration) https://stressnet.p2pool.observer/     
    
> **\<plowsof\>**     - "Ruckniums 1.4 release is using 107gb of ram compared to 1.5-prerelease using 14gb" via ofrnxmr     
    
> **\<plowsof\>** and an upcoming monero core 18.4.5 release      
    
> **\<plowsof\>** 🥶     
    
> **\<lm:matrix.baermail.fr\>** <lm:matrix.baermail.fr> 🤧     
    
> **\<plowsof\>** this is the last meeting of 2025 give yourselves a pat on the back please     
    
> **\<plowsof\>** get well soon lm 🔥 🙌     
    
> **\<plowsof\>** any other business before i freeze, i'd like to put an open end here for humanitarian reasons and thank everyone for joining     
    
> **\<nioc\>** I have not seen any recent communication from the 39C3 proposal and doesn't seem like they are here today      
    
> **\<plowsof\>** pls continue      

Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: plowsof | 2025-12-17T14:38:22+00:00
- Closed at: 2026-01-02T01:44:27+00:00
