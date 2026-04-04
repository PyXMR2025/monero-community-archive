---
title: show_transfers bug
source_url: https://github.com/monero-project/monero/issues/4285
author: carrie143
assignees: []
labels: []
created_at: '2018-08-20T11:37:23+00:00'
updated_at: '2022-04-08T15:09:20+00:00'
type: issue
status: closed
closed_at: '2022-04-08T15:09:19+00:00'
---

# Original Description
1.I have started the monero-wallet-cli service,"/monero-wallet-cli  --wallet-file /root/wallet_file/test-wallet --password xxxx"
2.I run the comand," show_transfers":to find the transaction history,the result follows:
![t](https://user-images.githubusercontent.com/24546264/44338097-7ee57880-a4af-11e8-8f16-04d263ac3d23.png)
My questions is that why the transctions which in red block have the "to" address detail,and the other transaction do not show the destination address?I guess may be ,these transactions is created before I restored wallet,so I create two new outgoing transactions,Still do not show the  destination address.I have no idea

# Discussion History
## moneromooo-monero | 2018-08-20T11:39:13+00:00
You are correct.

## carrie143 | 2018-08-20T11:40:18+00:00
why new transaction still do not show the destination address.?

## moneromooo-monero | 2018-08-20T11:44:33+00:00
Oh I see, the two ones below the highlighted ones you mean ?
If you type "set", what value is there for "store-tx-info" ?

## iDunk5400 | 2018-08-20T12:33:12+00:00
The other sends were most likely done using a different wallet cache file.

## moneromooo-monero | 2018-08-20T12:38:30+00:00
Or maybe crash/kill. Is this the case ?

## carrie143 | 2018-08-21T01:06:17+00:00
@iDunk5400 ,I use the same  wallet cache file to send the transactions

## carrie143 | 2018-08-21T02:35:04+00:00
1.yes,the two ones are new transactions that I send using the same the wallet file
2.what do you mean"If you type "set", what value is there for "store-tx-info"",I have no idea about the command "store-tx-info",where I should run it?


## moneromooo-monero | 2018-08-21T09:57:20+00:00
After sending the transactions with the missing destination, did the wallet crash, or did you kill it without saving ?

store-tx-info is not a command. set is a command which will show a number of settings, including one called store-tx-info.

## moneromooo-monero | 2018-09-09T12:41:09+00:00
ping

## selsta | 2022-04-08T15:09:19+00:00
No reply, closing.

# Action History
- Created by: carrie143 | 2018-08-20T11:37:23+00:00
- Closed at: 2022-04-08T15:09:19+00:00
