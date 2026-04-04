---
title: if wallet opened but not connet success,then do disconnect,the thread will
  blocked.
source_url: https://github.com/monero-project/monero/issues/6264
author: forever00010110
assignees: []
labels: []
created_at: '2019-12-29T12:16:52+00:00'
updated_at: '2020-01-19T19:12:08+00:00'
type: issue
status: closed
closed_at: '2020-01-19T19:12:07+00:00'
---

# Original Description
 in  accounts.cpp  141  line, example  in android device

  //-----------------------------------------------------------------
  void account_base::deinit()
  {
    try{
      m_keys.get_device().disconnect();
    } catch (const std::exception &e){
      MERROR("Device disconnect exception: " << e.what());
    }
  }
  //-----------------------------------------------------------------


# Discussion History
## moneromooo-monero | 2019-12-30T14:57:54+00:00
Ia this ledger, trezor, other ?

## forever00010110 | 2019-12-30T15:07:08+00:00
> Ia this ledger, trezor, other ?

build it and running in android device,in wallet  software

## forever00010110 | 2019-12-30T15:08:16+00:00
> > Ia this ledger, trezor, other ?
> 
> build it and running in android device,in wallet software

in api close wallet

## moneromooo-monero | 2019-12-30T15:27:56+00:00
Is this using a Ledger hw wallet, or a Trezor hw wallet ?

## forever00010110 | 2019-12-30T16:51:29+00:00
> Is this using a Ledger hw wallet, or a Trezor hw wallet ?

https://github.com/monero-project/monero/blob/master/src/wallet/api/wallet.cpp  line  760，deinit()  function

 In android device，not ledger，the old version don’t have this code，it not have this probelm

## moneromooo-monero | 2019-12-30T17:45:56+00:00
For non ledger/trezor, the disconnect call does nothing. That's why I asked. Did you change the source by any chance ?

## moneromooo-monero | 2019-12-30T18:55:45+00:00
Also, when it blocks, run gdb into the process, ie:
gdb /path/to/your/binary `pidof yourbinaryname`
yourbinaryname will likely be monero-wallet-cli or monero-wallet-rpc
Then:
thread apply all bt

There will be multiple pages, press enter till it's finished displaying all.


## forever00010110 | 2020-01-19T19:12:07+00:00
It block in other function，not in deinit()，I will closed it.

# Action History
- Created by: forever00010110 | 2019-12-29T12:16:52+00:00
- Closed at: 2020-01-19T19:12:07+00:00
