---
title: 'Research meeting: 17 June 2019 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/358
author: SarangNoether
assignees: []
labels: []
created_at: '2019-06-14T14:04:14+00:00'
updated_at: '2019-06-17T17:49:45+00:00'
type: issue
status: closed
closed_at: '2019-06-17T17:49:45+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Monday, 17 June 2019 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable
a. Sarang: CLSAG [multisig and code](https://github.com/moneromooo-monero/bitmonero/commits/crash), Lelantus [analysis](https://github.com/SarangNoether/skunkworks/blob/lelantus/lelantus/analysis.md) and [migration code](https://github.com/SarangNoether/skunkworks/blob/lelantus/lelantus/transaction.py), Omniring analysis
b. Surae: [Monero Konferenco](https://monerokon.com)
c. Others?

3. General questions

4. Action items

# Discussion History
## SarangNoether | 2019-06-17T17:49:45+00:00
    [2019-06-17 13:02:33] <sarang> GREETINGS
    [2019-06-17 13:02:42] <parasew[m]> hello!
    [2019-06-17 13:03:22] <sarang> So much happening this week...
    [2019-06-17 13:03:36] <sarang> suraeNoether: care to go first with your roundtable? Although I can probably guess what it'll be =p
    [2019-06-17 13:04:04] <suraeNoether> yeah, just konferenco stuff this week
    [2019-06-17 13:04:08] <suraeNoether> getting banners printed, etc
    [2019-06-17 13:04:10] <sarang> super excited
    [2019-06-17 13:04:15] <suraeNoether> there are THREE free volunteer tickets available for Konferenco
    [2019-06-17 13:04:21] <suraeNoether> you just need to DM @moneroKon on twitter to set it up
    [2019-06-17 13:04:26] <sarang> Take a look at banner, Michael!
    [2019-06-17 13:04:43] <suraeNoether> exchange 6 hours of work-ish time for a free ticket to this killer event :D
    [2019-06-17 13:05:20] <suraeNoether> Basically everything is coming crashing toward us like a freight train, but we have had everything set up and waiting for its arrival for a few weeks. working with sgp on streaming and video, etc. etc.
    [2019-06-17 13:05:49] <suraeNoether> we were originally going to record the whole thing and put it on youtube, but sgp is rigging up a livestream for us, which is fantastic and saving us a few grand on A/V costs
    [2019-06-17 13:06:02] <sarang> sounds... grand
    [2019-06-17 13:06:28] <suraeNoether> other than that, i'm more here to answer questions today. i've been doing light reading for research, including piratechain and nipopow and re-reading omniring, but my productivity is going toward monkon right now
    [2019-06-17 13:06:42] <sarang> cool
    [2019-06-17 13:06:44] <suraeNoether> and to take some marching orders from sarang re: omni
    [2019-06-17 13:06:49] ⇐ crCr62U0 quit (~crCr62U0@gateway/tor-sasl/crcr62u0): Ping timeout: 256 seconds
    [2019-06-17 13:06:49] <sarang> heh
    [2019-06-17 13:06:52] <suraeNoether> and the comparative analysis paper mooo mentioned
    [2019-06-17 13:07:22] <sarang> Any questions for suraeNoether?
    [2019-06-17 13:07:31] <sarang> Now is a good time for Konferenco questions probably
    [2019-06-17 13:07:42] <sfhi> Is the livestream from Monerokon going to be via Youtube?
    [2019-06-17 13:08:19] <suraeNoether> i believe that is the case, yes
    [2019-06-17 13:08:52] <sarang> Where will be the best place for non-attendees to get information about streams and videos and relevant links?
    [2019-06-17 13:08:55] <sarang> Here? r/Monero?
    [2019-06-17 13:08:55] <suraeNoether> the joint panel with zcon1 will be streamed by them, and i'm not sure which outlet they'll be using for that; i'm 99% sure they are also using youtube
    [2019-06-17 13:08:55] <sfhi> From awareness perspective, youtube is certainly the best platform to gain views, assuming the video and audio quality are good of course
    [2019-06-17 13:09:00] <sfhi> Okaya great
    [2019-06-17 13:09:30] <suraeNoether> sarang absolutely, we'll be throwing more information up into the Monero Konferenco general megathread on reddit, including links to the streaming talks. hopefully some folks will be livetweeting and liveredditing (is that... is that a thing?) and linking to the videos
    [2019-06-17 13:09:44] <sarang> Will slides be posted?
    [2019-06-17 13:09:54] <sarang> (for those presenters who choose to / have the rights to)
    [2019-06-17 13:09:57] <sfhi> sarang: Yeah, good question!
    [2019-06-17 13:10:05] <suraeNoether> i believe sgp is currently working on rigging a way to actually integrate them with the stream, not merely post slides after the talks
    [2019-06-17 13:10:16] <sarang> Neat... would still be nice to have posted too
    [2019-06-17 13:10:20] <sarang> esp. for things like charts/plots
    [2019-06-17 13:10:43] <suraeNoether> yes, i just need to seek permission from each speaker, which I will be doing when I start receiving their slides
    [2019-06-17 13:10:49] <sarang> Cool!
    [2019-06-17 13:10:53] — suraeNoether thumbs up
    [2019-06-17 13:10:59] <sarang> I like how BPASE did it, where they add links to the schedule
    [2019-06-17 13:11:05] <sarang> Keeps it all easy to find
    [2019-06-17 13:11:12] <suraeNoether> yeah, i liked that, too
    [2019-06-17 13:11:22] <suraeNoether> in fact, i really hate the monkon website, but that's a problem for next year I think. :P
    [2019-06-17 13:11:33] <sarang> Definitely a table view for schedule next time
    [2019-06-17 13:11:36] <sfhi> Currently there are 46 student, 126 general and 43 platinium tickets left. Does anyone remember what was the original amount for each?
    [2019-06-17 13:11:39] <sarang> or a more integrated platform for it
    [2019-06-17 13:13:11] <suraeNoether> sfhi the venue has a capacity of 280, but i dont' recall exactly how many tickets i made available in each category. I *think* it was 50 for students and platinum and 150 for general
    [2019-06-17 13:13:48] <suraeNoether> but i'm also having inventory issues with our backend and we have sold (a few) more tickets than are reflected there
    [2019-06-17 13:14:12] <suraeNoether> i believe our attendance will be around 110 after we count speakers and sponsors
    [2019-06-17 13:14:21] <sfhi> Alright thx, it seems that it just now that people are getting active and buying tickets (no surprise there)
    [2019-06-17 13:14:22] <sarang> Not too shabby for a first run!
    [2019-06-17 13:14:51] <nioc> could be wrong but it may have been 200/50/50
    [2019-06-17 13:15:11] <sfhi> Okay
    [2019-06-17 13:15:13] <suraeNoether> nioc that sounds more accurate and is closer to the numbers i'm seeing in my guest list.
    [2019-06-17 13:15:38] <sfhi> Cannot attend personally, but very much looking forward to the livestream :)
    [2019-06-17 13:15:56] <sarang> Any other questions for suraeNoether?
    [2019-06-17 13:16:14] <suraeNoether> (one of my action items for AFTER the konferenco will be to make a post mortem, including financials, media outreach, stuff like that, so that next year 1) we can decentralize the thing so more people are working on it and 2) we can learn our lessons, etc, and make the second annual more of a splash.
    [2019-06-17 13:16:21] <suraeNoether> but to be honest: i'm freaking thrilled at the attendance
    [2019-06-17 13:17:23] <sarang> I've been working on a few things this week, all of which were action items for me
    [2019-06-17 13:17:59] <sgp_> That will be very useful
    [2019-06-17 13:18:00] <sarang> First was getting my MonKon presentation done... very excited to share data on how our transactions have changed over time for efficiency
    [2019-06-17 13:18:16] <parasew[m]> sgp_ has been posting on meta to use the "frab" system for monero conferences and events in the future. i can highly recommend it, have been using it for the CCC and for other events already. imho something to look for in a longer term.
    [2019-06-17 13:18:26] — sarang pauses
    [2019-06-17 13:19:52] — sarang continues
    [2019-06-17 13:20:13] <sarang> I finished an analysis of the Lelantus transaction protocol, which now includes prototyping code for Monero-to-Lelantus output migration
    [2019-06-17 13:20:18] <sarang> https://github.com/SarangNoether/skunkworks/blob/lelantus/lelantus/analysis.md
    [2019-06-17 13:20:46] <sarang> Spend (i.e. not mint or migration) transactions are around 3-4 kB, plus ring representation
    [2019-06-17 13:20:47] → rehrar joined (~rehrar@gateway/tor-sasl/rehrar)
    [2019-06-17 13:21:11] <suraeNoether> sarang, good job on that lelantus report
    [2019-06-17 13:21:15] <sarang> Verification for a 2-2 txn is ~34 ms... and a batch works out to ~13 ms/txn
    [2019-06-17 13:21:24] <suraeNoether> when you say "plus ring rep" do you mean "not including ring rep?" or do you mean "and that includes ring rep?"
    [2019-06-17 13:21:31] <sarang> not including
    [2019-06-17 13:21:38] <sarang> because that depends how it's done
    [2019-06-17 13:21:49] <suraeNoether> is the improvement in verf time due to batching dependent on the number of txns being batched?
    [2019-06-17 13:21:49] <sarang> Big giant scary caveat: every spend requires a churn
    [2019-06-17 13:21:59] <suraeNoether> ^ important
    [2019-06-17 13:22:05] <sarang> suraeNoether: yes, of course
    [2019-06-17 13:22:20] <sarang> Many multiexp generators are shared
    [2019-06-17 13:22:28] <suraeNoether> so when you say the batch works out to 13 ms/txn... oh that's per txn
    [2019-06-17 13:22:33] <sarang> so the cost is amortized across all proofs for these generators
    [2019-06-17 13:22:33] <suraeNoether> *hits forehead*
    [2019-06-17 13:22:46] <sarang> I assume batched txns do _not_ share ring members
    [2019-06-17 13:22:58] <suraeNoether> so that's room for increased speed, too
    [2019-06-17 13:23:10] <sarang> btw those numbers are for 128-rings
    [2019-06-17 13:23:20] <suraeNoether> can you give us some intuition about what about the lelantus protocol requires the churn? is it the key image?
    [2019-06-17 13:23:28] <sarang> Increasing to, say, 1024-rings bumps the batch ver time to ~80 ms each
    [2019-06-17 13:23:38] <sarang> Well, serial numbers for the commitments
    [2019-06-17 13:23:59] <sarang> Those are revealed at spend time, and the original sender knows it too
    [2019-06-17 13:24:13] <sarang> A churn is required so that sender no longer knows the serial number at next spend tiem
    [2019-06-17 13:24:16] ⇐ bsm1175321 quit (~mcelrath@c-24-61-184-150.hsd1.ma.comcast.net): Ping timeout: 272 seconds
    [2019-06-17 13:24:28] <suraeNoether> sarang, do you mind if i publicly share the report you just publicly shared?
    [2019-06-17 13:24:45] <sarang> Yes, but... all the data contained therein has _not_ been verified by anyone else
    [2019-06-17 13:24:59] <sarang> and in fact, I'd like one of your action items, suraeNoether, to be checking my math
    [2019-06-17 13:25:07] <sarang> It's possible there are glaring problems with it
    [2019-06-17 13:25:49] <suraeNoether> want me to do checking before i share it, then, instead of the other way around? :P
    [2019-06-17 13:25:55] <sarang> Up to you!
    [2019-06-17 13:26:16] <sarang> I have been working with one of the Omniring authors to do the same analysis for that construction
    [2019-06-17 13:26:28] <sarang> that is not finished
    [2019-06-17 13:26:52] <sarang> Finally, moneromooo has taken my CLSAG code and fully integrated it into a branch for testing
    [2019-06-17 13:27:12] <sarang> moneromooo and I got it working for multisig and tweaked things a bit for non-malleability
    [2019-06-17 13:27:21] <sarang> https://github.com/moneromooo-monero/bitmonero/commits/crash
    [2019-06-17 13:27:34] <sarang> I am currently soliciting auditors for that code... no word yet
    [2019-06-17 13:27:35] <suraeNoether> yay!
    [2019-06-17 13:27:42] <suraeNoether> that's super exciting, sarang and moneromooo !
    [2019-06-17 13:28:06] <moneromooo> (it'll be in a separate branch for review, it's just in crash for convenience for now)
    [2019-06-17 13:28:15] <sarang> roger
    [2019-06-17 13:28:43] <rehrar> may I ask a question/make a suggestion for MRLs consideration?
    [2019-06-17 13:28:43] <sarang> As far as ACTION ITEMS go, mine is to complete the Omniring review, which will be a good check against the authors, who are doing the same
    [2019-06-17 13:28:47] <sarang> rehrar: sure
    [2019-06-17 13:28:53] <rehrar> Sorry if I'm dropping this at a poor time, but I am about to leave for something.
    [2019-06-17 13:29:06] <sarang> np
    [2019-06-17 13:29:19] <rehrar> One of the big issues we have had in the past with regards to definitive statements on privacy/fungibility is the fact that the "adversary" is always poorly defined.
    [2019-06-17 13:29:45] <sarang> Yes, because formalizing it is very tricky when done precisely
    [2019-06-17 13:29:54] <rehrar> Threat models are vast and varied, and so making a blanket statement about Monero's abilities to protect is fool hardy, and would lead to some believing it would help them when it wouldn't or ice versa
    [2019-06-17 13:30:27] <rehrar> But not doing anything about this leaves us floating in a strange limbo like state where no claims are made, except for the ambiguous ones like "private digital money"
    [2019-06-17 13:30:55] <rehrar> my suggestion is for the MRL to put out a bulletin or paper or whatever, where there common threat models are chosen (of varying severity), along with some assumptions about the adversaries in those models.
    [2019-06-17 13:31:03] <sarang> Yeah, this has been brought up a few times
    [2019-06-17 13:31:14] <rehrar> And Monero's ability to protect and keep things private is held against these three standards.
    [2019-06-17 13:31:17] <sarang> Part of me cringes every time, because you end up making such specific threat models
    [2019-06-17 13:31:26] <suraeNoether> it's worth noting, rehrar, that formalizing "the adversary" for ring confidential transactions is an active area of research. one of the reasons omniring is interesting (and one of ruffing's previous prints with a sublinear scheme) is that they were able to formalize a variety of threat models that had not yet been formalized
    [2019-06-17 13:31:40] <rehrar> At the very least, this gives us something to point to
    [2019-06-17 13:31:57] <Isthmus> I would be happy to contribute toward "an incomplete list of adversary models"
    [2019-06-17 13:32:00] <sarang> The big issue is external data
    [2019-06-17 13:32:09] <sarang> We can prove all sorts of things within the cryptography itself
    [2019-06-17 13:32:27] <sarang> but throw in things like "my ISP and my exchange are in contact with the government" and all the formal analysis falls apart
    [2019-06-17 13:32:29] <rehrar> sarang: right, but we don't know the extent of power the ambiguous "threat" has
    [2019-06-17 13:32:58] <rehrar> still, despite this, I see projects like tor and I2p have stated threat models that they will defend against, with "no guarantees" for anything else
    [2019-06-17 13:33:14] <suraeNoether> rehrar tor and I2p have literal security definitions to compare against
    [2019-06-17 13:33:16] <rehrar> and I would like to see Monero, being a respectable privacy project like it is, have something similar
    [2019-06-17 13:33:27] <suraeNoether> that's after several decades of research into private networking
    [2019-06-17 13:33:32] <suraeNoether> and mixnets, and so on
    [2019-06-17 13:33:36] <rehrar> hmmm...I see
    [2019-06-17 13:33:41] <suraeNoether> in one sense, what you are describing is exactly our job at MRL
    [2019-06-17 13:33:47] <suraeNoether> it just may take a *loooong* time
    [2019-06-17 13:33:52] <rehrar> well this perspective is helpful then
    [2019-06-17 13:34:02] <suraeNoether> in fact, some of the security models in the omni paper are relevant here
    [2019-06-17 13:34:14] <suraeNoether> and one of my security models in my ongoing churn analysis is also relevant
    [2019-06-17 13:34:20] <sarang> Yeah, you're taking many layers (signature schemes, proof of work, network layer, communication between colluding adversaries, graph analysis) and throwing them all together
    [2019-06-17 13:34:36] <suraeNoether> compiling a comprehensive source for all this? very important work. but ...
    [2019-06-17 13:35:03] <suraeNoether> but you are right: we should start collecting our security assumptions in a common and easily referenced locations so that we can point to them later
    [2019-06-17 13:35:14] <suraeNoether> having anything in this regard is going to be better than completely ignoring it and being vague
    [2019-06-17 13:35:18] <sarang> Still, I agree that it's good to think about. Part of why we did Breaking Monero was to try to peel apart some of these threats and explain them
    [2019-06-17 13:35:26] <suraeNoether> ^ *nod*
    [2019-06-17 13:35:46] <rehrar> I see. Thank you for the explanation.
    [2019-06-17 13:35:55] <rehrar> I do see the gigantic difference between Tor and Monero fwiw
    [2019-06-17 13:36:10] <rehrar> Tor is just networking/mixnet stuff, and that's just ONE FACET of Monero's security stuffs
    [2019-06-17 13:36:27] <rehrar> anyways, just thought I'd pop that out for consideration (again, evidently)
    [2019-06-17 13:36:35] <sarang> A very good topic to keep in mind, though
    [2019-06-17 13:36:37] <rehrar> thank you for entertaining me in this matter. :)
    [2019-06-17 13:36:45] <rehrar> have to split. Carry on.
    [2019-06-17 13:36:52] <sarang> thanks rehrar, see ya
    [2019-06-17 13:37:13] <sarang> My action items, besides giving a kickass MonKon talk, will be to continue Omniring analysis much in the same way that I did for Lelantus
    [2019-06-17 13:37:21] <sarang> and to continue further review of the code in moneromooo's branch
    [2019-06-17 13:37:32] <sarang> additional eyes on it, especially for multisig, would be welcome
    [2019-06-17 13:37:55] ⇐ MRL-discord quit (~MRL-disco@li501-43.members.linode.com): Remote host closed the connection
    [2019-06-17 13:38:09] → MRL-discord joined (~MRL-disco@li501-43.members.linode.com)
    [2019-06-17 13:38:25] <sarang> Also a huge thanks to everyone who supported my CCS funding request, either financially or in spirit
    [2019-06-17 13:38:28] <suraeNoether> i'll review those numbers to the best of my ability today after I get back from a few printshops (banners and stuff)
    [2019-06-17 13:38:31] <suraeNoether> OH GOD THE CCS
    [2019-06-17 13:38:32] <sarang> ty suraeNoether 
    [2019-06-17 13:38:38] — suraeNoether sighs
    [2019-06-17 13:39:10] <sarang> Speaking of action items... what are yours, suraeNoether? :D
    [2019-06-17 13:39:11] <suraeNoether> my action items are to write my research report for the past 90 days, request my funding for the next 90 days, to put on this conference, to review sarang's numbers, and to finally submit the thring signature paper to a peer-reviewed journal
    [2019-06-17 13:40:03] <sarang> Were there any questions on my work the past week?
    [2019-06-17 13:40:06] <sarang> (forgot to ask)
    [2019-06-17 13:40:54] <suraeNoether> in the past 6 months, MRL has put out 3 signature papers (thring sigs, clsag, dlsag), is hosting a conference, has attended two workshops, has had a public presence at MCC, and has put out several episodes of breaking monero. this has been a good couple of months. good job sarang, good job sgp, good job isthmus, good job moneromooo, and everyone else who has contributed
    [2019-06-17 13:41:32] <sarang> Plenty more to do :/
    [2019-06-17 13:42:15] <sarang> but that's the point of research :D
    [2019-06-17 13:42:29] <sarang> OK, anything else to cover before we formally adjourn?
    [2019-06-17 13:43:08] <sarang> going once
    [2019-06-17 13:43:13] <suraeNoether> OH OH
    [2019-06-17 13:43:19] <suraeNoether> i think i mentioned it but i'll say it again
    [2019-06-17 13:43:42] <suraeNoether> we have a few FREE volunteer tickets for konferenco. trade 6 hours of volunteer work checking people in and setting up tables, come to konferenco for free! DM @monerokon on twitter.
    [2019-06-17 13:43:48] <suraeNoether> aaand now i'm done
    [2019-06-17 13:43:59] <Isthmus> My action items are just finishing up slides and trying to not miss my flight
    [2019-06-17 13:44:05] <sarang> heh, nice!
    [2019-06-17 13:44:09] <sarang> OK, going twice...
    [2019-06-17 13:44:13] <Isthmus> Ooh and brainstorming about incomplete adversary list
    [2019-06-17 13:44:19] <sarang> going thrice...
    [2019-06-17 13:44:28] <sarang> Adjourned!

# Action History
- Created by: SarangNoether | 2019-06-14T14:04:14+00:00
- Closed at: 2019-06-17T17:49:45+00:00
