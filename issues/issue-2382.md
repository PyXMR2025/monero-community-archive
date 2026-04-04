---
title: Using "Sign tx file" on any non-tx/invalid file resets wallet balance to 0
source_url: https://github.com/monero-project/monero-gui/issues/2382
author: rbrunner7
assignees: []
labels: []
created_at: '2019-09-08T07:30:53+00:00'
updated_at: '2019-09-30T23:45:56+00:00'
type: issue
status: closed
closed_at: '2019-09-30T23:45:56+00:00'
---

# Original Description
Reddit user *NotOnceNotNevah* stumbled over this quite bizarre bug yesterday (see [this Reddit thread](https://old.reddit.com/r/monerosupport/comments/d0utpe/sign_tx_file_empty_wallet/)):

Open any wallet. Go to the *Send* tab. Click the *Sign tx file* button from the *Advanced options*. Select any random file except one that really contains any unsigned Monero transactions. Despite being invalid the file won't get rejected, but you will get a confirmation dialog stating that there are 0 transactions to sign. Accept nevertheless by pressing the *Ok* button.

Result: After a few seconds the balance of the wallet will go to 0 and stay there.

I found no way to "repair" the wallet after this short of a full rescan by setting the restore height. The transactions are still there, just the balance seems to go to zero.

Tested on Windows and on Linux with the 0.14.1.0 release GUI wallet, with a mainnet and a testnet wallet. I also had a look at the code, but I am afraid I don't know enough about GUI wallet structure/architecture to find out something with reasonable effort.

A quick test showed that the CLI wallet does not seem to have this bug: It rejects any file that does not contain valid unsigned Monero transactions as, well, invalid ...

# Discussion History
## xiphon | 2019-09-09T00:09:03+00:00
https://github.com/monero-project/monero/pull/5894

# Action History
- Created by: rbrunner7 | 2019-09-08T07:30:53+00:00
- Closed at: 2019-09-30T23:45:56+00:00
