---
title: 'Monero Community Workgroup Meeting: Sep 20th 16:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1271
author: plowsof
assignees: []
labels: []
created_at: '2025-09-20T10:47:30+00:00'
updated_at: '2025-11-05T10:12:10+00:00'
type: issue
status: closed
closed_at: '2025-11-05T10:12:10+00:00'
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
    - https://github.com/monero-project/meta/issues/1268
    - https://github.com/monero-project/monero-site/issues/2535 (contains links to related resources / PR's and further research)
News: [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/) - [This week in Monero](https://cyphergoat.com/blog)
4. [CCS updates](https://ccs.getmonero.org/)    
  a. [MoneroOS Resurrection](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/596)    
  b. [[hbs] EVM Atomic Swaps](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/597)    
  c. [Monero Python Maintenance](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/598)    
  d. [v1docq47 - monero konferenco 2025 voice-over and working on xmr.ru](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/607)    
  e. [Revuo Monero Maintenance (2025 Q4)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/610)    
  f. [Boog900 full time work on Cuprate (3 months)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/611)    
5. Workgroup reports    
  a. Dev workgroup
  b. Localization workgroup
  c. Outreach workgroup
  d. Events workgroup - [MoneroKon 2026](https://MoneroKon.org/)
  e. Website workgroup
  f. Policy workgroup
  g. Research workgroup
  h. [Seraphis Migration workgroup](https://github.com/seraphis-migration)
6. Open ideas time    
7. Confirm next meeting date/time    

[Previous meeting including logs](https://github.com/monero-project/meta/issues/1264)    

Meeting logs will be posted here afterwards.    

# Discussion History
## plowsof | 2025-11-05T10:11:39+00:00
Logs 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

## plowsof | 2025-11-05T10:12:05+00:00
Logs 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> meeting time https://github.com/monero-project/meta/issues/1271      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> greetings     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> we had the 18 block re-org  but then a 10 block re-org , some links here https://github.com/monero-project/monero-site/issues/2535      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> and TradeOgres seizure https://rcmp.ca/en/news/2025/09/rcmp-executes-record-seizure-more-56-million-dollars-cryptocurrency      
    
> **\<nioc\>** RCMP thinks the operator is from the US and died recently. The servers were in Canada     
    
> **\<nioc\>** pumpxmr waves     
    
> **\<Cindy\>** hi     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> hello, Datahoarder and ofrnxmr are doing things. should people be running https://github.com/nahuhh/monero/tree/dns_testpoints-public on testnet?      
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Not too many :P theres a bug that needs fixing     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> anyone can run it though, but we might break their nodes temporarily while testing selfish mining     
    
> **\<Cindy\>** is this compatible with the checkpoint system in older versions of monerod?     
    
> **\<DataHoarder\>** it is, just adds more records , does 2/3rd+1 consensus and reduces the check interval     
    
> **\<DataHoarder\>** previously it did 50%+1     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> Development of a Book on a Finality Layer     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org>  has moved to funding https://ccs.getmonero.org/funding-required/      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> hbs EVM atomic swaps gui is in line to be moved to funding https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/597      
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> DataHoarder: Also old versions only chrck hourly, and only check 4 domains     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> and i closed a proposal which was AI slop to save everyones time. then i had an interesting back and forth with this person https://repo.getmonero.org/monero-project/ccs-proposals/-/issues/197#note_31943 , thats all my ccs updates for today thank you     
    
> **\<nioc\>** wait, wut, that's it?     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> but how long before someone actually has to do something on the moneropulse DNS'?     
    
> **\<nioc\>** can I shill for rick here?     
    
> **\<nioc\>** *ruck     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> highlights of AI slop* we didnt cover the ideas yet, so you still can     
    
> **\<DataHoarder\>** That branch already checks moneropulse, and moneropulse (testnet) domains are being updated     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> 👏     
    
> **\<Cindy\>** plowsof: is the AI slop proposal in question the uhh "federation market nodes"?     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> it's alive dig -t txt testpoints.moneropulse.net +dnssec     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> correct      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> lets cover the open CCS ideas unless there are other highlights      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> News: Monero Observer (https://www.monero.observer/) - Revuo Monero (https://revuo-xmr.com/)     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> a. MoneroOS Resurrection (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/596)    from 4rkal     
    
> **\<4rkal\>** <4rkal> I’m here btw     
    
> **\<4rkal\>** <4rkal> If anyone has any questions     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> thanks for joining      
    
> **\<pumpxmr\>** I came across this, not sure if helpful to your proposal: https://github.com/MineCoreLive/minecore     
    
> **\<4rkal\>** <4rkal> @plowsof:matrix.org: This proposal has been open for two months now. Monero is under attack, this could help     
    
> **\<4rkal\>** <4rkal> I’ve answered all relevant questions. I see no reason as to why it shouldn’t be merged     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> thanks for sharing pumpxmr      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> any other questions/comments      
    
> **\<4rkal\>** <4rkal> pumpxmr: Looks abandoned     
    
> **\<4rkal\>** <4rkal> Interesting nonetheless     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> thanks for joining 4rkal, i think we can move on      
    
> **\<Cindy\>** i actually tried minecore a bit     
    
> **\<jmrdmatrix:matrix.org\>** <jmrdmatrix:matrix.org> Excuse me gentlemen, I just joined this group...may I be reminded of its purpose and how I can contribute?     
    
> **\<Cindy\>** it's pretty bare-bones     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> @jmrdmatrix:matrix.org: Work related things. this is a meetings on CCS proposals and other community updates and ongoinga     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> this is currently a meeting. people are giving opinions on CCS proposal ideas. the agenda is here https://github.com/monero-project/meta/issues/1271 they occur every other week , Saturday 16:00UTC     
    
> **\<@plowsof:matrix.org\>** <ofrnxmr:xmr.mx> See here^ > <@plowsof:matrix.org> meeting time https://github.com/monero-project/meta/issues/1271      
    
> **\<jmrdmatrix:matrix.org\>** <jmrdmatrix:matrix.org> Wow very impressive I will listen and watch...     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> Cindy did it work? xmrig downloaded + started?     
    
> **\<Cindy\>** it mines off of moneroocean     
    
> **\<Cindy\>** no p2pool     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> RIP     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> moving on     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> b. [hbs] EVM Atomic Swaps (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/597)     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> 7 updoots, time to merge      
    
> **\<Cindy\>** i was gonna work on something similar, like a super light image with nothing but a TUI program that ran xmrig     
    
> **\<hbs:matrix.org\>** <hbs:matrix.org> I'm here if there are any more questions, though I think I answered all those that were asked     
    
> **\<Cindy\>** that would be loaded via network TFTP boot by a master server (which hosts p2pool)     
    
> **\<Cindy\>** but i do't know about the interest on that     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> id reach out to actual miners with several machines already - see if they would consider switching to your proposed setup and what they would gain over their current. ive seen several posting on r/moneromining      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> moving on, thank for joining hbs     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> d. v1docq47 - monero konferenco 2025 voice-over and working on xmr.ru (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/607)     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> open for feedback     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> c. Monero Python Maintenance (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/598)     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> seems that a proof of concept showing the stressnet team who require multiple wallet rpc's to be running at the same time the benefits of this would be beneficial and/or dockerised. not happened yet     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> Rucknium has even considered monero-oxide (or already using?)     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> moving on     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> e. Revuo Monero Maintenance (2025 Q4) (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/610)     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> speaking of newsletters, should https://cyphergoat.com/blog/twim-3 be added to the meeting agendas?      
    
> **\<4rkal\>** <4rkal> @plowsof:matrix.org: Would be greatly appreciated!     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> you joined the meeting so its the least we can do      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> thanks for the newsletter      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> recanmann is the author? and will continue for the foreseeable future?     
    
> **\<4rkal\>** <4rkal> Yes     
    
> **\<4rkal\>** <4rkal> Btw the newsletter is also available via email     
    
> **\<4rkal\>** <4rkal> If anyone is interested     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> how does that work? subscribe to the list and receive text only version?     
    
> **\<4rkal\>** <4rkal> It’s a pretty html version     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> im blind, its right there "Stay updated - Get new posts via email"     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> Subscribed successfully.     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> ok lets move on     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> f. Boog900 full time work on Cuprate (3 months) (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/611)     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> boog will be back on Monday 👍️     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> with some time left i believe nioc wishes to shill something during any other business     
    
> **\<Cindy\>** is there any plas to make a lightweight monero library     
    
> **\<Cindy\>** that doesn't depend on the monolith of the official monero program     
    
> **\<Cindy\>** i'd like to eventually write one in C, mostly for embedded environments     
    
> **\<nioc\>** Rucknium has been doing a tremendous amount of work recently and has this page up  https://rucknium.me/donate/     
    
> **\<nioc\>** I would be willing to match donations given      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> generous offer, thank you nioc      
    
> **\<Cindy\>** i support nioc's shilling     
    
> **\<DataHoarder\>** It's time for the sponsored segment     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> Cindy i do not know, i would ask jeffro256 perhaps... this sounds like something hardware wallets are currently using. what features would you require? decoding outputs / signing transactions?      
    
> **\<nioc\>** DH may have a address on the p2pool site  :)     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> DataHoarders website with images https://blocks.p2pool.observer/      
    
> **\<DataHoarder\>** Or OpenAlias p2pool.observer     
    
> **\<Cindy\>** generating wallets would be the core part     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> i miss the low quality images which gave me quake2 nostalgia but they are high quality now     
    
> **\<Cindy\>** perhaps decoding outputs and signing would be side-features     
    
> **\<Cindy\>** yes, DataHoarder really up'd the image qualities     
    
> **\<DataHoarder\>** Thanks to Cindy for making the simple p2p SVG logo     
    
> **\<DataHoarder\>** It still has none officially but it's a good display     
    
> **\<Cindy\>** it was inspired by the original very low quality p2pool logo     
    
> **\<DataHoarder\>** For any small pool operators that want their logo shown please make one and don't just use Monero logo lol     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> ohh thanks      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> i noticed something     
    
> **\<DataHoarder\>** No idea where that logo was for either     
    
> **\<Cindy\>** did you take it from mining pool stats?     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> what about the likely AI slop generated thing for the nintendo64 Cindy? this is also C https://github.com/bowler-bear/retro-crypto     
    
> **\<DataHoarder\>** Yes, Cindy.     
    
> **\<Cindy\>** this looks like a mish-mash of stuff taken from other projects     
    
> **\<Cindy\>** (also the creator shows screenshots of the... linux build instead of the N64 build)     
    
> **\<Cindy\>** but i'll see if i could salvage parts from it     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> and anybody who has seen a QR code before knows what monospacing looking like      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> from this bounty https://bounties.monero.social/posts/168/4-022m-gamepad-controlled-cryptographic-multitool-with-offline-wallet-address-generator     
    
> **\<Cindy\>** i actually hope monero doesn't use AES at all     
    
> **\<Cindy\>** it would be crippling     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> an open end here, thanks all for attending      

Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: plowsof | 2025-09-20T10:47:30+00:00
- Closed at: 2025-11-05T10:12:10+00:00
