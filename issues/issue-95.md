---
title: Eliminating the 10-block-lock
source_url: https://github.com/monero-project/research-lab/issues/95
author: UkoeHB
assignees: []
labels: []
created_at: '2022-01-02T03:32:27+00:00'
updated_at: '2025-07-23T04:43:10+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
## Eliminating the 10-block-lock

This is a proposal for eliminating Monero's 10-block-lock, which prevents users from spending outputs until they are 10 blocks old. The proposal has two significant and clear drawbacks, but I believe it is the best possible solution given all the constraints.

If you are reading this, please first look at it academically before dismissing it out of hand. Yes, the drawbacks may be too severe, but before passing final judgement I would like a useful discussion.


### Motivation for 10-block-locks

In my view, there is one main reason for needing 10-block-locks in Monero.

Outputs in the PoW 'reorg zone' (the most recent \~1-10 blocks) can be completely removed from the chain by a reorg, because any output that can be reorged can be double-spent. If an attacker spams the network with double-spends of his own outputs, then on a regular basis 'naturally occurring' reorgs will cause some of his transactions to be replaced by his double-spends of those transactions' inputs. If an output created by the first group is used as a decoy by a random person, then that person's transaction will become invalid after the reorg.

In other words, decoys are vulnerable to the 'confirmation' problem. A tx author should only use decoys that are 'strongly confirmed', i.e. decoys that are buried below the 'reorg zone'.

Since all txs need strongly confirmed decoys, outputs in the 'reorg zone' will never be used as decoys. Hence, any output in the 'reorg zone' referenced by a tx input's ring signature must be that input's real spend. The tx author may be fine with revealing their real spend. However, if that output is used as a decoy in other users' txs, then since observers know it has been spent, they will know it is a decoy in those other users' txs. This weakens those users' ring signatures. To prevent that weakening, the 10-block-lock time is enforced. This way all decoys in a tx input are plausibly the real spend.


### Proposal

1. Allow transactions to have inputs with zero decoys if those inputs are very young (recently added to the chain).
1. After a grace period, remove outputs from the pool of eligible ring members if they have been spent in a zero-decoy input.

This offers a compromise between fast-spends and minimizing the damage those fast-spends can do to ring signature effectiveness.

```
// constants
DEFAULT_SPENDABLE_AGE = 10;
INPUT_ELIGIBILITY_GRACE_BLOCKS = 20;
ZERO_DECOY_ELIGIBLE_ZONE = DEFAULT_SPENDABLE_AGE + INPUT_ELIGIBILITY_GRACE_BLOCKS;  //30
PROVABLY_SPENT_DECOY_ELIGIBLE_ZONE = ZERO_DECOY_ELIGIBLE_ZONE + INPUT_ELIGIBILITY_GRACE_BLOCKS; //50

fn validate_input_age_zero_decoy(block_height, input_height) -> bool
{
    // only outputs in the zero-decoy eligible zone can be spent with zero decoys
    if (block_height - input_height > ZERO_DECOY_ELIGIBLE_ZONE)
        return false;
    else
        return true;
}

fn validate_input_age(block_height, input_height, input) -> bool
{
    // only outputs that reached the default spendable age can be referenced in a membership proof with > 0 decoys (IF they are not 'provably spent and older than the provably spent eligible zone')
    if (block_height - input_height <= DEFAULT_SPENDABLE_AGE ||
        (block_height - input_height > PROVABLY_SPENT_DECOY_ELIGIBLE_ZONE && is_provably_spent(input))
        )
        return false;
    else
        return true;
}
```

- Why are there grace blocks?

A transaction that lands in the tx pool may not be added to a block right away. If a tx spends a zero-decoy input that is 10 blocks old at the time of construction, it can't even be added to the in-progress block if there is no grace period.

If a tx with a normal input references a provably-spent input that is 20 blocks old, and provably-spent in a tx that is 10 blocks old, then it can't be added to the in-progress block without a grace period on provably-spent ring members.

When constructing a transaction, if a real-spend is within the 10-block-lock, then spend it as a zero-decoy input. Otherwise use a ring signature like normal (however, the tx author should avoid using decoys that are already provably spent). The grace blocks should not be abused to make zero-decoy inputs that are older than 10 blocks.


### Drawbacks

There are two main drawbacks to this proposal.

1. When a transaction is constructed, any decoys selected from the most recent \~20 eligible blocks _may_ become provably spent.
1. Since input-type-eligibility changes as a function of the block height where a tx gets mined, if a tx lingers in the tx pool for longer than the 20-block grace period, it may become invalid.
    1. Any tx with a zero-decoy input would become invalid.
    1. Any tx with a normal input that references a provably-spent output would become invalid. If deterministic binning is implemented, it may be impossible for deterministic references to work across the eligibility-barrier (i.e. because output ordering/indexing would change within blocks after provably-spent outputs are removed). In that case, txs with normal inputs would always become invalid at the end of the grace period.

Note that Seraphis membership proof delegation allows tx authors to always complete membership proofs right before submitting their txs, which would make slow txs like multisig/atomic swaps compatible with this proposal (otherwise the grace period would usually expire before a tx can be submitted).


### Looking at the future

If Monero implemented an ideal membership proof that could reference _all_ outputs in the chain, then this proposal could be greatly simplified to 'allow zero-decoy inputs if the inputs are < 30 blocks old'.


# Discussion History
## LocalMonero | 2022-01-02T04:27:28+00:00
Eliminating the 10-block-lock would be a quantum leap in the usability of Monero. Having to wait 20 minutes to spend isn't something that would be expected of a currency that is positioning itself as the next generation of money. If this is possible with Seraphis, it's a design goal that should be prioritized.

