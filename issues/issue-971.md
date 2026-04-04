---
title: Instead of Ring multisignatures, why not use multiparty computation for increased
  privacy?
source_url: https://github.com/monero-project/monero/issues/971
author: ChristopherKing42
assignees: []
labels: []
created_at: '2016-08-19T18:05:34+00:00'
updated_at: '2016-12-15T17:34:05+00:00'
type: issue
status: closed
closed_at: '2016-12-15T17:34:05+00:00'
---

# Original Description
The plan is currently that multisig will be implemented via ring multisignatures.

Multisig transactions and accounts will be able to be distinguished from non-multisig by looking at the blockchain. Also, the nature of the multisig wallet (the number of participants and the threshold) would be apparent. (Is this paragraph correct?)

Therefore, I propose that multiparty computation is used instead, as described [here](http://monero.stackexchange.com/questions/782/can-you-have-a-multsig-wallet-with-the-current-monero-protocol).

It would make multisig addresses indistinguishable from regular addresses. They would also be the same size as regular addresses as a corollary (in terms of what needs stored on the blockchain).

Moreover, this does not require any changes to consensus code, and is compatible with RingCT.


# Discussion History
## moneromooo-monero | 2016-08-19T18:49:57+00:00
>  (Is this paragraph correct?)

As far as I know, it is not.

If you are the person who devised another way to do multisig, you may want to discuss this with Shen Noether, so that any pros and cons of various methods may be compared. Ask fluffypony if so.


## ChristopherKing42 | 2016-08-19T18:53:41+00:00
Where can I contact Shen Noether?


## luigi1111 | 2016-08-19T19:09:04+00:00
This "ring multisignature" that has been proposed (I think by tacotime originally) **is** a multiparty computation. Basically what you describe (AFA being indistinguishable, etc). I believe the RingCT version will be similar.


## ChristopherKing42 | 2016-08-19T19:10:58+00:00
Oh, okay. Sorry. (I should have studied it closer.)


# Action History
- Created by: ChristopherKing42 | 2016-08-19T18:05:34+00:00
- Closed at: 2016-12-15T17:34:05+00:00
