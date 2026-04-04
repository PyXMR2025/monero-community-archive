---
title: Monero Research Lab Meeting - Wed 27 September 2023, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/901
author: Rucknium
assignees: []
labels: []
created_at: '2023-09-27T14:35:13+00:00'
updated_at: '2023-10-11T14:34:23+00:00'
type: issue
status: closed
closed_at: '2023-10-11T14:34:23+00:00'
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

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#897 

# Discussion History
## plowsof | 2023-10-07T13:18:00+00:00
Logs 
```
17:00:57 <Rucknium> Meeting time! https://github.com/monero-project/meta/issues/901

17:01:07 <Rucknium> 1) Greetings

17:01:12 <m-relay> <v​tnerd:monero.social> Hi

17:01:17 <rbrunner> Hello

17:03:37 <Rucknium> 2) Updates. What is everyone working on?

17:04:18 <m-relay> <v​tnerd:monero.social> Me: subaddressses in lws.

17:05:00 <Rucknium> me: Created some data tables to help "someone(s)" to track down which wallet
implementations may be producing nonstandard fee txs: https://github.com/Rucknium/misc-
research/tree/main/Monero-Nonstandard-Fees

17:05:53 <endogenic> i have some major improvements to fee normalization for lws clients fwiw

17:06:01 <endogenic> publishing momentarily

17:06:49 <endogenic> not sure if i should mention it so soon but i even normalized tx creation code

17:07:00 <endogenic> (discarding my custom entrypoint to cryptonote tx utils)

17:07:28 <rbrunner> I guess that normal users / non-devs have a hard time to see whether their fee is standard
or not when they transact with those wallets?

17:07:29 <Rucknium> Thanks. How do your improvements interact with jberman's fixes to MyMonero's fee
calculations?

17:08:16 <endogenic> which fixes, his old ones from like 2 yrs ago? one he solicited my feedback on causing me
to get banned on a certain github org's repos?

17:08:47 <Rucknium> rbrunner: I don't think so. Users just need to check what the fee per byte in the wallet
UI tells them. If it doesn't tell them, then they can look up the tx ID on xmrchain.net

17:09:04 <Rucknium> Yes, I think those fixes.

17:09:18 <endogenic> it supersedes them.. no need for them

17:09:31 <endogenic> they ensure decoy out pinning to previously chosen spendable outs

17:09:42 <endogenic> wallet2 code does that naturally

17:09:53 <endogenic> brb

17:10:54 <rbrunner> I was brainstorming about making a post on Reddit to get broader help, and there all kinds
of people would potentially try, also some that have never even seen a block explorer

17:11:23 <rbrunner> But not sure whether those people would be ready to transact and then send the tx id
somewhere, for inspection

17:11:56 <Rucknium> Exact fee calculation seems hard to me. Fee is part of a tx (as a variable integer C++
data type(?)). You have to know what the fee is to calculate the fee based on fee per byte. It's a little
recursive.

17:12:44 <Rucknium> In the tables I Just tried to get clusters of fees that were far from any standard fee
level so I didn't have to think about fees that are very close, but not quite, what wallet2 does.

17:13:42 <Rucknium> rbrunner: You can run the xmrchain.net block explorer locally if you have a non-pruned
monerod node. So they can avoid any privacy issues that way.

17:13:54 <endogenic> The fee is based on the data size or so-called weight of a transaction, and the fee field
is of fixed data size, so it should not actually affect the fee calculation

17:15:20 <Rucknium> Ok. I based what I said on Zero to Monero 2.0 "Transaction fee: stored as a variable
length integer, so ≤ 9 bytes". I don't know the details of the code, of course.

17:15:35 <rbrunner> Sure. We are talking a little past each other, maybe :) I am thinking about the proverbial
"grandmother" at the smartphone Monero wallet

17:16:06 <rbrunner> But never mind, will think about a little more

17:16:13 <plowsof> hello

17:16:22 <Rucknium> I agree that this treasure hunt isn't for grandmothers :)

17:16:57 <endogenic> oops

17:17:06 <endogenic> i'll have to go back and check. I did say that without full confirmation.

17:18:27 <Rucknium> plowsof: Did you have an update?

17:18:34 <endogenic> anyway, if the fee is actually stored as a variable length, it should probably be padded
for fungibility

17:20:47 <Rucknium> It looks like we are already in 3) Discussion. What do we want to discuss?

17:21:43 <rbrunner> If anything, what plowsof reported in Monday's wallet workgroup meeting, log here:
https://github.com/monero-project/meta/issues/898

17:21:51 <plowsof> apologies for the late update. for the BP++ peer review from CypherStack - i have added the
"out of scope" feedback received after they looked at the new paper (i placed an asterisk on "Efficiency"
incase the "Optimised Binary range proofs" point effects that (to be confirmed) but the price, for the new
paper will be $32,000

17:23:39 <Rucknium> So we would need to raise about 13,000 USD more in a new CCS, correct?

17:24:02 <Rucknium> Because we have https://ccs.getmonero.org/proposals/bulletproofs-pp-peer-review.html

17:25:22 <rbrunner> Looks like that to me

17:25:40 <plowsof> correct, more funds would have to be raised / come from somewhere.

17:26:24 <Rucknium> Probably MAGIC would be willing to host the fundraiser. CCS could too, of course.

17:27:08 <rbrunner> Is there somewhat more to do than assumed back in March when we did the original CCS?

17:27:21 <rbrunner> I mean, for CypherStack

17:28:52 <plowsof> i have not yet collated initial feedback / replied to zksecurity yet (tooth/ear/gum issues)
- but the reply to their interest would be pushing them to agree to a scope of work / concrete deliverables -
and aiming for a lower funding cost of $10k/week, and also if possible a '3 month' longer term grant (if they
feel that its required)

17:29:09 <Rucknium> plowsof: Has anyone given any reasons not to raise the rest of the funds for BP++ peer
review?

17:30:38 <plowsof> this is the first time sharing the new price

17:31:02 <Rucknium> Have any Monero-associated cryptographers commented about whether zksecurity would be a
good firm to do the job?

17:32:33 <rbrunner> I also wonder a bit who would go into concrete negotiations with them, as a question of
organisation on our side ...

17:34:49 <Rucknium> "We tried, but couldn't construct a math proof of security" is a possible outcome. That
makes this tricky.

17:34:53 <rbrunner> Anyway, the list of "our" cryptographers is not that long, probably UkoeHB, Tevador,
kayabaNerve and maybe lately and upcoming Jeffro256

17:35:41 <m-relay> <k​ayabanerve:matrix.org> jberman:

17:36:01 <m-relay> <k​ayabanerve:matrix.org> I believe they reached out to ZkSecurity, though I may be
thinking of a different firm.

17:38:44 <plowsof> zksecurity are interested , the tldr is they need to (after feedback received from some
nwlb/mrl members) is to tell us what they plan on doing (with concrete deliverables) for a 3 month time scale
which has been the norm for our funding platforms and push for the low end of their rates ($10k/week)

17:40:51 <plowsof> $120k for 3 month seraphis work would have to show its worth ... and then we
compare/contrast as cypherstack are also interested in seraphis work

17:41:10 <rbrunner> Well, yes, devs use to make 3 months CCSs, but for cryptographical work I think we could
easily be more flexible

17:41:37 <Rucknium> Isn't the scope Gist supposed to provide deliverables? We're dragging this out.

17:42:38 <rbrunner> All on my own I would probably entrust them first with something of smaller size, just to
test, say something that could be done in 3 weeks or, like the BP++ stuff

17:42:50 <rbrunner> and only then move up into six figure regions

17:42:57 <plowsof> ok, pin them on this https://gist.github.com/plowsof/8cb33e2efe4bf0239927ad3bd92326e0 and
receive the quote/timescales from Zksecurity + CS?

17:44:03 <Rucknium> The root of this problem is laying down a protocol and code without security proofs to
back them up.

17:45:29 <Rucknium> People who don't do cryptography (rbrunner, plowsof, me) cannot do this part of the
project IMHO.

17:45:36 <rbrunner> +1

17:45:47 <plowsof> <j​berman> The third bullet point would be blocked until the address spec is settled, but
creating a formal security model would not be*

17:46:47 <rbrunner> That's just a little additional problem on top of it all :)

17:47:28 <Rucknium> I try to provide some research infrastructure (moneroresearch.info, list of open research
questions, technical review on MAGIC committee), but I have limits and I have to focus on my own research.

17:48:00 <rbrunner> Maybe some of those cryptographers reads this log and is in the mood to take the lead here

17:48:14 <rbrunner> *Maybe one

17:50:08 <Rucknium> To be clear, no one owes Monero any labor. If our constraints include "we don't have
enough expert labor to move certain projects forward", then I can work within those constraints.

17:51:22 <rbrunner> Agree. Such things tend to go astray anyway if you try to force them. True interest
probably has no substitute.

17:52:51 <rbrunner> Let's wait and see a bit, Monero usually muddles through somehow.

17:53:57 <Rucknium> Bring back Triptych. It has security proofs :)

17:54:59 <rbrunner> Isn't that even implemented as well?

17:58:04 <Rucknium> I don't know. We can close the meeting here. Thanks everyone.


```
Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: Rucknium | 2023-09-27T14:35:13+00:00
- Closed at: 2023-10-11T14:34:23+00:00
