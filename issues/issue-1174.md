---
title: Monero Research Lab Meeting - Wed 19 March 2025, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1174
author: Rucknium
assignees: []
labels: []
created_at: '2025-03-18T22:26:03+00:00'
updated_at: '2025-03-28T17:21:22+00:00'
type: issue
status: closed
closed_at: '2025-03-28T17:21:22+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. Maintainers for the [`research-lab` GitHub repo](https://github.com/monero-project/research-lab).

4. [Babb, J., Goodell, B., Parker, L., Salazar, R., Slaughter, F., & Szramowski, L. (2025). "FROSTLASS: Flexible Ring-Oriented Schnorr-like Thresholdized Linkably Anonymous Signature Scheme."](https://github.com/cypherstack/frostlass)

5. [Salazar, R., Slaughter, F., & Szramowski, L. (2025). "Veridise Logarithmic Derivative Review."](https://github.com/cypherstack/divisor_deep_dive)

6. [Prize contest to optimize some FCMP cryptography code](https://github.com/j-berman/fcmp-plus-plus-optimization-competition).

7. [Release of OSPEAD HackerOne and CCS milestone submissions](https://github.com/Rucknium/OSPEAD). Analysis of risk of new decoy selection algorithm without a hard fork.

8. Research on [subnet deduplication for peer selection](https://github.com/Rucknium/misc-research/blob/main/Monero-Peer-Subnet-Deduplication/pdf/monero-peer-subnet-deduplication.pdf) to reduce spy node risk.

9. Any other business

10. Confirm next meeting agenda

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1171 

# Discussion History
## Rucknium | 2025-03-23T14:01:07+00:00
Logs

> __< s​packle:monero.social >__ Hi, I won't make the meeting today but on the topic of a new DSA without a hard fork:     

> __< s​packle:monero.social >__ I believe this has 3 requirements:     

> __< s​packle:monero.social >__ 1. The MAP decoder attack success must be significantly reduced     

> __< s​packle:monero.social >__ 2. A DSA classifier must not be able to distinguish between the new/old distributions with high confidence     

> __< s​packle:monero.social >__ 3. The implementation code changes must be absolutely minimal. A direct update of the values of GAMMA_SHAPE and GAMMA_SCALE is essentially the limit on what is acceptable.     

> __< s​packle:monero.social >__ I believe these requirements can be fulfilled, though I do not know what the specific target numbers should be.      

> __< s​packle:monero.social >__ I did a basic investigation, using tools and guidance generously provided by Rucknium, and saw some encouraging figures. With only a handful of attempts, the best result I got was with shape = 9.168 and rate = 0.8382 reducing the MAP decoder success to 16.4%. For DSA classification my methods got inconsistent results, but they did suggest that the worst of the fungibility defect i<clipped message>     

> __< s​packle:monero.social >__ ssue could be avoided (<90% DSA classification accuracy).     

> __< s​packle:monero.social >__ For clarity, the gamma distribution parameters above should reflect a distribution drawing 2/3 of its data from the status quo, and 1/3 of its data from parameters listed in the OSPEAD documents.     

> __< s​packle:monero.social >__ I hope this approach is promising enough to foster further discussion.     

> __< r​ucknium:monero.social >__ MRL meeting in this room in two hours.     

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1174     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< a​rticmine:monero.social >__ Hi     

> __< j​berman:monero.social >__ *waves*     

> __< rbrunner >__ Hello     

> __< s​yntheticbird:monero.social >__ Hello     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< r​ucknium:monero.social >__ me: I wrote some Rust that sped up the BJR estimator in OSPEAD by 14x : https://github.com/Rucknium/OSPEAD/blob/main/CCS-milestone-2/decoyanalysis/src/rust/src/lib.rs . Last time, it took about two weeks of compute time to process two years of blockchain data, so the new code can probably do it in about a day. I have also been researching the safety of deploying an improved decoy <clipped message     

> __< r​ucknium:monero.social >__ selection algorithm (DSA) without a hard fork.     

> __< j​berman:monero.social >__ me: reviewing PR 9844, CLI/RPC tests for FCMP++ are functioning, working through FCMP++ tasks I had kept on the back-burner (e.g. https://github.com/monero-project/monero/pull/9436#issuecomment-2519858103)     

> __< r​ucknium:monero.social >__ Ping jeffro256  if needed     

> __< r​ucknium:monero.social >__ The MoneroKon 2025 deadline for talks submission is March 24 (but I have read discussion of possibly extending the deadline): https://www.monerokon.org/     

> __< v​tnerd:monero.social >__ me: doing optimizations related to block sync time (focused primarily on reducing allocations in add_block)     

> __< r​ucknium:monero.social >__ 3) Maintainers for the research-lab GitHub repo. https://github.com/monero-project/research-lab     

> __< r​ucknium:monero.social >__ First, do we know who the maintainers are? The repo hasn't had a merged commit since 2018     

> __< rbrunner >__ I wasn't even aware of that repo until today     

> __< r​ucknium:monero.social >__ If MRL starts releasing Research Bulletins again (which I think it should), then we would want to add the bulletins to the repo.     

> __< plowsof >__ b goodell / fluffy have historic merges there, but definitely abandoned and in need of a maintainer       

> __< r​ucknium:monero.social >__ rbrunner: You will know it by its "issues", which are quite active.     

> __< rbrunner >__ I think if we manage to reach him, and get him to bother, fluffypony may probably be able to transfer rights to somebody new     

> __< rbrunner >__ I see. Yes, the issues are live :)     

> __< plowsof >__ i say this after Rucknium mentioned wanting to do things there. luigi can handle that      

> __< plowsof >__ handle transferring perms*     

> __< r​ucknium:monero.social >__ It would be good to have an active maintainer. I said in #monero-site:monero.social  that I would be willing to take a role with merge permissions in the repo if no one else would like to do it.     

> __< rbrunner >__ You as maintainer makes sense IMHO     

> __< r​ucknium:monero.social >__ We don't have to decide now, of course.     

> __< j​berman:monero.social >__ +1 to rucknium as maintainer     

> __< r​ucknium:monero.social >__ We have two new papers, organized by Cypher Stack. I have added them to MoneroResearch.info     

> __< r​ucknium:monero.social >__ 4) Babb, J., Goodell, B., Parker, L., Salazar, R., Slaughter, F., & Szramowski, L. (2025). "FROSTLASS: Flexible Ring-Oriented Schnorr-like Thresholdized Linkably Anonymous Signature Scheme." https://github.com/cypherstack/frostlass     

> __< s​yntheticbird:monero.social >__ Clearly Rucknium maintainer     

> __< s​yntheticbird:monero.social >__ +1     

> __< rbrunner >__ FROSTLASS: acronym overload     

> __< r​ucknium:monero.social >__ Is it correct that this is the first Monero multisig protocol (at least with RingCT) that has been mathematically proven to be secure?     

> __< rbrunner >__ I think so     

> __< rbrunner >__ The one in actual use certainly lacks ... something.     

> __< r​ucknium:monero.social >__ Big congratulations to everyone involved in the paper ( Josh Babb , kayabanerve  are here, at least)     

> __< r​ucknium:monero.social >__ AFAIK, FROSTLASS is actually feasible to use for more than a few signers, unlike the one in the Monero codebase     

> __< rbrunner >__ May be the reason why the multisig handling solution from tobtoht was never published in the current form: They may wait for this to become feasible     

> __< r​ucknium:monero.social >__ 5) Salazar, R., Slaughter, F., & Szramowski, L. (2025). "Veridise Logarithmic Derivative Review." https://github.com/cypherstack/divisor_deep_dive     

> __< r​ucknium:monero.social >__ kayabanerve commented on this review: https://libera.monerologs.net/monero-research-lab/20250317     

> __< r​ucknium:monero.social >__ Quoting:     

> __< r​ucknium:monero.social >__ > CS delivered their review of the Veridise work regarding sums of points, a prelude to their latest work which was recently delivered. It's in agreeance until we get to the last part, discussing the security of how the proof is proven over integers yet performed over a finite field. Veridise argued it secure. CS disagrees and says a range proof is needed.     

> __< r​ucknium:monero.social >__ > The faulty proofs CS describe aren't forgeries though, per our view. The fundamental gadget proven, that points sum to zero, holds its integrity. The prover solely gets to find alternative points without range proofs.     

> __< r​ucknium:monero.social >__ > This isn't expected to be an issue for Monero because as we move into a scalar multiplication gadget, from a sums of points gadget, we do successfully fix points in a way the adversary shouldn't be able to perform this malleation to effect.     

> __< r​ucknium:monero.social >__ > While CS is not signing off on our total gadget (that'd be the next scope of work), and this work has notes on this part, we agree we can move forward to this next scope of work and reconcile the concerns there.     

> __< r​ucknium:monero.social >__ > I'll follow up with CS to get a quote on the latest document from Veridise, certifying the full gadget and pseudocode of it.     

> __< r​ucknium:monero.social >__ Trying to interpret this, I think this means that some of the desired properties of the divisor technique were not properly proven, but that they might not be needed, since something else in the FCMP "context" of the cryptography surrounding the divisor technique "fixes" the problem that Cypher Stack found.     

> __< rbrunner >__ That's also how I read this, but frankly, with my limited knowledge about that stuff, that does not mean much     

> __< r​ucknium:monero.social >__ As a non-specialist in this area, I am a little worried that Eagen's divisor technique seems to have had a few major issues. IIRC, the divisor technique is not absolutely essential for FCMP, but speeds up performance a lot.     

> __< r​ucknium:monero.social >__ Here is part of the introduction of Salazar, R., Slaughter, F., & Szramowski, L. (2025):     

> __< r​ucknium:monero.social >__ > We find that the original paper [Bas24] lacks a formal backing for the results used and proven. The mathematics contained in the report are sound, but lack direct reference to the results or do not contain enough justification to be taken at face value.     

> __< j​berman:monero.social >__ agree with that reading as well, I think next on this is to await the next scope of work to see if concerns are fully reconciled there. If not, I agree concern seems warranted     

> __< r​ucknium:monero.social >__ Bas24 is the "Veridise" paper:  Alp Bassa. On the Use of Logarithmic Derivatives in Eagen’s Proof of Sums of Points. https://repo.getmonero.org/-/project/54/uploads/bfe9f49326a843ef1c9466e30a5d42c8/VAR_Monero_Logarithmic_Derivatives_Final.pdf     

> __< r​ucknium:monero.social >__ While we are here, is there anything else to discuss now about FCMP research/math review/code audits?     

> __< r​ucknium:monero.social >__ (The contest is the next agenda item, in case there is more to discuss there)     

> __< j​berman:monero.social >__ kayabanerve you sound confident the concerns will be reconciled. Might it make sense to delay the ec-divisors contest until those concerns are reconciled, or should we not be concerned?     

> __< j​berman:monero.social >__ (question for when kayaba eventually gets to it)     

> __< j​berman:monero.social >__ On the contest, it seemed from the NWLB meeting we came to the conclusion that a reasonably sized compile-time table would be ok to allow for the contest. We didn't exactly settle on size of the table. Curious if jeffro256 has thoughts there     

> __< j​berman:monero.social >__ The contest details still just need sign-off at this point. I don't know of any remaining issues beyond that^     

> __< j​effro256:monero.social >__ Hi, sorry I'm late     

> __< r​ucknium:monero.social >__ Let me put the agenda item:     

> __< r​ucknium:monero.social >__ 6) Prize contest to optimize some FCMP cryptography code. https://github.com/j-berman/fcmp-plus-plus-optimization-competition     

> __< j​berman:monero.social >__ Ah! I don't recall if I mentioned, but binaryFate agreed for the GF to fund the prizes     

> __< c​haser:monero.social >__ nice!     

> __< r​ucknium:monero.social >__ Great :)     

> __< j​effro256:monero.social >__ It depends on whether we are targeting embedded systems. The benchmark machine definitely isn't "embedded", so the code isn't going to be optimized for embedded systems, but there is a question of whether we should require extremely conservative limits in case we want to support embedded systems     

> __< r​ucknium:monero.social >__ Couldn't those embedded systems use the original implementation, which may have low RAM requirements?     

> __< r​ucknium:monero.social >__ But it could be very slow on those devices     

> __< j​effro256:monero.social >__ I say no, since the embedded systems folk are probably going to require large rewrites to the toolchain and specific optimizations for their system regardless of how we write the code. Also, I think it's pointless to target embedded systems for FCMPs in the real-world Monero use case, but that's somewhat subjective     

> __< j​berman:monero.social >__ I think if we get code that can't be re-purposed for embedded systems, then we could intro the new code behind a feature flag and maintain both impls, which kayaba seemed agreeable to     

> __< j​effro256:monero.social >__ Yes this too     

> __< j​effro256:monero.social >__ The more I think about this, the less I like it. Two implementations means more technical debt for everyone not on an embedded system     

> __< rbrunner >__ I tend to think we should not worry too much about all this, start the contest soon, and then watch what comes our way     

> __< rbrunner >__ We may worry altogether for naught, after all     

> __< j​berman:monero.social >__ it's a worst case scenario     

> __< j​berman:monero.social >__ If we get code that is significantly faster that can't run on an embedded system, we would want that code for the FCMP++ integration     

> __< j​effro256:monero.social >__ We would also need a reference machine (or at least an emulator) to test this on if we're serious about it working on am embedded system     

> __< rbrunner >__ Yeah, and one recurring quality of worst-case scenarious it that they don't happen :)     

> __< rbrunner >__ (Most of the time, at least)     

> __< j​berman:monero.social >__ jeffro seems you're proposing to scrap embedded system support in the lib, which I doubt kayaba is going to want and kayaba has prior agreed to maintain the lib, so the concern for technical debt seems misplaced     

> __< j​effro256:monero.social >__ Also there is an argument to be made that forcing support of embedded devices will dilute efforts towards optimizing targets that we actually care about for the Monero use case (i.e. not embedded devices)     

> __< rbrunner >__ Did anybody ever get "down to earth" and specified what "embedded devices" we should be speaking and thinking here?     

> __< j​effro256:monero.social >__ Realistically, once we activate mainnet in Monero, will we makes very many changes to the library?     

> __< j​berman:monero.social >__ I doubt it     

> __< j​berman:monero.social >__ Either way, this line of argument generally leans favorable toward allowing code in the contest that can't run on embedded systems (by allowing pre-compiled tables)     

> __< rbrunner >__ Most things I see that I would count as such "embedded devices" today have the power of a smartphone, and can run Linux and the Monero software on top ...     

> __< j​berman:monero.social >__ It's an open question for downstream how to bring that code into the lib, but we have options to deal with that if necessary     

> __< j​berman:monero.social >__ Would be nice to settle on contest parameters here     

> __< a​ntilt:we2.ee >__ prob largely only relevant for RamdomX v2. Here speaking of FPGAs     

> __< r​ucknium:monero.social >__ The most challenging embedded devices are hardware wallets like Keystone, Trezor, Ledger, etc., right?     

> __< j​effro256:monero.social >__ Yes     

> __< rbrunner >__ At least current and past models, yes. Newer devices seem to be on par with smartphones in power     

> __< rbrunner >__ E.g. Ledger Stax     

> __< rbrunner >__ Or our own XMRSigner     

> __< r​ucknium:monero.social >__ 7) Release of OSPEAD HackerOne and CCS milestone submissions. Analysis of risk of new decoy selection algorithm without a hard fork. https://github.com/Rucknium/OSPEAD     

