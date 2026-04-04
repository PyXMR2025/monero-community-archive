---
title: 'Seraphis wallet workgroup meeting #37 - Monday, 2023-09-18, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/895
author: rbrunner7
assignees: []
labels: []
created_at: '2023-09-15T14:47:26+00:00'
updated_at: '2023-09-18T18:43:49+00:00'
type: issue
status: closed
closed_at: '2023-09-18T18:43:48+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: https://github.com/monero-project/meta/issues/892

# Discussion History
## rbrunner7 | 2023-09-18T18:43:48+00:00
```
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/895
<d​angerousfreedom> Hello
<r​brunner7> Well ...
<d​angerousfreedom> Well, I wrote a big text for today:
<d​angerousfreedom> I made some perf tests on @jeffro256 implementation of base32 and it is 60% faster than 'mine'. It is also giving the same results when I use it to encode/decode my serialized structs when I use base32 for the knowledge proofs for example. So thank you @jeffro for improving it!
<d​angerousfreedom> I think I finished my [current work](https://github.com/seraphis-migration/monero/pull/1) (just wrote a description there) and I opened a [new CCS](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/409) to continue working on the wallet with the new tasks that came from this one and also some new tasks that I think we could implement now.
<d​angerousfreedom> So basically, in the current CCS, I created the transaction_history component (as simple as I could) where the goal is to store all the relevant information (SpTransactionStoreV1) from transactions made by the wallet and allow the user to efficiently access these information later (to visualize specific info from enotes or generate knowledge proofs for example). For this purpose, 
<d​angerousfreedom> whenever a transaction is created, it is important to store the `JamtisPaymentProposalSelfSendV1` and `JamtisPaymentProposalV1`. I used this component to create the knowledge_proofs (seraphis and legacy) and to visualize enotes.
<d​angerousfreedom> I could not yet fully follow the discussion of the new view_tags (planning to do so in the next couple weeks), but it won't affect this component as just the `PaymentProposal` or the `JamtisDestination` structs would be affected. 
<d​angerousfreedom> In the future CCS:
<d​angerousfreedom> I believe that now I (we) could be able to make a basic but broad demonstrator of seraphis_wallet by opening a wallet, use jberman's scanner to load legacy enotes, make transactions, make transaction proofs, show enotes and balance, close wallet (I would work on the first 3 points of [this](https://github.com/seraphis-migration/wallet3/issues/53) issue. So I opened a CCS to go in  
<d​angerousfreedom> this direction. A lot of work has been done already but not yet fully organized. So the goal is to have this basic but organized demonstrator capable of doing that. The node connection is still a mystery to me. I believe that the biggest challenge (and workload) in my opinion is on the node and the blockchain database itself. Maybe we could list the issues we need to solve in this
<d​angerousfreedom>  direction? I dont feel competent now to work on that but maybe someone more experienced can try to do it?
<d​angerousfreedom> The list with the tasks I foresee is described in the CCS. I would also probably need to change the knowledge_proofs since most probably the view_tags scheme will change (I still need to catch up with the full discussion about it) and there may be some rework to do when looking from the 'terminal' point of view. Also there are points to be improved and new tasks that appeared after 
<d​angerousfreedom> working in the transaction_history. I would like to try to address some of those too and finally will use/review/integrate @shalit's and @ghostway's work on the EnoteStore serialization and key_container.
<d​angerousfreedom> I guess this is it from my side. I apologize for the delay regarding this initial TransactionHistory (as I had an accident and a surgery on the way). I am open for feedbacks and I will be reviewing and cleaning it up in the next 2 weeks, I also need to separate what should be in the PR for the wallet from the PR for the seraphis_lib. This PR also depends on jeffro's work (basic_wallet
<d​angerousfreedom> and base32 (that's why it is failing the compiler tests)) so we need to merge them before I can merge my PR so it would be cleaner. Meanwhile I will keep the PR as a draft. In the next two weeks I will also be collecting ideas and structuring my next work. I will have a bigger time budget too from October on so I plan to catch up with the exciting discussion about the view_tags
<d​angerousfreedom> and others. Really nice to see the proposal for a dynamic view_tag, I just superficially looked at it but looking forward to understand it in more depth :)
<r​brunner7> Alright, thanks, just scanned it. This will develop further quickly now, right? Looks like you went (back) to work on Seraphis in earnest.
<j​berman> Update: working through merge conflicts on background sync in the main repo still (unfortunately this is dragging way longer than I had hoped), and also wrote a bank-of-the-envelope script to calculate the amount of data a light wallet would need to download in order to construct txs with full chain membership proofs here: https://paste.debian.net/1292373/
<d​angerousfreedom> Yeah, I will have more time from October on and my arm is getting better so yeah :)
<r​brunner7> Nice to hear.
<g​hostway> Hello
<j​berman> Context: to construct a full chain membership proof, a wallet needs the path in the merkle tree to the user's received enote. A user can either download the entire merkle tree, or just paths to their view tag matches, or just their path + decoy paths in order to avoid revealing which enote is theirs to a light wallet server. Assuming 100m enotes, according to my rough and not-yet-
<j​berman> reviewed calculations, it's ~21kb for a single merkle path, ~3.2gb for the entire merkle tree, and ~1.6gb for branches of view tag matched enotes alone. If those are right, this is why light wallets would sensibly be expected to download "decoy" merkle paths in order to constrct a tx is to avoid needing to download >1gb of data to sync on restore
<r​brunner7> Because say 40 kb instead of 20 or so is still ok?
<g​hostway> Hm, why 21kb for a single merkle path? D~=4 iirc?
<g​hostway> Do you mean with the proofs?
<r​brunner7> Ah, ok, that's per enote
<j​berman> a wallet will currently download 10+ mb to fetch the current distribution of outputs in the chain to select decoys, so we can fetch a lot of decoy paths to match that if we wanted
<r​brunner7> Interesting
<j​berman> ghostway:  see the script
<j​berman> that was for a single path
<j​berman> width * depth = 4 * 167, would need each layer in the path, I believe
<r​brunner7> Is this part of studying the feasibility?
<g​hostway> I think I talked with kayaba some time ago about this, but I don't remember anymore
<d​angerousfreedom> I roughly understand the idea but is it already proven that the FCMP is cryptographic solid?
<d​angerousfreedom> For Monero, I mean
<j​berman> rbrunner7: studying feasibility + also helping assess the view tag impl/final address scheme. I commented referencing this calc in response to jeffro256 's proposal for 1 or 2 byte view tags
<r​brunner7> For those who do not follow closely: @tevador and jeffro256 and sometimes UkoeHB have a still ongoing very lively discussion about modifications to Jamtis for better privacy in connection with 3rd party scanners.
<r​brunner7> I hope this will "converge" in the near to middle future.
<j​berman> not sure in what sense you're asking if it's solid danger, but I would say no not yet just to be on the cautious side answering that q
<r​brunner7> Well, it's not a big gamble, I hope the educated guess is that it's solid, but proofs are needed of course
<j​berman> would say the same for Seraphis as well
<r​brunner7> :)
<d​angerousfreedom> There was the curve discussion that we could not use Ed25519 and had to look for another one... I'm a bit lost about what is the main theoretical challenge now or if everything was solved and now is just a matter of implementation
<g​hostway> If someone has found a curve cycle with ed25519, it's ok
<g​hostway> I think tevador talked about it, no?
<s​halit> Hello
<r​brunner7> I hope Matrix is right and jberman really is still typing :)
<j​berman> kayabanerve: can give a more detailed probably more accurate answer, but my take as to the latest: kayaba has implemented proving and verifying reasonably efficient fcmp's in rust (https://github.com/kayabaNerve/full-chain-membership-proofs/). the impl relies on curve trees. kayaba posits that Seraphis should move to a curve cycle for perf reasons here: https://gist.github.com/kayabaNerve/97441ad851dc6e4d2a0b699f58a004f2 . There is still ongoing discussion surrounding this, but generally I think it's sensible to move forward working on implementing kayab's fcmp's in the Seraphis impl to have a stronger basis for discussion on how it would impact Seraphis (e.g. as discussed above as it relates to the light wallet tier). As far as theoretical research goes:
<j​berman> we still need to prove the foundation of Seraphis with security proofs and audits, then we could move on to hardened theoretical research on fcmp's (or try to continue on both in parallel)
<r​brunner7> Well, the most interesting immediate point is maybe how much of the already existing Seraphis library and related crypto stuff this will likely invalidate, or: How far any curve switching stuff will throw us back.
<r​brunner7> But anyway, research and discussion is ongoing, as you said :)
<r​brunner7> Ok, anything else for this meeting? I reviewed the Base32 PR from jeffro256 , and he revised based on that. Have yet to check the changes, but I think this is close to mergeable already.
<r​brunner7> That's this here: https://github.com/seraphis-migration/monero/pull/6
<r​brunner7> Alright, seems that's it for today. Thanks for attending, read you again next week at the latest!
<d​angerousfreedom> Thanks for the answer. It's a pretty big rabbit hole looking at the issues there :p
```

# Action History
- Created by: rbrunner7 | 2023-09-15T14:47:26+00:00
- Closed at: 2023-09-18T18:43:48+00:00
