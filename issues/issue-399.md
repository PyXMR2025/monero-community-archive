---
title: 'Research meeting: 14 October 2019 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/399
author: SarangNoether
assignees: []
labels: []
created_at: '2019-10-10T18:46:04+00:00'
updated_at: '2019-10-14T17:53:28+00:00'
type: issue
status: closed
closed_at: '2019-10-14T17:53:28+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Monday, 14 October 2019 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable
a. Sarang
b. Surae
c. Others?

3. General questions

4. Action items

# Discussion History
## SarangNoether | 2019-10-14T17:53:28+00:00
    [2019-10-14 12:59:47] <sarang> GREETINGS
    [2019-10-14 12:59:57] <suraeNoether> howdy!
    [2019-10-14 13:01:04] <sgp_> Hello
    [2019-10-14 13:01:06] <sarang> Small crowd today, apparently
    [2019-10-14 13:01:12] <sarang> Even so, we carry on
    [2019-10-14 13:01:17] <sarang> Let's move to ROUNDTABLE
    [2019-10-14 13:01:27] <sarang> I've been working on a few things this past week
    [2019-10-14 13:01:44] <sarang> First is getting caught up with the usual literature review
    [2019-10-14 13:02:08] <sarang> Second was finalizing things for World Crypto Conference and some background research associated to that
    [2019-10-14 13:02:20] <sarang> Third was getting balance proofs working in Triptych, which is now successful
    [2019-10-14 13:03:04] <xmrmatterbridge> <serhack> hello
    [2019-10-14 13:03:17] <sarang> This means that Triptych now supports a single proof showing all spends, correct key image construction, and balance
    [2019-10-14 13:03:30] <suraeNoether> nice!
    [2019-10-14 13:03:38] <sarang> How about you, suraeNoether?
    [2019-10-14 13:04:42] <suraeNoether> i've been furiously debugging my matching code as my primary task. there are some persistent problems. i wanted to finish this weekend but it didn't happen
    [2019-10-14 13:05:04] <sarang> Earlier you had indicated some known bugs... are these the same?
    [2019-10-14 13:05:16] <suraeNoether> no... every problem i solve reveals like... a small handful of new bugs, but the newer and newer bugs are becoming less frequent and less severe
    [2019-10-14 13:05:33] <suraeNoether> it *feels* like there's a single problem lurking that will cause the house of cards to stop falling down
    [2019-10-14 13:05:35] <suraeNoether> i'm very close.
    [2019-10-14 13:05:43] <suraeNoether> i really wanted it to be today
    [2019-10-14 13:06:12] <suraeNoether> i'm taking a break later today to read sarang's WCC talk (sorry for the delay on that) and I am taking a break later today to work on *literally anything else*
    [2019-10-14 13:06:34] <suraeNoether> i'm very frustrated with this project
    [2019-10-14 13:06:58] <sarang> Are the known bugs documented anywhere, so others might assist you?
    [2019-10-14 13:07:07] <suraeNoether> i'm sure a lot of community members are also frustrated, but i this is nearing completion
    [2019-10-14 13:07:23] <suraeNoether> no
    [2019-10-14 13:07:46] <suraeNoether> "test X not working for unknown reason" is not a helpful document to write
    [2019-10-14 13:08:36] <sarang> Hmm ok
    [2019-10-14 13:09:36] <sarang> Well, I selfishly hope you will take time off that project today and review my talk :D
    [2019-10-14 13:09:47] <sarang> Perhaps it will also help you clear your head
    [2019-10-14 13:10:41] <sarang> Does anyone else have interesting research to share as well?
    [2019-10-14 13:12:11] <sarang> In that case, let's go ahead and discuss ACTION ITEMS first, and then any lingering questions
    [2019-10-14 13:13:28] <sarang> First, I have an efficient verifier for the inner-product argument in IACR/944 that I've been meaning to implement in kenshamir[m]'s Rust code, which will be useful for benchmarking... that's in progress but with some algebra problems that I'm working out
    [2019-10-14 13:14:01] <sarang> Second, Triptych needs plenty more work: key aggregation, better Fiat-Shamir challenges, and some questions on proof elements and efficiency
    [2019-10-14 13:14:33] <sarang> Third, I want to see if it's possible to backport some of the new RCT3 changes to the older version without using spend aggregation, to check the resulting efficiency
    [2019-10-14 13:14:43] <sarang> and that's about it for now
    [2019-10-14 13:14:47] <sarang> suraeNoether: ?
    [2019-10-14 13:15:17] <suraeNoether> pushing this commit once my code is flowing. reading your WCC talk. catching up on tryptychychch
    [2019-10-14 13:16:24] <sarang> It definitely remains to be seen how efficient we can make Triptych... but as I mentioned last week, the underlying changes to the Groth proving system are very interesting regardless
    [2019-10-14 13:17:45] <sarang> and, as before, there is no security model for it yet
    [2019-10-14 13:19:50] <sarang> All righty, are there other questions on research?
    [2019-10-14 13:19:55] <sarang> This meeting has gone quite quickly
    [2019-10-14 13:21:57] <sarang> Oh, one note about what Isthmus brought up last week regarding transaction keys and subaddresses
    [2019-10-14 13:22:15] <sarang> It is apparently still the case that transactions to only standard addresses retain a single transaction key
    [2019-10-14 13:22:37] <sarang> Mandating separate transaction keys for all outputs would add 32 bytes to each additional output
    [2019-10-14 13:22:41] <sgp_> Standard = 4?
    [2019-10-14 13:22:55] <sarang> but we're already saving > 32 bytes per output after the last change to the Pedersen mask format anyway
    [2019-10-14 13:24:14] <moneromooo> Could there be a way to deterministically generate keypairs in such a way that the sender generates the secret keys from a seed, the recipients generate the pubkeys ? I think Bitcoin has such a scheme for generating addresses.
    [2019-10-14 13:24:57] <moneromooo> And hopefully the seed is <= 32 bytes :)
    [2019-10-14 13:25:13] — Isthmus clocks in
    [2019-10-14 13:25:21] — Isthmus starts catching up on backlog
    [2019-10-14 13:25:22] <sarang> Well, a big selling point of subaddresses is the efficient scanning across all addresses at once
    [2019-10-14 13:25:38] <sarang> Isthmus: only need to read up a few lines
    [2019-10-14 13:26:32] <moneromooo> Would such a scheme invalidate the efficient scanning ? It seems doubtful since the tx keys are currently arbitrary.
    [2019-10-14 13:26:46] <sgp_> How much effort is it to scan and see what proportion of transactions are only to standard addresses?
    [2019-10-14 13:26:59] <sarang> sgp_: to get a distribution of how common subaddresses are?
    [2019-10-14 13:27:10] <Isthmus> @sgp_ I think that @n3ptune accidentally did that recently
    [2019-10-14 13:27:18] <Isthmus> Lemme see if the plots are on GitHub anywhere
    [2019-10-14 13:27:22] <sgp_> sarang: essentially yes
    [2019-10-14 13:27:23] <sarang> Presumably this would be affected by which large players (like exchanges) support them
    [2019-10-14 13:27:43] <sgp_> Thanks Isthmus
    [2019-10-14 13:28:04] <Isthmus> https://github.com/noncesense-research-lab/tx_extra_analysis/blob/master/tx_extra_viz.ipynb
    [2019-10-14 13:28:16] <sarang> 404
    [2019-10-14 13:29:57] <Isthmus> Oh, private repo. Lemme grab the juicy parts
    [2019-10-14 13:30:32] <Isthmus> This might be the relevant one
    [2019-10-14 13:30:33] <Isthmus> https://usercontent.irccloud-cdn.com/file/LgrrzOIS/image.png
    [2019-10-14 13:31:14] <Isthmus> I suspect the diagonal is transactions that include a subaddress, while the horizontal bands are primary-only
    [2019-10-14 13:31:23] <Isthmus> Though I'm open to alternate interpretations
    [2019-10-14 13:31:30] <moneromooo> Oh I get it. The fast lookup would still exist, but verifiers would have to generate pubkeys, and *that* might be slow.
    [2019-10-14 13:31:45] <sgp_> Thanks
    [2019-10-14 13:33:26] <Isthmus> If that is the case, then I can slide a window over time and calculate fraction of transactions that appear to include no subaddresses
    [2019-10-14 13:34:14] <sgp_> I'm not the one who can say yes or no to that :/
    [2019-10-14 13:34:44] <sarang> Probably worth bringing up at the next dev meeting to see what others think of it
    [2019-10-14 13:34:52] <moneromooo> It is trivial to know whether >= 1 subaddress was used as an output in a tx.
    [2019-10-14 13:34:58] ⇐ ferretinjapan quit (ferretinja@gateway/vpn/privateinternetaccess/ferretinjapan): Quit: Leaving
    [2019-10-14 13:34:58] <moneromooo> If that was the question...
    [2019-10-14 13:35:27] <moneromooo> Oh wait. Maybe not, there's some funky going on with change being treated differently...
    [2019-10-14 13:40:07] <sgp_> A more meta question: how did this happen? What could have been done differently to help prevent this from happening?
    [2019-10-14 13:40:59] <sarang> That's probably a question for someone like stoffu who was more directly involved in the code
    [2019-10-14 13:41:11] <sarang> I suspect space saving was one consideration
    [2019-10-14 13:41:15] <sgp_> knaccc too?
    [2019-10-14 13:41:21] <sarang> but it's quite minor for the most part
    [2019-10-14 13:41:47] <Isthmus> @sgp_ meta answer: we rolled out a new feature that:
    [2019-10-14 13:41:54] <Isthmus> 1) you could tell use from blockchain as external observer
    [2019-10-14 13:41:56] <Isthmus> 2) was optional
    [2019-10-14 13:42:09] <Isthmus> Either one of those alone is ok, but together we end up in this situation.
    [2019-10-14 13:42:28] <sgp_> I always assumed 1 wasnt the case. I was very misinformed and thus misinformed others
    [2019-10-14 13:43:06] <Isthmus> Yeah, I think we're all just putting 2+2 together on that now
    [2019-10-14 13:45:13] <sarang> OK, something to discuss at next dev meeting, then
    [2019-10-14 13:45:19] <sarang> Are there any other topics to discuss for this meeting?
    [2019-10-14 13:45:37] <Isthmus> Oh yea, lemme grab a link
    [2019-10-14 13:46:39] <Isthmus> The CryptoEconSec paper by hasu and all is very interesting, and parts are relevant to both Monero and our lock time conversation
    [2019-10-14 13:46:46] <Isthmus> *et al
    [2019-10-14 13:47:08] ⇐ rex4539 quit (~rex4539@balticom-197-78.balticom.lv): Quit: rex4539
    [2019-10-14 13:47:34] <Isthmus> I definitely recommend reading it. Very approachable.
    [2019-10-14 13:47:38] <Isthmus> Here's the writeup: https://uncommoncore.co/research-paper-a-model-for-bitcoins-security-and-the-declining-block-subsidy/
    [2019-10-14 13:47:49] <Isthmus> And here is my analysis: https://twitter.com/Mitchellpkt0/status/1183581226357014528
    [2019-10-14 13:48:35] <Isthmus> I won't rehash it all here. Just take a pass through on your next commute. :- )
    [2019-10-14 13:49:36] <sarang> Thanks Isthmus 
    [2019-10-14 13:49:47] <sarang> Any last questions before we adjourn and continue discussions?
    [2019-10-14 13:51:35] <sarang> Righto, thanks to everyone for attending!


# Action History
- Created by: SarangNoether | 2019-10-10T18:46:04+00:00
- Closed at: 2019-10-14T17:53:28+00:00
