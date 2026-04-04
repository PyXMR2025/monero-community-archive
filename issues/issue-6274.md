---
title: (stagenet)get_transfer_by_txid  can not return wallet address tx
source_url: https://github.com/monero-project/monero/issues/6274
author: binlaniua
assignees: []
labels: []
created_at: '2019-12-31T03:41:40+00:00'
updated_at: '2020-01-01T05:20:34+00:00'
type: issue
status: closed
closed_at: '2020-01-01T05:20:34+00:00'
---

# Original Description
i use gui send xmr to wallet-rpc-cli, but when i use get_transfer_by_txid return -8
--------
![image](https://user-images.githubusercontent.com/5960462/71609305-489b2b80-2bc2-11ea-97ce-eb5d70a6a85e.png)
--------
![image](https://user-images.githubusercontent.com/5960462/71609320-62d50980-2bc2-11ea-90a0-ee7b138e5019.png)
--------
![image](https://user-images.githubusercontent.com/5960462/71609329-797b6080-2bc2-11ea-875c-9016b097eaf7.png)


# Discussion History
## binlaniua | 2019-12-31T05:16:53+00:00
get_transfer_by_txid  default use **account_index: 0**, what can i do **get_transfer_by_txid** by any account_index

## binlaniua | 2019-12-31T05:39:10+00:00
if i have many account, how to check tx is belong my wallet, loop check?

## moneromooo-monero | 2019-12-31T09:06:35+00:00
I suppose we could return all if the account_index parameter is not specified. I'm not sure it's a good idea though, since it would further merge accounts, and keeping them separate is a privacy feature.

## binlaniua | 2019-12-31T15:23:02+00:00
> I suppose we could return all if the account_index parameter is not specified. I'm not sure it's a good idea though, since it would further merge accounts, and keeping them separate is a privacy feature.

thanks reply。may be provider another argument **"all_account: true | false"**  :)

# Action History
- Created by: binlaniua | 2019-12-31T03:41:40+00:00
- Closed at: 2020-01-01T05:20:34+00:00
