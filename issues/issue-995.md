---
title: Monero Research Lab Meeting - Wed 24 April 2024, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/995
author: Rucknium
assignees: []
labels: []
created_at: '2024-04-24T12:34:19+00:00'
updated_at: '2024-05-01T20:41:46+00:00'
type: issue
status: closed
closed_at: '2024-05-01T20:41:45+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://web.archive.org/web/20230128130949/https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Potential measures against a black marble attack](https://github.com/monero-project/research-lab/issues/119).

4. Research [Pre-Seraphis Full-Chain Membership Proofs](https://gist.github.com/kayabaNerve/0e1f7719e5797c826b87249f21ab6f86). 

5. Any other business

6. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#992 

# Discussion History
## Rucknium | 2024-04-25T11:59:41+00:00

Logs:

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/995     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< rbrunner >__ hello     

> __< o​ne-horse-wagon:monero.social >__ Hello.     

> __< c​haser:monero.social >__ Hello     

> __< tevador >__ Hi     

> __< weechat2 >__ hi     

> __< a​rticmine:monero.social >__ Hi     

> __< r​ucknium:monero.social >__ weechat2: Are you vtnerd?     

> __< weechat2 >__ ah this again, soryr     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< h​into.janaiyo:matrix.org >__ hello     

> __< r​ucknium:monero.social >__ me: I have a draft framework for evaluating the ringsize-fee tradeoff to defeat black marble flooding. I can discuss in the black marble agenda item.     

> __< vtnerd >__ I focused on a fewbbugs in LWS, and a bug in the p2p ssl patch     

> __< tevador >__ I'm working on a Jamtis version compatible with the FCMP++ key format.     

> __< r​ucknium:monero.social >__ 3) Discuss: Potential measures against a black marble attack https://github.com/monero-project/research-lab/issues/119     

> __< h​into.janaiyo:matrix.org >__ me: nearing the end of Cuprate's db impl, reader/writer threads + request/response handling     

> __< r​ucknium:monero.social >__ I am working on estimating the best combination of raising ring size and/or increasing the tx fee to defeat black marble flooding. Any input is appreciated. Of course feedback can be included if given later, but sooner is better :)     

> __< r​ucknium:monero.social >__ Here is my idea: Compute the cost effectiveness of the alternatives and pick the alternative with the best cost effectiveness. Cost effectiveness is the cost of some option divided by the quantified desired outcome. Lower is better.     

> __< r​ucknium:monero.social >__ In our problem, it is the cost of raising ring size and/or fee divided by the effective ring size that a flooding adversary could achieve with some specified budget per day. The formula for effective ring size is equation (3) on page 7 of https://github.com/Rucknium/misc-research/blob/main/Monero-Black-Marble-Flood/pdf/monero-black-marble-flood.pdf     

> __< r​ucknium:monero.social >__ What is the cost of raising ring size and fee? My proposal: (1) Aggregate fees paid by transactors plus (2) the cost to store tx data by all node operators. To compute (1) take an average block's transactions and recompute tx size and fees with different ring sizes and fees/byte. I think we should use the four weeks of tx data before the March spam occurred.     

> __< r​ucknium:monero.social >__ My proposal for (2) is take the median price for a consumer 1TB SATA SSD, divide by one tera to get the cost to store one byte, then multiply by the estimated number of nodes on the network at https://monero.fail/map (about 20,000 now). Does that sound reasonable?     

> __< o​ne-horse-wagon:monero.social >__ Rucknium: Did the recent flooding attacks hurt anything at all in Monero?     

> __< r​ucknium:monero.social >__ You mean the March one or the two-day one in April?     

> __< o​ne-horse-wagon:monero.social >__ Some transactions were delayed but was there any real damage?     

> __< r​ucknium:monero.social >__ Read the linked PDF     

> __< r​ucknium:monero.social >__ Spam by an adversary can reduce the privacy of ring signatures. This problem has been known since 2014.     

> __< tevador >__ I think we could raise the ring size to match the future FCMP++ tx size, pending some perf analysis. That would also raise the min fee.     

> __< r​ucknium:monero.social >__ What I see in my preliminary results is that raising the ring size is much more cost effective than raising the fee. Of course, if the assumptions are very different, then a fee increase looks better.     

> __< rbrunner >__ I don't understand yet what you mean with this: "quantified desired outcome"     

> __< r​ucknium:monero.social >__ For example (preliminary), if the budget of the adversary is much, much higher than the March suspected flood and the cost to the node operators is assumed to be much higher than the simple SSD cost computation, then a fee increase can be more cost effective.     

