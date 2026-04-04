---
title: 'Can''t create transaction: unexpected error: Unable to send hidapi command.
  Error 64: Unknown error'
source_url: https://github.com/monero-project/monero/issues/7907
author: hendrash
assignees: []
labels: []
created_at: '2021-08-29T22:14:30+00:00'
updated_at: '2022-12-16T10:15:37+00:00'
type: issue
status: closed
closed_at: '2021-08-31T02:09:11+00:00'
---

# Original Description
![Screenshot from 2021-08-29 22-03-49](https://user-images.githubusercontent.com/26557257/131275372-f3a1acab-dd70-4b6c-9a91-24ea95eb4b1d.png)



# Discussion History
## selsta | 2021-08-29T22:15:21+00:00
Which OS? Do you have an anti virus?

## hendrash | 2021-08-29T22:16:00+00:00
Whenever you try to send money  with a hardware wallet from the Monero GUI you always get this error any ideas

## hendrash | 2021-08-29T22:30:23+00:00
I've tried it on windows and I've also tried on Linux, On Linux it's giving me an unknown error 

## selsta | 2021-08-29T22:33:17+00:00
Could it be a broken cable?

## hendrash | 2021-08-29T22:34:20+00:00
2021-08-29 22:31:54.617	E Unable to send hidapi command. Error 64: Unknown error
2021-08-29 22:31:54.618	E Can't create transaction:  unexpected error: Unable to send hidapi command. Error 64: Unknown error
2021-08-29 22:31:54.618	W "Could not convert argument 0 at"
2021-08-29 22:31:54.618	W 	 "onTransactionCreated@qrc:/main.qml:822"
2021-08-29 22:31:54.618	W "Passing incompatible arguments to C++ functions from JavaScript is dangerous and deprecated."
2021-08-29 22:31:54.618	W "This will throw a JavaScript TypeError in future releases of Qt!"
2021-08-29 22:33:05.764	E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2021-08-29 22:33:05.764	E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2021-08-29 22:33:05.765	E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2021-08-29 22:33:21.585	E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2021-08-29 22:33:21.585	E pull_blocks failed, try_count=3
2021-08-29 22:33:21.585	E daemonBlockChainHeight: Failed to connect to daemon
2021-08-29 22:33:21.586	E daemonBlockChainTargetHeight: Failed to connect to daemon



## selsta | 2021-08-29T22:36:09+00:00
Did you export your view key on wallet opening?

## hendrash | 2021-08-29T22:38:41+00:00
Yes when I first created the wallet it asked me to export my keys to this wallet 

## hendrash | 2021-08-29T22:39:39+00:00
Would there be any logging or debugging commands I could try?

## hendrash | 2021-08-29T22:40:55+00:00
It also says "No unmixable outputs to sweep"

## selsta | 2021-08-29T22:43:33+00:00
Is Windows and Linux installed on the same computer? I would try the following things:

- Make sure to use the latest Ledger firmware, Ledger monero app and Monero GUI
- Try a different USB port
- Try a different cable

## hendrash | 2021-08-29T23:03:22+00:00
 7f1153c2c800	WARNING	frontend	src/wallet/api/wallet.cpp:412	"Could not convert argument 0 at"
2021-08-29 22:35:54.533	    7f1153c2c800	WARNING	frontend	src/wallet/api/wallet.cpp:412		 "onTransactionCreated@qrc:/main.qml:822"
2021-08-29 22:35:54.533	    7f1153c2c800	WARNING	frontend	src/wallet/api/wallet.cpp:412	"Passing incompatible arguments to C++ functions from JavaScript is dangerous and deprecated."
2021-08-29 22:35:54.533	    7f1153c2c800	WARNING	frontend	src/wallet/api/wallet.cpp:412	"This will throw a JavaScript TypeError in future releases of Qt!"
2021-08-29 22:36:35.389	    7f11513aa700	ERROR	device.io	src/device/device_io_hid.cpp:201	Unable to send hidapi command. Error 64: Unknown error
2021-08-29 22:36:35.402	    7f1153c2c800	ERROR	frontend	src/wallet/api/wallet.cpp:416	Can't create transaction:  unexpected error: Unable to send hidapi command. Error 64: Unknown error
2021-08-29 22:36:35.402	    7f1153c2c800	WARNING	frontend	src/wallet/api/wallet.cpp:412	"Could not convert argument 0 at"
2021-08-29 22:36:35.402	    7f1153c2c800	WARNING	frontend	src/wallet/api/wallet.cpp:412		 "onTransactionCreated@qrc:/main.qml:822"
2021-08-29 22:36:35.402	    7f1153c2c800	WARNING	frontend	src/wallet/api/wallet.cpp:412	"Passing incompatible arguments to C++ functions from JavaScript is dangerous and deprecated."
2021-08-29 22:36:35.402	    7f1153c2c800	WARNING	frontend	src/wallet/api/wallet.cpp:412	"This will throw a JavaScript TypeError in future releases of Qt!"
2021-08-29 22:37:38.516	    7f11523ac700	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:14007	!r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2021-08-29 22:37:38.516	    7f11523ac700	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:7623	no connection to daemon
2021-08-29 22:39:43.496	    7f1153c2c800	ERROR	frontend	src/wallet/api/wallet.cpp:416	Can't create transaction:  
2021-08-29 22:39:43.496	    7f1153c2c800	WARNING	frontend	src/wallet/api/wallet.cpp:412	"Could not convert argument 0 at"
2021-08-29 22:39:43.496	    7f1153c2c800	WARNING	frontend	src/wallet/api/wallet.cpp:412		 "onTransactionCreated@qrc:/main.qml:828"
2021-08-29 22:39:43.496	    7f1153c2c800	WARNING	frontend	src/wallet/api/wallet.cpp:412	"Passing incompatible arguments to C++ functions from JavaScript is dangerous and deprecated."
2021-08-29 22:39:43.496	    7f1153c2c800	WARNING	frontend	src/wallet/api/wallet.cpp:412	"This will throw a JavaScript TypeError in future releases

## hendrash | 2021-08-29T23:04:23+00:00
That's from the monero-wallet-gui.log

## selsta | 2021-08-29T23:05:02+00:00
It's the same error.

## hendrash | 2021-08-29T23:39:11+00:00
The weird thing is sometimes it says creating transaction... then it never changes

## selsta | 2021-08-29T23:40:01+00:00
Do you accept the transaction on your Ledger?

## hendrash | 2021-08-29T23:52:47+00:00
It never asked 

## selsta | 2021-08-30T04:25:42+00:00
Please reply to this comment: https://github.com/monero-project/monero/issues/7907#issuecomment-907889094

I have read 2 reports about this online. One person resolved it by using a different USB port and another person resolved it by reinstalling Windows.

## hendrash | 2021-08-31T02:08:59+00:00
Thanks for the help  @selsta  I was able to solve my issue by using a brand new USB cable. The cable is very sensitive when sending monero It has to be in almost perfect condition I realized. 

## kipz | 2022-11-16T23:57:48+00:00
Same error here. New ledger and new cable. Works with other currencies.

## selsta | 2022-11-17T01:35:20+00:00
@kipz can you post more info? Which OS?

## jonathancross | 2022-12-16T10:15:37+00:00
I saw this a few times after a long sync in Monero GUI v0.18.1.2 on Linux.
Switching USB cable itself did not solve the issue, but restarting the GUI did.

# Action History
- Created by: hendrash | 2021-08-29T22:14:30+00:00
- Closed at: 2021-08-31T02:09:11+00:00
