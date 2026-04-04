---
title: 'Seraphis wallet workgroup meeting #79 - Monday, 2024-07-22, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1042
author: rbrunner7
assignees: []
labels: []
created_at: '2024-07-20T04:27:09+00:00'
updated_at: '2024-07-22T19:15:10+00:00'
type: issue
status: closed
closed_at: '2024-07-22T19:09:13+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: https://github.com/monero-project/meta/issues/1038

# Discussion History
## rbrunner7 | 2024-07-22T19:09:13+00:00
````
<r​brunner7> Meeting in 1 hour
<j​berman> @jeffro256 that's what this is: https://github.com/j-berman/monero/blob/93d9fd4cedcf87f677b9e1537d250a390ef711e3/src/blockchain_db/lmdb/db_lmdb.cpp#L367
<j​berman> tx proofs can specify a block hash, then daemon can read the root hash to verify
<j​effro256> Oh okay. Why a block hash instead of a block height though?
<j​berman> could be either
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1042
<s​needlewoods> hey
<j​berman> *waves*
<d​angerousfreedom> Hello
<j​berman> @jeffro256 with height, if there's a reorg, the node doesn't get indication the proof is invalid until the proof fails to verify
<j​berman> with a block hash, if there's a reorg, the node knows right away the proof is invalid before calling verify
<r​brunner7> What is there to report from last week?
<d​angerousfreedom> I have been trying to understand what FCMP are, now I know a bit more what the towering is and the idea of using Merkle trees. I would try to take on the task jeffro256  proposed but since jberman  said to hold on, I still dont know what to do. Would be great if I can get started doing a specific task so I can have a better grasp on these concepts and how these libraries are worki<clipp
<d​angerousfreedom> ng. So my question to jberman is: do you think I can help in the FCMP endeavour somehow? Otherwise, I would need a bit more time to think how I can be useful.
<j​effro256> howdy
<s​needlewoods> I'm still working on missing functions and taking notes, I don't want to promise anything, but hope to have the PR ready in 2-3 weeks
<j​berman> me: migration code for fcmp merkle tree is set up, ironing it out and working on growing the tree as the node syncs
<j​effro256> jberman: this could be remedied by nodes sending their block hash at height X to other nodes when notifying about news txs
<r​brunner7> SNeedlewoods: Sounds good. Will this be only definitions, or definitions plus implementations already?
<j​berman> I don't have a strong opinion on height vs hash there
<jeffro256> +1
<r​ottenwheel:kernal.eu> jberman @jberman ^
<r​ottenwheel:kernal.eu> Just in case you missed it.
<j​effro256> me: further testing of Jamtis-RCT
<r​brunner7> How about for a very early start dangerousfreedom just testing jberman ' bleeding edge code, in addition to reading it?
<d​angerousfreedom> Yeah, that would be good. Would need a basic guidance though where to get started.
<j​berman> was thinking over the weekend a bit more on how the wallet sync algo that you'd work on could work. in order to correctly update locally saved paths on reorg, wallets also would need to do the trim algo
<jeffro256> +1
<d​angerousfreedom> Probably you will need a big review later and I can start doing it to understand fcmp
<j​berman> starting to read the code I think would be great
<r​brunner7> Yeah, starting to go into review also could be interesting
<d​angerousfreedom> jberman:  I remember some time ago you had created a mock transaction in memory (using mostly Rust code on the backgroung) using the FCMP as the membership proof, do you still have that code? Could you share? Only the database integration was missing, right?
<j​berman> I think core components of that wallet sync algo would be the get_tree_extension + get_tree_reduction functions
<s​needlewoods> definitions + implementations when I'm relatively sure where they belong, else I have notes
<rbrunner7> +1
<j​berman> and those are complicated functions that take time to understand how all edge cases are capture, that I also still want to clean further
<j​berman> the task jeffro mentioned actually doesn't need to touch tx construction
<j​berman> it's syncing enough of the tree so that a tx *could* be constructed
<j​berman> that code was for FCMP's inside Seraphis
<s​needlewoods> e.g. not sure what to do with functions like `has_testnet_option` and similar https://github.com/monero-project/monero/blob/master/src/wallet/wallet2.cpp#L1268
<j​berman> I haven't gotten to creating a mock tx yet with FCMP++ (the current fcmp iteration)
<d​angerousfreedom> jberman: Ok. Do you think it is still worth it to continue working the fcmp on the seraphis_lib and put some efforts on integrating it with the database? How much overlap is there regarding the database integration between seraphis+fcmp and fcmp++ ?
<s​needlewoods> these functions are used in simplewallet and wallet_rpc_server, but not sure how the argument `boost::program_options::variables_map` fits in the API, where we only use standard type arguments
<j​effro256> Personally, I probably would leave the FCMPs in Seraphis alone for now; I don't know if that will be used in the future
<j​berman> +1^
<d​angerousfreedom> Ok
<r​brunner7> So basically the Seraphis library will go into hibernation for quite a while?
<j​effro256> Well not the Seraphis library that touches stuff we do now on the Monero protocol
<j​effro256> Just the stuff specific to the Seraphis protocol
<r​brunner7> jberman, would you agree?
<j​berman> ya
<j​berman> if we're discussing Seraphis lib + fcmp++  (and not the Seraphis protocol), the work will be mostly on wallet-side sync and tx construction, not so much database anyway
<j​berman> since Seraphis lib is basically a wallet lib
<r​brunner7> "database agnostic", so to say
<j​berman> database is daemon side
<r​brunner7> It doesn't even do anything in handling wallet file content, right?
<j​berman> right
<j​effro256> Even thought it would be expensive and useless currently, technically, a modified wallet could build up the FCMP++ output tree *right now* with a normal v0.18.3.3 daemon
<j​berman> @dangerousfreedom a wallet needs to save paths in the merkle tree of all received outputs, and as the wallet syncs, it needs to keep those paths complete to the root of the tree. a wallet needs to do that in order to be able to construct fcmp's
<r​brunner7> Does sound a bit tricky :)
<r​brunner7> Interesting, jeffro256
<j​berman> I think that the code I've written so far would be solid building blocks for that, but it's still in a rough state that I want to clean further. imo a good use of time would be understanding that code and how it can be used for that wallet sync algo
<dangerousfreedom> +1
<j​effro256> One general algorithm that would be immensely helpful for wallets is an automatic "prune" method (different from trim) where a caller can mark as leaf node as "prunable", and then the database class automatically deletes it, then checks its parent to see if all children are deleted and deletes it if so, so on and so forth
<d​angerousfreedom> Yeah, sounds tricky and there may not be an easy optimal solution. Looks like there will be tradeoffs to be made. Anyway, sounds good to start approaching it.
<j​effro256> Then the caller can decide the reorg depth for themselves and skip over calling this `prune` method on e-notes that they know they own
<r​brunner7> By the way, if some new repository as a fork of Monero master would be useful, e.g. for making code easily accessible to several parties, the *seraphis-migration* organisation could be a place where to create and keep it. Just a possibility so that we don't have stuff all over the place, but some "order" in things :)
<r​brunner7> (Part of my secret plan to take over Monero whole)
<jeffro256> +1
<sneedlewoods> +1
<j​effro256> Sorry to go off-topic but: At the next MRL meeting, I want to propose auditing the addresssing protocol for legacy Cryptonote addresses as outlined in @tevador's Jamtis-RCT document. For brevity, I call this protocol "Carrot" (Cryptonote Addresss on Rerandomiable-RingCT-Output Transactions) in the code to differentiate it from the old Cryptonote Adddressing protocol (with no forwa<clipped mess
<j​effro256> rd secrecy, no possible OVKs, etc), as well as the new Jamtis addressing protocol, even though most of the code is reused. Before wednesday, my plan is to create a document which condenses just the cryptographic details needed for Carrot, as well as the engineering requirements. Then auditors would audit the math in that document, and then later a code auditor would document that <clipped mess
<j​effro256> code in the `jamtis_rct` branch matches the document. Is this a good idea?
<dangerousfreedom> +1
<r​brunner7> jeffro256: So you see original tevador Jamtis-RingCT in definite need of some modifications? And you took on the job to work those out?
<r​brunner7> *Carrot* is cool as a name, IMHO
<r​brunner7> Ah, I think I probably misunderstand. You just enable easy discussion by giving a *part* of Jamtis-RingCT a catchy name, right?
<r​brunner7> Sounds good to me then, seems complex and important enough to merit a proper review.
<j​effro256> Yes to the second one
<j​effro256> I did discuss modifications to Jamtis-RCT with tevador but the legacy address side of things was mostly worked out
<r​brunner7> Would you later see a review of Jamtis-RCT as a whole as well?
<j​effro256> Yes definitely
<j​effro256> I would just like to see Carrot get integrated alongside FCMP++ since its a hard boundary and switching then will reduce fingerprinting issues
<j​effro256> And the sooner we switch the addressing protocol, the sooner people get OVKs and forwasrd secrecy
<j​effro256> Without being *required* to switch addresses
<r​brunner7> I think to win over kayabanerve we just have to be fast :)
<j​effro256> Honestly, Carrot is extremely similar to the current addressing protocol that we use now, so the audits should be pretty trivial IMO
<r​brunner7> Maybe now, with dangerousfreedom joining FCMP dev efforts things may work out
<j​effro256> It shouldn't take nearly as much funds as the GBPs or FCMP++ reviews
<r​brunner7> My gut feeling is that funds are not seen as the problem, but any threats of delays in the hardfork to FCMP++ much more
<j​berman> I see what you're thinking on pruning @jeffro256 . What's tricky is knowing exactly what's prunable and not, to be sure that you have enough saved to update your received output merkle paths as the tree grows or shrinks (and layers are added/removed to/from the tree potentially). With the algo `get_tree_extension(<right-most edge of the tree>, <new leaf tuples>)`, you know exactly<clipped messag
<j​berman>  which elements in the tree need updating, and so you can use that tree extension to update your wallet's locally saved receive paths. That takes care of syncing assuming no reorgs. For handling a reorg, you can use trim to correct your locally stored right-most edges of the tree at each block (and locally saved paths), up to a reorg depth
<j​berman> Above is why I suggest using my code, it's basically set up to handle the tricky logic. not to mention I have some helper functions implemented also like output_to_leaf_tuple etc.
<r​brunner7> Alright. Anything left to discuss in this meeting?
<j​effro256> rbrunner7: good point
<j​effro256> I'll try to be quick as possible then
<rbrunner7> +1
<j​berman> moving forward auditing jamtis-rct sounds good to me. I would advocate for jamtis-rct to not delay fcmp's if it comes down to it, but fine with moving it forwards today too
<k​ayabanerve> I'll read through the above, 2-5m please
<r​brunner7> Auditing Carrot first makes it possible to move into implementation, or become sure about that?
<r​brunner7> i.e. not auditing FCMP++ in total, all together
<k​ayabanerve> No, the tree can't trivially be a block height. That'd be an indirect reference and we want it properly binding.
<j​effro256> Thats only a performance issue though , right?
<k​ayabanerve> Ping jberman on not allowing identity points in the tree
<j​berman> ack
<k​ayabanerve> Existing Monero addresses aren't fit for auditing IMO. They've already been extensively reviewed, and they descend from existing stealth address schemes. Cryptographic audits would be to verify they meet certain properties, which requires specifying what properties they expect
<k​ayabanerve> Oh. So sorry. Auditing the way of sending to legacy addresses as newly defined.
<jeffro256> +1
<k​ayabanerve> That's absolutely my misinterpretation, sorry.
<k​ayabanerve> I would like the new protocol to send to CN addresses, at least offering F-S, to be adopted. I care less about generating all the wallet functionality as I do that extra randomness term for privacy. I was planning to prioritize that if it didn't already align.
<j​effro256> Yeah a sucky addressing protocol can mess up all the nice properties of a well reviewed address format ;)
<r​brunner7> Sucky addressing protocol modification ...
<k​ayabanerve> If jeffro wants to do F-S (and more), owning that work, I'd be in full support.
<j​effro256> Yeah carrot does forward secrecy and Janus mitigation for existing addresses and OVKs for regenerated addresses of the same format
<j​effro256> (I.e. backwards compatible)
<r​brunner7> Still sounds somehow like magic to me, that stuff
<k​ayabanerve> If you can own Carrot, great. I only ask for at least F-S with the HF.
<k​ayabanerve> rbrunner7: we had some math and it was good and we called it Monero. Now we just add more math and it's better :D
<jeffro256> +1
<k​ayabanerve> :p Output keys used to be very traditional public keys. They're now effectively Pedersen commitments. all existing public keys can be viewed as Pedersen commitments, just with their randomness set to 0. That's why it's backwards compatible with existing addresses.
<k​ayabanerve> But now that we have this PC and randomness, we can do all these nice new things.
<r​brunner7> Yeah, that a new scheme can bring so many nice new capabilities *and* still stay basically backwards-compatible astonishes me quite
<k​ayabanerve> Agreed. It's the more math in its internals and the possibilities open up when you use PCs for outputs.
<k​ayabanerve> jeffro256: Can you make a dedicated document for Carrot and your exact v1 proposal for my own review?
<j​effro256> Yup this is the plan!
<r​brunner7> Ok. Seems to me everybody has enough tasks to keep them busy. Let me close the meeting proper at this point. Thanks for attending everybody, read you again next week
<k​ayabanerve> Great! I'll be happy to see it.
<s​needlewoods> Thanks everyone, cu
<r​brunner7> So this was the day of the carrot. In one year we will have first aniversary of that :)
<d​angerousfreedom> Thanks rbrunner7
````


# Action History
- Created by: rbrunner7 | 2024-07-20T04:27:09+00:00
- Closed at: 2024-07-22T19:09:13+00:00
