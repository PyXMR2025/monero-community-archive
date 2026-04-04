---
title: Radical idea for forward secrecy and instant wallet sync
source_url: https://github.com/monero-project/research-lab/issues/106
author: tevador
assignees: []
labels: []
created_at: '2022-09-08T05:52:18+00:00'
updated_at: '2024-06-01T04:15:43+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Since [Jamtis has been modified](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024#gistcomment-4293118) to allow Seraphis membership proofs to have perfect forward secrecy, the Diffie-Hellman key exchange will become the weakest point of Monero with respect to forward (or post-quantum) privacy. There are probably adversaries scraping Monero addresses off the internet right now to use them in the future when the ECDLP is broken and view keys can be extracted.

There are 2 ways to fix this:

1. Use a post-quantum KEM.
2. Get rid of the key exchange.

The first option is not viable because existing lattice-based KEMs have public key + ciphertext sizes of several kilobytes and the hardness of lattices is uncertain.

The second option is possible if we radically modify the protocol so that **every user constructs their own outputs**. Then there is no need for a key-exchange exposed on the blockchain and we can use a 100x faster symmetric key derivation.

In the current Monero protocol, the sender gets an address and constructs the whole transaction, including the output for the recipient using a Diffie-Hellman shared secret to derive a one-time key and the blinding factor. The transaction input signatures reference all outputs and there is one aggregated range proof for all outputs. The recipient then scans the whole blockchain to find their outputs. This basically works like a wire transfer. You get the recipient's bank account number, you call your bank and ask the amount to be transferred to the recipient's account.

Instead of putting all responsibility on the sender, we could make sending a transaction work more like writing a check. A check is signed note that promises to pay the recipient a certain amount. The recipient can then go to the bank and cash the check.

In crypto-terms, it would work like this:

1. The recpient's address would consist of a single public key `K_r` ("receive key").
1. To send an amount `v`, the sender derives a one-time key `K_r' = K_r + H(K_r || n || v) G`, where `n` is a nonce.
1. The sender takes one or more of their e-notes and constructs a Seraphis composition proof signing `K_r'`. Transaction outputs are not signed.
1. If there is change to be received, the sender constructs a change output using a secret blinding factor.
1. The sender sends this half-transaction to the recipient out-of-band together with the amount `v`, the nonce `n` and the difference between the input blinding factors and the change blinding factor.
1. The recipient can complete the transaction by appending one or more outputs so that the whole transaction balances out. The recipient can then construct membership proofs for all inputs and then signs the transaction with the key `K_r'`.
1. The recipient can submit the transction to the network.

The sender can prove a payment by providing `K_r`, `n` and `v`.

#### Advantages

* Smaller public addresses (just 1 pubkey instead of 2-3).
* Bypasses the 10 block lock time. Membership proofs are constructed by the recipient, who can wait 10 blocks to finalize the transaction. Unconfirmed transactions can be chained easily.
* No publicly observable Diffie-Hellman key exchange. The transction secrets would be constructed using symmetric keys. Wallets would always know their owned outputs since they constructed them. No need for scanning except when restoring from the seed, which would be 100x faster due to the symmetric algorithms being used instead of slow ECDH.

#### Disadvantages

* The recipient learns the e-notes that are being spent. This can be mitigated by a churn transaction to separate the sent e-note from its source.
* Each output needs a separate range proof, which is less efficient.
* The sender needs a private communication channel with the recipient to pass the partial transaction.


# Discussion History
## boogerlad | 2022-09-09T08:34:10+00:00
Would this work for transactions with multiple recipients?

## tevador | 2022-09-09T19:24:40+00:00
Sending to N recipients requires N+1 transactions with this system.

First you create N outputs with the correct amounts for each recipient and a change output. Then you send one half-transaction to each recipient.

While this would increase the network load with additional tranactions, it mitigates the first two disadvantages (source of funds is hidden from the recipients and the recipients can make just 1 range proof because there is no change output from the sender).

## kayabaNerve | 2022-09-11T01:09:25+00:00
While I never want to suggest research shouldn't be accumulated, I don't think this has a path forward. Beyond the privacy implications on requiring buffer transactions, this is immediately comparable to Grin which failed horribly due to requiring IP-based addresses. Any attempt at this proposal would have to be as a non-distinguishable alternative to the current scheme, and it doesn't sound like this is (due to needing multiple range proofs). I do love the work against preventing DL-knowledgable parties from breaking privacy, which I see as the second biggest issue with privacy right now.

## tevador | 2022-09-11T09:59:31+00:00
> this is immediately comparable to Grin which failed horribly due to requiring IP-based addresses

Grin/Mimblewimble requires a roundtrip to complete a transaction, i.e. sender -> recipient -> sender. This scheme only needs the sender -> recipient part, which makes it "fire and forget". You can use any asynchronous channel to pass the transaction to the recipient, e.g. e-mail.

> non-distinguishable alternative to the current scheme, and it doesn't sound like this is (due to needing multiple range proofs)

Of course, if this was ever implemented, all transactions would need to look the same (2x range proofs or requiring the intermediate transaction).

