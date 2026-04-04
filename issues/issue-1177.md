---
title: Monero Research Lab Meeting - Wed 26 March 2025, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1177
author: Rucknium
assignees: []
labels: []
created_at: '2025-03-25T21:09:15+00:00'
updated_at: '2025-04-03T21:06:30+00:00'
type: issue
status: closed
closed_at: '2025-04-03T21:06:30+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. Maintainers for the [`research-lab` GitHub repo](https://github.com/monero-project/research-lab).

4.  [Salazar, R., Slaughter, F., & Szramowski, L. (2025). "Veridise Logarithmic Derivative Review."](https://github.com/cypherstack/divisor_deep_dive)

5. FCMP: [Veridise Formal Verification of Gadgets and Circuit Audit](https://gist.github.com/kayabaNerve/0de6320b67357dd348fba3ce80bf537d).

6. [Prize contest to optimize some FCMP cryptography code](https://github.com/j-berman/fcmp-plus-plus-optimization-competition).

7. [Release of OSPEAD HackerOne and CCS milestone submissions](https://github.com/Rucknium/OSPEAD). Analysis of risk of new decoy selection algorithm without a hard fork.

8. Research on [subnet deduplication for peer selection](https://github.com/Rucknium/misc-research/blob/main/Monero-Peer-Subnet-Deduplication/pdf/monero-peer-subnet-deduplication.pdf) to reduce spy node risk.

9. Any other business

10. Confirm next meeting agenda

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1174 

# Discussion History
## Rucknium | 2025-03-28T17:20:33+00:00
Logs

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1177     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< s​gp_:monero.social >__ hello     

> __< rbrunner >__ Hello     

> __< c​haser:monero.social >__ hello     

> __< j​effro256:monero.social >__ Howdy     

> __< a​rticmine:monero.social >__ Hi     

> __< love >__ I'm new here     

> __< j​berman:monero.social >__ *waves*     

> __< j​effro256:monero.social >__ love: welcome     

> __< v​tnerd:monero.social >__ hi     

> __< s​yntheticbird:monero.social >__ hello     

> __< love >__ Is it really mathematically impossible to implement a smart contract mechanism in Monero?     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< c​haser:monero.social >__ love: this is a weekly meeting with a set agenda, your question can be discussed later     

> __< love >__ Sure     

> __< r​ucknium:monero.social >__ love: Monero's current protocol doesn't support smart contracts. Implementing smart contracts would require a major protocol change. AFAIK, there is little support for this idea in the Monero community.     

> __< love >__ sounds interesting     

> __< j​berman:monero.social >__ me: implemented jeffro256 's suggestions to trim the tree via cached right-edge in the db on reorg + delay trimming until the tree is 10 blocks ahead of the chain (more on these here: https://github.com/monero-project/monero/pull/9436#issuecomment-2519858103) and finishing up some debugging at the moment. Got expected RPC functional transfers + blockchain tests working. Also work<clipped message>     

> __< j​berman:monero.social >__ ing on banning torsion at consensus for the FCMP++ fork     

> __< r​ucknium:monero.social >__ me: Wrote a simulation of the privacy risks of OSPEAD DSA deployment without a hard fork. Preliminary results here: https://gist.github.com/Rucknium/fb638bcb72d475eeee58757f754acbee . Also, some more work on speed improvements to part of OSPEAD estimation procedure (3x speedup on a days-long process).     

> __< j​effro256:monero.social >__ Me: Successfully integrated and tested Carrot scanning into `wallet2`: https://github.com/seraphis-migration/monero/blob/ebf18f4d4001b08676de29f47c07754649c1d240/tests/unit_tests/wallet_scanning.cpp#L660. With a net decrease in the size of `wallet2.cpp` I might add     

> __< r​ucknium:monero.social >__ There are some kayabaNerve items on the agenda, so ping kayabanerve     

> __< r​ucknium:monero.social >__ 3) Maintainers for the research-lab GitHub repo. https://github.com/monero-project/research-lab     

> __< r​ucknium:monero.social >__ luigi granted me some powers on the repo, so I can put things in the it (I think). Probably can start with updating the IRC server from freenode to Libera and adding the Matrix address. There's already a PR for that. And add jeffro256 's "docs/utils: add decoy selection implementation guides and tools" https://github.com/monero-project/monero/pull/9024     

> __< v​tnerd:monero.social >__ forgot to give updates me: working on perf updates and lws-frontend stuff     

> __< r​ucknium:monero.social >__ And put in the papers commissioned by MRL on FCMP so we have extra copies.     

> __< r​ucknium:monero.social >__ Any other suggestions for the repo?     

> __< r​ucknium:monero.social >__ 4) Salazar, R., Slaughter, F., & Szramowski, L. (2025). "Veridise Logarithmic Derivative Review." https://github.com/cypherstack/divisor_deep_dive     

> __< j​berman:monero.social >__ I guess kayaba isn't here, but not sure of much more to discuss on this review since we last discussed it. The general takeaway from it was that the next work item with CS is meant to address concerns raised in the paper     

> __< r​ucknium:monero.social >__ I read this. (I did not understand much). AFAIK, it's saying that it wished that the Veridise paper by Bassa had better practices with citing important mathematical theorems and lemmas in the research literature, but that things looked OK. It was also more clear/direct about the risks in the proposed protocol. That it needs a range proof or an adversary can produce a forgery. The <clipped message     

> __< r​ucknium:monero.social >__ Veridise paper by Bassa was not as direct about that IMHO.     

> __< r​ucknium:monero.social >__ I guess a range proof is needed (which could make the protocol much heavier in tx size probably) or there is some cryptography context surrounding this component that repairs the range prof issue     

> __< r​ucknium:monero.social >__ proof*     

> __< r​ucknium:monero.social >__ I guess we need someone external to verify that the context avoids the issue     

> __< j​berman:monero.social >__ AFAIU it's the latter. kayaba's claim as I understand it is that it's not relevant how we're using divisors, and that CS next slate of work is to verify the claim (and our use of divisors generally), while addressing that component     

> __< r​ucknium:monero.social >__ CS = Cypher Stack https://www.cypherstack.com/ , for anyone unaware     

> __< r​ucknium:monero.social >__ Ok sounds good. We will wait for that proposal     

> __< r​ucknium:monero.social >__ Any other comments on this item?     

> __< r​ucknium:monero.social >__ 5) FCMP: Veridise Formal Verification of Gadgets and Circuit Audit. https://gist.github.com/kayabaNerve/0de6320b67357dd348fba3ce80bf537d     

> __< rbrunner >__ "The research fund has over 250,000 USD at current prices." What is that again?     

> __< r​ucknium:monero.social >__ > Veridise has yielded a quote to work on formally verifying the non-interactive gadgets present. The FCMP++ specification has two interactive gadgets, one the discrete log proof they wrote security proofs for, and one the tuple-member-of-list gadget. Their quote also includes the development of a soundness proof for the tuple-member-of-list gadget.     

> __< r​ucknium:monero.social >__ This wording is confusing to me since it says Veridise would be verifying _non-interactive_ gadgets. But then it says FCMP++ has two _interactive_ gadgets. Is it worded like that to say that there is still work to be done on other gadgets after Veridise woulc omplete this proposed work?     

> __< j​effro256:monero.social >__ It might be a typo. FCMP++ shouldn't have any interactive gadgets AFAIK     

> __< j​effro256:monero.social >__ That would mean that each node would need a direct line of communication with the sender of a transaction ;)     

> __< r​ucknium:monero.social >__ Is all this code auditing, or some of it theoretical mathematics, too? If the latter, then we should comment to them (if not already) that we want more extensive citation practices than Bassa (2024), because Cypher Stack researchers suggested it.     

> __< r​ucknium:monero.social >__ rbrunner: What is the research fund? AFAIK, this: https://ccs.getmonero.org/proposals/fcmp++-research.html     

> __< j​berman:monero.social >__ "It might be a typo. FCMP++ shouldn't have any interactive gadgets AFAIK" -> believe this is correct     

> __< rbrunner >__ Ah, yes, of course. So it *was* 250,000 USD, when spending started :)     

