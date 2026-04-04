---
title: Coinbase Consolidation Tx Type
source_url: https://github.com/monero-project/research-lab/issues/108
author: UkoeHB
assignees: []
labels: []
created_at: '2023-01-04T17:49:58+00:00'
updated_at: '2024-10-24T18:30:37+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
With the advent of p2pool, coinbase enotes have become much more numerous on-chain, and consolidating p2pool coinbase enotes (which have very small amounts by design, so p2pool miners collect many small amounts that need to be consolidated) is costly both in terms of tx fees and chain bloat. There have also been [historical](https://github.com/monero-project/monero/issues/6688) observations (see [here](https://medium.com/@JEhrenhofer/lets-stop-using-coinbase-outputs-da672ca75d43) also) about how coinbase enotes generally weaken ring signatures since their owners are typically public information and since consolidating them is usually obvious.

Given those issues, I propose a 'coinbase consolidation tx type'. Coinbase and normal enotes would be completely segregated - coinbase enotes only spendable in consolidation txs, and normal enotes only spendable in standard txs. Moreover, since the owners of coinbase enotes are generally public information, and since consolidating coinbase enotes is very costly, I propose that consolidation txs do NOT use ring signatures for inputs and instead expose the inputs being spent directly (i.e. with a direct index into the list of on-chain coinbase enotes). In seraphis it would be very easy to make a consolidation tx type without ring signatures by simply removing the current grootle membership proof, however ringct is a little more challenging since ownership and key image correctness are tied to membership.

# Discussion History
## SamsungGalaxyPlayer | 2023-01-04T18:17:52+00:00
This goes back to the same proposal as before: separating coinbase spends from non-coinbase spends.

Upsides: protects non-coinbase spends from the de-anonymization risks associated with coinbase outputs. Coinbase outputs are likely to be attributed to either 1) a pool, or 2) a future p2pool consolidation transaction. Both cases lead to a strong heuristic (or worse) that indicates the decoy use is ineffective. If either 1 or 2 weren't true to result in the heuristic being weaker, then possibly this would be a non-issue. This would occur usually if p2pool use was small but not infinitesimal.

Downsides: force a "chrurn"-like spend of coinbase outputs for each miner, including mining pools and p2pool users. Implementation complexity.

I'm generally in favor of requiring this churn. Prevent non-coinbase spends from using coinbase outputs.

There are several options for how to handle rings for coinbase spends:

1. Remove rings entirely and cut the losses, saving on efficiency.
2. Select decoys from other coinbase outputs.

2 is interesting to me. Here are some strategies to keep in mind for option 2:

* We can set the ringsize to any number. Can be 16, can be 3.
* We can allow several numbers, eg: 1 (no decoys) and 3.
* We can select coinbase decoys from the same block. Eg: 2 decoys from the same p2pool block. This doesn't work for pools where there would only be 1 output.
* We can impose different rules on coinbase outputs that are unique to the block and those that are non-unique to the block. For example, where there are 3+ coinbase outputs in a block, we can use 2 decoys from that block. If there are only 1-2 coinbase outputs, we can enforce 0 decoys.

My first impression (subject to change) is the following:

If a coinbase output is being spent, then a wallet checks to see how many coinbase outputs are present in that transaction. If there are 3+, then set ringsize as 3 and select 2 decoys from the same block. If there is only 1 or 2, then select 0 decoys. Consensus code should perform this check to ensure p2pool users aren't sending coinbase rings without decoys.

This is one of the simplest ways to account for public pools mucking things up, while providing some basic level of protections for the coinbase outputs for p2pool users. In practice, this *should* mean that each p2pool spend is hidden among 2 other real p2pool miners in the same block. Consolidation transactions will result in negative heuristics, but they *should* be meaningfully less bad for a relatively small cost.

TODO: research/discuss this much more :)

---

Note on private miners and mining pools that was discussed in previous materials: this is now a non-issue in my mind. I am grouping these with p2pool users and focusing on protecting those instead.

## UkoeHB | 2023-01-05T19:42:34+00:00
There are two design choices available, leading to four combinations that differ from what we have today (coinbase and normal enotes mixed together).

Choice 1: membership proof (normal enote membership proofs would change to only reference normal enotes)
- **no membership proof**: coinbase enotes are spent directly with no decoys/ring signature
- **coinbase-only decoys**: coinbase enotes are spent with membership proofs that only reference coinbase enotes

Choice 2: tx type to spend coinbase enotes
- **normal tx**: coinbase enotes are spendable as a distinct input type in normal transactions (e.g. alongside legacy inputs and normal seraphis inputs)
- **coin consolidation tx**: coinbase enotes are exclusively spendable in a special tx type that is designed for consolidating coinbase enotes

The easiest and most efficient approach would be **no membership proofs** + **normal tx**. Balances would not need to be segregated, and the tech stack would not need to maintain another tx type (although separating the tx types would mean less dependencies to deal with when upgrading only one tx type).
- The main downside to this approach is the introduction of anonymity puddles between txs with only coinbase enotes (consolidations) and txs with mixed input types (spending from a general balance without taking extra care to consolidate coinbase enotes). It's easy to imagine some wallets mandating coinbase enotes be consolidated, while other wallets don't mandate that, leading to the implementation-defined puddling that we want to minimize. Currently there is no wallet-mandated consolidation, so consolidation vs free-spending is a user-choice distinction.
- A secondary downside would be exposing a fraction of the total input amount in normal txs (anywhere from 0%-100%).

