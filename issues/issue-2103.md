---
title: 'devguides: wallet-rpc query_key should list "spend_key" as a key_type value'
source_url: https://github.com/monero-project/monero-site/issues/2103
author: dimalinux
assignees: []
labels:
- '📚 docs: dev guides'
created_at: '2022-11-21T20:55:23+00:00'
updated_at: '2023-03-14T14:31:55+00:00'
type: issue
status: closed
closed_at: '2023-03-14T14:31:55+00:00'
---

# Original Description
Right now the `query_key` wallet RPC method only mentions `mnemonic` and `view_key` as valid inputs:
https://github.com/monero-project/monero-site/blame/ac1602403936f18bfe08ad757ad428f418d55c5e/resources/developer-guides/wallet-rpc.md#L1240

Thankfully, the undocumented `spend_key` value worked when I tried it. I see it in the tests as well: https://github.com/monero-project/monero/blob/da9aa1f/tests/functional_tests/wallet.py#L108-L109

 

# Discussion History
## plowsof | 2022-11-24T14:16:19+00:00
thanks, will do. (updating docs are paused now until the 'big one' is merged)

# Action History
- Created by: dimalinux | 2022-11-21T20:55:23+00:00
- Closed at: 2023-03-14T14:31:55+00:00
