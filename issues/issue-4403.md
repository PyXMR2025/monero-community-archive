---
title: monero-wallet-rpc get_incoming_transfers does not provide the account index
source_url: https://github.com/monero-project/monero/issues/4403
author: woodser
assignees: []
labels: []
created_at: '2018-09-19T16:59:00+00:00'
updated_at: '2018-09-25T23:32:52+00:00'
type: issue
status: closed
closed_at: '2018-09-25T23:32:52+00:00'
---

# Original Description
Per the [RPC](https://getmonero.org/resources/developer-guides/wallet-rpc.html#incoming_transfers) documentation, `incoming_transfers` does not return the account index so it is not possible to associate the transaction with an account.

This structure which is consistent with other methods is recommended:

```
"subaddr_index": {
  "major": 0,
  "minor": 1,
}
``` 

# Discussion History
## el00ruobuob | 2018-09-19T17:25:38+00:00
IIRC, the method can only return an incoming transaction on a specific (or default) account at the moment. Do you suggest to rewrite it completely to get all the accounts incoming transactions? Not mentioning the backward compatibility problem it would create.

## woodser | 2018-09-19T18:00:12+00:00
Ok so it is possible to associate returned transactions with the account because it's either 0 or the account index specified in the request.  Thank you.

The documentation should be updated to indicate it defaults to 0.  I can make that PR.

It probably does not make sense to return all transactions across all accounts since this behavior is inconsistent with the other transfer methods.

It would be my preference that the account index be returned like the other transfer methods but I understand this changes the return structure.

## el00ruobuob | 2018-09-19T18:06:18+00:00
No need to create a new PR, just give your thoughts on the actual one https://repo.getmonero.org/monero-project/monero-site/merge_requests/854  
But I keep in mind to add the default to 0 on every account_index input.

## moneromooo-monero | 2018-09-20T13:05:21+00:00
https://github.com/moneromooo-monero/bitmonero/tree/airpc should fix it. Can you check it works on your test case ?

## woodser | 2018-09-24T13:34:12+00:00
This will work on my test case although it does introduce additional inconsistency in the API.  Perhaps down the road we will want to release a new version of the API or some of its methods with a focus on consistency?

Can `address` be added as a field returned from incoming transfers also?

## moneromooo-monero | 2018-09-24T16:19:59+00:00
What inconsistency does it add ?

## woodser | 2018-09-24T17:10:38+00:00
Unless I'm mistaken the return structure will be:

```
{
  "subaddr_index": 0,
  "account_index": 0
  ...
}
```

Unlike the others which are:
```
"subaddr_index": {
  "major": 0,
  "minor": 1,
},
...
```

Edit: Sorry I took another look at it and it appears to be the latter, in which case it is consistent.

## moneromooo-monero | 2018-09-24T17:16:25+00:00
I see. Easy to fix. But I see what you mean, there's a field name collision... blech.

## moneromooo-monero | 2018-09-24T19:44:28+00:00
I've updated the tree to return the pair as subaddr_index as other RPCs do. I'll deem it fine since we have an incompatible wallet RPC change anyway (from v1 to v2) so I'll ride on its coattails. Not quite optimal but hey.

## moneromooo-monero | 2018-09-25T23:22:54+00:00
+resolved

# Action History
- Created by: woodser | 2018-09-19T16:59:00+00:00
- Closed at: 2018-09-25T23:32:52+00:00
