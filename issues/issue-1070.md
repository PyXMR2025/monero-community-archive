---
title: Allow view key to see outgoing transactions (consensus change)
source_url: https://github.com/monero-project/monero/issues/1070
author: ChristopherKing42
assignees: []
labels: []
created_at: '2016-09-12T17:48:26+00:00'
updated_at: '2022-02-10T21:37:06+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
In [this post](https://redd.it/51i0n7), I describe a way to modify the protocol to allow view keys to see outgoing transactions.

Essentially, every output has two keys: H_p(rA)G+B (what we currently have now) and H_p(rA)G+A. The first is controlled by the spend key and second by the view key.

When making a transaction, both keys need to be included in the key vector of a MLSAG (and therefore must be made someone holding the private spend (and view) key). Using the view key, you can identify the key image of the second key.


# Discussion History
## moneroexamples | 2016-09-15T07:03:44+00:00
Has it been confirmed that the matchs checks out?


## ChristopherKing42 | 2016-09-15T11:26:39+00:00
The cryptographers are still busy I hear. I just thought I would leave this here so I wouldn't forget to.


## MalMen | 2016-09-19T10:33:38+00:00
If the maths are corrected I am pro this change


## ChristopherKing42 | 2016-09-19T13:08:21+00:00
@MalMen you mean if the math is correct?


## UkoeHB | 2022-02-10T21:36:45+00:00
The [Jamtis](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024) addressing scheme for the WIP Seraphis tx protocol will have a wallet tier that can view outgoing txs.

# Action History
- Created by: ChristopherKing42 | 2016-09-12T17:48:26+00:00
