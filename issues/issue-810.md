---
title: 'Monero Community Workgroup Meeting: Saturday 25th March 2023 @ 16:00 UTC'
source_url: https://github.com/monero-project/meta/issues/810
author: plowsof
assignees: []
labels: []
created_at: '2023-03-13T10:01:20+00:00'
updated_at: '2023-03-29T14:01:02+00:00'
type: issue
status: closed
closed_at: '2023-03-29T14:01:02+00:00'
---

# Original Description
Location: [Libera.chat, #monero-community](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-community:monero.social?via=matrix.org&via=monero.social)

[Instructions for joining the monero.social Matrix server.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time
16:00 UTC [Check your timezone](https://www.timeanddate.com/worldclock/converter.html)

Moderator: plowsof

Please reach out in advance of the meeting if you would like to propose an agenda item.

Proposed Meeting Items:

1. Introduction
2. Greetings
3. Community highlights    
- MRL further discusses tx_extra #811
- tx_extra will now be limited (breaking the current form of morbinals) but mining pools must use the upcoming release. 
- Monerotopia [How Monero devs will respond to NFTs](https://yewtu.be/watch?v=sMixnK8FM_g)
- https://github.com/mooonero/mordinals
- [FeatherWallet 2.4.3](https://featherwallet.org/changelog/)
- [p2pool](https://p2pool.io) successful hardfork! also sech1: "It takes ~3 times less CPU time now to do the initial sync when starting P2Pool, thanks to more efficient caching after the fork, so it will sync faster for everyone, especially weak CPUs like Raspberry Pi."
- [AcceptXMR v0.12.0](https://github.com/busyboredom/acceptxmr/releases/tag/v0.12.0) [100% Funded](https://ccs.getmonero.org/funding-required/)
- https://gupax.io/ - [monero-bash](https://github.com/hinto-janai/monero-bash/releases) updates by hinto-janai
- [Monero in every corner of the world](https://www.reddit.com/r/Monero/comments/11vmidi/monero_in_every_corner_of_the_world) - [Lovera](https://nitter.it/BTClovera)
- R*ddit censors a thread about overcoming tyranny - hyc re-shares at https://monero.house/post/168 (monerobull set up monero.house which is falsely blocked by some ISPs) [tweet](https://nitter.it/hyc_symas/status/1638104358146437123#m)
- https://kuno.bitejo.com/ Launched! (created by anarkiocrypto) alternative URL redirect from plowsof @ https://p2pcrowd.fund
News: [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/) - [The Monero Standard](https://localmonero.co/the-monero-standard) - [Monero Moon](https://www.themoneromoon.com/)    
5. [CCS updates](https://ccs.getmonero.org/)    
  b. [Computational work for OSPEAD parameterization](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/375)    
  c. [dangerousfreedom - wallet development 2](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/377)   
  d. [Draft: New Animated Video series future](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/379)
  e. [P2P Publisher - Monerotopia Mexico City](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/380)
  f. [Maintaining flatpak package](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/381)
  g. [v1docq47 - monerokon 2022 (part 2) and monerotopia 2023 voiceover and working on xmr.ru](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/382)    
- CCS over funded proposals list @ https://github.com/plowsof/scrape_ccs_fr

We have been focusing on these 3 proposals:
- [Molly.IM](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/252#note_20900)
- [New Animated Video series](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/379)
- [SoloptXMR](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/299)

Out of these 3 proposals, all but Endor (of SoloptXMR) have showed meaningful progress with their CCS (although animated videos series has closed their proposal, they still displayed effort and produced content) 

delayed
  a. [Draft Bulletproofs++ Peer Review](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/358)    
 
6. Workgroup reports    
  a. Dev workgroup
  b. Localization workgroup
  c. Outreach workgroup
  d. Events workgroup - [MoneroKon 2023](https://github.com/MoneroKon/)
  e. Website workgroup
  f. Policy workgroup
  g. Research workgroup
  h. [Seraphis Migration workgroup](https://github.com/seraphis-migration)
7. Open ideas time    
  - Hackerone - is it time to allocate more funds here [like this previous proposal](https://forum.getmonero.org/8/funding-required/87597/monero-bounty-for-hackerone)
9. Confirm next meeting date/time    

[Previous meeting including logs](https://github.com/monero-project/meta/issues/)    

Meeting logs will be posted here afterwards.    


# Discussion History
## plowsof | 2023-03-26T12:00:05+00:00
Logs 
```
15:59:11 <plowsof11> is there a meeting today

15:59:53 <ofrnxmr[m]> Hello

16:00:12 <plowsof11> ah yes, Meeting time https://github.com/monero-project/meta/issues/810

16:00:14 <ofrnxmr[m]> Yes Sir.

16:00:20 <ofrnxmr[m]> Good morning.

16:00:34 <v1docq47[m]> hi all

16:00:58 <Rucknium[m]> Hi

16:01:01 <DiegoSalazar[m]> Hi

16:01:55 <CM_IV> Hello

16:02:02 <hinto[m]> hi

16:02:26 <plowsof11> lets throw some current events out there, we're pretty tx_extra / nft heavy right now?
the next release limiting tx_extra is imminent (on track for being tagged today) and out gitian builders will
be right on it verifying hashes (thank you)

16:02:42 <plowsof11> s/out/our

16:03:50 <plowsof11> anyone wants to listen to a monerotopia overview of the situation : good watch, features
someone claiming to be ofrnxmr - Monerotopia [How Monero devs will respond to
NFTs](https://yewtu.be/watch?v=sMixnK8FM_g)

16:03:50 <plowsof11>

16:05:13 <plowsof11> feathewallet.org updated.. p2pool hardforked woop woop , aand  https://gupax.io/ -
[monero-bash](https://github.com/hinto-janai/monero-bash/releases) updated too by hinto-janai

16:05:44 <plowsof11> do our mobile wallet friends have any updates to announce? how is stack wallet going , i
read something about a weeb mode

16:05:51 <ofrnxmr[m]> P2pool hard fork left behind a bunch if miners.

16:05:52 <ofrnxmr[m]> Please everybody update and spread the news

16:06:06 <ofrnxmr[m]> Stack Duo Diego Salazar:

16:06:28 <DiegoSalazar[m]> Yeboi

16:06:58 <DiegoSalazar[m]> Hopefully for iOS soon. Just received an app rejected this morning form apple cuz
they wanted to know the difference between Stack Duo and Stack Wallet.

16:07:04 <sech1> ofrnxmr[m] miners left behind are still mining valid Monero blocks and getting payouts, so
it's not critical

16:07:16 <DiegoSalazar[m]> I explained. Lower attack surface and stuff. Hopefully that'll go through now.

16:07:51 <plowsof11> nice, wishing you the best with that

16:08:14 <ofrnxmr[m]> For everyone else, Duo and Stack are the same codebase. Duo is BTC + XMR only

16:08:54 <plowsof11> i watch this short clip made by Lovera every morning whilst eating breakfast  [Monero in
every corner of the
world](https://www.reddit.com/r/Monero/comments/11vmidi/monero_in_every_corner_of_the_world) -
[Lovera](https://nitter.it/BTClovera)

16:09:02 <ofrnxmr[m]> Love it ^

16:09:12 <plowsof11> ft a clip of geonics movie

16:10:42 <plowsof11> AcceptXMR was funded since the last meeting also BusyBoredom is working away at milestone
1 🫡 has the tasks organised nicely on his github https://github.com/busyboredom/acceptxmr

16:11:19 <plowsof11> i doubt we'll have enough time to discuss today but there was a 'rust' monero
payments/business/invoice idea posted today, perhaps they could build upon acceptxmr

16:11:42 <plowsof11> Bulletproofs++ went to funding wat ?

16:12:17 <ofrnxmr[m]> Bp++ ccs was moved to funding after the MRL meeting

16:12:48 <fr33_yourself[m]> Do we know who will be reveiwing bp++?

16:12:57 <plowsof11> 121/130 already - the next MRL meeting on wednesday will be discussing another paper too,
exciting times for the MRL - options are wide open. CypherStack will be performing the peer review on that
paper*

16:13:06 <ofrnxmr[m]> Almost fully funded, and I believe it was funded with outside money. Have not confirmed

16:13:14 <plowsof11> that paper=bp++

16:13:28 <plowsof11> the general fund has not even had time to donate

16:14:18 <plowsof11> kuno.bitejo.com new fundraising platform (some sus things there at the moment, but
amazing work from anarkiocrypto to get it up and running)

16:14:38 <ofrnxmr[m]> The code was released as well iirc

16:15:10 <plowsof11> yep all open source

16:16:04 <plowsof11> News: [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-
xmr.com/) - [The Monero Standard](https://localmonero.co/the-monero-standard) - [Monero
Moon](https://www.themoneromoon.com/)  for other news sources

16:16:26 <plowsof11> shall we jump into the ccs ideas? anything else on your minds?

16:16:51 <Lovera[m]> Hi everyone

16:16:53 <ofrnxmr[m]> Majesticbank has been down for some days. Elitewallet as well

16:17:40 <Lovera[m]> ofrnxmr[m]: Just coincidence

16:18:00 <plowsof11> yes, since the 19th march i believe, apprently 'updating' to a DEX 🤔 waiting on updates
about their status

16:18:43 <ofrnxmr[m]> MajesticBank @MajesticBank:libera.chat:  please confirm

16:19:24 <plowsof11> oh just wanted to plug jeffro256 , making all kinds of pull requests to help speed our
Monero experience up

16:19:46 <Siren[m]> plowsof11: They must be either exit scamming some people or testing in production.

16:19:46 <Siren[m]> They were up on 22nd and went down on 9th confirmation for this person

16:19:46 <Siren[m]>
https://www.reddit.com/r/Monero/comments/121cu1v/sent_xmr_to_majesticbank_now_cant_reach_site_or/

16:19:49 <ofrnxmr[m]> Molly IM proposal update regarding wallet SDK has shifted the scope of the ccs. Im not
sure where to go with that.

16:19:50 <plowsof11> in tandem with jberman and rbruner

16:20:56 <plowsof11> the dev of valldrac has been active / working on the SDK , available to questions and
also consultancy for the serpahis migration team

16:21:08 <ofrnxmr[m]> ^ right

16:21:46 <plowsof11> endor00: has no updates for solopt work uhm

16:21:46 <ofrnxmr[m]> Regarding Molly, I wonder what we are tonexpect from molly

16:21:46 <ofrnxmr[m]> SDK sounds like standalone ccs

16:22:30 <ofrnxmr[m]> Cant be mad when the project manager was paid to leave the project in shambles

16:22:36 <plowsof11> yes the sdk looks good, created in a modular way from scratch, alot of benefits to the
existing tech

16:23:06 <ofrnxmr[m]> And cost and scope of SDK, imo, should be separate from Molly

16:23:42 <plowsof11> we can revisit that , the update of molly was just a 'tell all' update of where theyre
at. they will continue to work on the ccs , just progress has been slow

16:24:18 <plowsof11> lets jump to the merges, quickly glossing over this one which was closed

16:24:26 <plowsof11>  b. [Computational work for OSPEAD parameterization](https://repo.getmonero.org/monero-
project/ccs-proposals/-/merge_requests/375)

16:24:26 <plowsof11>

16:24:26 <plowsof11> Isthmus has closed the ccs citing 'not enough Q2 bandwidth' as one reason but will
continue contributing to OSPEAD on weekends (full comment here https://repo.getmonero.org/monero-project/ccs-
proposals/-/merge_requests/375#note_20926 )

16:24:31 <ofrnxmr[m]> Animated videos project has halted ******

16:24:58 <plowsof11>   c. [dangerousfreedom - wallet development 2](https://repo.getmonero.org/monero-
project/ccs-proposals/-/merge_requests/377)

16:24:58 <plowsof11> this proposal is contributing to the seraphis wallet migration efforts.  I've raised some
concerns in the comments about the original idea / DF's previous ccs. the proposal has now been adjusted and
obtained approval from the creator of seraphis koe and migration coordinator Rene.

16:25:25 <ofrnxmr[m]> So were closing, paying out 9xmr and I propose we repurposed the remainder at a
following meeting

16:25:48 <plowsof11> the no wallet left behind meetings can make the final push for that as they have more
people attending involved

16:26:32 <ofrnxmr[m]> Agreed that no mrl / dev should give the final OK on dsngerousfreedom's ccs

16:26:48 <plowsof11> ok yes, onto the video ccs as above ^

16:26:49 <plowsof11>   d. [Draft: New Animated Video series future](https://repo.getmonero.org/monero-
project/ccs-proposals/-/merge_requests/379)

16:26:49 <plowsof11> savandra has confirmed in the ccs comments that its over. but open to returning to
compete with others willing to take on the ccs. full details here: https://repo.getmonero.org/monero-
project/ccs-proposals/-/merge_requests/308#note_20952

16:27:07 <plowsof11> monerobull also comments for paying 9xmr and closing

16:27:53 <plowsof11> i agree with this also, there was talks of splitting payouts etc for dsmlegend but, for
simplicity , 9xmr to savandra and close is the easiest. they are 'sticking around' to compete also

16:27:57 <monerobull[m]> Hello

16:28:47 <plowsof11> closing and paying 9xmr (decide what to do with the remaining funds later meeting) yes/no

16:29:29 <Lovera[m]> plowsof11: Yes

16:29:30 <ofrnxmr[m]> The ccs is 9xmr = 4minute video.

16:29:30 <ofrnxmr[m]> Video 1 is 2 minutes, but the scripts (10% if the ccs aka 4.5xmr) for all 5 were
finished. So imo paying 9 is accurate and fair

16:29:47 <ofrnxmr[m]> (Yes)

16:30:28 <xmrfn[m]> Yes and hoping someone picks it up, the animations & scripts were so promising

16:30:39 <monerobull[m]> Not really

16:30:39 <hinto[m]> for the record, the leftover is 36 xmr

16:30:54 <hinto[m]> i agree, close

16:31:33 <plowsof11> consensus is clear to close and pay 9xmr , moving on?

16:31:48 <ofrnxmr[m]> Yes sir.

16:31:58 <plowsof11>   e. [P2P Publisher - Monerotopia Mexico City](https://repo.getmonero.org/monero-
project/ccs-proposals/-/merge_requests/380)

16:31:58 <plowsof11> i've seen this topic discussed here already. we've been given a dealine by the proposer
to get it funded soon, so we need to look and vote merge/close as the next meeting is after the deadline (3
days). Lovera shared that they will be attending MoneroTopia too!

16:32:16 <ofrnxmr[m]> IMO close. Childish ccs

16:32:17 <monerobull[m]> Close

16:32:22 <plowsof11> close

16:32:51 <monerobull[m]> Consensus 👍

16:33:18 <plowsof11> its jut not feasible , even if it was a good proposal we all liked - to get it to funding
before the deadline

16:33:28 <Lovera[m]> > <@plowsof:matrix.org>   e. [P2P Publisher - Monerotopia Mexico
City](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/380)... (full message at
<https://libera.ems.host/_matrix/media/v3/download/libera.chat/5f7915395c279527c24b51ce621728455b65f9da>)

16:33:32 <ofrnxmr[m]> The proposer "doug doesnt like me and I have nothing to do with monerotopia" but will
use monerotopia to get funding

16:33:48 <ofrnxmr[m]> Monerotopias name* to get funding

16:34:06 <monerobull[m]> That was the cherry on top

16:34:26 <plowsof11> also, we also have 36 xmr in an abandoned outreach ccs , something to discuss at another
meeting

16:34:46 <ofrnxmr[m]> And like 240 overfunded

16:34:48 <Lovera[m]> plowsof11: And about overfunded projects?

16:35:06 <Lovera[m]> ofrnxmr[m]: Yep

16:35:11 <plowsof11> ive listed a few proposals here we shold be able to tackle
https://github.com/plowsof/ccs-wip-list/issues

16:35:30 <ofrnxmr[m]> Wait. Where is plowsof update

16:35:35 <ofrnxmr[m]> Did he close out ccs?

16:35:53 <plowsof11> yes ccs coordinator was closed out and moved to completed yesterday

16:36:14 <ofrnxmr[m]> Volunteer 🐎

16:36:18 <plowsof11> we can get to this (overfunded also) after the next 2 proposals

16:36:37 <ofrnxmr[m]> plowsof11: Thank you

16:36:39 <plowsof11> im seeing consensus for closing the monerotopia / advertising proposal

16:36:51 <ofrnxmr[m]> Confirmed. Close

16:37:10 <plowsof11>   f. [Maintaining flatpak package](https://repo.getmonero.org/monero-project/ccs-
proposals/-/merge_requests/381)

16:37:10 <plowsof11>   im not sure BigmenPixel can make it today but is currently researching milestone 1
(will ask them to mark it as a Draft) : basically the build takes longer than a 6 hour limit - they're
investigating a fix atm, but want to hear how people feel about flatpak? and having a trusted/maintained
Monero-gui on the core monero repo?

16:38:13 <ofrnxmr[m]> I would like for milestones to be broken up in a feasible way

16:38:24 <ofrnxmr[m]> Monthly etc

16:38:40 <ofrnxmr[m]> Or quarterly

16:39:00 <plowsof11> quarterly sounds better yes

16:39:13 <plowsof11> do we know what flatpak is?

16:39:30 <ofrnxmr[m]> Otherwise ccs looks good to me

16:39:31 <plowsof11> ive used it before, handy for noobs to keep monero-gui updated

16:39:40 <ofrnxmr[m]> Flatpak is important for easy updates for grandma

16:40:08 <plowsof11> 3.5xmr will pay for the investigatoins/implementation to get it @ monero core , then only
monero approved persons can make changes

16:40:56 <ofrnxmr[m]> Yes, first step is to have it a verified Flatpak

16:40:57 <xmrfn[m]> Flatpak is a nice extra sandbox for apps and a way to avoid f--king up your machine with
depedencies

16:40:58 <ofrnxmr[m]> And have it hosted on getmonero instead on flathub similar to obs

16:40:59 <plowsof11> BigmenPixel is honest and wants to be certain its possible before considering moving it
to funding , just wants thoughts

16:41:02 <plowsof11> thanks for the comments

16:41:52 <plowsof11> the less times we have to reset the 0 days since 0.17.3.2 counter the better

16:41:53 <ofrnxmr[m]> IMO, quarterly (so he doesnt have to wait for payment) and its fine

16:42:12 <ceetee[m]> plowsof11: Did a quick research and as a complete Linux noob it seems pretty good & user
friendly. If it's a "secure" way to install monero, then I am all for it 👍

16:42:30 <ofrnxmr[m]> Perhaps also write guides

16:42:40 <plowsof11> ill be following up with him / trying to help if possible - and share when any progress
is made for step 1

16:42:49 <plowsof11> docs are always good yes

16:42:55 <ofrnxmr[m]> So users know the Flatpak is available, official and recommended

16:43:23 <plowsof11> there is a guide on... kicksecure? which recommends to use flatpak (thats the main reason
for the ccs really, as whonix has discontinued support for the monero packages, and points users to flatpak)

16:43:54 <plowsof11> hinto shared news of that in a monero-gui issue, and then a user on here told us about it

16:44:03 <hinto[m]> ideally each release should be reviewed in some way before labeling it verified

16:44:20 <hinto[m]> although that seems like more work for other people so...

16:44:22 <ofrnxmr[m]> Verified = it builds out of the Getmonero tagged releases

16:44:29 <ofrnxmr[m]> Monero-project***

16:45:23 <hinto[m]> if we could find a debian trusted maintainer that would be perfect

16:45:23 <plowsof11> and no need to trust 1 person didnt change something

16:45:24 <hinto[m]> apt repos would cover debian, ubuntu, tails, etc

16:45:33 <ofrnxmr[m]> Instead of where most flatpaks are submitted to flathub by "anyone", this ccs will bring
the Flatpak into the core repo

16:45:36 <hinto[m]> the current debian monero-gui is still 0.17.x.x iirc

16:45:50 <ofrnxmr[m]> Debian maintainer stopped maintaining

16:46:03 <ofrnxmr[m]> Flatpak is easier to keep updated as well, for the maintainer

16:46:22 <hinto[m]> that was for whonix's custom apt repo

16:46:57 <xmrfn[m]> IIRC, the issue with Debian & Whonix was basically that released are out-of-phase, they
can't deply important wallet updates quickly. Yes? Flatpack would help with that a lot

16:47:07 <xmrfn[m]> s/released/releases/

16:47:18 <xmrfn[m]>  * IIRC, the issue with Debian & Whonix was basically that releases are out-of-phase with
Monero's, they can't deply important wallet updates quickly. Yes? Flatpack would help with that a lot

16:47:35 <xmrfn[m]>  * IIRC, the issue with Debian & Whonix was basically that releases are out-of-phase with
Monero's, they can't deply important wallet updates quickly. Yes? Flatpak would help with that a lot

16:47:41 <xmrfn[m]> Same with Tails

16:47:56 <xmrfn[m]> (Tho I don't think Tails supports Flatpak)

16:48:17 <plowsof11> bigmenpixel has been keeping the flatpak already updated for over a year also, seems like
we 'like the idea of flatpak' and suggest changes to the milestones + possible extras (docs)

16:48:30 <plowsof11> quarterly

16:48:46 <plowsof11> moving on

16:48:59 <plowsof11> thanks for comments btw^

16:49:06 <plowsof11>     g. [v1docq47 - monerokon 2022 (part 2) and monerotopia 2023 voiceover and working on
xmr.ru](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/382)

16:49:06 <plowsof11> seens to have been working away on their current ccs, updates can be seen in comments
here https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/343. just for
visibility/transparency, there has been a slight rate/hour increase from 10$ to 14$ per hour, from 28~ to ~30
hours per week.

16:49:44 <plowsof11> formatting^ the previous proposal was stagnant for a long time because we couldnt find
any Russians to provide feedback - but when moved to funding , it was funded quite quickly

16:50:20 <v1docq47[m]> I will be glad to answer your questions

16:50:48 <plowsof11> in recent days weve had some RU users on here too, can only point them xmr.ru / the
xmr.du yotue channel

16:51:13 <plowsof11> so its making my life easier at least

16:51:36 <DiegoSalazar[m]> v1docq47[m]: You've been doing this work for years, man. Inflation happens to us
all.

16:52:43 <ofrnxmr[m]> The thing is, the Russian market is not very active HERE. But if his proposals are being
funded organically, I see no issue with the price.

16:52:43 <ofrnxmr[m]> Would be nice to have Russian users chime in

16:52:44 <v1docq47[m]> Yes, Russian users wrote to me. Basically, these were questions about RU blocking
localmonero

16:53:15 <plowsof11> it was posted 3 days ago, like the last one, ill try to point russian users there to give
feedback

16:53:24 <plowsof11> thank you v1d ,

16:53:32 <plowsof11> how do russian users buy monero without localmonero ?

16:53:47 <ofrnxmr[m]> But barring translating Russian feedback, id move it to funding and see how if they want
to fund it

16:53:54 <plowsof11> this will be helpful for Alex | LocalMonero | AgoraDesk when being asked angry questions

16:54:10 <v1docq47[m]> All communication of the Russian-speaking segment of Monero takes place in our telegram
group

16:55:08 <v1docq47[m]> directly in the group and through RU exchanges

16:55:26 <plowsof11> can i confirm that RU people can actually 'get' monero? xD

16:55:26 <Lovera[m]> ofrnxmr[m]: I’m speak Russian, and I can confirm that in Russian telegram Monero group is
active

16:55:42 <plowsof11> Lovera what 3 letter agency do you work for , you speak too many languages sir

16:55:55 <ofrnxmr[m]> Language barriers and internet censorship are a real issue with Russia.   Even though
its new, id move it to funding.

16:56:27 <Lovera[m]> plowsof11: For XMR

16:56:47 <plowsof11> hahah good answer

16:56:50 <v1docq47[m]> <plowsof11>, Yup :)

16:57:17 <ofrnxmr[m]> Work isnt set to start til may

16:57:27 <plowsof11> thanks i will point them in your TG group direction

16:58:07 <v1docq47[m]> Yes, there is some work that I did not include in CCS

16:59:06 <ofrnxmr[m]> 0 wait a week

16:59:06 <ofrnxmr[m]> 1 merge

16:59:06 <ofrnxmr[m]> 2 close

16:59:27 <plowsof11> 0+ for feedback

16:59:29 <ofrnxmr[m]> 2 weeks**

16:59:42 <plowsof11> its only posted 3 days ago

16:59:48 <ofrnxmr[m]> My issue with feedback is its russian

17:00:13 <Lovera[m]> 0 i think

17:00:28 <ofrnxmr[m]> How do we reach out, if not via VDO?

17:00:28 <plowsof11> will try to shill it to every RU user i see

17:01:23 <ofrnxmr[m]> Almost out if time.

17:01:23 <ofrnxmr[m]> Monerod updates coming soon. Keep your eyes open

17:01:50 <plowsof11> AOB

17:02:04 <ofrnxmr[m]> Help with the gitian builds if you are available after tagging

17:02:26 <plowsof11> the other ccs idea posted today https://repo.getmonero.org/monero-project/ccs-
proposals/-/merge_requests/383 Oceanus ERP Software for Small Businesses . will need to check those pdfs

17:02:33 <xmrfn[m]> https://github.com/monero-project/monero/blob/master/contrib/gitian/README.md

17:02:37 <plowsof11> for next time

17:02:55 <plowsof11> its not gunna be morbin time for long 💢

17:03:02 <ofrnxmr[m]> Thank you plowsof @plowsof:matrix.org:

17:03:12 <hinto[m]> i skimmed the pdfs

17:03:13 <hinto[m]> seemed pretty interesting

17:03:22 <ajs_[m]> AOB - monerokon CFP submission deadline 3rd April

17:04:11 <plowsof11> also i QUIT f' you all for ruining my life, see you next meeting ❤️

17:05:02 <ofrnxmr[m]> 3 months of 2022, 3 months of 2023

17:05:18 <ofrnxmr[m]> Next time you need to specify which year you'll do the 3 months in

17:38:12 <ofrnxmr[m]> Be sure to check tx volume today

17:38:25 <ofrnxmr[m]> Looks like 80% of volume is nfts

17:39:41 <ofrnxmr[m]> (Probably closer to 50%)

17:48:45 <plowsof11> i forgot to mention the overfunding of proposals - what to do with the excess, sorry
Lovera - giving it to the proposer spread out over the milestones (minus 'gas' fees) was suggested. also,
putting it all in one pile and paying for other things like audits.

17:53:26 <plowsof11> if you are a victim of overfunding gate - perhaps a 12 month deadline to come forward to
make a claim to your funds - after that - to be decided (i have +1 xmr to gain from this so i cant really give
a non-biased suggestion)


```
Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)


continued:
```
17:58:50 <BusyBoredom[m]> Maybe use it to match donations to CCSs in funding required for a while. Get things funded twice as fast for a bit. 
17:59:11 <ofrnxmr[m]> Overfunded proposals should noted 
17:59:40 <ofrnxmr[m]> Say koe is overfunded, and has another ccs coming 
17:59:43 <ofrnxmr[m]> We can roll it over 
18:00:36 <Lovera[m]> There are certain proposals that continue month to month like Monero Observer or even Feather Wallet, developer work, etc... It could be used to fund future proposals from the proposer I.e
18:01:43 <Lovera[m]> I am referring to proposals that have been overfunded and that it is known that there will be another proposal of the same kind proposer
18:02:44 <Lovera[m]> 12 months seems like a long time... 3 months maximum and then it could be donated to other proposals of interest such as audits.
22:47:32 <ofrnxmr[m]> NotMtth:  hey, you there?
22:53:25 <ofrnxmr[m]> https://xmrposter.club/notice/ATz4KfK5TcZySEX0D2
22:53:25 <ofrnxmr[m]> Wondering the bottom comment 
22:59:34 <escapethe3ra[m]> <btclovera[m]> "There are certain proposals that..." <- I agree. Extra MO CCS funds can go to audit/research/dev-security/other proposals of 'high interest' or to my future proposals if nothing requires additional funding at that time, up to the community.
```

john_r365 also suggests @ https://github.com/plowsof/scrape_ccs_fr/issues/1

> Presumably these excess CCS funds can be put to good use somehow.
>One such opportunity is getting some extra eyes on the Seraphis (or similar) code when it comes time. Specifically I mean at least one third party audit.
>Of course, there may be better suggestions for where to put the funds.

# Action History
- Created by: plowsof | 2023-03-13T10:01:20+00:00
- Closed at: 2023-03-29T14:01:02+00:00
