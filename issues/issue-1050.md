---
title: 'Seraphis wallet workgroup meeting #81 - Monday, 2024-08-05, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1050
author: rbrunner7
assignees: []
labels: []
created_at: '2024-08-02T19:59:16+00:00'
updated_at: '2024-08-05T19:01:00+00:00'
type: issue
status: closed
closed_at: '2024-08-05T19:01:00+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: https://github.com/monero-project/meta/issues/1045

# Discussion History
## rbrunner7 | 2024-08-05T19:01:00+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1050
<d​angerousfreedom> Hello
<s​needlewoods> hey
<j​babb> Hi
<j​berman> *waves*
<o​ne-horse-wagon> Hello.
<r​brunner7> Right on to the reports from last week
<s​needlewoods> just pushed this: https://github.com/monero-project/monero/compare/master...SNeedlewoods:seraphis_wallet:x_api_add_new_functions
<s​needlewoods> probably contains a bunch of errors, but it should help discussing where I'm at
<j​effro256> howdy
<j​effro256> me: I hope to open CCS for Carrot auditing in a couple days
<j​berman> me: implemented the tx class containing fcmp's; currently wrapping up the fcmp tree migration and tree algos, will draft documentation for the code, wrap up this CCS, then planning to open another to continue
<s​needlewoods> hey jeffro, thanks for mentioning me in the seraphis paper update
<jeffro256> +1
<j​berman> implemented changes to cryptonote tx class for fcmp's* to be clear
<d​angerousfreedom> This week I continued studying the theory of fcmp. I started writing a draft with my understanding of it and hopefully it will serve as an introduction to those willing to also get started. It is still far from ready (as there are still many things that I dont understand) but I will publish the first draft on next meeting. So hopefully after some iterations it will be clear (to me<clipp
<d​angerousfreedom>  at least) what it is being done.
<jbabb> +1
<jeffro256> +1
<sneedlewoods> +1
<one-horse-wagon> +1
<j​effro256> jberman: for "tx class", is it a new class separate from `cryptonote::transaction`?
<s​needlewoods> there are some functions where I don't know how I should translate the argument/return types to standard types
<s​needlewoods> https://github.com/monero-project/monero/compare/master...SNeedlewoods:seraphis_wallet:x_api_add_new_functions#diff-fde87cf4c4fb716c49c267b0f4323eb9c4e826ddcb57366362a5bde96c513276R1203-R1350
<r​brunner7> Yeah, I am also curious about the general approach of those new FCMP capable transactions of jberman
<s​needlewoods> Here are the troublemakers I found so far https://github.com/monero-project/monero/compare/master...SNeedlewoods:seraphis_wallet:x_api_add_new_functions#diff-fde87cf4c4fb716c49c267b0f4323eb9c4e826ddcb57366362a5bde96c513276R1229-R1237
<j​berman> nay sorry, implemented changes to cryptonote tx class for fcmp's* to be clear. Here are the core changes: https://github.com/j-berman/monero/commit/54d5d0d5c7ce1dd0d84ece841fb0d62d519db21e
<d​angerousfreedom> Just a quick confirmation:
<d​angerousfreedom> kayaba is working to get a solid theory and implementation of fcmp which will basically result in a `prove` and `verify` functions to generate such proofs.
<d​angerousfreedom> jberman is working on the node side trying to actually integrate the tree (hashes) into Monero so we can pass a valid tree root to the `prove` and `verify` that kayaba is creating.
<d​angerousfreedom> On the wallet side, we would need to:
<d​angerousfreedom> 1) Keep track of the outputs that we own and build a valid tree branch (with a valid tree root that Monero recognizes) so we can pass that branch (the whole path until our enote (output)) to the `prove` function.
<d​angerousfreedom> 2) Call the `prove` function which will be in Rust
<d​angerousfreedom> 3) Get the proof data and continue building the transaction.
<d​angerousfreedom> On the nodes side:
<d​angerousfreedom> 1) Verify usual stuff (if commitments match, unique key-image on base group, BP) and call the `verify` function in Rust for the membership proof.
<d​angerousfreedom> That is the idea, right?
<j​berman> At a high level, yes. The node also needs to construct the tree (with torsion cleared outputs and commitments that don't equal identity)
<dangerousfreedom> +1
<j​effro256> Are we excluding current output pubkeys with torsion when building the tree?
<d​angerousfreedom> Good question, but I think it wont make any difference now since they will be hashed anyway, right?
<j​berman> Some outputs that exist today will be excluded, but I believe should be invalid and unspendable today anyway (pinging @kayabanerve )
<j​berman> @kayabanerve also proposes that at the hf, we explicitly don't allow output pubkeys with torsion into the chain at consensus
<j​berman> Some outputs / commitments that exist today also equal identity after clearing torsion
<d​angerousfreedom> What that means? Do you know a tx with that behavior?
<j​berman> after clearing torsion on some output pub keys and commitments currently in the chain, those points are equal to the point at infinity (the idenity point)
<j​berman> I don't have one off hand but if you run the migration on a synced node (which I would recommend backing up your db first before running with the current code), it'll hit this line which you could log to get the tx hash
<j​berman> https://github.com/j-berman/monero/blob/5e76191afe911a5a0ffc62896324952b98110616/src/fcmp/curve_trees.cpp#L642-L645
<d​angerousfreedom> I'm curious about the commitment points
<j​berman> for the tower cycle (converting edwards y points to their wei x coords to arrive at Selene scalars) the conersion of identity points to wei x coords has undefined behavior
<d​angerousfreedom> You mean the value commitment C=aX+fH , right?
<j​berman> yep. fwiw it might have just been output pub keys, I don't recall if it was both / which one was triggering the error
<d​angerousfreedom> I will try to find some txs that are strange in the commitment side using my moneroinflation checker. I dont think I ever saw it
<d​angerousfreedom> Lets see :p
<r​brunner7> Challenge accepted then :)
<r​brunner7> Nothing gets past danger's checker, period.
<d​angerousfreedom> Nah, it is still in construction as always haha
<j​effro256> Can you even make a valid bulletproof on a pederson commitment equal to the point at infinity?
<d​angerousfreedom> Yeah, thats my question
<j​effro256> I guess for C=zG+aH with a=z=0 it could pass?
<d​angerousfreedom> With bulletproofs the Monero code always cleared the torsion. So it would mean that somebody created an adhoc software and the majority of nodes accepted it?
<r​brunner7> If that's it about reports, I have something general I would like to ask the attendance:
<r​brunner7> We currently have Monero dev related questions every now and then that have no "natural" meeting to discuss them, because they are not close to research and thus not a good fit for the MRL meeting, nor do they have something to do with wallets or now FCMPs and are at least so far not something we would readily pick up in our meeting
<r​brunner7> Once there were so-called "dev meetings" to discuss anything dev related, but those stopped quite a while ago already
<r​brunner7> As we have this meeting established, and most important "core" devs in attendance anyway, does anybody see a problem with officially widen the scope of our meetings a bit and welcome any dev related issues?
<r​brunner7> The only issue that comes to my mind right now is that our meetings might go over the alloted time too often after broadening the scope in this way
<j​effro256> We could bring them back if it was popular enough, I attended those back then even if I didn't speak much
<j​effro256> I think we should hold the -dev meetings in the -dev room IMO
<r​brunner7> You mean if we redefine this meeting we also should relocate?
<s​needlewoods> I honestly like the size of this group, but maybe we can try to widen the scope and if it's becoming too wide we could do "dev meetings" again
<d​angerousfreedom> I guess the actual integration of fcmp into wallet2 wont be so hard as building all the basis for fcmp. So yeah it makes sense to me.
<r​brunner7> Well, as for group size, I don't think we have many more devs that are regularly active anyway
<r​brunner7> We will probably have some of them in the MRL meeting, I intend to bring up the topic there as well
<o​ne-horse-wagon> IMO, I agree with rbrunner7 completely.  These meetings should broaden the scope to encompass development discussions.  Things are changing and we should change with them.
<j​berman> Cool with broadening the scope of this meeting. Also agree if this meeting becomes too over-scoped we can bring back -dev meetings
<j​effro256> good with me
<r​brunner7> Splendid. Let's see what the people in the MRL meeting think about this.
<r​brunner7> Anything else to discuss in this meeting here?
<j​babb> Just that monero-integrations/monerophp is reimplementing certain crypto functions in pure PHP (vs the old purpose of just wrapping rpc) and I’m reviewing it but would appreciate any of PHP coder eyes on it esp as it approaches merge-time
<s​needlewoods> Yeah, so if anyone can take a look at the links I provided earlier and give feedback on some of the "QUESTIONS" that would be great. Especially this https://github.com/monero-project/monero/compare/master...SNeedlewoods:seraphis_wallet:x_api_add_new_functions#diff-fde87cf4c4fb716c49c267b0f4323eb9c4e826ddcb57366362a5bde96c513276R1203-R1214
<r​brunner7> Josh Babb: That reimplementation thing sounds strange. Was that a good idea in the first place, to go down that route?
<j​babb> PR here: https://github.com/monero-integrations/monerophp/pull/154
<j​babb> I'm not sure.  I just got back to coding for Monero itself after some years absence to farm.
<s​needlewoods> and I just remembered this is still laying around https://github.com/monero-project/monero/compare/master...SNeedlewoods:seraphis_wallet:x_api_comments
<s​needlewoods> (it's the API comments PR based on the organize functions PR) 
<s​needlewoods> and not sure what to do with it
<r​brunner7> Where is that code reorder PR currently at? Waiting for merge into master?
<s​needlewoods> yes
<r​brunner7> I would say as soon as you can get that merged you double down with a comment PR, no?
<s​needlewoods> Okay, I'll be patient
<rbrunner7> +1
<j​effro256> SNeedlewoods: I think it would be fine to use `cryptonote::transaction` for the API, but I would try to avoid using `wallet2`-specific types
<j​effro256> e.g. `transfer_container`
<s​needlewoods> Thanks, I'd agree
<j​berman> +1
<r​brunner7> Sure, we want to get fully independent from wallet2 after all ...
<r​brunner7> That may mean quite some shuffling things back and forth, as woodser's C++ wallet interface implementation show
<r​brunner7> Alright, looks like we can wrap up. Thanks for attending everybody, read you again next week
<jbabb> +1
<s​needlewoods> thanks everyone, bye
<d​angerousfreedom> Thanks
````


# Action History
- Created by: rbrunner7 | 2024-08-02T19:59:16+00:00
- Closed at: 2024-08-05T19:01:00+00:00
