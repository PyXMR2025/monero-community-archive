---
title: '[Discussion] Multiple payment IDs in one transaction'
source_url: https://github.com/monero-project/monero/issues/1659
author: JollyMort
assignees: []
labels: []
created_at: '2017-02-01T17:43:18+00:00'
updated_at: '2017-08-25T21:18:24+00:00'
type: issue
status: closed
closed_at: '2017-08-25T21:18:24+00:00'
---

# Original Description
**Why?**

Having the possibility to use multiple payment IDs in one transaction would make some use cases simpler and could optimize some payments. It would also allow more flexibility with the newly proposed disposable address scheme and make it easier for exchanges/pools to pay to integrated addresses of either type (stealth PID scheme or disposable address scheme).

**Why not?**

Transactions like that would grow a bit to maintain privacy, but that's it - I think. If fee is paid per kB, it's all fair game to decide whether to use this or not. Considering the size of transactions with RCT range proofs, I think the growth would be insignificant (8bytes / output) and it would make sense to optimize multiple payments wih PID into one TX, rather than pay separately as it is now.

**Initial proposal (just to start the discussion)**

I understand that with the current format, each transaction has the TX-extra field, and each output is created by using the TX-key and output index. Thus, each output has a different shared secret, even when multiple outputs are sent to the same address.

P = H(rA || i)G + B, yes? where || is concatenation

Would something like the below be possible?

1. User specifies a list of integrated addresses and amounts as part of transfer command.
2. Wallet takes the address, builds outputs for each address.
3. An array of 64-bit values is built, of same number of members as number of outputs in the TX.
4. The i-th output will match the i-th PID array member. If used as it is, this would leak information as to which outputs belong to the same address.
5. So, I propose only the 1st appearance of a given PID to be used 'as it is', be it the stealth scheme where it's get encrypted or the disposable address scheme where it'd be plaintext.
6. Any following occurance for the same address would be XOR'd with the H(rA || i) of the matching output.
7. Also, change output would have to come with some random 64 bits. If normal addresses are used in the same TX, the same would have to be done for those.

The end result: n outputs, n payment IDs; all payment IDs would be different, and only the recipient would be able to tell a given 'set' is for him. On a second thought, under 6. we could just put some random 64 bits and it should work all the same, while the receiving wallet would parse only the first output's PID.

# Discussion History
## kenshi84 | 2017-02-02T14:33:22+00:00
I've been thinking along the same line, and I see some real use cases in this feature where the sender would like to transfer funds to multiple recipients using either integrated addresses with encrypted pID or disposable addresses with unencrypted pID. Since pIDs in integrated addresses are encrypted, they can be safely reused and can act as some kind of tags for payments (e.g. "monthly rent from Bob").

In my understanding, there seem to be two types of syntaxes for the `transfer` command: 1) one that has a long or short payment ID attached to the end separately, and 2) one that doesn't. For the first case, the syntax would look like:

    transfer [<mixin>] <address_1> <amount_1> [<address_2> <amount_2> ...] <long/short pID>

Note that no integrated/disposable addresses are allowed here. I hope this legacy syntax to be eventually deprecated since copying and pasting pIDs manually is a great source of human error.

In contrast, the new syntax

    transfer [<mixin>] <address_1> <amount_1> [<address_2> <amount_2> ...]

would allow any of the standard, integrated, and disposable addresses to be used for any number of times. To have a unified view toward addresses, I'd propose to see any standard addresses (including the change address) to be implicitly associated with 64bit pID of zero. This way, each output public key gets associated with a 64bit value corresponding to its payment ID, either encrypted using `H(aR || i)` or unencrypted (when used with the disposable address scheme). The resulting pIDs in the transaction will look all random and uniform.


## JollyMort | 2017-08-25T21:18:22+00:00
closing this in favor of way forward presented in #2056 

# Action History
- Created by: JollyMort | 2017-02-01T17:43:18+00:00
- Closed at: 2017-08-25T21:18:24+00:00