> __< r​ucknium:monero.social >__ Like I said in the updates, I wrote some Rust code that replaced bottlenecks in the R code of the BJR estimator in OSPEAD. It sped up the BJR estimator by 14x : https://github.com/Rucknium/OSPEAD/blob/main/CCS-milestone-2/decoyanalysis/src/rust/src/lib.rs . Last time, it took about two weeks of compute time to process two years of blockchain data, so the new code can probably do it in about a day     

> __< plowsof >__ 👏     

> __< a​ntilt:we2.ee >__ [ misinterpretation ]     

> __< r​ucknium:monero.social >__ Before the meeting, spackle  contributed some comments ^ on creating a criteria for evaluating the safety of changing the decoy selection algorithm (DSA) without a hard fork.     

> __< r​ucknium:monero.social >__ Last time I mentioned a couple of repeated measurements classifiers for classification of rings into decoy selection algorithms (DSAs). Here is a summary of some simulations.     

> __< r​ucknium:monero.social >__ The results are with a 50/50 split between the two DSAs. When the share is lopsided, i.e. when the new DSA is just starting to be adopted, the classifiers may have worse performance.     

> __< r​ucknium:monero.social >__ Hudimoto (1964), the one based on Mann-Whitney statistic, is "nice" because it has a simple closed-form formula for classifier error rate.     

