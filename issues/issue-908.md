---
title: Monero Research Lab Meeting - Wed 11 October 2023, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/908
author: Rucknium
assignees: []
labels: []
created_at: '2023-10-11T14:35:30+00:00'
updated_at: '2023-10-25T15:03:56+00:00'
type: issue
status: closed
closed_at: '2023-10-25T15:03:56+00:00'
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

#905 

# Discussion History
## plowsof | 2023-10-23T12:29:00+00:00
Logs 
> __< Rucknium >__ Meeting in this room in 1.5 hours.     

> __< Rucknium >__ Meeting time! https://github.com/monero-project/meta/issues/908     

> __< Rucknium >__ 1. Greetings     

> __< rbrunner >__ Hello     

> __< v​tnerd:monero.social >__ Hi     

> __< Rucknium >__ 2. Updates. What is everyone working on?     

> __< v​tnerd:monero.social >__ Me: back on subaddressses. No ETA, but been contacted by multiple people about it now, so it's hopefully done soon^tm     

> __< Rucknium >__ me: Writing down some early thoughts about analyzing PocketChange privacy. I also read the Ciphertrace employee's statement for the defense in the Bitcoin Fog case.     

> __< rbrunner >__ Anything really surprising there, in that statement?     

> __< Rucknium >__ Yes. It is interesting to see Chainalysis and Ciphertrace fight. I can discuss in the discussion section.     

> __< Rucknium >__ 3. Discussion. What do we want to discuss?     

> __< rbrunner >__ If nothing else pressing, please do report about that fight :)     

> __< Rucknium >__ Here is the filing from the Ciphertrace employee: https://storage.courtlistener.com/recap/gov.uscourts.dcd.232431/gov.uscourts.dcd.232431.159.1.pdf     

> __< Rucknium >__ This was filed after a short filing from Chaianlysis that responded to some questions by the court. The Chainalysis statement said that their methodology was not peer reviewed and it did not have a defined false positive rate (error rate).     

> __< Rucknium >__ My opinion is that the problems with Chaianlysis's methodology do not mean that blockchain surveillance is completely ineffective (i.e. that bitcoin privacy is "good enough"), but that Chainalysis's methodology is unscientific and unfit for producing the evidence up to the standard of proof in a legal system with strong protections for the accused.     

> __< Rucknium >__ If blockchain surveillance is more scientific, then yes bitcoin still has major privacy problems.     

> __< Rucknium >__ The Ciphertrace filing criticized the lack of false positive rates and Chainalysis's use of expanded change output classification rules. They call it "heuristic 2 (behavioral)", which I guess has some meaning in the original case documents that I have not read.     

> __< Rucknium >__ "Therefore, the discrepancy rate between Ciphertrace and Chainalysis Bitcoin Fog attribution is roughly 67%."     

> __< rbrunner >__ Those pages and pages of documented errors are pretty depressing, and damning.     

> __< Rucknium >__ The filing also has discrepancy rates for other entities like AlphaBay     

> __< rbrunner >__ Found it.     

> __< rbrunner >__ This is a quite rare look into the workings of these companies, right? Probably so far only their customers get such details.     

> __< Rucknium >__ The filing from the Ciphertrace employee says that maybe the defendant (Roman Sterlingov) was accused since he had the only KYC'ed account among all the suspected Bitcoin Fog operator withdrawals.     

> __< rbrunner >__ Did you find any heuristic in there that surprised you personally? That you never heard about, or thought that it would not work well enough?     

> __< Rucknium >__ Consider if the defendant was targeted by a different entity in a different place. Would a dictatorship allow him to review the evidence against him? What about a criminal gang coming to rob him? False accusations are as big of a threat, if not more, to users of transparent coins.     

> __< Rucknium >__ rbrunner: Mostly the filing refers to papers that have been posted publicly. One "new" statement is that Ciphertrace said that they do try to link bitcoin addresses/txs to IP addresses: "Ciphertrace collects IP addresses via our own node operation and links them to bitcoin addresses."     

> __< Rucknium >__ That's not surprising, but I had not seen a public statement from them that this is part of their surveillance     

> __< rbrunner >__ Ok     

> __< rbrunner >__ After reading this diagonally, Ciphertrace looks anyway much more "dangerous" than their competitor there ...     

> __< Rucknium >__ "Blockchain forensics should only be used to generate investigatory leads. Standing alone, they are insufficient as a primary source of evidence. What is striking about this case is the conclusions reached without any corroborating evidence for the blockchain forensics."     

> __< Rucknium >__ My note on Monero real spend classification using tx fungibility defects has a formula for the false positive rate, so I am ahead of Chainalysis in that regard: https://github.com/Rucknium/misc-research/tree/main/Monero-Fungibility-Defect-Classifier/pdf     

> __< rbrunner >__ :)     

> __< Rucknium >__ Ciphertrace was purchased by MasterCard, so their business outlook may be different from Chainalysis now.     

> __< rbrunner >__ Maybe they looked at both before buying and reached a good conclusion     

> __< Rucknium >__ Standards of evidence are going to be different for a court of law and advertising targeting, to take the two extremes.     

> __< rbrunner >__ The court case will go on, based on these filings, I assume?     

> __< Rucknium >__ MasterCard is probably doing regulatory compliance based on risks scores. Maybe some ad targeting too     

> __< Rucknium >__ I guess so. I think the prosecution is pushing for a plea deal like usual, so maybe they are in plea deal negotiations or if the defense thinks their side is strong enough they could take it to an actual trial.     