> __< j​berman:monero.social >__ "Is all this code auditing, or some of it theoretical mathematics, too?" -> it's both. In the list of remaining research tasks, this would cover 1) gadgets formal verification (theoretical), 2) gadgets impl audit (code audit), 3) circuit impl audit (code audit)     

> __< j​berman:monero.social >__ "then we should comment to them (if not already) that we want more extensive citation practices than Bassa (2024), because Cypher Stack researchers suggested it." -> seems a reasonable suggestion to me (pinging kayabanerve to notify)     

> __< r​ucknium:monero.social >__ Is it the intention that this proposed expenditure achieve loose consensus here at this meeting?     

> __< j​berman:monero.social >__ That was the intent     

> __< rbrunner >__ Wrong again. This is probably indeed what currently remains. I wasn't aware anymore how big the original CCS sum was.     

> __< r​ucknium:monero.social >__ > Finally, their quote includes an audit of generalized-bulletproofs-circuit-abstraction, generalized-bulletproofs-ec-gadgets, and full-chain-membership-proofs. The first library provides a higher-level API for the generalized-bulletproofs crate, audited by Aaron Feickert under Cypher Stack's solicitation, funded by a third party (Power Up Privacy).     

> __< r​ucknium:monero.social >__ This will audit a "wrapper" for something that has already been audited, or Veridise will audit the same library again?     

