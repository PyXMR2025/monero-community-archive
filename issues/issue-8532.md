---
title: Wallet transactions disappear after first confirmation when wallet rpc started
  with offline daemon
source_url: https://github.com/monero-project/monero/issues/8532
author: woodser
assignees: []
labels: []
created_at: '2022-08-23T13:51:11+00:00'
updated_at: '2022-09-10T23:05:12+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
1. Start monero-wallet-rpc with offline `--daemon-address`.
2. Open or create a wallet.
3. Connect to online daemon with `set_daemon`.
4. Receive funds, they appear as unconfirmed.
5. After first confirmation, wallet has 0 balance and no `transfers` or `incoming_transfers`.

moneromooo says: "That sounds like a refresh-from-block-height issue. If the wallet is created without a daemon, it'll guess, and the guess might be wrong. Which is probably is if you're starting with a clean chain."

The only issue is that the transactions do not re-appear after calling `rescan_blockchain`.

# Discussion History
## j-berman | 2022-09-10T23:05:12+00:00
Are you running into this using a custom chain by chance? I can repro when I do that, but it works fine on my end with mainnet/testnet. A few issues can surface when creating an offline wallet and then trying to connect it to a custom chain, this issue included. Like moo said, the offline wallet will set `m_refresh_from_block_height` using [this guess-timated approximate height - 1 month of blocks](https://github.com/monero-project/monero/blob/6402dbee69867c76530b45e8a21b692850fea03f/src/wallet/wallet2.cpp#L4844), and then will [skip processing blocks](https://github.com/monero-project/monero/blob/6402dbee69867c76530b45e8a21b692850fea03f/src/wallet/wallet2.cpp#L2579) until that height. By default that approximate height is going to be pretty high, so a custom chain's low height blocks will get skipped when processing.

# Action History
- Created by: woodser | 2022-08-23T13:51:11+00:00