> __< tevador >__ The "outcome" is probably the effective ring size for the black marble attacker     

> __< r​ucknium:monero.social >__ Our "quantified desired outcome" is effective ring size _if_ an adversary floods the blockchain with black marble outputs.     

> __< c​haser:monero.social >__ sounds reasonable to me. would you agree that the increase in tx creation and verification time is also a cost, although hard (or impossible) to properly quantify? qualitative factors like climate, etc.     

> __< c​haser:monero.social >__ * I should say computation cost, time is only a part of that     

> __< a​rticmine:monero.social >__ There is another factor here namely the surge factor. How much the short term median can grow without an increase in the long term median     

> __< r​ucknium:monero.social >__ chaser: Yes. This leaves out some costs. There are some benefits to higher fees like larger mining security budget, for example, too. And this simple storage cost assumes that there are no pruned nodes and all the nodes on monero.fail are real nodes (some are suspected spoofed nodes)     

> __< r​ucknium:monero.social >__ ArticMine: Right. My current draft does not try to analyze the short-term block size ceiling. I can try to model that, too.     

> __< j​effro256:monero.social >__ Howdy sorry i'm late     

> __< k​ayabanerve:monero.social >__ 👋     

> __< a​rticmine:monero.social >__ Essentially if the ring size is greater than the surge factor a black marble attack is theoretically not possible     

> __< r​ucknium:monero.social >__ By the way, with current numbers on SSD price and number of nodes, Monero's minimum fee/byte (20 nanoneros) is almost exactly the aggregate node storage cost. An astonishing coincidence. (This might be a Pigouvian fee on an externality.)     

> __< plowsof >__ M.     

> __< rbrunner >__ Over all those many nodes? Wow.     

> __< k​ayabanerve:monero.social >__ Re: what I'm working on, I published a PDF for FCMP++ with background, proper pacing, and details. Ill refrain from further comments until a relevant topic comes up. Sorry for being late to attend.     

> __< r​ucknium:monero.social >__ Eventually a spammer could raise the block size large enough, but it may take a lot of time.     

> __< rbrunner >__ Because it was an often-heard argument, that the spammer can store gigabytes in our blockchain for much to low a price. Does not seem like that?     

> __< r​ucknium:monero.social >__ 1TB SATA SSD is about 1XMR now. Divide 1XMR by a tera gets you 1 piconero. Min fee/byte is 20,000 piconeros (20 nanoneros). Unless I did something wrong with this simple arithmetic.     

> __< a​rticmine:monero.social >__ I consider 16 to be the minimum surge factor possible based upon the historical VISA data     

> __< a​rticmine:monero.social >__ Especially the ratio between the maximum capacity of the VISA network and average TPS     

> __< r​ucknium:monero.social >__ I will title this section "How i learned to stop worrying [about storage costs] and love big rings"     

> __< rbrunner >__ :)     

> __< k​ayabanerve:monero.social >__ Bad time to mention how larger rings increase data storage capabilities?     

> __< r​ucknium:monero.social >__ Good time to mention it. Storage is cheap! And most ring data is removed when you prune :)     

> __< k​ayabanerve:monero.social >__ I don't think that's an issue here, I just have to note :p     

> __< r​ucknium:monero.social >__ Run the numbers. Have people been worrying about nothing for so long, without running the numbers?     

> __< a​rticmine:monero.social >__ This is critically important in order to understand why Monero can scale and Bitcoin cannot.     

> __< r​ucknium:monero.social >__ I want to get to the next agenda item on FCMP at 17:30.     

> __< rbrunner >__ Well, lack of space for the blockchain on older computers is real. And never mind a 1TB SSD, over USB that may not be really fast, again depending on the USB variant available     

> __< r​ucknium:monero.social >__ Here are more questions to think about: We need a set of options to consider. Does ring size 16-60 and fee 1x to 10x current min fee sound reasonable? Should going below a specific effective ring size be avoided at all costs? What range of the adversary's budget should we assume? The estimated expenditure of the March spammer was about 2.5 XMR per day. Should we look at 1x to 100x that budget?     

> __< j​effro256:monero.social >__ Well it depends on if you only care about storage costs. You might also want the fees to cover aggregate CPU time to verify, bandwidth of broadcasted txs, other p2p communication costs, opportunity cost of RAM usage, etc     

> __< a​rticmine:monero.social >__ If the computer does not support USB 3 replace the hard drive.     

> __< r​ucknium:monero.social >__ jeffro256: You are right, yet those things are harder to get reliable estimates about. I can multiply the storage costs by some factor to approximate those other costs.     