> __< r​ucknium:monero.social >__ I'm not opposed to either alternative     

> __< j​berman:monero.social >__ The former as I understand it     

> __< r​ucknium:monero.social >__ Just making sure I understand the scope of work     

> __< s​gp_:monero.social >__ Hey all, I can comment a bit on the scope of work for this Veridise proposal     

> __< r​ucknium:monero.social >__ Thanks, sgp_     

> __< s​gp_:monero.social >__ https://matrix.monero.social/_matrix/media/v1/download/monero.social/MTCidUxooiQjtMoWcdgGaXij     

> __< s​gp_:monero.social >__ This is exactly how the current proposal is in the contract     

> __< s​gp_:monero.social >__ The redline was accepted, so you can ignore that     

> __< s​gp_:monero.social >__ This audit, in sum, is one of the largest remaining components of this research CCS     

> __< r​ucknium:monero.social >__ Is Picus source-available at least?     

> __< s​gp_:monero.social >__ The work will be completed in this manner:     

> __< s​gp_:monero.social >__ 1. Formal verification/proofs for the gadgets.     

> __< s​gp_:monero.social >__ 2. Review of the circuit and overarching proof.     

> __< s​gp_:monero.social >__ 3. Review of the implementation.     

> __< s​gp_:monero.social >__ It's in this order because if they find something incorrect in part 1 or 2, it can be fixed before wasting the rest of the time auditing a broken implementation     

> __< s​gp_:monero.social >__ https://github.com/Veridise/Picus     

> __< r​ucknium:monero.social >__ I think that marketers love using the "proprietary" adjective, even if inappropriately.     

> __< r​ucknium:monero.social >__ Well, maybe it's technically correct to use that word since it is copyrighted in their name, but it doesn't increase confidence in this situation.     

> __< s​gp_:monero.social >__ The estimated start date for this is April 7th, and I believe it's important to get started on this if there is approval for it     

> __< r​ucknium:monero.social >__ For (1), then MRL would get someone to review Veridise's mathematical proofs?     

> __< s​gp_:monero.social >__ Veridise is the preferred vendor because they have a lot of experience with these toolings. That's the main thing they are known for as I understand     

> __< s​gp_:monero.social >__ Yes, there will be a completely separate project for reviewing the divisors work, and Veridise will _not_ be the vendor for reviewing that work     

> __< r​ucknium:monero.social >__ Which would make it important to ask them to change their citation practices so that, potentially, Cypher Stack researchers wouldn't be distracted by it.     

> __< s​gp_:monero.social >__ I spoke with kayaba yesterday about that, and those quotes were not ready in time for this meeting. Buy they are being actively discussed     

> __< s​gp_:monero.social >__ I spoke with kayaba yesterday about that, and those quotes were not ready in time for this meeting. But they are being actively discussed     

> __< s​gp_:monero.social >__ It's possible that other vendors will be contacted for the divisors review as well, but Cypher Stack has done the two prior reviews and is the main firm being talked to for the final review     

> __< s​gp_:monero.social >__ This proposed Veridise audit is largely separate from the divisors work. It can be thought of as a distinct project for planning purposes     

> __< j​berman:monero.social >__ I'm a +1 on Veridise in this proposal. It's quite large in scope, and knocks out major tasks remaining. Veridise has demonstrated high quality work and has the requisite skills and knowledge to take this on     

> __< r​ucknium:monero.social >__ Thanks, jberman. More opinions on this proposal?     

> __< rbrunner >__ I am not aware about any mayor hiccup so far in the whole process, kaya seems to be on top of it, and I continue to trust his proposals hot to proceed     

