---
title: 'Feature request: add aditional 0-output in case of one output (when using
  RingCT)'
source_url: https://github.com/monero-project/monero/issues/1375
author: dnaleor
assignees: []
labels: []
created_at: '2016-11-25T00:01:50+00:00'
updated_at: '2017-04-20T13:49:59+00:00'
type: issue
status: closed
closed_at: '2016-12-15T16:00:24+00:00'
---

# Original Description
It is possible to add 0 XMR outputs using RIngCT.

I think in case someone builds a transaction that would only contain a single output, it would be beneficial for privacy to also add a 0 XMR output. This would make this transaction indistinguishable from any other transaction.

If certain transactions only have one output, this lowers the privacy significantly, as an observer will be able to know that all inputs (although using ring sig) are consolidated into one new output. When using the 0-output, it just looks like a regular "payment and change" transaction 

edit: this 0-output could be sent to a random generated address, or could be sent to the sender as "change". Avoid using an address that is already used by someone else, as this will be confusing when he refreshes his balance. 

# Discussion History
## moneromooo-monero | 2016-11-25T09:13:27+00:00
This adds pointless spam to the blockchain. However, if you want this, there's a patch which does this in my ringct history, which I subsequently took out, it was in src/wallet/wallet2.cpp and just a few lines IIRC, so should be easy to restore locally.


## ghost | 2016-11-25T09:55:01+00:00
Is it possible for someone to construct a transaction with a single output after ringct activates?

## moneromooo-monero | 2016-11-25T13:37:54+00:00
Yes.

## dnaleor | 2016-11-25T14:16:38+00:00
it does indeed add some "spam" to the blockchain, but on the other hand, it improves privacy, makes (almost) all transactions look the same. The more uniformity the better. Ring sigantures also add "spam" to the blockchain because we don't know if transactions are spent or unspent. Imho it's a trade-off. 

I will look into your code. 

## ghost | 2016-11-25T21:28:37+00:00
Is there any way to 'quantify' the relative loss of privacy? 

Maybe it would be better to inform the user their transaction is going to result in a single output which may compromise their security, and present them with the option of splitting it instead. 

## kewde | 2016-11-26T00:29:58+00:00
The only case where privacy loss may occur is in very odd situations. Adding a 0 output is not worth the trade-off.

This would however be prevent situations where a user or service systematically spends the whole output without any change over and over again establishing a pattern of one-output transactions only. 

Another one of them could be due to the fact that change addresses generally contain a lower amount of XMR (compared to the intended outgoing output) which would also results into it being more likely being spent along with multiple other inputs to achieve the necessary amount. If you would mix with one-output-transactions ONLY (which is highly unlikely but nonetheless a possible scenario) then it is more likely that the outputs stemming from transactions with multiple outputs are the ones being spent because the spender has scrapped all his change together. However, that is very very far fetched.


## dnaleor | 2016-11-26T09:33:45+00:00
> This would however be prevent situations where a user or service systematically spends the whole output without any change over and over again establishing a pattern of one-output transactions only.

I don't want to sound paranoid, but this can lead to anonimity (and maybe even mild fungibility) issues. I'm a fan of making all transactions as uniform as possible. Maybe enforcing the 0-output (that is, implementing a consensus rule that the minimum number of outputs in a transactions should always be 2 or more) is for some a bridge too far, but making it the default should be considered, imho.

## moneromooo-monero | 2016-11-26T10:44:22+00:00
I'll do that when Shen or Surae or other has a good study showing the details of what this entails :)