> __< k​ayabanerve:monero.social >__ Actual Q. Are we factoring DB reads into CLSAG 40 evaluations?     

> __< r​ucknium:monero.social >__ kayabanerve: I think we should. I would prefer to have good benchmarks for larger rings. With actual `monerod` code instead of theoretical benchmarks     

> __< r​ucknium:monero.social >__ Since the read time affects total verification time.     

> __< k​ayabanerve:monero.social >__ Right. The cryptography alone isn't enough if we need notable time to prepare the statement.     

> __< tevador >__ Another big advantage of FCMP++: no DB reads needed to verify a tx.     

> __< r​ucknium:monero.social >__ I may try to do those benchmarks by myself, but t is probably not my comparative advantage to figure that out.     

> __< k​ayabanerve:monero.social >__ tevador: I was waiting to say it :p     

> __< r​ucknium:monero.social >__ 4) Research Pre-Seraphis Full-Chain Membership Proofs https://gist.github.com/kayabaNerve/0e1f7719e5797c826b87249f21ab6f86     

> __< k​ayabanerve:monero.social >__ I published a PDF quite comprehensive in that regard.     

> __< k​ayabanerve:monero.social >__ I am eager for jeffro's thoughts.     

> __< c​haser:monero.social >__ FYI, link: https://github.com/kayabaNerve/fcmp-ringct/blob/develop/fcmp%2B%2B.pdf     

> __< r​ucknium:monero.social >__ kayabanerve: Could you link the PDF here for the meeting log?     

> __< k​ayabanerve:monero.social >__ jeffro, koe, and tevador all support the development CCS now.     

> __< k​ayabanerve:monero.social >__ chaser has it correct :)     

> __< j​effro256:monero.social >__ Kayaba: that is a good point, although I suspect that the DB read time is pretty insignificant compared to verify  run time for CLSAG or FCMP. I used to have the same thoughts, but after spending a lot of time trying to optimize LMDB and doing benchmarks, its surprisingly much faster than you would expect. TBF I did do those tests on an NVME     

> __< j​effro256:monero.social >__ LMDB really just is ridiculously fast     

> __< k​ayabanerve:monero.social >__ I'm not expecting it to be notable. I'd use a SATA SSD as a midpoint and ask how many ms it is for 100 * 16 decoy reads (decoys selected per distribution) from the mainnet set.     

> __< j​effro256:monero.social >__ The Blockchain class has bad concurrency but that's a different issue     

> __< k​ayabanerve:matrix.org >__ Regarding the research CCS, I have to reply on the CCS itself but I'll immediately call jeffro256 out for asking for scope creep D:     

> __< k​ayabanerve:matrix.org >__ To be clear, I support the F-S secret variant and was planning to impl the non-F-S variant per the PR, then branch and do the F-S variant for free. Its minimal extra work.     

> __< tevador >__ I'm starting to favor going with the forward-secret version of FCMP++ and adopt the key format for Jamtis.     

> __< k​ayabanerve:matrix.org >__ If tevador is dropping scope creep concerns, I'd be incredibly happy to move forward the F-S variant.     

> __< r​ucknium:monero.social >__ On the FCMP++ Development CCS koe said "I am fine with the current proposal as a valuable research endeavor. Regarding auditing and implementation, I expect it would take 1.5-2.5 years to reach a hardfork after this CCS is complete. Just the multisig integration on its own I expect to be a glacial review/auditing process, and then there are the substantial changes needed to suppor<clipped message     

> __< r​ucknium:monero.social >__ t full-chain reference sets. If Monero had less tech debt, then it would probably be 0.5yr faster."     

> __< r​ucknium:monero.social >__ https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/448#note_24260     

> __< rbrunner >__ Favor over what? Over the non-forward-secret version?     

