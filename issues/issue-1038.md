---
title: 'Seraphis wallet workgroup meeting #78 - Monday, 2024-07-15, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1038
author: rbrunner7
assignees: []
labels: []
created_at: '2024-07-12T16:49:24+00:00'
updated_at: '2024-07-15T19:05:17+00:00'
type: issue
status: closed
closed_at: '2024-07-15T19:05:17+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: https://github.com/monero-project/meta/issues/1035

# Discussion History
## rbrunner7 | 2024-07-15T19:05:17+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1038
<s​needlewoods> hello
<jberman> *waves*
<d​angerousfreedom> Hello
<k​ayabanerve> *waves*
<j​effro256> howdy
<r​brunner7> Nice to have you here, it's not yet the big summer lull :)
<r​brunner7> What is there to report from last week?
<d​angerousfreedom> Sorry, I was basically three weeks away but will work full-time in the next 4 weeks. Lately, things happened very fast in Monero, as usual, so my immediate goal is to give my work some unity and do something that makes sense.
<d​angerousfreedom> AFAIK, SNeedlewoods  is putting a lot of efforts in making the API independent from the wallet2, is that correct? What is the goal here? Have a modular wallet, as similiar as possible to wallet2? So it would be easier to integrate all the upcoming updates (enote-scanner, fcmp, etc)? 
<d​angerousfreedom> I guess jberman  and jeffro256  are very busy with the structural part of the protocol since many things changed lately and the wallet is not the priority for them now, right?
<d​angerousfreedom> From my side, I am still figuring out what makes sense to do (after these 3 weeks break which in one hand made me forget some stuff and on the other hand the project evolved). Does it still make sense to base my new wallet on the koe/seraphis_lib? Will the enote scheme be updated by jeffro256  or the plan is to use kayabanerve  library somehow (if it is already possible to create
<d​angerousfreedom> txs under the new scheme in C++)? Does anyone have an idea or can foresee how a protowallet would look like if we put all the pieces that we are building together? AFAIU from @rbrunner posts, building a new wallet is still relevant and we are using the seraphis_lib for that, right? So I will continue in the direction that I wrote in my last CCS and I will be talking to jeffro and
<d​angerousfreedom> jberman to see how the blockchain integration is going and what I can do to help them. This is what makes more sense to me now. What do you think?
<j​effro256> me: Jamtis RCT library support for legacy addresses is almost complete
<j​effro256> there were a lot of kinks to iron out
<jberman> me: started on the migration of cryptonote outputs into the merkle tree
<jberman>  "I guess jberman  and jeffro256  are very busy with the structural part of the protocol since many things changed lately and the wallet is not the priority for them now, right?" -> that's correct on my end, been basically exclusively focused on fcmp integration
<s​needlewoods> Still working on the API, but due to many distractions not as far done as I'd like to be.
<k​ayabanerve:matrix.org> The plan is still wallet2 for the initial FCMP++ fork AFAIK.
<r​brunner7> "The plan is still wallet2 for the initial FCMP++ fork AFAIK." Well, I opined in my last wiki entry that we should try to avoid that, and try to go into that already with the new wallet. But I did not hear any feedback regarding that particular point. Opinions?
<j​effro256> > I guess  jberman (@jberman) and  jeffro256 are very busy with the structural part of the protocol
<j​effro256> To be clear, I'm not working on the FCMP++ consensus protocol at the moment, just the addressing protocol. But once I'm done with that, I'd be happy to help with FCMP++ if @jberman or @kayabanerve can find anything for me to do integration-wise
<j​effro256> I agree. We should try to write the FCMP++ scanning code as completely independent from wallet2 as possible, and then tie it in modularly if we still have wallet2 by that time
<d​angerousfreedom> How would the enote_scanner be integrated in that case?
<jberman> once the tree is done, sections 6.9 and 6.10 are tasks that would be particularly sweet to get help on (enabling wallets to fetch decoy paths in the merkle tree using a gamma distribution across all unified coinbase, pre-rct and post-rct outputs) 
<k​ayabanerve:matrix.org> Sorry, I didn't mean to advocate against your view rbrunner7. If the new wallet is ready in time, which means a similarly timed PR and a drop-in API, I have no objections to its use.
<k​ayabanerve:matrix.org> The FCMP++ scanning code is identical to the classic scanning code if we don't modify the key derivation (as desirable for forward secrecy).
<s​needlewoods> dangerousfreedom currently I'm aiming to make the API feature complete, so it does everything that's needed by monero-wallet-cli, monero-wallet-gui and monero-wallet-rpc, while still relying on `wallet2` for the first step.
<dangerousfreedom> +1
<r​brunner7> "drop-in API" would now in that case be the "Wallet API" that SNeedlewoods is currently making feature-complete compared to wallet2
<jberman> on wallet2 versus the new wallet, I would lean towards sticking with wallet2 for speed of implementation and deployment, and then shifting focus to the new Seraphis-lib backed wallet
<jberman> so basically ya depends on how far along the Seraphis-lib backed API is
<r​brunner7> Well, I think an important unknown is the amount of changes in wallet2 code that would be needed for FCMPs. If they are substantial, it would be pity to have to work with the old spaghetti code, right?
<d​angerousfreedom> jberman: are you using at all the seraphis_lib in your implementations?
<k​ayabanerve:matrix.org> Scanning is currently proposed as identical, as are addresses.
<k​ayabanerve:matrix.org> We're using the RPC for path fetching initially (comparable to requesting decoy info).
<k​ayabanerve:matrix.org> That leaves which RingCT signatures we prove as the distinction.
<jberman> I'm still pretty far away from wallet-side stuff
<jberman> so no
<jberman> I'm using Seraphis lib style code though
<j​effro256> jberman: Do you prefer the gamma distribution fetching of paths versus keeping a pruned scanned tree in wallet storage ?
<d​angerousfreedom> So, at this point, where is the seraphis_lib used at?
<r​brunner7> jberman, but your scanner is mostly seraphis lib based?
<r​brunner7> "Scanning is currently proposed as identical, as are addresses." Hmm, no new long addresses after the first hardfork? Or do I misunderstand?
<s​needlewoods> jberman I took a quick look at your code and it's very pleasant for the eye, so +1 for style choice
<jberman> the wallet scanner I was working on is on hold, it's unrelated to fcmp's, it's a scanner that would replace wallet2's scanner today
<k​ayabanerve> The full tree would be multiple GB. A pruned tree would have a reorg limit (causing a rescan on limit break, unless you fetch the missing context from a node at time of necessity which would be a whole thing) yet would only be log(t) * o size, where t is the tree size and o the amount of outputs.
<jberman> my proposal for the seraphis lib is separate from fcmp's: that we use the seraphis lib to replace wallet2. I prioritize fcmp's higher than that task personally, but still consider it something we should include in our roadmap
<k​ayabanerve> For the reorg depth limit of 50, it'd be however many outputs in the past 50 blocks * some log scaling factor.
<r​ucknium> Is there an explanation somewhere (besides the FCMP++ pdf in sections 6.9 and 6.10) of what role the decoy selection plays in privacy with FCMP? Is it to protect a wallet from a malicious daemon? Why is gamma needed instead of uniform, for example?
<j​effro256> Yes to malicious daemon
<reuben> +1
<r​brunner7> I think it would be a good idea for you, dangerousfreedom , to have detailed chats with all people involved, to see what is there, and then come up with a roadmap of sorts how to go forward. I think you are in the best position to do that, and well, if it takes a full week, so be it. Extremely important work, if you ask me.
<j​effro256> Gamma is used for same reason as decoy selection: people spend recent outputs more often than old
<r​ucknium> Ok so OSPEAD can still be implemented to protect against a malicious daemon when the FCMP hard fork occurs.
<j​effro256> People would then likely naturally  request recent paths vs older paths
<j​effro256> Yup!
<j​effro256> I think
<r​ucknium> The only "problem" that OSPEAD would have then is that it couldn't be updated after FCMP goes into effect since the FCMP hides all the age information in the actual tx data on the blockchain
<r​ucknium> That is actually fine since updating it is tedious.
<k​ayabanerve> Until we move to locally stored trees. It's not infeasible, it's just prior not been scheduled for the first hard fork.
<rucknium> +1
<d​angerousfreedom> Well, yes. That is my immediate goal as I said. If nobody is prioritizing building a new wallet, maybe it doesnt make sense to do it. So it answers your question above. I still personally dont know the best to go for yet.
<k​ayabanerve> Since decoy selection now only matters for the RPC, I don't see why we couldn't update it. Definitely at HF boundaries, but even outside of boundaries.
<jeffro256> +1
<j​effro256> I think it would be a good idea to have a consensus rule that the miner tx holds the current tree hash in tx extra. Its basically free for validators, very low cost for miners, but would help verifiably recover the tree much much faster during a deep reorg yeah?
<r​ucknium> Anyway, the code that's being written for the FCMP "decoys" can easily be adapted to a new distribution by switching out the gamma for something else (or just changing the gamma parameters). Should be a few lines of code to change, later
<rottenwheel> +1
<k​ayabanerve> The tree hash should go in the header.
<k​ayabanerve> It's already specified to do so.
<r​brunner7> dangerousfreedom: You are thinking that maybe it would be best to you to switch and join FCMP efforts in some way?
<k​ayabanerve> *pretty sure it is at least
<r​ucknium> Technically, it can be updated, but not in practice since there would be no updated data to base a new fitted distribution on.
<k​ayabanerve> Also, upon reorg, knowing historical roots doesn't help as you can't grow from a root.
<d​angerousfreedom> I dont know, I have to see what makes more sense to do. It is pretty sad also to see the seraphis_lib being thrown in the trash.
<j​effro256> Should it go in the header? I think that would cause a lot of unnecessary changes to the block fornat. Also that would make headers significantly heavier and thus slower to sync . Additionally, what if we change proofs in the future and its no longer needed ?
<r​ucknium> How many FCMP decoys would a wallet request from a daemon?
<r​brunner7> dangerousfreedom: Alright, let us hear the results of your consultations and deliberations in one week :)
<dangerousfreedom> +1
<k​ayabanerve> The plan is to not throw out the seraphis lib. Solely not rush it to this HF, unless it isn't rushing it.
<k​ayabanerve> jeffro256: we're already making header changes for PoW reasons.
<k​ayabanerve> Rucknium: As many as arguable for a reasonable level of security. I'd presume whatever the ring len is at time of move.
<jberman> the idea for the wallet to store a pruned tree when scanning (i.e. the right-most edge of the tree) is very interesting and I think is sounding like a plausible stronger alternative to needing to fetch decoy paths from the tree
<r​brunner7> kayabanerve: Still wondering about your comment: "Scanning is currently proposed as identical, *as are addresses*" Does that mean no long addresses yet after the first FCMP hardfork?
<k​ayabanerve> Correct
<k​ayabanerve> Using the seraphis lib, and using JAMTIS, are additional discussions
<r​brunner7> Oh, that's a bit surprising, at least to me
<r​brunner7> But well, if that's still a working and sensible hardfork, and we don't hardfork again only about 3 months later, so maybe not that bad
<r​brunner7> Maybe your use and my used of the word "propose" are a bit different ...
<jberman> I think the way more grow_tree impl is currently implemented, it wouldn't be too much work for wallets to lean on the same functions to build that pruned tree locally. I think most of the heavy-lifting can be done external to wallet2 (e.g. prove(), get_tree_extension() when scanning), which means the changes to wallet2 would be minimal
<j​effro256> Yes but PoW change this has the benefit of making header syncing more DoS resistant, especially for deep syncing. I don't think content hashes should go in the header as they are not useful to someone who is just syncing headers
<k​ayabanerve> They benefit doing proofs off of that data.
<k​ayabanerve> also, cramming things in extra needs to be deprecated.
<rottenwheel> +1
<r​brunner7> Don't fully understand, but not cementing tx_extra further has my full support!
<j​effro256> Wallets would be downloading miner transactions during wallet sync anyways though
<r​brunner7> If it's part of some core mechanism, it's sure not "extra"
<j​effro256> Actually IIRC theres actually an option to skip scanning miner txs, but that seems like a premature optimization to me. Also, for wallets who DO  want to build the tree up wallet side, they will have to scan all transactions
<k​ayabanerve> That doesn't impact any of my comments at all.
<k​ayabanerve> That means the bandwidth doesn't change. Cool.
<k​ayabanerve> Placing the root in headers allow SPV without downloading any blocks.
<k​ayabanerve> It doesn't further use extra. It does grow the header (already being modified for DoS resilient).
<k​ayabanerve> We can place it in the block (in extra or a new field), yet that'd make proofs worse and most use cases won't save bandwidth.
<r​brunner7> I think you mentioned it somewhere, but I forgot: that "root" in the header, how many bytes do we speak about?
<j​effro256> How does this allow doing SPV without downloading any blocks? How would you know the paths of your owned enotes  without downloading blocks?
<k​ayabanerve> +32 bytes
<k​ayabanerve> jeffro256: That's not how SPV works.
<k​ayabanerve> If you have the complete header, someone can prove an output to you is in the output tree.
<r​brunner7> Did you detail this aspect somewhere. Sounds somehow hard to believe, seen from the outside by a noob.
<k​ayabanerve> Headers are currently 46 bytes. Adding 32 bytes for the PoW reason will make it 78. Adding 32 bytes for the tree root will make it 110 bytes.
<k​ayabanerve> Considering I think the keccak256 block size is ~64 bytes, we'd not add a keccak256 block. The PoW change already would.
<k​ayabanerve> rbrunner7: We're adding a merkle tree root to the header in this idea. Anyone can make a merkle tree proof to prove a leaf is present.
<k​ayabanerve> The leaf in this case is an output to you.
<j​effro256> I what you're saying, sorry I confused SPV with another term. However, I think the overhead of one block download (which can be reused) versus the verification time for one FCMP is pretty small . also I'd rather the SPV verifiers take on the cost of the block download versus block header syncers take on the disproportionate burden
<r​brunner7> Let me throw in a quick question whether we still have something closely wallet related left for this meeting?
<j​effro256> We can discuss this later though
<j​effro256> We should make a GH issue
<s​needlewoods> not from my side rbrunner
<k​ayabanerve> Sorry, keccak256 is weird with its block size definition. I think I'm correct this won't add a block size.
<r​brunner7> Ok, let's close the meeting proper then. Thanks for attending, nice to see how many things move in parallel in the codebase right now. Read you again next week!
<j​effro256> Thanks everyone !
<s​needlewoods> thanks everyone, cu
````


# Action History
- Created by: rbrunner7 | 2024-07-12T16:49:24+00:00
- Closed at: 2024-07-15T19:05:17+00:00
