---
title: 'PR #756: improve watch-only import handling'
source_url: https://github.com/monero-project/monero/issues/757
author: fluffypony
assignees: []
labels:
- enhancement
- wontfix
created_at: '2016-03-25T06:24:02+00:00'
updated_at: '2019-07-05T19:17:39+00:00'
type: issue
status: closed
closed_at: '2019-07-05T19:17:39+00:00'
---

# Original Description
Per https://github.com/monero-project/bitmonero/pull/756#issuecomment-201100119

> This needs public spend key (or address) I believe.
> 
> I'd suggest allowing an optional address which will be checked if provided and used for view key if needed.


# Discussion History
## moneromooo-monero | 2016-03-25T09:18:22+00:00
It works fine without an address. The generated address is different for the first part, but the second part is the same, and should still see the incoming txes I think, though I don't think I've tested that.


## moneromooo-monero | 2016-04-02T14:25:05+00:00
https://github.com/monero-project/bitmonero/pull/785


## luigi1111 | 2016-08-10T15:24:31+00:00
https://github.com/monero-project/bitmonero/blob/0fbe9cfcdb9df2b141024eec04c3c7412791b741/src/simplewallet/simplewallet.cpp#L1118-L1126

```
    if (field_address_found)
    {
      cryptonote::account_public_address address2;
      bool has_payment_id;
      crypto::hash8 new_payment_id;
      get_account_integrated_address_from_str(address2, has_payment_id, new_payment_id, testnet, field_address);
      address.m_spend_public_key = address2.m_spend_public_key;
    }
    m_wallet->generate(m_wallet_file, password, address, viewkey);
```

This won't work correctly. If address AND spendkey are not present, this should error instead of creating a wallet with on the view key pair.


## ghost | 2018-01-07T11:12:08+00:00
Is this issue still relevant?

## moneromooo-monero | 2018-01-08T18:05:10+00:00
Apparetnly not, the code errors out if !field_address_found (now in wallet2.cpp).

## jonathancross | 2018-08-27T13:10:32+00:00
Can this issue be closed then?

## ghost | 2019-06-25T12:27:54+00:00
Please be aware that "ancient" `help wanted` issues make a super-strange impression to newcomers.



## moneromooo-monero | 2019-07-05T19:08:17+00:00
Looks like it's moot now.

+wontfix

# Action History
- Created by: fluffypony | 2016-03-25T06:24:02+00:00
- Closed at: 2019-07-05T19:17:39+00:00
