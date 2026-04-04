---
title: Monero Research Lab Meeting - Wed 31 August 2022
source_url: https://github.com/monero-project/meta/issues/728
author: Rucknium
assignees: []
labels: []
created_at: '2022-08-29T23:13:30+00:00'
updated_at: '2022-09-05T15:45:19+00:00'
type: issue
status: closed
closed_at: '2022-09-05T15:45:19+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Improvements to the decoy selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

3. Seraphis. ( [UkoeHB's Seraphis Proof of Concept work](https://ccs.getmonero.org/proposals/seraphis-wallet-poc-2.html), [Seraphis repo](https://github.com/UkoeHB/Seraphis) ).

4. MRL Meta: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [MoneroResearch.info repository of Monero-related research papers](https://moneroresearch.info/), [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

5. Any other business

6. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: TBD

Previous meeting agenda/logs:

#727 

# Discussion History
## plowsof | 2022-09-04T22:20:27+00:00
Logs 
```
17:01:11 <Rucknium[m]> Meeting time: https://github.com/monero-project/meta/issues/728

17:01:16 <Rucknium[m]> 1. Greetings

17:01:21 <Rucknium[m]> Hi

17:01:25 <one-horse-wagon[> Hello

17:01:28 <xmrack[m]> Hi

17:01:31 <rbrunner> Hello

17:01:48 <jberman[m]> hello

17:03:04 <Rucknium[m]> 2. Updates, what's everyone working on?

17:04:10 <Rucknium[m]> Me: OSPEAD work. Reviewing xmrack 's work. Also, took an inventory of which multicoin
wallets survived the hard fork. It's been a bit of a bloodbath.

17:04:33 <xmrack[m]> I’m doing last minute editing on my final report for the MAGIC grant. It should be
released later in a post to reddit and matrix

17:05:14 <Rucknium[m]> xmrack: Do you want to discuss the results during this meeting, or wait until next one?

17:05:56 <xmrack[m]> I think we can do that next week once everyone has given the report at least a skim

17:06:00 <rbrunner> I think most, if not all, multicoin wallets depend either directly on MyMonero, or copy
technology from there, and if MyMonero is late, a bloodbath results ...

17:07:23 <Rucknium[m]> I don't think all of them rely on MyMonero. Here's my list, with date of fix:

17:07:52 <one-horse-wagon[> rbrunner: Why would a wallet like MyMonero be so late with an update when they
hold themselves out as mainly being a Monero wallet?  Doesn't make sense.

17:07:52 <jberman[m]> me: submitted wallet<>daemon hard fork compatibility PR (8544) and started looking into
the borked multisig seed recovery: https://github.com/monero-project/monero/issues/8537

17:08:10 <Rucknium[m]> Wookey (Aug 19), Exodus (Aug 25), Edge (Aug 27), MyMonero (Aug 29), Not yet fixed:
Atomic, Coinomi, Guarda, Zelcore.

17:08:13 <jberman[m]> no tangible updates on my end from last week on getting multisig security proofs done,
but figure it's worth sharing I'm also considering approaching Cypher Stack/Sarang to discuss working with
them as well

17:08:35 <Rucknium[m]> If anyone has different info, let me know. I have gathered info from Twitter and
Reddit.

17:09:31 <rbrunner> one-horse-wagon: complicated story, they detailed their woes and their bad luck on Reddit.

17:12:34 <Rucknium[m]> In a few months I may submit another CCS to (1) Evaluate safety of altering the wallet2
decoy selection algorithm when not at a hard fork; (2) Prepared an OSPEAD manuscript for submission to an
academic journal; (3) Evaluate different methods for transitioning decoy selection for Seraphis transactions.

17:13:20 <rbrunner> https://www.reddit.com/r/MyMonero/comments/wxbdb9/mymonero_important_announcement/

17:13:53 <Rucknium[m]> rbrunner's "no wallet left behind" for Seraphis seems to be particularly important
given the recent hard fork wallet bloodbath

17:14:55 <rbrunner> Yes, that hardfork will be several orders of magnitude bigger than this comparatively
small update

17:15:14 <rbrunner> And if you don't prepare you will miss for more than a few days :)

17:15:44 <kayabaNerve> Even nowadays we can discuss wallet upgrades being annoying thanks to items such as
Polyseed :/

17:16:02 <xmrack[m]> I havent been around for many hardforks. Was what we saw with v15 normal? Should we
consider giving more time for subsequent forks?

17:16:08 <kayabaNerve> *just in how it's a different seed format. I personally greatly appreciate it and
believe it should be used.

17:16:56 <rbrunner> Rucknium: Where would you place OSPEAD public disclosure in this timeline?

17:17:01 <hyc> I don't think the MyMonero fumble this time around was a normal occurrence

17:17:02 <Rucknium[m]> How many other coins have hard forks where old tx formats are not compatible? I wonder
if some of the wallets didn't understand that they had to take action with the hard fork.

17:17:04 <sech1> xmrack[m] v15 was more hectic than usual

17:17:09 <sech1> in terms of wallet support

17:17:20 <rbrunner> Or better, disclosure of the underlying problems

17:18:00 <hyc> and anyone who used wallet2 would have been able to integrate the new library well in advance

17:18:08 <jberman[m]> MyMonero offered me contracted work to prepare their libraries for the hard fork before
the fork. I decided I wouldn't want to work on moving forward a centralized wallet scanning service that has
access to view keys (unless the wallet makes it extremely clear what the tradeoff is and tucks the option deep
into the config settings rather than defaults it). They were not interested in such a drastic change at this
time

17:18:42 <rbrunner> Interesting background info

17:18:46 <sech1> maybe we need to think of a way to _force_ everyone to update _before_ the fork. Like mini-
fork or something when new nodes refuse to serve RPC to old wallets

17:18:46 <Rucknium[m]> rbrunner: The decision is mostly up to the review panel. Hopefully they will be done
reviewing by end of October. If disclosure is cleared, hopefully we can do it in November/December. If no
disclosure, then no (2) in my list above.

17:19:16 <rbrunner> Alright, thanks. Looking forward to it, as a curious person

17:19:42 <hyc> ringCT hardfork went pretty smoothly. this is certainly not the first time we've migrated txn
formats.

17:21:10 <kayabaNerve> sech1: Isn't that just the hard fork but without the benefits of it

17:21:36 <rbrunner> Yeah, and I guess users don't care why exactly their wallets don't work anymore, right?

17:21:47 <rbrunner> Mini-hardfork or not

17:22:32 <rbrunner> Maybe make the wallets 10 times slower ...

17:22:34 <sech1> I guess we can't solve 3rd-party developers' lazyness on protocol level :D

17:22:59 <rbrunner> Or calculate 10 times higher fees :)

17:23:37 <rbrunner> Something like ETH's difficulty bomb

17:24:15 <Rucknium[m]> It's unfortunate for users. On the other hand, I am not too sad about the death of
wallets that have defects in transaction uniformity.

17:24:15 <one-horse-wagon[> sech1: You really can't force people to upgrade because some people may go away
from Monero for years.  As it is right now, they can upgrade their wallets and all is good to go.

17:24:45 <sech1> They'll just upgrade when they get back?

17:24:50 <sech1> I'm talking about wallet developers

17:25:45 <sech1> something like protocol-level warning before the hardfork, so you can still use the wallet
but with some limitations

17:26:13 <hyc> sounds like a lot of effort for not much gain

17:26:27 <hyc> as it is, they will certainly have limitations once the hardfork occurs ..

17:26:56 <rbrunner> Call it natural selection for wallets. Adapt or die.

17:27:02 <jberman[m]> <sech1> "maybe we need to think of a..." <- I considered this for 8544; would have
vastly simplified that PR to just break clients immediately and require they update once the fork code is
ready to go. But I think the optimal UX is a smooth update transition where wallets give warnings ahead of
time. Plenty of modern apps use an approach like this

17:27:29 <jberman[m]> As far as avoiding this fork's problems, as basically mentioned above MyMonero uses
their own custom client<>lws<>daemon setup; I doubt their setup would be break-able pre-fork to avoid the
issue

17:27:52 <sech1> yes, an RPC call that tells you "fork is coming" is already better than nothing

17:27:58 <sech1> good wallets will show warnings to users

17:28:30 <hyc> isn't fork info already available in monerod rpc?

17:29:37 <sech1> that rpc call is not about upcoming forks

17:29:47 <sech1> https://github.com/monero-project/monero/pull/8544 adds this data

17:30:18 <hyc> I also seem to recall that while we were still on regular 6 month upgrades, the daemon would
have a timed announcement of "you should be looking for a software update" or somesuch

17:30:33 <sech1> it was a guesstimate

17:30:40 <sech1> daemon didn't know the actual fork height

17:30:47 <hyc> yes...

17:31:20 <rbrunner> and was wrong often enough at the end as to basically only annoy

17:31:26 <Rucknium[m]> Many of the wallets do not have a check next to their checklist here:

17:31:27 <Rucknium[m]> https://github.com/monero-project/meta/issues/690

17:31:35 <sech1> with 8544, if most nodes update well in advance, users will start getting proper warnings

17:31:40 <Rucknium[m]> It could be mostly a matter of better communication. Not sure.

17:31:45 <hyc> perhaps we can add a P2P message to propagate expected update notifications from new daemons to
not-yet-updated daemons

17:32:12 <sech1> hmm, how to avoid fake hardfork P2P messages then?

17:32:45 <Rucknium[m]> Signature verification from Core?

17:33:06 <jberman[m]> using the daemon RPC's get_hard_fork_info would require 2 extra round trips to the
daemon to know if client and daemon are both compatible, and also doesn't perfectly handle the case when there
is a double fork coming up. The changes I made in 8544 add hf version info into get_version so as to avoid
extra trips and more smoothly handle a future multi-fork update like this past one

17:33:10 <sech1> unless we switch to hardfork voting (aka 90% mined blocks have new version number in the
block header).

17:33:21 <sech1> then the old nodes can start suspecting something :D

17:34:28 <sech1> actually, we don't even need new RPC to show warnings on the old nodes. major.minor version
in the block header is enough to deduct there will be a hardfork soon

17:34:36 <hyc> feels like this is more of a -dev topic and not -research

17:34:41 <sech1> true

17:34:43 <rbrunner> Well, I still think if you take all MyMonero-related problems out of the picture, and also
wallets that hang on a very thin thread anyway for a long time already, not much is left

17:34:54 <hyc> agreed

17:36:19 <jberman[m]> a solid number of people reported issues from pointing to outdated nodes in the GUI.
8519 is also supposed to help there

17:36:31 <one-horse-wagon[> rbrunner: My sentiments exactly.

17:36:35 <Rucknium[m]> I wish tevador was here so their interesting proposal could be discussed:
https://github.com/monero-project/research-lab/issues/105

17:39:26 <kayabanerve[m]> Bitcoin had a p2p authenticated message layer. It was never used and there's a
reason they didn't restore it

17:40:29 <hyc> hm, that proposal sounds like can make the commitments both perfectly hiding and perfectly
binding at the same time. pretty great.

17:40:38 <kayabanerve[m]> I'm not personally a fan

17:41:09 <kayabanerve[m]> The byte increase is minimal. My complaint is it solves one problem yet not another

17:41:39 <kayabanerve[m]> The other problem being that if you can know the DL of H, you can know the DL of
everything else and spend users funds

17:42:13 <kayabanerve[m]> So between the integration complexity, the privacy concerns (it becomes an end user
option), and the remaining unsafeness of classical monero in a pq setting...

17:42:43 <kayabanerve[m]> My personal advocacy will just be to disable classical monero entirely when the time
comes. There's not really another discussion viable

17:43:19 <kayabanerve[m]> And that's a brutal comment, yet if an attacker can forge the monetary supply, they
can presumably also forge auth and it wouldn't be prove-able

17:44:52 <kayabanerve[m]> So sure, these are neat (minus the privacy concerns which become an end user
option), yet they don't create a user safe system. Just a protocol safe system. Due to how incomplete that is,
and the privacy concerns, and how it helps Seraphis survive but the need to burn RCT already gives us
precedence... I don't believe it's worth the effort.

17:45:26 <Rucknium[m]> Isn't counterfeiting a bigger forward-time threat than theft? Users can take action
(with enough time) to move their coins to the safer tx type. Are we getting into "turnstile" discussions?

17:45:52 <rbrunner> I don't understand half, but are you sure you don't reason along lines of "If I can't make
it perfect, I am not in the mood to improve" ...

17:47:48 <kayabanerve[m]> Rucknium: My comment is that we can prevent protocol inflation, sure, but doing so
still leaves an unsafe system not cryptographically secured.

17:47:56 <kayabanerve[m]> rbrunner: More lipstick on a pig.

17:48:12 <rbrunner> :)

17:49:04 <kayabanerve[m]> To be clear, part of this isn't fully logical, I have an immediate emotional
aversion to the privacy implications. While I fully understand this is privacy preserving, I assume wallet2
would by default pick the less private mode, as needed to justify this scheme, which gives me anxiety :/

17:49:10 <Rucknium[m]> User keys have to be targeted. Counterfeiting wouldn't require targeting

17:49:44 <kayabanerve[m]> Wait. Is this pointless?

17:49:48 <Rucknium[m]> As in, you have to already know that the target tx output is valuable (which is a point
that at least one study on Monero QC resistance has made)

17:49:51 <kayabanerve[m]> Can't you just still forge the membership proof?

17:50:15 <kayabanerve[m]> And claim non existent commitments exist without needing to break the existing
commitment relationship?

17:51:28 <kayabanerve[m]> ... eh. The argument is we've already upgraded to a PQ membership and are migrating
old commitments.

17:52:13 <kayabanerve[m]> Then yeah, the issue reverts to the fact anyone can migrate anyone's, and a PQ
adversary can still violate fund safety. Just on a user level instead of a protocol level. The note is that
the protocol enabled that theft instead of preventing it.

17:53:14 <kayabanerve[m]> Rucknium[m]: In RingCT land, if we used switch commitments, you'd need to factor two
points and do a 2^64 brute force (feasible even now) to gain access to an output.

17:53:58 <kayabanerve[m]> So yes, it's targeting, and yes, it's 2 per-output, not 1 and $$$. Targeting alone
isn't necessarily hard though.

17:54:14 <kayabanerve[m]> Statistical analysis, getting an exchange to send to you and noting the change...

17:55:48 <kayabanerve[m]> So beyond my personal privacy based aversion, my question becomes do we want the
monero protocol to enable theft, yet prevent inflation? Why wouldn't we want to prevent both? It's a
UX/security trade off and I'd rather pick security so we do properly communicate there is NO migration in the
future and you MUST do it now to preserve your funds.

17:56:30 <kayabanerve[m]> *in the far theoretical future where we deploy a PQ option and then the existing
migration process needs to be deprecated due to a QC being near

17:57:01 <rbrunner> You propose a cut-off date for spendability of RingCT based outputs at some time in the
future?

17:57:49 <kayabanerve[m]> rbrunner: it's needed even with the above proposal.

17:58:13 <kayabanerve[m]> The above proposal would only have Seraphis commitments be secure against inflation
in a setting with a quantum adversary.

17:59:02 <rbrunner> Hmmm, and how would you make a new RingCT output then, after the Seraphis hardfork?

17:59:07 <rbrunner> A forged one

18:00:34 <rbrunner> Ah, maybe you don't forge a bad output, just a bad proof?

18:00:41 <kayabanerve[m]> I'm using the inevitability of the death of RCT outputs, and the remaining
insecurity of Seraphis with a quantum adversary, to argue for the death of Seraphis in however many years
however, instead of user insecurity with protocol security where the protocol enables an attacker it knows
about to profit.

18:00:44 <kayabanerve[m]> ... I was thinking this can be forged at time of spending. Does it need to be forged
at time of creation? 🤔

18:00:56 <kayabanerve[m]> ... it really depends on the proof to migrate from an ECC commitment to a quantum
one, I guess.

18:01:14 <kayabanerve[m]> But if it was only forge-able at time of creation, we wouldn't need switch
commitments :p

18:01:44 <kayabanerve[m]> And I believe it's forge-able without issue at time of spending *so long as you have
an amount that isn't completely invalid*

18:02:08 <rbrunner> I understand even less now, but I am pretty sure a cut-off date for spending of any XMR
won't fly anyway.

18:02:31 <kayabanerve[m]> Cool, that'll cause inflation by a QC in 20 years

18:02:38 <kayabanerve[m]> :p

18:02:47 <rbrunner> I shiver in fear :)

18:03:14 <kayabanerve[m]> It's already a requirement for protocol security. This proposal means the protocol
is secure even under a QC, but users are still left unsafe.

18:03:48 <kayabanerve[m]> So if we already need to force users to migrate 20 years from now due to a QC, I'd
rather ensure they migrate before necessary and not let a quantum adversary steal funds.

18:04:35 <kayabanerve[m]> So I personally appreciate this proposal, and it does offer protocol security
increasing the amount of XMR we don't have to cut off, yet it doesn't achieve safe long term storage of funds
which is the reason why we don't want to cut off outputs.

18:04:35 <Rucknium[m]> Maybe I should read that CCS-funded QC report 🤔

18:04:42 <kayabanerve[m]> So it misses the point IMO

18:04:57 <kayabanerve[m]> *while increasing the amount

18:05:24 <kayabanerve[m]> I'll post my thoughts on the issue. I've talked here long enough :p

18:05:49 <rbrunner> Certainly a good idea

18:06:46 <hyc> definitely a good idea to outline on the issue what threats are being addressed

18:06:49 <Rucknium[m]> Ok good. We end on a cliffhanger. "Find out next time if Monero will survive the QC
revolution" :P


```
Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: Rucknium | 2022-08-29T23:13:30+00:00
- Closed at: 2022-09-05T15:45:19+00:00
