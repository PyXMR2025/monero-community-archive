---
title: Monero Research Lab Meeting - Wed 14 August 2024, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1057
author: Rucknium
assignees: []
labels: []
created_at: '2024-08-13T20:51:57+00:00'
updated_at: '2024-08-26T20:22:48+00:00'
type: issue
status: closed
closed_at: '2024-08-26T20:22:48+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://web.archive.org/web/20230128130949/https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Stress testing `monerod`](https://github.com/monero-project/monero/issues/9348)

4. [Potential measures against a black marble attack](https://github.com/monero-project/research-lab/issues/119).

5. Research [Pre-Seraphis Full-Chain Membership Proofs](https://www.getmonero.org/2024/04/27/fcmps.html).

6. Any other business

7. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1052 

# Discussion History
## Rucknium | 2024-08-19T17:55:48+00:00
Logs



Rucknium: Meeting time! https://github.com/monero-project/meta/issues/1057
Rucknium: 1) Greetings
one-horse-wagon: Hello.
ArticMine: Hi
r​brunner: Hello
jberman: *waves*
Rucknium: 2) Updates. What is everyone working on?
0xfffc: hi everyone. apologies. I have urgent issue to debug a minor issue with the serializatoin benchmark we need ( to measure the max limits of benchmark ). Plus I don't have any other update than what we talked Monday ( finishing this limit numbers, then going to BSS dynamic algorithm ). 
jeffro256: Howdy
jeffro256: me: polishing Carrot document and waiting on auditors to send quotes 
Rucknium: me: The new stressnet successfully hard forked from testnet on Saturday. I am reading papers and analyzing ideas to make the tx propagation protocol more efficient and keep good privacy. I read the new Hammad & Victor (2024). "Monero traceability heuristics: Wallet application bugs and the Mordinal-p2pool perspective." Does anyone mind if we add this paper as the last agenda item for today? Or do we need more time to digest it?
jberman: me: shooting to get the draft WIP PR for the fcmp++ integration out today. It builds smoothly on all CI builds now
jeffro256: huge
Rucknium: jberman: Thanks! Are performance benchmarks planned? (Maybe they are already in the draft PR)
jberman: planned, I haven't implemented multithreading yet, which actually should be fairly straightforward and should be a significant boost
jeffro256: multi-threaded verification?
jberman: multi-threaded tree building, verification integration isn't implemented yet
jberman: with the current impl that builds the tree on sync, it took me about twice as long to sync the chain from scratch. The migration was faster than syncing from scratch with a current version. Multithreaded tree building should materially speed up those times
Rucknium: 3) Stress testing monerod https://github.com/monero-project/monero/issues/9348
Rucknium: spackle wrote a report about what happened in the first two months: https://reddit.com/r/Monero/comments/1eoana8/the_stressnet_so_far/
Rucknium: Stressnet node operators seemed to see more alt blocks and re-orgs after jeffro256 's PR #9135 (blockchain sync: reduce disk writes from 2 to 1 per tx)  was merged. I plotted the alt blocks data from the monitor node and there wasn't a relationship between the number of alt blocks and the node release that had that PR.
Rucknium: Anything more on stressnet? We can move on
Rucknium: 4) Potential measures against a black marble attack. https://github.com/monero-project/research-lab/issues/119
Rucknium: The new paper analyzes Mordinals and P2Pool coinbase outputs that can act like black marbles.  Hammad & Victor (2024). "Monero traceability heuristics: Wallet application bugs and the Mordinal-p2pool perspective" https://arxiv.org/abs/2408.05332
Rucknium: "However, as a result of the spike in the number of coinbase outputs that was caused by P2Pool, most coinbase ring members are actually decoys, which means the heuristic is correct more often than not. Monero already has a proposal to avoid selecting coinbase outputs as decoys" footnote: https://github.com/monero-project/research-lab/issues/109
jeffro256: That's a pretty decent read for anyone interesting in tracing 
jeffro256: They calculate overlap/"collisions" of different heuristics and it's pretty low, which points to good effectiveness 
Rucknium: They estimated a false positive rate by comparing the techniques to each other. Moser et al. (2018) did a similar thing with zero-decoy rings and their guess-newest heuristic.
Rucknium: A lot of blockchain surveillance firms do not try to estimate false positive rates. These authors are doing better on that.
jeffro256: Since fcmp++ integration is apparently fast approaching, I might finally be able to retire https://github.com/monero-project/monero/pull/8815
r​brunner7: Totally forgot that you even implemented this ...
Rucknium: The authors know that their estimate of the accuracy of the "10 Block Decoy Bug" is too high but they don't have a good way to get a better estimate. They use the standard wallet2 behavior as the benchmark, but if there are nonstandard wallets that did not have a bug, they would be overestimating the accuracy.
r​brunner7: So that paper is solid work, and a good overview, but nothing really suprising?
Rucknium: "The [10 Block Decoy Bug] heuristic identifies 1, 365, 175 spent outputs". I didn't try to estimate this ex-post since I didn't think it was a good use of research time for a bug that had been squashed already. We get this estimate for free.
jeffro256: I think the novel thing about that paper is an analysis of putting all those separate heuristics together 
Rucknium: IMHO, the paper uses a lot of techniques that MRL-affiliated researchers already knew about. Their contribution is to get precise estimates for some of them and then combine the results.
r​brunner7: I see. Interesting.
Rucknium: "10 Block Decoy Bug": discovers by moneromoo, fixed by jeffro256. Mordinal/P2Pool: widely-known problem, analyzed by me. "Differ-by-One" discovered by isthmus (it's behavior from a nonstandard wallet that cannot be fixed remotely).
jeffro256: I didn't fix it, just wrote the report 
jberman: also koe discovered that one
Rucknium: oh. Got it.
jeffro256: I think moneromooo had a PR open for something unrelated, and koe noticed the inconsistency while reviewing 
jeffro256: Trying to find the PR #
jberman: https://github.com/monero-project/monero/pull/8794#issuecomment-1478116268
Rucknium: 5) Research Pre-Seraphis Full-Chain Membership Proofs. https://www.getmonero.org/2024/04/27/fcmps.html
Rucknium: I collected the security proofs and reviews of FCMP into a subcategory on moneroresearch.info: https://moneroresearch.info/index.php?action=list_LISTSOMERESOURCES_CORE&method=subcategoryProcess&id=1&catId=1
Rucknium: Tell me if anything is missing
Rucknium: From the homepage you can get to this page by Search -> Category Tree -> Monero-Focused Subcategories -> " Full-Chain Membership Proofs"
Rucknium: plowsof and I have decided that we will try to update the website to the latest version on WINIDX by the end of the month. It has some improvements to QuickSearch that I requested.
r​brunner: A quite surprising number of categories :)
jeffro256: Wasn't there a markdown document for the original specification of GBPs by the Curve Tree authors?
Rucknium: rbrunner: The long lists are keywords.
r​brunner: Ah, ok
Rucknium: And they keywords almost all come from the original bibtex entries of the papers.
jeffro256: This quick summary of the protocol might be nice to have in that folder: https://repo.getmonero.org/-/project/54/uploads/a9baa50c38c6312efc0fea5c6a188bb9/gbp.pdf
jeffro256: The GBP security proof paper also describes the protocol, but this is a bit easier to digest idk
Rucknium: Open invitation to anyone who wants to add more papers to moneroresearch.info . If you have an account, you can use it. If you don't have an account, I can add one for you.
Rucknium: Any more on FCMP++?
jeffro256: Just want to invite anyone to give feedback on https://github.com/jeffro256/carrot/blob/master/release/carrot_0.1.md
jberman: nothing from me, thanks for setting up this collection Rucknium 
jeffro256: Yes ^
Rucknium: We can end the meeting here. Thanks everyone.
ArticMine: Thanks for hosting 
m​oneromooo: I indeed did not discover that problem. In fact, I am pretty surprised it makes a usable difference for rings not using a member right at the 10 block limit.
jberman: WIP fcmp++ integration: https://github.com/monero-project/monero/pull/9436
kayabanerve: jeffro256: Why are you versioning by file name *in a Git repository*?
kayabanerve: If the answer is to avoid using GitHub's tag/release system, git has a native tag system usable for releases
kayabanerve: So there is no good answer :C
jeffro256: Lol the idea was so that all releases were easily available in one folder for n00bs 
jeffro256: But github tags does kinda make it irrelevant
jeffro256: As long as github doesn't go down .....
kayabanerve: *git tags also exist, you don't have to use github's*
kayabanerve: Heard re: n00bs but are we expecting a need to refer to historical versions? Isn't this just an rc before finality? 
jeffro256: Yeah this is true 
jeffro256: Updated 


# Action History
- Created by: Rucknium | 2024-08-13T20:51:57+00:00
- Closed at: 2024-08-26T20:22:48+00:00
