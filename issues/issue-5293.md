---
title: 'Can not start monero-wallet-rpc (boost::bad_any_cast: failed conversion using
  boost::any_cast)'
source_url: https://github.com/monero-project/monero/issues/5293
author: cearsmehul
assignees: []
labels: []
created_at: '2019-03-15T07:52:33+00:00'
updated_at: '2019-03-16T04:35:04+00:00'
type: issue
status: closed
closed_at: '2019-03-16T04:35:04+00:00'
---

# Original Description
Can not start **monero-wallet-rpc** using command

I tried bellow command to connect but it return error
`./monero-wallet-rpc --wallet-file=test --password=test --rpc-bind-port=18083  --disable-rpc-login`

error is :
`ERROR   wallet.rpc      src/wallet/wallet_rpc_server.cpp:4069   Exception at [main], what=boost::bad_any_cast: failed conversion using boost::any_cast`

Please help me as soon as possible.

# Discussion History
## dEBRUYNE-1 | 2019-03-15T10:40:16+00:00
Can you rename the wallet cache (the file without extension) from `<wallet-name>` to `<wallet-name>-old` and retry? 

## moneromooo-monero | 2019-03-15T10:56:23+00:00
https://github.com/monero-project/monero/pull/5280

## cearsmehul | 2019-03-15T11:52:38+00:00
@dEBRUYNE-1 it's not working.
This screen shot of after creating new wallet.
![image](https://user-images.githubusercontent.com/45064429/54429419-7c49b980-4746-11e9-8229-4703b9c55e9f.png)

This screen shot of 2nd try after change wallet file, As you say @dEBRUYNE-1
![image](https://user-images.githubusercontent.com/45064429/54429455-a1d6c300-4746-11e9-9ac0-02cf5e9bf467.png)


## dEBRUYNE-1 | 2019-03-15T16:00:02+00:00
@cearsmehul - Please see moneromooo's comment (i.e. recompile with #5280 included). 

## cearsmehul | 2019-03-16T04:35:04+00:00
Thanks a lot guys, 
For helping me.

# Action History
- Created by: cearsmehul | 2019-03-15T07:52:33+00:00
- Closed at: 2019-03-16T04:35:04+00:00
