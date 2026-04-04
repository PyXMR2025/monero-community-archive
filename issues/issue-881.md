---
title: 'Feature request: Transaction that require the signature of both the sender
  and recipient.'
source_url: https://github.com/monero-project/monero/issues/881
author: destenson
assignees: []
labels:
- enhancement
- proposal
created_at: '2016-06-26T04:43:42+00:00'
updated_at: '2018-07-23T04:08:06+00:00'
type: issue
status: closed
closed_at: '2018-07-23T04:08:06+00:00'
---

# Original Description
EDIT: Please see [this comment](https://github.com/monero-project/monero/issues/881#issuecomment-351917989) for a clearer explanation of the requested feature I've called "multi-sig transactions", for lack of a better term.

I would like to propose that Monero add the concept of multi-signature transactions (in addition to multisig wallets). A multi-signature transaction would be a transaction that requires the valid signature of all parties involved before it is actually committed to the blockchain as a valid transaction. A requester or recipient could be any valid address, not just multi-signature wallets. The transaction can be initiated by either the payer or the payee.

Requests for payment can be initiated by party A with a valid signature (or all required signatures if initiated by a multisig wallet) & when party B also signs the request, the actual transfer of funds from B to A will occur like a normal transaction. This will add invoicing as an intrinsic feature to Monero.

Outgoing payments to a third-party can also be multisig. In that case, the request is for acceptance of payment, and the transfer is completed when the recipient signs the transaction. Since the transfer is not valid until all parties sign, this allows the funds for the transaction not to be committed until the recipient accepts the payment. If funds are not available when the transaction is adequately signed, it will be rejected by the blockchain due to insufficient funds. A signatory can also rescind their signature before the transaction is accepted by all parties. This allows a fund transfer to be cancelled before payment is accepted. This is a feature that is missing from all major cryptocurrencies.


# Discussion History
## fluffypony | 2016-06-26T11:00:19+00:00
MRL work currently being done here: https://shnoe.wordpress.com/2016/03/22/ring-multisignature/


## ChristopherKing42 | 2016-08-09T02:03:40+00:00
Its already possible: http://monero.stackexchange.com/q/782/255


## luigi1111 | 2016-08-10T14:35:14+00:00
This is known. No one has wanted to take up implementation with RingCT coming "soon" and making it incompatible.

Getting the communication to be non-clunky will be a work of art in itself I think.


## Riiume | 2017-09-14T11:22:07+00:00
Dear developers, I have posted a $480 bounty for completion of this issue: https://www.bountysource.com/issues/35498752-feature-request-multi-sig-transactions

Best of luck!

## lessless | 2017-10-12T04:03:45+00:00
This is an **OUTSTANDING** feature! It will allow to create recurring payments: business can initiate transfers at the beginning of the each billing cycle and customer just sign them off in the wallet. 

What a brilliant idea! 

## Tails | 2017-11-01T10:56:43+00:00
The communications across the web are a bit ambiguous. Is multi-sig already possible now or not? Is it being worked on? When is it expected?

For example, it seems it was possible in 2016 based on this answer: https://monero.stackexchange.com/a/783

However, in the roadmap it is still listed to be done in 2017: https://getmonero.org/resources/roadmap/

And here it seems the feature is being reviewed and tested, waiting for integration: https://github.com/monero-project/monero/pull/2134

## destenson | 2017-11-01T12:10:17+00:00
@Tails, I'm sure the devs will have more to say, but it certainly appears to have been worked on recently. From the links you posted, it looks like many features are already implemented, but it's probably not considered complete yet.

However, @lessless's comment shows he understands that this particular issue that I posted originally is not about standard "multi-sig" as you normally think of when you think of multi-sig wallets, etc. This particular issue is about possibly generating a temporary ring between sender and receiver that would allow individual transactions to be completed when the recipient signs the transaction.

@luigi1111 or @fluffypony, or anyone who knows, does a recipient's address contain enough information to generate a 2-party ring-signed transaction that would allow/require both sender and receiver to sign before the transaction is complete? If private keys for both parties are necessary to create the ring-signature, that would prohibit the use-case(s) I was thinking of when creating this issue. But if the address contains a public key, and if only public keys are necessary to create the ring signature(s), then it definitely seems like it would be a viable way to implement this feature.

## moneromooo-monero | 2017-11-02T12:54:24+00:00
That stack exchange link essentially says "yes, it's possible, if you write the code". It does not say "yes, and the code is written". #2134 is the code for doing so, and is close to being fixed up to work with subaddresses.

## moneromooo-monero | 2017-11-02T12:57:55+00:00
I'm not sure I understand your question destenson, but:

- a recipient's address contains both the public spend key and public view key.
- to create a ring signature, you need a private spend key for one of the ring members (and multisig does that in reconstructing the results of using that private key).

So I think you will have to rephrase your question with specific details.


## destenson | 2017-11-02T14:02:27+00:00
@moneromooo-monero, thank you. That does answer my question. It would mean that this implementation of "multisig" as you refer to it, does not provide the features required to enable the kind of multi-sig _transaction_ [this issue requests](https://github.com/monero-project/monero/issues/881).

## moneromooo-monero | 2017-11-04T10:47:30+00:00
Then I suggest you explain it clearly, as the first post is very vague, due to being explained in flowing English. For instance, "Requests for payment can be initiated by party A with a valid signature" needs the following information: what is a request (from the point of view of the network), what is the initiation step (and what other steps are there, equally well defined), what information does the signature sign (if it is just "the request" then the request needs to be well defined), and it would be helpful to have an basic overview of whether monero is meant to flow from A to B, or B to A, or both.

## destenson | 2017-12-15T05:34:08+00:00
@moneromooo-monero, thank you. You are absolutely right. I agree and apologize. It was difficult to explain initially and I did not explain it very effectively. Let me try this again...

The idea is to have a sender, _Sam_, send a payment to a recipient, _Rita_, that either _Sam_ or _Rita_ can initiate or cancel (for little-to-no cost) and that must be signed with both _Sam's_ and _Rita's_ private keys before it can be mined.

I may have jumped ahead prematurely by suggesting a (_non- Monero-specific_) possible implementation using multi-sig technologies and then calling them "multi-sig _transactions_" in this thread. When I refer to a "multi-sig transaction", I mean a type of transaction that:
- may be created by _either_ Sam _or_ Rita, and
- transfers funds from _Sam's address_ to _Rita's address_, and
- must be signed by both _Sam_ and _Rita_ before it is considered complete, valid, and ready to mine, and
- might be implemented using ring signatures, if the ring signature parameters can be specified using only the public keys or addresses of each party. This type of ring signature would still require signers to sign with their private keys, but could create the ring easily from a pair of public addresses. (I have learned since the original post, that this feature may not be generally possible using ring signatures.)

This type of transaction would be similar to a traditional multi-sig account, but rather than requiring signatures of a certain number of pre-authorized accounts for the transaction to be complete and valid, it would instead require the signatures of both the sender and the recipient.

In the following examples, _Sam_ may represent a single individual address or a regular multi-sig wallet account/address. In the case of a multi-sig wallet, all necessary signing requirements for making transactions would remain intact. If _2-of-3 signatures_ is required to make payments from that address, then all _2-of-3 signatures_ would be required to be a valid signature as _Sam_ to initiate or approve an outgoing payment. When _Rita_ is a multi-sig address, it might make more sense to allow a single one of the authorized signers to acknowledge receipt instead of requiring all (e.g. _2-of-3 signatures_) to sign. But I think that should be user configurable, as some multi-sig owners may want it to be easier to receive payments and others may want it to be harder to receive unwanted payments.

This type of transaction,  a "_multi-sig transaction_" as I called it, could be created by either party:
1. _Sam_ makes a payment to _Rita_ by:
    * creating a transaction with payment details for _Rita_ and signing it.
    * then the incomplete, _half-signed_ transaction is provided to _Rita's client_ (specifically or broadcast to the network if clients are unreachable).
    * when _Rita_, or her automated client, notices the _half-signed_ transaction waiting for her to approve, acknowledge, sign and complete, she can:
      * sign the transaction and broadcast it to the network to be mined, completing the transaction and effectively providing _Sam_ the additional acknowledgement of payment acceptance as requested.
      * or cancel it, by requesting that the network remove the incomplete transaction from its list of incomplete, _half-signed_ transactions, effectively providing _Sam_ with the acknowledgement requested of _Rita_ as well as acknowledgement that _Rita_ disapproved the payment details supplied by _Sam's_ transaction.
2. Or _Rita_ creates an invoice requesting payment from _Sam_ by:
    * creating a transaction with payment details for _Sam_ and signing it.
    * then the incomplete, _half-signed_ transaction is provided to _Sam's client_ individually or broadcast to the network if clients are unreachable.
    * when _Sam_, or his automated bill-payment software ;), notices the _half-signed_ transaction awaiting his signature, he can:
      * sign the transaction and broadcast it to the network for mining, completing the transaction and providing _Rita_ with the acknowledgement, approval and transmission of payment she effectively requested.
      * or cancel it, by requesting that the network remove the incomplete transaction from its list of incomplete, _half-signed_ transactions, effectively providing _Rita_ acknowledgement from _Sam_ that he received the payment's details and disapproved of the payment.

By offering a half-signed transaction for _Rita_ to sign, _Sam_ is effectively requesting _Rita's_ acknowledgment and approval of the payment details as provided by _Sam's_ _half-signed_ transaction. And by offering a half-signed transaction for _Sam_ to sign, _Rita_ is effectively requesting _Sam's_ acknowledgement of the payment request, and his approval of the payment's details as provided by _Rita's_ _half-signed_ transaction.. Therefore, a _fully-signed_ transaction (signed by both _Sam_ and _Rita_) effectively provides both:
  * authorization (by _Sam_) to make the intended payment from his address, and
  * acknowledgement (by _Rita_) that approval was granted to receive the payment with her address.

Some benefits of having a type of "multi-sig transaction" like this available:
- Mistakes and accidents can be corrected before they cause the loss of funds. This would depend on the recipient address not auto-approving deposits. That would almost always be the case for mistyped/miscopied addresses that had never been used previously.
- _Sam_ can change his mind and cancel the transaction any time before _Rita_ signs it in order to prevent it from being mined.
- _Rita_ can send a _half-signed_ transaction effectively as an invoice. _Sam_ would only need to sign the transaction (and have it be mined) to complete the requested payment.
- _Rita_ can refuse to accept unexpected deposits by cancelling them. A broker, exchange or other service could refuse to accept any deposits that did not come from their list of known clients.
- _Sam_ can be more "creative" with budgeting and have more freedom to use funds in alternative ways if _Rita_ does not promptly acknowledge and accept _Sam's_ payment.
- Either party could cancel a transaction and replace it with a transaction having different payment details.

And some issues with having a transaction type like this available:
- Assuming the mempool would retain incomplete, _half-signed_ transactions awaiting approval, the network could become saturated with these non-mineable transactions. One solution could be to send _half-signed_ transactions directly to the other party instead of broadcasting them, using, for example:
  - a specially formatted URL that includes everything required to recreate the half-signed transaction, or
  - a _half-signed_ transaction _file_ that could be attached to email and opened by a compatible client, or
  - a messaging system, such as [Bitmessage](https://bitmessage.org/) (just an example, not an endorsement), that transmits the _half-signed_ transaction as a direct message to the other party.
- Network fees may change between the first and last signatures. Probably trivial to solve.
- There should be a reasonable expiration period for these types of transactions to prevent stale and unusable half-signed transactions from staying in the mempool for too long.
- To cancel a transaction, a party might need to sign a proof of cancellation. This could get problematic unless the cancellation proof replaces the existing half-signed transaction instead of allowing stale transactions to exist on the network in variously signed states. If signed proof is required, how long would that proof of cancellation be retained in the mempool? I think it really should just cause the removal of the _half-signed_ transaction from the network instead of adding another signed proof to the mempool. Removal of a _half-signed_ transaction from the network probably should be only be caused by expiration of the transaction or by cancellation of the transaction by one of the required signatories, either _Rita_ or _Sam_.
- Finally, transactions specifying UTXO as inputs may be difficult to reliably initiate by _Rita_, unless those inputs could be specified in a way that the transaction need not be re-signed when inputs change.
  - This could prevent a transaction of this type from working well on certain blockchains (such as Bitcoin and Monero 😦) that depend upon specifying unspent outputs to used as inputs for the transaction.
  - It might be more of an edge case that is really only a problem for addresses that send payments frequently, but I still think it's an issue to be solved before this idea is viable.
  - Depending on internal design, it might be possible to use sane defaults instead of specifying precised inputs, but that will introduce more edge cases when the defaults cannot be picked or used sanely or cheaply.
- There are probably many other things I haven't thought of as well. I encourage your feedback.

Hopefully you and others will find this explanation more digestible. Thank you for your suggestion. I look forward to more, since I am *not* an expert at Monero.


## moneromooo-monero | 2017-12-15T15:39:26+00:00
That was a lot more understandable, thanks.
First thing that comes to mind is that you'll be either spamming the chain with "cancel" notes, or allowing the cancelling pary to later replay a previously cancelled tx. Using the txpool like this is an attempt to bypass mining, and thus is not decided by consensus.

That said, the idea behind it is possible, by having both parties spend one of their inputs in that tx. Then cancellation becomes merely "not signing the tx" (that is, a passive absence of step rather than an active step). It seems similar to vespco's idea about dominant assurance contracts (search for those exact words).


## destenson | 2017-12-16T21:09:51+00:00
I did consider the additional load on the txpool might be excessive. With ethereum or bitcoin, that could be prevented by sharing the transaction with the other party directly, and submitted to the network only after being fully signed. Does Monero also provide that possibility?  If so, a half-signed transaction could be given to the other party "by hand" using a file, network message, or any other method of preventing the transaction from entering the txpool before it's been fully signed. And then, as you suggested, a cancelled transaction would simply be one that is not signed by all parties.

Also, is it true that Monero doesn't offer any method of communication between individual clients or addresses (besides submitting transactions to the txpool)? If so, and if this feature is added to Monero, you should consider adding a messaging feature as well. It might even be good to add messaging regardless, since it would permit additional use-cases that may have never been considered before. And if direct messaging were availabe, it would help to protect the txpool from such spam.

Can you help me understand what you mean by cancelling party replaying a cancelled tx? Do you mean that the a cancelling party could cancel a transaction, then later sign and submit it maliciously after the other party had concluded it was cancelled? Thanks.

## lessless | 2017-12-17T03:31:51+00:00
@moneromooo-monero as far as I understood from reading https://www.reddit.com/r/Monero/comments/6htvg3/monero_is_perfect_for_dominant_assurance/
DAC  will require a seller to attach extra funds to initiate a payment.
The first application of proposed feature, in my mind, is empowering  SaaS business model. So far it's not possible to use any other crypto in the SaaS model unless there is a 3rd party like Coinbase that will sign off periodical payments on the customer behalf. 

Using DAC in such condition doesn't seem reasonable (and it will be almost impossible to justify to any management) - business potentially can lose money with any of its customers when it wants to bill them. Quite opposite outcome.
One way around that is to increase a fee when accepting Monero and hedge the risk by including that extra in the monthly payments. Which will make the same service cost in fiat less, than it will cost in Monero. 

Off-chain sharing sounds like a nice option here. Maybe LN will help somehow? 

  

## dEBRUYNE-1 | 2018-01-08T12:35:39+00:00
+proposal

## destenson | 2018-01-24T18:55:13+00:00
I don't know how easily it can be implemented in Monero, but the Simple Schnorr Multisignatures recently described by [Blockstream](https://blockstream.com/2018/01/23/musig-key-aggregation-schnorr-signatures.html) in [this paper](https://eprint.iacr.org/2018/068.pdf), sound like exactly the kind of algorithm that would make this proposal feasible as described.

## moneromooo-monero | 2018-01-28T23:32:28+00:00
Above, cancelling a transaction is just not signing it. No active step. Not like a revocation you check, just the absence of an action. Therefore, the party can sign/relay it later, if wanted. The case I had in mind is:

Alice and Bob have a 2/2 multiisig wallet.
Alice creates a new tx, and passes it to Bob for signing
Bob does not sign it (Bob could claim he never received it too)
Stuff happens
Bob actually signs/relays it days later, surprising Alice

Here, "Stuff happens" could be "Alice makes another tx, and Bob signs it normally". If that tx doesn't invalidate the earlier one (through double spending), then Alice/Bob spent twice.

## destenson | 2018-07-23T04:08:06+00:00
I understand that is how it works now.

The suggestion would require allowing cancelling or revoking a transaction as an action.

As this topic is going nowhere. I'm ok if it's closed.

# Action History
- Created by: destenson | 2016-06-26T04:43:42+00:00
- Closed at: 2018-07-23T04:08:06+00:00
