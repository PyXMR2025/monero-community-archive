---
title: Proposal for FCMP++ HF Activation Rule to Retroactively Ignore Future `unlock_time`
source_url: https://github.com/monero-project/research-lab/issues/125
author: jeffro256
assignees: []
labels: []
created_at: '2024-10-22T19:13:09+00:00'
updated_at: '2024-11-22T23:29:31+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
### Proposal abstract

Upon FCMP++ hard fork activation, validators should ignore the `unlock_time` field retroactively for all non-coinbase transactions posted to the chain after a certain height. This height should be one that does not yet exist and is decided ahead of time by rough community consensus. From that point forward, the `unlock_time` feature will cease to work.

### Background

* FCMP++ intro: https://www.getmonero.org/2024/04/27/fcmps.html
* `unlock_time` field intro: https://web.getmonero.org/resources/moneropedia/unlocktime.html
* Lengthy discussion of pros/cons to `unlock_time`: https://github.com/monero-project/research-lab/issues/78
* Merged PRs for non-zero `unlock_time` ban by relay rule: https://github.com/monero-project/monero/pull/9151 and https://github.com/monero-project/monero/pull/9311
* Comment that initiated discussion of this proposal: https://github.com/monero-project/research-lab/issues/78#issuecomment-2415324570

### Problem

The `unlock_time` field acts as a DoS vector against wallets building the FCMP++ tree client-side. The purpose of building the FCMP++ tree client-side is to maintain the wallet's full-chain sender anonymity, even when using untrusted daemons. The act of building of the FCMP++ tree requires storing, in RAM or persistent storage, past transaction outputs for as long as they are locked on-chain, or duplicating RPC calls for refresh. Thus, long-lasting `unlock_time` values in transactions require greater memory/storage/bandwidth requirements for everyone else's wallets. If transactions are allowed to be posted to the chain with long-lasting `unlock_time` values in the future, then the requirements for building the FCMP++ tree will be unknown before the code is deployed.

### Proposed solution

For all non-coinbase transactions after some "ignore" block index `J`, treat all `unlock_time` values as if they were 0 when constructing the FCMP++ tree (for both daemon and wallet). This means that no matter the value of `unlock_time` in such a transaction, its outputs will always be inserted into the FCMP++ tree exactly 10 blocks after it is posted to the chain. Thus, when the hard fork activation occurs, transactions containing FCMP++ input proofs will be able to spend younger-than-index-`J` outputs, regardless of the `unlock_time` value. Any non-zero `unlock_time` value after this point has no effect. For uniformity's sake, non-zero `unlock_time` values should also be banned by consensus after the fork activation. Note that there is already a relay rule to ban non-zero unlock times.

There should be rough community consensus on the value of `J` before that block is actually mined. After it is mined, we can do analysis of the chain to figure out what the exact additional resources will be required because of non-standard `unlock_time` values. This can be done by a tool posted here: https://github.com/monero-project/monero/pull/9522. If everything is within acceptable bounds, we ship the code using the wallet locked output cache as designed. If not, we go back to the drawing board. The later scenario occuring is not likely because of the relay rule already in place. However, miners can still spam wacky `unlock_time` values up until block `J`.

### Timeline of proposed solution

1. Make a decision on "ignore" block index `J`
2. Wait for that block `J` to be mined on mainnet/stagenet/testnet
3. Perform analysis of on-chain occurences of `unlock_time` *before* index `J` and document expected wallet requirements
4. If all goes well, deploy FCMP++ code to daemon/wallet
5. Test, test, test
6. FCMP++ hard fork activates and proposed `unlock_time` rule kicks in
7. Wallet happily builds FCMP++ trees with low memory/storage requirements
8. Profit????

### What this proposal does NOT do

* Invalidate currently existing `unlock_time` values
* Set in stone the invalidation of `unlock_time` values after block index `J` outside of the FCMP++ hard fork activation. If FCMP++ falls through, then so does this rule.

### Alternative solutions

- Initiate a soft fork to restrict the value of `unlock_time` before the FCMP++ hard fork. 
- Only start ignoring `unlock_time` values for FCMP++ transactions, praying that miners don't spam non-zero `unlock_time` values between FCMP++ code deployment and activation.





# Discussion History
## jeffro256 | 2024-10-22T19:18:17+00:00
@j-berman @kayabanerve 

