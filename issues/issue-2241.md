---
title: '[idea] "Trusted Decoys" to counter possible Miner Sybil Attack'
source_url: https://github.com/monero-project/monero/issues/2241
author: dnaleor
assignees: []
labels: []
created_at: '2017-08-02T20:34:10+00:00'
updated_at: '2017-08-19T20:23:48+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
After reading [this article](https://steemit.com/cryptocurrency/@anonymint/is-monero-s-or-all-anonymity-broken) I think one of the issues mentioned can easily be solved.

A miner can create a lot of transactions for free by mining them privately. If the attacker doesn't broadcast them to the network, he will receive the transaction fee. This enables him to create full blocks that only consists of transactions of which he owns the keys for the TXO's. 
A wallet picks decoys for ring signatures at random. If a lot of hashing power is executing this Sybil Attack, the chances of picking lots of these compromised TXO's as decoys is high. 

To solve this, a wallet (node) could check whether a transaction was broadcasted to the network before it appears in a block or not. If the wallet saw the transaction as unconfirmed in the mempool, it gets a flag. When the wallet wants to create a new ring signature, it will try to use at least some of the "Trusted Decoys" in the ring signature, thus making sure that at least not every decoy is compromised by the attacker. 

WARNING: if your node is not online 24/7, you can be exposed to timing attacks: if you only connect for an hour every day between 13:00 and 14:00, you will only pick decoys that were created during that timeframe. If you then spend a TXO with a different timestamp, your ring signature is weakened. So either you need to have your node online 24/7 or your wallet needs to pick some random decoys that possibly aren't trusted, to avoid this timing attack.  

# Discussion History
## shelby3 | 2017-08-03T04:15:08+00:00
[Incorrect](https://steemit.com/cryptocurrency/@anonymint/re-finitemaz-re-anonymint-re-finitemaz-re-anonymint-re-anonymint-is-monero-s-or-all-anonymity-broken-20170803t034833586z).

## dnaleor | 2017-08-03T09:42:22+00:00
> The perpetrator doesn’t need to keep their spam transactions private. They would gladly have other miners add them to the blockchain. There is no way to distinguish a spam transaction from a normal one.

You claimed it was a free attack. This is only the case if the attacking miner mines his own transactions.

## shelby3 | 2017-08-03T16:01:22+00:00
Perhaps [this Reddit comment](https://www.reddit.com/r/Monero/comments/6r2xsm/is_moneros_anonymity_broken/dl3jdrj/?context=1) will help you understand better.

There is no need for the miner to keep the transactions private. He can submit them over the network and let any miner include them and fund his transaction fees from the transactions he includes in his blocks. Thus net transaction fees are zero.

## JollyMort | 2017-08-16T23:25:44+00:00
How is it free? He sacrifices his margin for the "free" attack. If all other miners are profitable with pocketing both block reward and the fees, then the attacking miner may not be profitable (he has to pay for electricity, remember) if he gives up his fee income to make an equivalent amount of dummy TX-es.

Miner 1, normal: mines a block with 1XMR block reward and 0.1XMR others fees, pays 1XMR for electricity. Earns 0.1XMR from what remains. If fees are big, will increase the blocks and earn more.

Miner 2, "attacker": mines a block with 1XMR block reward and only his own TX-es to fill the blocks. Pays 1XMR for electricity. Earns 0XMR. If he expands the blocksize, goes into negative earnings due to block reward penalty. If he has 10% network hash power, means he will control 10% of new outputs, so what? It would only weaken the effectiveness of ring signatures a bit. For 51%, we have other problems, too - what a surprise. Show me a blockchain which is not vulnerable to a 51% attack.

Miner 3, "attacker": mines a block with 1XMR block reward and others TX-es, gets 0.1XMR in fees. Uses those 0.1XMR to broadcast transactions which get picked up by other miners. Pays 1XMR for electricity. Earns 0XMR. If he broadcasts more transactions than what the 0.1XMR can pay for, goes into negative earnings but may get more than 10% outputs for a while (until he runs out of money / or is outbid by higher-fee TX-es if he causes TX-pool congestion).

So how do miners 2 and 3 get anything for free?

## anonimal | 2017-08-17T20:37:45+00:00
>Incorrect.

Are there any better sources out there other than some sociopath's quips on steemit? A paper or two perhaps?

## panopolis | 2017-08-19T20:23:48+00:00
As others pointed out the attacker in this scenario does not have to mine all of their own TX for it to be "free", and regardless, such an attacker would consider it cheap compared to the value of the information obtained, even if they do not recoup all tx fees. Also, correct me if I'm wrong, but just because a tx is not in your local mempool does not mean it was mined in secret. It may simply be that the tx had not propagated to your node before someone else mined the block. I think even if the described attack is feasible, in the worst case, the attacker would be able to analyse the block chain in a way comparable to bitcoin, but not more so. The privacy mechanics would still hold against everyone else besides the attacker. Those who are worried about this theoretical attack can still be anonymous by taking care not to leak IP address, or leaving a trail linking to bank account, etc

# Action History
- Created by: dnaleor | 2017-08-02T20:34:10+00:00
