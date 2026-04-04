---
title: balance change
source_url: https://github.com/monero-project/monero/issues/4239
author: carrie143
assignees: []
labels:
- invalid
created_at: '2018-08-09T11:46:44+00:00'
updated_at: '2019-04-14T10:25:19+00:00'
type: issue
status: closed
closed_at: '2019-04-14T10:25:19+00:00'
---

# Original Description
1,I have saved the wallet file in my computer,
2.and then someone send some monero to my wallet,
3.I use the code to check the balance of wallet,the result is that balance do not change?I want to know why
"
const monero = require('monero-nodejs-libwallet');
monero.openWallet({
	'path': path.join(__dirname, 'test-wallet'),
	'password': '123', 
	'network': 'mainnet',
	'daemonAddress': 'localhost:18081',
}).then((wallet) => console.log('New wallet succesfully created: ' + wallet.balance()))
   .catch((e) => console.log('Failed to create new wallet: ' + e));
"

# Discussion History
## jtgrassie | 2018-08-09T12:44:33+00:00
I was about to direct you to the monero-nodejs-libwallet github as this is not the place to ask about a 3rd party library, but you have already cross-posted.

Suggest you close this issue here.

## moneromooo-monero | 2018-09-09T12:42:04+00:00
Does the problem happen without the javascript layer ?


## moneromooo-monero | 2018-10-27T13:16:03+00:00
If there's no further information, I'll close this later.
In particular, whether the tx was mined already, and whether it behave the same without the javascript layer.

## moneromooo-monero | 2019-04-14T10:12:44+00:00
No further info, closing. It's likely the wallet just needs refreshing.

Reopen if more info is available, and make sure the wallet is refreshed first.

+invalid

# Action History
- Created by: carrie143 | 2018-08-09T11:46:44+00:00
- Closed at: 2019-04-14T10:25:19+00:00
