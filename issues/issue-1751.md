---
title: histogram reports no unlocked rct outputs, not even ours
source_url: https://github.com/monero-project/monero-gui/issues/1751
author: mmorrell
assignees: []
labels: []
created_at: '2018-11-24T17:38:18+00:00'
updated_at: '2018-11-25T21:21:42+00:00'
type: issue
status: closed
closed_at: '2018-11-25T21:21:42+00:00'
---

# Original Description
I'm using a modified monero-wallet-rpc with the required confirmations to unlock reduced to 1. 

Frequently when I try to call transfer using monero-wallet-rpc I get the message: "histogram reports no unlocked rct outputs, not even ours".

Is this expected and/or is there a workaround?

# Discussion History
## dEBRUYNE-1 | 2018-11-25T20:26:53+00:00
@mmorrell - This is probably related to `monero-wallet-rpc`. Therefore, could you please open this issue on the main repository? 

https://github.com/monero-project/monero/issues/new

# Action History
- Created by: mmorrell | 2018-11-24T17:38:18+00:00
- Closed at: 2018-11-25T21:21:42+00:00