## jtgrassie | 2023-01-06T23:38:57+00:00
> I propose that consolidation txs do NOT use ring signatures for inputs and instead expose the inputs being spent directly

The main downside of _not_ using decoys here would be leaking amounts, as coinbase outputs are not encrypted. If consolidation txs used rings _only_ of coinbase outputs, we could at least break this amount linkage (the new output(s) amount(s) would be unknown due to not knowing precisely which inputs are being spent). Hence, if we're going to add a new consolidation tx type, I'd certainly favor keeping ring sigs for this new tx type.




## tevador | 2023-01-09T13:30:35+00:00
> rings only of coinbase outputs

In practice, the ownership of coinbase outputs is publicly known (p2pool and most centralized pools publish this information), so such rings would do very little in terms of privacy. You could find the output that is owned by the same entity in each ring and that would reveal the real spends (and the amounts) in most cases.

It would actually be better if the "coinbase consolidation" tx didn't use ring signatures and only had one output. Such transactions would be very small and fast to verify (no membership proofs and range proofs needed) and would not leak any useful information since one output means the outputs have not changed ownership. The subsequent spend of the consolidated output would be fully protected.

Provably spent coinbase outputs would also enable more efficient pruning strategies. Currently about 15% of all newly created outputs are p2pool coinbase payouts, needlessly cluttering the output database.

> 2 decoys from the same p2pool block

As noted above, that would not work. P2pool publishes the address that owns each coinbase output. If you consolidate multiple outputs, all rings will have exactly one output owned by the same address, which leaks the real spends. 

Example with a 3-input transaction (ring members and their p2pool address):
```
ring 1:
42yAHAH5at...6dy78x2gbp
48gjGsibKv...gxUPMe5N7g
4BBb6ZBPPP...RKtLi1jcMb

ring 2:
48gjGsibKv...gxUPMe5N7g
47ab14EokG...vu6JqWMsGw
44YdBost8R...2nZ55pXeCU

ring 3:
4AxaapsBMR...dqmAZLqaGN
48gjGsibKv...gxUPMe5N7g
42Pv7DvpXF...4NCR5NWC2K
```
You can immediately see that the transaction is made by the miner `48gjGsibKv...gxUPMe5N7g`.

The only way how this could work is if the wallet had access to the p2pool sidechain and selected all decoys with the same owner, something like this:

```
ring 1:
47ab14EokG...vu6JqWMsGw
48gjGsibKv...gxUPMe5N7g
4BBb6ZBPPP...RKtLi1jcMb

ring 2:
4BBb6ZBPPP...RKtLi1jcMb
47ab14EokG...vu6JqWMsGw
48gjGsibKv...gxUPMe5N7g

ring 3:
48gjGsibKv...gxUPMe5N7g
47ab14EokG...vu6JqWMsGw
4BBb6ZBPPP...RKtLi1jcMb
```

## jtgrassie | 2023-01-09T14:53:41+00:00

> The only way how this could work is if the wallet had access to the p2pool sidechain

The wallet would not need access to the p2pool sidechain as it could just select previous (owned) coinbase outputs (though this is of course problematic for a new miner with no/few previous coinbase outputs).

You make a good point (one I overlooked; that of p2pool publishing output ownership), which suggests no-rings on consolidation txs makes more sense now. 



## SamsungGalaxyPlayer | 2023-01-09T15:26:53+00:00
Good point about the addresses @tevador - that's something I didn't consider.

## UkoeHB | 2023-01-11T18:07:57+00:00
After thinking more, I am not sure this proposal is the right direction. Enote consolidation being statistically significant, and consolidating enotes with small amounts being expensive, is a general problem not specific to coinbase enotes. Implementing a specific solution for coinbase enotes amounts to elevating the circumstances of miners to first-class status in the protocol, without solving the more general problem.

If another major project on the scale of p2pool becomes active in Monero and would benefit from specific protocol changes (not trivial benefits - privacy and scaling benefits even), should we hard fork to accommodate them? To support protocol longevity by reducing hardforks (and not setting precedents that would justify a relatively higher rate of future hardforks), it seems better to aim for general solutions to problems. In this case, one general solution to the privacy impacts of consolidation would be a [global membership proof](https://github.com/monero-project/research-lab/issues/100). The cost of consolidations might be addressed by using aggregate membership proofs that scale sub-linearly with the number of memberships being proven (i.e. number of tx inputs).

## MoneroArbo | 2024-02-15T16:14:23+00:00
Are Global / Full chain membership proofs really looking likely/soon enough to completely table this conversation?

I don't personally see an issue with having miners in a bit of an "elevated status" -- they're pretty much vital to any PoW chain anyway, and p2pool is something that tackles an inherent issue with PoW: pool centralization.

Plus, it's not like anyone was suggesting an extra hard fork specifically for this change so the whole thing about 'rate of hardforks' doesn't quite ring true for me.

## kayabaNerve | 2024-10-24T18:30:36+00:00
If we are to add anything, I'd support the ability to aggregate coinbase outputs using solely a GSP proof (not in combination with any membership proof, solely specifying the output directly). Notably, I'm suggesting leaving the option for users to aggregate transparently or privately using a standard transaction.

I don't support this at all however. While coinbase outputs harm user privacy under ring signatures, they no longer will under FCMPs. This proposal would be what harms privacy there. The other argument, efficiency, should be solved on P2Pool's (or another such protocol's) end.

# Action History
- Created by: UkoeHB | 2023-01-04T17:49:58+00:00
