---
title: 'Radical idea: Fix Monero''s iterated-EABE traceability problem and eliminate
  wallet scanning times by tagging outputs with a subaddress hash'
source_url: https://github.com/monero-project/research-lab/issues/75
author: knaccc
assignees: []
labels: []
created_at: '2020-07-09T16:20:02+00:00'
updated_at: '2020-09-01T12:39:32+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**The problem:**

The owner of a large exchange can uncover with high probability the transactional relationships between users of the exchange.

This is the iterated-EABE traceability problem. The first time EABE happens, there is a 2-hop anonymity-set size of 11+11^2=132. The second or third time EABE happens, the anonymity set size almost always collapses to 1, given that A's output shows up in the upstream blockchain graph twice or thrice despite there being tens of millions of outputs that could have been chosen from. Almost all untraceability is lost due to the intersection of 132-size anonymity sets. Even worse, increasing the ring size does not help much, given that even reasonably larger ring sizes will be overwhelmed by the huge numbers of outputs that could have been chosen from. Churn is also flawed because it causes blockchain bloat and because churns often stand out on the blockchain.

This situation does not just compromise transactional relationships with respect to the exchange. We're just one exchange hack away from huge numbers of real-world identities and the transactional relationships between them being exposed permanently to the world. 

**The solution:**

The anonymity set size is 132 on the first EABE occurrence, but needs to remain as 132 on subsequent EABE occurrences.

The way to achieve this is to change Monero's protocol to include a 32-bit hash of the destination subaddress alongside every output in a transaction. Wait, what? That's undoing the benefit of stealth addresses! You're crazy! "I'm not. No, I'm not." _- Joker, The Dark Knight (2008)_.

Putting a subaddress hash on every output will clearly publicly identify the relationship between outputs arriving at the same subaddress (but not to the same wallet). I find it difficult to see why this would be of any great loss. If a user is handing out a different subaddress to each person that sends funds to them, then the person sending funds to them already knows how many times they've sent funds to a particular subaddress.

Now that all outputs on the blockchain can be grouped by subaddress-recipient, a wallet can be much more intelligent when choosing an anonymity set. For outputs received from any particular source (e.g. the exchange), care can be taken to ensure that owned outputs from a particular source are repeatedly spent using decoys that are from the same decoy output groups.

To spell out the proposed process of choosing decoys:

1. The wallet will group incoming outputs by the subaddresses in the wallet they were received to.
2. On the first spend of any of the outputs in any particular group, randomly choose decoy outputs from the blockchain. Take care to often choose decoy outputs that have a group size of 2 or more. This is because if you want to anonymity among those that withdraw xmr from an exchange on more than one occasion, then you need to use decoys which at least some of the time represent subaddresses where funds have been received on more than one occasion.
3. On subsequent spends of any of the outputs in any particular group, always choose new decoy outputs from the same groups of the decoy outputs from the first spend from that group. It is also acceptable and perhaps desirable to often choose decoy outputs 1 or 2 hops downstream from the decoys in those decoy groups.

Not only does this solve the iterated-EABE traceability problem, but it also eliminates wallet scanning times. There no longer needs to be a compute-expensive EC variable-base scalarmult per tx output to scan for funds. Remote nodes can provide bloom filters that allow wallets to determine if any new outputs are waiting for them. Monero can become "instant-on". If Monero's tx volume increases 10x or 50x from here, eliminating wallet scan times will not just become useful, but essential.