> __< r​ucknium:monero.social >__ But its performance is poor, which is "not nice". That makes sense because the Mann-Whitney statistic really only uses the median of the two distributions to classify observations instead of using more information about the difference between the two distributions.     

> __< r​ucknium:monero.social >__ Its error rate is 15 - 20%.     

> __< r​ucknium:monero.social >__ I tried a similar idea with the Kolmogorov-Smirnov (KS) statistic, which uses all information in the distribution instead of just the median. I haven't seen any papers that specifically use the KS stat instead of Mann-Whitney, but its use here is logical to me.     

> __< r​ucknium:monero.social >__ With the KS stat, I got an error rate of 9 - 13%.     

> __< r​ucknium:monero.social >__ I used Bagui's "majority vote" classifier, but using a Bayes rule (i.e. using the ratio of the density of the two distributions) instead of Bagui's nearest-neighbor technique, since we have the actual distributions of the two decoy selection algorithms. I got better results when I manually adjusted the voting threshold, i.e. changed from majority to 6 of 16.     

> __< r​ucknium:monero.social >__ The error rate was 9 - 10%.     

> __< r​ucknium:monero.social >__ Then, spackle  suggested a neural net (NN) classifier. I was able to reproduce his basic results. A NN classifier is more of a "black box" than the other techniques above. I got a 6% error rate, best of everything I tried.     