> __< rbrunner >__ *how to proceed     

> __< rbrunner >__ Just saw that the fiat price almost doubled since people donated to that CCS. Good luck!     

> __< r​ucknium:monero.social >__ +1 This all sound good to me. Thank you everyone who put work into this important step :)     

> __< j​effro256:monero.social >__ Agreed!     

> __< r​ucknium:monero.social >__ Make sure the Veridise researcher(s) doing the mathematical proof reads Salazar, R., Slaughter, F., & Szramowski, L. (2025). "Veridise Logarithmic Derivative Review." https://github.com/cypherstack/divisor_deep_dive     

> __< s​gp_:monero.social >__ Rucknium: For the divisors, Veridise is not expected to do more work on that, unless another review demonstrates that they have something else to review     

> __< s​gp_:monero.social >__ They were shared a copy of that CS review work     

> __< r​ucknium:monero.social >__ sgp_: The Cypher Stack researchers had suggestions for how Veridise could present the work. That's the most relevant parts of it.     

> __< s​gp_:monero.social >__ Veridise disagreed with those, and believes no modifications are necessary     

> __< r​ucknium:monero.social >__ Well, at least they read it     

> __< s​gp_:monero.social >__ Further review work remains on divisors, but the suggested plan needs more work before presenting at a meeting     

> __< s​gp_:monero.social >__ So expect an update on those in a week or two (?) when there's a clear option to deliberate on     

> __< j​berman:monero.social >__ Circling back to Veridise, was that +1 from Rucknium and agree from jeffro also a favorable opinion on proceeding with Veridise on their proposal?     

> __< r​ucknium:monero.social >__ Yes, +1 from me on https://gist.github.com/kayabaNerve/0de6320b67357dd348fba3ce80bf537d . Thanks for checking     

> __< s​gp_:monero.social >__ Let me know if this has specific approval to move forward so I can execute the agreement     

> __< r​ucknium:monero.social >__ I see rough consensus in favor of the expenditure to contract Veridise for this scope of work: https://gist.github.com/kayabaNerve/0de6320b67357dd348fba3ce80bf537d     

> __< r​ucknium:monero.social >__ sgp_: You are approved to execute the agreement     

> __< s​gp_:monero.social >__ Thank you all     

> __< r​ucknium:monero.social >__ 6) Prize contest to optimize some FCMP cryptography code. https://github.com/j-berman/fcmp-plus-plus-optimization-competition     

> __< j​effro256:monero.social >__ +1 from me too     

> __< j​berman:monero.social >__ I have one point of discussion for the contest     

> __< j​berman:monero.social >__ kayaba is of the opinion that final divisors review will go smoothly, and that the contest should not be delayed by ongoing divisors review     

> __< rbrunner >__ You mean, not wait until it's really sure that those divisors hold, but take the small risk and start nevertheless?     

> __< j​berman:monero.social >__ Correct     

> __< j​berman:monero.social >__ I think there is still some non-0 (seemingly small) chance that final divisors review identifies issues     

> __< r​ucknium:monero.social >__ IMHO, the risk should be taken. Since it will probably be mostly people not currently involved in FCMP implementation, the loss would only be in XMR, not FCMP labor hours. That's my first impression.     

> __< rbrunner >__ Nothing against that from me. There is some risk inherent in almost every step here, so if chances look good I think we should march on     

> __< j​berman:monero.social >__ Here's a possible timeline: we launch the contest and say we start accepting submissions 1 month from today. In 4 weeks, the divisors review completes and identifies some issue, while the contest hasn't opened for submissions yet     

> __< j​berman:monero.social >__ Not exactly sure how to handle that situation     

> __< j​berman:monero.social >__ I'm thinking about including a clause in the divisors contest only that there is review work ongoing and that there is a small chance the review work identifies something that would affect the contest     

> __< j​berman:monero.social >__ Or in that situation do we just count it as a loss, and proceed with the contest as it originally was anyway and pay out any submissions that satisfy the contest rules still?     

> __< j​effro256:monero.social >__ I'm not sure I like that option. IMO if we open a competition with terms and people work on it, then we have an obligation to pay the winner who fulfills those terms. Also, saying "we accept submissions in 4 weeks but there'a a chance we close it" makes us sound weak/unsure and might drive off competition     

> __< j​effro256:monero.social >__ Doesn't exactly inspire confidence     

> __< j​berman:monero.social >__ Ok, good with me to take the risk     

