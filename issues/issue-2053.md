---
title: Monero GUI remembered mnemonic seed after logout of wallet
source_url: https://github.com/monero-project/monero-gui/issues/2053
author: minhng99
assignees: []
labels: []
created_at: '2019-04-04T08:39:02+00:00'
updated_at: '2019-04-16T20:46:49+00:00'
type: issue
status: closed
closed_at: '2019-04-16T20:46:49+00:00'
---

# Original Description
When you `Restore wallet from keys or mnemonic seed` then lock/logout of the wallet (not closed the wallet entirely) and try to `Restore wallet from keys or mnemonic seed` again then in the UI it will shows every detail that you've typed into the `Restore wallet` from the first import, including the seed, I think this is a security risk and the application should've cleared the UI data.

# Discussion History
# Action History
- Created by: minhng99 | 2019-04-04T08:39:02+00:00
- Closed at: 2019-04-16T20:46:49+00:00
