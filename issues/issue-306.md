---
title: 'Community Workgroup Meeting: 16 February 2019 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/306
author: SamsungGalaxyPlayer
assignees: []
labels: []
created_at: '2019-02-12T21:08:32+00:00'
updated_at: '2019-02-16T18:07:24+00:00'
type: issue
status: closed
closed_at: '2019-02-16T18:07:24+00:00'
---

# Original Description
**Location**

[Freenode](https://kiwiirc.com/nextclient/#irc://irc.freenode.net/#monero-community) | [Mattermost](https://mattermost.getmonero.org/monero/channels/monero-community) | [Slack](https://monero.slack.com/) | Irc2P

Please test the relays shortly before using. If there are any issues, please use Freenode IRC directly.

Please PM [SGP on Reddit](https://www.reddit.com/message/compose/?to=SamsungGalaxyPlayer&subject=Monero%20Slack%20invite%20(from%20GitHub)&message=Hello%20please%20send%20a%20Monero%20Slack%20invite%20to%20the%20following%20email:) with your email for a Slack invite if desired.

 - `#monero-community`

**Time**

17:00 UTC
12:00 ET
11:00 CT
09:00 PT

[Use this timezone calculator to convert UTC to your time zone](https://www.timeanddate.com/worldclock/converter.html?iso=20190216T170000&p1=tz_et&p2=28&p3=111&p4=49&p5=179&p6=70&p7=224&p8=48&p9=136).

**Proposed Meeting Items**

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

0. Introduction
1. Greetings
2. Community highlights
3. FFS updates
4. Workgroup report
5. Upgrade timeline discussion
6. Community PoW discussion (RandomX)
7. Open ideas time
8. Confirm next meeting date/time
9. Conclusion

# Discussion History
## SamsungGalaxyPlayer | 2019-02-16T18:07:24+00:00
(11:01:00 AM) sgp_ has changed the topic to: Community Meeting NOW
(11:01:10 AM) sgp_: 0. Introduction
(11:01:15 AM) sgp_: We would like to welcome everyone to this Monero Community Meeting!
(11:01:21 AM) sgp_: Link to agenda on GitHub: https://github.com/monero-project/meta/issues/306
(11:01:26 AM) sgp_: Monero Community meetings are a discussion place for anything going on in the Monero Community, including other Monero workgroups. We use meetings to encourage the community to share ideas and provide support. Stay up to date with the latest events by subscribing to this calendar: https://xmr.ncrypt.sh/index.php/apps/calendar/p/8dP6z6XQDnkPREo4/Monero-Meetings
(11:01:42 AM) sgp_: Lots of good discussions today
(11:01:44 AM) sgp_: 1. Greetings
(11:01:52 AM) el00ruobuob: Hello!
(11:02:16 AM) msvb-mob: Hello.
(11:02:20 AM) oneiric_: .>
(11:03:52 AM) ErCiccione[m]: Hi
(11:03:59 AM) sgp_: welcome everyone
(11:04:28 AM) sgp_: 2. Community highlights
(11:04:34 AM) sgp_: MoneroCrusher wrote a blog post wherein they estimated the proportion of ASICs on the Monero network by analyzing nonces. Here is the Reddit discussion: https://www.reddit.com/r/Monero/comments/ao8mho/analysis_more_than_85_of_the_current_monero/
(11:04:37 AM) monerobux: [REDDIT] Analysis: More than 85% of the current Monero Hashrate is ASICs and each machine is doing 128 kh/s (https://medium.com/@MoneroCrusher/analysis-more-than-85-of-the-current-monero-hashrate-is-asics-and-each-machine-is-doing-128-kh-s-f39e3dca7d78) to r/Monero | 317 points (98.0%) | 443 comments | Posted by MoneroCrusher | Created at 2019-02-07 - 21:07:33
(11:04:39 AM) sgp_: tevador posted this update on RandomX, explaining that the documentation was mostly complete: https://www.reddit.com/r/Monero/comments/aovypq/randomx_asic_resistant_pow_community_feedback/
(11:04:42 AM) monerobux: [REDDIT] RandomX - ASIC resistant PoW - community feedback (self.Monero) | 167 points (95.0%) | 430 comments | Posted by tevador | Created at 2019-02-09 - 19:55:26
(11:04:45 AM) sgp_: We will discuss PoW in #6.
(11:05:13 AM) sgp_: Coin Center published a report on protecting the ability to transact privately. Surae Noether contributed to the report: https://www.reddit.com/r/Monero/comments/ant51w/we_must_protect_our_ability_to_transact_privately/
(11:05:14 AM) monerobux: [REDDIT] We must protect our ability to transact privately online (https://coincenter.org/entry/we-must-protect-our-ability-to-transact-privately-online) to r/Monero | 211 points (99.0%) | 35 comments | Posted by vp11 | Created at 2019-02-06 - 17:31:42
(11:05:20 AM) sgp_: Monero will upgrade on block 1788000, approximately March 9. More discussions on this later in #5.
(11:05:26 AM) sgp_: Monero was added to Exodus Eden: https://www.reddit.com/r/Monero/comments/amcemx/youve_been_asking_we_finally_delivered_xmr_is/
(11:05:27 AM) monerobux: [REDDIT] "you’ve been asking... we finally delivered! $XMR is live in [Exodus] Eden version 19.2.2" (https://twitter.com/C0inAlchemist/status/1091449168244232192) to r/Monero | 199 points (96.0%) | 68 comments | Posted by dEBRUYNE_1 | Created at 2019-02-02 - 08:52:00
(11:05:38 AM) sgp_: Last week's Coffee Chat: https://www.youtube.com/watch?v=kNPjA4o4xSY
(11:05:39 AM) monerobux: [ Monero Coffee Chat - 2019.02.09 - YouTube ] - www.youtube.com
(11:05:54 AM) sgp_: Does anyone else have community (non-workgroup) updates to share?
(11:06:14 AM) msb17 left the room (quit: Ping timeout: 244 seconds).
(11:06:44 AM) sgp_: oh, rbrunner wrote this piece on possible Monero integration in OpenBazaar: https://rbrunner7.github.io/openbazaar
(11:06:49 AM) joshy left the room (quit: Quit: joshy).
(11:07:27 AM) sgp_: midipoet, Xeagu, and rehrar were at Tabconf last week
(11:08:23 AM) sgp_: 3. FFS updates
(11:08:33 AM) sgp_: rehrar says the FFS/CCS upgrade is scheduled for this Monday, pushed back from yesterday. cross your fingers
(11:08:46 AM) el00ruobuob: fingers crossed
(11:08:54 AM) sgp_: Also, please do not claim your free “Monero coins.” Some users received forum messages and emails.
(11:09:08 AM) sgp_: FFS proposals still needing funding:
(11:09:14 AM) sgp_: v1docq47: video creation / translations into russian (february – july) https://forum.getmonero.org/8/funding-required/91863/v1docq47-video-creation-translations-into-russian-february-july
(11:09:20 AM) msvb-mob: That's quite surprising that 85% rate is attributed to ASIC processing in the report.
(11:09:53 AM) sgp_: msvb-mob: that's an estimate that some dispute, but they walk through the methodology
(11:10:14 AM) sgp_: The Monero Conference was fully funded! It's happening!
(11:10:29 AM) vp11: Yahoo!
(11:10:40 AM) sgp_: Thanks to the Monero community for its generous donations, and thanks to the Zcash Foundation for completing the remaining funding required
(11:11:06 AM) sgp_: Are there are proposals in ideas that I missed? I don’t see any. Frankly any real ones are buried under helpline phone numbers.
(11:11:21 AM) midipoet: Sorry. Late hello!
(11:11:25 AM) el00ruobuob: My proposal is still under the radar
(11:11:38 AM) sgp_: el00ruobuob: can you link it directly?
(11:11:42 AM) el00ruobuob: but we stated with several core team member to wait until the new FFS
(11:11:44 AM) el00ruobuob: yes sur
(11:11:47 AM) el00ruobuob: *sure
(11:12:02 AM) sgp_: If you're ok with that, sure. But it has been quite a while
(11:12:09 AM) oneiric_: nop, waiting for the perpetual "next monday" ever name-changing funding system
(11:12:13 AM) el00ruobuob: https://forum.getmonero.org/8/funding-required/91269/el00ruobuob-january-to-march-part-time-for-a-new-quarter
(11:12:36 AM) vp11: Is 'next monday' the new 'soon'?
(11:12:39 AM) sgp_: el00ruobuob: do you want me to share this on Reddit?
(11:12:55 AM) el00ruobuob: Sure, you can sgp_
(11:13:01 AM) sgp_: ok, I will do
(11:13:05 AM) sgp_: any other FFS updates?
(11:13:17 AM) sgp_: or comments about any of the proposals?
(11:14:01 AM) oneiric_: happy to see ErCiccione[m] and the Konferenco get funded, that's legit
(11:14:01 AM) sgp_: 4. Workgroup report
(11:14:15 AM) sgp_: I know you have stuff to report ErCiccione[m]
(11:14:39 AM) ErCiccione[m]: I'm happy too oneiric_ thanks to everybody
(11:14:49 AM) ErCiccione[m]: yep, thanks sgp_
(11:14:51 AM) ErCiccione[m]: so
(11:15:57 AM) ErCiccione[m]: this emergency hard fork completely messed up all my plans for the localization workgroup. So, much stuff will be delayed, like the translation memory and the implementation of monerujo with pootle
(11:16:13 AM) ErCiccione[m]: this because now i have to get ready for the hard fork much earlier than planned
(11:16:15 AM) tat left the room (quit: Remote host closed the connection).
(11:16:29 AM) tat [~tat@gateway/tor-sasl/tat] entered the room.
(11:16:42 AM) ErCiccione[m]: so, as soon as the codebase will be stable enough i will port everything to pootle and translators will be able to start working on that
(11:17:08 AM) ErCiccione[m]: in the meantime, i will create a graphic guide to help new translators with pootle
(11:17:46 AM) ErCiccione[m]: THe CLI should be almost ready to be worked on, what worries me a bit is the GUI, but in the worst case scenario we will just have very few time, nothing too bad
(11:17:55 AM) ErCiccione[m]: ah
(11:18:15 AM) ErCiccione[m]: there is a lot going on about getmonero. Many translations coming and many are work in progress
(11:18:50 AM) ErCiccione[m]: German is online and announced. Soon we will have Chinese and Brazilian portuguese (MR already opened)
(11:19:16 AM) ErCiccione[m]: I probably forgot something, but this is everything coming in my mind right now
(11:19:17 AM) el00ruobuob: About pootle, are the CLI & GUI ready to be worked on for the 0.14?
(11:20:24 AM) ErCiccione[m]: el00ruobuob:  Not even close, funny enough. I uploaded all the strings for the CLI, announced it, people started working on it and few days later we got the announcement.
(11:20:46 AM) ErCiccione[m]: so at the moment on pootle there are the strings for 0.14.1ish
(11:21:06 AM) el00ruobuob: ok, thanks for the clarification
(11:21:15 AM) ErCiccione[m]: i will upload the repos again once the code will be a minimal definitive
(11:21:20 AM) ErCiccione[m]: np
(11:21:28 AM) sgp_: Thanks for your flexibility dealing with this new timeline. I know you've been put in a difficult position
(11:22:03 AM) ErCiccione[m]: It's ok, it wouldn't be fun otherwise!
(11:22:03 AM) ErCiccione[m]: :P
(11:22:18 AM) ErCiccione[m]: other questions?
(11:23:02 AM) sgp_: Does anyone else have a workgroup update?
(11:23:13 AM) oneiric_: ./
(11:23:31 AM) sgp_: ^ proceed :)
(11:23:38 AM) oneiric_: thanks sgp_
(11:24:14 AM) oneiric_: progress continues on tini2p, there will be a dev meeting on the 21st
(11:24:59 AM) oneiric_: will be at 18:00 UTC in #tini2p-dev
(11:25:04 AM) oneiric_: that's all
(11:25:07 AM) sgp_: oneiric_: can you post a quick notification here? https://github.com/monero-project/meta/issues
(11:25:18 AM) oneiric_: will do
(11:25:32 AM) oneiric_: will cross-post the meeting agenda
(11:25:50 AM) el00ruobuob: oneiric_, if you want me to post the meeting log on the website, i can do it
(11:25:55 AM) sgp_: I'll make it if my class doesn't take too much of my attention :p
(11:26:18 AM) oneiric_: no worries, will paste logs for those that can't make it
(11:26:31 AM) sgp_: Any other updates?
(11:27:30 AM) sgp_: Ok, discussion time then
(11:27:32 AM) sgp_: 5. Upgrade timeline discussion
(11:27:37 AM) sgp_: Here are relevant threads explaining Monero’s upgrade timeline:
(11:27:42 AM) sgp_: https://www.reddit.com/r/Monero/comments/apkvym/asic_resistance_hashrate_discussion_thread/
(11:27:44 AM) monerobux: [REDDIT] ASIC resistance & hashrate discussion thread + preliminary information regarding the upcoming scheduled protocol upgrade of ~ March 9 (self.Monero) | 87 points (97.0%) | 106 comments | Posted by dEBRUYNE_1 | Created at 2019-02-11 - 20:54:32
(11:27:47 AM) el00ruobuob: \o/
(11:27:48 AM) sgp_: https://www.reddit.com/r/Monero/comments/aqn6li/mailing_list_message_regarding_the_upcoming/
(11:27:49 AM) monerobux: [REDDIT] Mailing list message regarding the upcoming scheduled protocol upgrade of ~ March 9 (self.Monero) | 29 points (98.0%) | 19 comments | Posted by dEBRUYNE_1 | Created at 2019-02-14 - 18:56:17
(11:28:15 AM) sgp_: Last week, the Core Team decided to move the upgrade to March 9 (originally estimated mid April)
(11:29:07 AM) sgp_: The upgrade will occur in stages
(11:29:13 AM) sgp_: It is best depicted in this image here: https://i.imgur.com/gGz9dwK.jpg
(11:29:44 AM) sgp_: 0.14 will include only the required consensus changes and will be released soon
(11:30:08 AM) sgp_: 0.14.1 will include all other upgrades and will be available shortly after the hardfork
(11:30:34 AM) sgp_: Everyone needs to upgrade, including wallets, nodes, and miners
(11:30:45 AM) el00ruobuob: So only one consensus change?
(11:30:46 AM) sgp_: Are there any questions about the upcoming upgrade?
(11:31:00 AM) sgp_: el00ruobuob:
(11:31:10 AM) sgp_: This upgrade is moved forward approximately one month to patch some important security components. This upgrade includes the following changes: 1. A new Proof of Work algorithm, CryptonightR 2. A new dynamic block size algorithm 3. Slightly smaller transactions 4. Payment ID changes for improved privacy 5. Notification changes (see: https://paste.debian.net/hidden/0d0d3694)
(11:32:04 AM) oneiric_: why is payment id being included? thought it was consensus only?
(11:32:25 AM) sgp_: Not sure :/
(11:32:34 AM) sgp_: Probably because it's a small change that has been well-tested
(11:33:11 AM) oneiric_: was this the wallet disabling of separate payment id?
(11:33:48 AM) sgp_: That and automatically including a payment ID even when none are specifically added to the transaction
(11:35:11 AM) oneiric_: would have traded tor/i2p support for that, but not-my-coin
(11:35:35 AM) sgp_: I think there will be some concerns about the testing. Those will be available for 0.14.1
(11:35:47 AM) oneiric_: when 0.14.1?
(11:36:16 AM) sgp_: I believe approx. 1 month after
(11:36:35 AM) sgp_: The intent is for a RC to come up a bit earlier
(11:37:01 AM) sgp_: but people can test master in the meantime, which includes the Tor/i2p functionality now
(11:37:02 AM) oneiric_: ok, then no worries. thought point release might be pushed back many months
(11:37:24 AM) sgp_: oneiric_: that is one of my main concerns too, and I'm doing my best to make sure that doesn't happen
(11:37:30 AM) oneiric_: will definitely be testing that
(11:38:01 AM) sgp_: Any other questions?
(11:39:08 AM) sgp_: I am not entirely sure what's happening with the GUI releases
(11:39:26 AM) el00ruobuob: we do now that GUI == Later
(11:39:53 AM) el00ruobuob: *know
(11:40:27 AM) sgp_: Will there be a new GUI release for 0.14? Will it just be repackaged 0.13 with only the monerod upgrades?
(11:40:41 AM) el00ruobuob: but i hope it will come along with 0.14.1 GA
(11:42:08 AM) sgp_: If there will be no new GUI release before the upgrade, we should definitely start telling people
(11:42:27 AM) sgp_: vp11: do you know if there will be a release before the upgrade, and if so, what changes it will include?
(11:43:42 AM) sgp_: Perhaps we can come back to this
(11:43:56 AM) sgp_: I'm personally still a bit confused on the GUI release schedule
(11:44:04 AM) sgp_: 6. Community PoW discussion (RandomX)
(11:44:24 AM) sgp_: As mentioned earlier in the community updates, the last few weeks were mostly consumed with PoW dsicussions
(11:46:11 AM) sgp_: I wanted to reserve some time here for people to express their opinions and to have a more real-time discussion
(11:46:19 AM) oneiric_: what are the benefits/consequences of bricking/seriously crippling GPU miners with RandomX?
(11:47:32 AM) el00ruobuob: is it the same PoW used in the latest wownero HF (+ the last minute tweak)?
(11:47:53 AM) sgp_: el00ruobuob: yes
(11:48:10 AM) el00ruobuob: oneiric_, perf numbers seems close to CN/v2 on GPUs, what do you mean?
(11:48:25 AM) sgp_: oneiric_: this is a heated topic but I can try to provide some high-level pros/cons
(11:48:36 AM) ErCiccione[m]: I have to go folks. Will read the logs later, have a good meeting
(11:48:59 AM) oneiric_: bye c:
(11:50:29 AM) dEBRUYNE: <sgp_> Will there be a new GUI release for 0.14? <= New release
(11:50:59 AM) oneiric_: nice dEBRUYNE +1
(11:51:14 AM) sgp_: Pros of CPU-preferred: more commodotized, highly-available, everyone has one, harder to build ASICs for, often harder to scale
(11:51:14 AM) sgp_: Cons: more likely for botnets to mine
(11:51:14 AM) sgp_: Neutral: 4GB RAM requirement disables web miners
(11:51:14 AM) dEBRUYNE: For the GUI repacking 0.13.0.4 makes little sense imo
(11:51:21 AM) sgp_: I'm probably missing something
(11:51:36 AM) dEBRUYNE: A full new release will also allow us to get proper test reports (via users using the new version)
(11:51:40 AM) sgp_: neutral means "depending on your perspective" :p
(11:51:46 AM) sgp_: thanks dEBRUYNE
(11:52:13 AM) oneiric_: web miner can't get access to 4GB ram with HTML5 canvas and WebGL?
(11:52:25 AM) sgp_: I think there's a 2GB cap per tab
(11:52:30 AM) sgp_: by default
(11:52:42 AM) oneiric_: and as an extension?
(11:52:47 AM) dEBRUYNE: <sgp_> el00ruobuob: yes <= Isn't wownero implementing CryptoNightR?
(11:52:57 AM) sgp_: no idea, maybe could grab more as an extension
(11:53:45 AM) oneiric_: yeah, i liked the idea hyc or someone brought up of microservices/payments via hash-for-service
(11:54:24 AM) oneiric_: so if its possible with CryptonightR, and that doesn't brick GPU, why RandomX?
(11:54:24 AM) sgp_: speaking of that, I wonder if MoneroWorld premium is getting anywhere
(11:54:32 AM) ***sgp_ Justin will check later
(11:54:58 AM) sgp_: oneiric_: CryptoNightR doesn't claim to be highly ASIC-resistant
(11:56:19 AM) oneiric_: right, and RandomX is a total departure from Cryptonight
(11:56:43 AM) sgp_: yes
(11:56:53 AM) sgp_: Super informal fun poll: https://www.strawpoll.me/17441546
(11:57:20 AM) oneiric_: guess what i'm really getting at: is it possible to have comparable GPU performance on RandomX? is that desirable? is bricking GPU desirable, similar to bricking ASIC?
(11:57:55 AM) sgp_: oneiric_: I think most people don't have the requirement to weaken GPUs. I think it's mostly regarded as a necessary consequence
(11:58:17 AM) oneiric_: why necessary
(11:58:46 AM) oneiric_: no one has given me a good, straight answer on *why* RandomX *must* brick GPU
(11:58:56 AM) sgp_: because hyc and others can't think of as-good ways to make something work well with GPUs but not ASICs
(12:00:07 PM) sgp_: 3 votes at the poll, keep them coming!
(12:00:13 PM) sgp_: what a lively Monero community :p
(12:00:15 PM) oneiric_: ok, is that because of the compilation needed to run the random programs?
(12:00:43 PM) sgp_: oneiric_: hyc can speak in more detail than I can, but CPUs are better at handling this randomness than GPUs
(12:01:14 PM) sgp_: Once it's less random and built for GPUs, ASICs stand a better chance of getting performance boosts
(12:01:18 PM) oneiric_: sure, will ask hyc in #monero-pow, thanks for the high-level discussion sgp_
(12:01:53 PM) sgp_: Any other PoW questions or comments?
(12:02:06 PM) sgp_: We had some heated ones the past week in other channels
(12:03:00 PM) sgp_: All right then
(12:03:06 PM) sgp_: 7. Open ideas time
(12:03:23 PM) sgp_: Does anyone have a comment on something we did not already talk about?
(12:04:12 PM) sgp_: going once
(12:04:15 PM) xmrmatterbridge [~xmrmatter@lists.getmonero.org] entered the room.
(12:04:39 PM) el00ruobuob: not really, but i'm listening
(12:04:58 PM) sgp_: going twice
(12:05:10 PM) oneiric_: congrats on the breaking monero series and breaking zcash
(12:05:16 PM) sgp_: thanks!
(12:05:39 PM) sgp_: we have a lot of fun recording those
(12:05:59 PM) sgp_: 8. Confirm next meeting date/time
(12:06:04 PM) sgp_: The next community meeting will be in 2 weeks on 2 March at 17:00 UTC.
(12:06:15 PM) sgp_: The next Monero Coffee Chat will take place next Saturday on 9 March at 17:00 UTC.
(12:06:23 PM) sgp_: we can have a countdown party lol
(12:06:30 PM) sgp_: When in doubt, use the calendar: https://xmr.ncrypt.sh/index.php/apps/calendar/p/8dP6z6XQDnkPREo4/Monero-Meetings
(12:06:34 PM) sgp_: 9. Conclusion
(12:06:43 PM) sgp_: That’s all! Thanks for attending this Monero Community meeting, and we hope to see you on r/MoneroCommunity and #monero-community. Take care, and know that change starts with YOU.

# Action History
- Created by: SamsungGalaxyPlayer | 2019-02-12T21:08:32+00:00
- Closed at: 2019-02-16T18:07:24+00:00