> __< rbrunner >__ Somehow amazing how all those cryptocurrency funds and ETFs that spring up now risk loss of some of their funds because they turn out to be "dirty"     

> __< rbrunner >__ No wonder MasterCard tries to find something solid     

> __< Rucknium >__ Ironically Ciphretrace has permitted no peer review of their Monero "tracing" methodology. I would have guessed with the Mastercard purchase that they would stop working on it, but IIRC they released a statement at the August 2022 hard fork saying you can run but you can't hide, Monero users.     

> __< Rucknium >__ Anyway, I have been thinking about the privacy impact of users of Monerujo's PocketChange (and any similar system) to split wallet contents into multiple outputs to get around the 10 block lock.     

> __< Rucknium >__ There are two components: privacy before the PC tx and privacy after.     

> __< Rucknium >__ The biggest privacy impact in the post-PC txs would be if transactions consolidate outputs from the PC tx in a single tx later.     

> __< Rucknium >__ You would see two or more rings in the later tx that reference multiple outputs from the original PC tx     

> __< Rucknium >__ So we would want to know how often that ring pattern would occur as a coincidence when a tx actually has nothing to do with a PC tx     

> __< rbrunner >__ I guess such a consolidation can happen quite easily     

> __< Rucknium >__ I think that the false positive rate is going to be a function of the number of txs on the blockchain with more than two outputs, their age, and the decoy selection algorithm.     

> __< Rucknium >__ All roads lead back to the decoy selection algorithm and questions about what wallet2 actually does.     

> __< Rucknium >__ The DSA wasn't very important for the analysis of guessibility of real spends with tx fungibility defects because....well, just because     

> __< rbrunner >__ This consolidation problem does not get smaller if more and more wallets start to implement such a feature, right?     

> __< Rucknium >__ But how densely the DSA selects from certain regions of the output set matters a lot for PC analysis because the probability of selecting multiple outputs from the same exact transaction in a large sea of transactions is going to depend a lot of how big that sea is.     

> __< Rucknium >__ rbrunner: I think if there are more txs with greater than two outputs on chain, then a classification rule that uses multiple outputs from the same tx would have a higher false positive rate. How much more? The math has to be written.     

> __< Rucknium >__ I don't think I will develop the PocketChange analysis much further at this time unless I get a sudden lightning bolt of insight. I would probably put it in a list of possible projects to work on in a CCS later.     

> __< Rucknium >__ Priorities would be set partially based on community input.     

> __< Rucknium >__ I am giving advice to a research group that is planning to recreate the BTC transaction graph with Monero rules. gingeropolous thought it would be a good idea to do that.     

> __< Rucknium >__ A lot of things need to be modified. I am wondering if I am missing anything:     

> __< rbrunner >__ I don't understand. BTC transaction graph with Monero rules - what rules?     

> __< Rucknium >__ You need to eliminate the 10 block lock and even allow child txs within the same block. I guess you could do the idea of referencing by TXID instead out sequential output index     

> __< Rucknium >__ Have a private testnet where you broadcast and confirm the same txs in the BTC blockchain, but with monerod.     

> __< Rucknium >__ tx verification for mining blocks is going to take a very long time. I wonder if there is a way to just turn it off.     

> __< rbrunner >__ Sound a bit crazy, at first read.     

> __< Rucknium >__ They will need a lot of SSD space. I guess 3 TB at least     

> __< Rucknium >__ Why is it crazy?     

> __< rbrunner >__ Maybe I don't understand yet how that could possibly be useful.     

> __< Rucknium >__ You need coin emission to match BTC's emission.     

> __< rbrunner >__ Should this demonstrate that we could handle the same amount of transactions?     

> __< Rucknium >__ There are databases with entity labels on BTC transactions and addresses. Like centralized exchanges. The BTC tx graph can give you the behavioral parameters to simulate what EAE attacks could look like.     

> __< Rucknium >__ The main purpose of doing this would be to analyze the privacy of Monero when you have a ground truth of what an actual tx graph would be.     

> __< Rucknium >__ You would need to eliminate the limit on the number of tx outputs.     

> __< rbrunner >__ You mean you could let loose some heuristics on that new Monero-fied blockchain and then could see exactly how good they were?     

> __< Rucknium >__ Yes     

> __< rbrunner >__ Clever. But probably is anything but trivial.     

> __< rbrunner >__ But already the dropped 10 block limit would disturb things, I guess     

> __< Rucknium >__ Why not just create a simulation in Python or R? There would be pros and cons to doing a simulation. A real blockchain is what the research group wants to do.     

> __< rbrunner >__ So let them research, I would say :)     

> __< Rucknium >__ Methods based on timing analysis wouldn't apply in the exact same way, right.     

> __< Rucknium >__ Right, but I want to warn them if there's things that need to be modified so they are not surprised later.     

> __< rbrunner >__ Good idea. I think mining is no problem, you can easily accept arbitrarily low difficulties.     

> __< rbrunner >__ There is a switch in monerod already I think for that, to create a large blockchain easily     

> __< Rucknium >__ Yes. I pointed them to https://github.com/moneroexamples/private-testnet      

> __< rbrunner >__ Yup, " --fixed-difficulty 100 " as a daemon start flag     

> __< rbrunner >__ Maybe the growth limits of the blocks need to get relaxed     

> __< rbrunner >__ Or even dropped, if you want the same transactions in the same blocks?     

> __< Rucknium >__ We can end the meeting. Let me know if you think of anything major that they would have to modify.     


Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: Rucknium | 2023-10-11T14:35:30+00:00
- Closed at: 2023-10-25T15:03:56+00:00