## Rucknium | 2024-10-22T20:00:43+00:00
The new transaction relay rules for the network in version 0.18.3.4 of the Monero deamon have not prevented new transactions with nonzero unlock time from being confirmed on the blockchain. Gossip protocols are designed to reliably spread messages throughout the network even if many nodes fail to relay messages. In the absence of a hard fork, the robustness of Monero's gossip protocol can prevent new relay rules from being effective.

Below are all non-coinbase transactions with nonzero unlock time confirmed on the Monero blockchain between September 1, 2024 (height 3227566) and October 13, 2024 (height 3258526).

Version 0.18.3.4 of the Monero deamon, which prevents these transactions from entering the node's txpool, was released on August 22, 2024: https://github.com/monero-project/monero/releases/tag/v0.18.3.4

Info on lock time interpretation is here: https://github.com/monero-project/research-lab/issues/78

Data on which mining pool mined each block was collected using https://git.gammaspectra.live/WeebDataHoarder/monero-blocks . Blocks are labeled "P2Pool" when the coinbase transaction has multiple outputs. "\<NA\>" indicates missing data.

```txt
    block_height        mining_pool output_unlock_time                                                          tx_hash
 1:      3227570             P2Pool                 10 09e79c114d481446a487ba287318df3b2cd01268765eb55f6c08bacaafc6e273
 2:      3229130               <NA>                 10 8b707c5616081a2f3a498ddfb7a4e48834412e2e3966cf7da9c73055e6253395
 3:      3229443               <NA>                  1 acc5711c82d708b8f47e41976e365d1eef4f37cca43daf85ed9a237e8dfb380f
 4:      3230056     supportxmr.com                  9 3da7aa7cd1eab9f33c04db844d6d88d5b91a7d4f97e2b752a69bd3f4d359a3ca
 5:      3230071     supportxmr.com                  9 1885b9c32d33bbc5be3a29de3d7605a27342caf7fbe0d7d63269993bee0edbf1
 6:      3230108             P2Pool                  9 b68ef1ceb5a62233774ea65b5de37180a869a52d0c00bc91c3a75907fac28924
 7:      3230267               <NA>                  3 82f3a3961097fbdb799663bf4ee8b7678a7d5c0b5b6df329ee62a16fe0fc9c6b
 8:      3232617     supportxmr.com                 10 3e88d29def78fb4294fcc5b141c5e8b48898bb383974c5861b30e4c53d06d17f
 9:      3232981     supportxmr.com                  1 85d4f295f0076d8ef1e5618988b064cd2285e4c25bd006cc464c66a40d5bdb85
10:      3237887               <NA>                 10 aa34b67fd8a6cf650cf20590a069019a772fec236aff63ca8a63f6bddbfed63e
11:      3238081 moneroocean.stream                 10 4bf951e33552521037f09242648ea0f0525a07f3c93faaa94f76628387fa5164
12:      3238081 moneroocean.stream                 10 2220378654c414fb817026c10e70668aca077b426a422d21f57d585418ac460f
13:      3238092               <NA>                 10 0337b1ba26b2049f415a2b54392e505dc54dbff8f292bd2b767821b9fe1e812a
14:      3238137     supportxmr.com                 10 fcdafaf7f6cba22b107496a28367a6d133c05afdee272350dd05c6e942ed690c
15:      3245433     supportxmr.com                 10 2c6ca3b57c4a43819a225e0c67ea235610452d2ca9b83cdb4da914addc37a9de
16:      3248944   xmr.nanopool.org                 10 7c27d9ebbfcd1bebdbfca27c47a686b112c8670942a93a540cb0768a58db9e5f
17:      3249126     supportxmr.com                 10 a9468c5669a277f16f6ad8c3aa35ca4c4113953427b97c147fea76a0f507f2e5
18:      3251013   xmr.nanopool.org                  9 d1221e24b7484988bde174e25315490a8065cdd3e347336db7421497dab4d558
19:      3251028     supportxmr.com                  9 7299ebc83cdae8316477a7a6d2d57e68b26cb09be15743d00de31b6f44e7615b
20:      3252831     supportxmr.com                 10 d45069893c3e684befa71e279a86cb2d0e9715c9b5fe8df5f3f9f6407bf96efe
21:      3253319               <NA>                 10 d02f29e1d1bf3f67162d30fc758a915e21607a5fb7c02dc00965a5fac5ff7f84
22:      3253564   xmr.nanopool.org                 10 d14431487b75fa9a08c0a79bcd49abe9dcaf01505965a2e73e0106a4fbc87762
23:      3253899     supportxmr.com                 10 9cf7dfdc1bb080d0ba46c9499325102d55441f4c60385e27bd64f0c23b7e5f8b
24:      3254110     supportxmr.com                 10 51bdb219fd92e30532546eeb7e6b6b03b51778858ecde4b613cf9dc9bf11e331
25:      3254174     supportxmr.com            3254891 fdcdec97b5a29beb5828aaa612fc7d591d24ecf1fb83fc54fb2bf8f78427cf98
26:      3254393   xmr.nanopool.org                  9 9bc349873f3c07f70b0b20c51a2276c4aef7941a2cf42cc667ce37637cc8634e
27:      3254418   xmr.nanopool.org                  9 008fc62df18ca1a649a54959bd1f8bdd0a8a5d75e83a2870004c202d73221401
28:      3254439     supportxmr.com                  9 1a0e601ba9b64edc127aa622a352eaa40b9f2229c05aeb467cfd756354e01418
29:      3254459   xmr.nanopool.org                  9 3f3519b1ed8ded593600c3769712730f25efb5cd1322718ca5eb620d4389556b
30:      3254492   xmr.nanopool.org                  9 e72af53367c9ed862b240050a769b722943cc11ae499a34af68d5f8cf0b060c6
31:      3254516   xmr.nanopool.org                  9 24c3566878d389c0ad5a49ac0bd3fe05952f984436fc0bc2a86f4e4ebf572b10
32:      3254540     supportxmr.com                  9 a35cd4b38f8cd72e3821906c6f01f3055624e92ad9d8dbf2856310f4eea5dd1a
33:      3254587     supportxmr.com                  9 298c988a5fac4a2b6c0a4f8ac2231494df5d96288f18511ac0b7109c430c19f3
34:      3254587     supportxmr.com                  9 89ac028eb7cbaecd4adee85042105a6e22184839258a486f1d031515163b0743
35:      3254601   xmr.nanopool.org                  9 f5f218507c181dfa2b8823dd5906be129632401e972151cd6f571007402be2de
36:      3255331     supportxmr.com                  9 a3fbbbe5fa849d184c3d9b97823d3cd230a6202d8bf329fc16594f4ade10b5e8
37:      3255342     supportxmr.com                  9 44288272844ea7c29e8a26060aa1839487bc193cff99e10233726fe3f8af4fed
38:      3255472   xmr.nanopool.org                 10 de1777424ddceff86e804efd1b3e423749f8bdffee4290bcdbccf56da6ba7e4a
39:      3256401     supportxmr.com                 10 213d6affd7ba50311cc5ae6fe338f2a3ef6c96c6b3653fbd7d43702e9c1d06c9
40:      3256416   xmr.nanopool.org                 10 f5f94e9789aa5d9284ea54d8d90c5050d48963db4ae01aca1f4c71cede1fed27
41:      3256431   xmr.nanopool.org                 10 1728d99a5d1f214270e2175eb6e08c496a24e30f2cb3b7d179ea9b134a8893dd
42:      3256547   xmr.nanopool.org                 10 78fd59cad46578136fe0e1b9a5ce208eb7d728ebac17fbdaa16c9689505b9d79
43:      3256628   xmr.nanopool.org                  9 2ef8ada467726486de1a44b2ef3c2a05f66322fda3c831af1494262d8ee94113
44:      3256663   xmr.nanopool.org                  9 637640cc9f62c1a139f7e4d9323b1327a8d3b1acbb231f3892ef246926124e1b
45:      3256676     supportxmr.com                  9 8b44e3dadbcec428da66ca354e956e0062a9ed4ba33f12a6c38fa29a9559485b
46:      3256686   xmr.nanopool.org                  9 1df0d3a16392be6c1ece6895e5af796904355c4ebbc32cae34d87a4a7f653617
```

