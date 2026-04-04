---
title: 'Research meeting (Tuesday): 14 May 2019 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/344
author: SarangNoether
assignees: []
labels: []
created_at: '2019-05-10T20:33:39+00:00'
updated_at: '2019-05-14T17:45:01+00:00'
type: issue
status: closed
closed_at: '2019-05-14T17:45:01+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Tuesday, 14 May 2019 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable

3. General questions

4. Action items

# Discussion History
## SarangNoether | 2019-05-14T17:45:01+00:00
    [2019-05-14 13:00:34] <sarang> Agenda: https://github.com/monero-project/meta/issues/344
    [2019-05-14 13:00:39] <sarang> Logs of this meeting will be posted there
    [2019-05-14 13:00:45] <sarang> GREETINGS
    [2019-05-14 13:01:53] <suraeNoether> howdy!
    [2019-05-14 13:02:02] <suraeNoether> how is everyone?
    [2019-05-14 13:02:08] <suraeNoether> who had fun at MCC? *this guy*
    [2019-05-14 13:03:00] <suraeNoether> okay
    [2019-05-14 13:03:02] <suraeNoether> well let's beign
    [2019-05-14 13:03:06] <suraeNoether> begin*
    [2019-05-14 13:03:12] <suraeNoether> for the roundtable portion
    [2019-05-14 13:03:23] <suraeNoether> let's start with general questions from the audience, and let's go around and see if anyone has anything to present
    [2019-05-14 13:03:28] ← msvb-mob left (~msvb-lab@monero/hardware/michael): "Leaving"
    [2019-05-14 13:04:39] <suraeNoether> other than sarang and i anyway
    [2019-05-14 13:04:41] <sarang> Heh, I suppose we can move to presentations
    [2019-05-14 13:04:45] <suraeNoether> yup
    [2019-05-14 13:04:49] <sarang> go ahead suraeNoether 
    [2019-05-14 13:04:50] <suraeNoether> go ahead sir
    [2019-05-14 13:04:52] <suraeNoether> ahah
    [2019-05-14 13:04:52] <sarang> jinx
    [2019-05-14 13:04:56] <suraeNoether> okay
    [2019-05-14 13:05:37] <suraeNoether> well, CLSAG paper is undergoing the final round the corner. sarang and i are working on the final details today with randomrun, and i hope we can make a public version of the paper available in the next several days (unless some flaw is found)
    [2019-05-14 13:05:59] <sarang> Yeah, just need that timing data and a definite answer on the hash coeffs in the proof
    [2019-05-14 13:06:02] <suraeNoether> DLSAG paper is undergoing further review, but I believe we are putting up an IACR version of that in the coming days also
    [2019-05-14 13:06:14] <sarang> Yep, waiting on all authors to sign off
    [2019-05-14 13:06:48] ⇐ rottensox quit (~rottensox@unaffiliated/rottensox): Ping timeout: 252 seconds
    [2019-05-14 13:06:49] <suraeNoether> MRL11 is still in progress, but now that clsag and dlsag are off my plate, it's being cranked up in terms of priority
    [2019-05-14 13:06:59] <suraeNoether> i anticipate rapid progress on that as well
    [2019-05-14 13:07:29] <suraeNoether> May 20-24, sarang and endogenic and I are doing the Monero workshop, and I believe we may be having Gao from Clemson come give us talks on starks and fully homomorphic encryption in the RLWE setting
    [2019-05-14 13:07:38] <suraeNoether> (sarang, we should do some studying before then together on that)
    [2019-05-14 13:07:42] <sarang> of course
    [2019-05-14 13:08:15] <suraeNoether> I gave a talk, sat on a panel, and gave an interview at the magical crypto conference
    [2019-05-14 13:08:27] <suraeNoether> all of those are up on youtube; the talk was about four different branches of research here at MRL
    [2019-05-14 13:08:43] <suraeNoether> other than that, i guess i'd prefer answering questions rather than talking myself into a rabbit hole
    [2019-05-14 13:09:01] <suraeNoether> nioc and i have had some conversations about how long-winded i can be so i'm going to zip it unless folks want more details :D
    [2019-05-14 13:09:22] <sarang> Any questions for suraeNoether on this work?
    [2019-05-14 13:09:56] ⇐ midipoet quit (uid316937@gateway/web/irccloud.com/x-kjrfedcexirgscfw): Quit: Connection closed for inactivity
    [2019-05-14 13:10:07] <suraeNoether> so, for the audience members who are new
    [2019-05-14 13:10:55] <suraeNoether> DLSAG = dual-recipient output signatures = work toward the claim-or-refund primitive that can underly smart contracts and lightning network. CLSAG = compressed signatures making the rate of growth on the monterion blockchain hopefully 25% smaller and faster to verify
    [2019-05-14 13:11:08] <suraeNoether> MRL11 = traceability resistance analysis
    [2019-05-14 13:11:27] <suraeNoether> so, work is important, hard, and slow going, but doing it right is very important to us
    [2019-05-14 13:11:31] <suraeNoether> anyway, sarang, how about yourself?
    [2019-05-14 13:11:38] <sarang> Plenty to mention
    [2019-05-14 13:12:02] → rottensox joined (~rottensox@unaffiliated/rottensox)
    [2019-05-14 13:12:06] <sarang> I had overhauled some definitions and such in the CLSAG paper, which suraeNoether has completed more edits on
    [2019-05-14 13:12:18] <sarang> In particular, some stuff on multi-asset transactions that could be enabled by this
    [2019-05-14 13:12:30] <sarang> I'll get timing data and then we can release for review
    [2019-05-14 13:12:41] <moneromooo> "multi-asset" being akin to coloured coins ?
    [2019-05-14 13:12:44] <sarang> ya
    [2019-05-14 13:13:01] <sarang> Not saying I'm recommending such a thing for us, but it's an easy application
    [2019-05-14 13:13:30] <sarang> I've been working on some draft protocols for how a Monero coinjoin could work
    [2019-05-14 13:13:41] <sarang> Right now the initial scheme requires a certain amount of trust in a dealer, but is very efficient
    [2019-05-14 13:13:47] <sarang> This is obviously not ideal
    [2019-05-14 13:14:03] <sarang> MoJoin, I call it
    [2019-05-14 13:14:23] <sarang> FWIW it doesn't leak spend data to the dealer, only the partition of inputs-and-outputs to each player in the join
    [2019-05-14 13:15:01] <sarang> sgp_ and I did two Breaking Monero episodes, one on input/output counts and one on block explorers
    [2019-05-14 13:15:07] <sarang> that's the main stuff for me
    [2019-05-14 13:15:30] <suraeNoether> oh, guys: we are deciding to extend early-bird pricing for a few more days
    [2019-05-14 13:15:42] <suraeNoether> i'll be advertising it
    [2019-05-14 13:16:09] <suraeNoether> but don't forget to get your ticket at monerokon.com before prices change, if you are still coming
    [2019-05-14 13:16:26] <suraeNoether> students are especially encouraged to attend; there will likely be partial rebates at the door for student tickets
    [2019-05-14 13:16:33] <sarang> Any particular questions for me?
    [2019-05-14 13:16:52] ⇐ SuperMcFreaky quit (808a401e@gateway/web/cgi-irc/kiwiirc.com/ip.128.138.64.30): Remote host closed the connection
    [2019-05-14 13:17:22] <suraeNoether> how many rounds of interaction in mojoin?
    [2019-05-14 13:17:23] <moneromooo> The "Gao [...] fully homomorphic" thing makes me wonder if that could not be looked at in conjunction with dealerless coinjoin :)
    [2019-05-14 13:17:27] <sarang> 3
    [2019-05-14 13:17:35] <sarang> This is minimal because of the BP MPC
    [2019-05-14 13:18:05] <suraeNoether> yeah, that's cool. moneromooo i think that's probably a safe avenue of stuff for us to talk about
    [2019-05-14 13:18:13] <sarang> Er, no... 4 rounds now, sorry
    [2019-05-14 13:18:16] <sarang> I had to make a change
    [2019-05-14 13:18:18] <suraeNoether> oh
    [2019-05-14 13:18:48] <sarang> The extra round is to avoid commitment sums being used to brute-force the partition by an observer
    [2019-05-14 13:19:23] <sarang> Making the resulting transaction identical to one not MoJoined (although the output count is something of a giveaway)
    [2019-05-14 13:20:10] <moneromooo> BTW, something I've not done in the branch is merging outputs to the same destination (originally the intent was to make Alice + Bob atomically paying Carol).
    [2019-05-14 13:20:25] <moneromooo> Would that be possible with the dealer based coinjoin ?
    [2019-05-14 13:20:43] <sarang> So A+B generate a single joint output?
    [2019-05-14 13:20:49] <moneromooo> yes.
    [2019-05-14 13:21:08] <sarang> I don't think it's possible to do the BP MPC without leaking the full mask
    [2019-05-14 13:21:21] <sarang> unless that's acceptable
    [2019-05-14 13:21:35] <moneromooo> That's fine in that case since Alice and Bob to advertise what they're paying, since each of them verifies the other does pay.
    [2019-05-14 13:21:54] <sarang> Would this assume another side channel between them that's outside of the join?
    [2019-05-14 13:22:09] <sarang> So it'd be a plug-and-play operation into a join?
    [2019-05-14 13:22:17] <moneromooo> I dunno. If you need one I guess.
    [2019-05-14 13:22:27] <sarang> Hmm
    [2019-05-14 13:22:39] <sarang> It's probably possible, under the right trust model between A+B
    [2019-05-14 13:22:54] <sarang> Of course, "probably possible" is quite the weaselworld
    [2019-05-14 13:23:18] <sgp_> I'm here and caught up, sorry for being late
    [2019-05-14 13:23:36] <sarang> hi
    [2019-05-14 13:23:38] <suraeNoether> nbd
    [2019-05-14 13:23:42] <sarang> talking coinjoin
    [2019-05-14 13:24:14] <fort3hlulz> Whats the advantage for Monero in using a CoinJoin implementation? if its better to chat later about it Ill shutup :)
    [2019-05-14 13:24:41] <suraeNoether> no, that's a great question
    [2019-05-14 13:24:53] <moneromooo> It adds another layer of privacy. If Eve looks at one tx, she can't assume anymore than all the inputs are from hte same owner.
    [2019-05-14 13:25:06] <sarang> Yeah, it tries to break the common-ownership assumption
    [2019-05-14 13:25:25] <fort3hlulz> Ah, so its a mitigation of poisoning/EAE attacks specifically? How does it affect Tx size/blockchain bloat?
    [2019-05-14 13:25:38] <sarang> My thought about the dealer model (if it's a necessity, which is yet TBD) is that under a malicious dealer assumption, you basically revert back to the current model
    [2019-05-14 13:25:50] <moneromooo> If we're lucky, smaller txes since one single BP :)
    [2019-05-14 13:28:31] <sarang> Another quick note that hyc and I had a call with Trail of Bits, an auditor who submitted a SoW
    [2019-05-14 13:28:48] <sarang> they'll be updating their numbers, and noted that another project may be interested in helping fund RandomX
    [2019-05-14 13:28:56] <sarang> We'll have a call with those folks tomorrow
    [2019-05-14 13:30:15] <hyc> Hi, just finished my other call
    [2019-05-14 13:30:19] <sarang> yo
    [2019-05-14 13:30:28] <hyc> yeah, some good stuff from Trail of Bits
    [2019-05-14 13:30:31] <fort3hlulz> Awesome, I'm excited to learn more about CoinJoin on Monero as well as CLSAG, thanks guys! Ill get out of your hair now :)
    [2019-05-14 13:30:48] <sarang> Thanks for the question fort3hlulz 
    [2019-05-14 13:31:04] <sarang> The security of coinjoins in Monero is still very much in the air
    [2019-05-14 13:31:21] <hyc> also for the benchmark freaks (like me) Huawei has offered to give me access to some servers with their newest chip, for benchmarking purposes
    [2019-05-14 13:31:51] <hyc> will be getting efficiency numbers for CN/R and RandomX on ARMv8
    [2019-05-14 13:32:19] ⇐ Dean_Guss quit (~dean@gateway/tor-sasl/deanguss): Ping timeout: 256 seconds
    [2019-05-14 13:33:15] <suraeNoether> ooooh
    [2019-05-14 13:33:19] <suraeNoether> thats... fantastic...
    [2019-05-14 13:33:37] <sarang> nice
    [2019-05-14 13:33:44] <hyc> thes guys https://e.huawei.com/us/products/cloud-computing-dc/servers/arm-based
    [2019-05-14 13:33:48] <sarang> We'll post the ToB updated SoW when they provide it
    [2019-05-14 13:33:49] <suraeNoether> and MRL marches forward into tomorrow's yesterday of the future^tm
    [2019-05-14 13:34:13] <hyc> general availability is end of June, early access is nice
    [2019-05-14 13:34:19] <hyc> that's all for me
    [2019-05-14 13:34:31] <sarang> Does anyone else have research to present?
    [2019-05-14 13:36:17] <sarang> Or general questions at all?
    [2019-05-14 13:37:08] <suraeNoether> whats the coolest plane you've flown?
    [2019-05-14 13:37:09] <luigi1113> what kind of pie do you like?
    [2019-05-14 13:37:18] <suraeNoether> berry berry
    [2019-05-14 13:37:22] <sarang> suraeNoether: commercially, or piloting myself?
    [2019-05-14 13:37:25] <suraeNoether> with greek yogurt
    [2019-05-14 13:37:27] <suraeNoether> ^ both
    [2019-05-14 13:37:38] <sarang> Commercially, Nepal
    [2019-05-14 13:37:56] <sarang> Myself, in between buildings in downtown San Francisco and the Golden Gate
    [2019-05-14 13:38:02] <sarang> which apparently is legal
    [2019-05-14 13:38:15] <suraeNoether> not place, plane, but i'll accept your answer happily
    [2019-05-14 13:38:17] <suraeNoether> that's awesome
    [2019-05-14 13:38:24] <sarang> Oh heh, didn't see that
    [2019-05-14 13:38:31] <sarang> Commercially, B787
    [2019-05-14 13:38:37] <sarang> Myself, probably a DA40
    [2019-05-14 13:38:46] <sarang> it's got the aerodynamics of a glider
    [2019-05-14 13:39:27] <sarang> WEll
    [2019-05-14 13:39:31] <sarang> Let's move to action items
    [2019-05-14 13:39:32] <sarang> suraeNoether: ?
    [2019-05-14 13:39:45] <suraeNoether> final dlsag review today
    [2019-05-14 13:39:48] <suraeNoether> mrl11 rest of the week
    [2019-05-14 13:40:00] <suraeNoether> uhmmm... and if anything else is handed back to me like clsag
    [2019-05-14 13:40:06] <sarang> word
    [2019-05-14 13:40:10] <suraeNoether> adjective
    [2019-05-14 13:40:20] <sarang> I'll get those CLSAG timings into the paper and finalize the proof question we had
    [2019-05-14 13:40:27] <sarang> Carry on with MoJoin
    [2019-05-14 13:40:38] <sarang> etc.
    [2019-05-14 13:40:51] <sarang> Any final words before we formally adjourn?
    [2019-05-14 13:41:18] <dEBRUYNE> Perhaps a blog post from CLSAG could be written (similar to the one for Bulletproofs)
    [2019-05-14 13:41:20] <suraeNoether> just excited for lunch
    [2019-05-14 13:41:29] <sarang> "Signatures. They are smaller and faster."
    [2019-05-14 13:41:33] <dEBRUYNE> I don't think many community members would understand CLSAG from the technical paper alone :P
    [2019-05-14 13:41:44] <sarang> But yes, we could do that once we're satisfied with security
    [2019-05-14 13:41:47] <sgp_> People need these blog posts or else no one will know
    [2019-05-14 13:41:50] <suraeNoether> dEBRUYNE: that would be good, yes.
    [2019-05-14 13:42:22] <sarang> All righty, thanks to everyone for attending
    [2019-05-14 13:42:30] <sarang> We are now formally adjourned; logs will appear shortly

# Action History
- Created by: SarangNoether | 2019-05-10T20:33:39+00:00
- Closed at: 2019-05-14T17:45:01+00:00