> __< r​ucknium:monero.social >__ This classification is just one step in the procedure than an adversary could follow.     

> __< r​ucknium:monero.social >__ Once a tx classified into old or new DSA, the adversary can choose to apply the nonfungibility classifier or the MAP decoder.     

> __< r​ucknium:monero.social >__ NF classifier = classifier using nonfungibility defects (e.g. nonstandard DSAs) described in my https://github.com/Rucknium/misc-research/blob/main/Monero-Fungibility-Defect-Classifier/pdf/classify-real-spend-with-fungibility-defects.pdf     

> __< r​ucknium:monero.social >__ We must keep in mind that the error rate of the NF classifier depends on both the DSA classification of the transaction we are interest in _and_ the DSA classification of each of the 16 ring members. That can introduce a higher total error rate than is implied by the "6% error rate" I quoted above.     

> __< r​ucknium:monero.social >__ MAP Decoder = classifier leveraging the difference between the real spend age distribution and the decoy distribution     

> __< r​ucknium:monero.social >__ Now, we can perform a Monte Carlo simulation:     

> __< r​ucknium:monero.social >__ The simulation would look like this:     

> __< r​ucknium:monero.social >__ Let `k` be the share of transactions that have adopted the new DSA. We will want to do this with multiple different values for `k`.     

