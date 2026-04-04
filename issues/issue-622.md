---
title: Monero Research Lab Meeting - Wed 27 October 2021 @ 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/622
author: carrington1859
assignees: []
labels: []
created_at: '2021-10-21T09:51:29+00:00'
updated_at: '2021-10-27T18:33:26+00:00'
type: issue
status: closed
closed_at: '2021-10-27T18:33:26+00:00'
---

# Original Description
https://forum.monero.space/d/152-monero-research-lab-meeting-wed-27-october-2021-at-1700-utc

Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time:
17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Further analysis of July-Aug 2021 tx volume anomaly ( Isthmus / Mitchellpkt - see [these meeting logs](https://github.com/monero-project/meta/issues/621#issuecomment-948953655)) [Previous analysis](https://mitchellpkt.medium.com/fingerprinting-a-flood-forensic-statistical-analysis-of-the-mid-2021-monero-transaction-volume-a19cbf41ce60) with [Reddit discussion](https://www.reddit.com/r/Monero/comments/pvm634/fingerprinting_a_flood_forensic_statistical/)

3. Improvements to the mixin selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [JBerman's weekly updates](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/249#note_11480), [Binning PoC](https://github.com/monero-project/research-lab/issues/88)) @j-berman @Rucknium

4. Seraphis/Triptych/Lelantus Spark ( [UkoeHB's Seraphis Proof of Concept work](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/256), [Seraphis repo](https://github.com/UkoeHB/Seraphis), [Lelantus Spark](https://eprint.iacr.org/2021/1173) & [Tripych Multisig](https://github.com/cypherstack/triptych-multisig/blob/main/main.pdf) )

5. Rucknium's OSPEAD discussion ([CCS proposal](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/255) , Reddit discussion [1](https://www.reddit.com/r/Monero/comments/py8ub3/ccs_proposal_ospead_fortifying_monero_against/) & [2](https://www.reddit.com/r/Monero/comments/pyopq0/the_mathematical_nonsense_of_a_possible/)

6. MRL META: Active recruitment of technical talent, MRL structure (@Rucknium & others) [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

7. Examine sample size and random seed matters in Monero's unit tests. IRC discussion: [monero-dev](https://libera.monerologs.net/monero-dev/20211018#c39593) , [monero-research-lab](https://libera.monerologs.net/monero-research-lab/20211018)
8. Multisig Drijvers attack mitigation [Technical note](https://github.com/UkoeHB/drijvers-multisig-tech-note) , [Haveno bounty](https://github.com/haveno-dex/haveno/issues/103)
9. Any other business
10. Confirm next meeting agenda

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs: 

https://forum.monero.space/d/144-monero-research-lab-meeting-wed-20-october-2021-at-1700-utc/2

https://github.com/monero-project/meta/issues/621

# Discussion History
## carrington1859 | 2021-10-27T18:22:25+00:00
17:00:14 {UkoeHB> meeting time ( https://github.com/monero-project/meta/issues/622 )
17:00:14 {UkoeHB> 1. greetings
17:00:14 {UkoeHB> hello
17:00:35 {isthmus> Salutations
17:00:38 {monerobull[m]> Hello
17:00:46 {Rucknium[m]> Hi
17:01:12 {gingeropolous> hi
17:01:29 {carrington[m]> Hi everyone! It looks like MRL meeting time
17:01:53 {carrington[m]> https://github.com/monero-project/meta/issues/622
17:01:54 {jberman[m]> hello :)
17:01:54 {carrington[m]> Please see suggested agenda items & useful links in the github issue
17:02:15 {carrington[m]> If Koe is not around I can work through the agenda items
17:02:16 {monerobull[m]> This concludes the greetings, moving to point 1 on the agenda "Further analysis of July-Aug 2021 tx volume anomaly "
17:02:19 {UkoeHB> is the matrix bridge broken?
17:02:19 {carrington[m]> 1. Greetings
17:02:39 {monerobull[m]> monerobull[m]: just kidding lmao
17:02:46 {carrington[m]> You are coming through clear koe
17:03:00 {UkoeHB> carrington[m]: you didn't see my messages 2 mins ago
17:03:21 {x3nu[m]> The matrix bridge is acting wonky 
17:03:24 {gingeropolous> ive noticed matrix bridge is intermittently dropping things
17:03:29 {Rucknium[m]> From observations it seems like the IRC --> Matrix bridges sometimes needs to wake up from sleep or something. Your first message, koe, didn't come through to the Matrix side
17:03:35 {carrington[m]> Ah no those didn't come through. I see them on monerologs site though
17:03:42 {UkoeHB> sigh
17:04:04 {carrington[m]> I will keep an eye there and let people know if messages drop
17:04:04 {UkoeHB> anyway, I think the first item today is isthmus wanted to discuss an idea he had
17:04:18 {isthmus> :wave
17:04:28 {isthmus> Lemme pull over some notes from logs
17:04:32 {isthmus> I’ve been continuing to dig into the July 2021 txn flood. The anomaly has been a fantastic case study for ring signature deanonymization due to high volume and extreme transaction homogeneity.
17:04:32 {isthmus> Since doing recursive searches over ring signatures is grossly inefficient, i.e. O(R^H) for ring size R and number of hops H, I’ve been working on efficient encodings for analyses in O(# Txns) by working from genesis to head (which is presumably how any adversary with basic CS skills would approach it)
17:04:32 {isthmus> The data features may take a few days or weeks to build, but you only need to do it once, and then you can read in basically O(1).
17:04:32 {isthmus> One cool application is marking all of the outputs upstream of a given ring signature, which you can think of like an N-1 length bitstring attached to the Nth output, where a 1 at the jth index indicates that output J was a parent of output N.
17:04:32 {isthmus> (You can also imagine this as a triangular matrix with ((# outputs)^2)/2 nonzero entries)
17:04:34 {Rucknium[m]> I think the bridge has been woken up :eyes:
17:05:08 {isthmus> oops I just got booted
17:05:33 {isthmus> It’s a windowable method, for example our first application is identifying which (pre-flood) outputs were used to set up the transaction volume excess this summer. Since we can narrow our focus to a few months leading up to the anomaly, each tag is only a few kB, so we don’t need much computational power or disk space to pull it off.
17:05:33 {isthmus> It’s also surprisingly viable to apply this to the entire blockchain if you have a bit of patience for the first build. Back of the envelope estimation is that all edges in the Monero transaction tree could be naively encoded into this matrix / bitstring formalization in just over 100 TB
17:05:33 {isthmus> (which is very small from a big data industry perspective, where good data engineers are expected to sling around PB’s of dataefficiently.)
17:05:33 {isthmus> There are methods for encoding this more efficiency ( e.g. succinct posets: https://arxiv.org/abs/1204.1957 ), but honestly since the naively encoded data set is only ~100 TB it probably wouldn’t be worth the effort of implementing all the fancy math.
17:05:33 {isthmus> With the data in this shape, output recombination analysis becomes trivial, so we’ll be able to answer conclusively whether the transactions in the anomaly had two >0 outputs (amount + change) or only one valued output and one dummy (0-value) output.
17:05:33 {isthmus> The reason it becomes so simple is this: the way that we built the matrix means that it’s already sorted (both in terms of rows and columns). So now we can test hypotheses extremely quickly by slicing out columns then simply working top to bottom until you encounter the first [1,1]
17:05:47 {isthmus> For example, if a transaction created the xth and x+1th outputs, we 1) simply pull out xth and x+1th columns, then 2) throw out all the 0s before the xth index, then 3) only search as far as we need to to find the first [1,1].
17:05:47 {isthmus> It’s extremely efficient, which is pretty cool, and it doesn’t matter if there are 3 or 30 or 300 hops between when the second output gets folded in downstream of the first one.
17:05:47 {isthmus> For a given output, let delta be the height difference between output creation and the first recombination, with delta(x,x+1)=inf (or nan) if never recombined. The interesting thing is not how often recombinations occur, but how quickly.
17:05:47 {isthmus> There will always be spurious recombinations due to decoy selection, but when we look at the distribution of deltas, the baseline distribution (in a sense, the control case) will have a longer expectation value than what we observe during the anomaly if both outputs were valued.
17:05:47 {isthmus> It’ll take some time to code up the tags and build the data features, but I expect that our next report(s) on the flood will be able to deanonymize most of the ring signatures, conclusively answer whether the anomaly was producing dummy outputs or change outputs, and hopefully identify which transactions before the anomaly created the thousands of ‘mise en place’ outputs that were consumed when it began).
17:06:02 {isthmus> In terms of guessing true spends, we actually have 3 heuristics to combine:
17:06:02 {isthmus> 1) timing, usually 10-15 blocks old
17:06:02 {isthmus> 2) only interested in ring members that have the same fingerprint: 2 outputs, unlock_time = 0, fee matching core wallet, tx_extra length 44 bytes, etc
17:06:02 {isthmus> 3) above linking analysis
17:06:02 {isthmus> Oh and 4) throw out fresh off the coinbase
17:06:03 {isthmus> I think that even without #3 the other heuristics will knock it down to 1-2 plausible members per ring
17:06:05 {ErCiccione> hello, a bit late
17:06:12 {isthmus> Note also that even for normal wallets without recombination, #2 and #4 apply to change output chains
17:06:12 {isthmus> I was thinking that for analyzing the volume anomaly, we can probably just look at the ~500,000 inputs leading up to the start of the excess volume
17:06:12 {isthmus> (a few weeks)
17:06:12 {isthmus> That leaves us with few kB scale tags which will be easy to manipulate without much memory or computational power
17:06:12 {isthmus> And if we don't find the origin outputs in that window, we can just rerun it another 500k indices further back
17:06:15 * isthmus ends ramble
17:07:27 {carrington[m]> This analysis method seems powerful. Do you anticipate that chain analysis companies will already have been using something similar? Or does it lose most usefulness when we don't have homogeneous transactions and all the heuristics?
17:07:51 {isthmus> Probably and yes
17:08:23 {isthmus> Well, it's more useful in some situations than others. It'd also be a fast way to check EABE attacks (if you're eve) but there would be faster ways to look at small subgraphs
17:08:34 {carrington[m]> For example, if you collude with an exchange which holds many outputs. If that is the case I think we need to develop some mitigation strategies
17:08:57 {Rucknium[m]> isthmus: Should we also consider deploying my statistical attack on top of those 3? We probably wouldn't want to include results from that in what we publish, but it could be interesting.
17:09:44 {isthmus> Yea could be a validation method, albeit under limited circumstances (high volume and homogeneity)
17:11:03 {isthmus> I have to say, this transaction volume anomaly has been such a gift for trying out a bunch of analyses and visualizations where they can gain more traction than usual
17:11:55 {carrington[m]> Almost as if that was their intention 😟
17:12:24 {UkoeHB> are we guinea pigs in an alien experiment? :p
17:12:41 {isthmus> @UkoeHB I assume this to be the case
17:12:41 {Rucknium[m]> isthmus: So in a way if this was a genuine attack attempt, it may have backfired, as it may have increased our MRL technical capabilities 🤔
17:13:17 {isthmus> LOL yea I've probably gotten as much novel analysis out of this as they did 
17:13:23 {isthmus> Anywho that's the update from me. It's all pen and paper right now but will hopefully move  towards implementation in upcoming weeks/months
17:13:24 {monerobull[m]> carrington[m]: probably was one of you guys anyways /s
17:14:03 {carrington[m]> I'd be really interested to know what impact even simple binning would have on this technique
17:14:29 {UkoeHB> Cool thanks isthmus. Hopefully within the next couple hardforks we can reduce the range of fingerprintability.
17:14:37 {carrington[m]> Because the "delta" would always have multiple links simultaneously
17:14:55 {Rucknium[m]> isthmus: Do we plan to employ gingeropolous  's up-and-coming research computing server? Also, I think it would be good to fund that server via CCS
17:15:26 {UkoeHB> Next, let's revisit the 16-ring member recommendation from last meeting. There were a couple comments on the github issue (starting here: https://github.com/monero-project/research-lab/issues/79#issuecomment-948198584).
17:15:36 {UkoeHB> Anyone have anything they want to say about this?
17:16:43 {ErCiccione> 16 is fine. I personally prefer to keep it as low as possible tho. Weight is in the blockchain forever and all that
17:16:49 {monerobull[m]> general community supports 16 rings
17:17:47 {gingeropolous> i think it would be informative if we could dig up the reasons ringsize 11 was selected, as noted in that comment
17:18:07 {isthmus> @Rucknium[m] that could be great - will chat with you / ginger / neptune offline about this (neptune handles most DB dev and ops)
17:18:27 {isthmus> Seems like 16 has broad support, I propose we call it there 
17:18:42 {ErCiccione> did we get an input from core about it?
17:19:32 {monerobull[m]> on the topic of binning, nearly everyone supports deprecating timelock https://www.reddit.com/r/Monero/comments/q0oiln/proposal_to_remove_timelock_feature/?utm_source=share&utm_medium=web2x&context=3
17:20:44 {isthmus> Yes please 
17:21:08 {UkoeHB> are there alternative timelock schemes worth thinking about?
17:21:14 {Rucknium[m]> erciccione[m]: IIRC in the most recent dev meeting, UkoeHB brought up 16 and then agreed to take it to MRL for input. That input was given last MRL meeting.
17:21:21 {UkoeHB> e.g. the bitcoin one seems pretty popular
17:21:39 {Rucknium[m]> -dev is not Core, of course, but that's some info ^
17:22:28 {ErCiccione> > {@rucknium[m]:libera.chat> > {@erciccione[m]:libera.chat> did we get an input from core about it?
17:22:28 {ErCiccione> > 
17:22:28 {ErCiccione> > IIRC in the most recent dev meeting, UkoeHB brought up 16 and then agreed to take it to MRL for input. That input was given last MRL meeting.
17:22:28 {ErCiccione> i know, i was asking if anybody from core commented publicly about it, just to make sure you are onboard
17:23:07 {carrington[m]> Articmine wanted it higher in the GH issue, but I can see no other comments from core members
17:23:07 {ErCiccione> but there has been an open issue for some time i'm assuming they wrote something there. I don't recall at the moment
17:23:37 {ErCiccione> ah ok. Then maybe getting an input from them wouldn't be bad
17:23:47 {carrington[m]> The btc version of time locks is certainly more useful
17:24:14 {isthmus> But comes with the same privacy concessions as our current timelock, right?
17:24:18 {isthmus> Plaintext, fingerprintable, tec
17:24:22 {isthmus> s/tec/etc
17:24:27 {jberman[m]> UkoeHB: IIUC, to get the bitcoin version requires a way to have refundable tx's, which the research into DLSAG explored: https://eprint.iacr.org/2019/595.pdf
17:24:39 {isthmus> `{monerobux>` isthmus meant to say: "Plaintext, fingerprintable, etc"
17:25:47 {gingeropolous> bitcoin-style, as in "don't mine into block until blockheight x" ?
17:25:50 {carrington[m]> Unless encrypted, which has scalability drawbacks
17:26:24 {Rucknium[m]> ErCiccione: Check this meeting log for some statements from Core members about ring size:
17:26:24 {Rucknium[m]> https://github.com/monero-project/meta/issues/614
17:26:38 {jberman[m]> I was thinking bitcoin style = HTLC's, which essentially allow a recipient to claim an output as theirs before a certain time, and if they do not, the output is refunded to the sender, which seems to require a larger structural change to the tx protocol to support in Monero
17:27:33 {ErCiccione> > {@rucknium:monero.social> ErCiccione: Check this meeting log for some statements from Core members about ring size:
17:27:33 {ErCiccione> > https://github.com/monero-project/meta/issues/614
17:27:33 {ErCiccione> Thanks for the link. It's enough for me to know they are onboard with 16
17:27:45 {monerobull[m]> i dont think discussing this productive at this point, what would happen to timelocked transactions after a fork changing addresses?
17:27:59 {monerobull[m]> * discussing this is productive at
17:28:39 {UkoeHB> monerobull[m]: nothing. All old outputs need ‘transition’ tx to spend them, which is a tx type that must be supported indefinitely.
17:29:25 {UkoeHB> DLSAG might be worth revisiting in the context of seraphis
17:29:33 {isthmus> 🤔
17:29:51 {isthmus> Is that the one that has hidden colored coin support?
17:29:59 {carrington[m]> IMO timelock features can wait for some post-bigring hardfork, unless there is a technical reason to decide earlier
17:30:23 {jberman[m]> isthmus: It's a building block for bidirectional atomic swaps + payment channels
17:30:38 {UkoeHB> carrington[m]: well if it is easy to implement, might be worth considering
17:31:07 {UkoeHB> jberman[m]: afaik bidirectional swaps just needs tx chaining; payment channels need the timelock thing
17:32:28 {carrington[m]> tx chaining is part of present seraphis, yes?
17:32:34 {carrington[m]> Serpahis plans*
17:32:37 {UkoeHB> one variant yes
17:32:39 {monerobull[m]> indeed
17:34:01 {UkoeHB> anyway, we can move on; anyone have something to discuss? maybe from the agenda
17:34:04 {carrington[m]> Well if DLSAG and Seraphis can easily be smooshed together then that would be lovely. I seem to remember some sort of big drawback with DLSAG from ancient MRL logs though, can't remember what
17:35:04 {nioc> doubletxs?
17:35:19 {Rucknium[m]> Decoy Selection Algorithm is next on the agenda. I have updates. jberman, do you have updates?
17:35:44 {carrington[m]> Nah double txns was lelantus I think
17:36:22 {jberman[m]> This past week I hardened flaky decoy selection algo unit tests (PR 8024) + finished up working on restructuring the wallet-side binning algo to account for the flaw mentioned in MRL issue 86
17:36:30 {jberman[m]> An update to MRL issue 86 is coming, hopefully today
17:36:48 {jberman[m]> The gist of the change is that bins span a fixed number of blocks, instead of a fixed number of outputs
17:37:34 {jberman[m]> In order to avoid an edge circumstance where one can deduce an output in a ring must actually be a decoy 
17:38:39 {one-horse-wagon[> Spanning a fixed number of blocks is a terrific idea.
17:38:58 {Rucknium[m]> jberman[m]: Will your update to MRL 86 explain how such an edge case could occur?
17:39:07 {UkoeHB> Are you requiring the bin width (in blocks) to be >= the bin size (so if they are all empty, miner tx will be the bin members)?
17:39:21 {jberman> It's way easier to reason through and the algo is much simpler this way
17:40:11 {jberman[m]> Rucknium[m]: This comment explains the edge case in full: https://github.com/monero-project/research-lab/issues/88#issuecomment-947481223
17:40:37 {jberman[m]> Also apologies, I meant MRL issue 88, not 86
17:41:10 {jberman[m]> UkoeHB: This is something I've been thinking about
17:41:39 {UkoeHB> Is it possible to make a miner tx without any outputs? moneromooo 
17:42:53 {jberman[m]> I can double check that later if we don't get an answer
17:43:11 {UkoeHB> ok, just a small detail
17:43:46 {UkoeHB> thanks for picking up the ball on binning jberman[m] :)
17:44:04 {carrington[m]> Looking forward to the binning update, I think I have managed to grokk issue 88 so far
17:44:07 {isthmus> Yea tyty
17:44:24 {jberman[m]> But in any case, I've been debating including a bin width (in blocks) to be relatively small, potentially allowing even smaller than bin size. I'm not sure what the ideal parameter choice is there. The smaller the bin width, you protect against a certain circumstance where users may be spending outputs extremely close. The wider the bin width, the fewer issues there may be in the implementation
17:46:08 {carrington[m]> Surely the best protection against spending close outputs is to increase the "bin members"?
17:47:33 {carrington[m]> I.e. if we eventually have bins with 10 decoys each with seraphis the problem is basically negligible
17:47:40 {jberman[m]> definitely, but assuming we have limited number of ring members to work with, not so trivial to do
17:47:57 {Rucknium[m]> My main update is that ArticMine has examined my HackerOne submission, which included a rough outline to develop OSPEAD. He gave me some feedback. I believe that he will say something about it publicly soon.
17:48:31 {Rucknium[m]> In the next day or two I will start a, uh, viral marketing campaign for OSPEAD 😂
17:49:05 {Rucknium[m]> The main component is an animated gif of the Monero logo that illustrates statistics...
17:49:54 {Rucknium[m]> And then I may release a version of "Document A", which is a fairly precise mathematical definition of a key component of OSPEAD. So the community can see what I intend to do.
17:50:05 {carrington[m]> I have seen this logo and I can confirm it is the bees knees. Looking forward to digging into the HO report and OSPEAD when released
17:50:29 {Rucknium[m]> Then hopefully community consensus will be attained and my CCS proposal can go to "needs funding".
17:50:56 {Rucknium[m]> That is my update. Questions?
17:51:50 {isthmus> Ah I meant to review the CCS proposal closer and leave a comment, will do that in the next 24h
17:51:52 {carrington[m]> Honestly if you have not received any negative feedback I don't see why not move it to funding right away. If in the intermediate time it is determined that OSPEAD is flawed, the funds would just go back to the general fund in the end
17:52:54 {one-horse-wagon[> I'd rather wait to see what we're buying first.
17:53:17 {Rucknium[m]> I think that the main negative feedback is that my suggestion that part of OSPEAD should not be made public was quite controversial. That's not going to be a Rucknium-level decision, however. It is somewhat besides the point when it comes to whether the research should be funded, I think.
17:54:41 {Rucknium[m]> one-horse-wagon[: So you want to see Document A first? That would be fine. isthmus, jberman, ArticMine, Syksy, and mj-xmr have seem it so far. I will get a version ready for release in the next 4-5 days or so.
17:55:00 {Rucknium[m]> * have seen it_
17:55:22 {isthmus> I'm fine with it being shared, fwiw. I'd bet that at least one chain analysis company has figured this out already, and the rest will be able to connect the dots with how the solution is approached. So confidentiality might be hindering us more than them.
17:56:46 {Rucknium[m]> isthmus: What is "it" in you statement? Not that I disagree.
17:56:56 {Rucknium[m]> * your
17:57:34 {Rucknium[m]> ArticMine has his own views on disclosure.
17:57:49 {isthmus> The concepts / ideas in general, wasn't referring to any particular document
17:57:52 {carrington[m]> Well I guess we await this Doc A. I have a question on seraphis before we finish up here. Does this "supercop" stuff fall within the scope of the seraphis PoC? Seems it sped up CLSAG a lot, although I can't say I really understand how it works or relates to seraphis
17:58:58 {Rucknium[m]> one-horse-wagon: Could you answer my question above ^ ?
17:59:10 {UkoeHB> carrington[m]: it is not in-scope. Supercop is optimized crypto libraries, which can be implemented at a later date if appropriate.
17:59:20 {isthmus> Could you remind me what supercop stuff is?
17:59:31 {isthmus> ohh optimized crypto libraries
17:59:31 {isthmus> nvm
18:00:56 {carrington[m]> Ty. So all seraphis timing estimates should have a footnote that there are significant crypto optimizations not being accounted for
18:01:08 {UkoeHB> hmm I suppose so
18:01:39 {UkoeHB> afaict CLSAG is not using supercop, maybe someone can correct me
18:01:41 {jberman[m]> Refresher on the view tag: basically it's a 1-byte addition to tx's that would speed up scanning by 50-70%, and just needs someone to implement, ya?
18:02:02 {jberman[m]> 1 byte addition per output*
18:02:03 {one-horse-wagon[> Rucknium. What question are you talking about?
18:03:07 {Rucknium[m]> {Rucknium[m]> "So you want to see Document A..." {- ^ This one. What standard would I have to meet, according to your standard, for "see[ing] what we're buying first"?
18:03:37 {nioc> {jberman[m]> The smaller the bin width, you protect against a certain circumstance where users may be spending outputs extremely close. {{>> spending the outputs from mining on p2pool currently triggers the wallet warning that outputs are close
18:04:50 {carrington[m]> Maybe SGPs suggestion that we have coinbase-only rings should be revisited if p2pool takes off
18:04:54 {Rucknium[m]> "Document A" is explained in the logs here. Just search "Document A". I am terrible at naming things lol
18:04:54 {Rucknium[m]> https://github.com/monero-project/meta/issues/621
18:05:17 {jberman[m]> nioc: yep, it would provide protection in that kind of circumstance
18:05:38 {UkoeHB> jberman[m]: More or less. There is some fiddly logic around tx pub keys, and I'm not sure the best way to actually derive view tags. Using a truncated sender-receiver secret leaks bits of that secret, but using a hash adds ~1-3% to scan times (in my tests).
18:05:45 {jberman[m]> coinbase-only rings also a solid idea I think
18:06:16 {one-horse-wagon[> There are no standards I have in mind.  I would just like to see Document A that's all.
18:06:24 {UkoeHB> Also, max reduction should be only 40%
18:07:33 {Rucknium[m]> one-horse-wagon: Ok great. Yes, I will prepare Document A for public release. This will include removing a few things and making it slightly more understandable for laypeople. I warn that it is a technical document and will remain so, however.
18:08:59 {Rucknium[m]> Also, if isthmus, jberman, or mj-xmr could give me some feedback on Document A before release, that would be good, too. Not necessary, however.
18:09:00 {carrington[m]> Rucknium on the meta agenda item, I seem to remember you mentioning that there was someone interested in doing a CCS for reviewing Monero papers. Am I misremembering, and if not do you think this person will go ahead with that plan?
18:09:21 {one-horse-wagon[> Rucknium.  Very good.
18:09:49 {coinstudent2048[> I'll take a look at Document A, and run if I don't understand it.
18:09:49 {coinstudent2048[> carrington It's me.
18:10:07 {Rucknium[m]> There is no one in particular. I think we should be reviewing Monero papers, it may make sense to have one person be spearheading it, and it's important enough that it should probably be funded.
18:10:19 {jberman[m]> Rucknium[m]: Been meaning to, will do
18:10:27 {Rucknium[m]> Oh, oops, I guess coinstudent2048 was that person.
18:10:56 {isthmus> Yea, I'd love to see a survey of recent literature relevant to ring signature deanonymization. Even just a collection of relevant papers would give me a weekend of fascinating reading.
18:10:57 {Rucknium[m]> jberman: Ok great. Thank you.
18:11:18 {UkoeHB> We are past the hour on the meeting, so I will call it here for the logs. Continue discussing if you wish
18:11:29 {carrington[m]> I think it is a valuable idea! I tried to look through papers with Monero keywords and the volume/variety was quite overwhelming. There has to be at least a few easy wins from those
18:12:01 {coinstudent2048[> carrington: I am not sure though anymore, I fear personal stuff gets creeping in gradually.
18:13:41 {carrington[m]> It is a big task for sure. Maybe a bounty could be created for a bonus payout to whoever takes it on 
18:14:03 {jberman[m]> {UkoeHB> "jberman: More or less. There..." {- sounds like hash is the way just going off this snippet. it's a pretty significant optimization regardless, losing ~1-3% after gaining ~40% doesn't seem so bad, so seems like the safer conservative approach is sensible
18:15:09 {rbrunner> UkoeHB: I think new test runs for the modified/refined multisig PR code are a good idea. I am ready to do them, just let me know somehow when time has come


# Action History
- Created by: carrington1859 | 2021-10-21T09:51:29+00:00
- Closed at: 2021-10-27T18:33:26+00:00
