---
title: 'Research meeting: 3 June 2019 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/351
author: SarangNoether
assignees: []
labels: []
created_at: '2019-06-01T20:51:35+00:00'
updated_at: '2019-06-03T17:42:40+00:00'
type: issue
status: closed
closed_at: '2019-06-03T17:42:40+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Monday, 3 June 2019 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable

3. General questions

4. Action items

# Discussion History
## SarangNoether | 2019-06-03T17:42:39+00:00
    [2019-06-03 12:59:28] <sarang> OK, let's begin our meeting
    [2019-06-03 12:59:31] <sarang> Hello
    [2019-06-03 12:59:51] <sarang> Or rather, GREETINGS (according to the agenda)
    [2019-06-03 13:00:04] <suraeNoether> howdydoodily neighborini
    [2019-06-03 13:00:30] <sarang> Lots to talk about today
    [2019-06-03 13:00:42] <sarang> Anyone else around today?
    [2019-06-03 13:01:13] ⇐ siom__ quit (~siom@195.12.48.205): Ping timeout: 246 seconds
    [2019-06-03 13:01:25] <suraeNoether> hrmm. :P we need a publicist, it seems
    [2019-06-03 13:01:47] <sarang> Well, let's go ahead with ROUNDTABLE anyway
    [2019-06-03 13:02:06] <sarang> The DLSAG paper is now on IACR as a preprint: https://eprint.iacr.org/2019/595
    [2019-06-03 13:02:13] <suraeNoether> whoooo
    [2019-06-03 13:02:28] — needmoney90 stumbles in and waves
    [2019-06-03 13:02:29] <sarang> (the usual reminder that preprints are _not_ peer reviewed as a prereq to being on the archive)
    [2019-06-03 13:02:33] <needmoney90> is this thing on
    [2019-06-03 13:02:37] <sarang> yo
    [2019-06-03 13:02:39] <suraeNoether> needmoney90: welcome
    [2019-06-03 13:03:03] <needmoney90> I dont have much to say, but ill watch intently
    [2019-06-03 13:03:21] <sarang> CLSAG is also available, currently in a monero-site MR: https://repo.getmonero.org/monero-project/monero-site/merge_requests/1080
    [2019-06-03 13:03:33] <sarang> It will be submitted to IACR once suraeNoether gives it one last read-through
    [2019-06-03 13:03:34] <wow-discord> <Crappyrules Ⓤ> lurking intensifies
    [2019-06-03 13:03:39] <suraeNoether> ^ i'm reading through this sucker one more time before we submit to IACR, i'll be done later this afternoon
    [2019-06-03 13:03:54] <sarang> Those are two big projects that we'll be glad to receive feedback on
    [2019-06-03 13:03:54] <suraeNoether> not wow-discord, but the paper before it :P
    [2019-06-03 13:04:01] <sarang> lol
    [2019-06-03 13:04:17] <sarang> Any questions on DLSAG or CLSAG before we move on?
    [2019-06-03 13:05:43] <sarang> righto
    [2019-06-03 13:05:58] <sarang> A new sublinear transaction protocol, Omniring, was posted: https://eprint.iacr.org/2019/580
    [2019-06-03 13:06:14] <sarang> suraeNoether and I had been looking over early versions of it, courtesy of the authors
    [2019-06-03 13:06:30] <sarang> It's a very clever construction, but note that the batching numbers are incorrect
    [2019-06-03 13:06:37] <sarang> I'm told those will be updated in a later revision
    [2019-06-03 13:06:44] <suraeNoether> I spent this weekend on real_or_random et al's omniring paper, which is really elegant, imo. i'm also reading more about ringct3.0, lelantus, and spartan. sarang and i have our eyes on a comparison/state-of-the-art paper describing these different approaches and looking at concrete impacts on the monero chain if we upgrade protocols
    [2019-06-03 13:06:59] <Isthmus> Hey, I’m intermittently here
    [2019-06-03 13:07:13] <suraeNoether> neat, while we have you, do you want to jump in on the round table and describe what you've been working on?
    [2019-06-03 13:07:15] <sarang> Yes, I've begun running the numbers we need for Lelantus, using my toy implementation of it
    [2019-06-03 13:07:53] <suraeNoether> sarang is anyone working on a python implementation of omni for comparison purposes afayk?
    [2019-06-03 13:08:36] <Isthmus> I’m just making new transaction tree tracing heuristics
    [2019-06-03 13:08:43] → PrivateDolphin joined (cb7adb05@gateway/web/cgi-irc/kiwiirc.com/ip.203.122.219.5)
    [2019-06-03 13:08:44] <sarang> Isthmus: nice!
    [2019-06-03 13:08:53] <sarang> Anything to share at this point?
    [2019-06-03 13:09:01] <Isthmus> Step 1) Have gotten to the point of identifying wonky txns
    [2019-06-03 13:09:39] <Isthmus> Step 2) upcoming: look for wonky transactions who contain similarly wonky ring members
    [2019-06-03 13:10:16] <Isthmus> Which implies following true spend path with high probability
    [2019-06-03 13:10:34] <Isthmus> Step 3) fix it so we don’t leak this info moving forward
    [2019-06-03 13:10:53] <sarang> Are some of these heuristics a result of protocol choices?
    [2019-06-03 13:10:59] <sarang> Or bad user behavior?
    [2019-06-03 13:11:18] <Isthmus> Bad wallet behavior - wrong decoy Alto, etc
    [2019-06-03 13:11:33] <Isthmus> Ooh gotta run into a meeting, back in a bit probably
    [2019-06-03 13:11:36] <sarang> np
    [2019-06-03 13:11:41] <sarang> To your question, suraeNoether 
    [2019-06-03 13:11:44] <Isthmus> *algo
    [2019-06-03 13:11:58] <sarang> it's probably not necessary to do a full implementation of Omniring to assess its complexity
    [2019-06-03 13:12:09] <sarang> For Lelantus it was, since many building blocks were unspecified
    [2019-06-03 13:12:14] ⇐ wow-discord quit (~wow-disco@206.189.166.14): Remote host closed the connection
    [2019-06-03 13:12:28] <sarang> e.g. signatures
    [2019-06-03 13:12:32] → wow-discord joined (~wow-disco@206.189.166.14)
    [2019-06-03 13:12:55] <sarang> Oh, another note... my research report for the previous month is available: https://repo.getmonero.org/monero-project/ccs-proposals/merge_requests/34#note_6373
    [2019-06-03 13:14:29] <suraeNoether> I'm still drafting my research report, and I apologize to the community for the delay. Now that DLSAG and CLSAG are both "out the door," i'm summarizing my work immediately
    [2019-06-03 13:15:17] <sarang> So yeah, a lot of joint work between suraeNoether and me, for getting CLSAG and DLSAG out the door
    [2019-06-03 13:15:25] <sarang> and assessing these new sublinear proposals
    [2019-06-03 13:15:37] <sarang> Does anyone else have research to share?
    [2019-06-03 13:16:37] <sarang> or suraeNoether, if you have other things to share?
    [2019-06-03 13:16:59] <suraeNoether> The next 20 days or so are going to come quickly with the konferenco. other than reviewing CLSAG later today, I'm putting paper-writing down until after the conference. the next few weeks will be conference planning primarily and coding for mrl12 secondarily (and keeping up on reading new research as it comes out), with the hopes of finishing mrl12 before the conference.
    [2019-06-03 13:17:18] <sarang> Excellent
    [2019-06-03 13:17:23] <sarang> I'm really excited for the conference
    [2019-06-03 13:17:29] <suraeNoether> but i'm still going to be reading these sublinear protocol proposals and tinkerrrrring
    [2019-06-03 13:17:35] <sarang> Neato
    [2019-06-03 13:17:37] <suraeNoether> oh by the way
    [2019-06-03 13:18:01] <suraeNoether> if you are speaking at the konferenco, please make sure you get your slides to me by June 20 so we can work them into a common slide deck
    [2019-06-03 13:18:27] <sarang> Cool kids use PDFs for slides :D
    [2019-06-03 13:18:33] <suraeNoether> and if any speakers have any questions, please feel free to shoot me emails..  I'm catching up on a konferenco backlog
    [2019-06-03 13:18:56] <sarang> So, this moves to ACTION ITEMS already
    [2019-06-03 13:19:20] <sarang> suraeNoether will be working to run the conference smoothly, giving the ok for CLSAG to be submitted to IACR, and doing MRL-12 stuffs
    [2019-06-03 13:19:25] <sarang> (to summarize)
    [2019-06-03 13:20:06] <sarang> I will be getting those papers up-to-date (on the MRL archive and on IACR), continuing sublinear assessment, and beginning some investigation into ristretto implementation details
    [2019-06-03 13:20:17] → rehrar joined (~rehrar@gateway/tor-sasl/rehrar)
    [2019-06-03 13:20:23] <suraeNoether> yes, and konferenco speakers should make sure they get slides to me before June 20th. many of you hang out in this room :P
    [2019-06-03 13:21:13] <sarang> I shall submit them to you once I write them :D
    [2019-06-03 13:21:19] <sarang> but well in advance of the deadline
    [2019-06-03 13:21:52] <sarang> Despite having many things to discuss, this meeting is going quite quickly
    [2019-06-03 13:22:02] <sarang> Is there anything to discuss regarding sublinear schemes so far?
    [2019-06-03 13:22:19] <sarang> One thing to note is that I haven't identified a way to make RCT3 compatible with our key images
    [2019-06-03 13:22:30] <sarang> Omniring describes a way to do this, and I have a method for Lelantus
    [2019-06-03 13:22:54] <sarang> Note that Lelantus (like DLSAG) would require a self-spend (i.e. a single churn) to avoid spend tracing
    [2019-06-03 13:23:02] <sarang> Omniring does not have such a limitation
    [2019-06-03 13:23:09] <suraeNoether> my understanding is that spartan lacks any transaction structure
    [2019-06-03 13:23:15] <suraeNoether> so it'd be a ground-up protocol design
    [2019-06-03 13:23:22] <sarang> Spartan is only a proving system, right
    [2019-06-03 13:23:39] <suraeNoether> omniring surprised me about how simple it was, considering the heft of the paper, but most of it lies in new rigorous definitions of security, etc
    [2019-06-03 13:23:42] <sarang> We do not have any kind of circuit-optimized Monero-specific transaction protocol at this time
    [2019-06-03 13:24:15] <sarang> All of Lelantus, Omniring, and RCT3 provide a full transaction structure
    [2019-06-03 13:24:46] <rehrar> I have a question for MRL after current discussion ends
    [2019-06-03 13:25:03] <sarang> Sure, go ahead
    [2019-06-03 13:25:07] <suraeNoether> well, i don't have more research to discuss, so fire away rehrar
    [2019-06-03 13:25:42] <sarang> If it's not research related, we can adjourn first
    [2019-06-03 13:25:53] <rehrar> my issue is with view keys, and while I suspect it's a UX issue, I just wanted to verify that by having MRL confirm my thoughts (or disconfirm them if it is MRL related)
    [2019-06-03 13:26:26] <suraeNoether> in the words of sarang, 0_o
    [2019-06-03 13:26:33] <rehrar> One of the things that's not discussed much is the fact that "view keys" don't live up to their name and are fairly useless in their current form.
    [2019-06-03 13:26:46] <sarang> In that you only inherently get incoming information?
    [2019-06-03 13:26:50] <rehrar> Giving just a view key to someone doesn't do much in terms of accounting purposes.
    [2019-06-03 13:26:51] <rehrar> yes
    [2019-06-03 13:26:55] <sarang> Yes, it's a limitation for sure
    [2019-06-03 13:26:55] <rehrar> you need key images
    [2019-06-03 13:27:10] <rehrar> and I'm not aware of any tool that allows easy import/export of key images
    [2019-06-03 13:27:21] <moneromooo> monero-wallet-cli
    [2019-06-03 13:27:23] <rehrar> to make a REAL view key wallet
    [2019-06-03 13:27:30] <rehrar> moneromooo: for non-nerds
    [2019-06-03 13:27:57] — suraeNoether calls the fire department because mooo got nerd-burned
    [2019-06-03 13:27:58] <rehrar> I'm talking about Small Business Man Billy who wants to show his books to his accountant
    [2019-06-03 13:28:23] <rehrar> I'm talking about Farmer Joe who needs to prove to the IRS something or other
    [2019-06-03 13:28:30] <rehrar> these guys aren't going to use CLI
    [2019-06-03 13:28:40] <sarang> So what you're asking for is a good user-friendly way to export the information that Billy's accountant can import to verify details?
    [2019-06-03 13:28:40] <moneromooo> They're not going to use Monero in the first place :)
    [2019-06-03 13:28:56] <rehrar> now, as I said, this may just be a UX thing, and only a matter of time until someone makes it easy, similar to exa wallet multi sig thing today
    [2019-06-03 13:29:14] <rehrar> sarang: or if this is a limitation that must be adhered to period
    [2019-06-03 13:29:40] <rehrar> moneromooo: it's a catch 22 bro, one of the reasons they  may not use monero is because of stuff like this, but stuff like this doesn't get fixed because they won't use monero
    [2019-06-03 13:29:41] <moneromooo> Someone posted a way to make the view key also view outgoing txes IIRC. It's way down in the issues list in the monero repo.
    [2019-06-03 13:29:45] <sarang> What limitation exactly?
    [2019-06-03 13:29:50] <sarang> The need for key images at all?
    [2019-06-03 13:29:59] <sarang> Or how convenient the software makes it to import/export?
    [2019-06-03 13:30:08] <rehrar> sarang: more like what moneromooo is saying
    [2019-06-03 13:30:10] <sarang> The key image requirement is currently a protocol limitation, for sure
    [2019-06-03 13:30:24] <rehrar> a way to make view key also viewing outgoing
    [2019-06-03 13:30:32] <suraeNoether> moneromooo: if there is a way to make the viewkey outgoing also, i haven't seen it and i'd love to. i've been thinking about it for awhile
    [2019-06-03 13:30:34] <rehrar> without key images
    [2019-06-03 13:30:38] <sarang> Yes, that's been a discussion over time, but hasn't been brought up in a while
    [2019-06-03 13:30:48] <sarang> I recall seeing an idea (perhaps the one moneromooo is talking about)
    [2019-06-03 13:31:01] <sarang> If anyone has the link, I'd like to refresh my understanding of it
    [2019-06-03 13:31:08] <ArticMine> This if I recall came up last year over AML / KNC
    [2019-06-03 13:31:12] <sarang> yes
    [2019-06-03 13:31:22] <suraeNoether> i had this idea the other day: SBMB could publish an accumulator that contains his key images, in a way that allows the auditor to check if a given key image is in the accumulator, but the auditor has to trust that the accumulator was constructed faithfully (unless some protocol is used to prove fairness).  that plus the view key of the wallet allows the auditor to determine 1) all incoming XMR to that wallet
    [2019-06-03 13:31:22] <suraeNoether> and 2) any outgoing viewkeys included, allowing the auditor to determine anupper bound remaining in the wallet
    [2019-06-03 13:31:41] <rehrar> this would (imo) single-handedly would shoot Monero's real world use up incredibly
    [2019-06-03 13:31:50] <moneromooo> https://github.com/monero-project/monero/issues/1070
    [2019-06-03 13:31:52] <suraeNoether> for some auditors this would be enough, after all you have to trust that the client has actually provided access to all his wallets anyway
    [2019-06-03 13:32:00] <suraeNoether> thanks moneromooo
    [2019-06-03 13:32:33] <sarang> Yes, I believe this was the idea that I was vaguely remembering :)
    [2019-06-03 13:32:51] <sarang> It would be very interesting to reconsider such an idea now that we have multiple ways to make signatures smaller
    [2019-06-03 13:32:57] <suraeNoether> hmm
    [2019-06-03 13:33:17] <suraeNoether> that's... very promising.
    [2019-06-03 13:33:20] <rehrar> as a business man, something like this would be invaluable
    [2019-06-03 13:33:26] <moneromooo> Note that smooth (IIRC) had misgivings since this gives more spying power to people with the view key.
    [2019-06-03 13:33:30] <suraeNoether> but it would require a change to the transaction structure
    [2019-06-03 13:33:38] <rehrar> and would make posting a view key for something like general fund and/or CCS wallet actually useful
    [2019-06-03 13:33:51] <suraeNoether> unless the extra group element is stashed into tx_extra and then... well, anyone can put anything in there so
    [2019-06-03 13:34:00] <sarang> Right, there were concerns about how this affect other users' privacy in practice
    [2019-06-03 13:34:00] ⇐ ferretinjapan quit (ferretinja@gateway/vpn/privateinternetaccess/ferretinjapan): Ping timeout: 268 seconds
    [2019-06-03 13:34:28] <suraeNoether> wait, i'm not sure about this method
    [2019-06-03 13:34:43] <sfhi> I agree with rehrar that this would be really valuable for accounting purposes
    [2019-06-03 13:34:49] → fort3hlulz joined (~setsimmo@2001:420:2160:1281:6c7a:102a:3055:b868)
    [2019-06-03 13:34:53] <rehrar> obviously if the reduction in privacy heavily outweights the benefits, then perhaps it should be solved on a UX level
    [2019-06-03 13:35:13] <ArticMine> Can this not be brute forced by using all the existing key images in the blockchain?
    [2019-06-03 13:35:22] <sarang> Well, regardless of the implications of the linked suggestion, broader thoughts about privacy-aware auditing should be ongoing
    [2019-06-03 13:36:47] → ferretinjapan joined (ferretinja@gateway/vpn/privateinternetaccess/ferretinjapan)
    [2019-06-03 13:38:20] <sarang> Anything else specific to discuss while the meeting is ongoing?
    [2019-06-03 13:40:14] <sarang> Righto
    [2019-06-03 13:40:25] <sarang> Well, let's go ahead and adjourn, and let the general discussion continue
    [2019-06-03 13:40:35] <sarang> Thanks to everyone for attending; logs will be posted to GitHub shortly

# Action History
- Created by: SarangNoether | 2019-06-01T20:51:35+00:00
- Closed at: 2019-06-03T17:42:40+00:00
