---
title: Monero Research Lab Meeting - Wed 20 May 2026, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1393
author: Rucknium
assignees: []
labels: []
created_at: '2026-05-20T14:46:07+00:00'
updated_at: '2026-06-08T20:24:43+00:00'
type: issue
status: closed
closed_at: '2026-06-08T20:24:43+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Live log: https://libera.monerologs.net/monero-research-lab

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Post-quantum encryption](https://github.com/monero-project/research-lab/issues/151#issuecomment-4412416686).

4. [FCMP beta stressnet](https://github.com/seraphis-migration/monero/releases/).

5. [CCS proposal: ProbeLab P2P Network Metrics Proposal](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/667).

6. Any other business

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1388 

# Discussion History
## Rucknium | 2026-06-08T20:24:39+00:00
Logs


> __< rucknium >__ Meeting time! https://github.com/monero-project/meta/issues/1393     

> __< rucknium >__ 1. Greetings     

> __< tevador >__ Hi     

> __< jberman >__ waves     

> __< boog900 >__ Hi     

> __< UkoeHB >__ Hi     

> __< jpk68:matrix.org >__ Hello     

> __< rbrunner >__ Hello     

> __< vtnerd >__ Hi      

> __< rucknium >__ 2. Updates. What is everyone working on?     

> __< jeffro256 >__ Howdy      

> __< jberman >__ Beta stressnet debugging and working with jeffro256 on resolving a beta net specific consensus issue     

> __< jeffro256 >__ ^ Same      

> __< rucknium >__ me: Keeping stressnet stressed and monitored. Reviewing monerosim version 0.1.0     

> __< rbrunner >__ Still Polyseed in the Monero core software     

> __< vtnerd >__ Me: updating various prs in monerod and lws. Moving back to looking at serialization limits and block size again shortly      

> __< rucknium >__ 3. Post-quantum encryption (https://github.com/monero-project/research-lab/issues/151#issuecomment-4412416686).     

> __< tevador >__ I have no updates, I'm still going with AC1024 as discussed in the last meeting. I can answer questions if needed.     

> __< syntheticbird >__ Hi     

> __< rucknium >__ I thought more about having an interactive address option. I think some merchants have problems with non-interactive txs. Or you could say that they are accustomed to the "pull" procedure of digital fiat payments, but cryptocurrency txs are "push". In previous research, I found this set of complaints about accepting cryptocurr [... too long, see https://mrelay.p2pool.observer/e/nIrw_oQLU1NOeXQ5 ]     

> __< rucknium >__ Just some thoughts on UX. Or DX (developer experience) maybe.     

> __< rucknium >__ ^ AFAIK, that site blocks Tor. And I cannot get archive.org to work right now :(     

> __< tevador >__ I think that interactive transactions could be an option, but not the only option. There are use cases for non-interactive transfers.      

> __< rucknium >__ That reminds me that the Tor Project is running a cryptocurrency donation campaign for some internet privacy tools, including ones that are useful for research. I used OnionShare to collect user-submitted monerod logs, for example. The donation link appears in the blank page of the newest version of Tor Browser: https://internetfreedom.torproject.org/     

> __< rucknium >__ They accept XMR. Donations are being matched by Cake Wallet and Zcash Community Grants, plus some smaller donors.     

> __< rucknium >__ tevador: I agree. Not the only option. I just wanted to say that an optional interactive protocol could have some UX/DX advantages.     

> __< tevador >__ Yes, I'm still planning to include an interactive protocol in the appendix of Jamtis.     

> __< rucknium >__ 👍     

> __< tevador >__ In response to spirobel, for point 2, you cannot just pretend that passively posted donation addresses don't exist. They do and we are not going to discontinue that use case.     

> __< tevador >__ This is a response to: https://libera.monerologs.net/monero-research-lab/20260519#c677589     

> __< rucknium >__ Here was point 2: > <spirobel:kernal.eu> tevador: https://libera.monerologs.net/monero-research-lab/20260518#c677439     

> __< rucknium >__ > 2.the one-to-many "donation address" use case:     

> __< rucknium >__ > for this case the status quo is that we have systems like kuno, ccs, xmrchat.     

> __< rucknium >__ > there is a need for the group to see a donation counter go up.[... more lines follow, see https://mrelay.p2pool.observer/e/rcqJ_4QLX0kyemE4 ]     

> __< sgp_ >__ I agree passive donation addresses are important     

> __< rucknium >__ More discussion about PQ addressing?     

> __< rucknium >__ 4. FCMP beta stressnet (https://github.com/seraphis-migration/monero/releases/).     

> __< rucknium >__ This week we got above the 5MB block size ceiling, as predicted. To 6MB blocks :)     

> __< rucknium >__ https://stressnetnode1.redteam.cash/     

> __< rucknium >__ I also set up an alt chain visualizer because we needed it this week: https://stressnetconsensus1.redteam.cash/ https://stressnetconsensus2.redteam.cash/     

> __< rucknium >__ The same app code as for mainnet, adjusted a little for stressnet.     

> __< jberman >__ Modifying the long term window in the dynamic scaling algo to kick in at 2 weeks instead of the current 100k block window unfortunately triggered a consensus issue that's leading to a number of syncing problems / chain splits. After some rounds trying to resolve the issue cleanly, it seems the most efficient option on the table to proceed is to essentially restart the stressnet     

> __< jeffro256 >__ After a lot of discussion with j-berman, I think that it is decided that we are going to rollback the stressnet for the beta v2.0 release due to the grossness of the consensus break. I am going to put out a PR which clears the blockchain if using a previous version of the beta stressnet, merge in the LTM window cache size fix, [... too long, see https://mrelay.p2pool.observer/e/jeyo_4QLam01TTAy ]     

> __< rucknium >__ That sounds fine to me     

> __< rbrunner >__ So more or less one off-by-one bug, and stressnet broke down? Really shows the importance of code reviews :)     

> __< spirobel:kernal.eu >__ tevador: just to clarify: i am not for discontinuing the use case. its just that if someone wants this functionality, they have to continue to scan the whole chain. also again: my suggestion is non interactive.      

> __< jberman >__ It's worth noting this isn't an issue that would have affected mainnet, nor an issue with the updated scaling implementation proposed for FCMP++. It was strictly an issue with the stressnet specific change that would only affect stressnet to decrease the LT window so the chain could grow faster and get stressed faster on stressnet     

> __< rbrunner >__ Somehow missed that crucial detail, thanks for clarifying!     

> __< spirobel:kernal.eu >__ regarding the PQ addressing small addition: it would be good to have it as a separate document from jamtis and it shouldnt take up most of the space regarding addressing design choices. the discussion should be more focused on ux problems in the real world and how we can reduce scan time.  > <rucknium> More discussion about PQ addressing?     

> __< rucknium >__ The intended use of the new stressnet node is to just swap the old monerod out and start running the new one without deleting the old stressnet blockchain?     

> __< jberman >__ Ya basically just a smooth path for people upgrading to not have to manage deleting their db manually     

> __< rucknium >__ That would skip the long testnet sync from scratch :)     

> __< rbrunner >__ So basically one big reorg back to start of stressnet?     

> __< rbrunner >__ Dropping blocks like crazy :)     

> __< jberman >__ Ah sorry, I misinterpreted your message. No, it would actually delete the old stressent db, so it would re-sync from scratch     

> __< jberman >__ Unfortunately popping blocks needs an overhaul to be faster than just re-syncing     

> __< rbrunner >__ ... on testnet     

> __< jpk68:matrix.org >__ spirobel:kernal.eu: Why shift the focus even further away from the non-interactive side of the protocol? This seems like a needlessly large UX change with no apparent benefit     

> __< jeffro256 >__ For reference , my stressnet node wasn't even able to pop 100 blocks per hour on my older desktop computer, so we figured it would be literally faster to just clear the entire DB and re-sync from scratch     

> __< rucknium >__ pop blocks is very useful, but not when blocks are large.     

> __< rucknium >__ IIRC, BTC doesn't have an easy-to-use pop_blocks command.     

> __< rbrunner >__ That somehow sounds strange. I remember dropping blocks quickly. Really that much of a difference if they are large? Or maybe slower since FCMP?     

> __< rbrunner >__ (dropping blocks quite in general, years ago)     

> __< spirobel:kernal.eu >__ jpk68:matrix.org: i clarified earlier my approach is non interactive. further context: https://xcancel.com/spirobel/status/2020868563532382583#m and two more MRL messages ...      

> __< jeffro256 >__ Yeah, it's not a FCMP++-specific issue, but FCMP++ really doesn't help for popping blocks: https://github.com/monero-project/monero/issues/10207     

> __< jeffro256 >__ Especially when each block is >6MB     

> __< rbrunner >__ Ah, I see, I was dropping manually using one of the extra tools beside monerod     

> __< rbrunner >__ Which of course didn't put anything back into the pool     

> __< spirobel:kernal.eu >__ jpk68:matrix.org: https://mrelay.p2pool.observer/e/gIrIw4QLRzMzb2VC maybe i should turn this whole thing into a gist ... just to be clear i dont like interactive protocols ... where both parties have to be online at the same time.      

> __< rbrunner >__ monero-blockchain-export     

> __< rbrunner >__ --pop-blocks     

> __< rucknium >__ At one point, there were 9 orphaned blocks produced for the same block height. Was that caused directly be the consensus bug? It was a sight to behold.     

> __< jeffro256 >__ lol probably      

> __< rucknium >__ Did we have progress on the other stressnet issues?     

> __< rucknium >__ https://mrelay.p2pool.observer/m/monero.social/gYZDLUYFleUqMRKiFOSBRoOD.png (consensus-breakdown.png)     

> __< rucknium >__ ^ Here was the set of orphan blocks on https://stressnetconsensus1.redteam.cash/     

> __< rbrunner >__ Cool     

> __< rucknium >__ Can IRC side see images?     

> __< rbrunner >__ There is a link that works     

> __< rbrunner >__ (But might expire after some time, I guess)     

> __< rucknium >__ Thanks, DataHoarder[m] , for working IRC image links :)     

> __< jberman >__ Slight progress on impaired node connectivity after deep reorgs, and jeffro also made solid progress on 1) faster wallet loading when the pool is large, and 2) improved fix to unrestricted RPC when the pool is large > <rucknium> Did we have progress on the other stressnet issues?     

> __< jberman >__ The consensus issue has unfortunately taken up a solid amount of time     

> __< rucknium >__ Nice     

> __< rucknium >__ I mean nice to your first message     

> __< rucknium >__ After the meeting I will shut down my stressnet monitors while I re-sync testnet     

> __< rucknium >__ Any other discussion about stressnet?     

> __< jberman >__ Nothing from me     

> __< spirobel:kernal.eu >__ jpk68:matrix.org: the apparent benefit is that you dont have to sync wallets anymore.     

> __< rucknium >__ 5. CCS proposal: ProbeLab P2P Network Metrics Proposal (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/667).     

> __< rucknium >__ yiannisbot:matrix.org said he would arrive to the meeting at 18:00 UTC. In 6 minutes.     

> __< yiannisbot:matrix.org >__ Hi everyone, I'm here :)      

> __< yiannisbot:matrix.org >__ The general feeling of the community seems to be that we skip Milestone 1 and focus on Milestone 2. We won't only count unreachable nodes, but try to find better heuristics and derive insights that would help identify spy nodes and blockchain surveillance companies. We will also spend some time to investigate if POW systems wo [... too long, see https://mrelay.p2pool.observer/e/sP21gIULNmpoZmxz ]     

> __< yiannisbot:matrix.org >__ Does that sound like a good summary? We plan to update the proposal issue to reflect these new directions. Any extra feedback is more than welcome as we try to shape up the final version.      

> __< yiannisbot:matrix.org >__ rucknium:monero.social: plowsof what's your take and suggestions for next steps?     

> __< rucknium >__ That sounds good to me. Right, I think one would use monerosim when you are ready to actually implement a feature into the monerod C++ codebase. Initial research on the viability of a PoW approach would come before that.     

> __< rucknium >__ boog900:monero.social had some recent thoughts about spy node countermeasure that he may want to post here.     

> __< yiannisbot:matrix.org >__ Exactly. So if while doing the study we come up or identify a previously proposed approach that looks attractive, we can then port it into monerosim.     

> __< rucknium >__ More comments on this item? (I see someone typing)     

> __< vtnerd >__ For #2 (unreachable nodes) you kind of have to do the work if #1 anyway? Just no fancy dashboard?     

> __< boog900 >__ I had an idea on how we could prove nodes were not making too many outbound connections but it would require something like proof of storage. If we could do that though then we might be able to allow stemming to inbound connections, which would increase the stem graph and remove the privacy leak when nodes don't allow inbound.     

> __< yiannisbot:matrix.org >__ Yeah, kind of. That's why we included it as a first item/milestone. But given M1 is not desired we'll do just what is needed to be able to get to M2.     

> __< boog900 >__ It's pretty cheap to tag on with proof of storage though     

> __< rucknium >__ To get unreachable nodes, you take a different approach. You have to passively wait for nodes to connect to you. To get reachable nodes, you can just crawl rapidly through peer lists, connecting briefly to each reachable node. To get the ratio of reachable to unreachable, of course, you would do both.     

> __< rucknium >__ Or there may be a smarter way to get unreachable node count, but I don't know of one.     

> __< vtnerd >__ the primary value of unreachable node estimation is in d++ privacy related. Is that the consensus? Because funding the research for that makes sense     

> __< yiannisbot:matrix.org >__ vtnerd: Agreed, but to me that would be the natural next step.     

> __< rucknium >__ vtnerd:monero.social: Yes     

> __< yiannisbot:matrix.org >__ boog900: That's a good approach. We'll take this into account as we revise the methodology for Milestone 2.      

> __< boog900 >__ I feel Milestone 2's scope is getting large.     

> __< rucknium >__ Paraphrasing, the D++ papers said that unreachable nodes don't play a large role in the network, so they are ignored in the analysis. We could show that unreachable nodes do play a big role in the network, at least by the number of nodes.     

> __< rucknium >__ I am trying to find the quote. They don't use the term "unreachable"     

> __< rucknium >__ Can't find it at the moment.     

> __< rucknium >__ We can end the meeting here. Thanks everyone.     

> __< yiannisbot:matrix.org >__ Thanks. We'll be back next week with an updated proposal for Milestone 2 and hope to make progress from there.      

> __< tevador >__ spirobel: Your twitter post is too vague to properly judge the proposal. You should post a more detailed write-up, with all the keys and derivations, what constitutes an address, what is included on-chain and what must be shared off-chain.     

> __< tevador >__ I'm suspecting that in the process of writing it down, you will identify several issues.     

> __< spirobel:kernal.eu >__ tevador it is good enough to judge the core idea. no i don't think there is an issue with this. its a fairly clear idea     

> __< spirobel:kernal.eu >__ i will turn it into gist when i have more time      

> __< tevador >__ It's not clear to me. One paragraph says the sender includes an index verbatim, one paragraph says the sender increments an index and one paragraph says the sender fills part of the index with random data.     

> __< spirobel:kernal.eu >__ or write a prototype ...  do a kdf on the wallet seed and put it into the address ...  put the secret into the place where the dummy payment id is now      

> __< spirobel:kernal.eu >__ then only scan transactions that contain this secret in the dummy id      

> __< tevador >__ But that's a serious privacy regression. Any external observer can see the same pid repeating and can conclude that those two outputs are owned by the same party.     

> __< spirobel:kernal.eu >__ tevador ... yes because this works for only one tx, so after that this secret index needs to be incremented      

> __< tevador >__ That doesn't solve anything, the external observer can identify (pid, pid+1) just as easily as (pid, pid)     

> __< spirobel:kernal.eu >__ no it cant.  because after the initial transaction the channel is open and we can obviously "increment" it in away the channel observer wont know     

> __< tevador >__ Ah, so your proposal requires a secret channel between the sender and receiver. OK, in that case we don't actually need addresses, the receiver can just construct their own outputs every time.     

> __< spirobel:kernal.eu >__ and the point is: you find the channel opening ... and then you can find all others ... that where sent with this participant      

> __< spirobel:kernal.eu >__ no wallet syncing anymore      

> __< spirobel:kernal.eu >__ and just to be clear: by channel i mean this in the simplest way, just some ecdh with the viewkey in the address and just say: this is the next secret for the next transaction. then you can find it as easily as the first but the observer wont know. thats what i mean by increment      

> __< spirobel:kernal.eu >__ used the word channel because i had hedy lamarrs frequency hoping technique in mind, but its not some interactive off chain connection      

> __< spirobel:kernal.eu >__ so you can reconstruct the first secret from seed and you get all the others afterwards as the next "index" is always embedded in encrypted form in the transaction       

> __< tevador >__ Does it allow for stateless address generation? Probably not. You'd have to keep track of issued 'view keys' and never reuse the same key for two recipients (even if they don't send you anything). And you still have to scan, at least for the first transaction in every channel.     

