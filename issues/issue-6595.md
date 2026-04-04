---
title: '`get_reserve_proof` returns valid proof with amount greater than account balance'
source_url: https://github.com/monero-project/monero/issues/6595
author: woodser
assignees: []
labels: []
created_at: '2020-05-27T16:03:51+00:00'
updated_at: '2020-06-06T17:56:12+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
With unconfirmed transactions, `get_reserve_proof` returns a valid proof when called with an account index and an amount greater than the account's balance.  Checking the proof gives a total amount greater than the requested proof amount and a non-zero `spent` amount.  I figured the proof would only succeed with an amount less than or equal to the account balance?

# Discussion History
## moneromooo-monero | 2020-05-28T11:06:19+00:00
Seems to work for me. I added logs, and:

curl -k -X POST $URL -d '{"jsonrpc":"2.0","id":"0","method":"get_reserve_proof","params":{"account_index":1,"amount":"13529939118000","message":"Test message"}}' -H 'Content-Type: application/json'
{
  "error": {
    "code": -1,
    "message": "Not enough balance in this account for the requested minimum reserve amount"
  },
  "id": "0",
  "jsonrpc": "2.0"
}

2020-05-28 11:03:27.275	I get_reserve_proof: account_minreserve is set
2020-05-28 11:03:27.275	I    = 1 13.529939118000
2020-05-28 11:03:27.277	I Found usable output 6019, account 1, amount 0.899818240000
2020-05-28 11:03:27.277	I Found usable output 6021, account 1, amount 5.000000000000
2020-05-28 11:03:27.277	I Found usable output 6023, account 1, amount 5.000000000000
2020-05-28 11:03:27.277	I Total amount found: 10.899818240000
2020-05-28 11:03:27.278	E account_minreserve && balance < account_minreserve->second. THROW EXCEPTION: error::wallet_internal_error
2020-05-28 11:03:27.278	W /src/wallet/wallet2.cpp:11813:N5tools5error21wallet_internal_errorE: Not enough balance in this account for the requested minimum reserve amount




## moneromooo-monero | 2020-05-28T11:36:24+00:00
Please send the JSON you're sending, and the balance of the account in question.

## woodser | 2020-05-31T13:12:07+00:00
`get_reserve_proof` is called with this JSON: `{"method":"get_reserve_proof","id":"0","jsonrpc":"2.0","params":{"amount":"41900886994506","account_index":0,"message":"Test message"}}`

`get_accounts` returns `...{account_index=0, balance=41825886994506, ...}`

A proof signature is returned.  Calling `check_reserve_proof` with the signature returns:

`{id=0, jsonrpc=2.0, result={good=true, spent=29169365936882, total=42370606771561}}`

Account 0 has an unconfirmed incoming transfer (from a different account in the same wallet).

## moneromooo-monero | 2020-05-31T13:59:47+00:00
Is this a testnet/stagenet wallet you could send me the keys to ?

## woodser | 2020-05-31T14:11:06+00:00
Yes, it's a stagenet wallet:

`hijack lucky rally sober hockey robot gumball amaze gave fifteen organs gecko skater wizard demonstrate upright system vegan tobacco tsunami lurk withdrawn tomorrow uphill organs`

Height of first transaction: 589429

## moneromooo-monero | 2020-06-01T00:39:43+00:00
That JSON gets me "Not enough balance in this account for the requested minimum reserve amount". I guess I fixed it in my work branch. I did make changes to the reserve proof stuff for historical proofs, but that relies on some database changes so it'll be a bit.

## woodser | 2020-06-01T01:19:06+00:00
That JSON will give me the same thing unless there's an unconfirmed incoming transfer to the account.  Also, the transaction was sent from the same wallet.

## moneromooo-monero | 2020-06-01T01:32:43+00:00
Ah. Do you know what height your daemon was when you ran this and it failed ?

## woodser | 2020-06-01T01:47:58+00:00
No, but I just re-ran and reproduced the issue (height 592428).

## moneromooo-monero | 2020-06-01T11:07:28+00:00
Still works at that height, with a tx in the txpool. You may want to try with my crash branch, which includes that patch, or wait till I've PRed it (I started PRing one of the deps).

## woodser | 2020-06-01T12:11:18+00:00
I can try the branch to see if it resolve the issue.

## moneromooo-monero | 2020-06-01T12:34:26+00:00
It converts your db to v6 btw. Use on a copy.

## moneromooo-monero | 2020-06-01T19:28:26+00:00
https://github.com/monero-project/monero/pull/6616 has all the necessary patches for this without the other stuff.

## woodser | 2020-06-02T11:19:27+00:00
Will #6616 update my db to v6?

## moneromooo-monero | 2020-06-02T11:54:43+00:00
Yes.

## woodser | 2020-06-06T16:52:15+00:00
Still seeing this issue with #6616.

## moneromooo-monero | 2020-06-06T17:56:12+00:00
I'll try again with your wallet soon, in case I messed something up.

# Action History
- Created by: woodser | 2020-05-27T16:03:51+00:00