As for @UkoeHB's proposal. I have a question, what if the zero-decoy input actually pre-selects decoy outputs, including outputs within the <20 block zone, this way if the tx lingers for longer than the grace period it automatically converts itself into a standard tx?

## tevador | 2022-01-02T07:37:00+00:00
Since all Monero transactions must have at least 2 outputs, it would make sense to at least have a 2-member ring consisting of both outputs. This would avoid having provably spent outputs*. Note that the confirmation problem does not apply in this case, because the whole ring consists of outputs that were created by the user submitting the transactions.

So there would be 2 options:

1. Reference 11 ring members older than 10 blocks as usual.
2. Reference a previous `txid`, in which case the ring is formed by all outputs of that transaction.

\* In rare cases, we could still have provably spent outputs if both transactions outputs are spent this way.


## HavenoDEX | 2022-01-02T12:39:05+00:00
The 10-blocks lock is a big UX problem for normal users, which cannot spend coins they just received and are forced to wait 20 minutes; and for projects like Haveno, built on multisignature transactions (more details about how the lock negatively affects Haveno in our dedicated issue: https://github.com/haveno-dex/haveno/issues/203).

We strongly support the removal of the 10-blocks lock and we agree it should be a priority.

## UkoeHB | 2022-01-02T16:20:24+00:00
> As for @UkoeHB's proposal. I have a question, what if the zero-decoy input actually pre-selects decoy outputs, including outputs within the <20 block zone, this way if the tx lingers for longer than the grace period it automatically converts itself into a standard tx? @LocalMonero 

Once a zero-decoy signature has been made, the link between output and key image is guaranteed. Adding decoys later cannot hide that connection.

> Since all Monero transactions must have at least 2 outputs, it would make sense to at least have a 2-member ring consisting of both outputs. @tevador 

This is an interesting idea. However, the spent output could not be removed from the decoy pool. Zero-decoy vs. 1-decoy is not a huge gap, and would still weaken other ring signatures that use the referenced outputs as decoys.

My goal is to prevent weakening ring signatures even if a huge proportion of outputs are zero-decoy (e.g. due to an adversary).

## AncientSion | 2022-01-03T20:52:09+00:00
This is super exciting if its actually viable.

## MoneroArbo | 2022-01-03T22:04:36+00:00
> My goal is to prevent weakening ring signatures even if a huge proportion of outputs are zero-decoy (e.g. due to an adversary).

My question: Hypothetically, let's say after this change 50% of transactions are spent as 0-decoy within 10 blocks. That would reduce the number of potential outputs to select as decoys by half compared to the case where we keep the lock time, no?

It seems like reducing the available outputs for decoy selection would have *some* effect on the effectiveness of ring signatures -- can we quantify it?

## UkoeHB | 2022-01-03T22:16:15+00:00
> It seems like reducing the available outputs for decoy selection would have some effect on the effectiveness of ring signatures -- can we quantify it?

My intuition is reducing the total number of available decoys only affects the total depth/breadth of the transaction graph. It does not affect the average number of times a given non-zero-decoy output would be used as a ring member (it should be ~ equal to the ring size if tx volume is constant).

Once the graph is sufficiently large, further increases in size have negligible impact on privacy, so a reduction in size may also be negligible.

## tevador | 2022-01-03T22:35:09+00:00
I think the biggest risk is breaking the "privacy by default" property of Monero. With this change, it is theoretically possible to have a very active wallet with an entirely traceable history. Worse yet, exchanges may start requiring deposits to be zero-decoy transactions etc. It's a slippery slope that ends up down there with zcash.

## MoneroArbo | 2022-01-03T22:41:22+00:00
> Once the graph is sufficiently large

Do we have an idea for what counts as sufficiently large

> Worse yet, exchanges may start requiring deposits to be zero-decoy transactions etc

In order to accommodate this request, a user who has coins >10 blocks old would first have to self send which would mitigate the information gain? At least somewhat.

Hmm, although, that makes me wonder. You receive a TX with 10 decoys, then you spend that output as a 0-decoy TX --- wouldn't that also allow an observer to make an inference about which output in the previous 10-decoy TX was the real spend?

## Gingeropolous | 2022-01-03T22:47:57+00:00
> I think the biggest risk is breaking the "privacy by default" property of Monero. With this change, it is theoretically possible to have a very active wallet with an entirely traceable history. Worse yet, exchanges may start requiring deposits to be zero-decoy transactions etc. It's a slippery slope that ends up down there with zcash.

so much this. 

Additionally, this issue is something that can be "solved" with output management. 

## LocalMonero | 2022-01-03T23:00:33+00:00
> I think the biggest risk is breaking the "privacy by default" property of Monero.

Then another solution needs to be found. Nobody says that the 10-block-lock should be eliminated at all costs. Just that it's a high-priority goal.

> Additionally, this issue is something that can be "solved" with output management.

Details? Are you talking about generating txs with outputs for yourself? This doesn't solve any problem apart from sending multiple transfers that lock all your outputs in a row, such as to pay for two cups of coffee in the span of 5 minutes. Even then, it's an awful hacky solution that no average person should be expected to do, nor is it desirable to bloat the blockchain with transactions heavier than need be even if this functionality is abstracted away into the wallets that will automatically generate and send out these outputs on a regular basis, using up the device's resources, and they'd have to do it ahead of time too.

## SamsungGalaxyPlayer | 2022-01-03T23:03:18+00:00
@LocalMonero one can prepare in many cases to avoid having to deal with this problem. It doesn't solve for all cases though, hence "solved." Haveno is an example case that's difficult/impossible to plan around. You can't realistically tell someone who needs to put money in a 2/3 multisig to confirm a trade that they should have thought ahead :/

## LocalMonero | 2022-01-03T23:07:53+00:00
You can't realistically tell anyone that they should have thought ahead in the modern instant economy and call your product the next generation of money. Waiting 20 minutes to spend is not something to "hack around", it's something to solve. Spending unconfirmed coins is a massively useful application, ranging from instant payments between trusted parties to hot<->cold wallet management for exchanges to non-custodial service platform flow optimizations.

## SamsungGalaxyPlayer | 2022-01-03T23:17:51+00:00
I'm quite interested in debating the merits of the idea @tevador introduced. I'm also still wrapping my head around the implications, so please don't take these points as gospel.

Benefits of Tevador's method:
* Fewer things are *completely* known to be spent, preventing them from being completely ruled out.
* People using the Monero wallet for high-frequency transactions will at least get *some* transaction graph privacy.
* Better protections for decoys that are selected within this 10-20 block window.

Benefits of the originally-proposed method:
* Lazily-spent outputs are filtered out quickly.
* Better protections for decoys that are selected later after block 20.

Disadvantages of both methods:
* Encourages lazy/sloppy output use, where many exchanges, mining pools, and other services will see no meaningful reason to follow best-practices of cycling through different outputs and batching transactions.
* Adds complexity compared to the current method.
* If a 20 block grace period is selected and there is a typical 10-block lock window, that would reduce privacy somewhat for transactions spent between 10-20 blocks.

Recommended improvements:
* Impose a noticeable additional fee on instant send transactions to discourage sloppy use. Make it 10x more for example. That way exchanges and services which are making regular transactions have an incentive to not be apathetic towards privacy.

## AlejandroGuariguata | 2022-01-04T00:04:44+00:00



> I think the biggest risk is breaking the "privacy by default" property of Monero. With this change, it is theoretically possible to have a very active wallet with an entirely traceable history. Worse yet, exchanges may start requiring deposits to be zero-decoy transactions etc. It's a slippery slope that ends up down there with zcash.

This is by far the biggest drawback. New users may not be aware of the traceability of their transactions unless they research it themselves. Easy to use default privacy, without any gotchas, is one of the biggest reasons monero is so useful.

A solution that doesn't jeopardize this would be preferable.

## LocalMonero | 2022-01-04T01:24:33+00:00
> A solution that doesn't jeopardize this would be preferable.

I'd even go so far as to say that **only** a solution that doesn't jeopardize would be acceptable.

## janowitz | 2022-01-04T09:28:14+00:00
I agree, that this limitation in every day usage is probably the biggest limitation, already starting when you show someone how a wallet works and get him to download one onto their device. While receiving is literally instant at almost no cost, most want to try themselves sending some back to you which obviously is only possible after 10 blocks.

Still I wouldn't think sacrificing universal privacy would be a good option and maybe with new protocols like Seraphis with possible ring sizes it would be feasible to drop the requirement anyway by selecting a bunch of decoys from very recent transactions, maybe even unconfirmed. The latter might allow for instant-chaining in tx pool which is common on Bitcoin.

However, this would for sure require much bigger ring sizes and most probably even more research on decoy selection.

## Gingeropolous | 2022-01-04T14:28:44+00:00
> This doesn't solve any problem apart from sending multiple transfers that lock all your outputs in a row... Even then, it's an awful hacky solution that no average person should be expected to do.

That was sorta my point, hence the use of quotation marks. I don't think the current proposed solution solves it either. To me, it's equally as hacky - it's essentially "hey, well, in order to make monero more like bitcoin, we can remove some of the things that make monero monero." 

I whole heartedly agree that the 10 block lock is annoying and at odds with our ideal of money of the future, but this kind of solution seems like ... not a solution.

Hell, it's entirely possible that at some point the network hashrate is *so high* that it makes reasonable sense to reduce the 10 block lock to something lower... again, this isn't really a solution, but it's a hack that, in my opinion, doesn't chip away at monero's core protocol for the sake of convenience. 

I mean, at the surface, I kinda get it... like, these 0decoy transactions would essentially be treated as a pass-through on a tx graph. Like, yeah, tx A is linked to B right here, so it would just be clumped. So A -> B -> C would essentially be A -> C. So the default privacy for the user would depend on the users prior activity to ensure the privacy of the given transaction? 

And B wouldn't be a candidate used as a ring member for other users. 

So basically an attacker could flood the chain with 0decoy transactions, unless there's some limit on how many can be included per block, and then.... and then..... and then.... 

I dunno. To me, its like there's this well-oiled machine. And we're debating whether we should remove this cog over here because, well, is it really necessary *all of the time*? I dunno. 

Ultimately I hope my point thats being driven home is that, yes, I think this is an issue, but I don't think this is a solution. But I haven't done any academics on the topic. Need some simulations and demonstrations and confabulations and orchestrations and all the ions. 



## SamsungGalaxyPlayer | 2022-01-04T15:31:08+00:00
@LocalMonero @AlejandroGuariguata the idea as written is to effectively allow for transactions "without" ring signatures within a 20 (or so) block window. There are going to be severe privacy drawbacks with this if unaddressed.

This writeup describes some methods for mitigating these issues, though allowing this user experience is strictly worse for privacy, and even with mitigations, it's certainly problematic.

I'm not one to barge around saying that this privacy/UX tradeoff is completely horrible; clearly some applications like Haveno would benefit from not having to wait 10 blocks. However, the implications are worrying, even without getting into slippery slopes resulting from 2 classes of transactions. Earning this UX improvement comes at a privacy cost, period.

## LocalMonero | 2022-01-04T16:45:59+00:00
> Earning this UX improvement comes at a privacy cost, period.

It comes at a privacy cost *as far as you know*. The point of this MRL topic is to find ways to solve this problem without an unacceptable privacy cost. Hopefully, as this issue gains more traction we'll have more people looking into this problem and coming up with potential solutions.

## paulshapiro | 2022-01-04T16:47:37+00:00
I've been holding off replying since we'd need to hear from researchers and OGs like articmine, othe, Isthmus, the Noethers, luigi, etc on this one., but it struck me as unviable to begin with. Looks like an attack vector for a sufficiently well funded party and it's in place for a reason. As long as we're saying "there's no point to even researching chainable payments because of the possibility that it could harm privacy or segment outputs", I'd say we ought to be applying to same standard to any other decision, and we already know that zec shielded vs non-shielded does harm its privacy in practice. Monero's also an actual target, especially with real legitimacy and such low fees.

There does exist another alternative here. It doesn't entirely solve the problem, but I think it would get us pretty far. I even already have beta code for it which I intended to publicize soon, and have run it by a few people over the years.

At the moment, lots of e.g. pools will pay multiple pool members at a time with as few transactions as possible by including multiple destinations into the transactions. Meanwhile the majority of wallet software is creating transactions with two outputs - one going to the real recipient and one going back to the sender as either change or a dummy zero amount output to remain indistinguishable from txs with change. If you look at Isthmus's plot of the distribution of number of outputs generated by transactions (2-16) from ... 2019 or so, you can see maybe 20% have 16, maybe 60% have 2, and then there's a bunch of them in between.

At the moment we're using our lack of knowledge about the sources of these differently formed transactions as a proxy assumption for indistinguishability, but chances are, these populations are somewhat segmentable already.

Suppose we solve this problem at the same time as providing balances which are more likely to be liquidly spendable by creating a consensus rule that transactions always must have the Bulletproofs maximum of 16 outputs, and use, say, 6 of those extra outputs each transaction to decompose the change which is being sent back to oneself rather than lumping it into a singular change output which gets locked each transaction?

My team has done some analysis of this over the past couple years - I've had two CS grads work on it very lightly - and we found it actually allowed us to make an enhancement to the code quality around `create_tx` related to resolving the conflation of specification of the 'change addr' and the 'dests' passed in - this is incidental - but the analysis showed us that indeed the 16 output transactions do increase the size of each tx slightly, but that tx size increase does result in a higher payout to miners, as well as as plugging one of the last remaining fungibility gaps we have, aside from, I'd say, ring sigs themselves. 

What this would do is allow a wallet to accumulate "coins" and "notes" of different denominations in the form of multiple change outputs over time and for subsequent transactions, at the very least, the wallet software may have available to it some outputs to use at that time which are not already locked up in another transaction.

I recognize there is quite a lot of refinement which can be done in terms of selecting the denominations of the change outputs we're creating. At the moment our first-pass code only really just splits up the change into the set of outputs. I recall the wallet tx creation output selection algo already handles multiple existent outputs well.

By the way I suggest padding to 16 outs on txs rather than randomizing the number of outputs on txs because I believe this ends up with optimal privacy, since, for example, if we only randomize with an upper bound k of 16 minus the number of non-padding outputs which itself clearly varies across the userbase, you still end up with the question of how you harmonize your randomization with the networks', so 16 seems optimal.

What this suggestion does not solve is the fact that an output you have *just* received would remain locked until confirmation. 

There are some concerns I'm probably leaving out here but the actual code change to do this is pretty straightforward and modular, with only that `dests` modification I mentioned before required to mainline-crypto-core itself.

I first thought of this a couple years ago, but wasn't able to release the work publicly yet (soon[tm]) but I believe Monerujo is also working on something that sounds like this called PocketChange. 

## MoneroArbo | 2022-01-04T17:02:37+00:00
My initial concern with @paulshapiro's suggestion is that combining large numbers of inputs is also not great for privacy. If you have a TX that creates 16 outputs, then later recombine 6 of them, you'll have 6 separate ring sigs that each contain an output from a single previous TX. I think this would be a pretty strong heuristic.

I suppose one thing that might be done, is to have the decoy selection algorithm sometimes select decoys that also match this pattern; taking 6 outputs from a single TX and including them 1 per ring as decoys.

I'm not sure how well this would work with ring size 11/15 but maybe with Seraphis.

## janowitz | 2022-01-04T18:14:12+00:00
@paulshapiro thanks for sharing your interesting thoughts! However, I have a similar concern like @MoneroArbo since there are plenty of "mini" and "micro" tx, just think of pretty common uses paying for a VPN, VPS, domain or such. Splitting the change into 15 would mean for a user having 1 XMR as one single output having it split up into 30 after just two transactions, so you'd have to combine a pretty large bunch of them at some point and its most probably small output would be split up again into 15 even smaller ones. Combining a large bunch of (previously split up outputs yourself) is imo a high privacy concern, since you have a clear pattern in all your rings.

We'd need some research on that, with some simulations. Maybe instead of having at least two outputs, three would be better, already mitigating a lot of instant spending problems, since your change outputs would grow over time and combining would not impact privacy so much?

## MoneroArbo | 2022-01-04T18:38:56+00:00
@janowitz small correction, unless changed the standard wallet implementation prefers to create 2-input TXs when possible so in those cases the number of outputs would stay the same: 2 inputs consumed, 2 change outputs created. I think that's actually better though; it only makes sense to break a single output into change so many times. At some point you need to receive outputs that increase your balance.

Also they actually suggested 6 change outputs, not 15, and I think even that suggestion was arbitrary. The rest would be dummies, like the current empty output that's created when you have transactions with no change.

PS maybe this is too off topic since it's not technically about eliminating the lock?

## paulshapiro | 2022-01-04T18:50:40+00:00
All apparently valid and good observations, @MoneroArbo and @janowitz. I did not anticipate the output-group linkability thing, which seems obvious in retrospect, but again, likely is still an issue in many cases (people are certainly already combining multiple outputs in ways that are output-group-linkable). So it seems we should do some simulations and check how things turn out. 
The concern of accumulating and having to combine a huge number of outputs to accomplish a given transaction is there regardless, and should be managed at the output selection level, where the algo decides whether it wants to receive more change and/or combine multiple inputs for a given tx to manage that. 

However, the 3-output solution doesn't seem to really address the fungibility concerns for all the other users who need to send to more than one destination in a given transaction.

I would agree that the granular discussion should be taken to a new thread, from which this thread should be referenced.

## Gingeropolous | 2022-01-05T04:28:22+00:00
is there anything wacky that the new keys with all their different abilities can somehow tackle this issue? Or some key we didn't know we needed in order to get at this?

like, you send a blob that is a pre-transaction. It has everything but the ring members or some of them. Like, you send over ... gah I think im talking about payment channels ultimately. Because the question becomes well how does the sender guarantee that they won't craft their own transaction to counter the pre-transaction they sent over. 

but we could use some key so the receiver could know "ok this pre-transaction block checks out, the sender definitely has the monero needed for the transaction, but its obviously locked up in the 10 block lock because ring sigs are sooo much fun, so once that 10 block thing passes, this transaction blob will fire off".

i guess that doesn't permit chaining, per se. .. well it could, but then you end up in a weird payment channel thing. 

somewhere im not.... scatterbrained.....

## Gingeropolous | 2022-01-05T04:31:24+00:00
and also, in general, this might be a thing that is best solved on the mythical second layer. 

## DC4JG | 2022-01-06T12:24:27+00:00
The most important aspect of Monero is privacy. As far as I can tell this proposal would, in some way or the other, reduce the privacy or even could become a possible attack vector against Monero's privacy. That is a no go, even if it is implemented as an optional feature.

If this could be achieved without implications, it would be a great UX improvement and should be embraced.

In the meantime there might be a possible 'higher layer' feature which could be developed or made more accessible to users as a (partial) workaround to lessen the impact.

## cAP5L0CK | 2022-01-06T13:38:09+00:00
I do not comment here much, but I am also a long time Monero user.  This suggestion on it's face seems like a good idea for the reasons stated, but I think we must be EXTREMELY careful tinkering with the elements that make up the fundamental security of Monero's privacy.  A great deal of import is recently been put on Monero's use as CASH which is understandable since fungibility allows cash like transactions more than many other base properties of a crypto currency. 

But we MUST be extremely careful not to break Monero's privacy.  That is a tradeoff (particularly in the name of convenience) that I think is entirely not worth it.

I look forward to the input of some of the longer standing Monero community cryptographers and researchers on this very interesting, but potentially dangerous(?) idea.

## erciccione | 2022-01-06T14:06:28+00:00
Everyone involved in the conversation until now agrees that Monero's privacy shouldn't be lessened by the removal of the 10-blocks lock. Please let's keep that in mind when commenting. What we need is to find a way to make it happen without impacting the privacy of Monero users. Not easy and not clear if it will be possible, but as far as i can see we all agree it would be a huge improvement.

## trasherdk | 2022-01-11T04:09:31+00:00
> the modern instant economy and call your product the next generation of money. @LocalMonero  

In an economy where 1000 is less than the price of a decent red wine and more than some families monthly budget,
planning ahead is a must. You will not be able to spend that 1000 note in just any roadside mom-pop shop.

## ChristopherKing42 | 2022-01-11T20:44:43+00:00
Would it be possible to "0-conf" transactions that take 10 blocks to reach 1-conf? Like they just stay in the transaction pool until 10 blocks have been mined? Or would this have an adverse effect on privacy?

## UkoeHB | 2022-01-11T20:58:31+00:00
> Would it be possible to "0-conf" transactions that take 10 blocks to reach 1-conf? Like they just stay in the transaction pool until 10 blocks have been mined?

What would be the advantage to this?

## ChristopherKing42 | 2022-01-11T21:08:17+00:00
0-confs are popular for small transactions (for which I think two cups of coffee would count). Maybe even these delayed 0-confs would be fine.

A drawback is that any transaction that uses a recent transaction as a decoy must wait 10 blocks to 1-conf. It's not just when you spend a recent output. You might also need a consensus change to enforce this, since otherwise malicious wallets might specifically exclude transactions that are too recent to be mined immediately.

## UkoeHB | 2022-01-11T21:21:51+00:00
Do you mean compute a tx that fast-spends funds, but let it sit in the txpool for 10 blocks before mining it?

A) The tx can be invalidated if: reorg changes the order of outputs (invalidating output references if references are deterministic), reorg removes a ring member due to a double spend, reorg removes a real spend due to a double spend (if you are doing 0-conf then presumably this is not a concern).
B) Seraphis lets you do something like this already. You compute a partial tx without membership proofs and send it to the recipient, who can complete and submit it at a later date (via membership proof delegation). Doing that leaks the real spends of your tx to the recipient.