## kayabaNerve | 2024-10-22T23:08:33+00:00
Proposal SGTM.

While the data shows network resilience, please note only one is an actually timelocked TX and the rest are erroneous. Only one timelocked TX since the relay rule's activation is strong evidence this won't be an issue.

## chaserene | 2024-10-25T16:28:17+00:00
> If everything is within acceptable bounds, we ship the code using the wallet locked output cache as designed. If not, we go back to the drawing board.

@jeffro256 what prospective solutions do you see in case someone spams the network between now and `J`?

> Alternative solutions: Initiate a soft fork to restrict the value of unlock_time before the FCMP++ hard fork.

@jeffro256 sorry if obvious, but how can a soft fork enforce that restriction?

> While the data shows network resilience, please note only one is an actually timelocked TX and the rest are erroneous. Only one timelocked TX since the relay rule's activation is strong evidence this won't be an issue.

@kayabaNerve IMHO this only shows the current *willingness* to post actual timelocked tx's, not ability. at current hash rates, the above identified pools represent ~70% of the global hash rate, which translates to a hypothetical spammer's minimum accessible share of block space.

## kayabaNerve | 2024-10-25T16:36:48+00:00
A soft fork would have miners refuse to build on a chain with timelocked TXs. So long as they're a majority of hash power, the entire net will no longer include such TXs.