> __< j​effro256:monero.social >__ If we are going to go with FCMP++ (not saying it's a given at this time) I think we should skip right to the forward secret variant. The jump in complexity compared to doing FCMPs is minimal IMO and uses basically the same cryptography     

> __< tevador >__ Yes, over the non-foward-secret version. The tree proof is the same, they only differ in the GSP.     

> __< k​ayabanerve:matrix.org >__ The one concern is over the usage of a BP+ for spend authorization + linkability (SA+L). It's not a BP+ as in range proof, it's literally 1/64th the work (1/128th for a 2-output TX), but it puts as at half as small a CLSAG, not a quarter as small.     

> __< k​ayabanerve:matrix.org >__ rbrunner: Yes     

> __< rbrunner >__ That would also carry over to a later switch to Seraphis+FCMP, I assume?     

> __< k​ayabanerve:matrix.org >__ tevador: Technically, we need one more PoK of DLog in the first layer in order to output a blinded randomness commitment (and not a randomness commitment).     

> __< k​ayabanerve:matrix.org >__ But effectively, yes. Same principles, same gadgets.     

> __< r​ucknium:monero.social >__ "Forward-secret" in these discussions always means maintaining secrecy even against a theoretical future quantum adversary that can break discrete log cryptography, correct?     

> __< j​effro256:monero.social >__ yes     

> __< k​ayabanerve:matrix.org >__ Rucknium: I define it as an adversary with a discrete log oracle, which a PQ adversary satisfies.     

> __< j​effro256:monero.social >__ Usually assuming the attacker does not have knowledge of your cryptonote/Jamtis public addresses     

> __< k​ayabanerve:matrix.org >__ By showing an adversary with a discrete log oracle can find numbers ('forging' them) for any output to be the output spent, we show you can't find the actual output/the evidence for the found output is worthless (as it could be forged by the adversary).     

> __< tevador >__ Question: how much work would it be to adapt the existing Seraphis codebase to the new key formats?     

> __< k​ayabanerve:matrix.org >__ rbrunner: The first layer changes. Seraphis defines its own SA+L proof. This doesn't develop anything novel though.     

> __< k​ayabanerve:matrix.org >__ It's basically an extra function call to an already defined function.     

> __< r​ucknium:monero.social >__ But prevention of XMR counterfeiting by a quantum adversary is still not possible with any of the options that are being considered, right?     

> __< k​ayabanerve:matrix.org >__ Rucknium: You'd need PQ cryptography for that.     

> __< k​ayabanerve:matrix.org >__ Across the board.     

> __< k​ayabanerve:matrix.org >__ The most we can do now is tevador's prep commentary which extend the time it's safe to migrate from the old system to the theoretical new system.     

> __< tevador >__ I will publish the Jamtis-compat specs this week. It has the same features as Jamtis-Seraphis, but the addresses are backwards compatible with old CryptoNote addresses (or rather CN addresses are forward compatible).     

> __< c​haser:monero.social >__ relevant gist: "Zero-cost post-quantum mitigations for Seraphis" https://gist.github.com/tevador/23a84444df2419dd658cba804bf57f1a     

> __< tevador >__ That means there would be less disruption after the fork (users could still use old addresses).     

> __< j​effro256:monero.social >__ tevador: regarding adapting Seraphis to the new key formats, do you mean supporting an older version of the protocol inside the Seraphis lib, or changing the Seraphis lib to itself use those changed pubkeys in its protocol?     

> __< k​ayabanerve:matrix.org >__ Mind clarifying tevador? I thought the compatible version was 'Jamtis 0.5', with less features yet backwards compatibility.     

> __< k​ayabanerve:matrix.org >__ Are you just referring to not banning old addresses and having two address protocols at the same time?     

> __< tevador >__ The features are the same.     

> __< k​ayabanerve:matrix.org >__ With the two-key address protocol currently defined, you can accomplish all the features of the three-key Jamtis????     

> __< UkoeHB >__ tevador: Janus mitigation?     

> __< tevador >__ It will be clear from the specs. Most features of Jamtis stem from: having multiple DH key exchanges and the OVKs.     

> __< k​ayabanerve:matrix.org >__ So it's defining a new sending protocol over the existing 2-key address definition? 🤔 I'll wait for the gist yet very eager to see.     

> __< tevador >__ I mean, only Jamtis addresses would have the new features. Old addresses would obviously not have them, but they would still work.     

> __< k​ayabanerve:matrix.org >__ That sounds like my comments on F-S/OVKs     

> __< k​ayabanerve:matrix.org >__ Very eager to see.     

> __< tevador >__ Old addresses: no Janus mitigations, no filter-received wallet tier etc.     

> __< k​ayabanerve:matrix.org >__ Also, jeffro256, tevador is interested in the Seraphis codebase yet with FCMP++ replacing the Seraphis protocol (when the Seraphis protocol is concisely defined as its linking tag format)     

> __< tevador >__ But old addresses would still produce forward-secret transactions.     

> __< j​effro256:monero.social >__ tevador: nice. I assume by simply adding another generator component to the onetime address derivation?     

> __< k​ayabanerve:matrix.org >__ Obviously, the modern Seraphis work is a new transaction protocol, a new wallet protocol, so on. It's keeping all of that, yet removing the original basis of the protocol (the enote structure and linking tag definition).     

> __< tevador >__ jeffro: yes, exactly     

> __< k​ayabanerve:matrix.org >__ Changing the address derivation, instead of the address, is a great idea I'm extremely happy to see being explored ^_^ If that enables F-S on old addresses, I'd be amazed and love it.     

> __< rbrunner >__ Are you people just busily adding more possible variants of ways into the future? :)     

