---
title: 'Research meeting: 30 December 2019 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/423
author: SarangNoether
assignees: []
labels: []
created_at: '2019-12-26T23:25:55+00:00'
updated_at: '2019-12-30T18:03:14+00:00'
type: issue
status: closed
closed_at: '2019-12-30T18:03:14+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Monday, 30 December 2019 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable

3. Questions

4. Action items

# Discussion History
## SarangNoether | 2019-12-30T18:03:14+00:00
    [2019-12-30 12:01:56] <suraeNoether> welcome everyone, to the last MRL research meeting of the year
    [2019-12-30 12:02:09] <suraeNoether> if i had thought about it, i'd have something more in-depth prepared but it just occurred to me ;P
    [2019-12-30 12:02:17] <suraeNoether> let's start with 1) GREETINGS
    [2019-12-30 12:02:36] <endogenic> o/
    [2019-12-30 12:02:38] <sarang> hi
    [2019-12-30 12:02:49] <suraeNoether> good and you, oh not so bad
    [2019-12-30 12:03:10] <suraeNoether> isthmus was here mere moments ago
    [2019-12-30 12:03:35] <Isthmus> Kind of. Splitting headache. Looking at screen intermittently.
    [2019-12-30 12:03:41] <sarang> yikes
    [2019-12-30 12:03:44] <endogenic> :(
    [2019-12-30 12:04:08] <Isthmus> C'est la vie.
    [2019-12-30 12:04:16] <suraeNoether> okay, well; go away isthmus and come back when you're healthy
    [2019-12-30 12:04:23] <suraeNoether> you'll get us all sick with headaches left and right
    [2019-12-30 12:04:32] <endogenic> i have a headache now
    [2019-12-30 12:04:39] <Isthmus> See, we should just ban headaches at the protocol level
    [2019-12-30 12:04:42] <Isthmus> Not just in the wallet.
    [2019-12-30 12:04:45] <suraeNoether> no your headache now
    [2019-12-30 12:05:10] <suraeNoether> before we move onto 2) ROUNDTABLE I would like to bring up a single administrative issue
    [2019-12-30 12:05:35] <suraeNoether> i would like to propose that we consider switching meeting times; we selected 17 UTC mondays essentially at random about 2 years ago
    [2019-12-30 12:05:35] <sarang> ?
    [2019-12-30 12:05:47] <sarang> What's a preferred time?
    [2019-12-30 12:05:50] <suraeNoether> nowadays, not all of our participants easily are able to attend that time, so often it's just sarang and i
    [2019-12-30 12:06:18] <suraeNoether> so while i don't have a lot of time constraints, i wanted to hear from folks like isthmus who oftentimes have meetings at around the same time
    [2019-12-30 12:06:24] <suraeNoether> and open the room up for general discussion about timing for meetings
    [2019-12-30 12:06:31] <Isthmus> ty
    [2019-12-30 12:06:36] <suraeNoether> i know this is boring, but it's been on my mind for more than a month now
    [2019-12-30 12:06:58] <sarang> Suggestions on a better time?
    [2019-12-30 12:07:09] <endogenic> an hr fro
    [2019-12-30 12:07:09] <Isthmus> I'm normally on Pacific time so Monday 1700 UTC is early and right when I'm getting swamped at the office
    [2019-12-30 12:07:12] <endogenic> m now?
    [2019-12-30 12:07:17] <endogenic> nm
    [2019-12-30 12:07:24] <Isthmus> I'm just here now cuz on holiday & EST
    [2019-12-30 12:07:30] <sarang> How about 18:00 or 19:00 UTC?
    [2019-12-30 12:07:32] <endogenic> Weds?
    [2019-12-30 12:07:38] <Isthmus> Weds at 18 or 19 would be better
    [2019-12-30 12:07:55] <Isthmus> In that case, I think I could block it on my work calendar as a recurring event
    [2019-12-30 12:08:11] <sarang> We could always try a new datetime out and see how it goes
    [2019-12-30 12:08:27] <suraeNoether> i second wednesdays at 18-19 UTC provisionally for the first month of the year just to see how it works out re: participation
    [2019-12-30 12:08:29] <sarang> I make sure the topic bar shows the meeting datetime
    [2019-12-30 12:08:32] <Isthmus> +1
    [2019-12-30 12:08:39] <sarang> OK, Wednesday at 18:00 UTC it is
    [2019-12-30 12:08:51] <Isthmus> Thanks! Will be very helpful for me.
    [2019-12-30 12:09:10] <suraeNoether> okay, neato burrito
    [2019-12-30 12:09:15] <suraeNoether> onto 2) ROUNDTABLE
    [2019-12-30 12:09:18] ← lapav[m] left (lapavjunta@gateway/shell/matrix.org/x-dzuxxriyrdtwrngs): "Kicked by @appservice-irc:matrix.org  : User has been idle for 30+ days."
    [2019-12-30 12:09:52] <suraeNoether> since the holidays were last week, maybe we can make this not just a "here's what I did last week" thing but also a "here's what we did this year" thing, but that could end up being a... surprisingly long list
    [2019-12-30 12:10:04] <suraeNoether> but we don't have to go in-depth
    [2019-12-30 12:10:32] <suraeNoether> sarang or isthmus, do you guys want to begin? wait, no, isthmus: go away and treat your headache
    [2019-12-30 12:10:38] <sarang> I finished up a draft MPC for the aggregated version of RCT3 this past week
    [2019-12-30 12:10:59] <sarang> And am currently in the weeds with some Omniring stuff that has been puzzling
    [2019-12-30 12:11:26] <sarang> Additionally, my funding request is open: https://ccs.getmonero.org/proposals/sarang-2020-q1.html
    [2019-12-30 12:11:35] <suraeNoether> i strongly recommend that everyone donate to sarang's funding request
    [2019-12-30 12:11:44] <suraeNoether> well, i mean, whatever you are comfortable with
    [2019-12-30 12:11:48] <sarang> and I'm on pins and needles for any comments from suraeNoether on CLSAG or Triptych preprint updates
    [2019-12-30 12:12:09] <suraeNoether> what i mean to say is: this is a valuable request, and if you have been considering donating to the CCS but don't know where your money will have a big impact, sarang's fund is a high priority ticket imho
    [2019-12-30 12:12:22] <sarang> Much appreciation for all the support
    [2019-12-30 12:12:42] ← iarp[m] left (iarpavareb@gateway/shell/matrix.org/x-ifbxiqlcqmalajrx): "Kicked by @appservice-irc:matrix.org  : User has been idle for 30+ days."
    [2019-12-30 12:12:51] <sarang> I'm eager to see what the next year holds in the research space, particularly relating to transaction protocols
    [2019-12-30 12:13:16] ⇐ jeeg[m] quit (jeegkdeorg@gateway/shell/matrix.org/x-jzqltxxlzatvdmuj): Remote host closed the connection
    [2019-12-30 12:14:21] <Isthmus> Yea, what's our research theme for 2020
    [2019-12-30 12:14:37] <Isthmus> I'll obviously continue to be a huge PITA about information leaks
    [2019-12-30 12:14:45] <sarang> yes plz
    [2019-12-30 12:15:03] ← nartir[m] left (nartirlinu@gateway/shell/matrix.org/x-yajxrtvlwrjqgpiw): "Kicked by @appservice-irc:matrix.org  : User has been idle for 30+ days."
    [2019-12-30 12:15:19] <sarang> "2020: zero knowledge, infinite heart"?
    [2019-12-30 12:15:40] <Isthmus> Ring size 2020?
    [2019-12-30 12:15:43] <Isthmus> Oh wait, it's not a prime number
    [2019-12-30 12:16:24] <sarang> People are going to think there's a technical reason for having prime-number ring sizes :/
    [2019-12-30 12:17:04] <sarang> Interestingly, for some protocols, you specifically _can't_ have a prime number size!
    [2019-12-30 12:17:34] ← chris[m]5 left (chrispriva@gateway/shell/matrix.org/x-rfovhynzhwrghozf): "Kicked by @appservice-irc:matrix.org  : User has been idle for 30+ days."
    [2019-12-30 12:19:07] <suraeNoether> for any merkle-tree based approach, you have to stick with powers of 2
    [2019-12-30 12:19:28] <suraeNoether> for 2020, a few things i'd like would be a formal protocol specification for a tryptich-based protocol, using ristretto, going down to the nitty gritty details of optimized arithmetic, tor integration, etc
    [2019-12-30 12:20:44] → WhatDo joined (~Android@2600:8805:4806:5400:b44a:de96:4129:6262)
    [2019-12-30 12:22:44] ⇐ WhatDo_ quit (~Android@2607:fb90:d614:858c:0:9:8ff9:4b01): Ping timeout: 248 seconds
    [2019-12-30 12:22:49] <suraeNoether> thing is, i think we are eventually going to need to abandon the DL setting for efficiency and security reasons; either switching to multilinear pairings may be necessary for efficiency, but still boils down to computational security. on the other hand, switching to other hardness assumptions like RLWE, which are believed to be quantum-secure, is an area of active research. that assumption also has a
    [2019-12-30 12:22:49] <suraeNoether> very different profile for use in cryptocurrencies because key sizes and signature verification speeds are very different in the new setting
    [2019-12-30 12:23:01] ← jact[m] left (jactopenin@gateway/shell/matrix.org/x-ecrgwmxmhftgqdlf): "Kicked by @appservice-irc:matrix.org  : User has been idle for 30+ days."
    [2019-12-30 12:23:45] <suraeNoether> my roundtable contribution from this past week: i got flu-like symptoms after xmas, so all I could do was sit around and be grumpy, so I ... copy-edited triptych and clsag
    [2019-12-30 12:23:54] <suraeNoether> (best thing to do when grumpy is to grade papers???)
    [2019-12-30 12:24:04] <sarang> Looking forward to your notes on those
    [2019-12-30 12:24:14] <suraeNoether> should be before 3PM today
    [2019-12-30 12:24:22] <sarang> Hooray!
    [2019-12-30 12:24:31] <sarang> It's a Festivus miracle!
    [2019-12-30 12:24:45] <suraeNoether> i'll be switching back to matching simulation stuff literally next year
    [2019-12-30 12:25:07] <suraeNoether> festivus miracles involve being able to use the aluminum pole on your grievances
    [2019-12-30 12:25:54] <endogenic> i dont get that reference but i will google
    [2019-12-30 12:26:15] <sarang> I'll be continuing a deep-dive into some Omniring stuff this week, to determine if an issue I ran into presents a problem with any of the proofs
    [2019-12-30 12:26:48] <Isthmus> My roundtable is still plotting, but should be rendered shortly
    [2019-12-30 12:26:51] <suraeNoether> after recovering from the flu, or whatever i had, though, i have to say: i feel like a million bucks and i'm super excited to finish off triptych today
    [2019-12-30 12:27:03] <suraeNoether> endo and isthmus and sarang can all attest to the number of times per year i say i feel like a million bucks
    [2019-12-30 12:27:20] <Isthmus> :- )
    [2019-12-30 12:27:29] <endogenic> 1/4 times per year so far
    [2019-12-30 12:28:04] ⇐ olmvnec[m] quit (olmvnected@gateway/shell/matrix.org/x-eboiahqzntvscsfa): Remote host closed the connection
    [2019-12-30 12:28:19] <suraeNoether> when the moon hits your eye like a big pizza pie, thatsa N=1
    [2019-12-30 12:28:59] <Isthmus> Ah, here we go
    [2019-12-30 12:29:03] <endogenic> i feel for the transcription translators who do these logs
    [2019-12-30 12:29:03] ⇐ ronald[m]1 quit (ronaldriot@gateway/shell/matrix.org/x-safsxmfmfzlmynib): Quit: User has been idle for 30+ days.
    [2019-12-30 12:29:37] ← pothyurf[m] left (pothyurfcy@gateway/shell/matrix.org/x-kflznnsnjugnurki): "Kicked by @appservice-irc:matrix.org  : User has been idle for 30+ days."
    [2019-12-30 12:29:51] — Isthmus chuckles
    [2019-12-30 12:29:53] <Isthmus> https://usercontent.irccloud-cdn.com/file/ntGPLKhz/image.png
    [2019-12-30 12:30:11] <Isthmus> ^ non-coinbase TXNs as of late
    [2019-12-30 12:30:17] <suraeNoether> oh my fkn god
    [2019-12-30 12:30:26] <Isthmus> I zoomed in on lower values there, there are some absurd outliers
    [2019-12-30 12:30:27] <Isthmus> https://usercontent.irccloud-cdn.com/file/Uz5uJDlS/image.png
    [2019-12-30 12:30:35] <suraeNoether> so i like the idea of having an adjustable unlock time for smart contract reasons. ...
    [2019-12-30 12:30:57] <endogenic> for m'kids
    [2019-12-30 12:31:01] <suraeNoether> hey, sarang: think the range proof technique for the trigger block height in DLSAG could be janked around to hide *all unlock times*?
    [2019-12-30 12:31:20] <Isthmus> https://usercontent.irccloud-cdn.com/file/xS32XCWP/image.png
    [2019-12-30 12:31:23] <Isthmus> ^ All from the last few months
    [2019-12-30 12:31:29] <Isthmus> Excluding the giant ones
    [2019-12-30 12:31:39] <sarang> I believe it could
    [2019-12-30 12:32:18] <Isthmus> Apparently unlock_time supports both unix timestamps and height... There are 13 transactions that used UNIX time and the rest are height-based
    [2019-12-30 12:32:41] <sarang> unix timestamps? did not know that
    [2019-12-30 12:32:49] <Isthmus> There's one transaction whose outputs will unlock in the year 46000, lol
    [2019-12-30 12:32:54] <suraeNoether> hmmmm
    [2019-12-30 12:33:02] <suraeNoether> i can't think of a good reason to allow unix timestamps
    [2019-12-30 12:33:26] <endogenic> who uses unlock time currently?
    [2019-12-30 12:33:45] <suraeNoether> costs of hiding all unlock times is a new range proof, but that can be batched with bulletproofs... and variable unlock times are desirable for smart contracting...
    [2019-12-30 12:33:55] <Isthmus> @endogenic apparently 8 different sets of people, and they all use it differently
    [2019-12-30 12:33:57] <Isthmus> xD
    [2019-12-30 12:34:05] <endogenic> lol
    [2019-12-30 12:34:06] <suraeNoether> the DLSAG connection is strong with this
    [2019-12-30 12:34:16] <endogenic> surae is one of them
    [2019-12-30 12:34:28] <Isthmus> https://xmrchain.net/search?value=2c2762d8817ea4d1cb667752698f2ff7597a051d433043776945669043d908b5
    [2019-12-30 12:34:28] <Isthmus>   "unlock_time": 1420722551128,
    [2019-12-30 12:34:34] <suraeNoether> i'm *really* bad at monero
    [2019-12-30 12:34:35] <sarang> Not only batched, but aggregated for logarithmic size benefits
    [2019-12-30 12:35:01] <suraeNoether> can anyone think of a good reason to keep unlock time in plaintext?
    [2019-12-30 12:35:17] <endogenic> auditability
    [2019-12-30 12:35:24] <sarang> It's also smaller
    [2019-12-30 12:35:25] <endogenic> forgive me monero gods
    [2019-12-30 12:35:33] ← kobold[m] left (koboldkdeo@gateway/shell/matrix.org/x-eehuyzhmojntkrds): "Kicked by @appservice-irc:matrix.org  : User has been idle for 30+ days."
    [2019-12-30 12:35:37] <sarang> Otherwise you have to put it into a commitment
    [2019-12-30 12:35:38] <Isthmus> What is the point of unlock time?
    [2019-12-30 12:35:39] <Isthmus> Serious question.
    [2019-12-30 12:35:58] <Isthmus> I need to understand the intended use cases to figure out how we should handle it
    [2019-12-30 12:36:07] <moneromooo> A reason to use UNIX timestamps is to not depend on block time changes.
    [2019-12-30 12:36:16] <endogenic> (unreclaimable) vesting period; force-hodl
    [2019-12-30 12:36:19] <sarang> that's a fair point
    [2019-12-30 12:36:39] <Isthmus> If the unlock time is plaintext, then how can the hodl be forced?
    [2019-12-30 12:36:58] <Isthmus> Erm
    [2019-12-30 12:37:08] <Isthmus> *if is encrypted, how enforced
    [2019-12-30 12:37:29] <sarang> There's a range proof included, showing that the current block height exceeds the committed lock period
    [2019-12-30 12:37:52] <moneromooo> Can't you easily brute force it ?
    [2019-12-30 12:37:55] <sarang> The goal is to reduce heuristics around expected spends
    [2019-12-30 12:37:57] <suraeNoether> endogenic: auditability in this case would be the same security/threat model as our confidential transactions, so that wouldn't reduce our auditability... not to mention, for the folks in the audience, monero balances are guaranteed by the unforgeability property of our signatures; if anyone is capable of cheating the monero system with our confidential transactions, they can also forge signatures with
    [2019-12-30 12:37:57] <suraeNoether> elliptic curves, which breaks a lot more than just monero.
    [2019-12-30 12:38:11] <Isthmus> I second mooo's question
    [2019-12-30 12:38:19] <sarang> moneromooo: the lock time is in a Pedersen commitment
    [2019-12-30 12:38:22] <endogenic> suraeNoether: was joke :)
    [2019-12-30 12:38:23] <sarang> which is perfectly hiding
    [2019-12-30 12:38:24] <suraeNoether> isthmus: early cross-chain swap models require unlock times to elapse to use SPV
    [2019-12-30 12:38:41] <endogenic> but how does recipient easily verify time til unlock isnt ridiculous through only range proof?
    [2019-12-30 12:38:51] ⇐ gandi[m] quit (gandiubpor@gateway/shell/matrix.org/x-gsymdlbwtbcbznll): Remote host closed the connection
    [2019-12-30 12:38:51] <suraeNoether> endogenic: it's a joke, but like a making a math joke in a math class, it's always followed up by a serious discussion of why it's funny. #mathteacherlife
    [2019-12-30 12:38:58] <sarang> That needs to be communicated to the recipient endogenic 
    [2019-12-30 12:39:06] <endogenic> suraeNoether: one-up'd
    [2019-12-30 12:39:12] <sarang> The range proof is included at spend time
    [2019-12-30 12:39:15] <sarang> not at output generation time
    [2019-12-30 12:39:25] <Isthmus> Ohhhh
    [2019-12-30 12:39:27] <moneromooo> So a verifier gets a yes/no, and at some point a no becomes a yes.
    [2019-12-30 12:39:31] <suraeNoether> moneromooo: can't brute force due to sarang's observation about perfect hiding
    [2019-12-30 12:39:33] <moneromooo> Right ?
    [2019-12-30 12:39:36] <sarang> not quite
    [2019-12-30 12:39:40] <endogenic> sarang: out of band?
    [2019-12-30 12:40:03] <sarang> When you generate the output, you specify an unlock time commitment, and transfer the plaintext version to the recipient either encrypted or out of band
    [2019-12-30 12:40:06] <moneromooo> I mean, from a verifier's perpective, they will need to either reject a spend, or ok it.
    [2019-12-30 12:40:21] <Isthmus> -_-
    [2019-12-30 12:40:29] <sarang> When the output is spent, a range proof is generated using a particular time offset against the commitment, to show the lock time has been exceeded relative to the current block height
    [2019-12-30 12:40:36] <moneromooo> When they stop getting a verification failure, there's no other reason (currently) other than that, no ?
    [2019-12-30 12:40:46] <sarang> The method is a bit unintuitive until you write it out, TBH
    [2019-12-30 12:40:46] <moneromooo> Oh. I see. Thanks.
    [2019-12-30 12:40:55] <sarang> but it's included in the DLSAG preprint
    [2019-12-30 12:40:55] <moneromooo> er.
    [2019-12-30 12:40:58] <suraeNoether> moneromooo: you wouldn't be able to construct a range proof on [0, ..., N] with time offset -3
    [2019-12-30 12:41:03] <suraeNoether> it wouldn't be a valid proof
    [2019-12-30 12:41:22] <suraeNoether> the trickiness is in realizing how the DLSAG construction actually captures the offset
    [2019-12-30 12:41:32] <moneromooo> So you include the block hash at currnet block then ?
    [2019-12-30 12:41:46] <suraeNoether> let me pull it up
    [2019-12-30 12:41:55] <sarang> But moneromooo, it's important to note that you can't simply brute-force the verification at each successive block until it succeeds
    [2019-12-30 12:42:04] <suraeNoether> for the audience members: https://eprint.iacr.org/2019/595
    [2019-12-30 12:42:06] <sarang> The signer generates the proof once, at spend time
    [2019-12-30 12:42:06] <moneromooo> OK, that's good enough for me. Thanks.
    [2019-12-30 12:42:56] <sarang> There's some subtlety in choosing the offsets and such, to reduce heuristics, but the method makes sense
    [2019-12-30 12:43:13] <suraeNoether> bottom of page 10, left hand column
    [2019-12-30 12:43:32] <sarang> Cost would be replacing plaintext lock times with commitments, and extending bulletproofs to include the lock proof
    [2019-12-30 12:44:16] <suraeNoether> this would be the first step toward "private" smart contracts that depend on dev-selected unlock times
    [2019-12-30 12:45:05] <suraeNoether> in a sense it's more basic than DLSAG, almost an independent component used in DLSAG. it should have occurred to me before that it was basically it's own construction...
    [2019-12-30 12:45:33] <sarang> It is an independent component... you can do DLSAG with plaintext trigger heights
    [2019-12-30 12:45:38] <suraeNoether> *nod*
    [2019-12-30 12:45:41] <sarang> but it's probably a bad idea to do so
    [2019-12-30 12:46:05] <endogenic> i have to step out y'all
    [2019-12-30 12:46:08] <suraeNoether> which means it has its own stand-alone security definitions. in this case, the definitions rely on some adversarially generated blockchain, yadda yadda
    [2019-12-30 12:46:10] <Isthmus> I think that would be worthwhile to switch to unlock time commitments... Right now an adversary can partition (/fingerprint) the blockchain into ~20 different anonymity puddles based on unlock time alone.
    [2019-12-30 12:46:10] <Isthmus> When I first plotted it I was expecting a few Easter eggs, not heuristic info bleeding everywhere.
    [2019-12-30 12:46:21] — Isthmus waves at endo
    [2019-12-30 12:46:38] <endogenic> keep killin it Isthmus 🤜🤛
    [2019-12-30 12:48:06] <suraeNoether> okay, anyone else want to present any research or thoughts at our roundtable?
    [2019-12-30 12:49:02] <moneromooo> If you guys are looking at making unlock time a commitment, maybe this is a good time to look at a possible semantics change for unlock time to ease future things like atomic swaps etc.
    [2019-12-30 12:49:13] <Isthmus> ^ ooooh
    [2019-12-30 12:49:21] <sarang> How so?
    [2019-12-30 12:49:45] <suraeNoether> yeah, please go on
    [2019-12-30 12:49:48] <Isthmus> Ok, my head is figuratively literally splitting in half, so I'mma peace out. Thanks y'all.
    [2019-12-30 12:49:49] <Isthmus> gg
    [2019-12-30 12:50:04] <moneromooo> By... er... thinking of the requirements you know of for atomic swaps etc, and what semantics would best match those.
    [2019-12-30 12:50:29] <sarang> See ya Isthmus; feel better
    [2019-12-30 12:50:39] <sarang> also see ya endogenic
    [2019-12-30 12:50:45] <moneromooo> I'm thinking in particular of the fact monero's unlock_time semantics do not match bitcoin's, and bitcoin's used for more fancy things like atomic swaps.
    [2019-12-30 12:50:54] <sarang> Ah ok
    [2019-12-30 12:51:25] <Isthmus> Oh but before I go, huge shoutout to @n3ptune who curated the data set
    [2019-12-30 12:51:34] <Isthmus> Ok ciao!
    [2019-12-30 12:52:21] <suraeNoether> moneromooo: yeah, we need to nail down specific examples of usual atomic swaps with bitcoin and how the masked unlock times in monero will play with the unmasked lock times in bitcoin...
    [2019-12-30 12:52:22] <suraeNoether> for sure
    [2019-12-30 12:53:07] <suraeNoether> isthm and i are having a video call about it after he feels better. i'll take notes and we'll draft an issue.
    [2019-12-30 12:53:25] <suraeNoether> allrighty, we are coming up on an hour
    [2019-12-30 12:53:35] <sarang> Action items, I suppose?
    [2019-12-30 12:53:40] <suraeNoether> indeed
    [2019-12-30 12:54:41] <suraeNoether> Mine: sending comments to sarang re: triptych and clsag, consulting with isthm about masking unlock times... which maybe we should do over IRC instead of a video call... to make a donation to sarang's funding request...
    [2019-12-30 12:55:26] <sarang> I'll be continuing that Omniring issue, editing CLSAG/Triptych based on suraeNoether's reviews, and a few odds and ends relating to code libraries and MPC
    [2019-12-30 12:56:23] <suraeNoether> okay, my dog is crossing her legs, I have to take her out. >.< does anyone have any last questions?
    [2019-12-30 12:56:29] <sarang> Nay
    [2019-12-30 12:58:10] <sarang> I suppose we can adjourn then
    [2019-12-30 12:58:13] <gingeropolous> when ringsize a bajillion
    [2019-12-30 12:58:18] <sarang> Soon (tm)
    [2019-12-30 12:58:24] <gingeropolous> :)
    [2019-12-30 12:58:40] <sarang> Or the Futurama answer: "Soon enough." "That's not soon enough!"


# Action History
- Created by: SarangNoether | 2019-12-26T23:25:55+00:00
- Closed at: 2019-12-30T18:03:14+00:00
