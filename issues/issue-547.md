---
title: Monero Research Lab Meeting - 3 February 2021 @ 17 UTC
source_url: https://github.com/monero-project/meta/issues/547
author: SamsungGalaxyPlayer
assignees: []
labels: []
created_at: '2021-02-02T20:57:58+00:00'
updated_at: '2021-02-14T18:58:50+00:00'
type: issue
status: closed
closed_at: '2021-02-03T18:12:44+00:00'
---

# Original Description
Time: 17 UTC

Location: #monero-research-lab

Main discussion topics:

* Triptych (continued discussion)
* v15 ringsize
* https://github.com/monero-project/research-lab/issues/70#issuecomment-768036260

# Discussion History
## SamsungGalaxyPlayer | 2021-02-03T15:36:51+00:00
![image](https://user-images.githubusercontent.com/12520755/106770190-5613b800-6603-11eb-884f-a743712e3ea0.png)

## SamsungGalaxyPlayer | 2021-02-03T18:12:44+00:00
```
[2021-02-03 10:59:59] <sgp_> meeting time
[2021-02-03 11:00:02] <sgp_> 1. Greetings
[2021-02-03 11:00:14] <hyc> hola
[2021-02-03 11:00:23] <zkao> hoi
[2021-02-03 11:00:24] <sethsimmons> hey all
[2021-02-03 11:00:32] <sethsimmons> I'm actually around for something 😀
[2021-02-03 11:00:39] <rottenwheel> Hallo.
[2021-02-03 11:00:58] <sgp_> ping sarang moneromooo ArticMine knaccc vtnerd
[2021-02-03 11:01:07] <rbrunner> Hi (lurking a bit here for once)
[2021-02-03 11:01:10] → kowalabearhugs joined (c6368446@static-198-54-132-70.cust.tzulo.com)
[2021-02-03 11:01:17] <h4sh3d[m]> hi
[2021-02-03 11:01:52] <zkao> jwinterm midipoet
[2021-02-03 11:02:04] <endogenic> endogenic
[2021-02-03 11:04:20] <sgp_> hello everyone
[2021-02-03 11:04:27] <lederstrumpf> hello
[2021-02-03 11:04:28] <sgp_> are sarang and moneromooo here?
[2021-02-03 11:04:48] → rex4539_ joined (~rex4539@gateway/tor-sasl/rex4539)
[2021-02-03 11:05:33] <ArticMine> Hi
[2021-02-03 11:05:51] ⇐ rex4539_ quit (~rex4539@gateway/tor-sasl/rex4539): Remote host closed the connection
[2021-02-03 11:06:12] ⇐ rex4539 quit (~rex4539@gateway/tor-sasl/rex4539): Remote host closed the connection
[2021-02-03 11:06:26] <sgp_> hmm, apparently not
[2021-02-03 11:06:46] <sgp_> let's just start with the first high-level topic
[2021-02-03 11:06:47] <sgp_> https://github.com/monero-project/meta/issues/547#issuecomment-772600779
[2021-02-03 11:07:08] <sgp_> we need to think about which plan we prefer of the two
[2021-02-03 11:07:22] <sgp_> this has been discussed in prior meetings, but now they are written down
[2021-02-03 11:07:48] <sgp_> sarang mentioned that the research work for triptych will take approximately 2 months
[2021-02-03 11:07:56] <sgp_> 3 months for moneromooo is an estimate
[2021-02-03 11:08:06] <sethsimmons> I just don't see the need to delay a network upgrade for multisig, which is so infrequently used.
[2021-02-03 11:08:10] <sethsimmons> So Option 2 seems better to me.
[2021-02-03 11:08:29] <sgp_> just for clarity:
[2021-02-03 11:08:31] <sethsimmons> If we can work on multisig in parallel or fund someone else for that portion, great.
[2021-02-03 11:08:39] <sgp_> option 1 and option 2 will have some multisig wallet support
[2021-02-03 11:09:01] <sgp_> option 1 is doing 2 hardforks: 1 for BP+, another for triptych
[2021-02-03 11:09:09] <sgp_> option 2 is doing 1 hardfork with both
[2021-02-03 11:09:38] <sethsimmons> ah
[2021-02-03 11:10:06] <hyc> seems like the cautious route is to change one thing at a time
[2021-02-03 11:10:43] <ArticMine> My preference is option 1. I think the timeline for Triptych for option 2 is very optimistic.
[2021-02-03 11:10:44] <rottenwheel> Would love to first hear an informed stance from noether or moo before casting a vote, though one at a time is more cautious indeed.
[2021-02-03 11:10:48] <h4sh3d[m]> agree with hyc, an hard fork with two big changes is more risky
[2021-02-03 11:11:02] <zkao> hyc's point to me that sounds the most scientific way of doing things
[2021-02-03 11:11:08] <sgp_> fwiw, two hardforks also creates more headaches for the ecosystem than 1
[2021-02-03 11:11:16] <ArticMine> Still I want to hear from sarang on the timelines
[2021-02-03 11:11:18] → rj_ joined (~x@65.48.162.168)
[2021-02-03 11:11:39] <sgp_> note that I can speak for sarang in the 2 months for research. That is what he is telling me
[2021-02-03 11:11:59] <sgp_> I can't really speak for moo
[2021-02-03 11:12:23] <hyc> a 2nd hardfork 10 months after the previous doesn't sound like a big hassle
[2021-02-03 11:12:39] <hyc> considering we used to do them every 6 months, why is 10 months a problem?
[2021-02-03 11:13:10] <rbrunner> I don't understand yet the long time of 5 months in option 1 where there is only 1 bar "Support ..." active somehow. What happens there?
[2021-02-03 11:13:24] <sgp_> I'm just passing along that Cake kinda interrupts their dev process each time
[2021-02-03 11:13:50] <sethsimmons> Option 1 is the better option IMO as well -- fewer moving parts in a single HF, faster ring-size increase, still lots of lead time.
[2021-02-03 11:14:06] — needmoney90 is actually awake at a reasonable hour 
[2021-02-03 11:14:12] ⇐ rj quit (~x@65.48.163.231): Ping timeout: 258 seconds
[2021-02-03 11:14:14] <sethsimmons> <rbrunner "I don't understand yet the long "> I would assume delaying 2nd HF so that it's not too much pain on the ecosystem while focusing on improving musig support.
[2021-02-03 11:14:17] <needmoney90> [takes a seat]
[2021-02-03 11:14:36] <endogenic> still dreaming needmoney90
[2021-02-03 11:15:05] <rbrunner> Ok
[2021-02-03 11:15:14] → rex4539 joined (~rex4539@gateway/tor-sasl/rex4539)
[2021-02-03 11:15:17] <hyc> that part didn't bother me too much, presumably there will be other work to justify a hardfork as well
[2021-02-03 11:15:23] <sgp_> is August the soonest we can have v15? I'd actually rather move forward as much as possible if we want to go with option 1
[2021-02-03 11:16:41] <needmoney90> Are debruyne or selsta around?
[2021-02-03 11:16:42] <sgp_> I'd rather make it June tbh
[2021-02-03 11:17:06] <needmoney90> Both of them are front line support, and I think their perspectives here would be valuable.
[2021-02-03 11:17:43] <ArticMine> The other item for the HF is issue 70
[2021-02-03 11:17:51] <needmoney90> Lots of small fires to put out every HF, they have to deal with it every time.
[2021-02-03 11:18:24] — zkao is waiting till august
[2021-02-03 11:18:31] ⇐ rex4539 quit (~rex4539@gateway/tor-sasl/rex4539): Client Quit
[2021-02-03 11:18:48] → rex4539 joined (~rex4539@gateway/tor-sasl/rex4539)
[2021-02-03 11:21:58] <sgp_> dEBRUYNE is not here, but they were the one mostly championing option 2
[2021-02-03 11:22:15] <sgp_> I still personally prefer option 2, but I also get the arguments behind option 1
[2021-02-03 11:22:27] <rbrunner> Trouble once instead of trouble two times?
[2021-02-03 11:22:59] <ArticMine> There is an advantage to option 2 in that it does simplify the scaling side in that there is only one tx size (weight) to deal with
[2021-02-03 11:23:01] <moneromooo> I think timing will mostly depend when the code gets reviewed, no ?
[2021-02-03 11:23:17] <moneromooo> BP+ is all ready to go, bar review.
[2021-02-03 11:23:45] <moneromooo> Triptych is not plugged at all, and we might need a new way to represent rings, depending on how much we bump ring size.
[2021-02-03 11:25:05] <sarang> Hi
[2021-02-03 11:25:08] <moneromooo> Also, fucking multisig users over is not nice. We'd have to allow CLSAG txes in parallel, probably, so they can still spend their coins while multisig is worked out.
[2021-02-03 11:25:20] <gingeropolous> ^
[2021-02-03 11:25:39] <sgp_> moneromooo: it's my understanding that they wouldn't be "fucked over" in option 2
[2021-02-03 11:26:22] <sgp_> but it seems like most people are generally for option 1
[2021-02-03 11:26:24] <needmoney90> If Deb is behind option 2, I'm inclined to lean towards that option.
[2021-02-03 11:27:00] <sethsimmons> Both are fine IMO, I just lean towards one for faster ring-size increase, mostly, which is probably not a good enough reason.
[2021-02-03 11:27:25] <hyc> didn't realize this would be a breaking change for multisig
[2021-02-03 11:27:38] <hyc> so yeah, let's not screw anyone...
[2021-02-03 11:27:45] ⇐ TheoStorm quit (~TheoStorm@185.142.226.41): Quit: Leaving
[2021-02-03 11:28:17] <moneromooo> When I said review above, I meant audit by a third party. Not PR review.
[2021-02-03 11:28:20] <sethsimmons> Both options complicate multisig FWIW
[2021-02-03 11:28:24] <rbrunner> Potential multisig problem would be to not be able to spend coins out of a multisig wallet for a certain period?
[2021-02-03 11:28:44] <sarang> Research areas for this still include: cross-transaction batching, multisig algorithms and analysis, anonymity set binning
[2021-02-03 11:28:49] <needmoney90> There are ecosystem-wide repurcussions every HF. We should be leaning towards more consistency in our releases if at all possible. I think two HFs (when we know what will be included in both ahead of time) is less ideal due to this
[2021-02-03 11:28:55] <sgp_> rbrunner: I don't believe that would happen
[2021-02-03 11:29:01] <sethsimmons> sgp_: do you have a summary of the multisig effects of both?
[2021-02-03 11:29:25] <rbrunner> Just wondering what would be the "fuckery" ...
[2021-02-03 11:30:01] <sgp_> clsag multisig wallet users need to "convert" their wallet to a non-multisig wallet before they can spend triptych funds received in this same wallet
[2021-02-03 11:30:26] <sethsimmons> <needmoney90 "There are ecosystem-wide repurcu"> If we go this route and combine BP+ and Triptych, I'd vote for a long and pushed testnet/stagenet testing time.
[2021-02-03 11:30:44] <sethsimmons> With lots of pushes to get people running nodes, maybe even simple scripts for stress-testing scenarios
[2021-02-03 11:30:52] <sgp_> maybe I need to document this all clearly since there is a ton of confusion it seems
[2021-02-03 11:31:10] <needmoney90> That would cause much less strain on time, resources, and our surrounding ecosystem.
[2021-02-03 11:31:10] <rbrunner> Could do no harm :)
[2021-02-03 11:31:15] <sgp_> okay, so how about this
[2021-02-03 11:31:16] <sethsimmons> We generally don't do a ton of public test/stagenet testing before forks and its just a few of us involved. I'd like to see us actively try and rope in more users and define more test-cases.
[2021-02-03 11:31:27] <sgp_> I'll open a github issue for these two options with all the details I know of
[2021-02-03 11:31:29] <sethsimmons> <sgp_ "maybe I need to document this al"> Its very confusing lol
[2021-02-03 11:31:37] <sgp_> then everyone will have a week to comment
[2021-02-03 11:31:46] <sgp_> longer if needed
[2021-02-03 11:31:50] <needmoney90> A pushed back timeline would be a great chance for us to do a push for testing.
[2021-02-03 11:32:09] <sgp_> before I do that, why v15 in option 1 in August?
[2021-02-03 11:32:34] <moneromooo> BP+ isn't a huge advance over BP so I'd be fine pushing it till later tbh.
[2021-02-03 11:32:39] <sethsimmons> I'd vote for 1-2mo after audits complete.
[2021-02-03 11:32:50] <moneromooo> It doesn't hurt as it did for 12 kB -> 2.5 kB.
[2021-02-03 11:33:11] <sgp_> ArticMine: is really pushing for their fee change being included soon
[2021-02-03 11:33:38] <sgp_> so we can have bp+ audit finished in 2 months, pretty easy
[2021-02-03 11:33:45] <sethsimmons> For sure.
[2021-02-03 11:33:52] <sgp_> so that's sooner than August
[2021-02-03 11:33:53] <sethsimmons> I would only advocate a HF for it with other improvements like MRL70 and ring-size increase.
[2021-02-03 11:34:26] <sethsimmons> <sgp_ "so we can have bp+ audit finishe"> June sounds viable then.
[2021-02-03 11:34:39] <sgp_> is anyone here against late June?
[2021-02-03 11:35:16] <sgp_> because if no one is against late June, I can adjust option 1
[2021-02-03 11:35:42] <needmoney90> I would prefer to hear from our front line support before making a call here
[2021-02-03 11:35:54] <ArticMine> So BP+ audit by April HF in June. That makes sense
[2021-02-03 11:36:21] <moneromooo> This should be in -dev anyway. Research isn't concerned with fork timing.
[2021-02-03 11:36:26] <sgp_> okay, looks like I have some work to do then
[2021-02-03 11:36:52] <sgp_> I'll put out a github issue tomorrow AM at the latest with a summary
[2021-02-03 11:37:10] <sgp_> ArticMine: can you talk about the fees then?
[2021-02-03 11:37:19] <sgp_> https://github.com/monero-project/research-lab/issues/70#issuecomment-768036260
[2021-02-03 11:37:40] <sgp_> I'm a little concerned with the increase in the scaling limit from 1.4 to 2
[2021-02-03 11:37:56] <sgp_> it seems aggressive to me
[2021-02-03 11:38:27] <sgp_> if Monero adoption grows faster than whatever limit we set, the network doesn't break; transactions just get more expensive temporarily
[2021-02-03 11:39:40] <sgp_> does anyone have thoughts here?
[2021-02-03 11:39:43] <ArticMine> While I agree that under many circumstances something like 1.6 or 1.8 might be enough. There would be very little margin for error
[2021-02-03 11:40:30] <UkoeHB> p.s. I have not looked at fees yet... no head space at the moment
[2021-02-03 11:40:47] <sgp_> 2 would allow for a 32x increase in block size per year
[2021-02-03 11:40:54] <ArticMine> In 2016 we saw a rate over several months in excess of 2 and there was no increase in adoption during the 2014 - 2015 bear market
[2021-02-03 11:41:09] <sgp_> 1.4 allows for ~5.4x
[2021-02-03 11:41:38] <ArticMine> in 2019 - 2020 we saw an increase in adoption during a bear market
[2021-02-03 11:42:33] <sgp_> well, maybe we should make the upper limit in growth per year to whatever brings us up to Bitcoin's current transaction throughput
[2021-02-03 11:42:49] <sgp_> since the BTC network does work today with a limited size
[2021-02-03 11:43:28] <sgp_> is that unreasonable?
[2021-02-03 11:43:44] <ArticMine> add to this the recent regulatory changes and a repeat of what happened in 2016 and we will will be over 2
[2021-02-03 11:44:09] <ArticMine> Bitcoin is dysfunctional because of its limits to growth
[2021-02-03 11:44:23] <ArticMine> So following Bitcoin is unreasonable
[2021-02-03 11:44:48] <sgp_> there's still provision for growth however
[2021-02-03 11:45:32] <sgp_> it's a capped growth rate not a capped static siz
[2021-02-03 11:45:34] <ArticMine> Just because we have 2 it does not mean that that it will be maxed out
[2021-02-03 11:45:50] <sgp_> we need to prepare for spammers to try and cap it out however
[2021-02-03 11:46:17] <ArticMine> That is why the we introduce the LT median
[2021-02-03 11:46:54] <ArticMine> The attack that happened was the reverse
[2021-02-03 11:47:03] → nssy joined (~nssy@197.237.91.81)
[2021-02-03 11:47:04] <ArticMine> I mean just a month ago
[2021-02-03 11:47:26] <sgp_> yeah I get that, capping the decrease rate
[2021-02-03 11:47:35] <jwinterm> if it was maxed out under the two scenario: 1) how much would the blockchain grow in one year, and 2) how much in XMR fees would be paid in total over the year?
[2021-02-03 11:47:44] <jwinterm> if you happen to know
[2021-02-03 11:48:19] <sgp_> jwinterm: with this proposal, it would allow blocks to be max 32x larger than they were at the start of the year
[2021-02-03 11:48:28] <ArticMine> If we allow the short term median to remain above the long term median for an extended period of time then the type of attack we just has would be chap and disruptive
[2021-02-03 11:48:50] <ArticMine> cheap
[2021-02-03 11:48:51] <needmoney90> I think 32x/year is excessive, and gives us little time to react to an attack. We should be considering lead times in years at this point, not months.
[2021-02-03 11:49:11] <ArticMine> There is plenty of time
[2021-02-03 11:49:29] <ArticMine> to respont
[2021-02-03 11:49:35] <needmoney90> There is a flurry of support/ecosystem issues that pop up every HF.
[2021-02-03 11:49:42] <ArticMine> The is only just over 2 hour on the other side
[2021-02-03 11:49:51] ⇐ rj_ quit (~x@65.48.162.168): Quit: WeeChat 3.0
[2021-02-03 11:49:53] → p0nziph0ne joined (p0nziph0ne@gateway/vpn/privateinternetaccess/p0nziph0ne)
[2021-02-03 11:49:53] <needmoney90> Those must be considered in this equation
[2021-02-03 11:50:04] <ArticMine> That is ho long the short term median can fall drastically
[2021-02-03 11:50:18] <sgp_> Bitcoin has a little over 10x as many tx/day as Monero right now
[2021-02-03 11:50:21] <selsta> June is stressy and unrealistic
[2021-02-03 11:50:30] <needmoney90> Ah, welcome selsta
[2021-02-03 11:50:42] — selsta didn't read all backlog
[2021-02-03 11:50:57] <needmoney90> You should. Please catch up, your opinion here is greatly appreciated
[2021-02-03 11:51:16] <needmoney90> Since you deal with the support fallout from HFs
[2021-02-03 11:51:16] <ArticMine> So we are talking under 2 hours vs over 2 months to respond to an attack
[2021-02-03 11:51:27] <sgp_> ArticMine: let's separate these two things
[2021-02-03 11:51:44] <sgp_> there's 1) the maximum decline rate. We seem in agreement here
[2021-02-03 11:51:46] <ArticMine> What two things
[2021-02-03 11:51:54] <sgp_> then there's 2) the maximum increase rate
[2021-02-03 11:51:57] <sgp_> is this correct?
[2021-02-03 11:52:09] ⇐ kowalabearhugs quit (c6368446@static-198-54-132-70.cust.tzulo.com): Quit: Ping timeout (120 seconds)
[2021-02-03 11:52:36] <ArticMine> Yes but you are ignoring that the short term median can still be above the long term median for an extended period of time
[2021-02-03 11:52:45] <ArticMine> Setting the stage for an attack
[2021-02-03 11:53:02] <ArticMine> Such as the one that just occurred
[2021-02-03 11:53:24] → kowalabearhugs joined (c6368446@static-198-54-132-70.cust.tzulo.com)
[2021-02-03 11:53:57] <ArticMine> The whole point of the long term median is to give the community over 2 months to respond
[2021-02-03 11:54:04] <ArticMine> This does not change
[2021-02-03 11:54:43] <sgp_> because it's capped at ~2x growth?
[2021-02-03 11:55:26] <ArticMine> The Short term median is capped at 50x over the long term median
[2021-02-03 11:55:48] <ArticMine> To allow for a retain surge over a 1 - 2 month period
[2021-02-03 11:56:13] <ArticMine> This is why VISA has over 20x their average use as a maximum capacity
[2021-02-03 11:56:44] <ArticMine> This was all done when the long term median was introduced in 2019
[2021-02-03 11:57:06] <sgp_> I still think the bump is ambitious
[2021-02-03 11:57:19] <sgp_> sorry we are getting close on time
[2021-02-03 11:57:30] <sgp_> selsta: is August the earliest you support?
[2021-02-03 11:57:42] <sgp_> what are your thoughts there
[2021-02-03 11:57:46] <ArticMine> It is actually very prudent
[2021-02-03 11:58:02] <ArticMine> base uppon the transaction data
[2021-02-03 11:58:14] <sgp_> I think we will need to schedule another dedicated discussion on the block caps
[2021-02-03 11:58:46] → TheoStorm joined (~TheoStorm@97.69-247-81.adsl-dyn.isp.belgacom.be)
[2021-02-03 11:59:07] <ArticMine> I suggest the argument be made first in the issue on GItHub
[2021-02-03 11:59:21] <ArticMine> GitHub
[2021-02-03 12:00:33] <needmoney90> Let selsta catch up and reply to the upcoming github issue, take some time to collect their thoughts
[2021-02-03 12:00:37] <ArticMine> MAke the case for 1.6 or 1.8 vs to there
[2021-02-03 12:00:52] <ArticMine> vs 2
[2021-02-03 12:01:05] <selsta> needmoney90: can only catch up later
[2021-02-03 12:01:05] <sgp_> yes I can comment
[2021-02-03 12:01:14] <selsta> have to go again
[2021-02-03 12:01:16] <sgp_> but I also don't want the default to be an assumed increase to 2
[2021-02-03 12:01:24] <sgp_> the change to 2 is the proposed change
[2021-02-03 12:01:40] <selsta> but yes, last meeting I said I would be for late July / August
[2021-02-03 12:01:52] <sgp_> okay ty selsta
[2021-02-03 12:02:33] <sgp_> any final thoughts?
[2021-02-03 12:02:50] <sgp_> if someone wants to join the 2nd BP+ audit calls with me, please let me know
[2021-02-03 12:03:08] <sgp_> my takeaways:
[2021-02-03 12:03:11] <needmoney90> Are they going to be published later?
[2021-02-03 12:03:15] <needmoney90> The calls that is
[2021-02-03 12:03:23] <sgp_> needmoney90: no, I'm not going to record the calls
[2021-02-03 12:03:29] <sgp_> but the SoWs will be public
[2021-02-03 12:03:29] <needmoney90> OK.
[2021-02-03 12:03:36] <needmoney90> When will that be?
[2021-02-03 12:03:40] <needmoney90> The calls that is.
[2021-02-03 12:03:44] <sgp_> TBD, ideally within a week
[2021-02-03 12:03:53] <sgp_> it's on me to schedule
[2021-02-03 12:04:00] <needmoney90> Got it
[2021-02-03 12:04:10] <needmoney90> No further thoughts from me
[2021-02-03 12:04:12] <sgp_> I really would prefer sarang or someone else knowledgeable there
[2021-02-03 12:04:19] <sgp_> since I have no idea what this code is LOL
[2021-02-03 12:05:50] <sgp_> anyway
[2021-02-03 12:06:00] <sgp_> look for the update summary/timeline github issue
[2021-02-03 12:06:23] <sgp_> thank you everyone
[2021-02-03 12:07:12] <sgp_> oh, and I will also comment on the block size issue
```

## garlicgambit | 2021-02-14T18:58:50+00:00
@SamsungGalaxyPlayer, you mention that you'll open a github issue about the two hardfork options. Is that already available somewhere?

# Action History
- Created by: SamsungGalaxyPlayer | 2021-02-02T20:57:58+00:00
- Closed at: 2021-02-03T18:12:44+00:00