## ChristopherKing42 | 2022-01-11T21:26:10+00:00
> Do you mean compute a tx that fast-spends funds, but let it sit in the txpool for 10 blocks before mining it?

Correct!

## Hueristic | 2022-01-11T21:36:28+00:00
> Would it be possible to "0-conf" transactions that take 10 blocks to reach 1-conf? Like they just stay in the transaction pool until 10 blocks have been mined? Or would this have an adverse effect on privacy?

Interesting thoughts but wouldn't this allow bypass of dynamic block costs and open up spam attacks vectors?

## erciccione | 2022-05-18T08:04:13+00:00
I opened #102, which proposes to investigate the possibility of reducing the lock to <10 blocks. While i think that the best outcome would be to remove the lock entirely, worth exploring in parallel the possibility of reducing the lock to a lower numbers of blocks, since that should be easier to achieve.

## tevador | 2022-07-27T20:32:45+00:00
**Edit (May 2024): The proposal described in this comment is obsolete because it can't work with [full-chain membership proofs](https://gist.github.com/kayabaNerve/0e1f7719e5797c826b87249f21ab6f86).**

The reason for the 10-block lock time is to "confirm" the decoys and prevent the transaction from being invalidated by a chain reorg.

There are two ways how a reorg can break a transaction that has decoys from the "reorg zone":