> __< k​ayabanerve:matrix.org >__ rbrunner: I can promise my current proposal is still just FCMPs on RingCT     

> __< k​ayabanerve:matrix.org >__ but with forward secrecy     

> __< k​ayabanerve:matrix.org >__ but don't worry there's no wallet changes and that's it, I promise     

> __< k​ayabanerve:matrix.org >__ ;p     

> __< rbrunner >__ Right now I just worry a bit about a possible more complicated decision process what it finally will be.     

> __< rbrunner >__ The more options and variants, the harder to find consensus, maybe.     

> __< tevador >__ The most important advantage of sticking with FCMP++ is that we get one huge anonymity pool that starts with the genesis block.     

> __< k​ayabanerve:matrix.org >__ The JAMTIS evolution which is being discussed would be an amazing upgrade which can be done in a distinct hard fork. I'd likely support doing all of the wallet work in a hard fork after. The PDF I wrote details the minimal deployment plan where we don't do a new TX, the Rust is treated as a black box, and the only wallet change is fetching decoy info -> fetching paths, CLSAG sign to FCMP++ prove.     

> __< rbrunner >__ We had almost 2 years of a lull - "Seraphis will it be" and now we almost have an explosion of options. Surprising.     

> __< o​ne-horse-wagon:monero.social >__ It's really more enhanced options.     

> __< j​effro256:monero.social >__ definitely most of the Jamtis code is reusable, all of the legacy scanning code is reusable, the optimized Pippenger verification code is reusable, and probably some more things that I'm not thinking of rn     

> __< tevador >__ I'm also incorporating the 4-key variant of Jamtis since there was consensus on that. With flexible view tags.     

> __< rbrunner >__ If people can stay on the short addresses if they really want, those even longer addresses probably are not so hard anymore :)     

> __< k​ayabanerve:matrix.org >__ While I can say that makes us appear running all over the place, I'm personally excited about the revolution here, and will reiterate my PDF has a firm actual deployment plan made to be concise. It also seem to has agreement re: developers. This meeting seems to show that I need to tweak it to be the F-S variant, which I am fine with, and that's minimal text changes.     

> __< k​ayabanerve:matrix.org >__ *It, my CCS. Sorry.     

> __< rbrunner >__ We *are* running all over the place, but it may turn out to be worth it, IMHO.     

> __< tevador >__ I think it will stabilize soon.     

> __< k​ayabanerve:monero.social >__ I believe the PDF, noting the F-S variant, is stable.     

> __< k​ayabanerve:monero.social >__ tevador: Clarifying, this is all expected to be a following releasr, right?     

> __< k​ayabanerve:monero.social >__ I would say HF except it doesn't explicitly modify the on-chain protocol.     

> __< k​ayabanerve:monero.social >__ (Though it should be deployed with one)     

> __< tevador >__ We can deploy FCMP++ in one hard fork and then deploy the Seraphis codebase (with new addresses) later.     

> __< j​effro256:monero.social >__ Regardless of the FCMP-RCT *development* CCS proposal, I think we should have a contingency plan for if Seraphis is ready for deployment much sooner than expected, and FCMP-RCT isn't. In that scenario, should we simply go directly for Seraphis, as the stated reason for FCMP-RCT is expected time-to-release?     

> __< j​effro256:monero.social >__ s/development CCS proposal/research CCS proposal     

> __< k​ayabanerve:monero.social >__ I don't believe it relevant?     

> __< j​effro256:monero.social >__ why's that?     

> __< UkoeHB >__ IMO the timeline for Seraphis vs a FCMP-RCT/adjusted-Jamtis is probably the same if we aren't doing a major wallet rewrite (seems likely).     

> __< k​ayabanerve:matrix.org >__ With a decision to not deploy FCMP++s, only two milestones are dropped from the dev CCS.     

> __< k​ayabanerve:matrix.org >__ I believe it's ~15%.     

> __< j​effro256:monero.social >__ I'm talking about what we do with the network protocol     

> __< k​ayabanerve:matrix.org >__ UkoeHB: It's FCMP++ *without* any JAMTIS that I'm proposing.     