> __< r​ucknium:monero.social >__ I agree with jeffro256 .     

> __< rbrunner >__ Isn't the chance of a total loss smaller still? Maybe only small tweaks may be needed, that the submissions might be able to modify to     

> __< j​effro256:monero.social >__ If the gadget is broken, but the issue is minor and most of the performant code can be reused/refactor-ed, then it isn't a complete loss anyways     

> __< j​effro256:monero.social >__ rbrunner: jinx     

> __< rbrunner >__ :)     

> __< j​berman:monero.social >__ Awesome     

> __< j​berman:monero.social >__ Well then, contest is a go :) jeffro256 's given approval on the details     

> __< j​effro256:monero.social >__ A major loss for us would only occur if the issue was a major flaw in the divisors, which I feel is unlikely this far down in the process. I can forsee small issues, but IDK     

> __< rbrunner >__ Good. The tension waiting for the fun is getting hard for me :)     

> __< rbrunner >__ I am really curious how it will go     

> __< j​berman:monero.social >__ Proposal: we open the contest for submissions Monday April 27th, and the contest closes for submissions June 29th     

> __< j​berman:monero.social >__ And can commence the marketing blitz with xmrack 's help imminently     

> __< r​ucknium:monero.social >__ Sounds great to me. Thanks for all the work on this, especially jberman , jeffro256 , and kayabanerve     

> __< a​ck-j:matrix.org >__ 👍🏼   

> __< a​ck-j:matrix.org >__ Catching up on chat logs now     

> __< r​ucknium:monero.social >__ xmrack: Don't leave yet. Next item may be relevant to you :)     

> __< r​ucknium:monero.social >__ 7) Release of OSPEAD HackerOne and CCS milestone submissions. Analysis of risk of new decoy selection algorithm without a hard fork. https://github.com/Rucknium/OSPEAD     

> __< a​ntilt:we2.ee >__ This work suggests that the feared "dip" in eff. ring size during a transition period will not be a major problem, at least at the startup phase with >10% upgraded wallets.     

> __< r​ucknium:monero.social >__ New gist: "Preliminary results of risk of OSPEAD deployment without hard fork" https://gist.github.com/Rucknium/fb638bcb72d475eeee58757f754acbee     

> __< r​ucknium:monero.social >__ flip flop: That's right, according to very preliminary results.     

> __< r​ucknium:monero.social >__ In these very preliminary results, I find that it is better to deploy the OSPEAD-derived now, with any user adoption share, than to continue with the current DSA. There are some big caveats. Mainly:     

> __< r​ucknium:monero.social >__ 1) Some of the chosen distribution are not exactly what would be deployed     

> __< r​ucknium:monero.social >__ 2) The procedure I used is not necessarily the most powerful for the adversary. A procedure that puts everything into a machine learning algorithm might be able to achieve greater de-anonymization results.     

> __< r​ucknium:monero.social >__ IMHO, next steps are trying to put it all in a machine learning algorithm, possibly with the help of spackle , xmrack , and/or ack-j's prior code applying machine learning to stagenet/testnet txs: https://github.com/ACK-J/Monero-Dataset-Pipeline/tree/main/DataScience     

> __< r​ucknium:monero.social >__ And re-estimating OSPEAD using recent data and the faster code I've been working on, plus a few changes appropriate for deployment without a hard fork. Then the new estimates can be used for simulations.     

> __< r​ucknium:monero.social >__ Why is the risk not greater? IMHO, it's because the NN classification into new/old DSA become harder when the sample is very unbalanced, i.e. when the new-DSA users are a small minority. Yet, that is exactly the circumstances when a non-fungibility classifier is strongest.     

> __< r​ucknium:monero.social >__ For example, when 50% of txs are new-DSA and 50% are old-DSA, the NN classifier correctly predicts the DSA of new-DSA transactions in 91% of cases. When 5% of txs are new-DSA and 95% are old-DSA, the NN classifier correctly predicts the DSA of new-DSA transactions in only 67% of cases. This is a well-known issue with classification unbalanced samples. So well-known that they teach<clipped message     

> __< r​ucknium:monero.social >__  it in medical school: https://quoteinvestigator.com/2017/11/26/zebras/     

> __< r​ucknium:monero.social >__ Also, we must hold in mind that not just the "transaction of interest" must be classified into new/old-DSA by the NN classifier. The transactions of every ring member (the "antecedent transactions") must also be classified as new/old DSA, which multiplies the error.     