> __< r​ucknium:monero.social >__ 0) Generate rings (1 real spend and 15 decoys, each) with `k`% on the new DSA and (1 - `k`)% on the old one     

> __< r​ucknium:monero.social >__ 1) Classify all transactions by DSA by applying the NN classifier.     

> __< r​ucknium:monero.social >__ 2) Assume correct classification from step (1). Then check the classification error rate if we try each method (by NF classification or MAP Decoder).     

> __< r​ucknium:monero.social >__ 2b) If none of the ring members have the NF defect, then fall back to MAP Decoder.     

> __< r​ucknium:monero.social >__ When the adversary actually does the classification, it will choose the choice in (2) that has lowest error rate.     

> __< r​ucknium:monero.social >__ **From here, we figure out if, at a given `k`, does the adversary have a lower error rate when a new DSA is introduced, or when the status quo is left alone.**     

> __< r​ucknium:monero.social >__ I haven't written the full simulation yet, but that is the next step     

> __< r​ucknium:monero.social >__ We can also try this simulation with a "non-optimal" DSA, like spackle suggests, that may balance the effectiveness of the MAP Decoder attack with the effectiveness of the NF classifier.     

> __< r​ucknium:monero.social >__ Does anyone have thoughts on spackle 's suggestion that "The implementation code changes must be absolutely minimal. A direct update of the values of GAMMA_SHAPE and GAMMA_SCALE is essentially the limit on what is acceptable."?     

> __< a​ntilt:we2.ee >__ imo the uniform part is the problem.     

> __< r​ucknium:monero.social >__ I could try to re-run the parametric distribution fitter in OSPEAD to use the actual status quo wallet2 distribution form, but let GAMMA_SHAPE and GAMMA_SCALE vary. This idea differs from the "log gamma" fitted distribution in `OSPEAD-docs` because `OSPEAD-docs` uses a gamma distribution starting at the first spendable output (after the 10 block lock), but the wallet2 DSA starts a<clipped message     

> __< r​ucknium:monero.social >__ t chain tip, then re-allocates the unspendable portion to the RECENT_SPEND_WINDOW.     

