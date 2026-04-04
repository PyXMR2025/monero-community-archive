---
title: Monero Research Lab Meeting - Wed 04 January 2023, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/776
author: Rucknium
assignees: []
labels: []
created_at: '2023-01-03T23:05:32+00:00'
updated_at: '2023-01-10T01:17:51+00:00'
type: issue
status: closed
closed_at: '2023-01-10T01:17:51+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2.  Discuss [Jamtis address checksums](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024#64-checksum).

3. Improvements to the decoy selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

4. Seraphis. ( [UkoeHB's Seraphis Proof of Concept work](https://ccs.getmonero.org/proposals/seraphis-wallet-poc-2.html), [Seraphis repo](https://github.com/UkoeHB/Seraphis) ).

5. MRL Meta: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [MoneroResearch.info repository of Monero-related research papers](https://moneroresearch.info/), [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

6. Any other business

7. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#773 

# Discussion History
## UkoeHB | 2023-01-04T18:00:09+00:00
`[01-04-2023 16:59:06] <one-horse-wagon[> Hello.`
`[01-04-2023 17:00:01] <UkoeHB> meeting time https://github.com/monero-project/meta/issues/776`
`[01-04-2023 17:00:02] <UkoeHB> 1. greetings`
`[01-04-2023 17:00:02] <UkoeHB> hello`
`[01-04-2023 17:00:23] <rbrunner> Hi`
`[01-04-2023 17:00:24] <Rucknium[m]> Hi`
`[01-04-2023 17:00:42] <vtnerd> hi`
`[01-04-2023 17:01:33] <tevador> Hi`
`[01-04-2023 17:03:04] <UkoeHB> 2. updates, what's everyone working on?`
`[01-04-2023 17:04:10] <UkoeHB> me: continued cleanup/review of the seraphis lib. I am at least 2/3 done, and finding plenty of things to tweak, optimize, and generally clean up. I also reviewed tevador's updates to the jamtis spec, and his new URI spec (both looking good to me).`
`[01-04-2023 17:04:32] <Rucknium[m]> More data analysis of p2pool outputs. Also looking at tx confirmation latency. And writing responses to isthmus's comments on OSPEAD.`
`[01-04-2023 17:04:52] <tevador> I've been working on Jamtis URI schemes: https://gist.github.com/tevador/500d5d32d5ecc73b56997e12a9d2b20e`
`[01-04-2023 17:05:42] <vtnerd> not much to report again :/ there is a c version of bp++ for reference that will definitely help. otherwise its been doing stuff on other projects or vaca time`
`[01-04-2023 17:05:59] <UkoeHB> also @vtnerd all the seraphis PRs have been updated based on your comments if you want to review again :)`
`[01-04-2023 17:06:31] <vtnerd> yeah will circle back through that list again`
`[01-04-2023 17:06:37] <UkoeHB> thanks`
`[01-04-2023 17:06:49] <tevador> vtnerd: where can I find the C code?`
`[01-04-2023 17:06:59] <one-horse-wagon[> vtnerd: Do you have a reference for that C version?`
`[01-04-2023 17:07:17] <vtnerd> https://github.com/ElementsProject/secp256k1-zkp/pull/207/files`
`[01-04-2023 17:07:52] <one-horse-wagon[> Thanks`
`[01-04-2023 17:08:00] <vtnerd> its written for a different crypto lib so it cant be used directly, but rough numbers can be used and compared against bp (I think)`
`[01-04-2023 17:08:14] <UkoeHB> it's a pretty huge diff for a proof, BP and BP+ are only 1k lines`
`[01-04-2023 17:08:20] <tevador> Thanks. Much more readable than haskell.`
`[01-04-2023 17:08:50] <isthmus> I've just been working on a project to analyze rings that differ by only one ring member https://github.com/Mitchellpkt/ringxor`
`[01-04-2023 17:08:50] <isthmus> That implementation runs in ~O(N^2) and based on benchmarks this will take about a month to exhaustively check ring pairs. However, I have a ~O(N) solution in mind which will probably bring it down to sub-day on a decent machine.`
`[01-04-2023 17:08:50] <isthmus> h/t @rucknium shared a transaction with me that kicked this whole thing off, @neptune is going to help with the data, and @gingeropolous has been helping me get set up on research infra`
`[01-04-2023 17:09:35] <UkoeHB> I guess this one is 1k lines src/modules/bulletproofs/bulletproofs_pp_rangeproof_impl.h`
`[01-04-2023 17:10:50] <UkoeHB> 3. discussion`
`[01-04-2023 17:13:11] <UkoeHB> anything to discuss today?`
`[01-04-2023 17:13:51] <Rucknium[m]> I have number on the bytes added by p2pool coinbase txs. Over Oct-Dec the p2pool coinbases added 23 MB. That's 0.53% of the total bytes added to the blockchain over that period. p2pool found about 7% of blocks.`
`[01-04-2023 17:14:25] <UkoeHB> makes sense`
`[01-04-2023 17:14:47] <Rucknium[m]> p2pool miners would generally have to consolidate the payouts before making them spendable. That would cause X bytes to be added for each ring signature.`
`[01-04-2023 17:15:07] <Rucknium[m]> X is...something that someone could tell me`
`[01-04-2023 17:16:01] <tevador> Nowadays, every tx input has 2-3 p2pool decoys, which stick out like a sore thumb.`
`[01-04-2023 17:16:34] <UkoeHB> should be 640 bytes per input`
`[01-04-2023 17:17:26] <rbrunner> Would it be possible to get a rough estimate how much those consolidations will add to the blockchain?`
`[01-04-2023 17:17:36] <rbrunner> They seem to be much, much heaver at first sight.`
`[01-04-2023 17:17:58] <Rucknium[m]> IMHO, it would make sense to implement a no-coinbase decoy selection algorithm at the same time as (hopefully) the new decoy selection algorithm from OSPEAD is implemented. For implementation simplicity and so not to cause so many "anonymity puddles" in the ring member distributions.`
`[01-04-2023 17:19:13] <Rucknium[m]> rbrunner: Yes. Best way would be to just multiply the number of outputs in each p2pool coinbase tx (which I already have) by 640 bytes. That would be missing the weight of the output side, but that may be ok as  a good approximation`
`[01-04-2023 17:19:15] <UkoeHB> with seraphis binned ref sets you need to select from a contiguous integer range, you'd need to segregate coinbase from normal enotes`
`[01-04-2023 17:20:51] <rbrunner> With this idea, you would spend coinbase enotes with rings that only consist of coinbase stuff?`
`[01-04-2023 17:21:13] <rbrunner> with "a no-coinbase decoy selection algorithm"`
`[01-04-2023 17:21:17] <UkoeHB> you could implement a coinbase consolidation tx type that only allows coinbase inputs without ring signatures and only range proofs on outputs`
`[01-04-2023 17:21:52] <rbrunner> Yes, somehow you must be able to spend coinbase enotes :)`
`[01-04-2023 17:22:19] <UkoeHB> coinbase ownership is largely public information, so consolidating without ring signatures wouldn't necessarily be terrible`
`[01-04-2023 17:23:08] <ghostway[m]> <isthmus> "That implementation runs in ~O(N..." <- That's quite interesting. Can you elaborate if that's okay?`
`[01-04-2023 17:23:13] <Rucknium[m]> With quick calculations, I am getting 373,068,160 bytes from just the inputs/ring sigs on consolidation txs. p2pool had 582,919 payout outputs during this period.`
`[01-04-2023 17:24:21] <tevador> Coinbase consolidations without ring signatures sounds like a reasonable solution.`
`[01-04-2023 17:25:20] <isthmus> Sure @ghostway[m] happy to elaborate, here's what I have in mind:`
`[01-04-2023 17:25:20] <isthmus> I was thinking of it like this: Each output on the chain is a letter. Each ring signature is a word, with the letters [outputs] in chronological order (“ACBDE” –> “ABCDE”).`
`[01-04-2023 17:25:20] <isthmus> We eat the cost once to sort the list of words (rings) lexicographically. Then you make two fast passes over it, one where you compare each ring that starts with the same letter, and then a second pass where you compare against every ring whose first letter is my second letter.`
`[01-04-2023 17:25:20] <isthmus> In other words, Let l_{i,j} be the jth letter of the ith word. The "first letter" pass only compares words x and y if L_{x, 0} = L_{y, 0}. And the “second letter” pass only compares words x and y if L_{x, 0} = L_{y, 1}. Because we’re looking specifically for “differ by one” rings, you don’t need to make any further passes! I think this is kind of a pigeonhole principle thing.`
`[01-04-2023 17:25:20] <isthmus> And the reason this doesn’t subtly become O(N^2) for checks in the passes is because of the initial lexicographical sort (arguably the real magic here). If you’ve got the dictionary open to words that start with F and you want to check against other words that start with F, you already know where they are! You only need to thumb pages until you hit a word starting with an E or a G.`
`[01-04-2023 17:25:42] <rbrunner> According to this total blockchain growth in those 3 months was between 4 and 5 Gigabytes: https://localmonero.co/blocks/stats/blockchain-growth`
`[01-04-2023 17:25:46] <Rucknium[m]> Combining that with the 23 MB from the p2pool coinbase txs, that's 9.2% of all bytes added to the blockchain during this period.`
`[01-04-2023 17:26:15] <rbrunner> Right. 10% only to "digest" those enotes. Hmmm.`
`[01-04-2023 17:26:16] <Rucknium[m]> rbrunner: I have 4,302,893,381 bytes in my data`
`[01-04-2023 17:26:31] <UkoeHB> sgp_: iirc you have been advocating about coinbase enote issues for years`
`[01-04-2023 17:26:44] <ofrnxmr[m]> https://github.com/monero-project/monero/issues/6688#issuecomment-1190753103`
`[01-04-2023 17:26:46] <UkoeHB> sgp[`
`[01-04-2023 17:26:55] <UkoeHB> sgp[m]:  ^`
`[01-04-2023 17:27:02] <ofrnxmr[m]> sgp: `
`[01-04-2023 17:27:44] <gingeropolous> would this be wallet or consensus enforcement?`
`[01-04-2023 17:27:55] <sech1> Coinbase consolidations without ring signatures will also help reduce fees for consolidations which is a problem for small miners`
`[01-04-2023 17:28:14] <ghostway[m]> Cool trick isthmus,, had to guess that it's about ordering :)`
`[01-04-2023 17:28:26] <tevador> that github comment neglects the fact that real p2pool spends are easily recognized in practice`
`[01-04-2023 17:28:53] <ofrnxmr[m]> Agreed`
`[01-04-2023 17:28:57] <rbrunner> But the problem may come back with the binned approach of Seraphis, if we are not careful, do I understand that correctly?`
`[01-04-2023 17:29:05] <Rucknium[m]> gingeropolous: Changes to decoy selection could happen at the wallet level. Changes to allow coinbase outputs to avoid ring sigs would require consensus changes (hard fork) AFAIK.`
`[01-04-2023 17:29:09] <isthmus> ty ghostway[m] ^_^`
`[01-04-2023 17:29:54] <UkoeHB> rbrunner: no, if you want coinbase consolidations then coinbase enotes should be completely segregated from normal enotes (only spendable by consolidating)`
`[01-04-2023 17:30:22] <tevador> lower p2pool consolidation fees would be a big plus for mining decentralization`
`[01-04-2023 17:31:01] <Rucknium[m]> Right. It would also decrease the tx fee that p2pool miners pay for consolidations :)`
`[01-04-2023 17:31:08] <ghostway[m]> isthmus: I thought you had to compare it as a set of the people in the ring though?`
`[01-04-2023 17:32:48] <rbrunner> "with seraphis binned ref sets you need to select from a contiguous integer range": So you number the two types of enotes independently, somehow?`
`[01-04-2023 17:33:05] <UkoeHB> yes, just dump them into two different lists`
`[01-04-2023 17:34:11] <rbrunner> That could possibly have some repercussions in the codebase ... but yeah.`
`[01-04-2023 17:34:36] <UkoeHB> yeah it causes some wallet-side headaches especially`
`[01-04-2023 17:34:57] <UkoeHB> because there is a segregated balance`
`[01-04-2023 17:35:04] <isthmus> Yep, @ghostway[m] when it "compares words x and y" in the analogy that corresponds to taking two different rings and comparing their ring members, to see if they overlap by all but one ring member (in which case it gets marked as a DBO ring pair, otherwise it moves on to the next two rings to compare)`
`[01-04-2023 17:35:30] <isthmus> s/DBO/"differ-by-one"`
`[01-04-2023 17:35:43] <ghostway[m]> That doesn't sound O(N) though...`
`[01-04-2023 17:35:48] <rbrunner> So would probably good to know early if we really start to march into this direction with Monero transactions`
`[01-04-2023 17:36:25] <UkoeHB> ghostway[m]: it should be O(kN)`
`[01-04-2023 17:36:35] <rbrunner> We probably should, wishing for p2pool becoming the largest pool.`
`[01-04-2023 17:36:42] <ghostway[m]> Sure, ok`
`[01-04-2023 17:37:38] <rbrunner> Will probably be the horror to put this into `wallet2` still.`
`[01-04-2023 17:38:01] <UkoeHB> rbrunner: probably better to wait until seraphis`
`[01-04-2023 17:38:32] <ghostway[m]> So maybe wallet3 specification should be there (and also wait for seraphis)`
`[01-04-2023 17:38:34] <UkoeHB> it's also easier with seraphis because membership proofs are separate from ownership proofs`
`[01-04-2023 17:38:34] <ghostway[m]> Yea koe said it`
`[01-04-2023 17:40:11] <rbrunner> Well, yes, dev time going into this with the "old" codebase would probably delay Seraphis`
`[01-04-2023 17:40:13] <Rucknium[m]> rbrunner: I pretty much agree. If nothing is done, then either we believe that p2pool has little chance of getting larger or that we don't care much about effective ring size shrinking.`
`[01-04-2023 17:40:14] <Rucknium[m]> Decoy selection for non-mining users can be changed before Seraphis. Doesn't require a hard fork.`
`[01-04-2023 17:41:34] <Rucknium[m]> Is it hard to exclude coinbase outputs in the old codebase? There is no binning, so you can avoid those issues.`
`[01-04-2023 17:41:45] <rbrunner> And what then for miners? I am a bit confused`
`[01-04-2023 17:42:34] <isthmus> Haha yea +1 @UkoeHB O(kN) better notation than "2 ~O(N) passes". Though to be thorough it is true that *within a given letter* if there are F words starting with the letter 'f' we have to make (F^2-F)/2 checks. It's just that there's a huge number of letters (66921481 at time of writing) and only a handful of words starting with each letter, so those go by very quickly and zooming out it's effectively O(kN)`
`[01-04-2023 17:42:35] <Rucknium[m]> They don't select coinbase outputs as decoys either. They use the coinbase outputs as the real spend :D`
`[01-04-2023 17:42:58] <Rucknium[m]> So coinbase consolidations would be even more obvious than they are now.`
`[01-04-2023 17:43:02] <rbrunner> Ah, ok.`
`[01-04-2023 17:43:02] <moneromoooo> Hard now than coinbases have more than one output. Otherwise, not hard.`
`[01-04-2023 17:44:12] <rbrunner> So that's no contribution against any size saving, just the "nonsense" decoys get avoided, right?`
`[01-04-2023 17:44:41] <Rucknium[m]> Right. To address the privacy issue`
`[01-04-2023 17:44:52] <rbrunner> Ok. I think now I get it.`
`[01-04-2023 17:45:26] <rbrunner> But now the rings that do have coinbase enotes become somewhat nonsensical :)`
`[01-04-2023 17:45:45] <moneromoooo> Actually, probably not too hard, since the node can tell wihch outputs are locked, so it probably has access to the amount, and can thus see which outs are coinbases. `
`[01-04-2023 17:46:14] <sgp[m]> <UkoeHB> "sgp_ (New Account: @sgp:..." <- https://medium.com/@JEhrenhofer/lets-stop-using-coinbase-outputs-da672ca75d43`
`[01-04-2023 17:50:01] <rbrunner> Well, and now, any volunteers to code that ... :)`
`[01-04-2023 17:50:15] <UkoeHB> ok made an MRL issue for comments https://github.com/monero-project/research-lab/issues/108`
`[01-04-2023 17:50:30] <sgp[m]> Initially the focus was that the behavior of users never conceivably spent coinbase outputs, but that's no longer the case. "Normal" people (not just pools) now spend them. It may be tempting to sever these coinbase outputs from the normal decoy set if they grow large, but the benefits are less clear to me`
`[01-04-2023 17:50:36] <UkoeHB> I will let it marinate for 1-2 weeks then implement it in the seraphis lib if there seems to be consensus`
`[01-04-2023 17:50:37] <sgp[m]> Thanks UkoeHB , will review`
`[01-04-2023 17:51:08] <rbrunner> I guess it's less than trivial to put that into the library, for some newcomers?`
`[01-04-2023 17:51:19] <rbrunner> *more`
`[01-04-2023 17:51:34] <UkoeHB> adding coinbase tx type only took around 15hrs I think, this may take a bit more due to balance segregation`
`[01-04-2023 17:51:46] <rbrunner> For you as the author.`
`[01-04-2023 17:52:09] <isthmus> Can they use the current decoy selection algorithm code and reroll on coinbase enotes? Or does that introduce second order effects?`
`[01-04-2023 17:52:10] <UkoeHB> yes a newcomer would take quite a while, since you need to learn how the library is put together`
`[01-04-2023 17:52:36] <isthmus> Ah I think there is a second order effect if the ratio of normal enotes to coinbase enotes is not a constant. And I would NOT assume it to be constant. `
`[01-04-2023 17:52:50] <isthmus> 🤔`
`[01-04-2023 17:53:14] <isthmus> (it'd be OK to re-roll the whole ring. I just mean you can't throw out and re-roll one output)`
`[01-04-2023 17:53:23] <sgp[m]> isthmus: shouldn't be constant since p2pool is a minority of blocks`
`[01-04-2023 17:53:36] * isthmus nods`
`[01-04-2023 17:53:51] <isthmus> Yea that's probably not the right approach then`
`[01-04-2023 17:54:00] * isthmus walks back the suggestion`
`[01-04-2023 17:57:06] <UkoeHB> ok we are approaching the end of the hour, are there any final comments or questions to address?`
`[01-04-2023 17:59:30] <UkoeHB> I'll call it here, thanks for attending everyone`

# Action History
- Created by: Rucknium | 2023-01-03T23:05:32+00:00
- Closed at: 2023-01-10T01:17:51+00:00