## kayabaNerve | 2022-09-11T10:04:09+00:00
While there is a distinction regarding it not being round trip, I still don't believe that requirement can be successfully added to every transaction. When it comes to making every transaction having more range proofs... it's a massive slow down to support an alternate mode which has its own trade offs regarding privacy (while accomplishing privacy greatly desired and not currently offered...).

## boogerlad | 2022-09-11T12:19:14+00:00
Other than anonymous donations, what scenarios are there such that the sender doesn't notify the recipient via a communication side channel when they want to send Monero?

This honestly sounds like a great idea to me, and it solves the ux problem of proving you paid for something. Right now, you have to send an outproof, but if the recipient simply received a message from you via a verified communication channel that you use often, they automatically know it's you.

## kayabaNerve | 2022-09-11T12:54:28+00:00
For a more practical commentary going over the actual issues in depth:

1) This is horrible for multisig. It makes every recipience a signature which greatly increases load.
2) It removes the ability to be offline and receive funds. The sender can clawback funds until they're received. This means even if someone shows you they sent you funds, that's not guaranteed unless you accept them with your private key.
3) It dramatically reduces performance thanks to the multiple Bulletproofs. While there a multi-round MPC Bulletproofs protocol exists, sarang has commented they don't believe Bulletproofs+ could have MPC.
4) Adoption of this must remain indistinguishable. Even if its solely an alternative, we lose out on performance per the previous point.

And then as a side note, I don't see how sending an incomplete transaction is better than an out proof to prove sending. They should be equivalent for that immediate goal. Incomplete transactions have a load of other complications however. For the only example I know of, as out proofs are already rarely used, the proposal is for a shop frontend to process a payment without the wallet's view key (which covers all addresses, not just the relevant ones, though there's of course commentary on derived view keys...). If you're in this niche use case, this proposal doesn't work for you. One of three cases occurs.

1) The store would now have to be trusted to receive funds, as in, it could steal XMR from you.
2) You're trusting the sender not to double spend.
3) You're forced to run a server with 24/7 uptime to receive funds.

All of these options are major decreases in UX.

