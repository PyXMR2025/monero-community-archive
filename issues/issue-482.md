---
title: 'Research meeting: 8 July 2020 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/482
author: SarangNoether
assignees: []
labels: []
created_at: '2020-07-06T16:35:48+00:00'
updated_at: '2020-07-08T17:43:13+00:00'
type: issue
status: closed
closed_at: '2020-07-08T17:43:13+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Wednesday, 8 July 2020 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable

3. Questions

4. Action items

# Discussion History
## SamsungGalaxyPlayer | 2020-07-08T14:20:30+00:00
You can join with Mattermost if irccloud isn't working:

Mattermost relay: https://mattermost.getmonero.org/monero/channels/monero-research-lab

## SarangNoether | 2020-07-08T17:43:13+00:00
    17:00:19 <xmrmatterbridge> <sarang> OK, time to get started!
    17:00:23 <xmrmatterbridge> <sarang> As usual, GREETINGS first
    17:00:24 <xmrmatterbridge> <sarang> hello
    17:01:09 <ArticMine> Hi
    17:01:22 <xmrmatterbridge> <sgp_> Hi
    17:02:27 * the_real_isthmus waves
    17:03:01 <xmrmatterbridge> <sarang> We may have lower attendance than usual, since many people use IRCCloud and it's currently down
    17:03:27 <xmrmatterbridge> <sarang> But we can move along to ROUNDTABLE, where anyone is welcome to share research of interest with the group
    17:03:35 <xmrmatterbridge> <sarang> Does anyone wish to go first?
    17:04:11 <the_real_isthmus> I can share a quick update
    17:04:29 <xmrmatterbridge> <sarang> Go ahead, account claiming to be Isthmus!
    17:05:03 <the_real_isthmus> We examined a few mechanisms that were suggested at last week’s meeting. Triptych is not secure against Shor’s algorithm, as expected. Also, Keccak/chacha20 might run into issues with the Bernstein–Vazirani algorithm (hidden linear function problem).
    17:05:08 <the_real_isthmus> We’re starting to turn our attention from problems towards solutions, and we’re working through a lot of recent literature (h/t reading suggestions from surae).
    17:05:13 <the_real_isthmus> I’m amazed at some of the recent improvements. A few years ago, any post-quantum cryptography was laughably unwieldy. TB-scale keys, absurd verification times, etc.
    17:05:18 <the_real_isthmus> Today’s crypto schemes are less painful by a few orders of magnitude. Check out this paper highlighted by surae - MatRiCT: Efficient, Scalable and Post-Quantum Blockchain Confidential Transactions Protocol
    17:05:23 <the_real_isthmus> https://dl.acm.org/doi/pdf/10.1145/3319535.3354200
    17:05:27 <the_real_isthmus> MatRiCT supports ring sizes of around 64, verification time around 25 ms, 4 kB keys, 31 kB signatures. Not stellar, but could be much worse!
    17:05:32 <the_real_isthmus> Anyways, over the next week we’ll dig into some more modern schemes and I’ll report back here about the most relevant prospects.
    17:05:35 * the_real_isthmus tries to figure out how to hand the mic back to sarang from across a bridge
    17:06:06 <xmrmatterbridge> <sarang> Impressive numbers from that abstract
    17:06:25 <the_real_isthmus> Oh actually, looking at the tables, ring size 64 might be closer to 40 ms verification
    17:06:41 <xmrmatterbridge> <sarang> Not really suitable size-wise, compared to today's signatures, but not bad overall
    17:06:57 * the_real_isthmus digs around for a link
    17:07:21 <the_real_isthmus> https://eprint.iacr.org/2019/1287.pdf
    17:07:29 <xmrmatterbridge> <sarang> thanks
    17:07:50 <the_real_isthmus> Anyways, that's all from me. More info next week, same bat time, same bat channel
    17:08:07 <xmrmatterbridge> <sarang> Great, thanks for the update, possibly-Isthmus :)
    17:08:13 <ArticMine> Still there within a 10 year range of Nielsen's Law of Internet Bandwidth which is a factor of ~57x
    17:08:34 <ArticMine> This is really interesting
    17:08:37 * the_real_isthmus looks up Nielsen's law
    17:09:23 <the_real_isthmus> https://connectedhome2go.files.wordpress.com/2008/03/nielsens-law-of-internet-bandwidth.jpg?w=584
    17:09:24 <the_real_isthmus> ooh
    17:09:52 <xmrmatterbridge> <sarang> I wonder how widely those estimates apply
    17:10:08 <xmrmatterbridge> <sarang> e.g. in the United States, network providers charge absurd amounts of money for often terrible service
    17:10:14 <ArticMine> https://www.nngroup.com/articles/law-of-bandwidth/
    17:10:28 <xmrmatterbridge> <sarang> So for the average user, "possible" bandwidth is likely not "actual" bandwidth
    17:11:10 <ArticMine> The trend is pretty accurate, from my own experience in Canada
    17:11:20 <the_real_isthmus> Probably the same curve, just with a time lag
    17:11:33 <ArticMine> 1.5x a year compounded
    17:11:50 <xmrmatterbridge> <sarang> It may also be dangerous to assume that capabilities for "high-end users" (as the article says) are sufficient for basing protocol decisions on
    17:12:04 <xmrmatterbridge> <sarang> Then you start to run the risk of alienating entire groups of users
    17:12:13 <xmrmatterbridge> <sarang> and centralizing services around high-capacity entities
    17:12:19 <ArticMine> Actually the cost difference between high end and low end is narrowing
    17:12:36 <ArticMine> especially for consumer accounts
    17:13:27 <xmrmatterbridge> <sarang> I can share a few research items now
    17:14:04 <xmrmatterbridge> <sarang> I sent an updated CLSAG security model and linkable anonymity theorem/proof to the reviewers, who said the changes address their concerns
    17:14:20 <xmrmatterbridge> <sarang> We're trying to determine the best way to include these changes in a follow-up report
    17:14:47 <xmrmatterbridge> <sarang> They want to keep the original report mostly untouched, but I also think it's important to make clear what updates were made, and how those updates affect their conclusions
    17:14:52 <xmrmatterbridge> <sarang> After all, that's the point of the review
    17:15:26 <xmrmatterbridge> <sarang> The current IACR version of the preprint contains all the updates so far: https://eprint.iacr.org/2019/654
    17:16:20 <xmrmatterbridge> <sarang> Separately from this, PoPETs reviewers for Triptych and Arcturus suggested those preprints may be better suited for workshop submission due to their content and scope
    17:17:13 <xmrmatterbridge> <sarang> One reviewer for Arcturus claimed to have found a way to break the hardness assumption, but their supposed counterexample doesn't work... I don't think they tested it, or perhaps they didn't fully read through all the requirements of the assumption
    17:17:46 <xmrmatterbridge> <sarang> Arcturus is still technically under PoPETs consideration and can't be submitted elsewhere yet, but Triptych can
    17:18:03 <xmrmatterbridge> <sarang> I'm finalizing it for submission to an ESORICS workshop whose deadline is July 10
    17:19:40 <xmrmatterbridge> <sarang> Unfortunately CLSAG is far too long for ESORICS, but could be submitted to PoPETs at their next deadline; however, I fear it will be rejected for being too incremental
    17:20:17 <xmrmatterbridge> <sarang> Scaling it back to the ESORICS limit would basically nix all the security model improvements, and then the reviewers would probably (rightly) complain that such a security model is too weak
    17:20:28 <xmrmatterbridge> <sarang> So I don't think it's possible to win on that front :/
    17:20:41 <xmrmatterbridge> <sarang> Preprint submission is not a fun game
    17:20:55 <xmrmatterbridge> <sarang> Anyway, those are my updates
    17:21:49 <xmrmatterbridge> <sarang> Once again, I wish there were a Journal of Incremental Cryptography =p
    17:22:55 <xmrmatterbridge> <sarang> Does anyone else wish to share anything?
    17:25:44 <moneromooo> Encouragements to whoever "sarang" is for the submission work ^_^
    17:26:09 <xmrmatterbridge> <sarang> heh, thanks :)
    17:26:20 <xmrmatterbridge> <sarang> I wish there were better news on the submission front :/
    17:26:53 <xmrmatterbridge> <sarang> But the gist of the Triptych initial reviews seemed to be "this is an incremental improvement that appears not to have major flaws" and that's something
    17:27:17 <xmrmatterbridge> <sarang> Comments on Arcturus certainly addressed that an untested hardness assumption carries additional risk that may be offset by its benefits
    17:27:26 <xmrmatterbridge> <sarang> and that's a very valid point
    17:27:58 <xmrmatterbridge> <sarang> But at least the supposed counterexample doesn't appear valid (not that this demonstrates it's secure!)
    17:30:01 <xmrmatterbridge> <sarang> Since Arcturus is still under consideration, there's a rebuttal period where I can directly address reviewer comments
    17:30:13 <xmrmatterbridge> <sarang> (for Triptych, there is no such period available)
    17:31:43 <xmrmatterbridge> <sarang> I'll post the counterexample as a paste later, to have someone else verify my conclusion
    17:32:03 <xmrmatterbridge> <sarang> IIRC the rebuttal period ends around July 19 or so
    17:33:14 <xmrmatterbridge> <sarang> OK, if there isn't anything else to share, we can move to ACTION ITEMS for the upcoming week
    17:33:44 <xmrmatterbridge> <sarang> I'll continue to work with the CLSAG reviewers on the preprint side of things; they are still working on the code part of their review (which was delayed)
    17:34:14 <xmrmatterbridge> <sarang> Additionally, I'll finalize the Triptych submission to the ESORICS workshop, and send off some comments/questions for the Arcturus PoPETs rebuttal period
    17:34:28 <xmrmatterbridge> <sarang> If there's time, I'll continue with some output merging analysis using my new analysis toolkit
    17:34:35 <xmrmatterbridge> <sarang> Anyone else?
    17:35:57 <xmrmatterbridge> <sarang> Oh, and there's a lot of lit review that I wish to catch up on
    17:37:50 <xmrmatterbridge> <sarang> Righto, in that case, we can adjourn!
    17:37:53 <xmrmatterbridge> <sarang> Thanks to everyone for attending


# Action History
- Created by: SarangNoether | 2020-07-06T16:35:48+00:00
- Closed at: 2020-07-08T17:43:13+00:00