> __< r​ucknium:monero.social >__ Having a machine learning algorithm do all the steps may increase the de-anonymization risk since the ML can adjust the first DSA classification step rules to suit the later real spend classification step. Right now they are separated.     

> __< r​ucknium:monero.social >__ That's my update     

> __< s​packle:monero.social >__ Very encouraging preliminary results.     

> __< rbrunner >__ Of course we don't know much about potential adversaries, but I wonder who would still pour money into their tools and update after such a deployment, with FCMP++ approaching     

> __< a​ntilt:we2.ee >__ > For example, when 50% of txs are new-DSA and 50% are old-DSA, the NN classifier correctly predicts the DSA of new-DSA transactions in 91% of cases.     

> __< a​ntilt:we2.ee >__ ... that leaves 9% for old DSAs. Which is pretty good (low risk) !     

> __< r​ucknium:monero.social >__ The MAP Decoder is the strongest real spend classifier using just the timing data, according to Proposition 4 of Aeeneh et al. (2021). So a ML classifier in theory wouldn't be able to improve on it. My non-fungibility (NF) classifier is pretty good I think, but maybe it could be improved. I think the potential advantage from a whole-ML approach is in improvements in mixing the two<clipped message     

> __< r​ucknium:monero.social >__  real-spend classifiers and adapting the DSA classification rules/thresholds to serve the later real spend classification step.     

> __< a​rticmine:monero.social >__ This is very interesting. So in the case where we have 5% old DSA 95% new DSA?     

> __< a​ntilt:we2.ee >__ I really like this work, but "do nothing" is in fact a valid option... imho     

> __< r​ucknium:monero.social >__ ArticMine: Good question. These are some results with an older version of the NN classifier: When it is 10% _old_ DSA share, still there is not greater risk for those lagging users. But then at 5% _old_ I get modestly higher risk: 32.8% probability of guessing the real spend for those old-DSA users, compared to 27% baseline risk of MAP Decoder against the old DSA.     

> __< r​ucknium:monero.social >__ Then at 2% old I get 29.7% probability of the adversary guessing the real spend (again, using the older and less effective NN model).     

> __< r​ucknium:monero.social >__ Of course, by that point the risk for the new-DSA users is much smaller, and they make up the vast majority of users, so the aggregate mean risk is lower when we are that far into the adoption curve     

> __< a​ck-j:matrix.org >__ Rucknium: im pretty limited on free cycles but can probably whip something up fast if you point me to the dataset. We could also post it on kaggle and see who can tune the best NN     

> __< a​ntilt:we2.ee >__ ... when the baseline of 4.2 translates to 26.25%     

> __< j​effro256:monero.social >__ Also that's still "only" a 1/3 chance, where it's a 1/4.2 chance now, yeah?     

> __< r​ucknium:monero.social >__ jeffro256: Yes. Note that baseline MAP Decoder risk is a little higher in this simulation: https://gist.github.com/Rucknium/fb638bcb72d475eeee58757f754acbee#assumptionsinitial-parameters     

> __< a​ntilt:we2.ee >__ ... when the baseline of 4.2 translates to 23.2%     

> __< r​ucknium:monero.social >__ xmrack: Could you have more free cycles if I paid you to work on it (possible for spackle , too)?     

> __< a​ntilt:we2.ee >__ ... when the baseline of 4.2 translates to 23.8% [sry]     

> __< c​haser:monero.social >__ that's an interesting situation, reminding me a bit of a kind of a moral hazard/utilitarian position, i.e. users adopting the new DSA can reduce the effective ring size of those who stay on the old DSA. not making a judgment here, just noting.     

> __< r​ucknium:monero.social >__ I acknowledge that my knowledge of machine learning techniques is limited and I want to make sure we get all the help we can on this     

> __< a​rticmine:monero.social >__ It actually becomes an outreach / marketing problem. Minimizing the time where the new DSA / old DSA is most unbalanced     

> __< a​ck-j:matrix.org >__ Rucknium: its more a time constraint issue. I’ll happily help out as much as I can     

> __< r​ucknium:monero.social >__ chaser: I doubt that 95% rate of adoption could be achieved before a new hard fork. But yes you are right that there are interesting differential effects on adopters/non-adopters that raise normative questions.     

> __< r​ucknium:monero.social >__ xmrack: Thanks. I will work towards it.     

