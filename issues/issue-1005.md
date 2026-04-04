---
title: 'Seraphis wallet workgroup meeting #70 - Monday, 2024-05-13, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1005
author: rbrunner7
assignees: []
labels: []
created_at: '2024-05-10T14:06:33+00:00'
updated_at: '2024-05-13T18:44:03+00:00'
type: issue
status: closed
closed_at: '2024-05-13T18:44:02+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: https://github.com/monero-project/meta/issues/1001

# Discussion History
## rbrunner7 | 2024-05-13T18:44:02+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1005
<s​needlewoods> hey
<j​effro256> howdy
<d​angerousfreedom> Hello
<r​brunner7> What is there to report from the week that was?
<s​needlewoods> I've been working on the API and rebased to monero-project master https://github.com/monero-project/monero/compare/master...SNeedlewoods:seraphis_wallet:x_feature_complete_api_1
<jberman> *waves*
<d​angerousfreedom> Not much from my side this week. I decoupled my last prototype to use an interface and I'm struggling to make the EnoteStore serializable since I will need to add the proper functions to serialize a `tools::variant`. koe000  and jeffro256 , do you think it would make sense to change the classes `SpEnoteStore` and `CheckpointCache` to structs and make all variables public so we can<clipp
<d​angerousfreedom>  easily de/serialize it instead of creating functions to do its de/serialization in their classes?
<jberman> me: working on the fcmp tree `grow` algorithm, have made solid progress, currently implementing growing an existing tree, then implementing db code, adding more tests, polishing the code, then implementing `trim`
<j​effro256> Me: Posted milestone update https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/436#note_24480. Also worked towards reproducing issue https://github.com/monero-project/monero/issues/9317. No results yet.
<s​needlewoods> Things I'm not sure about yet:
<s​needlewoods> - Can we remove multisig data from `*.keys` file? I assume we'd have to be able to read the multisig data (for 'old .keys files), but then we could write that data (if wallet is multisig) to a new file `*.multisig`. Or is this a no-go because 'old' wallet software would not be able to read 'new' .keys files?
<s​needlewoods> - Would it make sense to also seperate fields from `WalletSettings` that are currently stored in `*.keys` into a new file named `*.settings`?
<s​needlewoods> - How to handle `m_blockchain` and things related to that?
<j​effro256> dangerousfreedom: we can either 1) make a do_serialize_member method using `BEGIN_SERIALIZE_OBJECT()` or 2) we can make the serialization function a "friend"
<s​needlewoods> serialization is also a topic I skipped so far
<r​brunner7> SNeedlewoods: These are things that would be within my reach to discuss. You could post here, or repeat here, specific questions, and we could discuss over the coming week.
<sneedlewoods> +1
<jberman> "Can we remove multisig data from `*.keys` file?" -> We could, but seems like extra work / maintenance burden for not much gain
<jberman> "Would it make sense to also seperate fields from `WalletSettings` that are currently stored in `*.keys` into a new file named `*.settings`" -> same as above
<j​effro256> @jberman: out of curiosity, how are tree nodes indexed ?
<d​angerousfreedom> I think separating the .keys file (so it just contains the private keys and can be used by key managers) was discussed here already and I think we reached a consensus that it should be made for seraphis. Since we will mostly keep the structure of wallet2 apparently, I dont know how we proceed with that. Would be great to discuss things like that.
<jberman> @jeffro256 : shared a draft schema here: https://gist.github.com/kayabaNerve/0e1f7719e5797c826b87249f21ab6f86?permalink_comment_id=5054800#gistcomment-5054800
<jberman> in memory I'm currently using a vector of vectors for the tree
<d​angerousfreedom> Thanks jeffro256
<j​effro256> SNeedlewoods: the multisig account keys are populated during the setup ceremony, so pruning that data from the .keys file would mean redoing the setup ceremony if you lost your cache file
<s​needlewoods> alright, thanks for the answers
<r​brunner7> Did I get that right, a full week went by without anybody coming up with some brand-new approach, scheme, Jamtis variant, and the like :)
<dangerousfreedom> +1
<rottenwheel> +1
<sneedlewoods> +1
<j​effro256> lmao
<jberman> we're moving!!
<j​effro256> still debating specific fine details of Jamtis, but no big developments
<jberman> @jeffro256 : here's what I'm using in memory: https://paste.debian.net/1316831/
<j​effro256> I'm going to rework the Jamtis library this next week to support Jamtis-RCT as well
<r​brunner7> jeffro256, do you already know whether the new Jamtis RCT proposal also solves the problem(s) that you solved with your Jamtis extension?
<r​brunner7> Or would it be a step back in this regard?
<j​effro256> rbrunner7: yes, @tevador made sure to include the LW privacy protections / scaling settings that were discussed in the original Jamtis proposal
<UkoeHB> jeffro256: Can we get the current Jamtis changes merged first before making another big change? I'd rather see incremental progress in the commits
<r​brunner7> And all this with so "few" keys? Isn't that quite surprising?
<r​brunner7> I mean, I understand almost none of the technicals behind this, but somehow that Jamtis RCT sounds like magic. Even compatible with current addresses.
<j​effro256> Sorry I didn't make that clear: you only get the LW/address generation/no subaddress lookahead features with the extra keys
<j​effro256> You get Janus protection and backwards compatibility with existing addresses
<j​effro256> If you regenerate a legacy style address, you can additionally receive forward secrecy and OVKs
<r​brunner7> Right. But isn't Jamtis RCT considerably simpler than original Jamtis plus your extensions on top?
<j​effro256> Not necessarily in the Jamtis-only side of things, it's about the same level of complexity. It just allows you to also do legacy addresses while keeping things as cohesive between them in terms of tx protocol
<j​effro256> there were a couple simplifications in terms of how certain intermediate values were derived, but the user won't necessarily notice that benefits besides a few % faster scanning speed
<r​brunner7> I see, thanks. That's somehow almost comforting.
<jberman> "How to handle `m_blockchain` and things related to that" -> IIRC the only thing we'd need to maintain for `m_blockchain` to function correctly is to make sure the size is correct for `adjust_priority`, or we can just rewrite `adjust_priority`
<r​brunner7> Still, sounds very attractive. I only hope that the possibility to stay put on the "old" addresses won't derail the whole introduction. Just think, to this day not all Monero software supports subaddresses ...
<jberman> Otherwise `m_blockchain` is only used for handling reorgs when scanning IIRC, and if we replace scanning with the Seraphis lib, we don't need to use wallet2's `m_blockchain` for it
<j​effro256> The proposal is great overall in the sense that all the different tx protocols are meshed together very cleanly and simply. However, the actual Jamtis part is very similar to the original proposal
<jberman> The Seraphis lib has a distinct internal data structure it uses for handling reorgs. We'll probably need to migrate the `m_blockchain` into the Seraphis lib's structure though
<j​effro256> @UkoeHB: sorry not to ignore your message. I will make those small initial modifications to the Jamtis paper and the code, I just also plan to support Jamtis-RCT
<r​brunner7> Ok. Anything special to discuss in this meeting, or is it already back to work? :)
<s​needlewoods> thanks jberman
<s​needlewoods> nothing else from me, will probably ask more questions during the week
<rbrunner7> +1
<r​brunner7> Alright, thanks everybody for attending, read you again in 1 week at the latest
<s​needlewoods> thanks everyone, cu
````


# Action History
- Created by: rbrunner7 | 2024-05-10T14:06:33+00:00
- Closed at: 2024-05-13T18:44:02+00:00