I meant social issue, not technical. A lack of use means a lack of users implies a lack of people who mind.

## jeffro256 | 2024-10-30T18:47:32+00:00
During Research Lab meetings [today](https://libera.monerologs.net/monero-research-lab/20241030) and [last week](https://libera.monerologs.net/monero-research-lab/20241023), rough consensus was found for setting the tentative ignore date as May 1st, 2025.

On mainnet, [block index 3270000](https://xmrchain.net/block/3270000) had a timestamp of 1730243700. If we use this block as an anchor, we can calculate the expected value of `J` given that we want the target date to be May 1st, 2025. The UNIX timestamp for May 1st, 2025 in UTC is 1746057600. The target delay between blocks is [120 seconds](https://github.com/monero-project/monero/blob/893916ad091a92e765ce3241b94e706ad012b62a/src/cryptonote_config.h#L80). Thus, `J` should be set to `(1746057600 - 1730243700) / 120 + 3270000 = 3401782`. The anchor block index 3270000 was chosen by rounding down to the nearest 10,000 based on the current height of the chain at the time of meetings today. 

## kayabaNerve | 2024-10-31T06:27:04+00:00
I advocate for a timestamp based anchor and using the network's median time to evaluate which block is first past the pole. There's an existing rule that new block's time must exceed the median, so it is monotonic. This would be portable to all networks and not just Monero's mainnet (testnet, stagenet).

## chaserene | 2024-11-20T03:40:05+00:00
> If everything is within acceptable bounds, we ship the code using the wallet locked output cache as designed. If not, we go back to the drawing board.

@jeffro256 I'm partially repeating my above comment, but I'm curios to understand:

1. what would it cost to generate unlock_time spam such that resource requirements would fall out of acceptable bounds?
2. in case the above happened between now and May 1, what prospective solutions do you see?

I'm asking again because, to me, the risks are not clear to be negligible. I keep being reminded that 9 months ago the protocol (theoretical effective ring size), the node software (peer connection stability, OOM crashes) and the wallet code (fee selection glitch) were all caught off-guard in a month-long transaction deluge that in total cost relatively little to whoever contributed to it. it did lead to the happy accident of inventing FCMP++, but I'd rather not the current timeline get delayed by months because of a similar event. it is due to this that I lean toward reducing the window of risk by setting the ignore time `J` to way earlier than May 1.

there was a solution proposed by @j-berman that, should a problematic amount of unlock_time spam happen, `J` can be changed retroactively such that it fits us (<code>J<sub>1</sub></code>). not only would this look horrible, it would also break the promise to anyone who will have submitted an honest non-standard unlock_time transaction between <code>J<sub>1</sub></code> and <code>J<sub>0</sub></code>. 

## kayabaNerve | 2024-11-20T03:57:24+00:00
There is no such promise to break. May 1st is solely the currently planned cutoff date assuming a lack of spam.

## chaserene | 2024-11-22T23:01:08+00:00
@kayabaNerve I don't see that stated in Jeffro's proposal. if that's the plan, then the proposal should say roughly this to make it explicit: "the protocol will stop honoring custom unlock_times in transactions mined beyond a certain cutoff point between [October 30](https://github.com/monero-project/research-lab/issues/125#issuecomment-2448077632) and May 1. the exact cutoff point will be chosen after May 1 such that as much of the period will be covered as possible, but it *will* exclude the period between any potential anomalous custom unlock_time load occurring and May 1."

## kayabaNerve | 2024-11-22T23:29:30+00:00
> There should be rough community consensus on the value of J before that block is actually mined. After it is mined, we can do analysis of the chain to figure out what the exact additional resources will be required because of non-standard unlock_time values. This can be done by a tool posted here: monero-project/monero#9522. If everything is within acceptable bounds, we ship the code using the wallet locked output cache as designed. If not, we go back to the drawing board. The later scenario occuring is not likely because of the relay rule already in place. However, miners can still spam wacky unlock_time values up until block J.

This section adequately covers it IMO but I have no objection to your description.

# Action History
- Created by: jeffro256 | 2024-10-22T19:13:09+00:00
