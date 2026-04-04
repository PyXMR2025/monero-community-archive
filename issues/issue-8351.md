---
title: Stealth_addresses outside prime subgroup
source_url: https://github.com/monero-project/monero/issues/8351
author: DangerousFreedom1984
assignees: []
labels: []
created_at: '2022-05-23T16:51:47+00:00'
updated_at: '2022-07-03T16:32:02+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hello guys,

I would like to raise awareness about a specific issue related to the EC point multiplications. At the moment Monero allows multiplications outside the prime subgroup and it may be a bad idea to allow that FOR EVERY POINT (Please give me your opinions about this statement).

Issue: I have been verifying the blockchain using the LibSodium library, which is a library "safer" than Monero as it only allows multiplications inside the prime subgroup, in order to check ring signatures and verify if the key_images belong to the prime subgroup, and noticed that there are many points (stealth_addresses) that actually don't belong to the prime subgroup. I have finished scanning (up top height 2651355) and the full list can be found here: https://github.com/DangerousFreedom1984/monero_inflation_checker/blob/main/points_outside_subgroup.txt .

So far, for the first 2.5 million blocks, there are 8931 transactions with 16 different stealth addresses that don't belong to the prime subgroup. Most of them come from version 1 blocks and they are basically the point P=9b2e4c0281c0b02e7c53291a94d1d0cbff8883f8024f5142ee494ffbbd088071, which is the genesis point copied from Bytecoin (https://github.com/bcndev/bytecoin/blob/c3d9b94e0d34ee486ff35e7c781f673c1097b955/src/crypto/crypto.cpp#L153). The points (Stealth addresses) are: 

{'b10ba13e303cbe9abf7d5d44f1d417727abcc14903a74e071abd652ce1bf76dd', '52d128bc9913d5ee8b702c37609917c2357b2f587e5de5622348a3acd718e5d6', 'fccffc95974651a33178b0aa235f058c3bc84769aa77939a53c1e936a991152d', 'e6f4ef5858e51bc046b195b41df7720a5583fbc92a6bff15d8216ad30d9a6949', '7c09e068d605f7debf5271f97901d122cf3430649ac25328deb91e8498972357', 'c574420256922b0783196e42c98156814e61d9ffa87c1262089be1d42e5f0d27', 'bc14c62db31ca6441c469443452fb609f3d8153d9855d7b4ee418fe63c5e35bc', 'b8ed916c56b3a99c9cdf22c7be7ec4e85587e5d40bc46bf6995313c288ad841e', '9b2e4c0281c0b02e7c53291a94d1d0cbff8883f8024f5142ee494ffbbd088071', '1b452b4ac6c6419e06181f8c9f0734bd5bb132d8b75b44bbcd07dd8f553acba6', '3e8cd0f1cd3035c5e5b7b78d7aa35c0f45d395cb39b69df2a71d166a938efc15', '8e7b4a8916c466874788030bb3e93db765016bee09313690412f910e045ec3ea', '2a74a3c4c36d32e95633d44ba9a7b8188297b2ac91afecab826b86fabaa70916'
'4844a2fec06bc897540533f500438d2c3d7a1f11b8715b28a9611de2b2ca73ae',
'6910bdf7beeae858bb3d3ded00184ed56ab62f8b13948a1bd9a9f63036e876f4',
2757dd54027e93c917251de2cc6777f7a3fa484f5b244ab54bf8783e7da80c36}

NOTICE THAT I DID NOT FIND ANY KEY_IMAGE POINT THAT IS OUTSIDE THE MONERO PRIME SUBGROUP. WHICH WOULD MEAN (IF I HAD FOUND) THAT SOMEONE COULD HAVE EXPLOITED IT FOR A DOUBLE-SPENDING.  

Severity: It is not severe as it cannot be straight forward exploited as Monero nodes checks if the key_images belong to the prime subgroup. Although there may be possible attacks. (https://eprint.iacr.org/2020/823.pdf). Please give me your thoughts on that as it may be worth to discuss.

This issue has other implications too:
- Prevents other implementations of wallets and nodes that use the LibSodium library. (A block/transaction containing a stealth-address or a ring-member outside the prime subgroup would be accepted in the Monero software but would raise an error on wallets using the LibSodium or Ristretto library)
- Damages fungibility. Someone looking at the ring-members could tell that a member does not belong to the prime-subgroup and consequently deduce that this member is or is not the owner of the transaction if he has more information about how it was generated (with the last Monero software or not).

Proposed solution:
Ideally, I believe that would be better to play safe and only allow multiplications inside the prime subgroup, for example using Ristretto. This solution may be a bit too complicated as implementing it would require a lot of efforts and maybe a big change in the source code. 

I propose then that we also check if the stealth_addresses belong to the prime subgroup when generating and mining a transaction. In this way, we would prevent future issues of compatibility and fungibility as we would be sure that the ring members (and all EC points stored at the blockchain basically) are inside the prime subgroup. AFAIK, the rangeproofs are not affected. There are specific operations in Bulletproofs to make sure that the points are stored in the prime subgroup. 

It should not be hard to do as we need to add just one more verification in the same way we do for the key_images.

I would be happy to propose a PR with the modifications if you guys think it is worth.

Please let me know your thoughts ;)