But FYI, I have a branch somewhere with a system that will send every input of a transaction separately, with random delay between the transactions [1]. This system is meant to avoid any temporal associations between inputs (because there's only one, ever). This system would cause a LOT of transactions with a single input *and* a single output, and these are even better than the 2x2.

There is a possibility that having just one output means you can have a special rct proof that's smaller than what you'd otherwise be, though this may involve more complex changes, so it's something I want to keep available for the future.

[1] random order, so you can't tell when it starts/stops since the theoretical last tx with an extra change output can be anywhere.

## dnaleor | 2016-11-26T14:26:07+00:00
I like the idea of only spending one input in a transaction at a time, but this is probably not possible for payments to businesses. It's a cool idea though, makes it indeed a lot more private, but adoption of this will be hard:

*Businesses want to see at least an unconfirmed transaction, if they only see a partial unconfirmed transaction, they can't even be sure that in the next x minutes the other parts will be send. This is a weak argument as I don't believe in using crypto for transactions in retail stores. It does however complicates how businesses integrate with monero online as well. 
*It's a mess when something goes wrong in the middle of broadcasting the stream of payments. Again, nothing that can't be solved, but needs additional tools and code for payment processors
*What about payment ID's ? When sending a payment that has a paymentID attached, will this paymentID be attached to all partial transactions? Or can we think about a scheme that changes the PaymentID with every partial transaction but still somehow links them together (and only the sender and receiver can do this) ? 

Also, as you already said yourself, you will have at least one transaction with a change output in this "stream payment". 
So I do expect that, even if the "payment stream" system gets implemented, it'll take a while before it'll become popular. So a lot of transactions will still have 2 outputs. Therefore, the stream payments will stand out among the "normal" payments. So I would still advocate for making payments look uniform and having that 0-output (at least as an option, preferable on by default). 

Another possibility for this is to have your wallet consolidate 2 outputs into one bigger one at random time intervals (and have that 0-output to not make this visible). If you do this, you end up with one big (or a few big) txo's that you can then spend separately (or use a maximum of 2 in a spending transaction). Although this is weaker than spending the individual outputs separately.



## kewde | 2016-12-05T20:31:30+00:00
There might be another reason for why you would one to include a 0 output into your commitment.

Quoting section 3.2 of the [RingCT paper](https://lab.getmonero.org/pubs/MRL-0005.pdf)
> Note that z is not computable to the originator of Xc’s coins, unless they know both of the y1;y2, but even this can be simply mitigated by including an additional change address (the usual case is
that the second commitment, with y2 as mask, is sent to yourself as change).

If you spend a ring signature back to the originator of Xc in one single output then they are able to calculate z. The paper describes that the commitment private key z is then added to the actual private key of the output, which remains unknown to the recipient. So on first sight they can't simply find the private key and recover for the keyimage that easily. The implementation however is different, the public key is not part of the last row where the output commitments are subtracted from the input commitments (respective to the TXO). In simple terms, the design as shown in the whitepaper suggests that the MLSAG can be bypassed if there is a _linkable_ ring signature on the last row, the implementation however does not do this.

Edit: removed wrong assumption, added extra information on implementation.

## dnaleor | 2016-12-06T01:15:44+00:00
yeah kwede, you're right. If inputs are spend separately (one input, one output) then the sender will be able to "follow" a certain txo of which he knows what the amount is (ingoring the fact that ring sigs are being used). When that 0-out is added, there is uncertainty about what the amount of the 2 new txo's is.

## kewde | 2016-12-06T09:51:02+00:00
He would still need to have knowledge of the mask  of the single output y1, limiting the attack. 

## moneromooo-monero | 2016-12-07T21:29:55+00:00
Feel free to ping me or others in -dev for such things, I found this by chance.
I did not realize that having one output would cause this. I patched this now.


## ghost | 2016-12-14T23:06:31+00:00
Hi @dnaleor Has version 0.10.1 achieved what you imagined with this? If so, would you mind closing this issue?

## luigi1111 | 2016-12-15T16:00:23+00:00
Solved in #1415 

## kewde | 2017-04-18T12:13:06+00:00
I wanted to add a bit of information to this thread, as it seems like a good place to store this. Note, this is still a draft that I'm working on by going through the paper. 

"Is the a 0 input required for _mathematical_ reasons when there is no alternative change output?"
I'm currently researching this, there are quite a few differences between the paper and the actual implementation which made this analysis much harder.

Let's envision the scenario of A->B->A,  where A can freely chose the public key on which B receives the output. This is an important fact, because the re-usage of a public key can be detrimental. 

The formula for keyimages is as follows: 
= `(x) * HashToEc(P) `
where x is the private key, and P the corresponding public key.

In the case of A->B->A, the adversary A can compute z (see above).
A still can't sign for the ring signature as the private key of the output is unknown, so the funds are okay. 

But she is able to compute one private key of the last row of the matrix, which sums all CT input commitments and subtracts all CT output commitments. Thus she should be able to compute the corresponding key image on her own and checks if it matches with the key image for that row provided with said transaction. 
Edit: after some more digging, I saw that there is actually no keyimage for this row. The implementation is substantially different from the whitepaper here, causing quite the confusion.

The code seems to differ from the whitepaper completely on this part, the public key is seemingly not added to the last row as described in the paper. Only the CT commitments and their respective masks. 
https://github.com/monero-project/monero/blob/master/src/ringct/rctSigs.cpp#L383 

There is also no key image provided for this row. 






# Action History
- Created by: dnaleor | 2016-11-25T00:01:50+00:00
- Closed at: 2016-12-15T16:00:24+00:00