One other bonus: it makes outputs [Janus-attack](https://web.getmonero.org/2019/10/18/subaddress-janus.html)-proof.

Note: thanks to @SamsungGalaxyPlayer for pointing out that there should not be these type of hashes on change outputs, in order to avoid linking outgoing transactions. Instead, the hash could be e.g. lower_32_bits(keccak(private view key || key image of spent output)).

Update: To avoid it being possible to know how many txs have been sent to donation addresses, a second 32-bit 'decoy' hash could be attached to each output. Now, the wallet owner will get false positives when searching for funds, but will achieve more privacy. 

Update 2: This idea has been refined greatly here https://github.com/monero-project/research-lab/issues/75#issuecomment-663935804

# Discussion History
## tevador | 2020-07-09T17:58:24+00:00
> Putting a subaddress hash on every output will clearly publicly identify the relationship between outputs arriving at the same subaddress (but not to the same wallet). I find it difficult to see why this would be of any great loss. If a user is handing out a different subaddress to each person that sends funds to them, then the person sending funds to them already knows how many times they've sent funds to a particular subaddress.

I can think of at least two cases when this "breaks" privacy:

* Donation addresses. When someone publishes a donation address, everyone will know when it receives donations.
* Pool miners. Pool miners are typically paid periodically to the same address. This may lead to some heuristics even if the address is unknown, e.g. the same address getting paid 60 blocks after a block found by some pool is likely an address of a miner on that pool.

## knaccc | 2020-07-09T18:03:39+00:00
@tevador Great thoughts, thanks. I'm very interested in hearing as many thoughts on this proposal as possible, because this is a very important problem.

## binaryFate | 2020-07-09T23:54:53+00:00
Not commenting on merit of general idea, but just to address @tevador concerns, could we salt the hash with the specific output? So it would be hash of (the destination address + output pubkey) alongside every output. Or whatever uniquely identifies the output like txid:output_index.
Would make scanning a tiny bit slower (need to compute a hash for every output instead of just comparing the same string) but I guess negligible compared to improvement you have in mind? 

## knaccc | 2020-07-10T00:20:18+00:00
![iteratedeabe-01ps](https://user-images.githubusercontent.com/25644571/87102937-6f11e180-c24b-11ea-8ff2-fcf9dcb846cd.png)

## moneromooo-monero | 2020-07-10T00:51:28+00:00
> On the first spend of any of the outputs in any particular group, randomly choose decoy outputs from the blockchain. Take care to often choose decoy outputs that have a group size of 2 or more. This is because if you want to anonymity among those that withdraw xmr from an exchange on more than one occasion, then you need to use decoys which at least some of the time represent subaddresses where funds have been received on more than one occasion.

Does this mean the wallet assumes that when it sees a tag appear twice, and not for the wallet, it assumes it may come from an exchange, but doesn't know which one ? And the intent is to hope to select at least a few that were sent from that exchange ?

Also, this cannot be consensus since subadresses aren't known by the verifiers, so an evil exchange could generate random hashes, thus preventing wallets from using this.

## knaccc | 2020-07-10T00:59:15+00:00
@moneromooo-monero the hash is just a simple hash of the subaddress. So alongside every output in every transaction (whether involving exchanges or otherwise), the hash that appears corresponds to whatever subaddress (or main wallet address) the recipient asked for funds to be sent to.

All tx senders, including exchanges, must use the correct hash, or wallets will not notice the incoming transaction because wallets can now directly look for hashes matching wallet subaddresses, instead of doing compute-heavy ECDH scanning.

Tx senders could send the wrong hash, but then they could also send the wrong tx-pubkey to cause the wallet not to notice an incoming transaction.

> Does this mean the wallet assumes that when it sees a tag appear twice, and not for the wallet, it assumes it may come from an exchange, but doesn't know which one? And the intent is to hope to select at least a few that were sent from that exchange?

A wallet only needs to find groups of outputs that it can be reasonably sure are owned by the same wallet. It does not need to hope it finds outputs sent in txs by any particular exchange (or by any exchange at all). As long as this scheme is in place, everyone has to assume that if "A" were to ever be the only exchange user that appears in all 3 branches, that was just bad luck and not a coincidence that can be read-into.

For this scheme to work, all that matters is that it's not only A's outputs that appear in all 3 branches, but other users' outputs appearing in all 3 branches too.

@binaryFate The objective has to be to group outputs on the blockchain by recipient-subaddress, so it would be counterproductive to try to obfuscate the hash such that this was not possible.

## UkoeHB | 2020-07-10T01:46:24+00:00
I see at least three issues with this proposal.

1. It does not fully solve what it attempts to solve, making the cost-benefit analysis very difficult. Once some decoy partners have been selected, you are kind of stuck with them. Imagine if your partners stop making transactions. Eve could use guess-newest to decide Alice, whose recent outputs were included in Bob's received outputs, was Bob's financier.
2. It either weakens the spend-age output selection algorithm (if at least some decoys are randomly selected from the distribution), or makes it hopelessly unusable (if decoy selection is highly constrained by past decoys selected). Spend-age heuristics such as guess-newest would become stronger.
3. It creates anonymity puddles that may weaken plausible deniability for people with certain behaviors. For example, there is a clear bifurcation between new wallets (or accounts) and those with a history. New wallets must make their first transactions from the set of outputs with low history, since older wallets will be pulling from other accounts with multiple outputs. However, if a new wallet receives an output from an older wallet, that output might easily be flagged as spent.

I expect users who find these heuristics uncomfortable or hard to imagine ways of circumventing will eschew subaddress tags altogether. Such users will either fall away from Monero, or suffer from reduced confidence in it. These are the users who today are less likely to be affected by iterated-EABA, since they have developed techniques of maximizing the current system. For example, by churning, avoiding exchanges, creating one-off wallets, etc. I'm guess they are the same users that find iterated-EABA is most concerning.

## knaccc | 2020-07-10T01:59:10+00:00
@UkoeHB thanks, I'll ponder your points. If decoy buckets get stale, the wallet could initiate a churn to make a clean break and select new buckets. Also, decoys should be chosen from some 1-item buckets, to prevent the issues with new wallets not having their outputs chosen as decoys. I am aware that these points do not completely address all of your concerns, or completely address any individual concerns. I'm hoping to get people thinking about what the proposal should be, and not just about whether this proposal is workable or not.

## knaccc | 2020-07-11T08:23:29+00:00
To reframe the proposal:

Through the lens of "does this fully solve untraceability"? The answer is no, therefore the proposal can be dismissed.

But imagine that the current state of Monero was that it had ring signatures and outputs tagged with subaddress hashes, and provided an instant-on UX.

Through the lens of "does removing the subaddress hash-tagging fully solve untraceability"? The answer is clearly no. Given that the downside of dropping subaddress-hash-tagging would be to scrap Monero's instant-on capability and replace that with multi-hour waits for anyone that didn't keep Monero running constantly, would we have removed subaddress-hash-tagging?

## knaccc | 2020-07-11T14:35:36+00:00
One other quick thing: to avoid disclosing the count of transactions going to donation addresses (or to any addresses when those addresses becomes known), more than one address-hash could be marked against each output. Now the wallet holder gets false positives when looking for incoming funds, but that's not a very significant burden and it provides plausible deniability.

## UkoeHB | 2020-07-11T17:52:10+00:00
"imagine that the current state of Monero was that it had ring signatures and outputs tagged with subaddress hashes"

When proposing to change something, if it is difficult to see the cost/benefit leaning one way or the other, I believe maintaining the status quo is the Schelling Point.

On another note, I have been thinking about the iterated-EABE problem. There are solutions that don't involve altering how transactions are constructed.
1. Churn, the standard answer. Enough churn can bury your transactions behind too many hops for meaningful analysis.
2. In the future, I expect a continuously increasing diversity of services offered and service-providers available. EABE becomes less relevant the lower share of market participation E has. In the first place, E is an unusual kind of market participant who both _receives_ and _sends_ money to multitudes of people. If in the long run exchanges are still dominant drivers of transaction volume, that probably means cryptocurrencies have failed to create robust digital marketplaces, and in my opinion have failed as an experiment in engineered money.
3. Payment manager. To get around the problem of 10-block lock times, I imagine a payment manager who makes payments on your behalf whenever you want (e.g. like a credit card provider). The manager is funded by 2-of-3 escrow, where the user locks up some funds and then releases them to the manager periodically. The manager can also operate on pure credit. Relevance here? The manager's payments are largely disconnected from the money movement of its users. Moreover, the manager doesn't even need to know the identities of its users or the recipients of their payments (the users provide pre-built one-time addresses).

## knaccc | 2020-07-11T18:53:28+00:00
> I believe maintaining the status quo is the Schelling Point

I agree, this proposal is not compelling enough _yet_ for even me to endorse. Having said that, 'instant-on' will become much more compelling if daily transaction counts go 10x from here. It took me over an hour to sync 14 days of transactions, because I didn't leave the GUI running over that period. If in the future an occasional user will be forced to endure a 12+ hour wait before being able to send funds, then that's a cripplingly severe UX problem.

> Churn, the standard answer

The reason I'm disillusioned with churn is because it's so obvious on the blockchain when someone takes an output and then churns it over and over. The anonymity set doesn't actually really rise that much at all. The second reason for disillusionment is that no one is interested in making it routine or automatic for people to churn, because of the blockchain bloat implications.

> In the future, I expect a continuously increasing diversity of services

You could be right. But then history tends to paint a picture of winner takes all. Right now, the leading XMR/BTC exchange is Binance with 93k 24-hr XMR volume, and the runner up is Poloniex with only 6k 24-hr XMR volume. The leading XMR/USD exchange is Binance with 104k 24-hr XMR volume, and the runner up is ZBG with only 8k 24-hr XMR volume. 

> Payment manager... The manager's payments are largely disconnected from the money movement of its users

This is very interesting. If pushing the point on the severity of the iterated-EABE problem leads to other ways of solving it, I'm all for exploring those.


## knaccc | 2020-07-11T19:08:00+00:00
Note that iterated-EABE is a problem even in a world without large exchanges.

Consider the iterated-ABC problem, where A is an employer, B is an employee, and C is a charity that offends the political bias of A (i.e. blue-state employer and a pro-life charity, or a red-state employer and a pro-choice charity).

Iterated-ABC means that if the charity C ever has its wallet hacked by activists and its contents dumped on the internet, an employer can discover with high certainty if any of its employees have donated to the charity on more than one occasion.

## tevador | 2020-07-11T23:05:15+00:00
I can now see some merit to this proposal. A few observations about the revised protocol:

> there should not be these type of hashes on change outputs, in order to avoid linking outgoing transactions. Instead, the hash could be e.g. lower_32_bits(keccak(private view key || key image of spent output)).

This is a good idea, however it may lead to change output being identifiable in some cases, paradoxically by their hash being "too random". Even with 100 million outputs in the blockchain, a (pseudo)random 32-bit hash only has a <2.5% chance of having previously occured, while repeated payments to the same address have a 100% chance. After a few repeated payments to the same address, the change outputs can be identified with a high probability.

I guess this could be avoided by having a separate "change subaddress" for each payee address. This would also somewhat simplify scanning for outputs as change outputs would not have to be treated differently from received payments when restoring a wallet.

> Update: To avoid it being possible to know how many txs have been sent to donation addresses, a second 32-bit 'decoy' hash could be attached to each output. Now, the wallet owner will get false positives when searching for funds, but will achieve more privacy.

I'm assuming that the decoy hashes would be selected from the blockchain and not randomly generated (to avoid them being identifiable in the same way as change outputs by being "random").

However, this decreases the effect of the EABE mitigation because for many repeated payments to the same address, the chance that Bob selects Alice's output correctly every time among the decoys drops rapidly. The exchange can eventually deduce that Bob is in fact spending Alice's outputs as opposed to selecting them as decoy ring members by their hash.

## knaccc | 2020-07-11T23:16:43+00:00
> a separate "change subaddress" for each payee address

Makes sense to me. Or alternatively, the hash could be fewer than 32 bits to cause just enough collisions to solve the problem, but with few enough false positives so that the wallet does not need to check more incoming outputs than is reasonable.

> I'm assuming that the decoy hashes would be selected from the blockchain

That was the initial thought. As you say, the decoy hash does cause the problem that the 'bins' will be more dilute (in terms of only containing hashes for addresses from the same wallet). It's a half-baked idea, but perhaps it sparks a thought.

## knaccc | 2020-07-12T00:39:28+00:00
It doesn't matter if a view-only wallet (that has no key images) cannot know the hashes of change outputs in order to search for them. The view-only wallet only needs to know about other people sending funds to it, to be useful. In fact, it's more useful when view-wallets don't detect change and misleadingly inflate the balance.

If key images are known, it's easy to locate change outputs by watching out for key images instead of for subaddress hashes.

So it doesn't really matter (from a wallet incoming-output-detection perspective) what the hash on a change output is. ~~It could even be the same as the hash put on the output being sent to the other party (or in a multi-out transaction, the same as any one of the many outputs being spent).~~ You're right, the best thing is a separate "change subaddress" for each payee address.

## knaccc | 2020-07-12T04:06:42+00:00
@UkoeHB makes the excellent point that "Once some decoy partners have been selected, you are kind of stuck with them".

It makes sense that this is the way things need to be. This proposal essentially recognizes that transaction-level anonymity causes severe intersection-related traceability problems, and so the proposal moves us approximately from transaction-level anonymity to user-level anonymity. It would therefore make sense that a wallet that claims not to have made a set of transactions to only want to choose decoy identities that existed prior to that wallet having been created. You obviously can't claim that a new user used you as a decoy partner before that new user existed.

In other words: instead of creating an output and choosing 10 decoy outputs, now you're creating a pseudo-identity and choosing 10 decoy pseudo-identities.

And just like you'd perform one level of churn if you want more than 10 decoy outputs, under this proposal you'd perform one level of churn on all incoming funds if you want more than 10 decoy pseudo-identities.

To avert the problem of your decoy pseudo-identities not making as many transactions as you might over time, decoy outputs can be chosen not just directly from decoy-pseudo-identity-received outputs, but also from outputs downstream from that set of decoy-pseudo-identity-received outputs. This means that you can use more recent outputs on the blockchain for your own recent transactions, where those recent decoy outputs will look like they might come from change outputs owned by the decoy pseudo-identity (even if the decoy pseudo-identity has not actually been active recently or received new outputs recently).



## knaccc | 2020-07-26T04:54:39+00:00
Update on the latest state of the idea, thanks to everyone that helped brainstormed this in the Monero Research Lab channel:

**The wallet scanning-time problem quantified:**
If we assume 1000 variable-base scalarmults per second is a reasonable wallet computation requirement, and in a world with heavy subaddress use where there is a txpubkey per output, this means that a wallet will not be able to scan more than 1000 outputs per second. As of block #2150353, (19295614-18443188)/30=28414 outputs per day are being generated on the blockchain (calculated as the average over the last 30 days). This means that a wallet will take 28414/1000=28.4 seconds to scan each day of transactions. This means that if a wallet is created today, and transaction rates stay the same, restoring the wallet a year from now will take 28.4*365/3600=2.9 hours of wallet scanning time. If the transaction volume were to increase 30x from here, it would take **86 hours per year of transactions scanned**. This is motivation to consider "instant-on". (Note: two simplifications have been made in the calculation. The first simplification is that it assumes @UkoeHB's view-tags have already been implemented to reduce the cost of scanning . The second simplification is that there is one scalarmult per output. In reality, 2-out txs require only one scalarmult for those two outputs. The calculation is a useful approximation, however).

**A simple example of why decoy identities need to be considered**
Imagine that on 8 different occasions, you purchased XMR from an exchange and withdrew the funds to your wallet. Later, you spent 5 of those outputs in a single transaction. It will be obvious to the exchange that it was you that made the transaction, even though it seemed like you had an anonymity set size of 5*11=55. The chances of you including 5 outputs all owned by a different user in your anonymity set will be practically zero. However, if you'd chosen 10 decoy identities for the transaction, your user-level anonymity-set size will be preserved as 11 rather than reduced to 1.

**Updates to the proposal:**

1. Instead of providing a simple hash of the destination address as a tag on each output in a transaction, a destination public key Y is listed, where Y = Hs("destination_tag" || destination subaddress)*G. This destination public key Y allows any blockchain observer to notice when subsequent outputs are sent to the same destination address. Note that if an integrated address was specified as the destination, it should be first converted to a standard address prior to being used inside this hash.
2. A 48-byte Schnorr proof is also listed alongside each Y, proving that the private key is known for Y. This prevents just anyone from spamming the blockchain with additional transactions that also look like they were destined for Y, because they cannot do this without knowledge of the destination address that Y applied to. The Schnorr signature is the pair of scalars (c, r) where c = lower_128_bits_of_keccack(output key image || kG),  k is a random scalar that can be discarded afterward, r = k - cy, and the signature is verified as c == lower_128_bits_of_keccack(output key image || rG+cY). It is possible to produce an aggregate Schnorr signature (across all outputs in the transaction) so that the cost of adding these signatures is reduced to one Schnorr signature per transaction instead of per output.
3. Wallets whose seeds have a birthday encoded into the mnemonic can be used to allow the decoy-identity set to be deterministic. When a wallet is created, a set of decoy identities is created deterministically based on the wallet's private view key and birthday. The wallet will look at the 30 days of blocks existing prior to the wallet birthday (`30*24*30=21600` blocks prior), and assign an index (starting with zero) to each distinct Y value observed. A total of y_count distinct Y values will be found. Ten different values of Y_i (with i=0..9) will then be chosen by the function Y_index_i = Hs(i || private view key || wallet birthday) mod Y_count. Since collisions may occasionally occur, duplicates will be skipped until 10 distinct Y indices are found. Now we have 10 Y values that will form the deterministic decoy-identity set for the wallet.
4. When a transaction is made, first the wallet will decide which of its own outputs will be spent. Obviously, the outputs available to spend will either be outputs that have been directly received from others, or outputs that are change outputs resulting from the wallet's prior transactions.
5. The wallet will examine the blockchain to find all outputs tagged with any of the 10 Y_i public keys. We will also find all outputs that, according to the blockchain, may be downstream from those outputs (i.e. they may not explicitly have the Y_i public key assigned to them, but they could plausibly also be owned by Y_i because they could be from a chain of change outputs from Y_i outputs being spent). When making a transaction, for each input ring, each of the decoy outputs is chosen such that they come from each of those 10 decoy-identity output sets. Decoy outputs will be chosen such that they are from roughly the same timeframe as the real outputs being spent. 

# Action History
- Created by: knaccc | 2020-07-09T16:20:02+00:00