# Discussion History
## UkoeHB | 2022-05-23T22:05:35+00:00
I am a little skeptical about the value of enforcing this.

1. There are already non-canonical onetime addresses in the ledger, so a ledger-parser always potentially has to deal with those anyway.
2. Outputs with non-canonical onetime addresses are unspendable by all existing wallets (i.e. even if you supposedly own such an output, you will never find it through normal view key scanning), so making outputs like that is essentially burning funds pointlessly.

## DangerousFreedom1984 | 2022-05-23T23:10:23+00:00
I agree that it might be burning funds. But we don't really care about the person spending. The problem I see is that it damages the fungibility of other transactions. As a thought experiment, imagine that someone is just creating a bunch of txs outside the prime subgroup. Let's say at a rate of 10% of txs. What is the implication of that for the fungibility of the other transactions? 10% less? I don't know. I would guess so. But enforcing stealth_addresses to be in the prime subgroup might avoid this 'theoretical problem' as it is really not a practical issue by now.

## UkoeHB | 2022-05-23T23:27:02+00:00
Invalid keys definitely affect fungibility, but I think this is in a special class of fungibility defects. If your wallet is making non-canonical onetime addresses then you are almost definitely burning funds, so you have a direct incentive to fix it.

In reality, there are a number of ways like this to burn funds that would reduce fungibility (e.g. set txo pubkeys to identity, reuse onetime addresses, etc.).

## DangerousFreedom1984 | 2022-05-24T10:18:21+00:00
Yes, you as a person have a direct incentive not to do it, I agree. But what if I want to attack the Monero network by compromising the fungibility? It is actually very easy to coordinate with others that also want to attack the network. Just say: substitute the stealth_address by a point outside the prime subgroup. Then let's spam it. Currently we are at 25k txs per day. Supposing that we pay 0.05$ USD/txs, it would cost $1250 per day to deanonimyze a good deal of txs. I don't know how to evaluate correctly but if remember well, most of ring members are chosen within the last 3 days or so. So if I do it for three days than I would publicly hurt at least half of the fungibility for all txs during these days. What do you think? Is this reasoning correct?

I don't know the advantage of allowing it. I just see disadvantages. I'm proposing adding one point multiplication for each output. I don't think the cost is that big.

## UkoeHB | 2022-05-24T12:28:07+00:00
> So if I do it for three days than I would publicly hurt at least half of the fungibility for all txs during these days. What do you think? Is this reasoning correct?

You are correct, however adding this check doesn't eliminate the attack because there are other ways to execute it (most of which are a lot easier than adding a torsion element to an EC point). Re-use onetime addresses, use hash-to-point of something, encode something weird in the tx extra, publish the onetime private keys of all your spam outputs, ...

> I don't think the cost is that big.

The added verification cost is not that big. The question for me is about hard fork policy. Is it worthwhile to hard fork to add a rule that A) hasn't been violated in years, B) there is a direct incentive to avoid, C) doesn't (and can't possibly) fully solve the problem(s) it addresses?

## DangerousFreedom1984 | 2022-05-24T15:10:59+00:00
Thanks for the answers. I agree with your points. I didn't mean to add this check for every transaction since the beginning, otherwise it would fail for the blocks listed above. I wanted to enforce from now on. I don't know exactly what should be done but should be doable I think. Don't need to add necessarily in the coming hardfork, but maybe would be nice to consider it for the next one. I haven't finished checking the rangeproofs yet but up to this point only these stealth addresses are outside the prime group (from all points stored in the blockchain). Would be safer I think if the miners enforced that only points in the prime subgroup are stored in the blockchain if it is basically for free.

## Mitchellpkt | 2022-06-01T15:54:52+00:00
Interesting find @DangerousFreedom1984 good eye :)

Could you share a few example transaction hashes? I want to take a peek at the data.

## DangerousFreedom1984 | 2022-06-01T16:14:00+00:00
> Interesting find @DangerousFreedom1984 good eye :)
> 
> Could you share a few example transaction hashes? I want to take a peek at the data.

Sure. Just look at the file: https://github.com/DangerousFreedom1984/monero_inflation_checker/blob/main/points_outside_subgroup.txt . This is not anymore updated as I am still scanning the blockchain but you can find the transactions looking at their block heights. (Sorry I didnt log the tx hashes) 
For example, for the first one, you can see the transactions at height 200382 (which is only one) and get its hash ([86c73c157e6fe10aa98c78f25d5a42dbc531e697cd8a366b1292e71cf372b33b](https://xmrchain.net/tx/86c73c157e6fe10aa98c78f25d5a42dbc531e697cd8a366b1292e71cf372b33b) )

## Mitchellpkt | 2022-06-01T16:23:56+00:00
Ah perfect! I didn't realize that column was block height. Thanks :pray: 

# Action History
- Created by: DangerousFreedom1984 | 2022-05-23T16:51:47+00:00