The benefit in this is the privacy benefit which is immense. It could arguably be worth using distinct output range proofs. The detriments are as I stated, which may mean almost no adoptance. Accordingly, local wallet churning (which won't publish an address which could be broken under the DLP) may be the simplest solution to accomplish very similar results.

## tevador | 2022-09-11T14:57:38+00:00
> This is horrible for multisig. It makes every recipience a signature which greatly increases load.

Fair point. This scheme shifts the trust requirement from address generation to payment acceptance, which may have security implications.

> It removes the ability to be offline and receive funds. 

No, it doesn't. You can receive offline, but you will only find out about the payment when you come online (and read your mailbox). I don't think there is any practical difference from the current situation. Do you consider a payment "received" if you don't know about it? Schrödinger would say no.

>The sender can clawback funds until they're received.

Irrelevant. The recipient will consider the payment to be complete when the receiving transaction has enough confirmations.

> It dramatically reduces performance thanks to the multiple Bulletproofs.

I would not be so confident to use the word "dramatically" without seeing some benchmarks. 

> The store would now have to be trusted to receive funds, as in, it could steal XMR from you.

I don't think this is much different from a store that generates subaddresses. It also has to be trusted to use the correct public spend key when generating addresses.

> You're trusting the sender not to double spend.

No, as explained above. Double-spends are not considered valid payments and the recipient can easily verify if a payment has been double-spent or not. The only disadvantage is that you cannot accept zero-confirmation payments, but those already involve some level of trust with the current setup.

> You're forced to run a server with 24/7 uptime to receive funds.

Not a practical disadvantage for any online commerce application. Doesn't matter for donations, which can be easily received by e-mail. E.g. my donation address would be

```
tevador+xmr1qkv5dy8fz2sh9g99knxyrfra98ph5ep8dlxtlaf7l6gxhcldmvmv@example.com
```

The sender can decode my public key by parsing the characters between `+` and `@` and then send the payment to this e-mail address (encrypted with the public key), using a disposable mailbox.

> local wallet churning (which won't publish an address which could be broken under the DLP) may be the simplest solution to accomplish very similar results

This will accomplish nothing. A future DLP-breaking adversary will still learn all payments (including amounts) recieved to any public address regardless of any subsequent churning.

## kayabaNerve | 2022-09-11T18:29:43+00:00
> No, it doesn't. You can receive offline, but you will only find out about the payment when you come online (and read your mailbox). I don't think there is any practical difference from the current situation. Do you consider a payment "received" if you don't know about it? Schrödinger would say no.

There's a difference between being online with your key, able to complete the transaction, and able to verify a payment happened.

> I don't think this is much different from a store that generates subaddresses. It also has to be trusted to use the correct public spend key when generating addresses.

Fair. I'll retract this and apologize for not thinking it through.

> I don't think this is much different from a store that generates subaddresses. It also has to be trusted to use the correct public spend key when generating addresses.

There are models where payments are processed before the wallet key, or some middleware with some wallet key, comes online. Forcing them to be online makes this a synchronous protocol, and while not round trip as there's no response, may dramatically effect the UX. When you define it as synchronous, you're correct there's no double spends. I'm not advocating for a shift to a synchronous model however.

> This will accomplish nothing. A future DLP-breaking adversary will still learn all payments (including amounts) recieved to any public address regardless of any subsequent churning.

The address churned to wouldn't be public as it'd be local. Privacy conscious users, adding an extra step locally without affecting the protocol, would achieve full plausible deniability. While it is a manual buffer TX, your own proposed scheme requires a buffer TX for privacy. Accordingly, while I think your proposal has merits in a variety of ways, I do think the simpler approach is a much more well-rounded suggestion.

And re: performance, while I have yet to run benchmarks, the multiexp should help dramatically here. The biggest issue would likely be the size, though the performance decrease wouldn't be ignorable. We can always say it's sufficiently low to be acceptable for sufficient gain however.

## tevador | 2022-09-11T19:14:51+00:00
> There's a difference between being online with your key, able to complete the transaction, and able to verify a payment happened.

That difference is meaningless in practice. People use their view keys to detect incoming payments. The "receiving key" in this proposal is like a view key.

> The address churned to wouldn't be public as it'd be local. Privacy conscious users, adding an extra step locally without affecting the protocol, would achieve full plausible deniability.

I fail to see how the churn protects you. It doesn't remove the original receiving transaction from the blockchain.

For example, if it's a donation address, the money flow would be `donors -> donation address -> churn addresses`. A DLP-breaking adversary can still locate and decrypt all of the `donor -> donation address` transactions including the amount that was received. There is no plausible deniability.

## kayabaNerve | 2022-09-12T16:15:23+00:00
It doesn't remove the original receiving transaction, but it puts up distance and severs the link. While you're right, for posted public addresses, it can be linked without issue, it prevents a person with 3 stores from having those 3 stores linked to them. But yes, this idea is much more comprehensive at privacy.

Also, there is a slight distinction with receiving keys and addresses. If you're a repeat user who reuses an address, the server can't alter an already sent address to hijack future payments.With a receiving key, the server can decide to take the incoming stream whenever. A lot of these distinctions become frivolous edge cases though (such as mine, as your privacy commentary is correct and important).

## jeffro256 | 2024-01-25T03:48:09+00:00
> Each output needs a separate range proof, which is less efficient

Wouldn't the sender be able to construct one range proof for all outputs at the time of sending assuming that the receiver agrees to the amount commitments that the sender provides (ostensibly alongside or inside the partial tx)? This would reduce flexibility for the receiver if they wanted to say, split their output into 5, but we wouldn't have to require separate range proofs. 

## jeffro256 | 2024-06-01T04:15:41+00:00
If we assume a two-way channel (e.g. most online merchants and physical PoS machines), we can make a F-S instant sync payment protocol that A) doesn't tell the receiver which enotes are spent, B) has bulletproofs aggregated like normal, C) can have multiple recipients in the same transaction, and C) allows recipients to perform regular Jamtis balance recovery in the case of lost channel info and/or wallet caches. Here's how it would work:

1. Receiver sends `amount`
2. Sender does input selection for given `amount` and sends `input_context` (this is a hash of the key image set for non-coinbase txs)
3. Receiver generates <code>D<sub>e</sub></code>, constructs a self-send enote for given `input_context`, and then sends all enote information and blinding factor <code>(K<sub>o</sub>, C, a<sub>enc</sub>, addr_tag<sub>enc</sub>, view_tag, D<sub>e</sub>, k<sub>a</sub>)</code>
4. Sender checks that <code>C ?= amount H + k<sub>a</sub> G</code> and includes all that enote information in transaction. They then complete and braodcast the transaction as normal by adding a change enote, signing, and generating proofs (notice that bulletproofs can be aggregated like normal w/ no privacy loss since the sender is constructing the proofs and already knows the send amount)
5.  Receiver can either A) do normal Jamtis balance recovery or B) do instant sync using cached enote information from earlier to process the incoming transaction

One thing that is a bit tricky about this scheme is that the receiver can't do a normal payment proof since the receiver constructs a self-send enote. However, since we are doing a two-way channel, we can have the receiver actively sign the message <code>(amount, input_context, K<sub>o</sub>, C, a<sub>enc</sub>, addr_tag<sub>enc</sub>, view_tag, D<sub>e</sub>, k<sub>a</sub>)</code> and then that can be used as the payment proof later (assuming that that information matches what is on-chain).

This doesn't work well for payment to miners since `input_context` depends on the block height, so the back-and-forth would have to be redone every time the chain state changes.

This exposes the view-balance secret to the service running the recipient's invoice service. This might not be ideal, so a small tweak to Jamtis's internal send protocol can be used where the "generate-image" scalar private key is not derived from (and otherwise independent from) the symmetric secrets (<code>X<sub>1</sub></code>, <code>X<sub>2</sub></code>, <code>X<sub>3</sub></code>) used to derive the incoming enote information, instead of them both being <code>s<sub>vb</sub></code>.

# Action History
- Created by: tevador | 2022-09-08T05:52:18+00:00