> __< k​ayabanerve:matrix.org >__ I don't mind a contingency for that 15%. I'm just noting almost all of the work is still relevant to Seraphis.     

> __< tevador >__ I don't think we should plan to deploy the Seraphis key image format anymore if FCMP++ works.     

> __< j​effro256:monero.social >__ Well yes, sorry I worded it wrong. Regardless of any CCS developments / sunk dev costs anywhere, can we agree that we should *deploy on the network* Seraphis+FCMP if it is ready before/around the same time as FCMP-RCT?     

> __< UkoeHB >__ Yes I'm not pushing against your CCS work. The question is whether to stick with cryptonote key images or continue on to Seraphis, and I think those two are on similar timelines.     

> __< k​ayabanerve:matrix.org >__ If it'll let us move forward, I'll note if the Monero protocol decides to evolve in a way that invalidates the purpose of a milestone in its entirety, then the milestone won't be paid out and the coins yielded to the Research fund? And if the Research fund has a milestone invalidated, those coins would become remaining and part of a MRL fund?     

> __< k​ayabanerve:matrix.org >__ Oh. That's a very distinct discussion jeffro256.     

> __< j​effro256:monero.social >__ tevador: it that because of the privacy implications of the enote migration?     

> __< k​ayabanerve:matrix.org >__ Do we want a unified privacy pool, no migration, no invalidation of addresses or efficiency? That's the question.     

> __< k​ayabanerve:matrix.org >__ The Seraphis first layer is smaller, and the Seraphis SA+L proof is smaller. We'd also have the option of any curve cycle, not any curve cycle with 2**255-19.     

> __< k​ayabanerve:matrix.org >__ That may end up, in total, ~2x faster. That'd be my favorable estimate.     

> __< k​ayabanerve:matrix.org >__ Also, UkoeHB, I didn't even mean to invalidate your timeline estimate. I solely wanted to clarify your timeline estimate noted something not being included at this time. I don't feel you're pushing back at all, and do ack your timeline estimate.     

> __< tevador >__ Yes, the migration has privacy implications and also the disruption to the Monero ecosystem would be much larger if we invalidate old addresses.     

> __< rbrunner >__ That "2 address types in parallel ad infinitum" remains to be seen, I am still a bit sceptical.     

> __< rbrunner >__ This has anyway also potential for confusion.     

> __< k​ayabanerve:matrix.org >__ To be clear, without a breakthrough in how the proof is written, we have 4 PoK DLog proofs in Seraphis FCMPs. In FCMP++s, we have ... 7 PoK DLogs *and* 1 DLog? The reason that alone isn't 50% is because the set membership is the same. If we want a set of at least 4 billion, we need to do 256**4, and that means we need at least 1024 in-circuit multiplications. We can't get below that :/     

> __< r​ucknium:monero.social >__ How would the non-mandatory new addresses work in practice? Would the new wallets have the ability to produce the new and old address versions? But only be able to use OVK features with coins sent to the new addresses?     

> __< k​ayabanerve:matrix.org >__ 1024 + 4 PoK DLogs = ~1640. 1024 + 7 PoK DLogs + DLog = ~2000.     

> __< j​effro256:monero.social >__ New wallets might just want to make the new addresses, so they don't have to scan for enotes to the old format     

> __< r​ucknium:monero.social >__ SegWit addresses took a long time to get adopted in BTC.     

> __< k​ayabanerve:matrix.org >__ It's within the same power of 2, from my napkin math here I'd need to triple check.     

> __< tevador >__ There would be a bit flag set in the Polyseed phrase that determines if the wallet produces old or new addresses.     

> __< rbrunner >__ Sometimes a hard cut and break with the past, even if painful, is better than endless agony, to put it a bit bluntly.     

> __< k​ayabanerve:matrix.org >__ So at best, I'd hope for Seraphis FCMPs (and its SA+L proof) to be 2x faster.     

> __< UkoeHB >__ rbrunner: There is a certain endless agony in the need for backward compatibility.     

> __< rbrunner >__ True.     

> __< k​ayabanerve:matrix.org >__ And sorry, I know that's scattered. I hope my intent gets across.     

> __< k​ayabanerve:matrix.org >__ Also, isn't tevador's proposal for the new addresses to be indistinguishable from old addresses?     

> __< r​ucknium:monero.social >__ rbrunner: I think you may be correct. The lack of mandatory address upgrade means that there is a circular chicken-and-egg problem for adoption: no one creates the addresses since no one send to them, and vice versa.     

