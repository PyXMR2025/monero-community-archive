---
title: Monero Research Lab Meeting - Wed 30 August 2023, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/888
author: Rucknium
assignees: []
labels: []
created_at: '2023-08-29T21:28:31+00:00'
updated_at: '2023-09-05T17:48:22+00:00'
type: issue
status: closed
closed_at: '2023-09-05T17:48:22+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Discuss: Reducing 10 block lock: https://github.com/monero-project/research-lab/issues/102#issuecomment-1577827259

3. Discuss: [Exploring Trustless zk-SNARKs for Monero's payment protocol](https://github.com/monero-project/research-lab/issues/100). What are the bottlenecks for potential implementation?

4. Improvements to the decoy selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

5. Seraphis. ( [UkoeHB's Seraphis Proof of Concept work](https://ccs.getmonero.org/proposals/seraphis-wallet-poc-2.html), [Seraphis repo](https://github.com/UkoeHB/Seraphis) ).

6. MRL Meta: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [MoneroResearch.info repository of Monero-related research papers](https://moneroresearch.info/), [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

7. Any other business

8. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#884 

# Discussion History
## plowsof | 2023-08-30T09:59:06+00:00
BP++ peer review: Do we return to cypherstack saying "yes, the out of scope things are fine, what are the next steps now" https://gist.github.com/plowsof/534778636eca474951e4661507cdc205

Seraphis: this draft scope of work to make the papers(s) complete will be used to approach auditors for quotes unless someone states something is missing https://gist.github.com/plowsof/8cb33e2efe4bf0239927ad3bd92326e0

## plowsof | 2023-08-30T18:27:51+00:00
Logs 
```
17:01:07 <Rucknium> Meeting time: https://github.com/monero-project/meta/issues/888

17:01:19 <Rucknium> 1) Greetings

17:01:41 <m-relay> <v​tnerd:monero.social> Hi

17:01:49 <rbrunner> Hello. Given the number of 888, this will be one lucky meeting.

17:02:10 <m-relay> <d​angerousfreedom:matrix.org> Hello

17:03:28 <Rucknium> 2) Updates: What is everyone working on?

17:04:48 <Rucknium> me: N block lock analysis (scope expanded). Identifying nonstandard fees on the blockchain
(analysis is paying off).

17:06:25 <Rucknium> Announcements: CCS Retroactive funding for Full Chain Membership Proofs is expected to be
decided by the end of the week: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/403

17:06:32 <m-relay> <c​ompdec:matrix.org> I'm continuing on EAE stuff, hoping to hear more about my submission
soon.

17:07:32 <m-relay> <v​tnerd:monero.social> I've got SSL+p2p coded up, including optional authentication, but
there's still at least 1 bug for me to track down

17:07:34 <Rucknium> bitcoincashautist has a proposal for BCH<>XMR atomic swaps:
https://gitlab.com/0353F40E/cross-chain-swap-ves/-/blob/master/README.md

17:07:45 <Rucknium> More discussion: https://bitcoincashresearch.org/t/monero-bch-atomic-swaps/545

17:07:56 <Rucknium> There is a 10.5 XMR + 2 BCH bounty open:
https://bounties.monero.social/posts/37/10-501m-bch-xmr-atomic-swaps

17:08:50 <Rucknium> compdec: by "hoping to hear more about my submission soon" do you mean "hoping for
feedback soon"?

17:10:20 <m-relay> <c​ompdec:matrix.org> yeah, Justin seems to want more before considering the milestone is
completed, but I can only guess at that

17:11:17 <Rucknium> 3) Discussion. plowsof added two agenda items to the meeting GitHub issue:

17:11:37 <Rucknium> "BP++ peer review: Do we return to cypherstack saying "yes, the out of scope things are
fine, what are the next steps now" https://gist.github.com/plowsof/534778636eca474951e4661507cdc205 "

17:11:51 <Rucknium> "Seraphis: this draft scope of work to make the papers(s) complete will be used to
approach auditors for quotes unless someone states something is missing
https://gist.github.com/plowsof/8cb33e2efe4bf0239927ad3bd92326e0 "

17:12:01 <m-relay> <c​ompdec:matrix.org> I'll update the document by Friday with more progress

17:12:29 <Rucknium> compdec: Thanks.

17:13:11 <Rucknium> Anyone have opinions about the BP++ peer review scope?

17:14:02 <rbrunner> Pretty much out of my depth here ...

17:14:22 <Rucknium> Me, too.

17:15:24 <Rucknium> Here is the original scope: https://ccs.getmonero.org/proposals/bulletproofs-pp-peer-
review.html

17:16:59 <rbrunner> I guess we can agree on "Multi-asset transactions" being out of scope. We don't have
multiple assets, and probably never will, if I understand "assets" correctly

17:17:21 <rbrunner> (as something like different "coins" also living on the Monero blockchain)

17:17:39 <Rucknium> The scope looks reasonable to me, but I don't know much about cryptography at this level.

17:18:05 <Rucknium> I think plowsof was seeking input from tevador at least.

17:18:49 <Rucknium> What about the Seraphis draft scope of work?

17:20:14 <rbrunner> Pass :)

17:20:53 <m-relay> <d​angerousfreedom:matrix.org> At least the batch verification of bp++ should be done,
right?

17:21:49 <rbrunner> I think talk was it would be good to have, but well, if the paper is light on details? "it
provides no details on the corresponding algebra"

17:22:09 <Rucknium> That would be asking Cypherstack to develop the math for batch verification. That's
different from reviewing what's already in the paper. It could be requested, maybe.

17:22:24 <m-relay> <g​hostway:matrix.org> If it doesn't slow you down, do you have a mid-analysis report?
Sounds interesting

17:22:24 <rbrunner> Sounds reasonable

17:22:41 <Rucknium> Biu then they cannot review their open implementation

17:22:55 <m-relay> <d​angerousfreedom:matrix.org> Oh okay, sorry. I didnt read the bp++ paper yet

17:22:57 <Rucknium> But*

17:23:12 <Rucknium> own implementation*

17:25:29 <plowsof> The seraphis scope of things to be done has the approval of those who made it
(kayaba/koe/jberman)

17:25:30 <Rucknium> ghostway: I will post a gist about the fee analysis after the meeting. I don't have much
about N block lock ready to go. Mostly just the table of attack success probabilities. Rosenfeld (2014)
already has that for N <= 10.

17:25:40 <m-relay> <d​angerousfreedom:matrix.org> Where can I find the link of the c++ implementation of bp++
?

17:26:28 <Rucknium> Rosenfeld (2014). See Table 1:
https://moneroresearch.info/index.php?action=resource_RESOURCEVIEW_CORE&id=191

17:27:33 <m-relay> <g​hostway:matrix.org> Ok

17:27:33 <m-relay> <g​hostway:matrix.org> Is how to do the swap (in the bounty) already closed? Or are there
problems still

17:28:34 <rbrunner> Are you asking about the BCH-XMR swap?

17:28:42 <m-relay> <v​tnerd:monero.social> https://blog.blockstream.com/bulletproofs-a-step-towards-fully-
anonymous-transactions-with-multiple-asset-types/

17:29:08 <m-relay> <v​tnerd:monero.social> There's links in the post to the pr requests

17:29:12 <m-relay> <g​hostway:matrix.org> Yep rbrunner

17:29:26 <Rucknium> ghostway: bitcoincashautist has not claimed the bounty by executing his swap on the
mainnets. I'm not sure why.

17:30:22 <m-relay> <g​hostway:matrix.org> Huh

17:30:33 <Rucknium> We would need a knowledgeable person to review the swap after it happened to make sure it
is truly atomic.

17:31:34 <Rucknium>
https://www.reddit.com/r/btc/comments/1455rxe/bchxmr_atomic_swaps_solution_using_introspection/

17:31:48 <Rucknium> "There's a 10 XMR bounty for the implementation! Feel free to go for it using my contract,
you don't owe me anything."

17:33:02 <m-relay> <g​hostway:matrix.org> That's odd

17:33:02 <m-relay> <d​angerousfreedom:matrix.org> Thanks. So what is being done is just a theoretical review
of the bp++ paper ? We still need to implement it using our curve?

17:33:54 <Rucknium> dangerousfreedom: AFAIK, it's just a review of the mathematics. Not a code audit.

17:33:54 <m-relay> <v​tnerd:monero.social> Correct. The paper initially had no peer review, not sure about the
latest iteration

17:34:25 <Rucknium> The authors submitted it to a conference earlier this year, but it didn't make it in.

17:34:45 <m-relay> <d​angerousfreedom:matrix.org> Okay, thanks. Someone is working on implementing it to be
used in Monero?

17:36:22 <Rucknium> IIRC, we don't know if BP++ is compatible with kayabaNerve's Full Chain Membership Proofs
proposal.

17:36:26 <rbrunner> Didn't vtnerd go the way at least in part?

17:36:49 <m-relay> <k​ayabanerve:matrix.org> BP++ supports ACs.

17:36:58 <m-relay> <v​tnerd:monero.social> Yes I did, but I stopped as I couldn't figure out the last part,
without just blindly copying the c variant

17:37:34 <Rucknium> kayabaNerve: does that mean they are compatible?

17:37:42 <m-relay> <k​ayabanerve:matrix.org> The issue is that Curve Trees requires a VCS on top of a R1CS AC
proof, and the only known applicable VCS is an unproven one for BPs (if you ignore my hack).

17:37:48 <m-relay> <v​tnerd:monero.social> And I think at least one portion of the c/blockstream variant had
an unnecessary calculation in it, but who knows

17:38:32 <m-relay> <k​ayabanerve:matrix.org> sarang is currently researching a VCS for BP+, one of the reasons
being BP++ argues its norm argument reduces to BP+'s weighted inner product argument, which BP+ in turn argues
can be used in place of BP's inner product argument.

17:38:34 <m-relay> <d​angerousfreedom:matrix.org> Okay, cool! Thanks vtnerd ! Hopefully I will find some time
this year to read the paper (and the code if ready)

17:39:08 <m-relay> <k​ayabanerve:matrix.org> So BP++ has the bones, an extra piece is needed, sarang is
researching that piece for BP+, that piece for BP+ likely helps development of a similar piece for BP++.

17:39:30 <Rucknium> Thanks for explaining, kayaba

17:39:39 <rbrunner> Who finances that research?

17:40:23 <m-relay> <k​ayabanerve:matrix.org> Though of course, FCMPs can use BPs while range proofs use BP++s.

17:40:44 <m-relay> <k​ayabanerve:matrix.org> rbrunner: Right now, Firo.

17:40:51 <rbrunner> Ah, ok, thanks.

17:40:54 <m-relay> <k​ayabanerve:matrix.org> It's part of the collaboration I orchestrated prior to and at
Monerokon.

17:41:05 <rbrunner> Yeah, yeah, I think I remember now.

17:41:48 <Rucknium> kayabaNerve: iI the scope on the BP++ peer review satisfactory to you?

17:41:50 <rbrunner> At least not in immediate danger of more "retroactive funding" drama, right?

17:47:03 <Rucknium> More discussion? (If not, I can talk about N block lock and nonstandard fee analysis.)

17:48:16 <Rucknium> My question is "What does Monero gain from having a 10 block lock instead of a 9 block
lock? What does it lose from not having an 11 block lock?"

17:48:36 <m-relay> <k​ayabanerve:matrix.org> Rucknium: I don't know what the scope is, sorry

17:49:19 <Rucknium> https://ccs.getmonero.org/proposals/bulletproofs-pp-peer-review.html  is the original
scope

17:49:55 <Rucknium> https://gist.github.com/plowsof/534778636eca474951e4661507cdc205 is the modifications to
the scope after they looked at the paper

17:51:43 <Rucknium> I thought for a complete analysis we would want to know the security budgets of PoW coins
that have had malicious deep block reorgs. Then compare with Monero's security budget.

17:52:06 <Rucknium> A coin's "security budget" is the coin unit's purchasing power multiplied by its block
reward emission to miners. endor00 and I are starting to gather that data.

17:52:20 <m-relay> <d​angerousfreedom:matrix.org> I add to your question, should the lock time be a wallet
feature?

17:52:45 <m-relay> <k​ayabanerve:matrix.org> Feedback is sane. IIRC, the binary range proofs (optimized or
not) don't need to be in scope as the way BP++ achieves its range proof perf is via a hexadecimal base.

17:53:32 <Rucknium> Block time be a wallet feature? It used to be default in wallet2, but not consensus. Then
it was changed to consensus since some wallet software did not use the N block lock.

17:53:35 <m-relay> <k​ayabanerve:matrix.org> dangerousfreedom: Considering it's a security function which
would be a mess for opt-in wallets to track if wallets can opt-out, I'd vote no.

17:54:51 <m-relay> <g​hostway:matrix.org> Is it actually about double spending or is it about reorderingm

17:54:54 <m-relay> <g​hostway:matrix.org> ?

17:55:17 <Rucknium> It's about lots of things.

17:55:24 <m-relay> <k​ayabanerve:matrix.org> To be clear on BP++, as my only other comment, it sounds
infeasible to scope MPC at this time. That should be dropped, which it sounds like it may have been?

17:56:14 <m-relay> <k​ayabanerve:matrix.org> It's mainly about the chain reaction as one TX being reordered
invalidates all future TXs, AFAIK

17:56:33 <Rucknium> It prevents maliously double spends. Also, since ring members in Monero are referenced by
index number in the chain and rings that reference outputs that are no longer in the chain are invalid, a deep
re-org can invalidate txs completely.

17:56:37 <m-relay> <k​ayabanerve:matrix.org> Though also, I retract my comment on wallet implementation
difficulties. I didn't think it through, yet I think we could make it opt-in/opt-out...

17:57:02 <m-relay> <g​hostway:matrix.org> That's what I guessed, making decoys invalid and reducing the ring
size

17:57:02 <m-relay> <k​ayabanerve:matrix.org> Whether or not we should remains a discussion, just not impeded
by wallet dev complexity.

17:57:50 <Rucknium> Two issues on the 10 block lock: https://github.com/monero-project/research-lab/issues/95

17:57:51 <Rucknium> https://github.com/monero-project/research-lab/issues/102

17:59:10 <m-relay> <d​angerousfreedom:matrix.org> I remember when you needed 6 confirmations in bitcoin to get
a transaction accepted on an exchange for example. Today there are some that accepts even with 1 confirmation.
I guess the limiting factor would be the hashing power of the network then? Is there any studies to correlate
with hashing power to analyze that probabilistic ?

17:59:48 <Rucknium> Originally, I thought the anti-double-spend justification for the 10 block lock was
paternalistic. It is paternalistic, but there is also a moral hazard problem with centralized exchanges
deciding to accept a low confirmation number.

18:00:24 <Rucknium> dangerousfreedom: Yes, Rosenfeld (2014) does those calculations for minority hashpower
share.

18:00:30 <m-relay> <g​hostway:matrix.org> Id imagine it's more about % of the total hashrate like rucknium's
paper suggests

18:00:43 <Rucknium> We know the attack success probabilities for any hsahpower share.

18:00:58 <plowsof> binance accepts Monero deposits after 3 confirmations

18:01:52 <Rucknium> By "moral hazard" I mean the standard economics definition: An agent makes a risky
decision where the agent does not bear 100% of the potential negative consequences for that decision

18:02:55 <Rucknium> If an exchange becomes the victim of a double spend attack, they lose money. But the coin
itself loses confidence, too.

18:03:19 <Rucknium> We are past the hour. Let's end the meeting here. Thanks everyone.


```
Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: Rucknium | 2023-08-29T21:28:31+00:00
- Closed at: 2023-09-05T17:48:22+00:00
