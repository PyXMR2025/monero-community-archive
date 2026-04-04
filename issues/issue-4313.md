---
title: Coin control.
source_url: https://github.com/monero-project/monero-gui/issues/4313
author: OrginalS
assignees: []
labels: []
created_at: '2024-05-05T19:32:02+00:00'
updated_at: '2025-02-14T08:09:18+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
All new UTXOs, including change, have a 20-minute lock on them, resulting in an inability to send multiple transactions in a row. This can be mitigated by splitting up coins into multiple UTXOs. However, the official gui wallet has no capability to spend or even show individual UTXOs. Because of this, accurate splitting up of UTXOs requires guessing, checking the transaction fee to estimate the number of UTXOs used in it and using the 20-minute lock to force the wallet to use the desired UTXOs.

Please implement a coin control feature.

# Discussion History
## b4n6-b4n6 | 2024-08-28T09:24:52+00:00
> All new UTXOs, including change, have a 20-minute lock on them, resulting in an inability to send multiple transactions in a row. This can be mitigated by splitting up coins into multiple UTXOs. However, the official gui wallet has no capability to spend or even show individual UTXOs. Because of this, accurate splitting up of UTXOs requires guessing, checking the transaction fee to estimate the number of UTXOs used in it and using the 20-minute lock to force the wallet to use the desired UTXOs.
> 
> Please implement a coin control feature.

Do a one-to-many self send transaction where you send to, for example, 10 recepients where every recepient is an address from your own wallet and every receipients receive amount is utxo size you want it to be split into - for me this works well in practice

## Arrow-Archer | 2025-02-14T08:03:12+00:00
> All new UTXOs, including change, have a 20-minute lock on them, resulting in an inability to send multiple transactions in a row. This can be mitigated by splitting up coins into multiple UTXOs. However, the official gui wallet has no capability to spend or even show individual UTXOs. Because of this, accurate splitting up of UTXOs requires guessing, checking the transaction fee to estimate the number of UTXOs used in it and using the 20-minute lock to force the wallet to use the desired UTXOs.
> 
> Please implement a coin control feature.

I have to use a third party wallet just because the official wallet doesn't have a coin control feature! This is nonsense! Give me a coin control feature right now, other shit can wait!

# Action History
- Created by: OrginalS | 2024-05-05T19:32:02+00:00
