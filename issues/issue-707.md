---
title: 'Monero Community Workgroup Meeting: Sunday 29th May 2022 @ 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/707
author: plowsof
assignees: []
labels: []
created_at: '2022-05-20T12:33:15+00:00'
updated_at: '2022-05-29T19:28:19+00:00'
type: issue
status: closed
closed_at: '2022-05-29T19:26:40+00:00'
---

# Original Description
Location: [Libera.chat, #monero-community](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-community:monero.social?via=matrix.org&via=monero.social)

[Instructions for joining the monero.social Matrix server.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time
18:00 UTC [Check your timezone](https://www.timeanddate.com/countdown/wrestling?iso=20220529T18&p0=1440&msg=Monero+Community+Workgroup+Meeting&font=sanserif)

Moderator: plowsof

Please reach out in advance of the meeting if you would like to propose an agenda item.

Proposed Meeting Items:

1. Introduction
2. Greetings
3. Community highlights    
News: [Monero Observer](https://www.monero.observer/) - [Monero Moon](https://www.themoneromoon.com/) - [Revuo Monero](https://revuo-xmr.com/) - [The Monero Standard](https://localmonero.co/nojs/the-monero-standard/)
    -SethForPrivacy helping with the HF with simple [testnet monerod nodes](https://www.reddit.com/r/Monero/comments/utzyyz/help_test_out_the_upcoming_monero_network_upgrade/) and he made a [BTCpay server guide](https://sethforprivacy.com/guides/accepting-monero-via-btcpay-server/) for Monero
    -Ditatompel adds 'fee estimate' to [node list](https://www.ditatompel.com/monero/remote-node)
    -[HackLiberty](https://status.hackliberty.org/status/hackliberty) adds Tor remote nodes (Stagenet also)
    -[P2Pool is growing!](https://www.reddit.com/r/Monero/comments/urh3oe/p2pool_is_growing/)
    -[Monero.fail](https://monero.fail) adds 'Web compatible' (usable for browser wallets such as HotShop
    -RINO willing to partly fund an audit for multisig fix [#8149](https://github.com/monero-project/monero/pull/8149)
    -XMR<->ETH [Atomic swaps on stagenet](https://www.reddit.com/r/Monero/comments/ux6lzk/ethxmr_atomic_swap_development_update_live_on/)
    -Twitter Space to discuss the forthcoming network upgrade on July 16th! [Listen to the recording here](https://twitter.com/monero/status/1529482668097916929) 
4. [CCS updates](https://ccs.getmonero.org/) Previously discussed open ideas can be re-discussed, just ask!
  a. [Moneroj.net improvements, articles and maintenance (3 months)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/318)    
  b. [XMR BTC Atomic Swaps Desktop GUI - Continued development](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/321) | [reddit thread](https://www.reddit.com/r/Monero/comments/uybc5n/ccs_proposal_xmrbtc_atomic_swaps_gui_desktop_app/)  
  c. [jeffro256: part-time dev work 2022Q3](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/319)    
5. Workgroup reports    
  a. Dev workgroup
  b. Localization workgroup
  c. Outreach workgroup
  d. Events workgroup
    -#708
    -#705
  e. Website workgroup
  f. Policy workgroup
  g. Research workgroup
    -#709
    -#706
6. Open ideas time    
  -Interested in NFC / Badge Monero payments? contact msvb-labs .
8. Confirm next meeting date/time    

[Previous meeting including logs](https://github.com/monero-project/meta/issues/704)    

Meeting logs will be posted here afterwards.   

# Discussion History
## plowsof | 2022-05-29T19:26:39+00:00
Logs 
```
18:02:03 <plowsof[m]> Alot of activity here, just in time for the meeting :D https://github.com/monero-project/meta/issues/707
18:02:20 <plowsof[m]> 2. Greetings 
18:02:21 <msvb-web> Hello.
18:02:24 <plowsof[m]> Hello everyone!
18:02:42 <binarybaron[m]> Hello
18:02:42 <spackle_xmr[m]> Hello
18:02:43 <monerobull[m]> Hi
18:02:48 <Morpheus[m]> Hi
18:02:51 <selsta> hi
18:03:24 <plowsof[m]> Thanks for joining us, lets just go over some of the events that happened since the last meeting ~2 weeks ago 
18:03:31 <Rucknium[m]> Hi
18:03:53 <plowsof[m]> the usual news sources: News: [Monero Observer](https://www.monero.observer/) - [Monero Moon](https://www.themoneromoon.com/) - [Revuo Monero](https://revuo-xmr.com/) - [The Monero Standard](https://localmonero.co/nojs/the-monero-standard/)
18:04:26 <plowsof[m]> Firstly i just wanted to thank SethForPrivacy for helping with the HF with simple [testnet monerod nodes](https://www.reddit.com/r/Monero/comments/utzyyz/help_test_out_the_upcoming_monero_network_upgrade/) and he made a [BTCpay server guide](https://sethforprivacy.com/guides/accepting-monero-via-btcpay-server/) for Monero
18:05:12 <plowsof[m]> Ditatompel adds 'fee estimate' to [node list](https://www.ditatompel.com/monero/remote-node)
18:06:34 <plowsof[m]> -[Monero.fail](https://monero.fail) adds 'Web compatible' (usable for browser wallets such as HotShop 
18:07:12 <plowsof[m]> and p2pool has been growing, ALOT 
18:07:18 <plowsof[m]> we even have XMR<->ETH [Atomic swaps on stagenet](https://www.reddit.com/r/Monero/comments/ux6lzk/ethxmr_atomic_swap_development_update_live_on/)
18:07:42 <plowsof[m]> RINO willing to partly fund an audit for multisig fix [#8149](https://github.com/monero-project/monero/pull/8149)
18:08:48 <plowsof[m]> "web compatible" column in monero.fail for website wallets.. there has been alot of news in the last 2 weeks. would anyone like  to talk about anything on their minds?
18:09:10 <monerobull[m]> Majestic bank kinda goofed up 
18:09:26 <msvb-web> Rino is looking very good, especially for those of us who prefer not using web wallets but want the convenience.
18:10:07 <plowsof[m]> Majestic bank giving away 40 free tickets to Monerokon 
18:11:08 <monerobull[m]> They have good intentions but they executed it without putting much thought into it
18:11:57 <plowsof[m]> Hopefully Monerokon has a great turnout. The events team are nothing but professional in their planning 
18:12:49 <plowsof[m]> will jump into ccs ideas if no one wishes to bring some events up 
18:13:29 <monerobull[m]> I am once again asking for the closure of Afghanistan expansion strategy ccs
18:14:43 <plowsof[m]> noted. spirobel is currently reinventing that proposal / resubmitting it i believe, so we await the new one. (will touch on it again later)
18:15:54 <plowsof[m]> We have binarybaron and morpheus with us i believe to discuss their current proposals 
18:16:00 <plowsof[m]> 4. [CCS updates](https://ccs.getmonero.org/)
18:16:29 <Morpheus[m]> Yep I'm here guys
18:16:29 <plowsof[m]> [Moneroj.net improvements, articles and maintenance (3 months)](https://repo.getmonero.org/monero-project/
18:16:34 <binarybaron[m]> Me too
18:16:40 <plowsof[m]> Thanks!
18:16:53 <plowsof[m]> lets discuss moneroj.net first 
18:16:59 <plowsof[m]> thje proposal has changed slightly 
18:17:20 <plowsof[m]> Morpheus has created 10 new charts from his CCS list, and also split it in half as a sign of good faith. so if the new proposal is funded, a 2nd one would be made for further work.
18:17:51 <plowsof[m]> sorry , here is the link to the proposal https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/318
18:18:14 <monerobull[m]> Morpheus: is there any way the site could get speed up with more funding? Some charts take quite some time to load
18:18:44 <Morpheus[m]> Yes, I intend to use a better server, and I need funding to spend some time working on the database
18:19:14 <Morpheus[m]> The website should take less than a second to load when everything is done
18:19:26 <selsta> is the amount 35 or 70?
18:19:27 <Rucknium[m]> Morpheus: You mention that having an onion hidden service would be difficult. In my experience, it is quite easy. Just adjust some config options in NGINX and get `tor` running. SethForPrivacy has a guide on his blog. I think you may be able to do it without much additional work.
18:19:29 <ofrnxmr[m]> "New server, fix bugs, loading speed, improve the interface and build new charts
18:19:29 <ofrnxmr[m]> I need to invest into a new, improved and faster server;
18:19:29 <ofrnxmr[m]> "
18:20:11 <Morpheus[m]> Rucknium[m]: Cool, I can try that too in the future. Can I talk to you about this when It's time?
18:20:26 <Morpheus[m]> I would like some tips too
18:20:32 <plowsof[m]> amount is now 35 - with a 2nd proposal for another 35 after 1st complete
18:21:12 <sethforprivacy> Morpheus[m]: Ping me when the time comes, happy to help you get a hidden service setup 🙂
18:21:23 <plowsof[m]> ooo123 don't worry we are discussing jeffros ccsd, after the atomic swaps gui
18:21:29 <ofrnxmr[m]> Is the proposal split? Or a second proposal is a new proposal 
18:21:43 <Morpheus[m]> sethforprivacy: I'll certainly ping you. Thanks a lot
18:22:34 <plowsof[m]> i suggested to split it into 2 proposals if the community had an issue with a 1st ccs being for higher amounts
18:22:48 <selsta> is it a static website?
18:22:54 <escapethe3ra[m]> Morpheus: you can also ping me if Seth is busy at the time, I recently created a hidden service for MO and can help as well
18:23:01 <plowsof[m]> if 1st proposal is funded and everyone is happy, the 2nd proposal would also be funded 
18:23:14 <Rucknium[m]> Morpheus: Sure, no problem. My other comments are that the website seems quite focused on Monero as a speculative investment. That's not my cup of tea, but I know that it is some people's cups of tea, so it's OK I suppose. Also, I think you refer to Gresham's law in the text of the website, but misapply it IMHO.
18:23:42 <monerobull[m]> Rucknium[m]: The charts make me feel better about buying xmr lmao
18:23:55 <Morpheus[m]> ofrnxmr[m]: I split the original into two so people would be more comfortable. This is the first one, and it is about half the work of the original. Dont know if I'm being clear
18:24:11 <Rucknium[m]> Gresham's law deals with the case when the face value of coinage is the same but the coinage has different metal content value.
18:24:56 <monerobull[m]> Is there no other meaning?
18:24:56 <ofrnxmr[m]> At current prices, 35 and 70xmr is still a lot. (6-12k)
18:24:56 <ofrnxmr[m]> Would this require constant funding ?
18:25:12 <plowsof[m]> selsta : at the moment it is javascript site, but morpheus has attempted to reduce the amount of js required? 
18:25:13 <selsta> shouldn't we be careful with darknet related statistics?
18:25:27 <Morpheus[m]> escapethe3ra[m]: Thanks, I love your work
18:25:46 <monerobull[m]> selsta: It's arguably our niche
18:26:19 <Morpheus[m]> selsta: I run python to calculate the charts on the backend
18:26:34 <monerobull[m]> Morpheus: do you know any markets that currently accept ZCash?
18:27:26 <plowsof[m]> to clarify , you are asking for 35 xmr now. and then you will make another ccs of 35 xmr in the future?
18:27:26 <Morpheus[m]> > <@ofrnxmr:monero.social> At current prices, 35 and 70xmr is still a lot. (6-12k)
18:27:26 <Morpheus[m]> > 
18:27:26 <Morpheus[m]> > Would this require constant funding ?
18:27:26 <Morpheus[m]> No.. it's just because I have to put a lot of time to build the charts, after they are ready, the server costs are small
18:28:11 <Morpheus[m]> plowsof[m]: Yes, that's the idea, because there will still be a lot of work ahead if people want more data on the website, or more improvements
18:28:57 <selsta> I still think we should be careful with darknet related stats
18:29:42 <selsta> but the core team has to decide that in the end if they are ok with funding something like that on the CCS
18:30:02 <Morpheus[m]> selsta: I believe my mission is to provide information. The website should be transparent in that sense
18:30:06 <monerobull[m]> People who feel like they need to use the markets should know only xmr is safe
18:30:25 <Morpheus[m]> But I can understand your view, sure
18:30:57 <selsta> Morpheus[m]: yes, but if you directly or indirectly link to darknet markets this can cause issues if it's funded by the monero community
18:31:01 <Morpheus[m]> monerobull[m]: No, xD not yet
18:31:32 <monerobull[m]> selsta: Doesn't he just show dread subscribers?
18:31:46 <selsta> I'm going by what is says in the proposal
18:31:55 <selsta> Darknet adoption (DN markets, seft reported);
18:32:31 <ofrnxmr[m]> This is only for 45 days?
18:32:31 <ofrnxmr[m]> I have to vote no.
18:32:31 <ofrnxmr[m]> - same proposal but basically forced a second.
18:32:31 <ofrnxmr[m]> - rates are higher than researcher rates
18:32:46 <Morpheus[m]> selsta: Ah, ok, I understant now. Yeah, I wont lilnk anything about darknet on the website.
18:33:05 <mj-xmr[m]> selsta: So far the "regulators" have been really easy on us for some reason.
18:33:06 <selsta> there were websites that were raided that just linked to darknet markets
18:33:09 <Morpheus[m]> The only DN chart I built is about forum users, so that's ok I think
18:33:23 <selsta> the operators were raided to be precise
18:33:36 <monerobull[m]> 0.o
18:33:57 <Morpheus[m]> Yeah, you guys are right. I wont build the darknet markets chart, just leave the one I already built, which is about users on a Forum
18:34:06 <mj-xmr[m]> selsta: It's very important that you make us all aware of this.
18:34:40 <selsta> Morpheus[m]: what would be your hourly rate?
18:34:45 <monerobull[m]> Well linking to the .onion ala dark.fail is way different than having a chart that says alphabay: 500 vendors
18:34:53 <Morpheus[m]> selsta: Yeah, I can remove that. No problem.
18:35:49 <ofrnxmr[m]> selsta: About 1xmr per day, excluding weekends 
18:37:02 <selsta> ofrnxmr[m]: seems to be higehr than 1xmr
18:37:26 <selsta> it would be nice if you could more clearly write down the rate and hours planned to work per month
18:37:52 <selsta> unless i overread it
18:37:58 <Morpheus[m]> selsta: Being honest, I am already working 8 hours a day on this, because I have a lot of free time. For example I built 5 charts this week and worked yesterday the whole day, so I'm calculating around 6 hours a day at 21 usd / hour I think
18:38:31 <plowsof[m]> I think we have brought up all the relevant points for this proposal? (needs more discussion / input from core it seems ) we have 2 more to discuss 
18:38:56 <Morpheus[m]> Something around that. 5 hours a day isn't that hard for me, because I like working on my project
18:39:06 <selsta> Morpheus[m]: ok, would be great if you could clarify it in the CCS and so that it is possible to see how you calculated the 35 XMR
18:39:26 <Morpheus[m]> Ok, no problem
18:39:45 <plowsof[m]> Right binarybaron 
18:40:31 <ofrnxmr[m]> Thats on 7 days per week.
18:40:31 <ofrnxmr[m]> 5 days Lee week is 34/hr
18:40:38 <ofrnxmr[m]> Per*
18:41:14 <Morpheus[m]> As I said, I work on weekends because that's something I like to do
18:41:53 <Morpheus[m]> Today I worked the whole morning, uploaded the new charts, etc
18:42:15 <plowsof[m]> This can be clarified and discussed again shortly. (the rates and such) lets move on to the other proposal. Thank you for taking the feedback on board Morpheus 
18:42:26 <Morpheus[m]> ok
18:42:34 <plowsof[m]> [XMR BTC Atomic Swaps Desktop GUI - Continued development](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/321) | [reddit thread](https://www.reddit.com/r/Monero/comments/uybc5n/ccs_proposal_xmrbtc_atomic_swaps_gui_desktop_app/)  
18:42:43 <monerobull[m]> Move
18:42:45 <monerobull[m]> Forward
18:43:29 <plowsof[m]> my 2 cents : As an outsider who has not used atomic swaps, i have only seen the support questions.. the thing where you have to 'do something' before 'x blocks / time' or you lose your funds because 'something happened' (e.g. technical issue or alice doesnt have enough funds). The process is not noob friendly at all.
18:43:29 <plowsof[m]> Part of the proposal is to tackle this issue so the cancel / refund will be made much easier. (people will be able to do it using the GUI / see a warning / timer)
18:43:53 <plowsof[m]> this is a 'new' proposal but has alot of updoots on reddit 
18:45:51 <ajs_[m]> wasn't atomic swaps abandoned by the comit team?
18:45:53 <plowsof[m]> i was assured that it would 'work' after the hard fork. but one thing we must consider is that comit is officially 'not maintained' 
18:46:00 <selsta> ajs_[m]: yes, that's what i thought too
18:46:17 <monerobull[m]> Doesn't binarybaron maintain it with 2 others
18:46:18 <plowsof[m]> and this proposal is 4 months funding into the future 
18:46:20 <monerobull[m]> Unpaid
18:46:42 <ofrnxmr[m]> 150xmr for an interface
18:46:42 <ofrnxmr[m]> is comparable to haveno
18:46:42 <ofrnxmr[m]> But the backend isnt maintained and this is only maintenance 
18:46:47 <plowsof[m]> in the ccs proposal they state 5% or so of time may be fore actuall pull requests to the 'swap_cli'
18:46:52 <ajs_[m]> https://github.com/comit-network/xmr-btc-swap/commits/master
18:47:45 <plowsof[m]> are we funding a gui for an abandonned project when we could fund him to make a gui for 'farcaster' ? is my only concern 
18:48:38 <monerobull[m]> Just curious but did Farcaster do anything in the last 6 months? 
18:48:45 <selsta> yes https://github.com/farcaster-project/farcaster-node/commits/main
18:49:25 <monerobull[m]> Ok 👌
18:49:34 <ajs_[m]> they are presenting stuff at monerokon
18:50:20 <ajs_[m]> and have a workshop on using farcaster
18:50:27 <plowsof[m]> binarybaron assures that the atomic swaps are functional though and will continue to be after the hard fork , its just a concern about its 'not maintained status' - but the popularity of the proposal / people willing to donate is clear
18:51:37 <selsta> how dependent would the gui be on swap-cli from comit?
18:52:00 <ajs_[m]> could it work on farcaster?
18:52:40 <plowsof[m]> good question(s) will pass these on to baron 
18:53:35 <plowsof[m]> the meeting might extend passed the hour to discuss the jeffro proposal (if we have devs in here to discuss it)
18:53:44 <selsta> also for his CCS it would be good to write down the rate and approx worked hours per week
18:54:05 <plowsof[m]> more clarification of rates again, yep
18:54:28 <ofrnxmr[m]> I dont think we should be funding a ui for a separate project that is dead/unmaintained and mostly benefits people that need to get rid of dirty bitcoin 
18:54:28 <ofrnxmr[m]> If a ui for farcaster, then you can compare to haveno.
18:54:28 <ofrnxmr[m]> But if comit is in limbo..
18:54:41 <ofrnxmr[m]> 37xmr/month to maintain an existing up
18:55:12 <plowsof[m]> ok lets take the gloves off and let oo123  jump into the jeffro proposal. he has been very patient 
18:56:05 <plowsof[m]> [jeffro256: part-time dev work 2022Q3](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/319)  
18:56:47 <selsta> support from my side, with focus on gui, rpc, protocol spec
18:57:28 <plowsof[m]> oo123 , if you consider point number 10 to be the most controversial, we have assurance that he is gong to 'leave it alone' / not do drastic changes 'just because' 
18:57:55 <plowsof[m]> i would love if jeffro focussed on the gui with selsta / community node list
19:02:20 <plowsof[m]> damn, thanks mj !
19:03:00 <mj-xmr[m]> jeff vs oo000.
19:03:00 <mj-xmr[m]> Fight.
19:03:48 <plowsof[m]> Thank you all for joining btw, we're just waiting for everyone to voice their concerns on jeffros proposal. MoneroObserver put up their proposal today also.
19:04:39 <ooo123ooo1234567> > <@mj-xmr:matrix.org> 1st milestone and a Minimal Viable Product of SolOptXMR:... (full message at https://libera.ems.host/_matrix/media/r0/download/libera.chat/27591763725baf154604a624eed2b4b5f16a0292)
19:04:53 <ooo123ooo1234567>  * What was the hardest / the most time consuming part in that work ? What's the nutshell of that work ? What would be included into mvp without fluff to simulate working hours ?
19:05:02 <plowsof[m]> :( ok thats not about jeffro 
19:05:14 <ooo123ooo1234567> > <@mj-xmr:matrix.org> 1st milestone and a Minimal Viable Product of SolOptXMR:... (full message at https://libera.ems.host/_matrix/media/r0/download/libera.chat/4a82a022ec7a5498766d23f9e916c745eccf8c69)
19:05:26 <ooo123ooo1234567> And the same steps for the next milestones ?
19:05:36 <mj-xmr[m]> ooo123ooo1234567: They were all pretty hard. There were just a few easy parts.
19:05:36 <mj-xmr[m]> I don't understand the 2nd part of your question.
19:06:16 <mj-xmr[m]> ooo123ooo1234567: Yes. There's a Quickstart section in the README.md from the start for a reason. Have you tried?
19:06:41 <ooo123ooo1234567> mj-xmr[m]: Ok, can pull steps from README.md and put them into list under your proposal ?
19:06:47 <ooo123ooo1234567> So that anyone can verify what you've done
19:06:52 <ooo123ooo1234567> now and any time later
19:07:17 <ooo123ooo1234567> And learn from you how to simulate 96 hours from few python libs
19:07:32 <mj-xmr[m]> ooo123ooo1234567: Always the same way - run the quickstart steps. I care about documenting my stuff and I'm happy for a constrictive criticism.
19:07:45 <ooo123ooo1234567> Your fiction literature docs leave for incompetent people who will read/write/or even use that code
19:07:59 <ooo123ooo1234567> * who will not read/write/or even
19:07:59 <mj-xmr[m]> ooo123ooo1234567: No, thanks. Be a manager of your own project.
19:08:19 <mj-xmr[m]> ooo123ooo1234567: Aye. Continue living in a DisneyLand.
19:08:20 <ooo123ooo1234567> mj-xmr[m]: community proposals are supposed to be verifiable
19:08:26 <mj-xmr[m]> Mine is.
19:08:42 <ooo123ooo1234567> mj-xmr[m]: List concrete steps under your proposal, ideally with hours split
19:08:43 <plowsof[m]> Unrelated but : NFC is cool msvb-labs is knowledgeable on this, had some great discussions the other day. (also monerujo has nfc functions), cryptogrampy is busy with hotshop :D
19:08:46 <mj-xmr[m]> OK guys, just tell me when you want to switch subject :)
19:08:50 <cryptogrampy[m]> ooo123ooo1234567: WOULD ENJOY SOME STIMULATION OF MY PYTHON LIB
19:09:05 <cryptogrampy[m]> sorry hi I'm here at this meeting
19:09:24 <msvb-web> If there are questions about implementing NFC interactions in hardware, I will try to answer.
19:09:27 <mj-xmr[m]> oh hi! How's life? :)
19:09:49 <ooo123ooo1234567> mj-xmr[m]: Don't jump from topic
19:10:21 <mj-xmr[m]> I don't want to be annoying, but I think you don't realize, that you're attracting a bit too much attention now.
19:10:24 <cryptogrampy[m]> NFC instant payment is a nogo for HotShop FYI.  discussed with a couple people and wallet 1's viewkey/primary will not be able to generate an offline unsigned tx for wallet 2 (customer) to sign offline and send back via NFC for monero technical reasons
19:10:25 <ooo123ooo1234567> python is the easiest language, there are many people who can code in it; please, describe how to verify your work; others want to learn
19:10:38 <plowsof[m]> would you benefit from a developer 'mocking' up the workflow of a monero transaction using an NFC badge msvb-labs , or , are the steps involved known? 
19:10:48 <cryptogrampy[m]> wallet 1 would need wallet 2's primary/view key to generate an unsigned payment
19:11:46 <monerobull[m]>   Before I go through the hassle of submitting a proposal, would anyone support giving me 15 xmr to subsidize 100 1.75kg boxes of stickers? Right now there are only 5 more subsidized packages available 🥺
19:11:49 <cryptogrampy[m]> If anyone can get luigi1111  on the phone though, Milestone 2 is complete- i'd like to have the payment go to my grandson's monero address.  I've been getting some amazing feedback for completing Milestone 3. 
19:11:53 <mj-xmr[m]> ooo123ooo1234567: OK. I verify it by monitoring the battery drain. If you are presented with a solution that shows you, that the battery charge goes below it's declared minimum, then I failed my milestone.
19:13:03 <msvb-web> I would not benefit from that plowsof[m], no.
19:13:05 <mj-xmr[m]> cryptogrampy[m]: I usually text him directly on such issues. He reacts after max 2 days.
19:13:23 <cryptogrampy[m]> plowsof[m]: no, there's literally no way for a PoS to generate an unsigned tx for someone's random offline wallet without some custodial magic involved, or someone learning the view key of the customer.
19:13:44 <ofrnxmr[m]> monerobull[m]: Open a proposal for 70xmr 
19:13:57 <monerobull[m]> The way of the ccs kek
19:14:55 <plowsof[m]> ok i think we can call the meeting over at 15~ mins passed the hour, apologies as we still have some loose ends to tie up , thank you all for attending 
19:14:59 <ooo123ooo1234567> mj-xmr[m]: Concrete steps under each milestone how to verify that it was reached; not here, in your proposal
19:15:21 <mj-xmr[m]> ooo123ooo1234567: OK.
19:15:53 <cryptogrampy[m]> If anyone has HotShop recommendations though- that they would like to see added into Milestone 3 release, please feel free to ping me. 
19:16:20 <cryptogrampy[m]> I would still really appreciate it if anyone could get a web-compatible public node up and running.  *cough* Seth For Privacy  *cough*
19:16:57 <mj-xmr[m]> ooo123ooo1234567: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/299#note_16611
19:17:12 <cryptogrampy[m]> https TLS + rpc-access-control-origins=* in your node config.  
19:17:47 <ooo123ooo1234567> mj-xmr[m]: Concrete steps for each milestone without recursion or any links
19:17:56 <plowsof[m]> meeting adjourned, i can now go back to reading reddit and watching youtube and get  popcorn to read ooo123 , my guilty pleasure 

```
tail end
```
19:18:03 <ofrnxmr[m]> Is https working ok for you? Or did you have to use Arleta's master-beta
19:18:04 <ooo123ooo1234567>  * self-contained concrete steps for each milestone without any links
19:18:08 <mj-xmr[m]> I don't repeat myself.
19:18:09 <cryptogrampy[m]> * node config.  Tor nodes only need the rpc-access-control-origin=* flag- please don't add https to your tor node.
19:18:10 <ofrnxmr[m]> Selsta
19:18:52 <plowsof[m]> so an NFC badge ... would need to 'give' its view key when swiping..
19:18:58 <cryptogrampy[m]> ofrnxmr[m]: hard to say.  I haven't seen any crazy stuff with leaking memory usage or CPU, but I have had to restart the node a couple times.
19:19:10 <cryptogrampy[m]> I'm using the regular node
19:19:10 <plowsof[m]> the PoS would need to... ok im lost 
19:19:41 <cryptogrampy[m]> i did try building selstas with some modifications to seth's dockerfile to no avail.  have to look a little closer i guess
19:19:43 <ofrnxmr[m]> cryptogrampy[m]: Yeah, after I would make a few https connections my node would stop accepting connections and would have to restart 
19:19:44 <msvb-web> Good meeting and great moderation plowsof[m], dankon.
19:20:02 <SerHack> Thanks for the meeting
19:20:08 <selsta> ofrnxmr[m]: yes?
19:20:25 <selsta> for now i'm not sure about the security implications of running with `rpc-access-control-origin=*´ so I don't have it on my nodes
19:20:45 <Morpheus[m]> <ofrnxmr[m]> "Open a proposal for 70xmr..." <- What do you recomend I do? I'll indeed put as many hours into it as possible, and I'll probably deliver way mone than what is in the proposal. I'm fine with criticism, that's good. Do you happen to like my work? 
19:20:45 <mj-xmr[m]> msvb-web: Yes thanks. Love that proto-German too.
```
Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: plowsof | 2022-05-20T12:33:15+00:00
- Closed at: 2022-05-29T19:26:40+00:00
