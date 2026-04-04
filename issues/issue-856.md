---
title: 'Seraphis wallet workgroup meeting #28 - Monday, 2023-07-03, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/856
author: rbrunner7
assignees: []
labels: []
created_at: '2023-06-30T15:42:10+00:00'
updated_at: '2023-07-03T18:45:50+00:00'
type: issue
status: closed
closed_at: '2023-07-03T18:45:50+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: #850

# Discussion History
## rbrunner7 | 2023-07-03T18:45:50+00:00
````
rbrunner7[m]> Meeting time. Hello! https://github.com/monero-project/meta/issues/856
<dangerousfreedom> Hello
<jeffro256[m]> Howdy
<rbrunner7[m]> 2 weeks since last meeting, with Monerokon in between. Something to report nevertheless?
<dangerousfreedom> This week:.
- I was using jberman[m]  scanner to get the legacy enotes and make the knowledge proofs using them but as far as I understood he built his scanner on the old seraphis_lib (before the the 'mega squash commit') and many files have changed since then. I tried to go through the files but there are so many changes that I got lost. 
jberman[m]  Would be great if you could give us a patch of the scanner in relation to the most updated seraphis_lib or rebase your seraphis_lib_scanner to the seraphis_lib. From my side it would be useful to use it for getting the legacy_enotes from the EnoteStore after you do the scanning.
- I started reading the curve trees paper to understand the concepts related to the full membership proofs. Seems it will be useful in the future.
- Opened [this](https://github.com/seraphis-migration/wallet3/issues/56) since to generate the legacy proofs I can either get it from offline stored information or query the node. Definitely it would be easier for me to query the node and basically copy the code from wallet2. I'm not sure that it is the best approach though. But since these proofs are deprecated it is also not worth to invest so much time/efforts.
<rbrunner7[m]> jeffro256: That `libwallet2_basic` you mentioned shortly before the meeting, is that the extracted wallet reading and writing code?
<jeffro256[m]> Just reading 
<jeffro256[m]> (at least for right now)
<rbrunner7[m]> For migrating we probably won't need more, right?
<rbrunner7[m]> Sounds like you jumped right back into work, dangerousfreedom[m] . Nice :)
<dangerousfreedom> rbrunner7[m]: I'm trying to :)
<jeffro256[m]> Probably won't need more than that. Even if we use the wallet2 engine to construct txs up to a certain fork date, we don't need to store that information persistently in wallet2 format 
<dangerousfreedom> Much more motivated now after the Monerokon
<rbrunner7[m]> Some us us were there, but I would like to report a bit for the benefit of our "silent readers" and people who will read up later
<rbrunner7[m]> Regarding the technological future of Monero and Seraphis, the biggest subject, at least as I experienced it, were certainly "full chain membership proofs"
<rbrunner7[m]> Don't ask me too many details, but such proofs would allow us to get rid of rings and their problems for good
<dangerousfreedom> jeffro256[m]: Are you familiar with the blockchain files? It is a big mystery to me yet how we will start storing the information into files... No work has been done in this direction as far as I know and would be great to store sp txs for example...
<jeffro256[m]> As for the issue here https://github.com/seraphis-migration/wallet3/issues/56, you could create an interface whose implementation maps from output offsets to output pub keys. There could be an "offline" implementation  (your TransactionHistory idea) and an "online" implemention (what wallet2 does now). 
<rbrunner7[m]> kayabanerve has taken the lead on his own initiative and has implemented non-trivial parts of such a system over the course of the last weeks it seems
<rbrunner7[m]> He had a talk at the conference about this, I think the video is already online somewhere
<rbrunner7[m]> He infected a number of people with his enthusiasm :)
<jeffro256[m]> dangerousfreedom[m]: Wdym by "blockchain files"? Are you talking about the LMDB database files?
<dangerousfreedom> Yeah, I thought about it too. I could try to solve this problem for wallet2 already but then I would have to save this information somewhere in the wallet2 files too. Which doesnt seem the best thing to do now, do you think it is worth?
<rbrunner7[m]> dangerousfreedom[m]: Regarding storing Seraphis transaction into the blockchain, IMHO this is still the issue describing it: https://github.com/seraphis-migration/wallet3/issues/7
<dangerousfreedom> jeffro256[m]: > <@jeffro256[m]:libera.chat> > <@dangerousfreedom[m]:libera.chat> jeffro256[m]: Are you familiar with the blockchain files? It is a big mystery to me yet how we will start storing the information into files... No work has been done in this direction as far as I know and would be great to store sp txs for example...
<dangerousfreedom> > 
<dangerousfreedom> > Wdym by "blockchain files"? Are you talking about the LMDB database files?
<dangerousfreedom> Yes. What if we could already play with some basic LMDB files instead of making everything on memory
<dangerousfreedom> I have no idea how it will be done
<jeffro256[m]> The hashchain class stores the "backbone" of the chain (all the block hashes) for wallet2. Defintion here: https://github.com/monero-project/monero/blob/0a1eaf26f9dd6b762c2582ee12603b2a4671c735/src/wallet/wallet2.h#L183
<rbrunner7[m]> We have here a number of quite different things, we have to be careful not to confuse things. If you like, dangerousfreedom[m] , we could clear up some things by talking more about it here on another day this week
<jeffro256[m]> Once you start talking about storing all transaction outputs, you're basically talking about running a pruned node at that point 
<rbrunner7[m]> That does not sound like something that would be useful, and I don't think we need something like that ...
<jeffro256[m]> (or at least storing data in quantities of the same magnitude as a pruned node)
<dangerousfreedom> Haha yeah sorry. I just wanted to start a small discussion of ideas for that point :p
<jeffro256[m]> Yeah there's definitely tradeoffs of caching blockchain information 
<rbrunner7[m]> It would certainly be a good idea to go into detail with more time and care, to reach a common level of understanding of the concepts and the architecture
<rbrunner7[m]> Over time, there were sometimes discussions about turning wallet caches into LMDB files, to better cope with "monster wallets" of some exchanges with purported 10,000 or even 100,000 enotes. Personally I don't think that's a realistic goal, at least not anymore with the complexity that Seraphis brings.
<jeffro256[m]> It could be cool to have to a configurable size blockchain data cache at the wallet side 
<jeffro256[m]> It could potentially save a lot of bandwidth if it was filtered correctly 
<rbrunner7[m]> I think that would be very hard to get foolproof. One word: Reorgs.
<rbrunner7[m]> By the way, still searching for someone who goes into that "single unified tx type encompassing legacy and Seraphis transactions" problem
<jeffro256[m]> That's a bad word take it back
<dangerousfreedom> rbrunner7[m]: What do you mean?
<rbrunner7[m]> shalit[m] tried but ran into some difficulties, and "released" the job again, so to say
<jeffro256[m]> rbrunner7[m]: Oh yeah jberman mentioned that issue to me. I can put that on my medium-term TODO list to see if I can't get that working. I'd imagine this type would only really be used on the wallet side, yeah?
<rbrunner7[m]> Maybe read that issue #7 I linked, I tried to describe the principal problem there
<rbrunner7[m]> Er, no, throughout the code base. That unified tx type would be the one to serialize into the blockchain, be what floats around in the mempool, etc.
<jeffro256[m]> I'd want to be careful passing around that class at the node verification level because there would be an incredible number of combinations of states that that class could take on 
<rbrunner7[m]> So daemon side, and wallet side
<jeffro256[m]> Since we're rewriting this all-encompassing tx type, I want to split the transaction type into a cached and uncached version unlike what we currently have 
<rbrunner7[m]> Well, current thinking is it could be a variant over all the possible tx types, with "visitors" to access them
<jeffro256[m]> For tx caching safety 
<rbrunner7[m]> I am not sure what you mean, but my gut feeling tells me that maybe our ideas are still quite distant from each other
<rbrunner7[m]> Anyway, I would gladly discuss such ideas with you at a convenient time :)
<jeffro256[m]> Because rn there's nothing stopping me from modifying the transaction data and not invaliding the hashes, we just gotta hope that we don't ever use that pattern. However, if you wanted to receive a mutable reference to the underlying transaction data, we could encapsulate this in an outer class and force hash cache invalidation which would be a lot safer 
<jeffro256[m]> Just a nice safety requirement to add to your unified tx type idea 
<jeffro256[m]> Something I've been thinking of adding to cryptonote::transaction but it would require a lot of refactoring
<jberman[m]> Sorry I'm late, no update from me. Working on rebasing to the latest dangerousfreedom[m], getting through the merge conflicts
<dangerousfreedom> jberman[m]: Great! Thank you!!
<rbrunner7[m]> jeffro256: Ok for you to go through my issue in detail, read the few comments there, and then we try to find some quiet time to discuss things together, on a high conceptual level?
<rbrunner7[m]> I think whatever we do with transactions, quite a lot of refactoring will be in the works
<rbrunner7[m]> Just look at the many, many places in code that deal with txs
<jeffro256[m]> rbrunner7[m]: Which issue is it ?
<jeffro256[m]> I’d be happy to btw
<rbrunner7[m]> https://github.com/seraphis-migration/wallet3/issues/7
<rbrunner7[m]> Splendid :) I hang around here.
<rbrunner7[m]> So, anything more for today's meeting?
<rbrunner7[m]> If not, thanks for attending, read you again in 1 week at the latest
````


# Action History
- Created by: rbrunner7 | 2023-06-30T15:42:10+00:00
- Closed at: 2023-07-03T18:45:50+00:00
