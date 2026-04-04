---
title: 'Research meeting: 5 August 2020 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/496
author: SarangNoether
assignees: []
labels: []
created_at: '2020-08-03T15:56:32+00:00'
updated_at: '2020-08-05T18:07:51+00:00'
type: issue
status: closed
closed_at: '2020-08-05T18:07:51+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Wednesday, 5 August 2020 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable

3. Questions

4. Action items

# Discussion History
## Mitchellpkt | 2020-08-05T16:49:49+00:00
Rough schematic of how an outside observer with a quantum computer could might approach deanonymization of the blockchain without participating in any transactions:

<img width="969" alt="image" src="https://user-images.githubusercontent.com/21246742/89441085-dbc4b280-d709-11ea-8987-13686d96836e.png">

Note the recursive attack vector if stealth address are compromised (row 3)

Completely unrelated, Neptune engineered some great systems for parsing and analyzing tx_extra. Found some whimsical unencrypted PIDs, see [https://github.com/noncesense-research-lab/monero_tx_extra/blob/master/ascii_data.md](https://github.com/noncesense-research-lab/monero_tx_extra/blob/master/ascii_data.md)


## SarangNoether | 2020-08-05T18:07:51+00:00
    [2020-08-05 11:59:12] <sarang> OK, let's get started with the meeting
    [2020-08-05 11:59:13] <sarang> GREETINGS
    [2020-08-05 11:59:16] <sarang> hello
    [2020-08-05 11:59:30] <ArticMine> Hi
    [2020-08-05 12:00:27] → bearretinjapan joined (ferretinja@gateway/vpn/privateinternetaccess/ferretinjapan)
    [2020-08-05 12:00:44] — needmoney90 realizes a meeting is happening 
    [2020-08-05 12:01:05] ⇐ ferretinjapan quit (ferretinja@gateway/vpn/privateinternetaccess/ferretinjapan): Ping timeout: 240 seconds
    [2020-08-05 12:01:49] <needmoney90> Is this thing on?
    [2020-08-05 12:01:52] — needmoney90 taps mic 
    [2020-08-05 12:02:03] * bearretinjapan → ferrretinjapan
    [2020-08-05 12:02:09] <n3ptune> Hello
    [2020-08-05 12:02:09] * ferrretinjapan → ferretinjapan
    [2020-08-05 12:02:31] <sarang> Let's move to ROUNDTABLE, where anyone can share research of interest with the channel
    [2020-08-05 12:02:42] <ArticMine> Well I will start
    [2020-08-05 12:03:19] — Isthmus waves
    [2020-08-05 12:03:29] <ArticMine> My main contribution is on https://github.com/monero-project/research-lab/issues/70
    [2020-08-05 12:04:18] <sarang> Yes, it looks like some recommendations for fees and block growth
    [2020-08-05 12:04:25] <sarang> UkoeHB_ also responded to it with questions
    [2020-08-05 12:04:45] <ArticMine> It deals with ah issue that is actually very serious once the block growth grows significantly
    [2020-08-05 12:04:56] <Isthmus> I haven't yet read in depth enough to comment, but can tell that this is very detailed/thoughtful work - thanks for contributing this pretty hefty analysis
    [2020-08-05 12:05:53] <sgp_> hello
    [2020-08-05 12:06:10] <ArticMine> I will be talking about this also at Defcon on Friday
    [2020-08-05 12:06:16] <sgp_> I second Isthmus's comment
    [2020-08-05 12:06:21] <sgp_> ArticMine: awesome
    [2020-08-05 12:06:43] <ArticMine> At this point what I need of course is review and feedback
    [2020-08-05 12:06:48] <sarang> right
    [2020-08-05 12:06:53] <ArticMine> thanks sgp_
    [2020-08-05 12:07:08] <sarang> I assume that it is not your intent to get this into the October upgrade ArticMine?
    [2020-08-05 12:07:15] <sarang> The code freeze for that is August 17
    [2020-08-05 12:07:29] <sgp_> speaking of that, did the janus mitigation stuff make it?
    [2020-08-05 12:07:49] <sarang> nope
    [2020-08-05 12:07:57] <sgp_> darn
    [2020-08-05 12:08:15] <ArticMine> It is very tight for the October 17 upgrade
    [2020-08-05 12:08:17] <sarang> There are a few approaches, and not enough broad agreement about choosing one
    [2020-08-05 12:08:22] <sarang> ArticMine: I would not go for it
    [2020-08-05 12:08:39] <sarang> Next upgrade could include fee/block update, transaction structure if desired, etc.
    [2020-08-05 12:09:44] <ArticMine> The best alternative is to do nothing with respect to fees / scaling at this fork and keep the current reference transaction size etc.
    [2020-08-05 12:10:14] <sarang> Even with the CLSAG transaction size change?
    [2020-08-05 12:10:44] <ArticMine> There is no problem leaving things as they are
    [2020-08-05 12:10:50] <sarang> Which drops the transaction size by 32*(N-1) bytes per spent input, at ring size N
    [2020-08-05 12:10:55] <ArticMine> The other option can be a partial implementation
    [2020-08-05 12:11:33] <ArticMine> The drop is from ~2600 to ~2000 bytes over all for a 2 in 2 out tx
    [2020-08-05 12:11:45] <sarang> 2.5 kB to 1.9 kB for 2-2
    [2020-08-05 12:12:17] <ArticMine> So the fees will still drop.
    [2020-08-05 12:12:43] <sarang> I noticed you also commented on sgp_'s coinbase idea ArticMine
    [2020-08-05 12:12:53] <sgp_> is it okay if the fees drop? honesty fees seem super low already
    [2020-08-05 12:13:06] <ArticMine> Yes this is where it gats a bit interesting
    [2020-08-05 12:13:33] <ArticMine> If the response is to increase the ring size to mitigate this
    [2020-08-05 12:13:54] <sgp_> "If the selection is algorithm is weighted towards current transactions then one would expect at most about 5% of compromised coinbase outputs in a ring" I don't think this is correct
    [2020-08-05 12:14:06] <sgp_> it's closer to 20%
    [2020-08-05 12:14:17] <Isthmus> "If the response is to increase the ring size to mitigate this" :- D
    [2020-08-05 12:14:37] ⇐ xiphon quit (~xiphon@45.43.14.47): Ping timeout: 264 seconds
    [2020-08-05 12:14:53] <ArticMine> It is also the reason I provided a second option where the reference tx is basically the same
    [2020-08-05 12:15:11] <ArticMine> SO it can accommodate a ring size increase
    [2020-08-05 12:15:23] <Isthmus> "Sorry everybody Monero got too efficient, so we had to add some extra privacy to round things out" 😅
    [2020-08-05 12:15:38] <sgp_> Isthmus: lmao hilarious
    [2020-08-05 12:15:54] <sgp_> transactions were so tiny we just HAD to improve privacy, sorry all
    [2020-08-05 12:16:31] <ArticMine> My 5% figure came from using current tx data. If one takes tx data from a year ago the results are very different
    [2020-08-05 12:16:31] <UkoeHB_> the fee stuff is not time sensitive (we need a lot more tx volume for it to be serious) so I feel it's safe to hold off one hardfork
    [2020-08-05 12:16:32] <sgp_> ArticMine: I don't agree with your assessment, but it's probably not worth discussing before my Defcon talk
    [2020-08-05 12:16:32] <sarang> FWIW increasing ringsize 12-13 would put verification where it is right now
    [2020-08-05 12:16:58] <ArticMine> The best place is to comment on the issue in response
    [2020-08-05 12:17:44] <sgp_> ArticMine: I get that, but I have nothing to add now before the talk
    [2020-08-05 12:18:13] <sarang> OK, anything else to discuss presently ArticMine?
    [2020-08-05 12:18:44] <ArticMine> No that is a good summary. Thanks
    [2020-08-05 12:18:53] <sarang> Thanks ArticMine
    [2020-08-05 12:19:00] <ArticMine> You are welcome
    [2020-08-05 12:19:05] <sarang> Isthmus: you had something on the agenda issue
    [2020-08-05 12:19:27] <Isthmus> Ah yea, just some quick notes
    [2020-08-05 12:19:30] <sgp_> just to be clear: we are deciding we do not need to make a decision on ringsize and transaction size/fees for this month?
    [2020-08-05 12:19:49] — Isthmus pauses
    [2020-08-05 12:19:52] <sarang> Unless there is a compelling reason, I do not think increasing the ring size for October should be done
    [2020-08-05 12:20:12] <sarang> and big changes to fee/size so quickly seems unwise
    [2020-08-05 12:20:54] <ArticMine> I am neutral on the ring size question. I will wait for sgp_ 's talk first
    [2020-08-05 12:21:34] <ArticMine> ... but I do agree it is getting very close for the October fork
    [2020-08-05 12:21:42] <sarang> Note that it was repeatedly stated that transaction size _will_ go down
    [2020-08-05 12:22:11] <sgp_> my vote is no unless it's critical
    [2020-08-05 12:22:52] <sarang> OK, Isthmus?
    [2020-08-05 12:23:05] <Isthmus> We drew up a rough schematic of how an outside observer with a quantum computer could might approach systematic deanonymization of the blockchain without participating in any transactions:
    [2020-08-05 12:23:11] <Isthmus> https://usercontent.irccloud-cdn.com/file/Dp8NjuDw/image.png
    [2020-08-05 12:23:25] <sarang> What assumes a candidate destination address suspected by the attacker?
    [2020-08-05 12:23:33] <sgp_> Isthmus: ooooooh can we share?
    [2020-08-05 12:23:53] <Isthmus> sgp_: where
    [2020-08-05 12:24:10] <sarang> sgp_: without a ton of context, people might freak out unnecessarily...
    [2020-08-05 12:24:17] <needmoney90> I'm behind raising ring sizes. I would eventually hope we can hit three digits.
    [2020-08-05 12:24:33] <Isthmus> sarang: what was your question?
    [2020-08-05 12:24:51] <Isthmus> This assumes a noninteractive attacker just analyzing the blockchain
    [2020-08-05 12:25:18] <sgp_> idk, twatter
    [2020-08-05 12:25:26] <sarang> Payment IDs and amounts are encrypted using the DH shared secret, which involves recipient address and transaction key
    [2020-08-05 12:25:41] <sarang> So are you assuming the attacker has a list of addresses they suspect could be recipients?
    [2020-08-05 12:26:10] <sarang> If so, they could use these to check
    [2020-08-05 12:26:10] <moneromooo> Am I reading it right above "I have relevant info but I'll send it to the media, not you" ?
    [2020-08-05 12:26:25] <sarang> ?
    [2020-08-05 12:26:57] <sgp_> ?
    [2020-08-05 12:26:59] <UkoeHB_> nicely presented figure Isthmus
    [2020-08-05 12:27:21] <moneromooo> < sgp_> ArticMine: I get that, but I have nothing to add now before the talk
    [2020-08-05 12:27:39] <moneromooo> I have no background on this so I might be misinterpreting (I hope).
    [2020-08-05 12:28:05] <Isthmus> Ah @sarang I see what you mean. I have a meeting with Adam later today, and will unpack the assumptions under the hood to clarify
    [2020-08-05 12:28:14] <Isthmus> Given that, let's not share yet sgp_
    [2020-08-05 12:28:32] <sarang> Isthmus: yeah, same with the stealth address stuff
    [2020-08-05 12:28:43] <sarang> I think it's important to clarify what requires candidate addresses
    [2020-08-05 12:28:52] <sarang> It doesn't make everything magically ok, but it's important IMO
    [2020-08-05 12:28:56] → xiphon joined (~xiphon@45.43.14.47)
    [2020-08-05 12:29:06] <sgp_> okay I'll not share that image
    [2020-08-05 12:29:15] <sarang> I read what you have now as "you need the chain and no other information"
    [2020-08-05 12:29:16] <Isthmus> Maybe the rows should be reordered (3,1,2,4)
    [2020-08-05 12:29:18] <sarang> but I don't think that's the case
    [2020-08-05 12:29:29] <sgp_> but re: moo: yes I'll share all the researhc I've done on coinbase rings at Defcon after discussing them here for years
    [2020-08-05 12:29:44] <sarang> also: "key signature" -> "key image"?
    [2020-08-05 12:29:45] <sgp_> will be good to have a talk
    [2020-08-05 12:29:55] <moneromooo> Ah, so this is just stuff already discussed, fine then.
    [2020-08-05 12:30:24] <Isthmus> In other words, step 1 would be using Shor's + Grover's to extract real address from stealth address, then use that moving forward for the other decryptions
    [2020-08-05 12:30:37] <Isthmus> But yea, lemme have some offline conversations and clarify next week
    [2020-08-05 12:30:51] <Isthmus> ahhahaa "key signature"
    [2020-08-05 12:30:54] <Isthmus> that was my bad, brain fart
    [2020-08-05 12:31:11] <sarang> Can you briefly explain pulling addresses from stealth?
    [2020-08-05 12:32:29] <sarang> If you pull addresses successfully, then sure, you can derive the shared secret and use it to get pID/amount
    [2020-08-05 12:34:23] <Isthmus> Grover's algorithm kind of lets us brute force the address space in O(sqrt(N)) whereas classical computers are limited to O(N)
    [2020-08-05 12:34:52] <Isthmus> Maybe O(N^(1/3)) but not committing to that yet
    [2020-08-05 12:35:05] <Isthmus> I'll try to get a better diagram/explanation for next week
    [2020-08-05 12:35:15] <sarang> OK
    [2020-08-05 12:35:16] <Isthmus> Will have thorough public writeups in the next few weeks anyways
    [2020-08-05 12:35:32] <sarang> Thanks for the update Isthmus
    [2020-08-05 12:35:38] <Isthmus> Completely unrelated, Neptune engineered some great systems for parsing and analyzing tx_extra
    [2020-08-05 12:35:43] <sarang> ah sorry, go ahead
    [2020-08-05 12:35:44] <Isthmus> We found some whimsical unencrypted PIDs, see https://github.com/noncesense-research-lab/monero_tx_extra/blob/master/ascii_data.md
    [2020-08-05 12:35:52] <Isthmus> Nah, that's all
    [2020-08-05 12:36:07] <sarang> Another data point for stricter tx structure...
    [2020-08-05 12:36:37] <Isthmus> Thought y'all might get a chuckle out of those on-chain easter eggs
    [2020-08-05 12:36:52] <sarang> You misspelled "fingerprints" :/
    [2020-08-05 12:37:25] <moneromooo> If something is found just once, it's not really a fingerprint. Are there duplicates ?
    [2020-08-05 12:37:27] <sgp_> haha cool stuff
    [2020-08-05 12:37:43] <Isthmus> Boatloads of duplicates
    [2020-08-05 12:38:14] <moneromooo> If boatloads, that points more to malice.
    [2020-08-05 12:38:36] <sgp_> I don't think it's that magnitude of "boatloads"
    [2020-08-05 12:39:00] <sgp_> well, intent is whatever, but not enough to impact network privacy for other users
    [2020-08-05 12:39:25] <Isthmus> "fluffypony is the best pony ever" alone was used 85 times
    [2020-08-05 12:39:37] <sgp_> lol
    [2020-08-05 12:40:00] <Isthmus> Dates also often repeated
    [2020-08-05 12:40:02] <Isthmus> https://usercontent.irccloud-cdn.com/file/jJoGVIwT/image.png
    [2020-08-05 12:40:36] <Isthmus> 101 txns that had the uPID `EYEixhEvFzEcyJapqxJsoEwmeNULJYFV`
    [2020-08-05 12:40:44] <Isthmus> (to give some context for 'boatloads of duplicates')
    [2020-08-05 12:41:35] <sgp_> cool treasure hunt
    [2020-08-05 12:41:43] <sarang> Any other questions/comments for Isthmus on his update?
    [2020-08-05 12:42:10] <sarang> If not, I'll provide an update
    [2020-08-05 12:42:18] <Isthmus> Shoutout to n3ptune who built the whole framework that made the treasure hunt possible
    [2020-08-05 12:42:25] <sarang> Pleased to announce that the CLSAG audit is complete: https://web.getmonero.org/2020/07/31/clsag-audit.html
    [2020-08-05 12:42:34] <Isthmus> Nice!
    [2020-08-05 12:42:39] <sgp_> great post
    [2020-08-05 12:42:42] <sarang> Note that the audit report reflects the _original_ version of the preprint, not its update
    [2020-08-05 12:42:48] <sgp_> cool logo too
    [2020-08-05 12:43:01] <sarang> The update contains many updates to address the reviewers' concerns and improve the security model and proofs
    [2020-08-05 12:43:15] <sarang> The code did not require any changes
    [2020-08-05 12:43:45] <sarang> Ledger and Trezor support is continuing nicely, and I'm in contact with their teams
    [2020-08-05 12:44:14] <sarang> I updated some branches/PRs for things like wallet signing, key encryption, transaction proofs
    [2020-08-05 12:44:22] <sarang> Some minor things for `monero-site`
    [2020-08-05 12:44:29] <sarang> Work related to BP+
    [2020-08-05 12:44:47] <sarang> There's been a fair amount of discussion since the BP+ CCS was posted
    [2020-08-05 12:44:59] <fluffypony> Isthmus: and that wasn't even me
    [2020-08-05 12:45:24] <sarang> As I'd brought up recently, the original numbers proposed for moving from BP to BP+ would not be nearly as good as the table suggests
    [2020-08-05 12:45:29] <iDunk> Various people did that, IIRC.
    [2020-08-05 12:45:40] <sarang> since the authors didn't account for some optimizations consistently
    [2020-08-05 12:46:02] <sarang> The short version of this is that we'd drop 96 bytes from each transaction, with a marginal speedup (very marginal)
    [2020-08-05 12:46:45] <sarang> I'm of the opinion that BP+ is worth continuing to research and investigate, but I don't think the benefits are significant enough to rush into it
    [2020-08-05 12:47:32] <sarang> However, the CCS proposers did say they were open to the idea of auditing a hypothetical future implementation, since they have expertise relating to the BP+ construction
    [2020-08-05 12:48:02] <sarang> Any other thoughts on this?
    [2020-08-05 12:49:24] <ArticMine> What kind of timeline would be reasonable for BP+?
    [2020-08-05 12:49:35] <sarang> Certainly not the October upgrade
    [2020-08-05 12:49:48] <ArticMine> That is out of the question
    [2020-08-05 12:49:59] <sarang> But I think it could be within a few weeks to code and get initial tests up and running
    [2020-08-05 12:50:07] <sarang> Auditing would be a separate timeline, of course
    [2020-08-05 12:50:28] <ArticMine> Six months?
    [2020-08-05 12:50:39] <sarang> Absolutely, provided the auditors have availability
    [2020-08-05 12:51:01] <needmoney90> Six months between hard forks isn't manageable
    [2020-08-05 12:51:05] — Isthmus has to hop into another meeting, will be back in a later
    [2020-08-05 12:51:07] <needmoney90> At this point it's 9m min
    [2020-08-05 12:51:11] — Isthmus takes off lab coat and goggles
    [2020-08-05 12:51:39] <needmoney90> Just want to pipe in and mention that, because the coordination is hell and a lot of people not involved don't realize how bad it got
    [2020-08-05 12:51:54] <sarang> Again, I don't think there's a particular rush for BP+ since the benefits, while present, are marginal
    [2020-08-05 12:52:09] <sarang> needmoney90: I'm not necessarily advocating for any particular upgrade timeline, to be clear
    [2020-08-05 12:52:19] <sgp_> if it happens, then it happens, whenever the next update would happen anyway :p
    [2020-08-05 12:52:49] <needmoney90> I'm just trying to express that if it's not this update, we're nine months out min
    [2020-08-05 12:53:04] <sarang> It will not be this update
    [2020-08-05 12:53:05] <sarang> No way
    [2020-08-05 12:53:12] <needmoney90> No advocacy either, just statement of fact
    [2020-08-05 12:53:28] <sarang> And given how new the construction is, I would prefer that it receive additional scrutiny
    [2020-08-05 12:53:36] <sarang> It's straightforward, but still very new
    [2020-08-05 12:53:43] <ArticMine> Then lets us make it nine months for the next HF
    [2020-08-05 12:54:35] <sarang> I do agree with needmoney90 that a longer time would be very beneficial for coordination and ecosystem communication
    [2020-08-05 12:54:50] <sarang> Getting hardware device support for this update was a bit of an ordeal, for example
    [2020-08-05 12:55:04] <sarang> to say nothing of software wallets, exchanges, etc.
    [2020-08-05 12:55:04] <sgp_> ping dEBRUYNE to remind them about the relevant post on upgrades ^
    [2020-08-05 12:55:08] <needmoney90> Plus code freezes, followed by translations team and wallet code
    [2020-08-05 12:55:23] <needmoney90> Lots of stuff has to be done in serial for a release
    [2020-08-05 12:55:26] <sarang> right
    [2020-08-05 12:55:29] <needmoney90> And only after code freeze
    [2020-08-05 12:55:38] <needmoney90> Which makes it a total nightmare
    [2020-08-05 12:55:42] <sarang> Well, it sounds like there isn't any major opposition here to a longer time
    [2020-08-05 12:55:46] <ArticMine> Lead time is a very valid issue
    [2020-08-05 12:55:48] <needmoney90> Fixing an airplane while it's in the air and all
    [2020-08-05 12:55:57] <sarang> and at any rate BP+ wouldn't make it for October
    [2020-08-05 12:56:36] <sarang> I do think the CCS proposers would produce a quality code review
    [2020-08-05 12:56:58] <sarang> And having additional researchers participating in the ecosystem is very positive
    [2020-08-05 12:57:18] <needmoney90> How would you suggest we go hunting
    [2020-08-05 12:57:18] <sarang> The proposers could write the code, but then they shouldn't audit it of course
    [2020-08-05 12:57:27] <sarang> needmoney90: ?
    [2020-08-05 12:57:39] <needmoney90> For additional researchers
    [2020-08-05 12:57:56] <needmoney90> What can we do to entice more people onboard?
    [2020-08-05 12:58:32] <needmoney90> Oh, I see you were referring to the CCS proposes as the researchers, I misread.
    [2020-08-05 12:58:37] <needmoney90> Still, relevant question
    [2020-08-05 12:58:43] <sarang> Yes, sorry for any confusion
    [2020-08-05 12:58:43] <needmoney90> Proposers*
    [2020-08-05 12:59:26] <sarang> That's also a good question, and not one I have a good answer to... researchers seem to find the project if/when they have aligned research interests
    [2020-08-05 12:59:31] <needmoney90> Link to the CCS for the record?
    [2020-08-05 12:59:39] <sarang> e.g. the DLSAG team, Isthmus and friends, the BP+ CCS researchers
    [2020-08-05 12:59:41] <sarang> one sec
    [2020-08-05 12:59:41] <needmoney90> Since we're talking about it.
    [2020-08-05 12:59:56] <sarang> BP+ CCS: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/156
    [2020-08-05 13:00:02] <needmoney90> Thanks.
    [2020-08-05 13:00:41] <sarang> For clarity, I am claiming that the improvements shown in Table 1 at that link are not representative of what we'd see in an implementation
    [2020-08-05 13:00:47] <sarang> at least not for verification
    [2020-08-05 13:02:13] <sarang> All right, in the interest of time, does anyone else wish to share research of general interest?
    [2020-08-05 13:03:20] <sarang> OK, in that case, let's adjourn!
    [2020-08-05 13:03:24] <sarang> Thanks to everyone for joining


# Action History
- Created by: SarangNoether | 2020-08-03T15:56:32+00:00
- Closed at: 2020-08-05T18:07:51+00:00
