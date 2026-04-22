---
title: Proposal for FCMP++ HF Activation Rule to Retroactively Ignore Future `unlock_time`
source_url: https://github.com/monero-project/research-lab/issues/125
author: jeffro256
assignees: []
labels: []
created_at: '2024-10-22T19:13:09+00:00'
updated_at: '2026-04-22T17:02:15+00:00'
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

## Rucknium | 2026-04-22T16:15:49+00:00
**TL;DR: Four (4) transactions with custom unlock time have appeared on the blockchain since the May 1, 2025 deadline.**

I re-ran the data gathering script to collect data since [my earlier comment on October 22, 2024](https://github.com/monero-project/research-lab/issues/125#issuecomment-2430142343), up to block height 3654036 on 2026-04-16. Transactions with custom lock time have continued to appear in the blockchain despite the transaction relay rule that prohibits them. In the tables below I have only included custom unlock times that "bind". Many users misinterpret custom lock time. They think that the unlock number indicates _relative_ block height. Unlock time actually indicates _absolute_ block time. There are many new transactions with lock time in the single digits, but these have no effect. See issue #78 for interpretation of unlock time.

Below is a table of the four transactions with binding custom unlock time confirmed on the blockchain since May 1, 2025. The "already_unlocked" column indicates whether the lock has already been released by the current block height (3654036).

|transaction_timestamp | unlock_height|already_unlocked |tx_hash                                                          |
|:---------------------|-------------:|:----------------|:----------------------------------------------------------------|
|2025-06-28 00:19:21   |       4293212|FALSE            |96a657af388225933f00edbe620540ad3183046ff4d976c6fbd110876b55f588 |
|2025-07-08 18:08:24   |       4251172|FALSE            |cb6e8dff050cb8bc7e4c4b402752bc39a8fd4d6e6ee19c4b687984ae05d71d0d |
|2025-07-08 18:08:24   |       4351128|FALSE            |08dbf2c3f52ac1cd5cff1ed3be3c5a2c6797b075444ab1a747718707d3f75527 |
|2025-11-11 02:18:09   |       4341103|FALSE            |edff72030ea4107e1e52679080685e46bbf9b1ca35f89a30451b3fe8cc6ddced |


Below is all transactions with binding custom unlock time confirmed on the blockchain between heights 3258526 and 3654036 (October 13, 2024 and April 16, 2026).

|transaction_timestamp | unlock_height|already_unlocked |tx_hash                                                          |
|:---------------------|-------------:|:----------------|:----------------------------------------------------------------|
|2024-11-09 00:13:11   |       3277863|TRUE             |d37b6803770ce59c169132223c621eee1fc14625851c03afbe0259841c8f3d1f |
|2024-11-09 21:52:09   |       3278596|TRUE             |6d9fc55de84b1d1510ee068bf59000b1aa6969c1ebf18b0fe128edef681ec4c2 |
|2024-11-09 22:31:46   |       3279325|TRUE             |dc6c0e75a707c549221fa8b74a6a3f199e6688948dcbf0577b2e9711744eefd5 |
|2024-11-09 23:53:12   |       3280035|TRUE             |2fe071da56274d99dfb57c79b54fe8c665f15497aded71f0dc144bb979a080fa |
|2024-11-15 02:45:12   |       3283193|TRUE             |0a5846ef885c4211de666fca42ee276d0cee5d52be00fde08c0cde49213fdca6 |
|2024-11-15 18:56:30   |       3283913|TRUE             |b6fcc94817a82ec8edeb6fcd079f46140f2e6dc935903a70cdc2998880c52f22 |
|2024-11-15 18:56:30   |       3284913|TRUE             |9365090311ddff59eccef6ca678b3f0116bea250f302f50b2ad1a9069bd59c24 |
|2024-11-15 18:59:26   |       3285913|TRUE             |409288eccd1222552ee67099f84a96e8f3132a892d1a58969907d40adbe3fb3f |
|2024-11-15 19:14:50   |       3286914|TRUE             |9d945dd12cab33b209c5c22a900977d4fd382ee333bfde228cb8bd1105a9e6e3 |
|2024-11-15 19:29:59   |       3287912|TRUE             |750448a281f006c6f11ecdda9fd85ad76df203189f15b3584617da84f488dcf9 |
|2024-11-15 19:29:59   |       3288912|TRUE             |025139c03f7220001058030653db735e4b8bcd941464cda0b941b5f1e1976ea6 |
|2024-11-15 20:01:51   |       3289912|TRUE             |fa2af688ba955245c0d100362a6ae25427481f5f6bdb655f941db5a8f39b3e4d |
|2024-11-15 20:01:51   |       3290912|TRUE             |e934edef1722045679e3a1749bcb7476d7b01548d39088d6abf4f415a83d1916 |
|2024-11-16 01:03:56   |       3291912|TRUE             |ce0b8e1fc62504da6e0ba913349dca324872374d49ae84e3ff9b62a7f550de13 |
|2024-11-16 01:03:56   |       3292912|TRUE             |e0e5a52fd5f7d4349c06b61c4ed7476e372906630b65df762d5895419160f683 |
|2024-11-16 01:03:56   |       3293912|TRUE             |1f58ba0fac2af1a1a37ac68841396752f51c747682d74915040900f701ea24bd |
|2024-11-16 01:03:56   |       3294912|TRUE             |b285ad9da58b13995d2695369a7abf3f91861aaf4523bb3e206bd4787e347963 |
|2024-11-16 01:41:04   |       3295914|TRUE             |0ecd5293a98b958fd7d94e3c6650ce33f86bb05a6d4bce1b3a93443433bb7aca |
|2024-11-16 01:41:37   |       3296915|TRUE             |d4feb5cde4b054caec42be685a177fd0a5547bbee34e1f0d4563b33fd8925982 |
|2024-11-16 01:45:31   |       3297916|TRUE             |5b1dee96d47d49e62021692b7e2effe5859be35e995ffa5c4c6118b7f8b2ebd6 |
|2024-11-16 01:58:07   |       3298912|TRUE             |d6aaf3e31043d196fa6a27c59739ab287946d4b06dbc89f02cc874242d19b520 |
|2024-11-16 02:16:23   |       3299912|TRUE             |5db171897653aa84f8f03c96f2d8a60768165b87ea14793b6b4047bdf6901aa7 |
|2024-11-16 02:24:50   |       3300912|TRUE             |36a07b69d517be250bf23cb21265d1f0acaa2c59ada9b4c2bb8a70a8cb2a63bf |
|2024-11-16 02:24:50   |       3301913|TRUE             |a6f9f9ada67d2d0bfa97d456d1b68735136de3d1d819b3f1632c555dc3d9c8d3 |
|2024-11-16 02:53:41   |       3302915|TRUE             |5b8c011d4686da9f2951b029940f060d94186638305fb1268c432f199a492ae3 |
|2024-11-16 03:11:46   |       3303915|TRUE             |d0077fb2190089e0b7ad9f5a2e1f87e283ffd0acb0819c79c2f07607953dee72 |
|2024-11-17 03:32:17   |       3304915|TRUE             |318b20074bd2a8f09ac89bb5813061870c66367c9c084ab67dbdb5009375e105 |
|2024-11-17 03:32:17   |       3305915|TRUE             |12ea3a87244a1e21a419f86dc145355251d9085beffcc6ef54bf030c2a00e6b1 |
|2024-11-17 04:13:37   |       3306915|TRUE             |6c55a60ebfb4f8827502023d2fe0fa10f84ea4f28df0550d5f3def143972f684 |
|2024-11-17 04:13:37   |       3307916|TRUE             |7728111c769dd168af6fc3d6a28b98ba2cf19e01b8a0c4c595a746e996b68aaa |
|2024-11-17 18:04:46   |       3308918|TRUE             |738a27a02b3f72d287451db5c0c31a875d19c26aa50bff103d3997b7931dbe19 |
|2024-12-08 07:32:51   |       3309918|TRUE             |573763b23b94c2eeb87c7dbfb8ea869a99565627746fc5af55f2d4050c1b5404 |
|2024-12-08 07:32:51   |       3310918|TRUE             |7e0cbd8b4982bf800fad9d81181dc46afc6c1ab2b971229ad14685cda987bf57 |
|2024-12-08 07:37:10   |       3311918|TRUE             |e95a478a18b30ed3b0e92f17ed1877afb06bca80261a76d7b16c8e0dc5a370aa |
|2024-12-08 07:37:10   |       3312919|TRUE             |6f9ab44fa4f75427103b9f55d60219a39afb6671a504fa8fcb5986c3a12b6462 |
|2024-12-08 08:08:20   |       3313919|TRUE             |62e0d9a464c17289df3c89084fc9e27f308b31ff786156bd260831a7514c308a |
|2024-12-08 08:08:20   |       3314919|TRUE             |a9b2ae48fa40cc3cafab95c8067413803a34e2cb7ef391bc8d17bb12580ad6d5 |
|2024-12-08 08:08:20   |       3315919|TRUE             |105488eb91ff753527c4cf408624f265eb5cccca3f4df81dff2a5d7aef0ad360 |
|2024-12-08 08:11:43   |       3316919|TRUE             |80eb19ab6f764f4bba3e79ab74a5839da6ebbbebcec9779156b17b7ad95dfc0d |
|2024-12-08 08:32:57   |       3317921|TRUE             |a56b4a19d599dc9de58ebdc5f1f42e38cedd624ad6564b8379aa8b7b9b70b30c |
|2024-12-08 08:32:57   |       3318921|TRUE             |2757607e5a079f4fc5019bfee5fed7b0915730083e0c19aae082af580bea3439 |
|2024-12-08 08:35:14   |       3319921|TRUE             |ea0abdb7cd4956fec196519a0b2d3a17e5727d9f08b37d530e509f4eeab4b314 |
|2024-12-08 08:35:14   |       3320922|TRUE             |783f9cba615d9737d1fea3836a9814df043b98a6e309b354620703967f5df65a |
|2024-12-08 08:52:21   |       3321922|TRUE             |fd3e3fd5c98b587cd59cc61cfbe7633c4ec1d18559aa6ac68fa90f765f180013 |
|2024-12-08 08:52:21   |       3322922|TRUE             |66b915691aca3b2a2486744a5ddd867032b5cc3600c34cb78201f5cab81dec5d |
|2024-12-08 08:52:21   |       3323922|TRUE             |1791c04fcd2e288797d64904f474596ae093d0f6a5ae3bf34606f3246eb16122 |
|2024-12-08 09:02:50   |       3324922|TRUE             |9f7efea512b6a6da7cc69e54621322a0fa8027a5d99c11596fbf80f9224f43cd |
|2024-12-08 09:02:50   |       3326012|TRUE             |df936e300e93cd8172323711e0a95d9e07f91a6f85d9dbcf548c1bf86ecdcbfb |
|2024-12-08 09:15:09   |       3327012|TRUE             |5e1806fdefcda52c06bf46706a151e676cdecf43b6f95dfa9ddca34d68e74a04 |
|2024-12-08 09:19:22   |       3328012|TRUE             |c80e6399d49059a09118fad8864787eba9209290cc6ab6628003c893ad0e630e |
|2024-12-09 03:57:18   |       3329012|TRUE             |1c911964f277c66eb9a0d0354336eb3853e16cfd6d377668165e0cc18da515ee |
|2024-12-10 10:41:23   |       3330012|TRUE             |cfdbbdd8b7769c36d566e4cd818ed2919aec90804890b393a9d7f0cdd2872e1a |
|2024-12-11 03:17:22   |       3331012|TRUE             |89dd60afbea002496b78ee2204949cea38e3f0825659a3627e532455bf587ef4 |
|2024-12-11 03:50:15   |       3333012|TRUE             |43760db256e1eac643370fb2b8de5bb7d14c9a84e0c2a564e2f41e82f1da9544 |
|2024-12-11 03:50:15   |       3332012|TRUE             |822e2eec8255eed79299bf2cbf8aa3c40b83fadfd25718db57adcf3ea4d50871 |
|2024-12-11 03:50:15   |       3334012|TRUE             |e3e801f93cde776349d34621b6ab3edd2d06ae7c7d446327d62c6cbe7db12b3c |
|2024-12-11 03:50:15   |       3335012|TRUE             |fc25742de69ff61a289d336f2f61884531aa0f19e04852f414f0ec701636c449 |
|2024-12-11 04:56:14   |       3336012|TRUE             |c0c0855144c57930184f902f352b7025508881184d3e4a8188cb76548f19e2c9 |
|2024-12-11 04:56:14   |       3337013|TRUE             |2fb068ce3a1751040cc61bcb47eae01741a3e27832613df9469ac3de32584368 |
|2024-12-11 04:56:14   |       3338013|TRUE             |0a5e182f1c8ed42368917a06d8387fc29ee51c38b70baf82928f601656c2ae41 |
|2024-12-11 04:56:14   |       3339013|TRUE             |661b2cf47d790ad39ea2d139d6a4ae413648f195c8d8921e3b75ccd6c2d2fbd2 |
|2024-12-11 05:35:53   |       3340014|TRUE             |b7a34377ddf9c95d88dca6f869e4405242b9bbb21ff3a5c113f51470d3af603e |
|2024-12-11 05:35:53   |       3341014|TRUE             |7d4dc8cd3031803f2ec0cce469778318daddc40b65b21be66dc99c5f0a137cff |
|2024-12-11 05:53:43   |       3342014|TRUE             |c97e0ffd09c26b885ebc16339e2227635b98941f420aa06c836fe457c2c6ff9b |
|2025-01-10 15:25:16   |       3323323|TRUE             |5ecbb2e6227edc0b6acac0b76e46bf0d109601b41e9a8bfff6e64cdf027eb1f1 |
|2025-02-01 23:31:15   |       3338609|TRUE             |b4433900718e1d6e386bb80c7160b543e4b65349522916ae43196c0db0b56e64 |
|2025-02-05 03:14:00   |       3340972|TRUE             |b3ed3a9bf3fd370c887b6710dcee34f36d8ede14e8315bd1f38c8b4fd45c597d |
|2025-02-27 02:37:13   |       4181692|FALSE            |0ebc0f3336050a954b27cab3cf901a33cc0b3c2e57dfe6c213007d3202ac7777 |
|2025-03-14 08:40:25   |       3630232|TRUE             |e418c9bcbcfde4767f0a137b48f60cfabb53b07afecab656ada5e2b04e082ef4 |
|2025-03-14 11:51:51   |       3867520|FALSE            |054cd188b58bb1d0474180c6660df1d86fd34a4ce325efd2fbeaffc1d542e1b1 |
|2025-03-14 13:58:09   |       3867573|FALSE            |adf72c98932a0dcd7215c0d00a97dcb5917ce1935480e214c26c11aef9790cf3 |
|2025-03-14 15:07:40   |       3867614|FALSE            |25aa360621c20abe3e0c6c9840a961c9e55dd6e7db52a5f77defb228b356322f |
|2025-03-14 15:46:57   |       4167642|FALSE            |24cadd5444d55ee9f26c415d2cf389dfcdda0c51bc998f0ea34abc1490a93bae |
|2025-03-14 16:28:16   |       4067661|FALSE            |23d5dde36bacffcb7e979c78e8988548b3c4fb16e7051fc4eddcfd5708d29ff6 |
|2025-03-14 18:07:22   |       4067725|FALSE            |392ee5e2f66dff153b06c8cb63dc2555e61b51ace2c2582b0919dcce88601052 |
|2025-03-15 17:40:21   |       4268422|FALSE            |03758a9c7279019be3490bd99c8054c4828d0a79571e44f9dd40d1f93ba88585 |
|2025-03-16 09:46:58   |       4168963|FALSE            |7e473eb0165a14dabbff0fe487ea2e3bc05a8eaf9494771a3984d1afabf2298b |
|2025-03-17 10:05:37   |       4169669|FALSE            |f9d3678be0a29751c549d809e0845b0f372175bd44efca9768d5e1eb94aa896a |
|2025-03-17 16:03:50   |       3371853|TRUE             |9fa7c11424cc580fbf1fb0a496cb7b6bc6bf01899422dff4615d11576a6ace90 |
|2025-03-19 01:50:03   |       3372859|TRUE             |142b7de27de3d531c3a3fbe7cad304a941f63cc5901fe0b6efea16911eb46612 |
|2025-03-19 05:53:54   |       4170982|FALSE            |d4ef9dea7f183b8f8cdacaaf107c8d1d0b5ec6339909fbae3c75a691bd0eb584 |
|2025-03-19 08:38:53   |       4171088|FALSE            |f8a590015cae85782c6cb348a0d9a675df73eb39f33d3618d5342523b443a44c |
|2025-03-20 05:39:50   |       4171691|FALSE            |76888c7a9f0a158144cf79ad7adb95bd5fa6d18d9596f6de454cf69f48267bc7 |
|2025-03-21 01:33:00   |       3374282|TRUE             |41d6a9adb3f1c6dcdd4bfd5dfdbb40a2401fd8f4699e35a8d952361d4adc63dc |
|2025-03-23 14:24:20   |       3375124|TRUE             |19fad3efddea39fc0c521a201904e2d34de5274d81c21c4721b69f4db688e15b |
|2025-03-25 08:10:57   |       4175362|FALSE            |eb92e655751e059448f54e65f30973605a695b313d3ffe4719bd123242c883d9 |
|2025-03-25 13:30:18   |       4175528|FALSE            |91405854e4badcdf61afa65c6d84aac2ef29146ee4f7310abc8f81251c9a4c92 |
|2025-03-26 03:38:22   |       3376940|TRUE             |d79821fa05681244c1e537fa0dc70411cc632450cde2e4166c4c0749efacdd76 |
|2025-03-28 09:56:35   |       4177599|FALSE            |e8d6f4fe98ab2623e2449eaaebd8ba1956d4a1b0c97038be4e5f22267f457f52 |
|2025-03-31 19:28:14   |       4180048|FALSE            |cccc9066f48ce043cc6be4025e77e30b4e555eb55c18a1077ecd7f1241c92f5b |
|2025-04-02 15:34:09   |       4181365|FALSE            |bef6e6de3baf78d77174c7fb5c3a601f0c861af640d2750da9d36839482c4858 |
|2025-04-08 16:58:42   |       4185701|FALSE            |55475aae5f5576168cc43c50649524c98d2bdfefe4b31b14b74f7c72cf0cd681 |
|2025-06-28 00:19:21   |       4293212|FALSE            |96a657af388225933f00edbe620540ad3183046ff4d976c6fbd110876b55f588 |
|2025-07-08 18:08:24   |       4251172|FALSE            |cb6e8dff050cb8bc7e4c4b402752bc39a8fd4d6e6ee19c4b687984ae05d71d0d |
|2025-07-08 18:08:24   |       4351128|FALSE            |08dbf2c3f52ac1cd5cff1ed3be3c5a2c6797b075444ab1a747718707d3f75527 |
|2025-11-11 02:18:09   |       4341103|FALSE            |edff72030ea4107e1e52679080685e46bbf9b1ca35f89a30451b3fe8cc6ddced |


Below is an updated graph of [jeffro256's unlock time running balance](https://github.com/monero-project/monero/pull/9522#issuecomment-2420299652):

<img width="800" height="800" alt="Image" src="https://github.com/user-attachments/assets/a2c2087e-6d8c-4014-9ce0-315ab5c633bf" />



## Code

Run [this script](https://rucknium.github.io/OSPEAD/CCS-milestone-2/OSPEAD-docs/_book/ring-gathering.html#code) with `current.height <- 3654036` until line `output.index <- returned.temp$output.index.collected`. Then:

```R
recent.timelocks <- output.index[block_height > 3258526 & output_unlock_time > 3258526 & tx_num != 1, ]
# tx_num != 1 to exclude coinbase txs

setorder(recent.timelocks, block_timestamp)

recent.timelocks.display <- recent.timelocks[, .(unlock_height = unique(output_unlock_time),
  transaction_timestamp = as.POSIXct(unique(block_timestamp )),
  already_unlocked = unique(output_unlock_time) < 3654036), by =  tx_hash]

setcolorder(recent.timelocks.display, c("transaction_timestamp", "unlock_height", "already_unlocked", "tx_hash"))

knitr::kable(recent.timelocks.display, format = "pipe")
```

Code for locked running balance:

```R

library(data.table)

locked <- read.csv("blockchain-find-locked-output.csv")

setDT(locked)

setorder(locked, block_index)

png("locks_balance.png", width = 800, height = 800)

plot(locked[block_index <= 3654036, .(block_index, nonstandard.blocktime.locks.balance)], type = "l")

dev.off()

```


# Action History
- Created by: jeffro256 | 2024-10-22T19:13:09+00:00
