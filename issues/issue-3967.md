---
title: Any special reason why Blockchain::get_transactions is template member function?
source_url: https://github.com/monero-project/monero/issues/3967
author: moneroexamples
assignees: []
labels: []
created_at: '2018-06-09T03:59:26+00:00'
updated_at: '2018-06-10T22:51:45+00:00'
type: issue
status: closed
closed_at: '2018-06-10T22:51:45+00:00'
---

# Original Description
The template is defined here
https://github.com/monero-project/monero/blob/master/src/cryptonote_core/blockchain.h#L688

but the the definition and explicit initialisation are done only for std::list as second and third parameter.
https://github.com/monero-project/monero/blob/master/src/cryptonote_core/blockchain.cpp#L4561

This is very confusing especially since documentation says:

```
 * @tparam t_tx_container a standard-iterable container
 * @tparam t_missed_container a standard-iterable container
```

and at present you can't call get_transaction with only vectors for example. You have to call it with vector as first argument and lists as second and third one. This is problematic because list and vector don't have same api. Lists don't have subcript operators for example.


# Discussion History
## moneromooo-monero | 2018-06-09T09:03:59+00:00
For the record, it's changing to vector/vector in the wallet refresh code.

## moneroexamples | 2018-06-10T05:00:25+00:00
Do you know when this change is going to take place?

## moneromooo-monero | 2018-06-10T08:10:17+00:00
No.

## moneromooo-monero | 2018-06-10T11:29:25+00:00
Though I just rebased #3716 (which contains this change) so it's now ready for review.

## moneroexamples | 2018-06-10T22:51:45+00:00
Thanks.

# Action History
- Created by: moneroexamples | 2018-06-09T03:59:26+00:00
- Closed at: 2018-06-10T22:51:45+00:00