> __< k​ayabanerve:matrix.org >__ If we lift all old addresses *and not just internally, yet their communication is identical*, then it's a vastly distinct discussion from Bitcoin SegWit.     

> __< j​effro256:monero.social >__ don't think they can be: they are different sizes     

> __< tevador >__ On-chain, they are indistinguishable.     

> __< k​ayabanerve:matrix.org >__ Oh. On-chain, they're indistinguishable :/ That was my confusion earlier and why I asked about your JAMTIS 0.5 work.     

> __< k​ayabanerve:matrix.org >__ (as that was the off-chain indistinguishable version)     

> __< rbrunner >__ Only think how much confusion those lowly "integrated addresses" sometimes produced ...     

> __< tevador >__ No, old addresses would stay the same, 2 keys and base58.     

> __< k​ayabanerve:matrix.org >__ I am curious how far we can go with off-chain indistinguishability. I believe we may able to do better than prior posited. I'd have to see tevador's proposal and do some further thinking.     

> __< rbrunner >__ And would we get hardware wallets to support two very different address types?     

> __< UkoeHB >__ IMO there is a risk that if FMCP doesn't pan out and we don't migrate to Seraphis key images, we won't see any ring size improvements maybe *ever*. Seraphis gives Grootle proofs as a fall-back.     

> __< k​ayabanerve:matrix.org >__ If we don't do FCMP++s, we definitely should do Seraphis. No question there.     

> __< tevador >__ If FCMP++ doesn't pan out, we can still migrate to Seraphis key images later. But we can't migrate back to the compatible version.     