> __< r​ucknium:monero.social >__ flip flop: You mean, wallets should randomly vary the GAMMA_SHAPE and GAMMA_SCALE parameters themselves, when they construct each of their rings?     

> __< j​effro256:monero.social >__ Is the classifier classifying whether a whole distribution belongs to the old DSA or the new DSA, or is the sample mixed 50/50, and the classifer is classifying whether each "pick" is from the old or new ?     

> __< a​ntilt:we2.ee >__ ... but for perspective: 1x churning alleviates the whole upgrade - and works since 2018. So, the discussion is highly academical.     

> __< a​ntilt:we2.ee >__ no, thats an addon.     

> __< r​ucknium:monero.social >__ For all of these, the end result is a classification of the whole ring. I think part of spackle's idea was to have a "halfway" DSA that would mix two distributions in the actual wallet code. But that mixture is just a mixture distribution that can be easily statistically modeled.     

> __< r​ucknium:monero.social >__ The "majority vote" idea from Bagui first classifies each ring member individually, but the second and last step is to classify the whole ring.     

> __< j​effro256:monero.social >__ So in this model the rings weren't a mixture, it was either old XOR new?     

> __< r​ucknium:monero.social >__ By "second and last step" I mean there are only two steps.     

> __< r​ucknium:monero.social >__ In my simulation results that I gave above, it was all-new or all-old     

> __< r​ucknium:monero.social >__ spackle had some of his own results that mixed them.     

> __< a​ntilt:we2.ee >__ right. in response to the soft-fork-upgrade discussion, he mentioned that     

> __< r​ucknium:monero.social >__ IMHO, spackle is better at the neural net techniques than me. And xmrack  would be a good person on this, too.     

> __< j​effro256:monero.social >__ Okay cool thanks. I read "50/50" split as possibly meaning that each sample set was a split between old picks and new picks     

> __< a​ntilt:we2.ee >__ right. in response to the soft-fork-upgrade discussion, he mentioned that. "baby steps" kinda.     

> __< r​ucknium:monero.social >__ Ah. Sorry. I meant that 50% of users were using the new DSA, and 50% the old.     

> __< j​effro256:monero.social >__ I'm pretty surprised that such a simple technique yielded an error rate <= 20%. Impressive     

> __< s​gp_:monero.social >__ We're working with Veridise and CS to help reconcile some of these differences, since Veridise disagrees with some of CS's review. So far, signs still point to this being usable and not an issue in practice.     

> __< r​ucknium:monero.social >__ We can end the meeting here. Feel free to continue discussing. Thanks everyone.     

> __< j​effro256:monero.social >__ I'm excited to see the results     

> __< j​effro256:monero.social >__ Thanks all     

> __< r​ucknium:monero.social >__ In the converse, I am surprised that neural nets did a lot better than all the simple techniques. AFAIK, NN do well when there are a lot of correlations and nonlinear relationships between variables. All the ring members are independent, so there is no correlation between them. Probably NN is doing well since it can optimize the threshold rules, and combine different model "ideas"<clipped message     

> __< r​ucknium:monero.social >__ . I needed to manually adjust the Bagui-like voting rule threshold to get good results.     

> __< r​ucknium:monero.social >__ And the Bagui idea is really based on work by Fisher, Neyman, and Pearson in the 1930s. Same with the MAP Decoder. Old but gold.     

> __< k​ayabanerve:matrix.org >__ Rucknium: No, thring signatures had proofs IIRC. It was a MRL publication.     

> __< k​ayabanerve:matrix.org >__ The concerns weren't with the logarithmic derivative section, even though CS had criticisms there. The concerns were with the finite field section. CS argued you can malleate which points sum to identity, which challenges the notion of proving points sum to identity. That malleation isn't an issue as both the original and the malleated still have to sum to identity. While there's <clipped message     

> __< k​ayabanerve:matrix.org >__ a question of the statement proven, the reduced statement us sufficient for the scalarmul gadget we want.     

> __< k​ayabanerve:matrix.org >__ The criticisms were on how the evidence was presented, not on if they agreed with the claims, I should say.     

> __< j​berman:monero.social >__ Do their concerns translate into an increased likelihood that divisors as implemented (and would be implemented for the contest) get scrapped?     

> __< k​ayabanerve:matrix.org >__ No     



# Action History
- Created by: Rucknium | 2025-03-18T22:26:03+00:00
- Closed at: 2025-03-28T17:21:22+00:00