1. The new chain contains the decoys but they have different output indices than on the original chain.
2. One or more decoys have been permanently eliminated from the new chain by a double-spend.

The first problem has an easy fix: reference decoys in the "reorg zone" the same way as Bitcoin does, i.e. using the TXID and output index within the TX.

The second problem requires a much more complex solution, but I think the drawbacks are acceptable.

The solution is two-fold:

1. Lowering the risk of selecting a decoy that's double-spending.
2. Lowering information leakage if a decoy is permanently eliminated from the chain.

Currently, the best way for an attacker to get a double-spend to be mined is to construct two transactions A and B spending the same output and broadcast them simultaneously to different parts of the network. Thus, network nodes will end up either with transaction A or transaction B in their mempool. If a miner mines a block with transaction A at roughly the same time as another miner mining a block with transaction B, it would be possible for a 3rd party to select a decoy that's about to be permanently invalidated.

Monero nodes already keep track of which transactions in the mempool are double-spending, but the problem is that such transactions are not propagated through the network. I propose that the P2P protocol is modified to relay information about double spends. There would be no changes to how the mempool works. Nodes would have an additional "double spend pool" with entries in the following format:

```
key_image
txid
alt_signature
```

* `key_image` is the key image being double spent. The pool would be indexed by this value and each node would only keep one record per key image to prevent this from being a DoS vector.
* `txid` is an ID of a valid transaction either in the node's mempool or in the blockchain.
* `alt_signature` is a valid ring signature that produces `key_image`, but is different from the signature in transaction `txid`. This is basically a cryptographic proof that someone has attempted to double spend the output.

