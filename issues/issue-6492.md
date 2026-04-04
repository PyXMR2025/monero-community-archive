---
title: spelling errors in monero binaries
source_url: https://github.com/monero-project/monero/issues/6492
author: adrelanos
assignees: []
labels: []
created_at: '2020-05-01T14:32:51+00:00'
updated_at: '2020-10-15T22:44:40+00:00'
type: issue
status: closed
closed_at: '2020-10-15T22:44:39+00:00'
---

# Original Description
wrong right

offets offsets
additionnal additional
enought enough
droppped dropped
requred required
Distrubution Distribution
unsuported unsupported

That's just what `lintian` is telling me.

grep -r unsuported

Binary file usr/bin/monero-blockchain-ancestry matches
Binary file usr/bin/monero-blockchain-usage matches
Binary file usr/bin/monero-blockchain-mark-spent-outputs matches
Binary file usr/bin/monero-blockchain-export matches
Binary file usr/bin/monero-blockchain-import matches
Binary file usr/bin/monero-blockchain-depth matches
Binary file usr/bin/monero-blockchain-prune matches
Binary file usr/bin/monero-wallet-cli matches
Binary file usr/bin/monerod matches
Binary file usr/bin/monero-blockchain-stats matches
Binary file usr/bin/monero-blockchain-prune-known-spent-data matches
Binary file usr/bin/monero-gen-ssl-cert matches
Binary file usr/bin/monero-wallet-rpc matches
Binary file usr/bin/monero-gen-trusted-multisig matches

# Discussion History
## moneromooo-monero | 2020-05-19T16:00:13+00:00
https://github.com/monero-project/monero/pull/6565

Some of those don't appear to be ours.

## moneromooo-monero | 2020-10-15T22:44:39+00:00
Fixed for those in our code. Open a new bug if you find more.

# Action History
- Created by: adrelanos | 2020-05-01T14:32:51+00:00
- Closed at: 2020-10-15T22:44:39+00:00
