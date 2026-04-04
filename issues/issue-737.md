---
title: 'Monero Community Workgroup Meeting: Saturday 24th September 2022 @ 16:00 UTC'
source_url: https://github.com/monero-project/meta/issues/737
author: plowsof
assignees: []
labels: []
created_at: '2022-09-21T12:15:07+00:00'
updated_at: '2022-09-24T18:36:58+00:00'
type: issue
status: closed
closed_at: '2022-09-24T18:33:53+00:00'
---

# Original Description
Location: [Libera.chat, #monero-community](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-community:monero.social?via=matrix.org&via=monero.social)

[Instructions for joining the monero.social Matrix server.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time
16:00 UTC [Check your timezone](https://www.timeanddate.com/countdown/fall?iso=20220924T16&p0=1440&msg=Monero+Community+Workgroup+Meeting%3A+Saturday+24th+September+2022+%40+16%3A00+UTC&font=sanserif)

Moderator: Luigi1111

Please reach out in advance of the meeting if you would like to propose an agenda item.

### Main Agenda
Discuss CCS merge list @ https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests

  a. [MoneroSigner. Fork of seedsigner for Monero](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/323)    
  b. [[monero-bash] continued development (3 months)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/333)    
  c. [The-Monero-Moon-CCS-Proposal-August2022-John-Foss](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/336)    
  d. [Monero archive](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/339)    
  e. [Forgotsudo monero marketplace](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/340)    
  f. [escapethe3RA Monero Observer maintenance (Autumn 2022)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/342)    
  g. [v1docq47 - monerokon and monerotopia voiceover and working on xmr.ru](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/343)    

Other:
- MSvB - Hackers Congress Paralelní Polis (HCPP) 2022  https://last-shot.hcpp.cz/ — MSvB and SethForPrivacy are named speakers at the event - *September 30- October 2, 2022* 


prev logs #723 

# Discussion History
## plowsof | 2022-09-24T18:33:52+00:00
Logs 
```
16:00:58 <plowsof> Hello! meeting time https://github.com/monero-project/meta/issues/737

16:01:17 <plowsof> greetings all

16:01:33 <msvb-web> Hello.

16:01:38 <dangerousfreedom> Hello

16:01:44 <monero_archiver[> Hello

16:01:45 <v1docq47> Hello

16:01:47 <Rucknium[m]> Hi

16:01:53 <NorrinRadd> selenze[m] the bridges are already active

16:01:58 <NorrinRadd> Hi All

16:02:17 <gunslinger_zach[> hello

16:02:24 <hinto[m]> hi

16:02:34 <plowsof> main topic is to discuss CCS merge list @ https://repo.getmonero.org/monero-project/ccs-
proposals/-/merge_requests , oldest first

16:03:26 <plowsof> a. MoneroSigner. Fork of seedsigner for Monero

16:04:07 <midipoet> hello all

16:04:20 <Rucknium[m]> AFAIK, this got merged, but is in some sort of formatting limbo

16:05:04 <luigi1111w> yeah let me look at it quick

16:05:10 <luigi1111w> but we don't need to discuss it, it's merged

16:05:19 <plowsof> ok nice

16:05:37 <plowsof> so he has to fix "something" for it to appear on Funding required?

16:05:51 <luigi1111w> nah I usually do

16:06:53 <plowsof> that was easy then, thanks, onto the next:

16:06:57 <plowsof>   b. [[monero-bash] continued development (3 months)](https://repo.getmonero.org/monero-
project/ccs-proposals/-/merge_requests/333)

16:07:39 <plowsof> 1 shill comment from myself there

16:07:54 <luigi1111w> I think this is a yes if he fixes the mr

16:08:18 <plowsof> we wanted him to define his rates last meeting, not much else

16:08:19 <luigi1111w> wait nvm

16:08:24 <ajs_[m]> how this bash thing better than just downloading the sources directly

16:08:24 <plowsof> the xmr , usd amount?

16:08:39 <plowsof> hinto: hinto

16:08:42 <luigi1111w> milestones and amount is backwards

16:08:48 <hinto[m]> mr = market rate?

16:08:54 <luigi1111w> merge request

16:09:03 <duggavo[m]> plowsof: Isn't $22 per work hour a little bit too much for a bash script?

16:09:25 <NorrinRadd> no

16:09:50 <plowsof> "bash scripts" is an oversimplification

16:09:56 <hinto[m]> not sure what to say other than to look at the source

16:10:00 <Rucknium[m]> Programming labor is expensive.

16:10:11 <hinto[m]> its around 4k lines of code

16:10:23 <plowsof> what advantage do i get from using monero bash , other than "downloading sources directly"

16:10:58 <duggavo[m]> duggavo[m]: I mean that the proposal might not be worth its cost

16:11:35 <ajs_[m]> it is a nice tool, but it seems too niche that only a few people will ever use

16:12:17 <plowsof> off the top of my head i see its used for easy p2pool install / setup (monero node setup)

16:12:56 <hinto[m]> i agree its pretty niche, from what i can tell from github stats it seems theres 50~100
users

16:13:35 <luigi1111w> current hourly is $19.5 or so if unchanged

16:13:58 <hinto[m]> ideally these packages would be available direct in all linux repos but thats almost never
going to happen

16:14:19 <luigi1111w> hinto[m] please move amount: ahead of milestones:

16:15:27 <luigi1111w> seedsigner is up

16:15:38 <plowsof> thanks

16:15:40 <Rucknium[m]> How can the existence of monero-bash be used to increase p2pool use?

16:15:56 <Rucknium[m]> Can we get p2pool guides to recommend it?

16:17:58 <plowsof> we like documentation and ease-of-use, are you alive hinto

16:18:03 <hinto[m]> luigi1111w: will do

16:18:40 <hinto[m]> Rucknium: im not sure since it does require a bit more setup/knowledge

16:18:55 <hinto[m]> maybe the way forward is for ease-of-use implementations of p2pool

16:19:15 <NorrinRadd> i find p2pool setup very easy

16:19:26 <hinto[m]> rather than monero-bash, which is geared more for power-users(?)

16:19:36 <NorrinRadd> monerod, p2pool, and xmrig are one line each in order to get them started

16:20:27 <hinto[m]> ease-of-use as in 1 program on windows that mines on p2pool with full hashrate

16:20:52 <hinto[m]> no configuration other than wallet, no terminal, easy one click

16:21:05 <duggavo[m]> NorrinRadd: Yes, a one-line script could be made by simply replacing newlines with "&&"

16:21:06 <hinto[m]> although i definitely can't build something like that

16:21:42 <duggavo[m]> I could build it as a cross-platform GTK+ application

16:21:47 <luigi1111w> if you believe it you can build it

16:22:00 <duggavo[m]> but that's unrelated with the CCS

16:22:46 <luigi1111w> I would rather the ccs had concrete deliverables instead of monthly

16:23:00 <luigi1111w> given the potential issues with such

16:25:36 <plowsof> time to put the 8 milestones below into concrete payouts , would be better

16:26:16 <luigi1111w> agree. We need to move on

16:26:27 <plowsof>   d. [Monero archive](https://repo.getmonero.org/monero-project/ccs-
proposals/-/merge_requests/339)

16:26:38 <luigi1111w> it's a yes but needs fixed

16:26:39 <plowsof> monero_archiver

16:26:49 <monero_archiver[> I think I have just fixed the format?

16:26:55 <monero_archiver[> Could you have a look?

16:27:09 <luigi1111w> looks much better

16:27:23 <luigi1111w> you don't need XMR on the amount ## though I'm not sure if it'll break it or not

16:27:39 <luigi1111w> if it does I can fix

16:28:04 <monero_archiver[> Okay I deleted it

16:28:46 <luigi1111w> merged. Let's see if it works

16:29:16 <luigi1111w> the biggest thing to discuss is newsletters funded by CCS and choosing winners and
what's appropriate

16:29:26 <luigi1111w> let's here them thots

16:29:29 <luigi1111w> hear*

16:29:54 <hinto[m]> luigi1111w: does the final completion of it all count as a deliverable? as in, 1 amount
only paid upon completion

16:30:12 <luigi1111w> hinto[m] sure if you are ok with that

16:30:18 <hinto[m]> sorry for late reponse the gitlab repo hangs my computer lool

16:32:25 <plowsof> my opinion specifically of johnfoss is written in the comments. (he is currently away for
another week or 2 so unable to comment) he is asking for almost double his competitor, and i call into
question his literacy skills / proof reading (he still has mistakes in his proposal) purchasing followers with
giveaways and using that as a benchmark.. has 400 followers and hasnt been able to get much thumbs up after
putting his proposal in

16:32:25 <plowsof> several of his newsletters, i am still FOR funding newsletters , as long as the author
produces good content

16:35:03 <luigi1111w> the balance of feedback supports merging observer and closing moon

16:35:16 <Rucknium[m]> Monero Observer is very good. Somehow both in-depth but to-the-point. Very timely. Like
a news wire service. CakeWallet is now using it for their news feed, an endorsement of its quality.

16:35:22 <luigi1111w> it's a bit unhandy we have "nahuhh" and "nope" floating around voting on stuff

16:35:47 <plowsof> i am indeed FOR monero observer

16:36:15 <plowsof> nahuhh is ofrnxmr , i do not know who nope is

16:36:39 <gnuteardrops[m]> +1  Monero Observer

16:37:41 <luigi1111w> ah ok, why don't they use the same name? Weight is given to "known" actors

16:38:11 <plowsof> ofrnxmr

16:38:16 <midipoet> +1 Monero Observer (mainly as i prefer the design and the manner content is presented)

16:38:27 <Rucknium[m]> M.O. also watches all the things that need to be watched: GitHub, CCS gitlab,
Matrix/IRC, etc. Probably has notifications for all those set up.

16:38:35 <luigi1111w> sounds like observer is an obvious merge. Please make your opinions known on ccs or just
upvote if you want

16:39:54 <plowsof> +1 MO

16:40:18 <monerobull[m]> Yes monero observer

16:41:40 <plowsof> there are sockpuppets who vote on ccs proposals, clearly, as luigi states, weight is given
to known characters , and feedback from these meetings is combined with multiple sources (reddit threads etc)
to make a decision

16:42:59 <plowsof>   g. [v1docq47 - monerokon and monerotopia voiceover and working on
xmr.ru](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/343)

16:43:46 <plowsof> this is a 're-vamp' proposal, (after translations no longer ccs) - offering transcriptions
, video content , and clear milestones goals

16:44:11 <luigi1111w> he's one of the longest standing ccs users

16:44:24 <luigi1111w> though I don't have a good way to tell if he's effective or not

16:44:47 <plowsof> and pricing at 10$/hour

16:45:12 <plowsof> organised nicely on his "twello" thing

16:45:36 <Rucknium[m]> Would like to hear from Russian speakers about the demand for this.

16:46:41 <v1docq47> i'm afraid that they are not frequent guests in irc

16:47:00 <ajs_[m]> not all monerokon videos are up yet.. WIP

16:47:14 <plowsof> i would like it to be advertised to a Russian audience and to have feedback from them , i
am swinging more to +1 than not , but our russian isn't good to judge

16:47:55 <plowsof> note - ENG transcriptions also for some thing

16:48:03 <midipoet> the videos seem pretty neat on the youtube channel (XMR.RU videos)

16:51:12 <plowsof> we want to see a demand from their Russian audience?

16:51:13 <Rucknium[m]> I have come across a few Russian-language research papers that mention Monero, FWIW

16:51:37 <plowsof> translating russian research papers to english , nice possibility

16:52:02 <plowsof> easier to review

16:52:18 <plowsof> well, for an MRL member

16:52:39 <msvb-web> The group who can understand russky is quite large, similar to french or english in
crossing culture borders.

16:53:02 <v1docq47> what kind of research work is this?

16:53:12 <Rucknium[m]> My overall impression is that the papers are sort of review papers that don't have much
indpendent scientific contribution, but I would be wrong obviously.

16:54:02 <Rucknium[m]> I did not save links to the papers since I couldn't understand them. I could probably
dig them up after a search

16:54:48 <plowsof> he has been translating into russian for 5+ years, if it was trash we would have known by
now

16:55:21 <Rucknium[m]> Um, I can remember one of them saying "Monero is obviously the best of the privacy
coins", which struck me as not too scientific.

16:55:50 <luigi1111w> that sounds very scientific

16:57:11 <plowsof> few minutes left, before we touch on msvb-labs presentation ... any other points on ths RUS
proposal?? our concern is "demand" ?

16:57:46 <Rucknium[m]> Something to keep in mind is that my English-language search found these papers, but
there could be other Russian-language papers in the references of the papers that my search did not hit.

16:58:35 <midipoet> can i quickly raise something on my own CCS before we move off them?

16:58:53 <plowsof> sure, whats happening

16:59:00 <midipoet> My own CCS is at ‘Work in Progress’ stage: https://ccs.getmonero.org/proposals/midipoet-
Oslo_Freedom_Forum_CCS_proposal.html

16:59:11 <midipoet> I have travelled to the event, and delivered a report:
https://www.reddit.com/r/Monero/comments/v18o78/ccs_report_midipoet_at_the_oslo_freedom_forum/

16:59:12 <plowsof> should be completed?

16:59:45 <midipoet> well, no. I had planned to be involved in a podcast, reporting on the event as a follow-up
to a podcast I did last year, but this will no longer be happening.

16:59:55 <midipoet> I had also planned to distribute flyers at the Oslo event - and this did not happen
(mainly as I was advised against it on the original CCS and also privately on IRC).

17:00:13 <midipoet> With this in mind, I propose to refund a portion of the CCS to the General Fund (i.e.,
refund the initially projected cost of the prep for the podcast and the cost of the initially proposed flyer
printing). This is because the originally planned work could not/was not completed. As per the CCS rules, the
XMR attributed to this work should get refunded to the GF.

17:00:31 <midipoet> The second payout is supposed to be 4.25 XMR. I propose refunding 2 XMR to the GF, which
equates to roughly €300 at current rates (€100 for the printing, and €200 for the four hours prep time for the
podcast).

17:00:46 <plowsof> thank you for the full disclosure

17:00:49 <midipoet> The remaining balance (2.25 XMR) will be paid out to me.

17:00:58 <luigi1111w> this is acceptable to me

17:01:03 <midipoet> cool. thanks

17:01:05 <plowsof> +1

17:01:24 <luigi1111w> midipoet can you write in the original mr your proposal? I'll do the payouts then

17:01:28 <plowsof> - MSvB - Hackers Congress Paralelní Polis (HCPP) 2022  https://last-shot.hcpp.cz/ — MSvB
and SethForPrivacy are named speakers at the event - *September 30- October 2, 2022*

17:01:43 <midipoet> luigi1111w: yes - will do

17:01:58 <Rucknium[m]> Don't we have dangerousfreedom proposal and the sudo shop?

17:02:17 <msvb-web> I have no well prepared presentation @plowsof, just reminding that the hackers conference
of Paralelni Polis (HCPP) is next week.

17:02:25 <msvb-web> The official direction has cancelled all Monero technology from the conference,

17:02:25 <msvb-web> but the good news is that fiat is cancelled as well. There is a strong presence

17:02:25 <msvb-web> of Bitcoin, Litecoin, Ethereum, and the official currency system is Lightning.

17:02:30 <msvb-web> We did this due to lack of participation and a lot of Bitcoin groups wanting the

17:02:30 <msvb-web>  opportunity that Monero usually abandons.

17:02:35 <plowsof> MRL have endorsed DF;s proposal, i see no issue from moving forward with it

17:02:36 <msvb-web> Other good news is that electronic badges produced for the conference are fully

17:02:36 <msvb-web> open, meaning that the Bitcoin logic stored on them can be replaced with Ethereu

17:02:36 <msvb-web> m, Monero, or any other currency technology.

17:02:58 <msvb-web> For example, if anybody stops by the badge clinic, we can show how to replace the Bitcoin
logic with Monero.

17:03:14 <plowsof> thanks msvb-web, safe journey to/from and good luck!

17:03:20 <escapethe3ra[m]> msvb-web message me the details, if you have more for a MO report, or at least a
community message

17:03:42 <msvb-web> I can try to make something in one paragraph escapethe3ra[m], suitable for the Observer
yes.

17:03:55 <escapethe3ra[m]> great

17:04:19 <luigi1111w> sudo shop

17:04:44 <msvb-web> Any questions about HCPP, or the cryptocurrencies participating there? It's off the topic,
because no Monero. So we can continue to the next topic.

17:04:53 <monerobull[m]> The idea is obviously great but i don't know to much about the devs

17:05:08 <plowsof> they have been working on it for years at least

17:06:07 <ajs_[m]> there has been a few proposals over the years to make a monero market, but none have panned
out. i am skeptical this would be any different.

17:06:09 <monerobull[m]> Idk about the web of trust thing. Do we have any idea how desnakes project might work
in regards to this?

17:06:27 <luigi1111w> I'm a bit leery about funding such an endeavor through ccs

17:07:04 <luigi1111w> also is its plan to be revenueless?

17:07:12 <monerobull[m]> Yeah

17:07:19 <monerobull[m]> Decentralized marketplace

17:08:04 <monerobull[m]> I think they said something about monetizing in the future but keep free listings

17:08:04 <plowsof> are we feeling another dust collector in "work in porgress"? the devs are atleast putting
the effort in, 3 years old https://gitlab.com/beardog/Onionr

17:08:09 <Rucknium[m]> IMHO, with things like this building the userbase is harder than building the app. You
need a buyer and a seller for the same set of goods/services. Very hard to generate the networl effect.

17:08:56 <monerobull[m]> Rucknium[m]: Not if it allows drugs... ._.

17:09:33 <hinto[m]> luigi1111w: fixed the formatting, is it ok now?

17:09:48 <hinto[m]> also changed the payout from monthly -> only upon full completion if thats ok with
everyone

17:10:18 <luigi1111w> yes I like that better

17:10:28 <ajs_[m]> -1

17:11:02 <plowsof> better yep

17:12:10 <monerobull[m]> Sure a decentralized marketplace based on xmr would be nice to have for circular
economy but I'm not sure if we should fund it

17:12:38 <monerobull[m]> Especially if desnake is really working on something already

17:13:16 <monerobull[m]> Let the free market spawn markets 👀

17:13:36 <midipoet> the web of trust system (milestone 1) might be good for other p2p efforts - especially
atomic swaps/dex. could we just ask for that to be completed first, so we can gauge quality/uptake?

17:14:17 <Rucknium[m]> v1docq47: A few Russian-language papers that mention Monero:
https://elibrary.ru/item.asp?id=49057736 https://elibrary.ru/item.asp?id=46572705

17:14:24 <luigi1111w> wot is more innocuous

17:14:27 <monerobull[m]> monerobull[m]: Security and privacy are expected to be better just out of necessity

17:16:14 <v1docq47> Rucknium[m]: tnx

17:16:40 <plowsof> i have to pop out so i will say my thanks and goodbyes, enjoy the rest of your evening all


```
Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)


```
17:18:30 <luigi1111w> thanks plowsof let's call it here
17:19:23 <midipoet> i left a comment on the forgotsudo MR asking about breaking it up into smaller projects
17:19:52 <msvb-web> Great meeting everyone, and thanks to plowsof for organising it.
17:19:53 <luigi1111w> thanks
17:20:46 <v1docq47> however, I did not quite understand what result we came to in the key of my CCS proposal
17:21:23 <Rucknium[m]> v1docq47: Another one: https://uprav-uchet.ru/index.php/journal/article/view/1699
17:21:50 <Rucknium[m]> That is the one that says, "The article discusses cryptomonets with increased anonymity ZCASH and DASH in terms of those criminal risks that entail data digital assets. The author notes that both projects are noticeably inferior to the Monero cryptoactive both in popularity and in technical development."
17:25:20 <luigi1111w> v1docq47 no conclusion yet
17:31:15 <v1docq47> can i somehow help in solving this conclusion, or does nothing depend on me here?
17:32:23 <luigi1111w> seeking more feedback, esp from those who might consume this content would be great
```

# Action History
- Created by: plowsof | 2022-09-21T12:15:07+00:00
- Closed at: 2022-09-24T18:33:53+00:00
