---
title: Monero Research Lab Meeting - Wed 08 December 2021 @ 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/637
author: Rucknium
assignees: []
labels: []
created_at: '2021-12-06T04:30:11+00:00'
updated_at: '2021-12-14T15:53:19+00:00'
type: issue
status: closed
closed_at: '2021-12-14T15:53:19+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Discuss requirements to get [the multisig PR](https://github.com/monero-project/monero/pull/7877) merged.

3. Adaptive CPU regulation for improved mining performance ( maxwellsdemon )

4. "Seeing a bug in Aeon transactions where multiple inputs in one transaction use the same output. " https://github.com/monero-project/monero/pull/8047

5. Cryptographic performance benchmarks https://github.com/Rucknium/misc-research/tree/main/Monero-Cryptography-Benchmarks

6. Further analysis of July-Aug 2021 tx volume anomaly ( Isthmus / Mitchellpkt - see [these meeting logs](https://github.com/monero-project/meta/issues/621#issuecomment-948953655)) [Previous analysis](https://mitchellpkt.medium.com/fingerprinting-a-flood-forensic-statistical-analysis-of-the-mid-2021-monero-transaction-volume-a19cbf41ce60) with [Reddit discussion](https://www.reddit.com/r/Monero/comments/pvm634/fingerprinting_a_flood_forensic_statistical/)

7. Improvements to the mixin selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [JBerman's weekly updates](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/249#note_11480), [Binning PoC](https://github.com/monero-project/research-lab/issues/88)) @j-berman @Rucknium

8. [The Science of Blockchain Conference 2022 Jan 24-26](https://cbr.stanford.edu/sbc22/#cfp). Submission deadline: November 23, 2021 11:59pm PST

9. Seraphis/Triptych/Lelantus Spark ( [UkoeHB's Seraphis Proof of Concept work](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/256), [Seraphis repo](https://github.com/UkoeHB/Seraphis), [Lelantus Spark](https://eprint.iacr.org/2021/1173) & [Tripych Multisig](https://github.com/cypherstack/triptych-multisig/blob/main/main.pdf) )

10. Rucknium's OSPEAD discussion ([CCS proposal](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/255) , Reddit discussion [1](https://www.reddit.com/r/Monero/comments/py8ub3/ccs_proposal_ospead_fortifying_monero_against/) & [2](https://www.reddit.com/r/Monero/comments/pyopq0/the_mathematical_nonsense_of_a_possible/)

11. MRL META: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

12. Examine sample size and random seed matters in Monero's unit tests. IRC discussion: [monero-dev](https://libera.monerologs.net/monero-dev/20211018#c39593) , [monero-research-lab](https://libera.monerologs.net/monero-research-lab/20211018)

13. Multisig Drijvers attack mitigation [Technical note](https://github.com/UkoeHB/drijvers-multisig-tech-note) , [Haveno bounty](https://github.com/haveno-dex/haveno/issues/103)

14. Any other business

15. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#635  

# Discussion History
## carrington1859 | 2021-12-11T00:06:51+00:00
17:00:09 _UkoeHB> meeting time: https://github.com/monero-project/meta/issues/637
17:00:09 _UkoeHB> 1. greetings
17:00:09 _UkoeHB> hello
17:00:44 _Rucknium[m]> Meeting time! 🤩
17:00:49 _rbrunner> Hi there
17:01:09 _one-horse-wagon[> Hello
17:01:32 _jberman[m]> Howdy
17:04:11 _UkoeHB> 2. updates, what has everyone been up to the past week?
17:04:44 _Halver[m]> Hi
17:05:01 _h4sh3d> Hi
17:05:03 _SerHack> Hi
17:05:13 _UkoeHB> btw andytoshi isn't  DLP security half the number of bits? If you know the DL of your secret key is between [G, 2^128 G], won't your security only be 64 bits?
17:05:23 _rbrunner> Ha, this time I have sometimes. I ran some tests with the latest multisig PR code, as written in the issue. All successful, zero problems.
17:05:30 _rbrunner> *something
17:06:48 _UkoeHB> cool thanks rbrunner; this week I reviewed a multisig patch from wfaressuissia and got to learn all about the wonderful `export_multisig()` and `import_multisig()` functions. I feel your pain...
17:07:24 _jberman[m]> Been more rigorously re-testing "batched" wallet scanning based on UkoeHB's feedback on view tag PR (1 more small commit incoming soon, no significant changes), started reviewing multisig PR (grateful vtnerd is reviewing this, it's fairly challenging for me but I'm getting the gist of the code), started reviewing Rucknium's preliminary OSPEAD work (not much to report on that yet on my end, but looking solid)
17:07:52 _Rucknium[m]> Doing some work on mining revenue, sort of in preparation for tail emission issues. Getting feedback from jberman on my "dry run" of OSPEAD. Have decided for now to use the Akaike Information Criterion (AIC) to compare distribution families when using Maximum Likelihood Estimation (MLE). MLE visualization and results table should be posted in https://github.com/Rucknium/OSPEAD soon.
17:09:09 _Rucknium[m]> However, my Monero work is slowing since I need to pivot back to BCH work. BCH people are asking "What has BCH CashFusion Red Team been up to lately?" The answer is red-teaming Monero ;)
17:09:35 _andytoshi> UkoeHB: great question. i *think* the answer is no
17:10:01 _andytoshi> i think in a 256 bit group, the security is always the minimum of 128 and the entropy of your secret
17:10:24 _andytoshi> but i guess, there is almost certainly some way that you could choose a secret with 128 bits that'd give a boost to pollard-rho..
17:10:38 _andytoshi> i just don't think that "choose from [0, 2^128]" is such a way
17:10:52 _andytoshi> anyway i am not confident. you should not take my word on this :)
17:11:58 _andytoshi> maybe, to be sure, users should just always use 224-bit secrets, which should be fine even if they lose half their bit-security
17:12:00 _UkoeHB> I think baby step giant step would do it if you just generate the keys [0, 2^64] ( https://en.wikipedia.org/wiki/Baby-step_giant-step ).
17:12:16 _UkoeHB> > users should just always use 224-bit secrets
17:12:16 _UkoeHB> yeah I was thinking this as well
17:12:43 _andytoshi> yeah you might be right about baby-step-giant-step. i'll try to work it out
17:13:32 _UkoeHB> 254-bits*
17:14:15 _bbqcore[m]> UkoeHB: hows the seraphis POC work going? i dont see any updates in the ccs
17:15:01 _UkoeHB> thanks for the updates guys
17:15:01 _UkoeHB> 2. discussion, any topics to discuss today? I don't think there are _new_ agenda items. Maybe we can highlight tevador's seraphis address scheme idea ( https://github.com/monero-project/research-lab/issues/92#issuecomment-985018982 ).
17:15:39 _UkoeHB> bbqcore[m]: a couple weeks ago I released performance results https://github.com/monero-project/research-lab/issues/91
17:16:03 _UkoeHB> Right now I am in the 'taking a break' part of the ccs, where design decisions need to be made and I need to finish the paper.
17:16:04 _Rucknium[m]> The only new item was from maxwellsdemon , and they cannot make it to the meeting today.
17:16:24 _UkoeHB> ah
17:17:17 _UkoeHB> wow almost a month since perf results...
17:17:17 _bbqcore[m]> UkoeHB: yeah i remember seeing this now. whats next?
17:20:00 _Rucknium[m]> I want to reiterate now that if anyone want to see the OSPEAD technical specification, i.e. "Document A",  let me know and I can send it to you. I haven't posted it publicly since i want to make a somewhat laypeople-friendly version soon and I don't want two versions floating around out there in public.
17:20:58 _Rucknium[m]> It's important for interpreting https://github.com/Rucknium/OSPEAD   (and even now I am working with jberman on improving the interpretability of the dry run results there)
17:22:29 _rbrunner> "I reviewed a multisig patch from wfaressuissia" Is this public, or still hidden / connected with Hacker One?
17:23:16 _UkoeHB> Ok yeah since that report I mostly took a vacation, worked on reviewing multisig security issues, and added an efficiency section to the paper (with various other updates). Next steps, I need to finish the paper (coinstudent2048[ continues to work on/improve the security model, which is non-trivial), and I am hoping we can hone in on an address scheme and decide which seraphis variant to use. After that, I will fork my 
17:23:16 _UkoeHB> perf branch to clean up the code so I can hand it off to other developers for a potential future hard fork.
17:23:39 _UkoeHB> rbrunner: not public yet... hopefully later this week if wfaressuissia gets back to me
17:23:58 _rbrunner> Holding my breath :)
17:27:17 _rbrunner> There was talk of submitting something to some conference. Did that happen?
17:27:31 _rbrunner> I think the flood analysis, right?
17:27:37 _bbqcore[m]> UkoeHB: i only ask because the ccs proposal said 6 weeks. not rushing you, just curious as to the status and what the next steps are possibly getting seraphis into monero codebase
17:30:47 _UkoeHB> yeah, for design decisions I really need the input of other people at this point... especially people who have read and understood the paper
17:31:27 _dEBRUYNE> Think we should do a meeting dedicated to some design choices for Seraphis that have to be made 
17:31:29 _UkoeHB> Seraphis-Squashed seems promising, but relies on unusual security assumptions.
17:31:40 _Rucknium[m]> rbrunner: Yes, isthmus submitted the "Fingerprinting a Flood" paper to the Science of Blockchain conference.
17:32:37 _rbrunner> Nice!
17:32:37 _UkoeHB> dEBRUYNE: sounds good to me
17:32:37 _Rucknium[m]> I expect that we should hear a reply on acceptance within the next two weeks maybe since the conference happens late January.
17:33:22 _Rucknium[m]> What would an audit process on Seraphis look like? Who might do it and how long do these things typically take?
17:34:11 _UkoeHB> Idk the process, but it would be a very big audit since there are two new proof structures and an entire tx protocol.
17:34:31 _UkoeHB> With a whole new address scheme.
17:35:08 _one-horse-wagon[> Are there any plans to run Seraphis as a testnet first?
17:35:22 _rbrunner> Maybe a look back to the Bulletproof audits will shed some light on this, e.g. https://blog.quarkslab.com/security-audit-of-monero-bulletproofs.html
17:35:30 _UkoeHB> one-horse-wagon[: I would be amazed if it doesn't run on testnet for over a month before use.
17:35:43 _rbrunner> At least 2 different companies reviewed the code, as far as I remember
17:36:01 _rbrunner> With CCS to finance
17:36:29 _rbrunner> Yeah, running on testnet first is a must
17:36:29 _Rucknium[m]> _UkoeHB> "yeah, for design decisions I..." _- What can people like me who don't really understand cryptography do to help with feedback? "Nothing" is a valid answer :)
17:36:59 _UkoeHB> you can look at https://github.com/monero-project/research-lab/issues/92
17:37:17 _rbrunner> Well, some design decisions have UI/UX consequences, and those should be accessible to us non-cryptographers ...
17:38:10 _UkoeHB> Yes, other than address schemes the other UI/UX decision that comes to mind is whether to support collaborative funding or not.
17:38:32 _UkoeHB> And what to do about timelocks...
17:39:56 _rbrunner> Nuke them from orbit, of course
17:40:25 _UkoeHB> And, the best way to implement ring-member-references for large rings (e.g. https://github.com/monero-project/research-lab/issues/84 https://github.com/monero-project/research-lab/issues/88 ).
17:41:41 _rbrunner> This will probably keep us busy the whole 2022
17:41:42 _UkoeHB> rbrunner: I'm wondering if there is an alternative timelock scheme that could be simple but useful. It would be really helpful if the advanced users like atomic swap experts could cleanly describe what would/wouldn't be useful from timelocks.
17:42:24 _rbrunner> Would be interesting to hear, yes
17:44:35 _one-horse-wagon[> Timelocks were talked about a little before.  Few people use them.  I believe the number was about 200.  
17:44:35 _one-horse-wagon[> If you just removed the timelocks, the coins would still be there.  I wouldn't let the issue interfere with the movement toward the adoption of Seraphis.
17:45:58 _one-horse-wagon[> Timelocks are also a possible vector of attack as they stick out on the block chain.
17:46:37 _rbrunner> I think timelocks that are encrypted avoid many of these problems, but are quite costly, if I got that correctly.
17:47:05 _UkoeHB> seraphis is a tx protocol, so it would be nice to have all the tx protocol questions worked out before finalizing the design
17:47:21 _rbrunner> And it looks like atomic swaps really could take off, so users of timelocks could, in theory, be finally there
17:47:39 _UkoeHB> but, it isn't necessary; just bringing up the topic so we can make progress
17:48:12 _jberman[m]> _UkoeHB> "rbrunner: I'm wondering if there..." _- I've gotten some more feedback on that. Thomas from COMIT answered a bunch of q's I had. First off, again, current timelocks are not and wouldn't be useful for atomic swaps. Second, a timelock that prevents an output from being spendable in the chain until height N would be useful and I have to go back through the conversation to get full details on exactly how
17:49:13 _UkoeHB> > a timelock that prevents an output from being spendable in the chain until height N 
17:49:14 _UkoeHB> This is literally the timelocks we have right now.
17:49:50 _rbrunner> Well, now it's all outputs of a tx, maybe that's the difference?
17:50:21 _Rucknium[m]> Maybe it is "tx cannot be mined until block N" That's bitcoin-style time locks, right?
17:50:41 _Lyza> yeah, with btc for example you can *sign* a transaction that can't be mined until N, so the monero lock time on outputs is different
17:51:21 _jberman[m]> I miswrote, that^ is what I meant
17:51:31 _jberman[m]> like the tombstone concept you've mentioned in the past
17:52:00 _UkoeHB> Can you get that effect right now by spending an output that is timelocked?
17:52:49 _jberman[m]> No because it still allows the ability to spend the output with a separate tx
17:53:10 _UkoeHB> you mean the timelocked output?
17:53:23 _UkoeHB> so there s a race condition
17:54:12 _jberman[m]> You could collaboratively sign a tx with another party that can't be included in the chain until time N but spends output X, but before time N are still able to spend output X
17:55:31 _UkoeHB> Can't you do that with bitcoin timelocks as well? I am confused
17:56:17 _jberman[m]> This is Bitcoin's equivalent: https://en.bitcoin.it/wiki/NLockTime
17:57:22 _jberman[m]> You can't do this with Monero's timelocks today because if output X is in the chain and timelocked until time N, no one is able to spend it until time N
17:57:55 _UkoeHB> No, the idea is you make a timelocked dummy output, then spend it in your tx you want locked.
17:58:02 _andytoshi> UkoeHB: yeah, i'm pretty sure baby-step-giant-step will work just fine breaking a DL in a known range (with runtime sqrt(that range)
17:58:16 _andytoshi> thanks!! i will stop casually suggesting that 128 bit secrets are ok
17:58:25 _UkoeHB> sure :)
18:00:35 _UkoeHB> ok we are at the end of the hour, so I will call the meeting here; thanks for attending everyone
18:00:59 _Rucknium[m]> UkoeHB: I think part of the benefit of BTC-style time locks is that one party gives the signed but currently unmineable tx to another party. Then if something goes wrong, Bob can broadcast that timelocked tx to recover funds or something.

# Action History
- Created by: Rucknium | 2021-12-06T04:30:11+00:00
- Closed at: 2021-12-14T15:53:19+00:00
