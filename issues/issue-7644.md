---
title: 'monero-wallet-cli: improve error message when sending 0'
source_url: https://github.com/monero-project/monero/issues/7644
author: moneromooo-monero
assignees: []
labels: []
created_at: '2021-04-03T17:21:11+00:00'
updated_at: '2022-05-25T10:32:50+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
From anon_udxf6fdz[m] on IRC

CLI user experience improvement

Reproduction:
monero-wallet-cli --stagenet --daemon-host stagenet.community.xmr.to --wallet-file /home/thinkpad/Monero/wallets/stagenet --password asdf --command transfer monero:59McWTPGc745SRWrSMoh8oTjoXoQq6sPUgKZ66dQWXuKFQ2q19h9gvhJNZcFTizcnT12r63NFgHiGd6gBCjabzmzHAMoyD6 

This command fails with the following error:

Error: one of destinations is zero

At a minimum the command should fail with the error:

Error: Amount is zero

It would be most preferred to prompt the user to enter their desired amount to transfer

Applicable sections of code
https://github.com/monero-project/monero/blob/master/src/wallet/wallet2.cpp#L8753
https://github.com/monero-project/monero/blob/master/src/wallet/wallet2.cpp#L8912
https://github.com/monero-project/monero/blob/master/src/wallet/wallet2.cpp#L9885

# Discussion History
## ghost | 2021-04-06T22:40:23+00:00
I opened #7651 to improve the errors, but I didn't add a prompt. I thought doing so would make the behavior of commands inconsistent (since most just produce an error if missing an argument), but it can still be added if we want it.

# Action History
- Created by: moneromooo-monero | 2021-04-03T17:21:11+00:00
