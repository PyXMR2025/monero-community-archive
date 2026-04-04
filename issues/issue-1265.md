---
title: 'Monero Tech Meeting #136 - Monday, 2025-09-08, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1265
author: rbrunner7
assignees: []
labels: []
created_at: '2025-09-05T15:35:41+00:00'
updated_at: '2025-09-08T19:51:54+00:00'
type: issue
status: closed
closed_at: '2025-09-08T19:51:54+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1262).


# Discussion History
## rbrunner7 | 2025-09-08T19:51:54+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1265
<s​needlewoods> hey
<s​yntheticbird> hi
<j​berman> *waves*
<j​effro256> Howdy
<r​brunner7> What are the reports from last week?
<r​brunner7> I worked jeffro256 's review comments into my PR, but today he found some little thing more to polish :) https://github.com/monero-project/monero/pull/9939
<s​needlewoods> same procedure as every week
<s​needlewoods> just one thing worth to mention, I didn't see a good reason why the CLI `set_daemon` command had no option for daemon login and proxy, so I added both options ([commit](https://github.com/monero-project/monero/commit/78e22f7eb526cc9bcf45dceb5f4005aebd6ec7e4))
<j​berman> Almost exclusively worked on PR 81, the PR to refactor wallet2 refresh and fix fcmp++ reorg handling (and last blocker for stressnet). I worked on implementing using the existing `short_chain_history` approach to request blocks with some modifications (the goal with `short_chain_history` is to minimize trips to the daemon / data downloaded when handling reorgs). I detailed the modifications and rationale in the PR description, and in a follow-up comment. It's a bit complicated. I think it would be solid to get consensus on the PR's approach https://github.com/seraphis-migration/monero/pull/81
<r​brunner7> So pouring all this work into `wallet2` still is in the interest of working well for FCMP++, right?
<j​effro256> Reviewing @j-berman's PR #81 today, have been working on a multisig fix upstream for the last few days. A wallet2 reorg handling issue with multisig exchange messages has been plaguing Haveno ever since Qubic started all those reorgs
<j​berman> I'd say yes. The seraphis refresh mechanism has months of work to get it to production ready
<r​brunner7> I see
<r​brunner7> Oh, multisig data exchange *and* reorgs, sounds like fun :)
<r​brunner7> I dimmly remember thinking while implementing the MMS years back "Well, there won't be any reorgs while this code here runs, hopefully"
<r​brunner7> And for a long time that was almost a given. Not anymore right now, of course.
<r​brunner7> Is there an ETA for the first FCMP++ based network starting to run?
<r​brunner7> With the nodes of a handful of testers
<j​berman> 7 days after we get PR 81 in
<r​brunner7> Ok :)
<r​brunner7> Looks a bit scary from the description alone already, not sure it's within my reach to review. Will try to have a look.
<j​berman> "Modification 1" is the main thing I'm hoping to get consensus on
<j​berman> I can try to explain it a little more here with shorter context
<j​berman> First a primer on `short_chain_history` and requesting blocks using the `block_ids` param in getblocks.bin
<j​berman> The idea is to include a short, ordered list of hashes that the wallet has already seen. The daemon will then traverse this list, starting from the highest block included in the request (i.e. most recent), and upon encountering a block id that is in the main chain, the daemon will then return a contiguous set of blocks starting from that block id
<j​berman> If there was a reorg, then the daemon will include contiguous blocks starting from the *first* block included in the request that is *still* in the main chain
<j​berman> This way the wallet will know if there was a reorg based on the daemon's response
<j​berman> *end context on short_chain_history/block_ids`
<j​berman> Now on to this PR: I modified the core approach in wallet2 to make sure that the `short_chain_history` in every request to getblocks.bin *always* reflects the wallet's known view of contiguous blocks, making sure that the list of `block_ids` **always** includes the oldest block that the wallet can handle reorgs back to
<j​berman> ALSO importantly, the request will always include the genesis block in it as well, so if the daemon serves blocks contiguous from genesis, the wallet will know it cannot handle the reorg
<j​berman> This way the daemon response will **always** serve the blocks that the wallet can handle reorging, OR the wallet will be able to tell that it cannot handle the reorg
<j​berman> (another piece of context and why there is a max reorg depth that the wallet cannot handle reorging below: the FCMP++ tree that the wallet is building locally is "pruned" so that it doesn't take GB's of space. It has a max reorg depth so that the wallet can prune the tree effectively)
<j​berman> So that is the necessary context to understand how the PR aims to maximize benefit of short_chain_history
<j​berman> Following this so far?
<j​effro256> wallet2 doesn't include the block ID for max reorg depth already?
<r​ucknium> What if `max-reorg-depth` on a wallet is set very deep? Will the list of `block_id`s fit inside an RPC message?
<j​effro256> Just cheked... ig not lol
<s​needlewoods> with "wallet cannot handle reorgs", you mean without `rescan_bc`?
<j​effro256> That's definitely an improvement
<r​brunner7> "Following this so far?" Not yet, I would say, lacking basic knowledge how the wallet synchs so far in detail, but I think your context written here will be valuable
<sneedlewoods> +1
<jberman> +1
<j​effro256> The short chain history uses exponential backoff, so it will only be logarithmically bigger
<j​berman> The short_chain_history works like this: start with 10 most recent blocks, then go step-wise *2. So first 10, then 12th, then 16th, then 24th, etc. So going back to the start of max reorg depth is log 2. Quick someone do the maths
<jeffro256> +1
<j​berman> right it doesn't
<j​berman> Ok jeffro is following, so I think I will just continue and I think it will eventually click for all at some point
<r​brunner7> Just curious: You write in the PR description "Correctly handles deep reorgs". Where is the limit of the old i.e. current code?
<r​ucknium> Makes sense. So you get more of the set of block ids fitting inside of a message, at the cost of more messages.
<j​berman> m_max_reorg_depth
<j​berman> Old code (as in code on release branch) I don't think is broken though AFAIK. It's  fcmp++-stage fcmp++ integration that this is fixing tbc
<r​brunner7> Ah, now I understand.
<j​berman> So continuing rn on the core thing I want to get consensus on: right now, wallet2 fetches the **next set of blocks** asynchronously in  parallel to synchronously processing the **previous** set of blocks
<j​berman> process_parsed_blocks is where the block processing is done
<j​effro256> If I understand correctly, `rescan_bc` might not be usable for soft resets after FCMP++ since we need to download all outputs since the starting refresh point to build the FCMP tree
<j​berman> and that is where wallet2 sync m_blockchain, the local data structure keeping track of which blocks wallet2 has synced
<j​berman> sorry, yes, this is what I meant
<sneedlewoods> +1
<j​berman> will double check rescan_bc soft after this
<j​berman> Continuing from here. Since process_parsed_blocks internally handles syncing m_blockchain (including handling reorgs), that presents a synchronicity conflict: how to make sure we're fetching the next set of contiguous blocks in parallel without needing to wait for `process_parsed_blocks` on the prev set of blocks to complete, using the expected short_chain_history that reflects the latest chain state
<j​berman> I solved this by maintaining a second struct `hashchain cur_chain` that I read in the control thread executing the request for the next set of blocks in parallel
<j​berman> That struct is distinct from m_blockchain, but I duplicate the reorg /sync logic to make sure that cur_chain handles reorgs the exact same way
<j​berman> This way I maintain wallet2's approach to fetch next set of blocks in parallel to processing the prev parsed blocks
<j​berman> I wrote about an alternative relatively simple approach here that would present another change to wallet2's refresh structure, but would avoid the duplicated logic of reorg handling: https://github.com/seraphis-migration/monero/pull/81#issuecomment-3263948108
<j​berman> And that decision is the thing I'm hoping to get consensus on
<j​berman> I don't think it needs consensus in this meeting, but hopefully that context helps to reach conensus faster
<j​berman> And helps explain the PR's approach
<k​ayabanerve> *waves*
<j​berman> rescan_bc soft is still good, it clears m_transfers, m_blockchain, and m_tree_cache. It just doesn't clear things like notes and labels
<k​ayabanerve> Apologies for being late. My only update is how the fcmp++-stage branch merged the latest fcmp++ code and I'm very happy about that.
<sneedlewoods> +1
<r​brunner7> "I don't think it needs consensus in this meeting" That would be asking for a bit much ....
<j​berman> (faster prove time for large inputs will be in stressnet)
<r​brunner7> Nice
<j​berman> Sorry that explanation above ended up longer winded than I had hoped
<r​brunner7> Ok, thanks for all the background info, probably helps understanding a lot
<r​brunner7> Well, I think that's very often the most valuable info: general approach, intent, and overall structure of code
<j​berman> *thumbs up*
<r​brunner7> Ok, if that's it about that PR, do we have anything else to discuss today?
<j​effro256> Wouldn't you still need to have a "copy" of the hashchain in this proposed appraoch to revert to in case there as an error in block processing?
<j​effro256> Nah it was good info
<jberman> +1
<j​berman> This is a good point to raise and is one of the complications to deal with as result of duplicated logic
<j​berman> I initially missed it in my first pass, but this should solve that issue: https://github.com/seraphis-migration/monero/pull/81#issuecomment-3263948108
<j​berman> Resetting that locally scoped cur_chain to the state of m_blockchain in the event of an error should make sure the next loop continues from where it's supposed to
<r​brunner7> "error in block processing" also includes interruptions of the communication with the daemon?
<j​effro256> That's the proposed method I was referring to. So you would be syncing hashchain updates before making the next request to the daemon. Doesn't that mean you need to copy & mutate the hashchain before the processing in case the processing goes wrong?
<j​effro256> Like I think you have to have it either way, no?
<j​berman> yep, and also CLI errors upon encountering a receive and user needs to input their password
<j​effro256> Unless you add new logic to rollback changes made before processing
<j​berman> So first in the control thread, it rolls back the locally scoped cur_chain as needed for next loop
<j​berman> Then next loop makes the request for that next set of blocks in parallel
<j​berman> Then it continues processing prev parsed blocks on top of m_blockchain (which has not been updated yet for the rollback)
<j​berman> process_parsed_blocks will then *also* handle rolling back m_blockchain internally (using duplicated reorg handling logic)
<j​effro256> Is this the current state of #81?
<j​effro256> The last 4 messages?
<j​berman> if process_parsed_blocks errors, then the control thread should hit that catch statement, and cur_chain should reset back to m_blockchain
<j​berman> And in effect, this will have been a wasted request for the next set of blocks, but no local state change should happen to the wallet
<j​berman> yes
<r​brunner7> Alright, discussion between people in the know about PR #81 can continue of course, but allow me to close the meeting proper. Thanks everybody for attending, read you again next week!
<j​berman> Wait I had one other thing to raise!
<j​effro256> Thanks everybody
<j​effro256> jk
<j​berman> actually a couple sorry
<r​brunner7> Sorry, didn't suppose that ...
<j​berman> Just going to mention in here, I'm pretty ok with ArticMine 's latest fee proposal to scale fee by tx byte size alone without considering verification time, considering tx size as a whole actually *does* increase a significant amount as n inputs increases beyond just membership proofs size
<jeffro256> +1
<j​berman> pinging kayabanerve
<j​berman> this kayabanerve
<j​berman> the figures: https://github.com/seraphis-migration/monero/issues/44#issuecomment-3150754862
<k​ayabanerve> I still support a fee by verification time too, to the point it's never worse re: fees to make multiple small TXs vs one large TX.
<k​ayabanerve> But I'll concede if I'm in the minority
<r​brunner7> The discussion in the last MRL meeting gave me the impression that consensus about the new fees is still somewhere in the distance ...
<r​brunner7> I myself don't have an opinion there, don't know enough about fees unfortunately
<j​berman> the latest MRL meeting had a lot of discussion on block weight penalty, which is another discussion. I do think we are closer to a finalized weight calculation
<r​brunner7> We may see in 2 days, hopefully
<j​berman> I think the latter point still holds using artic's current proposed figures, but will double check it
<k​ayabanerve> It shouldn't, as the inputs are linear but the proof sizes favor large TXs.
<j​berman> oh wait, I misread you as flipped
<k​ayabanerve> Unless it's superlinear to proof size still.
<k​ayabanerve> Then ack, I stated my criteria and can be happy however it's satisfied 👍
<j​berman> you're saying you would prefer that users not have the incentive to make one large tx, versus multiple txs?
<k​ayabanerve> Coreecr
<k​ayabanerve> *Correct
<ofrnxmr> -1
<j​berman> But verifying larger should always be faster than smaller too? So you're making 2 points there, A) that you would still support verification time, and separately B) that you would not prefer an incentive to make larger txs
<j​berman> > But verifying larger should always be faster than smaller too
<j​berman> In that 128-in fcmp verify should be slightly faster than 16x 8-in
<j​berman> It seems like these 2 points are in conflict
<k​ayabanerve> Not if we weight verification time superlinearly as to achieve an incentive for many lower-verification-time TXs.
<k​ayabanerve> I won't complain if they're at least equal but would argue a 128-input TX should pay twice as much as 19 8-input TXs :C
<k​ayabanerve> I would also argue 128-input TXs shouldn't exist and point out you wanted booting a Monero node to require sampling ~200k points which would take around a minute D:
<k​ayabanerve> But that's not the community's vibe at this time :p So instead I made it so loading those 200k points take ~40x less time.
<j​berman> https://github.com/seraphis-migration/monero/issues/44#issuecomment-3187685572
<j​berman> 16x 8-in is almost twice as large as 1x 128-in
<j​berman> bandwidth is likely to be the main limiting factor to scaling long term
<k​ayabanerve> And should be <half the cost IMO.
<k​ayabanerve> The input limit will be the limiting factor to scaling if we ever introduce transaction uniformity, if every TX must be 100 KB due to the inputs.
<k​ayabanerve> From transaction uniformity to IVC (which could compress all inputs to just one), the input limit is an incredibly important factor.
<k​ayabanerve> I think it should be lower. It'll be 128. I think people shouldn't be encouraged to make TXs with 128 inputs.
<k​ayabanerve> *IVC would presumably also have a fixed input limit.
<j​berman> The reality is the current hf and what's planned for it in particular and I think goal should be to optimize for that, not a future hf which may have distinct tech/research to achieve the goal of uniform txs
<k​ayabanerve> Except people keep bitching about the idea of reducing inputs and this would gently nudge them to build better wallet software themselves, reducing friction in any inevitable future where Monero development doesn't die off.
<k​ayabanerve> At some point, Monero will either be technically stagnant or will adopt a fixed-input limit (even if solely internally considered and not exposed to the user) for privacy or scaling, I'd bet on it.
<j​effro256> I wonder if, without proper broadcasting of this rule, people making very large TXs will ever do the math and be deterred from making large TXs, or they'll just go "hmmm... that's a really big fee, oh well..."
<k​ayabanerve> I mean, I'd bet like $100, I'm not a millionaire.
<k​ayabanerve> jeffro256: p2pool is probably a large enough force that someone will build an optimized p2pool aggregator
<k​ayabanerve> It doesn't require users be smarter. It requires a few devs be smarter with the systems users use.
<j​effro256> But aggregators do technically break the current UX of using Monero, so the users at least have to be aware of why it is being done
<k​ayabanerve> Any part of Monero 'breaks' the UX of Monero, fight me /s
<k​ayabanerve> Aggregators already exist. This does aggravate them, but in a softer way than what I originally pushed for, in hopes they'll adjust and it'll flow downstream so it never comes to the shove I wanted.
<k​ayabanerve> The fact users may not have noticed aggregators exist, or sweeping may be necessary, is solely due to the conditions which may or may not always exist. This narrows the chance they live in blissful ignorance, sure, but it sets a transition path and encourages uniformity now.
<j​berman> I still think your line of reasoning is giving too much weight to how you imagine a future hf would be designed to accommodate tx uniformity
<k​ayabanerve> I understand I'm disagreed with and I'm not a dictator here
<k​ayabanerve> Feel free to move on :p
<j​berman> I think a future hf that achieves tx uniformity in some solidly designed /agreed upon way is fine to then "shove" toward tx uniformity at that point
<j​berman> rather than push for it in next hf
<j​berman> the goal is still rough consensus on weights for this current hf. sounds like you still wouldn't agree with weights scaled by byte size alone and would NACK what's currently on the table
<j​berman> which is an important NACK to take into account
<r​brunner7> For what it's worth, my gut feeling is also to get FCMP++ out of the door in any reasonable, acceptable form, see how that works, and then adjust and improve starting from that
<r​brunner7> It's already a giant step, a bit problematic to make it bigger still
<j​berman> I think byte size has strong justification and has major benefit of being simple
<j​berman> I'm content with closing discussion on this issue for now :)
<j​berman> at least within this meeting that's still quasi ongoing
<j​berman> I did want to raise one other thing, but I'll hold off on it
<r​brunner7> So next week for that "one more thing"?
<j​berman> or I'll just say it now and whoever wants can discuss
<j​berman> 1 sec
<r​brunner7> It will at least make it into the meeting log :)
<j​berman> I raised a point in 81 that is unrelated to 81, that I will probably make a separate issue out of: https://github.com/seraphis-migration/monero/pull/81#issuecomment-3197430438
<j​berman> jeffro256 and ofrnxmr and I then had a discussion on it that is interesting
<j​berman> my TL;DR: if a pool's tx FCMP++ uses a tree root that will no longer be part of the main chain e.g. daemon user pops blocks 40 blocks or there is a >= 10 block reorg, then said tx will no longer validate (unless of course, the tree becomes the main chain tree again), and as such I propose we kick the tx from the pool as a step in a better direction from current (the tx remaining in the pool and preventing a user from spending the inputs that tx included)
<r​brunner7> TL;DR if the tx is absolutely hopeless kick it?
<j​berman> yes
<j​berman> jeffro argues that since the tx could theoretically become valid again, it may make sense to keep the tx around in the pool
<r​brunner7> Sounds good, with a watertight predicate "Is hopeless" of course
<j​berman> (I think is his argument, may be putting words in his mouth sorry jeffro)
<r​brunner7> Yeah, saw something of that argument. I think that may have merit, but not with a full week of expiry. I would guess if after 1 day there is no switch back of the chain it's over.
<b​oog900> We could keep the tx but drop it if another tx comes in that double spends it but is valid?
<b​oog900> or we could just keep both in the pool
<b​oog900> why drop either :)
<r​brunner7> Uh, tx id must be key in tons of related structures
<j​berman> I think the latter is arguably the optimal long term solution, but more involved of a change that I don't exactly think is worth it for v1
<r​brunner7> Keeping both might not be trivial
<b​oog900> tbf this is an issue that needs fixing now not with FCMP
<b​oog900> and it doesn't need to be a HF/consensus change
<j​berman> that's fair too
<r​brunner7> Alright, *now* I declare the meeting proper to be over. Thanks again, until next week.
<j​effro256> I would only be okay with keeping both if the signable transaction hash is the same. But perhaps as a v1, I guess it makes sense to drop the transaction under a >=10 block reorg and allow a new transactions, rather than keeping that input completely locked for 3 days (current mempool expiry period)
<jberman> +1
<s​needlewoods> thanks everyone, until next time
<j​berman> the problem with keeping the tx around (without other modifications) is that a deep reorg by a malicious actor could be even more problematic for honest users than it needs to be (honest users get their txs stuck and can't spend the inputs)
<b​oog900> I think dropping txs in the pool after a reorg is fine as only txs in the pool before the reorg would be affected if the main chain comes back
<j​berman> another contextual element: blocks that are reorged also have their txs placed back in the pool
<j​berman> and I think it's a better step for v1 to drop those 2 if they can't be included in what is at the time the main chain
<j​berman> those too* lol
````


# Action History
- Created by: rbrunner7 | 2025-09-05T15:35:41+00:00
- Closed at: 2025-09-08T19:51:54+00:00