> __< spirobel:kernal.eu >__ do subaddresses allow for stateless address generation? no we increment the subaddress index.  " never reuse the same key for two recipients " exactly what we recommend now for subaddresses ...      

> __< tevador >__ Jamtis does allow for stateless address generation.     

> __< spirobel:kernal.eu >__ and scanning for open channels: no. the expensive part is the cpu work ... and even if we were to still to do all the network fetching (which is not necessary, as this secret is similar to a txhash an "index" in the sense of a database index, so we can retrieve just what we want. its just a matter of in the case of remote node [... too long, see https://mrelay.p2pool.observer/e/zYKsgoULTVN4M0RS ]     

> __< tevador >__ It could probably work if the channel opening transaction included the original index. But at least the sender is always stateful. If they ever forget how many transactions they have sent, repeated 'view tags' will appear in the blockchain.     

> __< tevador >__ spirobel: you can't have stateless address generation that supports "index lookup" because you don't know which addresses exist.     

> __< spirobel:kernal.eu >__ yes i dont see statefulness as a big issue. wallets have to do this in practice. statefulness is cheap compared to having to scan every single transaction everyone is sending all the time      

> __< spirobel:kernal.eu >__ and also for logical reasons: if you want to compartmentalize your identity you have to make different identifiers for the people you interact with in any case      

> __< tevador >__ Stateful addresses get you issues like this: https://github.com/monero-project/monero/issues/8138     

> __< spirobel:kernal.eu >__ but that is an engineering issue. because wallet2.cpp sometimes left gaps ... in my wallet library i increment the index for every address generated      

> __< tevador >__ And how do you know the value of the index when restoring from a seed?     

> __< spirobel:kernal.eu >__ this whole lookahead thing is clunky ... also statelessness is not worth the price ... we can literally do away with scanning entirely ... which is a much practical step towards scaling than something like tachyon (which needs to update a proof constantly to be able to spend, different topic, but shows the different directions here ...)      

> __< spirobel:kernal.eu >__ "And how do you know the value of the index when restoring from a seed?" you would know how many addresses you generated ... you can easily just make 100000. just call the kdf make the  secret ask the node if there where txs for these ... just a database lookup     

> __< spirobel:kernal.eu >__ and the incremented indeces per participant only come into play if a tx was found ... if that is the case its easy ... because the info is in the tx      

> __< spirobel:kernal.eu >__ alright its getting late here I am getting sleepy. has been fun chatting with you cya      

> __< DataHoarder >__ <rucknium> Can IRC side see images? > 19:47:26 <rbrunner> There is a link that works > 19:47:58 <rbrunner> (But might expire after some time, I guess)     

> __< DataHoarder >__ the links won't expire unless the content is deleted on the matrix side     

> __< DataHoarder >__ and bridge stays up, it mainly proxies the authenticated call 1:1     



# Action History
- Created by: Rucknium | 2026-05-20T14:46:07+00:00
- Closed at: 2026-06-08T20:24:43+00:00