Nodes would relay the list of double spending key images and, upon request, the cryptographic proof. After a small propagation delay, all nodes would eventually end up with the double spending key image in their "double spending pool". Entries would be removed from the pool some time after the double spent output has reached 10 confirmations. This should happen eventually as there must be at least one valid tx spending that output. The requirement to have at least one valid tx is to ensure that an attacker trying to flood the double spending pool will have to pay fees.

Now we can add a simple rule when selecting blockchain decoys:

**The outputs of a double-spending transaction are never selected as decoys in the reorg zone.** Otherwise decoys would be selected from all blocks, including the top block.

A side benefit of this change is that 0-conf transactions would become slightly more trustworthy.

An attacker can still double spend, but this would require colluding with a miner who has significant hashpower. If this happens, users affected by the double spend will have to submit a new transaction with a ring signature that doesn't contain the eliminated decoy. To avoid leaking the real output, the new transaction *must* use the same set of decoys as the original transaction (apart from the eliminated ones). This can be implemented in the wallet by temporarily storing the decoys of each spent output until all of the decoys have left the "reorg zone".

#### Advantages

* Reduction of the 10-block lock time to a 1-conf requirement.
* Does not introduce provably spent outputs.
* Slightly more trustworthy 0-conf transactions.

#### Drawbacks

