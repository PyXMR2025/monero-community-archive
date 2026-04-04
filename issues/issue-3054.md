---
title: monerod testnet options
source_url: https://github.com/monero-project/monero/issues/3054
author: hyc
assignees: []
labels:
- enhancement
created_at: '2018-01-03T17:07:33+00:00'
updated_at: '2018-02-18T19:32:35+00:00'
type: issue
status: closed
closed_at: '2018-02-18T19:32:33+00:00'
---

# Original Description
Two topics:
1) we have a --testnet flag for running in that mode. We also have a plethora of --testnet-* flags corresponding to the same purpose as the regular flags. (e.g. --testnet-rpc-bind-port corresponding to --rpc-bind-port, etc.) Since monerod can't operate on both mainnet and testnet simultaneously, all of these --testnet-* flags are redundant. We should just use the plain flags and toggle their behavior according to the overriding --testnet flag, and delete all of the other --testnet-* flags.

Also, when we remove the --testnet-data-dir option: the --data-dir option will always refer to the mainnet directory. The "/testnet" will be hardcoded to be appended to whatever selected directory. The hardcoding is intended to avoid getting mainnet and testnet DBs confused with each other.

2) this also impacts #3017 but it should actually help, by avoiding even more proliferation of flags.
  

# Discussion History
## dEBRUYNE-1 | 2018-01-08T12:46:55+00:00
+enhancement

## moneromooo-monero | 2018-02-18T19:24:34+00:00
+resolved

# Action History
- Created by: hyc | 2018-01-03T17:07:33+00:00
- Closed at: 2018-02-18T19:32:33+00:00