> __< c​haser:monero.social >__ Rucknium good point. in that case, as ArticMine said, the goal would be to boost the initial adoption wave to push the mark past the first 5% as quickly as possible.     

> __< r​ucknium:monero.social >__ "It" = seeing how I can set something up for you to easily plug in data to what you already have, etc     

> __< a​ntilt:we2.ee >__ on marketing: does monerod throw a (aggressive) warning to peers, which are not up to date?     

> __< r​ucknium:monero.social >__ I liked spackle 's idea to have a delayed trigger in a release version that would have all updated wallets start using it after a predtermined block height, maybe 1-2 months after release. Then you could "skip" some of the adoption curve     

> __< s​packle:monero.social >__ Rucknium: My preference is to contribute what I am willing and able to as a volunteer. That said, I'll consider the possibilities.     

> __< a​ntilt:we2.ee >__ on marketing: does monerod throw a (aggressive) warning to peers, which are not up to date? [ like i.e. zanod does ]     

> __< c​haser:monero.social >__ the delayed trigger sounds like a good idea.     

> __< r​ucknium:monero.social >__ flip flop: What needs to update is the wallet, not the nodes. Anyway, the GUI wallet suggests updates when they are available. And the "third party" mobile wallets would probably suggest updates, too, or they automatically update on some users' devices     

> __< r​ucknium:monero.social >__ spackle: I'm using your NN model setup in my simulations.     

> __< c​haser:monero.social >__ Feather Wallet gives you a notification in its status bar (at the bottom) upon new releases. it can't even be turned off, which, in this case, is a good thing :)     

> __< r​ucknium:monero.social >__ I will post the simulation code soon. Right now it is a little more confusion than I would like, since it has to switch between the two DSA possibilities a lot.     

> __< a​rticmine:monero.social >__ I like the delayed trigger idea.     

> __< r​ucknium:monero.social >__ confusing*     

> __< r​ucknium:monero.social >__ Let's end the meeting here since we are 45 minutes past the hour. Feel free to continue discussing any items after the meeting. Thank you everyone.     

> __< s​packle:monero.social >__ Thanks all     

> __< k​ayabanerve:matrix.org >__ Apologies. My timing was off today     

> __< k​ayabanerve:matrix.org >__ jeffro256: The two interactive gadgets refers to the gadgets requiring the Fiat-Shamir transform: the discrete log gadget and the tuple-set-membership gadget. One was proven, the other would have security proofs under this proposal.     

> __< k​ayabanerve:matrix.org >__ It's only the gadgets which are non-interactive which would be formally verified. The ones requiring a hash function aren't really eligible. It's those we either have security proofs for or would get a security proof under this quote.     

> __< b​asses:matrix.org >__ there actually a delay monero.social/matrix.org issue again I guess     

> __< k​ayabanerve:matrix.org >__ As for the largely, distinct discussion on divisors/the discrete log gadget's security proofs, I'll try to have a complete comment these next few days.     

> __< k​ayabanerve:matrix.org >__ *largely distinct, that comma shouldn't be there D:     

> __< c​haser:monero.social >__ love: regarding your earlier question about smart contracts, which is actually a good question. what Rucknium said is all correct. I'll raise attention though to two items:     

> __< c​haser:monero.social >__ * Kayaba proposed a scheme in which Monero would evaluate an R1CS circuit, a sort of a fertile ground for verifying ZK proofs of execution of arbitrary logic. they also proceeded to sketch out a concrete design: https://github.com/monero-project/research-lab/issues/116#issuecomment-1947749510     

> __< c​haser:monero.social >__ * Andrew Poelstra's "scriptless scripts." the general idea is to exploit certain properties of a signature scheme to "encode" logic. Poelstra's work explores this concretely using Schnorr adaptor signatures (https://download.wpsoftware.net/bitcoin/wizardry/mw-slides/2018-05-18-l2/slides.pdf). I (very boldly) conjectured that other schemes, including Monero's current CLSAG, could b<clipped message>     

> __< c​haser:monero.social >__ e exploited in this way. however, scriptless scripts are much more constraining (you can't just write a contract you want), and I expect their currently understood form to become irrelevant for Monero on the mid term because there's momentum to abandon elliptic curve cryptography in favor of post-quantum crypto.     




# Action History
- Created by: Rucknium | 2025-03-25T21:09:15+00:00
- Closed at: 2025-04-03T21:06:30+00:00