* Additional RAM and bandwidth requirements for nodes.
* Possibly a lot of new code that would need to be reviewed.
* Does not completely eliminate the possibility of having a transaction invalidated by a reorg, but the chance would be very low and the impact limited.



## UkoeHB | 2022-07-27T21:17:46+00:00
> The first problem has an easy fix: reference decoys in the "reorg zone" the same way as Bitcoin does, i.e. using the TXID and output index within the TX.

AFAIK this does not work with deterministic references, which is required for any large reference set size.

> Does not completely eliminate the possibility of having a transaction invalidated by a reorg, but the chance would be very low and the impact limited.

This is true under stable network conditions, but what about unstable conditions when reorgs go deeper than the 2-3 blocks we typically see?


## tevador | 2022-07-27T22:07:52+00:00
> AFAIK this does not work with deterministic references, which is required for any large reference set size.

Yes, recent outputs would have to be referenced explicitly. Older outputs can use the deterministic method. This will somewhat increase the transaction size. I guess this belongs in the "drawbacks" column.

> This is true under stable network conditions, but what about unstable conditions when reorgs go deeper than the 2-3 blocks we typically see?

It should be fine unless we start seeing reorgs deeper than 10 blocks or malicious reorgs done by a miner specifically to double-spend (at the moment, there is probably only one miner capable of doing that with success - the minexmr pool).

## UkoeHB | 2022-07-27T22:13:32+00:00
> Yes, recent outputs would have to be referenced explicitly. Older outputs can use the deterministic method. This will somewhat increase the transaction size. I guess this belongs in the "drawbacks" column.

"Somewhat" might be an understatement here. If it's 16 bytes to store a hash of the referenced output, and with binning we can have like 8 bin members per bin (for example), that's already 128 bytes for one bin in the 'explicit references' zone.

## tevador | 2022-07-28T05:55:03+00:00
If there are just 1-2 bins in the reorg zone, this cost seems acceptable to me.

## iamsmooth | 2022-12-25T03:35:09+00:00
> No negative effects on privacy that I can see

