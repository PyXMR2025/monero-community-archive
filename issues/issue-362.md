---
title: 'Research meeting: 1 July 2019 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/362
author: SarangNoether
assignees: []
labels: []
created_at: '2019-06-29T17:13:09+00:00'
updated_at: '2019-07-01T18:14:48+00:00'
type: issue
status: closed
closed_at: '2019-07-01T18:14:48+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Monday, 1 July 2019 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable
a. Sarang: speedups to [MLSAG](https://github.com/monero-project/monero/pull/5707) and [CLSAG](https://github.com/SarangNoether/monero/commits/clsag-plumbing) verification (more in progress), DEF CON workshop/talk, [monthly report](https://repo.getmonero.org/monero-project/ccs-proposals/merge_requests/34#note_6648)
b. Surae
c. Others?

3. General questions

4. Action items

# Discussion History
## SarangNoether | 2019-07-01T18:14:48+00:00
    [2019-07-01 12:51:33] <suraeNoether> agenda here: https://github.com/monero-project/meta/issues/362
    [2019-07-01 12:51:46] <rehrar> howdy ho suraeNoether
    [2019-07-01 12:56:14] <suraeNoether> heighty hi, neighborino
    [2019-07-01 13:00:25] <suraeNoether> Good morning everyone!
    [2019-07-01 13:00:32] <suraeNoether> let's get this research meeting started
    [2019-07-01 13:00:38] <suraeNoether> Agenda is here, to refresh: https://github.com/monero-project/meta/issues/362
    [2019-07-01 13:00:45] <suraeNoether> Sarang will not be joining us today
    [2019-07-01 13:01:08] <suraeNoether> Before we get going, who all is here other than rehrar and myself?
    [2019-07-01 13:01:30] <moneromooo> I am here, in read only mode.
    [2019-07-01 13:01:38] ⇐ spaced0ut quit (~spaced0ut@unaffiliated/spaced0ut): Remote host closed the connection
    [2019-07-01 13:01:55] <suraeNoether> isthmus is usually in meetings at this time, maybe he'll jump in later
    [2019-07-01 13:02:10] <rehrar> chmod moneromooo 777
    [2019-07-01 13:02:10] <suraeNoether> okay, we'll get going either way :D looks to be a short meeting
    [2019-07-01 13:02:16] <rehrar> fixed, albeit drastically
    [2019-07-01 13:02:31] — moneromooo fandangoes on filesystem
    [2019-07-01 13:02:57] <suraeNoether> So, firstly, Sarang posted his monthly research report, has been working on MLSAG speedups and some other CLSAG stuff, along with organizing for defcon
    [2019-07-01 13:03:48] ← rehrar[m] left (rehrarmatr@gateway/shell/matrix.org/x-nvaxqbumboksfiui): "User left"
    [2019-07-01 13:03:52] <suraeNoether> I have not posted my research reports yet because I've been running around post-konferenco trying to get some stuff finished, getting back into research and simulations, and learning a lot from TheCharlatan who, through some unfortunate mishaps with passports, is still in town after the kon :P
    [2019-07-01 13:04:24] <suraeNoether> One thing I wanted to post with my reports was a post-mortem of the konferenco: total (final) attendee and sponsorship and speaker numbers, budget actuals, etc
    [2019-07-01 13:05:10] <suraeNoether> Other than that, there was a Monero coffee chat right after the Konferenco that sgp hosted. I'm not sure where the link was, but we had a lot of folks from the konferenco live, a huge portion of the MAGIC board of directors... it was a great conversation
    [2019-07-01 13:06:00] <suraeNoether> I'm anticipating making a push to my matching code either later today or tomorrow (TheCharlatan has helped me with a couple of development issues that were bogging me down)
    [2019-07-01 13:06:16] <suraeNoether> Beyond that, I can answer questions on more details, but I want to pass it off to anyone else who's done any work in the past week they want to share
    [2019-07-01 13:06:30] — kennonero[m] sent a long message:  < https://matrix.org/_matrix/media/v1/download/matrix.org/jMOsKdEkdMDXHbQiupLSAOQW >
    [2019-07-01 13:07:20] <suraeNoether> kennonero just asked two questions: first, when will CLSAG be merged, and second, has anything come up with the audits for CLSAG yet?
    [2019-07-01 13:08:14] <suraeNoether> in answer to the first question, based on my last conversation with sarang we are optimistically (but unlikely) shooting for the next hard fork for CLSAG, but there is a good chance it will be put off till the next hardfork... sarang is currently the middle man between MRL and the auditors, so I probably shouldn't get into further detail for fear of putting words in his mouth
    [2019-07-01 13:09:00] <suraeNoether> "middle man..." "contact person..."
    [2019-07-01 13:09:18] <TheCharlatan> lol
    [2019-07-01 13:09:37] ⇐ xiphon quit (~xiphon@ip135.ip-147-135-99.us): Ping timeout: 245 seconds
    [2019-07-01 13:09:54] <rehrar> there was a dev meeting yesterday
    [2019-07-01 13:10:04] <rehrar> and in it we all thought it was unlikely CLSAG makes it in this hard fork
    [2019-07-01 13:10:19] <rehrar> it's just really tight
    [2019-07-01 13:10:19] <suraeNoether> ^ there we go
    [2019-07-01 13:10:26] <suraeNoether> it is, it is
    [2019-07-01 13:10:47] <moneromooo> OTOH the Random X reviews fell into place quick, so...
    [2019-07-01 13:11:07] <rehrar> how are those going btw?
    [2019-07-01 13:11:16] <suraeNoether> yeah, i do wish sarang and I had a conversation about audits before this meeting.
    [2019-07-01 13:11:28] <suraeNoether> perhaps hyc is online and has some nontrivial info?
    [2019-07-01 13:12:04] <moneromooo> He got the X41 report, but I heard no more beyond "we got what we asked for".
    [2019-07-01 13:12:21] <kennonero[m]> suraeNoether: is there a vetting period for CLSAG security proof, or is it once the auditors are finished?
    [2019-07-01 13:12:34] <dEBRUYNE> I am more worried about third party software than the core software getting up to date for CLSAG in time
    [2019-07-01 13:12:54] <rehrar> "we got what we asked for" sounds kind of disappointed :P
    [2019-07-01 13:13:21] <TheCharlatan> yeah, some lead time for third parties should be taken into account.
    [2019-07-01 13:13:22] <suraeNoether> kennonero[m]: we haven't discussed that yet
    [2019-07-01 13:13:48] <moneromooo> Whoever wants to code their own already has the source.
    [2019-07-01 13:14:05] <moneromooo> (modulo yet another small speedup sarang wants to adD)
    [2019-07-01 13:14:32] <moneromooo> Is anyone really doing their own beyond mymonero ?
    [2019-07-01 13:14:53] <suraeNoether> if you ask me, the CLSAG scheme is not so different from MLSAG to be worried about the security (unforgeability), but it was sufficiently different that we couldn't "drop in" the security proof and a new one had to be written. but the proof doesn't have anything novel in it, and has all the same cryptographic assumptions as our present signatures...
    [2019-07-01 13:15:04] <endogenic> moneromooo: lots of ppl actually
    [2019-07-01 13:15:24] <suraeNoether> but on top of that, if we won't be able to get CLSAG into this hard fork and we have to push to the next hard fork anyway, that's still an additional 6 months of people looking at the proofs
    [2019-07-01 13:15:25] <endogenic> but otoh more are being discovered of late to have been using our lib
    [2019-07-01 13:15:26] <moneromooo> I find that hard to believe, but I'll accept that.
    [2019-07-01 13:16:09] <suraeNoether> moneromooo: one of the interesting things about isthmus' talk was the statistical evidence of a whole ecology of monero code out there that doesn't match our reference code or mymonero either
    [2019-07-01 13:16:12] <endogenic> i find it hard to accept lol
    [2019-07-01 13:16:25] <moneromooo> suraeNoether: it'll be 5 months of nothing, plus one month of looking. Instead of being one month of looking now.
    [2019-07-01 13:16:25] <endogenic> suraeNoether: i thought so too
    [2019-07-01 13:16:39] <suraeNoether> one thing i would like to bring up is the "juvenile transaction" problem that isthmus brought up in that talk too
    [2019-07-01 13:17:30] <suraeNoether> namely, it's convenient to be able to dump a bunch of transactions into the mempool all at once and walk away assured that eventually they will all be confirmed
    [2019-07-01 13:17:54] <suraeNoether> but if a transaction is in the mempool and uses an output that hasn't expired it's lock time, i feel like htat transaction should be considered invalid
    [2019-07-01 13:18:12] <suraeNoether> but then you have people who have to wait to create sequential transactions
    [2019-07-01 13:18:12] <endogenic> consensus all the things
    [2019-07-01 13:18:35] <suraeNoether> one question was "is there harm in allowing juvenile transactions to be hanging out in the mempool?"
    [2019-07-01 13:18:55] <endogenic> sounds like it
    [2019-07-01 13:19:07] <suraeNoether> a non-consensus way of helping things would make it so that such transactions *aren't relayed until after the lock time is expired*
    [2019-07-01 13:19:09] <moneromooo> smooth may have an opinion on that.
    [2019-07-01 13:19:25] <suraeNoether> i feel like it's a vector for the big bang attack or it will make flooding attacks way more simple or something like that
    [2019-07-01 13:19:33] <moneromooo> If it's not mined yet, it can't take others with it, so it seems much less annoying.
    [2019-07-01 13:20:29] <moneromooo> Good point. Currently the txpool is limited to... somehting like 300 MB I think. So you could make these unmineable txes with huge fees, but using an output locked for 10 years...
    [2019-07-01 13:20:41] <moneromooo> And it'd muscle out all other txes -> empty blocks.
    [2019-07-01 13:20:59] <gingeropolous> hold my beer, ima go pwn the monero network
    [2019-07-01 13:21:33] <moneromooo> Could be a separate txpool for those I guess.
    [2019-07-01 13:21:34] <suraeNoether> lolol
    [2019-07-01 13:21:49] <kennonero[m]> moneromooo: would it be logical to split the mempool into txs that can be spent now?
    [2019-07-01 13:22:33] <moneromooo> I'd have to think a lot more to decide whether it's logical I think.
    [2019-07-01 13:22:42] <suraeNoether> it's an interesting problem and there aren't obvious immediate ways to look at the trade-offs
    [2019-07-01 13:22:52] <suraeNoether> my favorite kind of problem
    [2019-07-01 13:22:53] <kennonero[m]> And maybe add a tx expiry time, so that txs cannot be in the pool for longer than a day or so
    [2019-07-01 13:23:01] <moneromooo> There is.
    [2019-07-01 13:23:02] <kennonero[m]> Sure
    [2019-07-01 13:23:17] <TheCharlatan> How about adding the locktime to the dandelion stem phase?
    [2019-07-01 13:23:32] <suraeNoether> vtnerd ^
    [2019-07-01 13:23:41] <moneromooo> What does this mean ?
    [2019-07-01 13:24:04] <suraeNoether> well, in the stem phase of dandelion++ you hang onto transactions for a random period of time before you pass it down the stem
    [2019-07-01 13:24:28] <suraeNoether> perhaps that random time could/should be >= the lock time of the transaction
    [2019-07-01 13:24:51] <moneromooo> Even easier to DoS nodes then, no ?
    [2019-07-01 13:25:22] <suraeNoether> hmmmm
    [2019-07-01 13:26:00] <suraeNoether> i suppose in the sense that it requires/requests that miners hang onto a transaction longer before removing it from the mempool, so the pool would get bigger
    [2019-07-01 13:26:20] <suraeNoether> okay, let's delay this discussion until after the meeting. too much in the weeds. :P but fun
    [2019-07-01 13:26:47] <suraeNoether> does anyone else have any research or other devleopment they want to brag about?
    [2019-07-01 13:27:15] → xiphon joined (~xiphon@ip135.ip-147-135-99.us)
    [2019-07-01 13:27:29] ⇐ vtnerd quit (~Lee@173-23-103-30.client.mchsi.com): Ping timeout: 248 seconds
    [2019-07-01 13:27:53] <suraeNoether> Okay, so let's move onto action items, I guess!
    [2019-07-01 13:28:14] <moneromooo> Oh, reminds me. You or sarang said there was a "secret paper" to be presented at the Monero konferenco that would add another possible MLSAG replacement ?
    [2019-07-01 13:28:30] <moneromooo> Or was that DLSAG and I got confused?
    [2019-07-01 13:28:31] <suraeNoether> ohhohoho so that was omniring
    [2019-07-01 13:28:36] <moneromooo> OK.
    [2019-07-01 13:28:41] <suraeNoether> that was secret until about 2 weeks before the konferenco
    [2019-07-01 13:29:17] <suraeNoether> so we had two MLSAG replacement talks: lelantus and omniring. and we had 4 papers of interest: lelantus, omniring, ringct3.0, and Spartan
    [2019-07-01 13:29:22] → vtnerd joined (~Lee@173-23-103-30.client.mchsi.com)
    [2019-07-01 13:29:32] <rehrar> can we just implement them all?
    [2019-07-01 13:29:41] <rehrar> or make a hodge podge of them like a soup and toss them in
    [2019-07-01 13:29:58] <suraeNoether> we've already excluded spartan for lack of a ZK language being proven (although the others present such a language for each example and there will eventually be some compatibility)
    [2019-07-01 13:30:25] <suraeNoether> i believe the batching for ringct3 and omniring ended up not panning out the way we had hoped, so our interest has zeroed in on lelantus (not a zerocoin joke when i started typing it, definitely a zerocoin joke by the time i was done typing it)
    [2019-07-01 13:30:49] <suraeNoether> so rehrar: maybe? shrugemoji
    [2019-07-01 13:31:14] <suraeNoether> it will be a stew of thermodynamics and money
    [2019-07-01 13:31:37] <suraeNoether> Any questions before we move onto action items?
    [2019-07-01 13:32:15] <kennonero[m]> <suraeNoether "i believe the batching for ringc"> suraeNoether: For lelantus has there been any updates on the issue of having to send your received amount to yourself, so the original sender does not know when you spend?
    [2019-07-01 13:32:43] <suraeNoether> nope kennonero[m] that's the unfortunate trade-off with lelantus that has not yet been solved
    [2019-07-01 13:33:55] <kennonero[m]> Oh okay, thank you
    [2019-07-01 13:35:53] <suraeNoether> okay, moving onto action items
    [2019-07-01 13:36:02] <suraeNoether> My non-research things: konferenco post-mortem, research report, quarterly funding request. My research things: getting my github repo more orderly and pushing my Matching changes.
    [2019-07-01 13:36:15] <suraeNoether> oh and reviewing 5707
    [2019-07-01 13:37:09] <suraeNoether> Anyone else have any action items?
    [2019-07-01 13:38:23] <rehrar> update on RandomX when we can find it
    [2019-07-01 13:38:52] <suraeNoether> ^ i believe sarang will be on later today or tomorrow and he can bring us up to date on that. i may ask him to write a blog post describing the progress.
    [2019-07-01 13:39:13] <suraeNoether> okay, let's call this meeting adjourned, and hope we can hear from isthmus and sarang later


# Action History
- Created by: SarangNoether | 2019-06-29T17:13:09+00:00
- Closed at: 2019-07-01T18:14:48+00:00