> __< k​ayabanerve:matrix.org >__ If they do work out, Seraphis theoretically may offer 2x performance, the newer codebase now (not in a follow up deployment), and explicitly migrates addresses (though technically, we can have wallet2 refuse to send to old addresses to force that migration? So that's not unique to Seraphis?)     

> __< tevador >__ There can be a gradual phase-out of old addresses instead of a sudden invalidation.     

> __< k​ayabanerve:matrix.org >__ tevador is correct Seraphis would forever prohibit the unified pool proposal. If the current FCMP proposal is fundamentally flawed, I'd still support Seraphis however.     

> __< UkoeHB >__ The problem comes with implementation. Refactoring the Seraphis library to support a different approach might be a substantial effort, so once you fork it needs to be a solid plan.     

> __< rbrunner >__ Anyway, overall I think nobody finds something that prevents us to at least *start* work on those FCMPs as soon as possible.     

> __< rbrunner >__ Where we will finally end is another question, quite some time in the future.     

> __< r​ucknium:monero.social >__ IMHO, having a unified privacy pool is not a huge benefit because tx outputs turn over so frequently. Maybe there is tech debt reasons to do it, but I don't see a really strong privacy reason if there is a longer delay and/or worse performance with a unified pool.     

> __< o​ne-horse-wagon:monero.social >__ kayabanerve: So what is the next step you need to take to get the FCMP protocol underway today?     

> __< k​ayabanerve:monero.social >__ *Personally*, I am fine waiting to see tevador's address format and continue the discussion next week. We don't need an immediate answer.     

> __< UkoeHB >__ tevador: Are you starting a new gist for Jamtis-C (Jamtis over Cryptonote)?     

> __< k​ayabanerve:matrix.org >__ Merge my CCS?     

> __< tevador >__ Yes, new gist.     

> __< k​ayabanerve:matrix.org >__ Ideally both of them?     

> __< UkoeHB >__ Ok, I will read when you are ready     

> __< k​ayabanerve:matrix.org >__ I'd be really unhappy if I can't start talking to auditors now, cash in hand, and have those slowdowns and bureaucracy.     

> __< k​ayabanerve:matrix.org >__ But there's no technical blockers to my work and I already started the first milestone.     

> __< tevador >__ At least the Development CCS should be merged ASAP.     

> __< rbrunner >__ I mean seems to me nobody is seriously considering anymore a future Monero *without* FCMPs - given they "work out" of course.     

> __< j​effro256:monero.social >__ why development before research?     

> __< r​ucknium:monero.social >__ Can some of the gist links be posted to https://github.com/monero-project/research-lab/issues/100 ? Gists never have memorable URLs.     

> __< k​ayabanerve:matrix.org >__ Immediately after my gist, I started a circuit specification. I had a milestone for the circuit specification, and that become a milestone for a protocol specification per tevadors comments. I then made a PDF detailing various aspects, which I published now for the group's clarity on the work. It's not yet a specification, yet I will edit it to be the specification.     

> __< tevador >__ The "Research" is basically audits.     

> __< j​effro256:monero.social >__ fair     

> __< k​ayabanerve:matrix.org >__ jeffro256: Because the research CCS is actually more auditing than actual research (and proofs for the existing research).     

> __< c​haser:monero.social >__ will do so after the meeting     

> __< k​ayabanerve:matrix.org >__ To be clear, not funding the research CCS impedes us ensuring we're on the right track and not developing components which have difficulty proving/auditing that cause us to use a fallback. It also adds to 'when completed' due to the delays of the bureaucracy :/     

> __< c​haser:monero.social >__ rbrunner: the long-term future of Monero has to be FCMP, one way or another. I can envision ring size increases as short/mid-term temporary stepping stones to improve privacy until we get to FCMP.     

> __< k​ayabanerve:matrix.org >__ To be clear, my specific FCMP proposal may not be the inevitable upgrade to full-chain membership proofs.     

> __< r​ucknium:monero.social >__ You already added two pluses to FCMP. Another proposal will have to be called something else. Three pluses are against the rules AFAIK :P     

> __< a​rticmine:monero.social >__ I agree     

> __< c​haser:monero.social >__ well, we did discuss that this path may have terminal obstacles, e.g. not being able to prove the soundness of GBPs.     

> __< j​effro256:monero.social >__ Just like how valve isn't allowed to make a game with a 3 in its name     

> __< k​ayabanerve:matrix.org >__ No, I've written two alternatives to that.     

> __< k​ayabanerve:matrix.org >__ One 25% slower, one a few times slower.     

> __< k​ayabanerve:matrix.org >__ So there may be terminal obstacles per our current ability, but GBPs alone are not.     

> __< k​ayabanerve:matrix.org >__ Rucknium: I can go back to FCMP+SA+L if that's less wordy and acronymy for you ;)     

> __< c​haser:monero.social >__ got it, I stand corrected (and happily so). what are some actual terminal ones?     

> __< k​ayabanerve:matrix.org >__ And before anyone claims I didn't document those two alternatives, they're both in the PDF. Please read the PDF. It is the comprehensive overview to the proposal.     

> __< r​ucknium:monero.social >__ kayabanerve: Your PDF says that the two alternatives still need security proofs, right?     

> __< k​ayabanerve:matrix.org >__ The GBPs *and* the fallback *and* the fallback's fallback failing.     

> __< k​ayabanerve:matrix.org >__ Yes, all three would need proofs. The second one actually may be quite trivial?     

> __< k​ayabanerve:matrix.org >__ I believe it can be formally argued as a prior proof before the existing Bulletproof.     

> __< c​haser:monero.social >__ having a plan C sounds like a good level of assurance     

> __< k​ayabanerve:monero.social >__ Hm. Matrix.org has stopped sending to monero.social.     

> __< k​ayabanerve:monero.social >__ > Or rather, a prior modification to how the statement is formed, independent of the Bulletproof itself.     

> __< k​ayabanerve:monero.social >__ > If the divisors fail, we fallback to incomplete addition with a window size of 2 (nothing novel, truly already understood, already widely used, 2x slower than divisors for proving DLogs)     

> __< k​ayabanerve:monero.social >__ And no, that 2x wouldn't compound with other things such as the 25% number I'd gave. They share some inefficiencies.     

> __< k​ayabanerve:monero.social >__ So yes, it's definitely meant to be robust.     

> __< k​ayabanerve:matrix.org >__ Or rather, a prior modification to how the statement is formed, independent of the Bulletproof itself.     

> __< k​ayabanerve:matrix.org >__ If the divisors fail, we fallback to incomplete addition with a window size of 2 (nothing novel, truly already understood, already widely used, 2x slower than divisors for proving DLogs)     

> __< k​ayabanerve:monero.social >__ The concern would become performance, not theory, yet I've also worked to dramatically increase performance from my initial Monerokon estimate.     

> __< k​ayabanerve:monero.social >__ Shall we call the meeting here, Rucknium? I'm unsure if there's active conversations and not just whatever will trickle.     

> __< r​ucknium:monero.social >__ Yes, meeting called     

> __< c​haser:monero.social >__ thank you everyone, I really appreciate all this work and coordination that we see here.     

> __< a​rticmine:monero.social >__ Thank you all     

> __< m​rwonderland:tchncs.de >__ I second this! Really appreciate all of your guys work ❤     


# Action History
- Created by: Rucknium | 2024-04-24T12:34:19+00:00
- Closed at: 2024-05-01T20:41:45+00:00