The negative effect on privacy from these sort of recent-spending schemes is indirect. If you are spending a recent output, you will reference it, say explicitly by txid. In fact if you are doing so non-maliciously, the cost of doing so is negligible or zero (transaction is larger but presumably you decided this is a positive tradeoff for you vs. waiting).

However, if you are referencing a decoy, there is no particular reason to do this. You are potentially risking invalidation, and also directly increasing cost if you could reference older outputs by index but newer ones require a txid. Therefore, you can expect that cost-conscious wallets will (at least over time even if not right away) will tend to avoid including recent outputs as decoys. This introduces a statistical bias that weakens privacy.

You require that all valid transactions reference some recent decoys as a countermeasure. There might be further complications to this, I haven't completely thought it through. For example, referencing your own or some other known-non-malicious recent outputs (mining pools?) as decoys doesn't risk invalidation the way referencing unknown anonymous outputs from the pool might.

## tevador | 2022-12-25T11:05:43+00:00
> You require that all valid transactions reference some recent decoys as a countermeasure.

Yes, that was the idea. 1-2 bins would be required by consensus to be referenced by hash.

> There might be further complications to this, I haven't completely thought it through. For example, referencing your own or some other known-non-malicious recent outputs (mining pools?) as decoys doesn't risk invalidation the way referencing unknown anonymous outputs from the pool might.

The tx builder would rely on the double-spend propagation mechanism to make sure the selected decoys are non-malicious. The only realistic way to invalidate a recent output would be a malicious chain reorg, which has real costs that rational actors would not pay for temporarily invalidating a few transactions in the mempool.

## iamsmooth | 2022-12-27T04:35:40+00:00
@tevador For context, I wasn't replying to your double spend p2p proposal. My reply was intended to describe the purpose for the 10 confirmation rule and how it relates to privacy. To summarize, the incentives for using unknown outputs in one's own transaction depend on doing so having negligible cost/risk. To make that happen, 10 confirmations is set as a cutoff between deemed-negligible and deemed-non-negligible. The exact number is arbitrary of course, but the underlying purpose doesn't depend on the number.

As for your proposal, I don't think it entirely works because one of the ways for double spends, and reorgs to occur,  probably even non-maliciously, is network instability and fragmentation. In a fragmented network, spend attempts from the "other network" wouldn't propagate so double spends wouldn't necessarily be detected, and then the double spend notices won't propagate either. Also, you can't assume that everyone will use the p2p at all, it's ultimately optional. People can submit their transactions directly to a miner or be a miner. All that being said, It would likely improve things in the usual case, I think.

## tevador | 2022-12-27T11:01:02+00:00
> My reply was intended to describe the purpose for the 10 confirmation rule and how it relates to privacy

Although the topic of this discussion is how to eliminate the rule. I guess a possible outcome is "we can't eliminate it without significant drawbacks".

> As for your proposal, I don't think it entirely works because one of the ways for double spends, and reorgs to occur, probably even non-maliciously, is network instability and fragmentation.

The proposal already handles non-malicious reorgs. Transactions will stay valid even if the order of outputs in the reorg zone changes unless there is a double-spend.

In an unstable/fragmented network, double-spends would be easier to make, but this could be countered by waiting longer before selecting decoys from the top block (potentially only relaxing the 10-conf rule down to 2- or 3-conf rule). 

The only way to reliably make double-spends would be to collude with a miner. The cost of such an attack would be not just the transaction fees but also the lost block rewards from the unsuccessful reorg attempts (unless the malicious miner has over 50% of the network hashrate).

A successful attack would only cause a minor reduction of the effective ring size (from 128 to 120 in the worst case) and some hassle with having to re-submit a transaction (with seraphis, this can be done by anyone with view access to the wallet). I think those costs may be acceptable given the high demand for eliminating the 10-conf rule.


## iamsmooth | 2022-12-27T23:19:50+00:00
@tevador 

Double spends are not always malicious! They can happen due to wallet bugs or maybe not bugs but softer failures with not-quite-ACID-consistency or deployment issues (for example, the same keys being used on two different systems). 

Or people just doing weird things. In a decentralized network people come with "clever" ways to do things the may be arguably "wrong" but still not necessarily malicious. Not everyone will use the reference code, or code as good as the reference code (they think theirs is "better", even if wrong). They don't have to be reliable either, to still happen. Sometimes the weird things people do are unreliable (will double spend, but only rarely), or reliable under normal conditions but not well thought out for degraded or adverse conditions.

Also, I don't really have time to think carefully about your proposal but one issue I see is that double spend reports can be used to spam the pool. If you double spend and the report gets propagated, you are filling the pool without incurring any cost (since the double spend clearly won't get mined and incur a fee). This is similar to one of the reasons why double spends aren't propagated at all (if they were, everyone could detect that type of double spend just by looking at their local pool, no need for reports).

## iamsmooth | 2022-12-27T23:33:11+00:00
I do think that referencing recent outputs by txid might be enough to reasonable reduce the 10-conf rule to a lower number, maybe 2-3. If the routine 1-3 block reorgs (usually 1) that happen regularly don't break transactions that might be enough for people to not care. Double spends beyond a few blocks have to be quite rare and would likely always be so (deliberately it's an attack, as you say, and non-deliberately will be very rare since both non-malicious double spend and non-malicious deep reorgs are themselves both independently rare). The added cost of larger transactions might still be an issue where people disagree on the tradeoffs.

## tevador | 2022-12-27T23:55:24+00:00
> Double spends are not always malicious!

Accidental double-spends can happen (e.g. a wallet trying to spend a previously spent output due to a bug), but the second transaction will typically never get propagated or mined. So "accidental" double-spends can be ignored in this discussion because they will not have any practical impact.

