---
title: 'Monero Community Workgroup Meeting: Sunday 15th May 2022 @ 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/704
author: plowsof
assignees: []
labels: []
created_at: '2022-05-11T21:49:49+00:00'
updated_at: '2022-05-15T19:16:50+00:00'
type: issue
status: closed
closed_at: '2022-05-15T19:07:53+00:00'
---

# Original Description
Location: [Libera.chat, #monero-community](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-community:monero.social?via=matrix.org&via=monero.social)

[Instructions for joining the monero.social Matrix server.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time
18:00 UTC [Check your timezone](https://www.timeanddate.com/countdown/vote?iso=20220515T18&p0=1440&msg=Community+Workgroup+Meeting&font=sanserif)

Please reach out in advance of the meeting if you would like to propose an agenda item.

moderator: plowsof
Proposed Meeting Items:

1. Introduction
2. Greetings
3. Community highlights    
News: [Monero Observer](https://www.monero.observer/) - [Monero Moon](https://www.themoneromoon.com/) - [Revuo Monero](https://revuo-xmr.com/)
* 255 p2pool miners paid [here](https://xmrchain.net/tx/d0c3d1efa68b78aa49839177d91228a61f4d399f6ba71e655ea8a51e359bc519)
* 5XMR bounty from xmrvsbeast for bounties bot rework/fix. C# remake [here](https://www.reddit.com/r/Monero/comments/upi39o/monero_bounties_service_rewrite/)
* Community node list for the Monero GUI in Simple Mode
* MO maintainer statement reg. [source](https://www.reddit.com/r/Monero/comments/uohuns/comment/i8hxtox/?utm_source=share&utm_medium=web2x&context=3)
* [Shruum wallet](https://git.mayumi.one/mayumi/shruum) (Monerujo fork) [telegram](https://t.me/shruumwallet) ( [juicysims](http://juicysms.com/) for 1 off ~50 cent in XMR sms *consider the tg account one time use as recovery not possible)
4. [CCS updates](https://ccs.getmonero.org/)
   a. [Research Computing Upgrade](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/317)
   b. [Moneroj.net improvements, articles and maintenance (3 months)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/318)
6. Workgroup reports    
  a. Dev workgroup
      -Prev logs #703 
  b. Localization workgroup
  c. Outreach workgroup
  d. Events workgroup
      -Prev logs #701 
  e. Website workgroup
  f. Policy workgroup
  g. Research workgroup
      -Prev logs #702 
7. Open ideas time    
9. Confirm next meeting date/time    

[Previous meeting including logs](https://github.com/monero-project/meta/issues/695)    

Meeting logs will be posted here afterwards.    

# Discussion History
## plowsof | 2022-05-15T19:07:52+00:00
Logs 
```
18:01:04 <plowsof[m]> 2. Greetings 
18:01:09 <plowsof[m]> hello
18:03:03 <Rucknium[m]> Hi
18:04:02 <plowsof[m]> ill just plug some things we discussed earlier while we wait for people to roll in 
18:04:09 <w[m]> Greetings
18:05:01 <ofrnxmr[m]> Good aftermorning 
18:05:27 <r4v3r23[m]> sup
18:05:28 <plowsof[m]> Monero Observer is now open [source](https://www.reddit.com/r/Monero/comments/uohuns/comment/i8hxtox/?utm_source=share&utm_medium=web2x&context=3)
18:05:33 <plowsof[m]> hii
18:06:13 <plowsof[m]> 3. Community highlights    
18:06:47 <plowsof[m]> devs are all busy with the upcoming testnet fork tomorrow 👀
18:07:56 <plowsof[m]> is there anything on the tip of anyones tongue (other than what was discussed earlier today) 
18:08:19 <ofrnxmr[m]> Multisig needs reviews
18:08:19 <ofrnxmr[m]> If anyone knows anyone, there are a few bounties on haveno as well
18:08:58 <ofrnxmr[m]> 2@2500$ and a few in the 500-1000 range
18:09:16 <plowsof[m]> true, it was nice to see that instead of 'being disabled' ~ moneromoo is working on adding it in but , off by default , with some warnings when enabled 
18:09:19 <w[m]> Pinging spirobel: 
18:09:38 <ofrnxmr[m]> Moo is too fast. Already finished
18:10:09 <plowsof[m]> for someone that says he is not involved in monero anymore he is sure doing alot of work still 
18:10:25 <plowsof[m]> thanks moo
18:10:39 <ofrnxmr[m]> https://github.com/monero-project/monero/pull/8328
18:11:08 <plowsof[m]> Amazing thanks!
18:12:12 <plowsof[m]> Not sure how the 5xmr bounty is progressing to 'fix the bounties site' ~ but the wheels are in motion and a c# implementation was made with alot of improvements [here](https://www.reddit.com/r/Monero/comments/upi39o/monero_bounties_service_rewrite/)
18:12:44 <plowsof[m]> we wouldn't have had viewtags implemented for the next HF if it wasn't for the bounties site 
18:14:22 <plowsof[m]> can also touch on the community node list. i set up a little experiment and made 2500~ transactions from around 800 nodes, with no high fees found 
18:14:56 <plowsof[m]> sech1 suggests that it is possible an attacker can perform a 'pop up shop' attack where they rent hash power , throw a malicious node up , and mine the block containing the high fee 
18:15:12 <plowsof[m]> a community node list would prevent this 
18:15:19 <plowsof[m]> for simple mode gui users
18:16:18 <monerobull[m]> plowsof[m]: I read about the malicious node just not broadcasting the transaction until he mines the high fee block himself, could that actually work?
18:16:36 <ofrnxmr[m]> I believe so.
18:16:38 <monerobull[m]> That way they are WAY more likely to benefit from the high fees
18:17:10 <plowsof[m]> interesting, ill follow that up and ask sech about it 
18:19:01 <plowsof[m]> as always, community events can be found on these news sites [Monero Observer](https://www.monero.observer/) - [Monero Moon](https://www.themoneromoon.com/) - [Revuo Monero](https://revuo-xmr.com/)
18:20:08 <ofrnxmr[m]> I think a community list for GUI is ideal.... (full message at https://libera.ems.host/_matrix/media/r0/download/libera.chat/fdddbada04346ce5b094cd94d7e83d8820b47cc0)
18:20:22 <plowsof[m]> yep feather too
18:20:42 <monerobull[m]> SerHack: someone told me the woocommerce gateway at checkout shows a slightly wrong xmrchain domain. It has one too many / and therefore is broken
18:21:26 <plowsof[m]> dont worry - they won't work after the HF 
18:21:50 <monerobull[m]> Hardfork will break the gateway?
18:22:15 <plowsof[m]> actually no, its using xmrchain and / or monero wallet rpc, ignore that
18:22:41 <plowsof[m]> ill make sure he hears about that bug thanks
18:23:02 <monerobull[m]> It's the link to xmrchain to view the transaction you just made.
18:23:43 <plowsof[m]> RIght , shall we jump into talking about some CCS ideas?
18:24:01 <w[m]> Spiro didnt make it :(
18:24:15 <monerobull[m]> <monerobull[m]> "I am once again asking for the..." <- :)
18:24:23 <plowsof[m]> 4. [CCS updates](https://ccs.getmonero.org/)
18:24:33 <plowsof[m]>    a. [Research Computing Upgrade](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/317)
18:25:36 <plowsof[m]> every time i read about some MRL research , its always ' gingeropolous let us use his server to do x y z' and now he is asking for some upgrades / maintenance fees 
18:26:08 <plowsof[m]> Ruckniumcurrent research will directly benefit. and has left comments on this ccs detailing some other projects it will help / gingeropolous has helped 
18:27:01 <plowsof[m]> and he offers all MRL members to use his resources.. i think its a no brainer ?
18:27:35 <monerobull[m]> Chainalysis probably has supercomputers so we should have them too.
18:28:17 <ofrnxmr[m]> If he's open to suggestion, id have one.
18:28:17 <ofrnxmr[m]> That be the distribution.
18:28:35 <plowsof[m]> dangerousfreedom has a ccs in progress now, but only has his laptop - an example of the benefits 
18:29:37 <ofrnxmr[m]> 30:27 is the current hardware to labour
18:29:37 <ofrnxmr[m]> but im bullish.
18:29:37 <ofrnxmr[m]> Id go 35:22 
18:29:37 <ofrnxmr[m]> 3months from now xmr price
18:29:54 <plowsof[m]> maths 🤔
18:30:10 <w[m]> Supercomputer go brr
18:30:33 <plowsof[m]> his rates could be better adjusted to account for current price drops?
18:31:08 <ofrnxmr[m]> He's requesting 57 xmr total
18:31:08 <ofrnxmr[m]> 30 for hardware 27 for labour over 3 months.
18:31:08 <ofrnxmr[m]> Id go 35 to 22, if not a problem 
18:31:28 <plowsof[m]> ah ok , i get you 
18:33:12 <plowsof[m]> the next CCS has some drama in the comments... 👀
18:34:02 <plowsof[m]>    b. [Moneroj.net improvements, articles and maintenance (3 months)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/318)
18:34:35 <plowsof[m]> the author is going to respond to the criticisms shortly though 
18:36:36 <plowsof[m]> one valid concern i have heard is that the website is focussed on monero price .. stock to flow things that are not actually 'proven' .. kind of like trade analysis , i'd rather the money was put into other research things 
18:36:51 <ofrnxmr[m]> Agree with majestic
18:37:41 <ofrnxmr[m]> 45 USD/hour? You should re-consider your hourly rate based on how much Monero core developers are paid to work on code that really matters. There is no guarantee neither reference that you are producing code not even on similar level.
18:37:53 <plowsof[m]> will have to wait for his rebuttal, its early days now, hopefully some things are changed / addressed 
18:38:12 <w[m]> This is where plowsof comes in
18:38:20 <w[m]> Stuff like that, imo, should be waas
18:38:23 <plowsof[m]> CCS's should be priced in 'selstas' 
18:38:30 <plowsof[m]> at a rate of 0.7 selstas per month
18:38:54 <w[m]> Even koe.
18:39:09 <plowsof[m]> indeed xd 
18:39:46 <w[m]> And what about poor old Seth 
18:40:06 <w[m]> I plan to get privacy-preserving statistics using Plausible (which has a monthly cost), the same way Seth does at https://sethforprivacy.com
18:40:44 <plowsof[m]> the final boss on twitter for anti monero people / privacy community leader / father of an undisclosed amount of monero nodes in the ecosystem? 
18:42:22 <ofrnxmr[m]> Also official ceo
18:43:16 <ofrnxmr[m]> For 5000/month, thats too much for a website ive yet to visit.
18:43:40 <ofrnxmr[m]> 5000 @ 175usd/xmr.
18:43:40 <ofrnxmr[m]> 87xmr total 
18:43:56 <plowsof[m]> and thats just 3 months.. theres more months in a year so im told
18:45:29 <w[m]> Anybody else have any input?
18:45:32 <plowsof[m]> spirobel isnt here to fight monerobull reg the afghan proposal
18:46:03 <w[m]> Spiro was here all night though. Saying rotten hero's the proposal
18:46:05 <monerobull[m]> There is no fight. It's a legitimately unneeded proposal
18:46:23 <w[m]> Veto*
18:46:36 <monerobull[m]> With plenty of feedback saying it's unneeded
18:47:05 <plowsof[m]> yeah , not much has happened since luigi asked to 'see something different' 
18:47:14 <plowsof[m]> otherwise it would be closed 
18:47:32 <ofrnxmr[m]> I *really* dont like the sound of
18:47:32 <ofrnxmr[m]> Im going to send 2300$ overseas to someone that I know. DW about it, they will be able to do something with it
18:48:05 <ofrnxmr[m]> 2300$ isn't enough to transform a neighborhood, nevermind an entire country.
18:48:14 <monerobull[m]> Translations need previous work
18:48:24 <monerobull[m]> Why should this work with "my gf will do it"
18:48:41 <plowsof[m]> objection your honour , speculation / hearsay 
18:48:46 <monerobull[m]> Dismissed
18:48:49 <plowsof[m]> thanks 
18:49:34 <plowsof[m]> yeah so the moneroj .net , is early days, lets wait for his rebuttal also 
18:49:51 <w[m]> I made my thought clear in monero chat
18:49:52 <w[m]> Its too of an amount (you can bankroll that yourself) and too vague and too much trust involved 
18:49:52 <w[m]> Waas. 
18:50:21 <plowsof[m]> spirobel could easily put his monero javascript wallet forward for ccs funding 
18:50:35 <w[m]> Regarding spirobel afganistan proposal
18:50:35 <w[m]> Too low* of an amount
18:51:17 <plowsof[m]> i hope he does make a ccs for the js wallet , the community would welcome that with open arms
18:51:34 <plowsof[m]> getting into the last 10 minutes now 
18:51:34 <w[m]> If it was a 1 man project, ok. But meena exists. Why is meena not in discussions. 
18:52:14 <plowsof[m]> 6. Workgroup reports    
18:52:32 <plowsof[m]> moneromoo is too quick.. already done what he promised reg multi sig warning lol 
18:53:43 <ofrnxmr[m]> "I havent contributed in months"
18:53:43 <ofrnxmr[m]> *checks GitHub*
18:53:43 <ofrnxmr[m]> moneromoo activity on 🔥
18:53:43 <monerobull[m]> Btw what makes a workgroup a workgroup? Am i in a workgroup?
18:53:43 <plowsof[m]> the events team have their Merch pack : (unfortunately names 'STD pack') but it seems nice: 'Merchpack STD': tshirt, bucket hat, cotton socks, carrying bag, lanyard, shoelaces, patch, screen cleaner, inkpen, USB drive, bandana, tattoo, cold storage, party wristband, plastic bottle.
18:54:05 <plowsof[m]> exactly^ lol i am all for paying him his open work in progress ccs 
18:54:43 <monerobull[m]> monerobull[m]: I do marketing you know
18:55:49 <plowsof[m]> monerobull has started some kind of fund to help 'monero guerrillas' purchase stickers to distribute them around their area  
18:55:58 <plowsof[m]> i guess you are in the outreach workgroup now
18:56:04 <monerobull[m]> plowsof[m]: https://www.reddit.com/r/Monero/comments/uq3s32/option_to_fund_guerrillas_get_funded_now_available
18:57:41 <plowsof[m]> looking forward to see how that goes.. also an idea of a map to show where they have been distributed?
18:58:41 <monerobull[m]> Yeah I've updated the privacy policy a little. Will probably do monthly/quarterly reports on the general region subsidized packages went to
18:59:17 <monerobull[m]> Because right now most orders go to Europe/ NA and not a lot of other places
18:59:31 <ofrnxmr[m]> Plowsof, care to repeat latest devel of waas
19:00:30 <plowsof[m]> WaaS is at the stage where it is 'dockerised' and you can just start it.. add .. edit.. remove wishes at will. 
19:01:09 <plowsof[m]> more info here https://github.com/plowsof/flipstarter-waas-wip (docs need improving)
19:02:20 <plowsof[m]> the hour has come to an end , i will make sure to include the logs of earlier chats today 
19:02:53 <ofrnxmr[m]> And current version supports
19:02:53 <ofrnxmr[m]> bch, xmr, and wow now?
19:02:53 <ofrnxmr[m]> Sooner or later I may try to take a crack at it. 
19:02:53 <ofrnxmr[m]> A cool feature would be donating hr 
19:03:42 <plowsof[m]> Let me know, always available to help. Thanks for joining everybody. 2nd time i've done this so bare with me. next meeting should be in 2 weeks at the same time
19:04:19 <plowsof[m]> we're not allowed to talk to each other anymore now 
19:04:30 <monerobull[m]> Thanks for moderating plowsof
19:05:34 <ofrnxmr[m]> Good meeting plowsof 
19:05:58 <plowsof[m]> i can test my auto log post script now 

```
Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

Earlier logs with some community highlight discussion:
```
11:00:43 <plowsof[m]> There is a meeting today to share some opinions the the CCS ideas / recent events. What would you like to talk about? https://github.com/monero-project/meta/issues/704
11:31:56 <plowsof[m]> we're all reading the dev/events/mrl work group chat logs now.. right guys?? 🥹
14:07:17 <monerobull[m]> I am once again asking for the closure of Afghanistan ccs
14:08:34 <monerobull[m]> On the 255 miner payout: did one miner receive 0.5 out of the 0.6 xmr?
14:13:52 <plowsof[m]> sorry the 255 miner payout - that means that 255 based chads worked together to mine 1 block 
14:14:13 <plowsof[m]> checks notes
14:14:17 <plowsof[m]> one of them got 0.5?
14:14:31 <monerobull[m]> Seems like it?
14:15:00 <ofrnxmr[m]> Where?
14:15:30 <plowsof[m]> https://xmrchain.net/tx/d0c3d1efa68b78aa49839177d91228a61f4d399f6ba71e655ea8a51e359bc519
14:15:39 <plowsof[m]> my understanding is each tx was sent to an individual miner?
14:15:48 <Rucknium[m]> It probably means that one of the miners found most of the p2pool blocks, right? Nothing unexpected.
14:15:53 <monerobull[m]> 191: b126713b7e7a0a179301768ae50d1e93eebb4d0c63c18e2ca67301cbfc52225d	0.507397953508
14:15:56 <ofrnxmr[m]> spirobel: meeting soon. 
14:15:57 <monerobull[m]> Yeah I know
14:16:21 <plowsof[m]> ah good spot , so 1 guy did most of the work but the small hashes contreibuted still
14:16:45 <monerobull[m]> Just not as decentralized as the 255 might imply
14:17:12 <plowsof[m]> the meeting is in ... almost 4 hrs from now https://www.timeanddate.com/countdown/vote?iso=20220515T18&p0=1440&msg=Community+Workgroup+Meeting&font=sanserif
14:17:46 <plowsof[m]> monerobull[m]: trying to shill p2pool mini , please forgive the marketing strat
14:17:53 <monerobull[m]> Kek
14:17:58 <monerobull[m]> Mini is awesome
14:18:23 <nioc> one miner has that much hr 
14:18:30 <ofrnxmr[m]> Yes
14:18:47 <nioc> it has been known since mini was created
14:18:58 <plowsof[m]> Like how those little fish chill out under sharks 
14:19:23 <monerobull[m]> Yeah it's obviously needed so it actually finds a block every once in a while
14:19:53 <ofrnxmr[m]> https://mini.p2pool.observer/miners
14:21:34 <plowsof[m]> sech is preparing p2pool for the HF also 😊 testnet fork tomorrow
14:22:09 <ofrnxmr[m]> Also.. android binaries are good to go now
14:22:26 <monerobull[m]> plowsof[m]: Do we have a countdown?
14:22:53 <ofrnxmr[m]> Til HF? Yeah
14:23:55 <plowsof[m]> countdown as in a nice site like the 'tail emission' countdown , i think not but the exact blockheight for the hardforks are known 
14:24:03 <ofrnxmr[m]> https://p2pool.io/tail.html
14:24:52 <plowsof[m]> btw i left some spaces in the dev meeting log so you can skim over to see whats going on with multisig
14:25:51 <r4v3r23[m]> shruum wallet now has a telegram chat: https://t.me/shruumwallet
14:26:10 <r4v3r23[m]> monerujo fork focused on privacy & security
14:28:46 <ofrnxmr[m]> Possibly to ask them to open a channel here? And bridge?
14:28:46 <ofrnxmr[m]> I dont know how (I dont use telegram) but endor posted how to bridge matrix to telegram the other day
14:29:11 <plowsof[m]> do you need a mobile phone sim to use telegram
14:29:54 <ofrnxmr[m]> Need a phone number. worked with a burner/digital number though
14:30:23 <plowsof[m]> (i used my real one ofcourse but just wanted to look like im a cyberpunk too) 
14:30:28 <ofrnxmr[m]> Err... I mean.. im not on telegram 🤐
14:30:40 <r4v3r23[m]> plowsof[m]: juicysms.com offers unused phone numbers for telegram registration
14:30:44 <r4v3r23[m]> accepts XMR and costs like 50 cents
14:30:53 <plowsof[m]> Juicy thanks!
14:31:05 <ofrnxmr[m]> 50 cents indefinitely? 
14:31:13 <ofrnxmr[m]> Or one time use
14:31:41 <r4v3r23[m]> > <@ofrnxmr:monero.social> Possibly to ask them to open a channel here? And bridge?
14:31:41 <r4v3r23[m]> > 
14:31:41 <r4v3r23[m]> > I dont know how (I dont use telegram) but endor posted how to bridge matrix to telegram the other day
14:31:41 <r4v3r23[m]> devs not a fan of matrix
14:31:53 <r4v3r23[m]> bridges are messy but maybe
14:32:03 <r4v3r23[m]> ofrnxmr[m]: pretty sure one time
14:33:53 <nioc> do we really need a bridge to link to telescam
14:34:55 <Rucknium[m]> If you care about keeping your Telegram account, be advised that using a one-time SMS service could lead to loss of the account since you'll need that number for account recovery.
14:35:41 <nioc> "monerujo fork focused on privacy & security"  <<>> is monerujo is not focused on that
14:35:58 <plowsof[m]> yeah lol will edit that
14:37:14 <ofrnxmr[m]> nioc: Monerujo IMO is solid.
14:37:14 <ofrnxmr[m]> Doesn't connect to any fiat value or exchange services unless you specifically ask it to
14:37:32 <plowsof[m]> 'monerujo fork' seems safe ^^
14:37:37 <ofrnxmr[m]> Removing LAN is a step back.
14:37:37 <ofrnxmr[m]> But fixing the tor usage is a major step forward 
14:40:47 <w[m]> Rucknium: and plowsof: would you guys help spirobel understand how waas works
14:41:17 <plowsof[m]> aggressively shill it to him or does he want to use it?
14:41:21 <r4v3r23[m]> <nioc> ""monerujo fork focused on..." <- not saying MJ isnt private or secure
14:41:26 <w[m]> The former 
14:41:45 <r4v3r23[m]> shruum just hardens it a bit, check out the feature list
14:42:02 <plowsof[m]> docker-compose up -d 🤷
14:42:50 <w[m]> The alternative is approving the CCS due to emotions instead of a fair conversation.
14:42:50 <w[m]> Its only 2300$ and imo would do better without an "approval" wall. 
14:44:05 <plowsof[m]> what about reemuru who abandoned the dev guides CCS because he 'made it work locally with docker' :( 
14:44:42 <plowsof[m]> (he still has to create the guides)
14:46:18 <plowsof[m]> ill help anyone with the waas though no problemo, need to pump my wownero bags
14:47:11 <plowsof[m]> (added wow due to it forcing solo mining and being like-for-like with monero rpc)
14:47:24 <w[m]> Im not familiar with reemuru CCS, but am with reemuru.
14:47:24 <w[m]> Spiro seems to have felt entitled to be approved. I get it, not asking for a lot. But same way, thats too much drama for 2000$. 
14:47:30 <w[m]> plowsof[m]: God tier
14:47:32 <w[m]> Plowsof for ceo
14:47:49 <w[m]> Also, wow people tip and tip hard. 
14:47:51 <Rucknium[m]> From the perspective of a user, WaaS works like this:
14:47:51 <Rucknium[m]> 1) Install the WaaS Docker image on a VPS
14:47:52 <Rucknium[m]> 2) Go through a terminal-based setup wizard, giving the XMR/WOW view keys and BTC/BCH XPUBs so that the WaaS can generate new addresses. No private spend keys are given to the server unless you ask it t generate the wallet for you.
14:49:00 <Rucknium[m]> 3) Write descriptions of the wishes and set the goal amounts.
14:49:00 <Rucknium[m]> 4) Make your website configuration point to the Docker instance
14:49:26 <Rucknium[m]> 5) When one of your wishes is 100% funded, you have to deliver!
14:50:24 <ofrnxmr[m]> Underrated.
14:50:27 <plowsof[m]> the 'usd' amount adjusts in real time - but when the wish is fully funded - it is frozen - and it is up to you to get the funds into whatever currency you need 
14:51:20 <plowsof[m]> it is for people who you trust already though, who have shown evidence of previous work. The CCS and its 'custodial' nature still has its place 
14:51:54 <plowsof[m]> but ofc we have problems with the 'permission ed' aspect , which works great sometimes.. and others not 
14:52:30 <Rucknium[m]> Right. The donations go to your wallet immediately. There is no "release" of funds with milestones or things like that.
14:52:58 <w[m]> Considering Spiro CCS. Should be ideal
14:53:59 <w[m]> Spiro wants to send the money to someone else in afganistan. Someone they trust, but we dont.
14:53:59 <w[m]> Its a small amount, so those who trust and were willing to help spiro should have no problem funding it. 
14:56:04 <w[m]> Someone they have vetted* but we have not* 
14:56:04 <w[m]> So the proposal relies on your believe that Spiro will deliver.
14:56:04 <w[m]> After a successful run on waas id imagine Spiro would have less friction trying to do another CCS. (Will have dilivered and earned trust)  
14:59:31 <ofrnxmr[m]> Lets hope Spiro makes to the the meeting.
15:00:23 <ofrnxmr[m]> He missed the last one and thinks rotten veto'd his CCS.
15:01:06 <plowsof[m]> he who shall not be named!
15:01:52 <ofrnxmr[m]> * and thinks ~rotten, * rotten~, *  *voldemort* veto'd his
15:02:03 <ofrnxmr[m]> Fixed 
```

# Action History
- Created by: plowsof | 2022-05-11T21:49:49+00:00
- Closed at: 2022-05-15T19:07:53+00:00
