---
title: Cant create reserve proof with message
source_url: https://github.com/monero-project/monero/issues/8443
author: MexicanTakeout
assignees: []
labels: []
created_at: '2022-07-18T17:09:29+00:00'
updated_at: '2022-07-19T19:11:36+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
This is on  Monero 'Fluorine Fermi' (v0.18.0.0-b6a029f22) stage net. Steps to reproduce:
- create wallet
- use a faucet to supply moneroj to wallet
- open wallet and type in get_reserve_proof 10 "this is a message"
response shows Error: usage: get_reserve_proof (all|\<amount\>) \[\<message\>\]

Strangely enough, it works with single word message but the signature turns out to be bad when check with check_reserve_proof. Other than that, get_reserve_proof  works fine with just the amount.


# Discussion History
## reemuru | 2022-07-19T17:10:28+00:00
This is not true. You can in fact create reserve proof with a message. From a technical standpoint there is no reason to have whitespace in a message. Hence change it to `this_is_a_message` with no quotations. You are thinking of 'message' as in terms of a written sentence with proper punctuation.

## MexicanTakeout | 2022-07-19T18:56:38+00:00
@reemuru RPC call can parse message inside double quotes like here https://i.imgur.com/epIinY6.png
So I think this is an inconsistency issue.

The use of message string also wasn't clear to me at first. I expected it to be like a secret message that would reveal to a receiver after verified proof, but it is more like a password to use in decrypting the reserve proof.

## MexicanTakeout | 2022-07-19T19:11:36+00:00
> Strangely enough, it works with single word message but the signature turns out to be bad when check with check_reserve_proof. Other than that, get_reserve_proof works fine with just the amount.

In response to the bad signature problem, the message is __required__ for a reserve proof with message.



# Action History
- Created by: MexicanTakeout | 2022-07-18T17:09:29+00:00