> If you double spend and the report gets propagated, you are filling the pool without incurring any cost

You are paying fees for one of the two transactions that will get mined. Repeated double-spends (triple-spends etc.) of the same TX will not be propagated, so the attacker will need to keep paying fees if they want to keep spamming the pool. Note that this is different from actually propagating the double-spending transaction, which would strain the network without costing the attacker anything.


## iamsmooth | 2022-12-28T00:03:38+00:00
> but the second transaction will typically never get propagated or mined

They can be propagated by a different part of the network and mined by another miner who saw them first, though usually this would only happen if they're generated close to the same time (or during a network fragmentation). For example, consider a poorly-designed redundant wallet backend where the same output is spent to perform the same payment from two different nodes using different decoys. Some dumb exchange might do this (exchanges are high on the list of entities doing dumb things at the network level, including even paying unnecessarily high fees). It costs them nothing but can pollute the network.

> Note that this is different from actually propagating the double-spending transaction, which would strain the network without costing the attacker anything.

I think it is the same, as long as you don't propagate the triple spend. What you're propagating as a report is actually quite similar to the second transaction (continaing key image and signature), albeit abbreviated so lower absolute cost, but same principle. 

Either way means the spammer can spam the network once every time they make a transaction. Not catastrophic, but it's a cost to consider.

One other thing, I don't think 1-conf is quite enough even with your proposal, if you just received the block. If the double spend and the block happen about the same time you may receive the block before getting the double spend notification. You would need to wait a "reasonable" amount of time.

## tevador | 2022-12-28T10:16:29+00:00
> They can be propagated by a different part of the network and mined by another miner who saw them first

In theory yes, but it never happens in practice.

Does it even matter if a double-spend is malicious or not? The outcome is the same and the defense mechanism should be the same.

> I think it is the same, as long as you don't propagate the triple spend.

Validating the double-spend report is much faster than validating a full transaction (that includes range proofs, membership proofs etc.). The double-spend report is also smaller in size.

> Either way means the spammer can spam the network once every time they make a transaction. Not catastrophic, but it's a cost to consider.

Yes, it's even listed in the drawbacks of my proposal.

> You would need to wait a "reasonable" amount of time.

Yes, in practice you would only select decoys from blocks older than some threshold larger than the average time it takes to propagate a double-spend report.

## iamsmooth | 2022-12-28T21:38:43+00:00
> Does it even matter if a double-spend is malicious or not? 

Mostly not, as long as you consider 'deliberate' cases, even if not "intended" as malicious as well as accidental ones. The latter could be viewed as a natural phenomenon with a probability (even if not exactly known), but the former would depend on someone's decisions. It might never happen ("in practice") for a while and then happen a lot if someone (a high volume transactor) decides to do something stupid. Malicious and stupid is about the same.

> average time it takes to propagate a double-spend report.

What is the "average time" it takes if there is a network split? This is where you get into cases that aren't necessarily probabilistic in nature in the usual sense.

## tevador | 2022-12-28T22:42:59+00:00
> What is the "average time" it takes if there is a network split? This is where you get into cases that aren't necessarily probabilistic in nature in the usual sense.

In practice, there is a value that works in most cases and if it doesn't, the tx builder would just deal with the outcome. That's the price to pay for the elimination of the 10-conf rule.

## iamsmooth | 2022-12-29T04:33:29+00:00
> In practice, there is a value that works in most cases and if it doesn't, the tx builder would just deal with the outcome. That's the price to pay for the elimination of the 10-conf rule.

You can't assume that the tx builder actually cares about eliminating the 10 conf rule.  Some will some won't. Remember, the context here was explaining why the 10 conf rule benefits privacy, and the listing "no negative effects on privacy" isn't actually clear. The benefit of the 10 conf rule accrues because everyone is willing to use the same rule for selecting decoys, removing any biases. If that breaks down, then privacy suffers (it may only be a little, but let's recognize that for what it is).

## tevador | 2022-12-29T09:44:45+00:00
> You can't assume that the tx builder actually cares about eliminating the 10 conf rule.

This is a research topic how to eliminate the 10-conf rule and I contributed by proposing a solution that does exactly that (without introducing provably spent outputs). Whether it should be done or not is another question.

> the listing "no negative effects on privacy" isn't actually clear

I changed the wording to a more factually correct statement "Does not introduce provably spent outputs" to emphasize the main privacy benefit over the first proposal.

## kayabaNerve | 2023-06-28T19:29:59+00:00
As a mitigation to the 10-block lock, we could implement input splitting.

Instead of proving input A exists in tree, we state input B exists as A[0]. Input B takes A's linking tag.

Then, input C doxxes itself as a split spend, and exists as A[1]. It has a distinct linking tag, and a balance of A - B.

This requires a range proof be added to input B, to make sure it doesn't exceed A's balance. Then C would need to prove the existence of A *and B*, making it twice as expensive and require we maintain a separate tree.

I don't think this is worthwhile, yet found it sufficiently novel, and accordingly worth commentating.

## kayabaNerve | 2025-07-23T04:43:10+00:00
The argument for the 10-block lock is protection against re-organizations (re: DoS concerns from computational effort expended) and to prevent TXs from being invalidated on reorganization. TXs will still be invalidated on reorganization if they cite a reference which is removed from the blockchain. This means even with FCMP++, the lock makes sense.

Alternatively, you need a way where reorganized-out roots remain valid on the new blockchain (potentially via an additional block being mined which cites the orphaned chain as an uncle). The issue is if any transactions were reorganized out, the alternative root isn't valid as you can't distinguish if a TX spends one of the outputs reorganized out.

# Action History
- Created by: UkoeHB | 2022-01-02T03:32:27+00:00
