---
title: 'monero-wallet-rpc: get_transfers does not show transactions from sub-accounts'
source_url: https://github.com/monero-project/monero/issues/3678
author: mmorrell
assignees: []
labels: []
created_at: '2018-04-21T19:48:13+00:00'
updated_at: '2018-04-22T12:16:04+00:00'
type: issue
status: closed
closed_at: '2018-04-22T12:12:56+00:00'
---

# Original Description
I sent Monero to a sub-account. During/after the blockchain confirmations, I am unable to see the transaction in the output of get_transfers API call in monero-wallet-rpc (all params set to true).

It appears that get_transfers only returns incoming transfers to the main account.

# Discussion History
## krtschmr | 2018-04-22T08:12:27+00:00
i can confirm.

## moneromooo-monero | 2018-04-22T10:29:17+00:00
Did you set account_index to whatever you want to get ?

## mmorrell | 2018-04-22T12:12:56+00:00
Thanks @moneromooo-monero . you are right again. The documentation site was out of date which was missing some of the parameters:

`      uint32_t account_index;
      std::set<uint32_t> subaddr_indices;
`

I'll look into getting the documentation site updated.



# Action History
- Created by: mmorrell | 2018-04-21T19:48:13+00:00
- Closed at: 2018-04-22T12:12:56+00:00
