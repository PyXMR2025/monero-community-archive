---
title: Removing/Fixing/Encrypting monero's timelocks
source_url: https://github.com/monero-project/research-lab/issues/78
author: sedited
assignees: []
labels: []
created_at: '2020-10-21T23:14:03+00:00'
updated_at: '2024-10-16T01:03:28+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Following discussions during a #monero-research-lab meeting, see logs [here](https://github.com/monero-project/meta/issues/519), there seems to be some support for removing monero's timelock implementation. This issue should open further discussion on this topic. There are future use cases, for example payment channels and payment channel networks, that require some form of timelock, as described in the [DLSAG paper](https://eprint.iacr.org/2019/595.pdf).

Monero's timelock is used with the `unlock_time` field, which is available in every transaction. By default it is always 0. A user can choose to either set it to a block height, indicating until which block all the outputs of the transaction remained locked, or a timestamp, indicating until what time all the outputs should be locked. A user receiving an output in a timelocked transaction can only spend this output once it has expired.

The `unlock_time` field has a host of problems. I detailed most of them in a series of blogposts: https://thecharlatan.ch/Monero-Unlock-Time-Privacy/. 

The problems can be summarised in short:
1. 98% of its usage does not have semantic meaning. These are unlock_time values between 1 and 15 that have been expired shortly after genesis. Their usage does not lock up any monero. This weird pattern potentially allows linking these transactions to a single service.
2. Actual legitimate usage is really low. The 2% are a total of 195 transactions in the past 1'000'000 blocks that use the block-based locktime. Exactly one transaction used the time-based locktime, [a test transaction by Mitchell](https://twitter.com/Mitchellpkt0/status/1251621277179146240).
3. The ring member selection does not take the timelock values into account. An output mined a long time ago, but only recently expired is treated the same as any other output mined with it.
4. The timelock locks an entire transaction. Not just the recipient's outputs, but also any change or outputs of other recipients. If the lock is moved to a single output, change outputs become distinguishable.
5. The value range is very big, allowing to lock transactions until close to the heat death of the universe.

The `unlock_time` can be [encrypted](https://github.com/monero-project/research-lab/issues/65), which solves all these issues, but costs about a doubling in transaction verification time and a significant increase in transaction size. With current usage being so low, this is a high price to pay. If a legitimate use case arises the price becomes more acceptable though.

Alternatively, there are a number of things that can be done to improve the situation without increasing transaction size or verification time:
1. Use a more compact representation. Sensible values can be conveyed in as little as two bytes - a significant improvement over the current varint, which can represent up to a 8-byte/64-bit number
2. Only use block_height based unlock_time
3. Repair the ring selection by taking the unlock_time of selected outputs into account
4. Forbid the unlock_time to be set in the past apart from the 0 value

Even with these improvements, usage patterns can still emerge and leak significant information, for example identifying transactions from a special wallet that always sets the `unlock_time` 150 blocks into the future. I therefore support removing the field. If an actual use case appears in the future, timelocks canbe re-added in a fashion best fitting this use case (and hopefully encrypted).

# Discussion History
## SamsungGalaxyPlayer | 2020-10-22T00:42:58+00:00
I'm currently cautiously for the removal of the timelock field. In no case would I recommend adding encrypted timelocks in current form.

## apertamono | 2020-10-22T11:00:35+00:00
Yes, it makes sense to remove the timelock field and not to re-introduce it in encrypted form until we know what kind of precision is needed for a relevant use case.

## iamamyth | 2020-10-23T01:27:55+00:00
I've long disliked the current `unlock_time` semantics, precisely because they try to anticipate a use case by being overly generic and complicated, as you've stated. If the implementation were sound, but unused, I could see a case for preserving it, but, given that it has serious flaws, I favor scrapping `unlock_time`.

## apertamono | 2020-10-31T20:17:37+00:00
Just wondering, and this isn't a reason to keep it, but are there any practical objections to take into account, e.g. tools like explorers expecting the timelock field?

## iamamyth | 2020-10-31T20:49:47+00:00
I think it makes sense to keep the field in any existing RPC interfaces, as unlock times did (on rare occasion) exist for old blocks. So, there wouldn't be a compatibility problem. But, the RPC documentation should be updated to reflect the fact that the value will be fixed for all blocks after a certain point. And, care must be taken not to introduce an identically named field with alternate semantics later, as that could be a recipe for serious problems in existing clients (the clients could, of course, alter their interpretation of the field based on height, but that approach seems more likely to introduce errors).

## ghost | 2021-05-20T13:27:52+00:00
We used the timelocks as a way to verify the amount in the donation fund https://github.com/aeonix/aeon/issues/215. So not totally useless, yet also still very confusing how to use it. Would be better to just lock for `n` blocks rather than so many different behaviors. If there is a timestamp preferred better to have a separate function `lock_time` `lock_blocks`. Then no confusion. 

## b-g-goodell | 2021-05-21T14:48:46+00:00
Rather than removing, there should be a minimum timelock that actually
makes practical sense, and that should be enforced by consensus. This would
be preferable to removing time locks entirely, and less preferable than
encrypting them.

On Thu, May 20, 2021 at 7:28 AM yorha-0x ***@***.***> wrote:

> We used the timelocks as a way to verify the amount in the donation fund
> aeonix/aeon#215 <https://github.com/aeonix/aeon/issues/215>. So not
> totally useless, yet also still very confusing how to use it. Would be
> better to just lock for n blocks rather than so many different behaviors.
> If there is a timestamp preferred better to have a separate function
> lock_time lock_blocks. Then no confusion.
>
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/research-lab/issues/78#issuecomment-845121172>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AD2ZD7XYECDIJQTZMZPD4CLTOUE65ANCNFSM4S2NKZAA>
> .
>


## iamamyth | 2021-07-10T19:12:33+00:00
I think the issue wouldn't be whether the feature has a possible use, but whether that use justifies the overall code complexity (and also, relatedly, whether removing it likely increases long-term complexity due to likelihood of future re-introduction). Proving wallet balance via timelocks doesn't seem terribly compelling to me, one can achieve a similar end by simply executing periodic send-to-self transactions and publishing a viewkey. I suppose one can argue that timelocks actually improve privacy in this scenario, as they allow the daemon to reject guaranteed timelocked transactions, a database of which could be assembled for analysis, similar to mining pool payout data (note this argument also applies to encrypted timelocks).

Atomic swaps could require timelocks, but, to my knowledge, a lot of other pieces would have to fall into place for such a scenario to arise (i.e. no current atomic swap proposals use them on the Monero chain, depending instead on the alternate chain's timelock implementation).  

## UkoeHB | 2021-09-04T21:55:42+00:00
Unlock times have another drawback: they don't play well with deterministic ring member selection (see Issue #84).

Since any output could potentially be locked, if you deterministically select a locked output to be a decoy, then you have to rewind tx building to try a new ring member generation seed. That alone isn’t catastrophic, but binning makes it a big problem. What if the local outputs around the output you want to spend are all locked? There might not be enough decoy outputs available to make a bin with the real spend in it. This opens a serious attack vector.

There are a few solutions:
- Use hidden timelocks. Costly, but effective.
- Only append locked outputs to the set of unlocked on-chain outputs (for ring members selection) when they are unlocked.
  - Possible poison attack: make many poison outputs that unlock at the same time.
- Deprecate timelocks altogether (as recommended by this issue), and use the 'append at the end' method for coinbase outputs (which have a 60-block lock time enforced by consensus).

## Hueristic | 2021-09-04T23:48:05+00:00
>     * Use hidden timelocks. Costly, but effective.

Effective? 
Wouldn't this just increase cost of the attack as well which would not put it out of scope of some adversaries?

## UkoeHB | 2021-09-05T00:00:19+00:00
> Effective?
> Wouldn't this just increase cost of the attack as well which would not put it out of scope of some adversaries?

Hidden timelocks are hidden, there are no attack vectors. They would be enforced by range proofs.

## j-berman | 2021-09-22T06:23:26+00:00
## Current Status

Discussion on what to do with Monero's current timelock feature is ongoing. In the [last MRL meeting](https://github.com/monero-project/meta/issues/610), there seemed to be some support for deprecating the feature in either the hard fork after next, and/or in the hard fork that would bring the next major tx protocol change (such as Lelantus/Seraphis/Triptych). Deprecation is supported because of the feature's potential to introduce privacy issues, and its lack of compelling use cases. There also seems to be support that if a compelling use case is known that utilizes the feature, then it could be brought back (or kept).

In the rest of this post, I'll:

- present my view of pros/cons for deprecating vs. keeping as-is vs. encrypting
- highlight known use cases for Monero's timelocks
- highlight how the proposed protocols/implementations for atomic swaps and payment channels on Monero work around the Monero timelock's limitations

## Pros/Cons of Deprecating/Keeping/Encrypting

### Deprecating

**Pros**

- eliminates issues of privacy arising using timelocks (discussed in greater detail [here](https://thecharlatan.ch/Monero-Unlock-Time-Privacy/))
- allows for a safe/smooth implementation of "binning", which seems to be a generally supported upgrade for the decoy selection algorithm (discussed in greater detail [here (6.2)](https://arxiv.org/pdf/1704.04299/),#84, and #86)
- eliminates griefing vector for malicious party to send unspendable outputs to a service provider who does not correctly check unlock time (described [here](https://github.com/monero-project/research-lab/issues/78#issuecomment-925312477))

**Cons**

- gets rid of the known niche use cases discussed below
- makes it more difficult to bring back if some compelling use case emerges

### Keeping as is (& enforcing sensible minimum as proposed [here](https://github.com/monero-project/research-lab/issues/78#issuecomment-846005365))

**Pros**

- enables niche use cases discussed below
- researchers/programmers may be more inclined to consider the feature for some compelling use case in the future

**Cons**

- maintains some issues of privacy arising using timelocks (discussed in greater detail [here](https://thecharlatan.ch/Monero-Unlock-Time-Privacy/))
- makes a "binning" strategy in the decoy selection algorithm marginally more dangerous/complex/challenging to implement (reasoning highlighted [here](https://github.com/monero-project/research-lab/issues/78#issuecomment-913046076))
- maintains griefing vector for malicious party to send unspendable outputs to a service provider who does not correctly check unlock time (described [here](https://github.com/monero-project/research-lab/issues/78#issuecomment-925312477))

### Encrypting

**Pros**

- eliminates issues of privacy arising using timelocks (discussed in greater detail [here](https://thecharlatan.ch/Monero-Unlock-Time-Privacy/))
- allows for a safe/smooth binning implementation
- enables niche use cases discussed below
- researchers/programmers may be more inclined to consider the feature for some compelling use case in the future

**Cons**

- roughly doubles transaction verification time and is a significant increase in transaction size
- development time/adds some complexity to the code & consensus
- the use cases for the feature aren't very compelling yet
- maintains griefing vector for malicious party to send unspendable outputs to a service provider who does not correctly check unlock time (described [here](https://github.com/monero-project/research-lab/issues/78#issuecomment-925312477))

## Known use cases

### Proof of unspent funds

As highlighted [above](https://github.com/monero-project/research-lab/issues/78#issuecomment-845121172), timelocks can be (and have been) used to have an entity prove they have unspent funds.

The prover constructs a tx where the amount of funds are locked in an output until block X, then the prover provides the tx key for the transaction before block X to a verifier.

[Also highlighted above](https://github.com/monero-project/research-lab/issues/78#issuecomment-877689472), a prover could instead re-construct tx's and provide tx keys (or a view key) on request, without needing to lock outputs at all. However, this has a privacy issue where publicly revealed outputs are more likely known spent via this method (e.g. you had this much Monero *then*, and likely re-sent *that output* to yourself in *this tx* = link from *this tx* to prior tx = known spent output on chain).

### Subscription model

This is a creative idea with some known privacy/UX/technical challenges shared by @moneromooo-monero in #monero-dev. Let's say a user wants to sign up for a subscription service, has all the Monero up-front ready to go for the service, wants the option to pay monthly, and wants the option to cancel the subscription at any time.

A user could sign (and not broadcast) a number of transactions that each have 2 inputs. 1 input is a normal output, and the other input in each transaction is an output that is locked *until the start date of each month's billing cycle*. The user could then send *all* the transactions over to the service provider. The service provider could then broadcast each transaction at the start of each billing cycle. Before each transaction is broadcast, the user has the option to spend the normal output in all the transactions sent to the service provider, which would effectively render the pre-signed transactions impossible to broadcast to the network, thereby "canceling" the subscription.

The privacy issues with this approach are:
- unless there is a pool of a bunch of locked outputs (that are locked until the same exact date of the start of each billing cycle) that the user can use to construct the transactions in advance, the service provider would be able to deduce which output is the one being spent in each transaction (by seeing which output is locked). Therefore linkability to a prior tx is broken.
- transactions constructed this way would have a particular trace on chain (their rings would reference outputs way in the past, rather than recent outputs). This affects sender/receiver privacy, and affects other transactions on chain.

UX challenges:
- user would need to submit an equivalent number of transactions to create outputs that lock until the specified dates.
- user would need to re-do the process once all pre-signed transactions have been broadcast.

An alternative way of supporting a subscription model would be for a wallet to support an "auto-pay" feature that would send out payments to intended recipients when the wallet is running.

### Extreme budgeting/exec payouts

Similar to the concept of "vesting" and/or restricted stock, you could send an output to someone that does not allow them to use it until a later date. However, unlike restricted stock, the sender can't reclaim the the funds after sent.

## Misunderstood non-use cases for Monero's timelocks

In the latest MRL meeting and in ensuing conversation, there was also some confusion over the use cases that Monero's current timelocks have (in atomic swaps/payment channels), so summarizing what I've surmised since then: Monero's timelocks as currently designed are limited to niche use cases, and are not useful for atomic swaps and payment channels AFAIU. The critical ingredient for swaps/channels is the ability for a recipient to claim the output before the timelock expires, and if not, the output is refunded to the sender. However, Monero's timelocks do not enable this. Monero's timelocks strictly lock an output for a specified period of time, preventing the recipient from spending the output until the timelock expires.

### Atomic Swaps

@iamamyth appears correct in saying the current swap implementation only relies on Bitcoin's HTLCs, and not Monero's timelocks. The protocol uses adaptor signatures to work around Monero timelock limitations. From [the COMIT paper](https://arxiv.org/pdf/2101.12332.pdf):

> Within this work we present our current efforts on cross-chain atomic swaps
using adaptor signatures. In particular, we show how adaptor signatures can be
employed to swap between Monero and Bitcoin. Notably, the former does not
support scripts or timelocks.

Also from Daniel over at COMIT:

> we are not building on top of [Monero's timelocks] at the moment and I don't think there are any plans to do so. So I don't think we would be advocates for needing it (at least at the current point in time).

### Payment Channels

#### [DLSAG: Non-Interactive Refund Transactions For Interoperable Payment Channels in Monero](https://eprint.iacr.org/2019/595.pdf)

This would essentially be a fundamental change to Monero's tx protocol that would allow for refundable transactions, and would need a hard fork to support. Additionally, it's what introduces the concept of hidden timelocks in the first place. Basically, as I understand it, timelocks as currently constructed are not useful for the payment channels proposed in this paper without a separate hard fork that would allow for someone to claim an output *before* the timelock expires.

#### [PayMo: Payment Channels For Monero](https://eprint.iacr.org/2020/1441.pdf)

> One of the main challenges that we face in constructing a fully-compatible [payment channel] for Monero is the lack of a time-lock functionality of its scripting language. To “simulate” this functionality off-chain, our constructions will resort to the usage of time-lock puzzles.

The basic idea behind time-lock puzzles is that a recipient would take a pre-determined amount of time to solve the puzzle off-chain, such that they can spend the output with the solution to the puzzle. It's a workaround to simulate the expected "refund" mechanism of timelocks, the mechanism that Monero's timelocks don't presently support.

EDIT: modified the "keep as is" option to "keep as is (& enforce a sensible minimum)"
EDIT2: clarified PayMo
EDIT3: added griefing vector described [here](https://github.com/monero-project/research-lab/issues/78#issuecomment-925312477)

## Rucknium | 2021-09-22T08:29:23+00:00
@j-berman For the subscription model, this approach may yield some insight:

https://bitcoincashresearch.org/t/introducing-arcc-allowable-revocable-contract-chain-system-for-bitcoin-cash/522

## ghost | 2021-09-22T14:53:33+00:00
Subscription model makes no sense - no subscription I've ever had locks X amount of payments ahead of time.

## UkoeHB | 2021-09-22T14:55:46+00:00
> Subscription model makes no sense - no subscription I've ever had locks X amount of payments ahead of time.

The point is - how can you have scheduled payments that can be canceled (i.e. without pre-paying all months) in Monero? The method he described is one of the few available methods, even if not very appealing UX.

## iamamyth | 2021-09-22T17:20:30+00:00
I agree that the subscription use case makes very little sense: The subscriber needs to record which transaction to broadcast in order to cancel the subscription, meaning there must be client-side support for subscription tracking and cancellation. If the client must perform such bookkeeping, it seems easier for it to simply record addresses and frequencies of subscriptions, and auto-pay at the appropriate time.

The following is not, and should not be considered, investment advice: I think the "vesting" concept strains credulity, as vesting schemes involve selling an issuer's contractual right in a common enterprise. There's no common enterprise here, and minting Monero has a cost, so why would anyone deliberately lock it away? The act of locking itself introduces a negative return, which isn't really the case with unvested stock.

## ghost | 2021-09-22T17:29:08+00:00
> > Subscription model makes no sense - no subscription I've ever had locks X amount of payments ahead of time.
> 
> The point is - how can you have scheduled payments that can be canceled (i.e. without pre-paying all months) in Monero? The method he described is one of the few available methods, even if not very appealing UX.

Features should reflect real world habits and use cases. No need for complicated UX to solve a nonissue - if you have the funds for a yearly subscription upfront you usually get a discount  to pay in full. This is one instance where the market decides.

## UkoeHB | 2021-09-22T17:33:12+00:00
> Features should reflect real world habits and use cases.

Ok... academically, it is our responsibility to enumerate theoretical use cases. After enumerating them, then you can assess practicality and usability. Which you have been doing, but I want to be clear that @j-berman is not in the wrong for discussing subscriptions.

## ghost | 2021-09-22T17:34:03+00:00
I understand, but no one sets aside a year worth of payments upfront. Otherwise they'd just pay in full.

The idea of recurring payments is interesting, but I don't think locking up funds for future payments is the solution.

## iamamyth | 2021-09-22T20:39:09+00:00
I think you're missing an important downside to timelocks: They require recipients to check the timelock status of received funds. I've seen cases where service providers fail to implement such checks and end up with effectively unspendable funds. 

## j-berman | 2021-09-23T08:52:01+00:00
To be clear, I'm also in favor of deprecating Monero's timelocks as is. I think the privacy/safety benefits far outweigh the potential niche use cases. I'm just trying to give as much weight as possible to the counter-arguments. I figure it's best to be cautious in deprecating a feature. Perhaps we could give it another month or so, and if no compelling counter-arguments emerge, we could more officially pencil it in for deprecation in a later hard fork (not this hard fork, but the one after, or the one with the tx protocol change). Most seem strongly in favor of removing it when it's brought up for discussion in #monero-research-lab/#monero-dev as well.

In any case, I also agree the subscription model described (and "vesting" concept described) is (are) probably not useful in practice. Perhaps the ideas may inspire other ideas and seemed worth sharing to be comprehensive. You could in theory combine the concepts to have a "cancelable" payout schedule for whatever purpose, however, I believe the core of the privacy/UX challenges of that use case remain, and there are probably better ways to support that use case anyway. I would agree that delayed cancelable payouts (with significant privacy/UX challenges) probably not compelling enough to support keeping the timelock feature when weighed against the cons.

So far it seems the "proof of unspent funds" feature may be the most compelling use case for keeping Monero's timelocks as is, though I personally feel the alternative methods of achieving this use case today are suitable. Fleshing out some alternative methods of achieving this use case:

## Simply provide a tx key for a single new on-chain tx

A prover submits a new tx to themselves with an amount they want to prove, then provides a verifier with the tx key/address pair.

In @yorha-0x 's case for example, I'm not seeing why not simply say to the prover: "on future date X, please send yourself a tx containing the amount of funds you're in control of, and give us the tx key to verify." The drawback to this approach versus using a timelock is that a verifier can't be certain that the prover doesn't spend the output *after* the tx entered the chain, and *before* some later date. But is that really necessary?

As far as holding an entity accountable, I don't see why there is practical value to a verifier in ensuring the prover remains in control of the funds for some small period *after* the date the output was constructed. I also don't see major institutions (such as exchanges) locking up outputs for meaningful periods of time for the timelock use case to be useful.

## get_reserve_proof / check_reserve_proof

This method allows a prover to prove control of unspent funds without an on-chain tx, and allows the verifier to know exactly when the outputs are spent in the future.

It's offered by the reference wallet and is documented [here](https://www.getmonero.org/resources/developer-guides/wallet-rpc.html#get_reserve_proof) and explained further [here](https://monero.stackexchange.com/questions/9991/how-does-the-get-reserve-proof-command-work). Copied from `monero-wallet-cli`'s description of the command (and that 2nd link):

```
Command usage: 
  get_reserve_proof (all|<amount>) [<message>]

Command description: 
  Generate a signature proving that you own at least this much, optionally with a challenge string <message>.
  If 'all' is specified, you prove the entire sum of all of your existing accounts' balances.
  Otherwise, you prove the reserve of the smallest possible amount above <amount> available in your current account.
```

Basically the proof is composed of all (or < amount >'s worth of) the unspent outputs in a wallet, the key images for those outputs, key image signatures to prove the outputs correspond to the key images, and shared secrets to know the outputs were sent to a given address.

The drawback (or pro, depending on context I guess) with this approach is that a verifier will know exactly when the outputs are spent in the future. There are some (imperfect) mitigations to this drawback, but I feel it would be out of scope of this issue to get deep into it.

## Conclusion

I don't think the timelock adds much practical value compared to alternative methods of proving unspent funds.

## ghost | 2021-09-24T17:18:38+00:00
That is good. Timelock proof of funds is one use case but that is confusing because it is not the intended use. The reserve proof is better. Optionally privacy for spent outputs could be added. 

I can believe vesting would be a useful tool in what @j-berman says. Proving you have a vested holding in monero for a set duration of time in order to perform some role. 

## carrington1859 | 2021-10-02T14:36:59+00:00
Regarding the get_reserve_proof method and the drawbacks, it seems that if you were being audited you would first consolidate you inputs and then go through a churning process if you didn't want the reserve proof to impact you past/future privacy.

I've seen no compelling case for keeping timelocks.

## Minthos | 2021-10-04T03:24:12+00:00
I keep most of my stack timelocked at all times to force myself to hodl and protect against the $5 wrench attack. I agree the interface is clunky but I would prefer to keep the functionality.

## j-berman | 2021-10-06T06:53:05+00:00
Highlighting some more use cases from reddit

#### [Comment 1](https://www.reddit.com/r/Monero/comments/q0oiln/proposal_to_remove_timelock_feature/hfazxfh/)

> I staunchly oppose this and love this feature. I know I’m a fringe use case but I depend on it; my compulsions, addictions, and lack of sobriety or discipline cause me to do stupid things.

#### [Comment 2](https://www.reddit.com/r/Monero/comments/q0oiln/proposal_to_remove_timelock_feature/hf9z4iw/)

> Didn't know that xmr had a time lock option... Its use case seams to be to inconvenience the receiver. Now why would a sender want to inconvenience the receiver ?
1 sending it to yourself as self control action to prevent spending and force holding
2 sending to someone to prevent them from spending fast.(eg. send 12 transactions, but let every one unlock month by month, so maybe your kinds don't spend it all at once )
3 forcing the receiver to become a hodler against their will to functionally increase xmr price by removing it from circulation (remember goldfinger from James Bond)
4 send some xmr asap , but some time locked to the monero donation address to give incentive to maintain the project
4.1 demand that some exchanges accept time locked xmr to diminish damage from rug pulling and incentivize long term operations.
4.2 To partially prevent day trading
5 locking it from yourself for a period of time so that it cant be stolen by someone coercing you, wrench attack.
5.1 inform potential attackers that your xmr is time locked so they cant get it within the next 10 min, 24h or a week or month or some other time. As a deterrent from fast wrench attacks, torture-mutilations to get the xmr fast and or making long term kidnaping impractical.

## neptuneresearch | 2021-10-13T01:59:52+00:00
Here is an updated look at on-chain usage of `unlock_time`. 

TheCharlatan's last blog article "Monero timelock woes" on October 10, 2020 covered up to height 2,197,574 (date 2020-09-29), here is the data since then: from height 2,197,574 to height 2,466,799 (date 2021-10-09). 

Of the 7,907,125 transactions in this height range, 775 transactions (0.01%) used `unlock_time`. Their `unlock_time` values can be grouped as follows:

| Value group                               | Number of transactions    | % of `unlock_time`-using transactions since height 2,197,574 |
| -                                         | -                         | -                                                            |
| Never locked, value < 15                  | 623                       | 80.4%                                                        |
| Never locked, value 751,000 - 753,000     | 66                        | 8.5%                                                         |
| Never locked, value close to transaction's block height but lesser than | 3                         | 0.4%                                                         |
| Block height lock, value between transaction's block height and `CRYPTONOTE_MAX_BLOCK_NUMBER = 500000000`                         | 83                        | 10.7%                                                        |
| Timestamp lock, value greater than `CRYPTONOTE_MAX_BLOCK_NUMBER = 500000000`                            | Not used                  | Not used                                                     |

## Reproducing the same plots from "Monero timelock woes" with the previous year's data:

### 1. `unlock_time` usage

![block_height x log tx_unlock_time](https://user-images.githubusercontent.com/39543276/137052394-e75384bd-564c-48f4-8238-c257473e4e95.png)

### 2. Usage distribution of low values

| unlock_time            | 1     | 3     | 10    | 11    | 12    | 13    | 14    |
| -                      | -     | -     | -     | -     | -     | -     | -     |
| Number of transactions | 143   | 24    | 121   | 105   | 103   | 82    | 45    |

TheCharlatan's conclusion still applies here as before: "Either somebody forgot to add the current block height on top of the desired amount of locked blocks, or they are misusing the field to convey some extra information."

### 3. "The difference between a meaningful block height `unlock_time` and its mined height, revealing the actual number of blocks each transaction is locked for"

![block_height x lock_for_n_blocks](https://user-images.githubusercontent.com/39543276/137052407-1408cf4d-3a96-4cdb-a699-38818b8be422.png)

That picture is wide, so here is another version that uses log scale on the amount of locked blocks:

![block_height x log lock_for_n_blocks](https://user-images.githubusercontent.com/39543276/137052423-54c2906a-29b5-419a-a8e1-01d82fc7f81a.png)

Also note that in the previous year, each amount of locked blocks was only used once or twice; the most repeat usage was where the 0 (`unlock_time = block_height`) and 1 (`unlock_time = block_height + 1`) block amounts were each used exactly 3 times. In the previous year at least, there are really no puddles like "Transactions locked for exactly N blocks".

| Number of occurrences | Unique amounts of blocks each tx is locked for|
| -                     | -                                             |
| 1                     | 45 different amounts                          |
| 2                     | 16 different amounts                          |
| 3                     | 2 different amounts (values `0, 1`)           |

## tevador | 2021-11-12T08:49:27+00:00
> I keep most of my stack timelocked at all times to force myself to hodl and protect against the $5 wrench attack. I agree the interface is clunky but I would prefer to keep the functionality.

This can be done entirely off-chain using a [time-lock puzzle](https://people.csail.mit.edu/rivest/pubs/RSW96.pdf).

I'm in favor of the removal. All of the mentioned use cases have better alternatives.

## sboulden | 2021-11-15T20:01:31+00:00
Hi, I would just like to voice my opinion & support for keeping the locked_transfer feature.

I recognize & understand that my use case for my locked_transfers may not appear legitimate & necessary to just about anyone, but I'd like to express it anyway.  

I made a decision several months ago to lock away about 25% of my Monero for 1,000,000 blocks.  This was done as a form of impulse control, fueled by me admitting to myself that my lack of self-control, lack of self-discipline, and (sometimes) lack of sobriety has caused me to FOMO my XMR into other crypto projects and regret it later.  I spend too much time watching markets & charts with an addictive personality, and locking my balance away was the perfect solution to guard me from bad decisions.

Had Bitcoin had a locked_transfer feature back in 2010, I certainly would be in a nicer place financially than I am now.  Being a long-term XMR bull, and committing to not selling for 5-10 years, I made a full commitment to lock a significant sum of Monero for the maximum time of 1,000,000 blocks (~3.8 years).  I want absolutely no amount of panic & bearish fear to cause me to irrationally sell too early.  Now, it is fully out of my hands, no matter how desperately I would want to sell in any mental state, I am forced HODL!

Had the CLI allowed for a time limit longer than 1,000,000 blocks, I certainly would have done so.  I have a desire to schedule myself an annual birthday gift of 1 XMR every year for the rest of my life.  It seems like something that future me would look back at with appreciation.  I can't predict what the market will look like in the year 2035, but most likely I would have sold the majority of my Monero on various pumps by then, if it were up to me.  Having the locked_transfer would completely take this off the table.

(/u/rbrunner7 had a funny comment on [this reddit thread about the topic](https://redd.it/mwrm6g) about compiling your own wallet to extend beyond the 1,000,000 block limit)

I personally would not want to take this feature off-chain.  Anything involving a "trusted" 3rd party escrow is completely off the table.  I really like having the transaction on-chain, confirmed, the balance is perfectly visible in my wallet (despite being locked), and provides peace of mind.  It's already a completed and confirmed transaction, and I have high confidence it can't go wrong while waiting to unlock.  

The current implementation of this feature is simple, seamless, and easily executed in 1 command just the same as any transaction.  I did not look into @tevador 's time-lock puzzle, but the idea of offchain multisig puzzles just sounds overwhelming on the surface.  I would be worried that a future hardfork could cause the multisig to not execute and fail due to incompatibility.

The duality of the argument that these locked_transfers take up extra space on the blockchain, while also demonstrating that they are VERY rare in quantity, seems like a non-issue.  Using a few extra bytes on a tiny sum of transactions feels very affordable.

However, I do concede that the griefing vector could be problematic, although completely avoidable by simply having recipient wallets check for locked outputs.

All that being said, I completely understand if my use case does not seem "real" or compelling enough.  If I were in your shoes, I wouldn't find this to be a compelling argument either.

I just really want to voice support for keeping the feature, as I do intend to keep using it, and it has already saved me from selling my Monero during multiple moments of weakness.  I would like to see it stay.

## ghost | 2021-11-15T20:19:48+00:00
I don't see why hodling needs to be enforced at the protocol level.

You say it forces you to not sell but what if you were in an emergency and needed those funds?

‐‐‐‐‐‐‐ Original Message ‐‐‐‐‐‐‐
On Monday, November 15th, 2021 at 3:01 PM, sboulden ***@***.***> wrote:

> Hi, I would just like to voice my opinion & support for keeping the locked_transfer feature.
>
> I recognize & understand that my use case for my locked_transfers may not appear legitimate & necessary to just about anyone, but I'd like to express it anyway.
>
> I made a decision several months ago to lock away about 25% of my Monero for 1,000,000 blocks. This was done as a form of impulse control, fueled by me admitting to myself that my lack of self-control, lack of self-discipline, and (sometimes) lack of sobriety has caused me to FOMO my XMR into other crypto projects and regret it later. I spend too much time watching markets & charts with an addictive personality, and locking my balance away was the perfect solution to guard me from bad decisions.
>
> Had Bitcoin had a locked_transfer feature back in 2010, I certainly would be in a nicer place financially than I am now. Being a long-term XMR bull, and committing to not selling for 5-10 years, I made a full commitment to lock a significant sum of Monero for the maximum time of 1,000,000 blocks (~3.8 years). I want absolutely no amount of panic & bearish fear to cause me to irrationally sell too early. Now, it is fully out of my hands, no matter how desperately I would want to sell in any mental state, I am forced HODL!
>
> Had the CLI allowed for a time limit longer than 1,000,000 blocks, I certainly would have done so. I have a desire to schedule myself an annual birthday gift of 1 XMR every year for the rest of my life. It seems like something that future me would look back at with appreciation. I can't predict what the market will look like in the year 2035, but most likely I would have sold the majority of my Monero on various pumps by then, if it were up to me. Having the locked_transfer would completely take this off the table.
>
> (/u/rbrunner7 had a funny comment on [this reddit thread about the topic](https://redd.it/mwrm6g) about compiling your own wallet to extend beyond the 1,000,000 block limit)
>
> I personally would not want to take this feature off-chain. Anything involving a "trusted" 3rd party escrow is completely off the table. I really like having the transaction on-chain, confirmed, the balance is perfectly visible in my wallet (despite being locked), and provides peace of mind. It's already a completed and confirmed transaction, and I have high confidence it can't go wrong while waiting to unlock.
>
> The current implementation of this feature is simple, seamless, and easily executed in 1 command just the same as any transaction. I did not look into ***@***.***(https://github.com/tevador) 's time-lock puzzle, but the idea of offchain multisig puzzles just sounds overwhelming on the surface. I would be worried that a future hardfork could cause the multisig to not execute and fail due to incompatibility.
>
> The duality of the argument that these locked_transfers take up extra space on the blockchain, while also demonstrating that they are VERY rare in quantity, seems like a non-issue. Using a few extra bytes on a tiny sum of transactions feels very affordable.
>
> However, I do concede that the griefing vector could be problematic, although completely avoidable by simply having recipient wallets check for locked outputs.
>
> All that being said, I completely understand if my use case does not seem "real" or compelling enough. If I were in your shoes, I wouldn't find this to be a compelling argument either.
>
> I just really want to voice support for keeping the feature, as I do intend to keep using it, and it has already saved me from selling my Monero during multiple moments of weakness. I would like to see it stay.
>
> —
> You are receiving this because you commented.
> Reply to this email directly, [view it on GitHub](https://github.com/monero-project/research-lab/issues/78#issuecomment-969270555), or [unsubscribe](https://github.com/notifications/unsubscribe-auth/AKKABDDRPRBKPN3YKTW4XHTUMFRKPANCNFSM4S2NKZAA).
> Triage notifications on the go with GitHub Mobile for [iOS](https://apps.apple.com/app/apple-store/id1477376905?ct=notification-email&mt=8&pt=524675) or [Android](https://play.google.com/store/apps/details?id=com.github.android&referrer=utm_campaign%3Dnotification-email%26utm_medium%3Demail%26utm_source%3Dgithub).

## sboulden | 2021-11-15T20:28:53+00:00
And that's fine.  As I emphasized (twice), I really don't expect anyone to see my opinion as anything other than nonsense.  It's a perfect solution for me personally, and so far there have been zero comments in support of keeping the feature, so I felt it would be productive to add the perspective of someone who legitimately uses the functionality.

I prefer it enforced at the protocol level because I had never known of any other way to securely pull this off.  I saw several highly upvoted comments about doing this with a "trusted 3rd party escrow" and I could only shake my head at the absurdity of those words.

The whitepaper on time-lock puzzles is very dense, and doesn't give me direction on where to find an alternative solution off-chain.  If you could provide a simple guide for an alternative locking mechanism which is fully secure, fully decentralized & trustless, future hardfork-proof, and working right now, then I would absolutely test it out and switch.  👍 

---
(As far as my emergency fund situation, I don't believe this question is relevant to the topic of deprecating the feature.  But just to provide an answer - I do not invest more than I can afford to lose, I still kept about 75% of my Monero unlocked, and I have a comfortable balance in my fiat savings account of liquid capital which is adequate to any foreseeable scenarios.)

Would anyone be able to provide an easy step-by-step writeup to creating locked transfers off chain for me?

## ghost | 2021-11-15T20:39:46+00:00
For the paper tevador referenced, my understanding is it is basically a difficult problem that takes computation time to solve like proof of work hashing. That works okay for locking your own coins because you can just throw away the secret once you have created the puzzle. It fails for trusting that others have locked their coins. The puzzle will always require that the original secret was discarded.  If you want to know if another person has locked their coins, that requires a third party arbiter to control a secret. That is why the timelock puzzle is not an appropriate substitute for this mechanism. I don't see how it is possible to replicate this functionality off chain without trusted third party to keep a secret. 

## sboulden | 2021-11-15T20:47:37+00:00
I appreciate you taking the time to hear me out.

I'm not about to die on this hill.  I get it.  If the feature is deprecated, I will be just fine.

I would obviously prefer if there is an alternative and equally secure & viable method first, before deprecation.  But again, I get it, and maybe this is simply a neat feature that will become a relic.  This always struck me as a very cool, albeit tiny, QoL feature that no other crypto has.  

## dysbulic | 2021-11-17T16:21:16+00:00
A use that I'm familiar with from Bitcoin that I was hoping to use with Monero is timelocking as a failsafe on an escrow.

The escrow service signs a 2/3 transaction timelocked for the future and sends it to the buyer. If the deal falls through ultimately they can get their money back by signing and submitting that transaction.

Reading this issue though, it seems like maybe it wouldn't work since people are saying your timelocks aren't appropriate for lightning, and this is similar. That, and I'm uncertain the way y'all do multisignature transactions is compatible either.

It's unfortunate. I'm contemplating a serverless market and that has a trusted third party while the transactions are being done, but there's no long term instance to be shut down.

## tevador | 2021-11-28T14:26:44+00:00
When deciding whether to remove timelocks, we should consider all the pros and cons. At the moment it looks like the pros of removing positively affect the majority of users (improved privacy, protection from malicious transactions), while the cons only affect a small minority.

> If you want to know if another person has locked their coins

What are some practical use cases of this? As mentioned above, the current timelocks are not suitable for payment channels and atomic swaps. This limitation can be worked around by using a 2/2 multisig address with some kind of "punishment" script on another blockchain if the other party misbehaves.

> The escrow service signs a 2/3 transaction timelocked for the future and sends it to the buyer. If the deal falls through ultimately they can get their money back by signing and submitting that transaction.

This will not work. The timelock doesn't prevent the transaction from being submitted to the network, just none of the outputs can be spent until the timelock expires. The buyer would be able to steal the funds immediately and spend them later.



## beshanoe | 2021-12-30T17:59:11+00:00
One of a very smart timelocks usages in bitcoin and liquid is by Jade hardware wallet. It uses 2of2 multisig on funds where the second signature comes from 2FA of their centralized server. But if they go bankrupt and 2FA server is no longer working the funds can be released using only your first sig after 1 year(or the time you specify in the wallet). It makes this wallet really safe, cause even your seed was stolen, they can't transfer without your 2FA. I believe other wallets can start using this approach.
But I'm new to Monero and don't know if such a script is even possible having that it's not supporting multisig in the canonical sense

## tevador | 2021-12-30T21:44:18+00:00
@beshanoe It has been mentioned numerous times that timelocks in Monero don't work the same way as Bitcoin timelocks and cannot be used for such features.

If you lock up a Monero transaction for 1 year, outputs of that transaction will become unconditionally unspendable for 1 year regardless of multisig.

## UkoeHB | 2021-12-30T22:06:35+00:00
There is an alternate timelock scheme that could work a lot better for Monero: `mineable_when = [a, b]`. This is a range of 64-bit block heights expressed as a pair of Pedersen commitments `A,B`. To submit a transaction, the tx author must A) state two block heights `h_a, h_b`, B) make 2 range proofs for `h_a*H - A` and `B - h_b*H`. The tx is only valid for inclusion in a block with height `h` if the range proofs are valid and `h_a <= h <= h_b`.

## meordeuw | 2023-01-27T21:05:13+00:00
Hi

I have to express my opinion because I think it would be an important loss for Monero if this frozen transaction feature was removed.
I agree with the fact that this feature is currently misused and that it negatively impacts privacy, but to solve this problem it is sufficient to make a change that will discourage creation of frozen transactions. For example we could require that frozen transaction have 2 times higher fee. Then this feature would be used only when it is really needed and it would not be misused. Alternatively, we can require minimum freeze time (for example 20 block after current block). That would also eliminate misusing. And then this feature would no longer have a significant impact on privacy.

I will describe two use cases which are very useful to me.

First use case - tax law.
In my country, the tax law requires that I pay percentage tax each year from all my assets (wealth tax) including cryptocurrencies. But if I froze my Monero for 10 years (send a transaction with future arrival time 10 years later), I don't have to pay tax from my Monero for 10 years. I have to pay tax only once 10 years later instead of 10 times (each year) - but this is much smaller tax. During those 10 years I don't own Monero so I don't have to pay tax. This is not cheating, this is legal. Even if I wanted to pay tax, I can't because I don't have money. If I frozen 1000000000USD in Monero for 100 years, i wouldn't have to pay huge tax for my entire life. It would be really stupid and immoral law if it was required. Someone malicious could send such frozen transaction to my Monero address (or malware on my computer) and I would go to the jail because I don't have money to pay tax - nonsense.
Some people freeze their cryptocurrency for 5 years because they know that 5 years later they will be living in country where there is no cryptocurrency tax. Other people froze their funds because they don't want to pay tax and don't want to commit crime by hiding crypto from government and they consider moving to another country with no tax if the cryptocurrency value increases significantly.
Some people froze crypto for retirement and thanks to that they don't have to pay wealth tax their entire life each year.
Some people hope that tax law will be changed when their Monero unfreeze.

Second use case - bankruptcy law.
In my country, when I have debt and I can not pay the debt, then I declare bankruptcy and that means that I lose all my assets and all my debts are forgiven. This means that I would also lose all my Monero (if it wouldn't be frozen!). If there is frozen Monero transaction in blockchain with freeze time 10 years into future, that means I still don't own this Monero. I will own this Monero only 10 years later. If I declare bankruptcy now (not 10 years later) I don't have to give my Monero, because I can't! And my debts still are forgiven now.
Knowing that I can freeze my Monero, I can sleep peacefully, knowing that I will not lose them if I fell into debts.
But if this feature were deleted, I would not be able to sleep peacefully anymore holding Monero. I would have to convert my Monero into Bitcoin, because in case of debt collection, I couldn't use centralized exchange to convert because of KYC.


Please don't remove this feature. Even if the fee for frozen transaction was 100 times higher, I would still be using it. Converting Monero to Bitcoin in order to freeze Bitcoin is much more expensive. And I need Monero privacy features. I really need this feature.

## tevador | 2023-01-27T21:21:18+00:00
> If there is frozen Monero transaction in blockchain with freeze time 10 years into future, that means I still don't own this Monero. I will own this Monero only 10 years later.

I'm not a lawyer, but this sounds dubious. There are fiat-denominated term deposits which work in a similar way and I'm pretty sure the depositor is still considered to be the owner although they can't withdraw the funds.

In any case, helping you avoid paying taxes/debts is definitely not something that would be considered a legitimate use case when deciding to deprecate the "time-lock" feature.

## meordeuw | 2023-01-27T21:40:54+00:00
> I'm not a lawyer, but this sounds dubious. There are fiat-denominated term deposits which work in a similar way and I'm pretty sure the depositor is still considered to be the owner although they can't withdraw the funds.

I'm just saying what law is in my country. I don't say that this law is everywhere. I'm also not 100% sure that this is true so I'm not telling the name of my country, because I don't want that someone go to jail if I'm mistaken and I don't want to have fiscal control, but I'm using time locked transactions and I'm not paying taxes legally. And I'm convinced that this is not tax avoidance or debt avoidance. In my country it is commonly believed that this is fair and not immoral and not unfair.
People know that if they lock their money, they don't have to pay taxes. This applies not only to cryptocurrencies but also to fiat money for retirement. Our government provides special system for freezing money for retirement and people who use them don't have to pay tax (completely legally). And debt collector in our country also can not take this money which was frozen for retirement.
People in our country live peacefully knowing that our money frozen for retirement is safe (even if we have debt). People who froze Bitcoin for retirement in our country also live peacefully. People using Monero also should have such possibility. I know that maybe in other countries law is different and maybe this causes privacy issue, but i think that higher fee for frozen transaction is best trade-off. It will be used only rarely when it is really needed.

 

## unknowntrojan | 2023-07-09T21:16:57+00:00
Has there been any notable increase in usage of timelocks, or is the feature just as niche as when this issue was first posted? Have some of the discussed usecases moved off-chain? From what I've seen discussion has basically stopped around the topic for the time being. I believe the discussion around timelocks should go for a second round, to determine whether it would benefit Monero to leave it alone, remove it, or change it in a way that alleviates some of the issues raised and allows us to implement some of the things the original timelocks were unsuited for.

## jeffro256 | 2023-10-03T18:38:47+00:00
After studying the decoy selection algorithm in `wallet2`, @Rucknium and I made an observation that further warrants the removal of transaction timelocks. Because of the possible existence of timelocked transactions, `wallet2::get_outs` picks more decoys than necessary for each ring (assuming some may be locked and/or have EC points not in the main subgroup), according to a gamma distribution, but does so without replacement. Then, after the daemon returns the information about all picked decoys, the wallet filters out the time-locked and/or malformed outputs, then picks against those outputs according to uniform random distribution, also without replacement.

The effect of choosing M elements of D elements according to some distribution without replacement, then choosing N elements from those M elements uniformly at random has the effect of distorting the distribution of your N picks towards a uniform random distribution. What this means for users is that sender-privacy is slightly degraded depending on how noticeable this statistical effect is. 

To this, one could respond with a reasonable question: "Why not just change that one specific wallet implementation?" Certain solutions have different downsides, but all downsides could disappear if *all* outputs on-chain before a certain height are usable for decoy selection or known to be unusable ahead of time. In other words, making solid non-fingerprinting decoy selection implementations is much, much easier if time-locked outputs are not something that we have to worry about.

Let's say that we forked/changed relay rules to ban unlock times in future transactions. Assuming that we still honor the unlock times of past transactions, we obviously still need to account for timelocked transactions in future decoy selection algorithms. However, since we know that only ~0.01% of transactions used `unlock_time`, we could reasonably store a static list of every custom-locked output index to wallets when selecting decoys, with the information only taking up a couple dozen kilobytes, many times smaller than the RCT output distribution. Then, when doing the actual decoy selection, we pick *exactly* the number of decoys we need, skipping over unusable outputs, which we know ahead of time.

It is not currently possible to know which outputs are unusable before/during decoy selection without adding more database tables 
and RPC calls since the list of custom-locked outputs may grow arbitrarily large. 

## johnr365 | 2024-02-10T13:03:06+00:00
@jeffro256 - thanks for the summary, ie:

"What this means for users is that sender-privacy is slightly degraded depending on how noticeable this statistical effect is."

My understanding is that time locked transactions are currently very limited in use.

In terms of the actual privacy implications for the network and transactions currently, is there a way to quantify this?

For example, of x% of transactions implicated, we see a privacy degradation of y?

## dimalinux | 2024-02-14T04:39:54+00:00
> @jeffro256 - thanks for the summary, ie:
> In terms of the actual privacy implications for the network and transactions currently, is there a way to quantify this?

I assume the privacy implications right now are negligible. The question is what will happen if someone, knowing this issue, decides to start spamming the network with time locked outputs for some time period `X` before a payment that they know is forthcoming. The decoy selection algorithm favors recent outputs, so they might be able to create a privacy impact that is quantifiable for some reasonable cost in fees.

## jeffro256 | 2024-02-14T04:49:08+00:00
@dimalinux Yes you would have to be the wallet's node and if you created a ton of time-locked outputs and the user makes an RPC request which contains all locked outputs except for one, there's a near guarantee that that user owns that output.  

> For example, of x% of transactions implicated, we see a privacy degradation of y?

I haven't done any kind of analysis like that unfortunately. 

## Rucknium | 2024-02-14T17:06:25+00:00
> I haven't done any kind of analysis like that unfortunately.

I just finished doing an analysis like that.

I'm using data on transactions since the last hard fork (August 2022) until the first week of this year (2024). The number of non-coinbase transactions with custom unlock times is:

| unlock_time       | number of txs | share |
|-------------------|---------------|-------|
| 1                 | 106           | 2.81  |
| 2                 | 7             | 0.19  |
| 3                 | 2777          | 73.74 |
| 5                 | 1             | 0.03  |
| 6                 | 4             | 0.11  |
| 9                 | 112           | 2.97  |
| 10                | 478           | 12.69 |
| 12                | 1             | 0.03  |
| 20                | 1             | 0.03  |
| 1e+04 - 5e+08     | 265           | 7.04  |
| 1.4e+09 - 1.4e+12 | 14            | 0.37  |

These transactions make up about 0.036% of the 10.38 million transactions on the blockchain in this period. [Remember](https://thecharlatan.ch/Monero-Unlock-Time-Privacy/) that when `unlock_time` is less than 5,000,000, consensus rules interpret it as absolute block height. (When it is greater than 5,000,000, it is unix epoch time.) 93% of these custom unlock times have no effect since they are literally at block height 12 and below, i.e. blocks in 2014.

## Privacy impact

I performed the same analysis for some of the unlock_times that I did for nonstandrad fees to evaluate the impact on the privacy of users who are creating transactions with these nonstandard unlock times. The Positive Predictive Value (PPV) is the probability that the real spend can be guessed. Please read my [Discussion Note: Formula for Accuracy of Guessing Monero Real Spends Using Fungibility Defects](https://github.com/Rucknium/misc-research/tree/main/Monero-Fungibility-Defect-Classifier/pdf) for more info about how an adversary can attempt to guess the real spend when a wallet is producing nonstandard transactions.

| unlock_time | PPV | beta | mu_C |
|----------|-----|-------|-------|
| 3 | 93.9 | 0.023 | 93.6 |
| 9 | 70.7 | 0.0009 | 68.7 |
| 10 | 34.3 | 0.004 | 29.9 |

The probability of guessing the real spend is as high as 94% and as low as 34%. With ring size 16, the probability of guessing the real spend randomly when the probability is equal is 1/16 = 6.25%.

*Numbers revised Feb 14, 2024 21:00 UTC. In a previous version I accidentally excluded some transactions.*

## jbird186 | 2024-02-14T22:18:17+00:00
I know most of the discussion is regarding Monero-style timelocks, but I'd like to bring up the possibility of implementing Bitcoin-style timelocks. For those unaware, [nLockTime](https://en.bitcoin.it/wiki/NLockTime) prevents a signed transaction from being accepted into a block before time/blockheight `X` (meaning, nLockTime has no connections to the UTXO set whatsoever), as opposed to Monero's timelocks which directly prohibit outputs in a mined transaction from being spent in a later transaction before time/blockheight `X`.

nLockTime would enable Monero-first atomic swaps, simple & robust payment channels (even a Lightning Network clone, maybe?), and other layer-2 systems.

nLockTime has much fewer privacy issues than Monero's system, and yet is much more powerful. There are still some privacy considerations, but I believe they could be overcome at relatively little cost. I just wanted to potentially start a discussion on this, so I won't go into possibly-unncessary details on that.

## xmrrmxntom | 2024-09-22T05:44:25+00:00
@Minthos @Cactii1 

<h1>A Plea to Restore a Crucial Feature in XMR</h1>
<p>As a computer science student and a long-time follower of XMR & Dr. Daniel Kim (sweetwater.consulting), I'm compelled to share my thoughts on a feature that I believe is <strong>important</strong> to the value proposition of XMR. I've created an account specifically to express my disappointment and frustration with the removal of the <code>locked_transfers</code> and <code>locked_sweep_all</code> feature.</p>
<h2>A Personal Journey with XMR</h2>
<p>I've been following the XMR project since 2018, and its value proposition was evident to me even back then. However, I wasn't technical enough to fully appreciate its features. This year, I became proficient enough to run a full node and use the CLI, which is when I discovered the <code>locked_transfers</code> and <code>locked_sweep_all</code> features. I immediately utilized them, and they have been <strong>invaluable</strong> to me.</p>
<p>As someone who has impulsively sold assets like NVIDIA, BTC, and TSLA before they reached their full potential, I've come to realize that XMR is a <strong>long-term play</strong> that will appreciate in value over the next 5-20 years. The ability to lock transactions for an extended period has been a <strong>game-changer</strong> for me, allowing me to make sacrifices that my future self will appreciate.</p>
<h2>The Value of Locked Transactions</h2>
<p>The <code>locked_transfers</code> and <code>locked_sweep_all</code> feature was a <strong>unique selling point</strong> for XMR, offering me the ability to make long-term commitments to the blockchain. By removing this feature, we're depriving users of a valuable tool that would help them appreciate the embedded on-chain hodl properties of the XMR blockchain.</p>
<h2>A Call to Action</h2>
<p>I urge the XMR community to reconsider the removal of this feature and to implement safeguards to prevent similar decisions in the future. Specifically, I request:</p>
<ol>
<li><strong>Reinstatement of the feature</strong>: Bring back the <code>locked_transfers</code> and <code>locked_sweep_all</code> feature to allow users to make long-term commitments to the blockchain.</li>
<li><strong>Safeguards for feature deprecation</strong>: Establish a formal, non-trivial process or procedure to determine whether a feature should be deprecated, ensuring that user feedback and concerns are taken into account and valued.</li>
<li><strong>Improvement or alternative</strong>: If the feature cannot be reinstated, explore alternative solutions that would provide similar functionality and benefits to users.</li>
</ol>
<h2>Conclusion</h2>
<p>As more users join the XMR community, they will come to appreciate the unique properties of the blockchain. I firmly believe that the <code>locked_transfers</code> and <code>locked_sweep_all</code> feature helps users <strong>HODL</strong> with the long-term success of XMR. I hope that my plea will be heard, and we can work together to restore this important feature.</p>
<h2>A Final Appeal</h2>
<p>I've gone from hearing about XMR as the real <strong>privacy-focused vision</strong> of BTC, to buying some XMR on an exchange, to self-custodying on Exodus wallet, and finally to downloading and running the CLI. XMR is <strong>beautiful</strong>, and it's <strong>idealistic</strong>. Please keep or reimplement this feature.</p>

https://reddit.com/r/Monero/comments/mwrm6g/how_to_lock_send_future_monero_to_yourself_with/

<p>This was the post and feature that motivated me to dedicate a weekend last semester to read the documentation, compile from source, and use the CLI.</p>
<p>…Please keep this feature…</p>


## nahuhh | 2024-09-22T06:27:24+00:00
Monero (the blockchain) has 1 job. Digital currency. 

Gambling on its fiat valuation is completely unrelated to Monero and is very poor reasoning to reinstate what is, among other things, a privacy harming feature.

If you want to force yourself to HODL:
A) learn impulse control
B) store funds in a paper wallet
C) store funds in a multisig
D) store funds with a custodian

## j-berman | 2024-10-15T23:13:59+00:00
I've hit a hiccup in wallet side scanning for fcmp++ because of timelocks. TL;DR they can slow down full wallet scanning under fcmp++.

### Context

fcmp++ works by proving you own an output (or "enote") within a special merkle tree called a curve tree. All valid, spendable (i.e. **unlocked**) outputs across the entire chain compose the leaves of the tree. When constructing the full-chain membership proof, the user proves their output is a member of the tree, without revealing which output it is. To construct the proof, a wallet needs the output's path in the tree (from leaf to root) at the latest block. The state of the tree changes every block, so an output's complete path in the tree changes every block as well.

I'm currently working on building the tree locally as the wallet syncs, so that wallets can update received outputs' changing paths while syncing (and can therefore construct fcmp++ txs without leaving any statistical trace to the daemon which output is being spent when the user constructs an fcmp++ tx).

In order to build the tree correctly, clients need to grow the tree with outputs that unlock each block.

### The problem

Thanks to timelocks, an output's unlock block can be any block far in the future, so clients need to take special effort to keep track of outputs by unlock block.

### Solution A

Clients download all outputs that unlock in a block in addition to outputs created in a block. This is bad because it's almost 2x'ing the amount of data clients download in order to sync.

### Solution B

Clients locally keep a cache of locked outputs, and then remove from the cache upon inclusion in the tree. The main problem with this is thanks to timelocks, it's a potentially unbounded cache that clients need to store.

### Solution B++

Keep track of valid **normally locked** (i.e. **not** timelocked) outputs in a persistent cache in the client, then remove from the cache upon inclusion in the tree. Modify `/getblocks.bin` to support returning timelocked outputs as they unlock in a block. This means clients will have to download almost 2x the data for timelocked outpus. Note: this solution could also be tweaked to avoid needing to re-download coinbase outputs.

_____

If we remove timelocks at consensus, it closes the door to enabling excess scanning cost to clients via timelocks, and full wallets can reasonably keep a local cache of all locked outputs.

Note that keeping a locked outputs cache in the client would increase the client's space footprint by `n * 72 bytes`, where n is all currently locked outputs as of the latest block.

P.S. also open to any ideas on other solutions.

## UkoeHB | 2024-10-16T00:07:54+00:00
> Keep track of valid normally locked (i.e. not timelocked) outputs in a persistent cache in the client, then remove from the cache upon inclusion in the tree.

Why would this be needed if you are just growing the tree with every block received?

> Modify /getblocks.bin to support returning timelocked outputs as they unlock in a block.

This seems the best option to me. Let the daemon keep track of which block an enote will unlock in. The main problem is potential DoS by locking many enotes to a single block. If timelocks are deprecated then this is no longer as big an issue because 'known DoS targets' can be hard-coded (if there are any).


## jeffro256 | 2024-10-16T00:28:59+00:00
> Why would this be needed if you are just growing the tree with every block received?

You can't include transaction outputs inside the merkle tree until the moment that it is valid to spend them. So even for normal transaction outputs, you have to keep them around for 10 blocks before insertion. If they were added to the tree before, then the validators wouldn't be able to determine whether you were spending a "locked" output or an "unlocked" output. All they can tell is whether that transaction output is an element contained in the tree, or not.

> Modify /getblocks.bin to support returning timelocked outputs as they unlock in a block.

The problem here for me is that this isn't easily verifiable to the wallet. Normally all content returned by `/getblocks.bin` (except for new output indices which will be not needed post-FCMP) can be hashed and validated as belonging to that block ID. This wouldn't be the case for transaction outputs of previous blocks, unless a sister/brother transaction ID merkle proof was included per-output. One of the main reasons for building the FCMP tree client-side is so that daemon trust is minimized. 


## jeffro256 | 2024-10-16T00:35:53+00:00
> Clients locally keep a cache of locked outputs, and then remove from the cache upon inclusion in the tree. The main problem with this is thanks to timelocks, it's a potentially unbounded cache that clients need to store.

I think solution B is fine give the current usage of Monero timelocks is niche and the fact that there is currently a relay rule in place to prevent future transactions from including an unlock time. We could initiate a soft fork *before* the FCMP hard fork to completely cement the rule in-place, or we could decide to not honor time-locked transaction outputs past height X during the building of the FCMP tree. Both of these would allow us to know the exact size of the wallet cache before deploying the code. 

## j-berman | 2024-10-16T01:03:27+00:00
Good point on the relay rule -- I also generally agree solution B will be acceptable in combo with a guarantee we'll know the size of the wallet cache before deploying.

> We could initiate a soft fork before the FCMP hard fork to completely cement the rule in-place

This seems a cleaner break to me, rather than setting a precedent of voiding prior expectations.

# Action History
- Created by: sedited | 2020-10-21T23:14:03+00:00
