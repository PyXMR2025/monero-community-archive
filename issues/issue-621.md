---
title: Monero Research Lab Meeting - Wed 20 October 2021 @ 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/621
author: carrington1859
assignees: []
labels: []
created_at: '2021-10-18T20:00:19+00:00'
updated_at: '2021-10-21T19:52:28+00:00'
type: issue
status: closed
closed_at: '2021-10-21T09:49:24+00:00'
---

# Original Description
https://forum.monero.space/d/144-monero-research-lab-meeting-wed-20-october-2021-at-1700-utc

Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time:
17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211020T170000&p1=1440)

Main discussion topics:

1. Greetings

2. How many decoys should be used in the upcoming network upgrades? [Discussion for interim increase](https://github.com/monero-project/research-lab/issues/79), the next generation of transactions are expected to use ringsize>100

3. Triptych/Lelantus Spark/Seraphis ( [Lelantus Spark](https://eprint.iacr.org/2021/1173) , [Seraphis repo](https://github.com/UkoeHB/Seraphis) & [CCS proposal for a PoC](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/256), [Tripych Multisig](https://github.com/cypherstack/triptych-multisig/blob/main/main.pdf) )

4. Rucknium's OSPEAD discussion ([CCS proposal](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/255) , Reddit discussion [1](https://www.reddit.com/r/Monero/comments/py8ub3/ccs_proposal_ospead_fortifying_monero_against/) & [2](https://www.reddit.com/r/Monero/comments/pyopq0/the_mathematical_nonsense_of_a_possible/)

5. MRL META: Active recruitment of technical talent, MRL structure (@Rucknium & others) [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

6. Improvements to the mixin selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [JBerman's weekly updates](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/249#note_11480), [Binning PoC](https://github.com/monero-project/research-lab/issues/88)) @j-berman @Rucknium

7. Examine sample size and random seed matters in Monero's unit tests. IRC discussion: [monero-dev](https://libera.monerologs.net/monero-dev/20211018#c39593) , [monero-research-lab](https://libera.monerologs.net/monero-research-lab/20211018)
8. Multisig Drijvers attack mitigation [Technical note](https://github.com/UkoeHB/drijvers-multisig-tech-note) 
9. Any other business
10. Confirm next meeting agenda

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs: 

https://forum.monero.space/d/139-monero-research-lab-meeting-wed-13-october-2021-at-1700-utc

https://github.com/monero-project/meta/issues/618

# Discussion History
## carrington1859 | 2021-10-20T18:12:42+00:00
17:01:40 _UkoeHB> MRL meeting time (https://github.com/monero-project/meta/issues/621)
17:01:40 _UkoeHB> 1. greetings
17:01:40 _UkoeHB> hi
17:02:00 _isthmus> Salutations
17:02:03 _rbrunner> hello
17:02:10 _jberman[m]> hiya
17:02:11 _Rucknium[m]> Hello
17:02:19 _h4sh3d> Hi
17:02:19 _carrington[m]> I guess I didn't mean completely deterministic. Just that the distribution amongst bins would be deterministic
17:02:26 _carrington[m]> Hello
17:04:56 _SerHack> Hi
17:06:24 _UkoeHB> Today I'd like to nail down ring size for next hard fork, since it is... a blocker for next hard fork. I like 15 (less than 50% rise in input size/verification costs), or 17 (aesthetics: prime number).
17:06:28 _dartian[m]> Salutations 
17:06:35 _UkoeHB> This is agenda item 2.
17:07:01 _carrington[m]> Regarding ringsize increase, I think 16 is the way to go unless binning is implemented in the next upgrade in which case it should be 22
17:07:40 _UkoeHB> Reasoning?
17:07:50 _jberman[m]> In last dev meeting we discussed going with a number that would smooth the binning implementation so no remainder in a bin
17:08:08 _carrington[m]> There was discussion about binning with two outputs from each bin, so 22 gives you a bin for each current output
17:08:22 _jberman[m]> 22 was tossed as ideal since it maintains the current gamma selection + yields the benefit of binning
17:08:27 _carrington[m]> A number with many factors basically was said to be good for binning options
17:08:29 _jberman[m]> when you have 11 bins + 2 members per bin
17:08:48 _UkoeHB> Ok, jberman[m] can you update us on status of binning proposal?
17:09:08 _carrington[m]> I have not yet had time to look over the binning PoC
17:09:09 _Halver[m]> hello
17:09:30 _jberman[m]> I found a flaw yesterday in my proposed wallet-side binning algorithm that is fixable: basically trying to randomly select an output from a block in the final step for each output can cause a situation where an output is guaranteed to be a decoy
17:09:40 _isthmus> Good catch
17:09:44 _jberman[m]> Working on the fix
17:10:35 _jberman[m]> the reason it randomly selects an output from a block in the final step is to mitigate a miner re-ordering a block to their advantage (e.g. ordering a bunch of outputs into a bin)
17:10:55 _carrington[m]> Articmine also stated that if ringsize goes beyond 24 with CLSAG, there would need to be some changes to the dynamic block size system
17:11:42 _Rucknium[m]> From a decision making point of view, isn't it the case that the exact state of the binning PoC isn't too important, as long as we believe that there are not fatal flaws with binning as a concept?
17:12:19 _UkoeHB> Yes that's true, my brain is still warming up on this subject.
17:12:25 _Rucknium[m]> One scenario: We go to an even number of ring size in the next hard fork. Then, later, binning is released in a new wallet release -- it requires no hardfork.
17:13:10 _rbrunner> Log of the dev meeting in question is here, btw: https://github.com/monero-project/meta/issues/614#issuecomment-933010683
17:13:18 _isthmus> There aren't many even primes :/
17:13:29 _gingeropolous> hrm, but doesn't that also get into the whole enforcing of ring member selection thing. 
17:13:36 _gingeropolous> u could end up with wallets that bin and those that don't
17:13:41 _UkoeHB> We have hard from: UkoeHB, carrington[m], jberman[m] about ring sizes. Does anyone else have things they want to say? sgp_ ?
17:13:57 _gingeropolous> ringsize a bajillion
17:14:37 _jberman[m]> A switch to binning in the wallet is guaranteed to cause rings to have a clear different distribution of rings from older rings, so it would be nice to have it in place for a hardfork to try and get as many people as possible using the updated algorithm, though not strictly necessary
17:14:55 _sgp_> hi. nothing changes from me; I still recommend 16-17 absent binning
17:15:21 _Rucknium[m]> gingeropolous: Yes, that would almost 100% happen -- or a least there would be a lag as other wallet implementations adopt it.
17:15:34 _UkoeHB> To be clear: an increase from 11 to 22 ring size will double per-input size/verification costs.
17:15:37 _selsta> 16-17 seems good to me too, I would rather not go too high due to verification time
17:16:15 _Rucknium[m]> My not-completely-thought-out suggestion is ring size 16 since it would allow 2-output bins later.
17:16:37 _rbrunner> Well, if there is a later :)
17:16:49 _wfaressuissia> Hello
17:16:50 _sgp_> with binning would be 8x2, seems reasonably acceptable but a little low
17:16:56 _rbrunner> Or better said, another hardfork between the coming one and Seraphis ...
17:17:22 _carrington[m]> Whether 8 2-ouput bins is better than 4 4-output bins, I'm not so sure
17:18:16 _Rucknium[m]> sgp_: I agree with "seems low". I would want a substantial overhaul of the decoy selection algorithm to be in place before or at the same time as 8x2 binning.
17:18:38 _gingeropolous> i like 22 mainly because its the largest number that seems acceptable at this time, and allows for simple binning that seems acceptable by all
17:18:44 _atomfried[m]> with BP+ how much bigger would a 16-17 ring tx be compared to a current one?
17:19:31 _sgp_> 22 is quite large but indeed has no downside compared to current with binning turned on
17:19:34 _Rucknium[m]> gingeropolous: If 22 is feasible, that would be nice. It seems to be outside of the range that people have typically thrown around, however.
17:20:17 _sgp_> the highest I realistically want to go is 18
17:21:47 _selsta> vtnerd wanted to add ASM speedup for syncing
17:21:50 _gingeropolous> its literally been 3 years since ringsize 11 enforced. tech has advanced since then to accommodate. 
17:21:52 _carrington[m]> Doesn't BP+ lower txn size by a flat 96 bytes?
17:22:03 _selsta> with that added, it might allow for a bit higher ring sizes, depending on the speedup
17:22:41 _sgp_> yeah tech hasn't advanced 100% though :p
17:22:44 _UkoeHB> Let's look at just 16 vs 22.
17:22:44 _UkoeHB> 16: conservative, avoid 2xing size/verification costs per-input
17:22:44 _UkoeHB> 22: optimistic about binning
17:23:17 _gingeropolous> 22: also puts the gas on the pedal for seraphis
17:23:24 _isthmus> (and 22 = more statistical noise to lower the power of heuristic analyses intended to deanonymize ring signatures)
17:23:26 _gingeropolous> wait i messed up that metaphor
17:23:34 _UkoeHB> lol
17:23:38 _isthmus> haha
17:24:08 _jberman[m]> _carrington[m]> "Whether 8 2-ouput bins is better..." _- the Moser paper recommends bin sizes of 2, but need to review the math a bit deeper. their reasoning is basically that bins of size 2 provide mitigation for the worst of any potential problems with pure gamma selection, while still allowing for many gamma-selected outputs in the ring
17:24:38 _UkoeHB> In my view, the pattern/precedent of conservative design choices in Monero favors 16 over 22.
17:24:43 _carrington[m]> So... 18 is the happy medium? Also allows bin sizes of 3
17:24:52 _gingeropolous> ah ha, there's the compromise. 16 now, but include in code that ringsize grows by 2 every year for some n years
17:24:55 _sgp_> just to ground everyone in reality, most of the targeted heuristics don't care about ringsize 11 v 22. It doesn't make those twice as hard
17:25:49 _sgp_> I'm by no means a "small ringsize-r", but going for 22 only makes sense to me if we want to do 11x2 binning
17:25:50 _carrington[m]> Automatic ringsize increase sounds unnecessarily complicated
17:26:12 _gingeropolous> re: sgp, does that include binning bonuses?
17:26:13 _carrington[m]> As presumably the decoy selection would need to change at the same time
17:26:25 _rbrunner> And one would really hope that a next-gen protocols is not several years out
17:27:16 _sgp_> gingeropolous: probably, if you assume 2+ poisioned outputs
17:27:49 _gingeropolous> i just dunno if the heuristics have been done against binning
17:28:56 _UkoeHB> Once again, I feel us going in circles on this subject.
17:29:00 _sgp_> we're getting off topic, but that's not the relevant test at play here for 2+ poisoned outputs
17:29:18 _gingeropolous> yep. im fine with 16,17,22. anything >11 is fine
17:29:36 _rbrunner> The dev meeting participants seemed to grativate towards 16, so ...
17:29:46 _rbrunner> *gravitate
17:29:57 _carrington[m]> Maybe we file this question under "awaiting more binning research"
17:30:03 _sgp_> I'm good with 16
17:30:13 _gingeropolous> nah, one of the goals is to nail down a number
17:30:17 _gingeropolous> no more can kicking
17:30:30 _h4sh3d> seems like no one is against 16 so...
17:30:41 _UkoeHB> Imo if binning were to be enforced by consensus, then the case for 22 would be stronger.
17:31:08 _sgp_> 11 -> 16 is the largest increase ever (not by % obv)
17:31:45 _UkoeHB> Ok how about tentatively 16 ring size for next hf. Any objections? We can revisit this again if anyone wants to before go-live.
17:32:11 _isthmus> 👍
17:32:23 _gingeropolous> ^
17:32:23 _sgp_> no objections
17:32:27 _wfaressuissia> "Once again, I feel us going in circles on this subject." right, especially considering undelivered triptych with 100+
17:32:31 _jberman[m]> none from me
17:32:47 _isthmus> Well, except the fact that it's not prime :- P
17:32:52 _gingeropolous> ^^
17:32:53 * isthmus is superstitious 
17:33:01 _UkoeHB> isthmus: at least it's a power of 2!
17:33:15 _h4sh3d> power of 2 and prime would be good :p
17:33:41 _rbrunner> 16 will probably make also possible nice displays in block explorers and such
17:34:15 _UkoeHB> Let's move on to other agenda items. This part is open-ended.
17:35:22 _rbrunner> I have a question regarding Seraphis that may be of common interest and also came up recently on Reddit:
17:35:22 _UkoeHB> I'll just add my update for the log: yesterday I ran the first performance tests for one design variant of my Seraphis PoC. As expected, it is ~similar in verification cost to Triptych, and smaller size scaling on inputs.
17:36:20 _rbrunner> If I understand correctly Seraphis has the potential to offer better view-only wallets, even in more than 1 variant
17:36:27 _rbrunner> The Seraphis draft whitepaper seems to speak about "design choices" regarding this
17:36:34 _rbrunner> Does this mean we can freely choose among several possibilities, as a community, and the "loose consensus" can get implemented?
17:37:02 _UkoeHB> Yes the consensus can be implemented
17:37:18 _isthmus> Sounds good to me
17:37:27 _UkoeHB> Technically addressing are all 'conventions', not enforced by consensus.
17:37:40 _UkoeHB> addressing schemes*
17:38:18 _rbrunner> Do addresses change in length depending on the choice of the "power" of view-only wallets?
17:38:26 _UkoeHB> Yes
17:38:38 _UkoeHB> Some variants require 3 key addresses
17:39:00 _rbrunner> What must be result in a new record length for all coins :)
17:39:50 _isthmus> I'm intrigued. I think that the limits on our current view key system really lower the practical utility
17:40:24 _h4sh3d> Does 2 key addresses remain compatible?
17:42:24 _UkoeHB> here is a summary of address schemes https://usercontent.irccloud-cdn.com/file/fhZ3XPcM/seraphis_address_schemes_4.png
17:42:35 _UkoeHB> h4sh3d: no there is no variant that remains compatible
17:44:03 _rbrunner> Very interesting. Is that from a text that also explains what a "tier" is?
17:44:34 _UkoeHB> no it's just a summary; I just call a 'tier' a different level of authority
17:44:55 _isthmus> I like Janus A
17:45:36 _rbrunner> Depending on how many private keys one holds?
17:45:44 _isthmus> I like Janus A
17:45:49 _UkoeHB> rbrunner: more or less
17:45:52 _isthmus> oops sorry for the dupe, connectivity issues
17:46:33 _rbrunner> I see
17:46:40 _sgp_> what does Janus mean if it's in the table under a tier?
17:46:48 _UkoeHB> you can check section 4.6.2 in the seraphis draft paper
17:47:00 _UkoeHB> sgp_: you can detect janus attacks with that tier
17:47:16 _isthmus> I think there's value in having view received and view spent separately
17:47:16 _isthmus> In the case of a charity that publishes their view key, it might be better to just share the show received, since it's undesirable to publicly reveal a large number of spends
17:47:16 _isthmus> But for a company running audits on internal wallets, having view spend is desirable
17:48:18 _UkoeHB> isthmus: the problem is you can usually detect spends by looking at change outputs
17:48:32 _rbrunner> "Plain B" looks interesting because it does not yet seem to require a third key
17:48:37 _UkoeHB> so it is of questionable utility to separate the tiers
17:48:59 _UkoeHB> separate the capabilities*
17:49:05 _sgp_> Janus A seems the best then. Janus B would be cool for minimizing info known to lightweight wallets, but not being able to observe Janus is a downside
17:49:18 _UkoeHB> However, if ring size is expanded to 'all the outputs', then the distinction can be useful.
17:49:28 _isthmus> Well, my accounting department isn't going to want to heuristically infer spends from change outputs :- P
17:49:34 _isthmus> But yea, that is a bummer for the charity use case
17:50:18 _sgp_> even so, the distinction is useful from an auditability perspective
17:50:59 _sgp_> using key images to confirm guesses is terrible UX
17:51:01 _isthmus> Yea, with Monero's current setup, the ONLY way for accounting to get a full view of wallet activity is if they have access to sensitive keys
17:51:08 _UkoeHB> To be clear: a tier 2 wallet has all the capabilities of a tier 1 wallet
17:51:23 _isthmus> Whereas with e.g. Janus A, they could have a full dashboard to monitor all wallet activities, without ever needing access to a sensitive key
17:51:25 _isthmus> Which is sweet
17:51:37 _isthmus> (from a secure systems design perspective)
17:51:41 _carrington[m]> Couldn't change outputs be sent to a different subaddress? That way, you couldn't infer the full flow of funds with a "view incoming" key for a specific address
17:52:10 _carrington[m]> Maybe a bit convoluted, and possibly completely wrong
17:52:19 _isthmus> 🤔
17:52:23 _moneromooo> Apologies if this was said, I just popped in, but why does plain B have three distinct tiers with only two keys ?
17:52:25 _UkoeHB> isthmus: you get the same thing with all the other variants except Plain A
17:52:32 _isthmus> Yea
17:52:49 _rbrunner> Aren't keys address-independent?
17:52:53 _isthmus> They're all improvements over Plain A
17:53:21 _UkoeHB> moneromooo: there are actually 3 private keys in Plain B, but only 2 public keys in the address
17:53:34 _rbrunner> Sounds quite clever
17:53:39 _moneromooo> Thanks
17:54:17 _rbrunner> So it seems we can start discussion and let any future hardfork to Seraphis come nearer in a relaxed way because the design can be finalized quite quickly
17:54:38 _UkoeHB> I suppose so
17:54:51 _jberman[m]> "Janus" types wouldn't leave an additional 16 bytes of data on chain, but require larger addresses in order to protect against Janus?
17:55:00 _UkoeHB> jberman[m]: correct
17:55:36 _UkoeHB> Even if you use 16 bytes to mitigate janus, the janus address variants still need 3 keys to get the more versatile permissions
17:55:45 _sgp_> how long we talking
17:56:04 _isthmus> It would be a kind of cool UI feature if I could export / import the view keys as mnemonic word lists
17:56:27 _jberman[m]> got it
17:56:35 _UkoeHB> sgp_: until what?
17:57:13 _sgp_> long in size, 50% longer?
17:57:31 _UkoeHB> yes the Janus variants would be 50% longer
17:58:01 _UkoeHB> One last minute question: is anyone working on Drijvers attack mitigation? wfaressuissia ?
17:58:29 _carrington[m]> Longer addresses are better than more data on chain
17:58:57 _h4sh3d> UkoeHB: I had a look at your technical note. Was surprised to not see reference to MuSig2 work, is it intentional?
17:59:17 _wfaressuissia> yes
17:59:31 _UkoeHB> h4sh3d: I did not read that paper
17:59:45 _UkoeHB> Since I guess the other papers are sufficient
17:59:55 _sgp_> carrington: agree 100%, quite a minor downside
18:00:14 _h4sh3d> worth having a quick look at 1.3 Concurrent Work then, just to get an idea, https://eprint.iacr.org/2020/1261.pdf
18:01:32 _sethsimmons> Users just copy-paste and verify first and last few characters, so longer addresses don't really matter in any way I can think of, and Monero's addresses are already dauntingly long lol
18:01:34 _h4sh3d> yes FROST cover the same
18:03:28 _UkoeHB> wfaressuissia: great thank you! :)
18:03:47 _UkoeHB> Ok we are at the end of the meeting. Let's do another meeting same time next week. Thanks for attending everyone.
18:03:49 _carrington[m]> Worth noting for the logs: Haveno are offering a $2500 bounty for fixing the Wagner/drijvers attack
18:04:17 _isthmus> Productive meeting
18:04:25 _isthmus> I’ve made some progress in a little side project inspired by the transaction volume excess I could share too, but I forgot to add to the agenda
18:05:46 _isthmus> Should I brain dump now or save it for next week's episode? :- P
18:06:21 _carrington[m]> Rucknium  are we any closer to reviewers deciding if your hackerone disclosure should be published? Haven't seen mention in a while
18:08:36 _gingeropolous> i guess u should save it for next week isthmus 
18:08:43 _carrington[m]> Isthmus I can add that to the top of the next agenda, if you give me a title to hype it up.

## carrington1859 | 2021-10-21T19:52:28+00:00
18:16:57 _isthmus> Next week is iffy for me. I'll whip up an abstract now while it's fresh on my mind, and then we can tentatively pencil it in for next week
18:22:46 _isthmus> I’ve been continuing to dig into the July 2021 txn flood. The anomaly has been a fantastic case study for ring signature deanonymization due to high volume and extreme transaction homogeneity.
18:22:53 _isthmus> Since doing recursive searches over ring signatures is grossly inefficient, i.e. O(R^H) for ring size R and number of hops H, I’ve been working on efficient encodings for analyses in O(# Txns) by working from genesis to head (which is presumably how any adversary with basic CS skills would approach it)
18:23:02 _isthmus> The data features may take a few days or weeks to build, but you only need to do it once, and then you can read in basically O(1). 
18:23:09 _isthmus> One cool application is marking all of the outputs upstream of a given ring signature, which you can think of like an N-1 length bitstring attached to the Nth output, where a 1 at the jth index indicates that output J was a parent of output N.
18:23:17 _isthmus> (You can also imagine this as a triangular matrix with ((# outputs)^2)/2 nonzero entries)
18:23:24 _isthmus> It’s a windowable method, for example our first application is identifying which (pre-flood) outputs were used to set up the transaction volume excess this summer. Since we can narrow our focus to a few months leading up to the anomaly, each tag is only a few kB, so we don’t need much computational power or disk space to pull it off.
18:23:41 _isthmus> It’s also surprisingly viable to apply this to the entire blockchain if you have a bit of patience for the first build. Back of the envelope estimation is that all edges in the Monero transaction tree could be naively encoded into this matrix / bitstring formalization in just over 100 TB (which is very small from a big data industry perspective, where good data engineers are expected to sling around PB’s of data 
18:23:41 _isthmus> efficiently.)
18:23:49 _isthmus> There are methods for encoding this more efficiency ( e.g. succinct posets: https://arxiv.org/abs/1204.1957 ), but honestly since the naively encoded data set is only ~100 TB it probably wouldn’t be worth the effort of implementing all the fancy math.
18:24:04 _isthmus> With the data in this shape, output recombination analysis becomes trivial, so we’ll be able to answer conclusively whether the transactions in the anomaly had two >0 outputs (amount + change) or only one valued output and one dummy (0-value) output.
18:24:13 _isthmus> The reason it becomes so simple is this: the way that we built the matrix means that it’s already sorted (both in terms of rows and columns). So now we can test hypotheses extremely quickly by slicing out columns then simply working top to bottom until you encounter the first [1,1]
18:24:21 _isthmus> For example, if a transaction created the xth and x+1th outputs, we 1) simply pull out xth and x+1th columns, then 2) throw out all the 0s before the xth index, then 3) only search as far as we need to to find the first [1,1].
18:24:39 _isthmus> It’s extremely efficient, which is pretty cool, and it doesn’t matter if there are 3 or 30 or 300 hops between when the second output gets folded in downstream of the first one.
18:24:46 _isthmus> For a given output, let delta be the height difference between output creation and the first recombination, with delta(x,x+1)=inf (or nan) if never recombined. The interesting thing is not how often recombinations occur, but how quickly. 
18:24:52 _isthmus> There will always be spurious recombinations due to decoy selection, but when we look at the distribution of deltas, the baseline distribution (in a sense, the control case) will have a longer expectation value than what we observe during the anomaly if both outputs were valued. 
18:25:01 _isthmus> It’ll take some time to code up the tags and build the data features, but I expect that our next report(s) on the flood will be able to deanonymize most of the ring signatures, conclusively answer whether the anomaly was producing dummy outputs or change outputs, and hopefully identify which transactions _before_ the anomaly created the thousands of ‘mise en place’ outputs that were consumed when it began).
18:42:54 _jberman[m]> Checking my understanding: you're starting with suspect outputs created in a set of suspect tx's, then seeing when they're first used in a ring later in the chain. If you find that a large swathe of the suspect outputs are first used in a ring later on much sooner than what one would expect from the decoy selection algorithm, then you can guess those suspect outputs were more likely to be spent in those rings?
18:49:56 _isthmus> Bingo
18:50:22 _isthmus> In terms of guessing true spends, we actually have 3 heuristics to combine:
18:50:28 _isthmus> 1) timing, usually 10-15 blocks old
18:51:31 _isthmus> 2) only interested in ring members that have the same fingerprint: 2 outputs, unlock_time = 0, fee matching core wallet, tx_extra length 44 bytes, etc
18:52:10 _isthmus> 3) above linking analysis
18:52:29 _isthmus> Oh and 4) throw out fresh off the coinbase
18:52:53 _isthmus> I think that even without #3 the other heuristics will knock it down to 1-2 plausible members per ring
18:57:09 _UkoeHB> wfaressuissia: it seems MuSig2 has a marginally more efficient spec for bi-nonce signing compared to FROST/SpeedyMuSig (https://eprint.iacr.org/2020/1261 section 4.1 'Second round signing'); they use a single nonce aggregation coefficient `b` to reduce the cost of combining all nonces (thanks h4sh3d for mentioning this paper)
19:07:09 _isthmus> Note also that even for normal wallets without recombination, #2 and #4 apply to change output chains 
19:14:26 _jberman[m]> Very neat, looking forward to hearing more :) A challenge with applying it in the general case seems to be that you need a large initial set of suspect tx's, and trying to guess at initial sets seems difficult. But if you start with a large set of initial suspect tx's (and expect quick spends), you have a lot to go off of
19:34:53 _isthmus> I was thinking that for analyzing the volume anomaly, we can probably just look at the ~500,000 inputs leading up to the start of the excess volume
19:34:55 _isthmus> (a few weeks)
19:35:19 _isthmus> That leaves us with few kB scale tags which will be easy to manipulate without much memory or computational power
19:36:14 _isthmus> And if we don't find the origin outputs in that window, we can just rerun it another 500k indices further back
19:51:36 _Rucknium[m]> _carrington[m]> "Rucknium  are we any closer to..." _- I am aware that some reviewers have been slowed by unrelated circumstances. 2.5 weeks ago I agreed to not discuss OSPEAD and related issues in detail publicly for the time being since, well, there was quite a bit of controversy.
19:52:46 _Rucknium[m]> However, I think it is reasonable at this point to "break the silence" about some details of where we are in the process, especially since it has been over a month since I submitted to HackerOne.
19:53:33 _Rucknium[m]> Some reviewers have not identified themselves publicly, so some of what I say will be vague.
19:53:50 _Rucknium[m]> Current status on my end of things:
19:55:47 _Rucknium[m]> 1) A biostatistician within the Monero community has written a "review" of my submission. Overall, I feel that it is a very positive review. In essence, it found no fundamental flaws with my attack nor my proposed solution to it, according to my interpretation of the review.
19:56:25 _Rucknium[m]> I caution that the biostatistician specifically stated that his opinion should not be considered a go/no go judgement, however.
20:01:41 _Rucknium[m]> Here's the thing about peer review: Generally an arbiter would have a review and a reply together. I also note that the biostatistician said he reviewed my HackerOne submission as if it were a scientific publication. Reviewing it that way implies a high level of scientific rigor.
20:03:43 _Rucknium[m]> I didn't write my submission in the style of a scientific publication, so I am somewhat uncomfortable sharing the review without my reply, since the context is lacking. I wrote it to be a...HackerOne submission, for the purpose of getting broad feedback from the Vulnerability Response Process team about what could be shared and what cannot in composing my CCS.
20:06:26 _Rucknium[m]> So what has been occupying my Monero time is two activities:
20:06:26 _Rucknium[m]> 1) Writing an extensive reply to one of the biostatistician comments about the description of OSPEAD being too vague to comment on at a technical statistical level. I agree it was vague. I specifically state in my submission at one point:
20:07:07 _Rucknium[m]> "I have the mathematical definitions of these [ideas] worked out in my head, but they are not written here."
20:07:58 _Rucknium[m]> So I wrote out a description in words of a key part of OSPEAD in about 2 pages in my HackerOne submission. This is Section 7 of my submission.
20:10:49 _Rucknium[m]> I have recently written a fairly precise treatment of what I intend to do (in that key part of OSPEAD) as, essentially, a response to the comment about it being vague. It's about 10 pages of fairly technical mathematics. The presentation is much more technical than anything contained within my HackerOne submission. Let's call this Document A.
20:11:42 _Rucknium[m]> I have given Document A to the biostatistician, isthmus, and jberman. However, there are more reviewers who would probably want to see it.
20:13:27 _Rucknium[m]> Importantly, I believe that it may be safe to publicly release a slightly modified version of Document A so as to more clearly explain to the community what I intend to do. The overall thrust of Document A is not sensitive and would, I think, not be useful to a Monero adversary. I am not certain on this point, however.
20:14:47 _Rucknium[m]> Well, I said "what has been occupying my Monero time is two activities", but let's disaggregate further:
20:16:58 _Rucknium[m]> 2) I am finishing a detailed technical critique of Section 6.1 "Fitted Mixin Sampling Distribution" of Moser et al. (2018). This was basically requested in the biostatisticians' review.
20:17:47 _Rucknium[m]> 3) General replies to the biostatistician's other comments. Those replies don't really require any further research work.
20:18:48 _Rucknium[m]> 4) Some new results that extend some parts of my HackerOne submission. These results are useful in judging current risks to user privacy.
20:19:03 _Rucknium[m]> 5) A fifth thing.
20:20:33 _Rucknium[m]> Once I finish with 1-5, which is hopefully be in the next few days, I will send it to all current "reviewers" of my HackerOne submission. At that point, I will halt technical work on the decoy selection algorithm until the funding situation is clearer.
20:21:33 _Rucknium[m]> Yes, 1-5 also includes the original review by the statistician, along with my replies to his comments. In total, it would be about 30 pages I think.
20:23:32 _Rucknium[m]> ^ This presents an unfortunate or maybe interesting possibility that I am producing research faster than it can be reviewed by the people who want to review it, since my original HackerOne submission was 28 pages, and 1-5 will be more technical than my HackerOne submission.
20:24:24 _Rucknium[m]> Most of the work to produce 1-5 was envisioned to have occurred under the plan laid out in my original CCS proposal, so it's not wasted effort or anything.
20:24:40 _Rucknium[m]> carrington:  Ok, done with update :)

# Action History
- Created by: carrington1859 | 2021-10-18T20:00:19+00:00
- Closed at: 2021-10-21T09:49:24+00:00
