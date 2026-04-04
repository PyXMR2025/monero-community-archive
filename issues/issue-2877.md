---
title: spelling errors in monero binaries
source_url: https://github.com/monero-project/monero-gui/issues/2877
author: adrelanos
assignees: []
labels: []
created_at: '2020-05-01T14:02:20+00:00'
updated_at: '2020-05-01T14:33:15+00:00'
type: issue
status: closed
closed_at: '2020-05-01T14:33:15+00:00'
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


# Discussion History
## xiphon | 2020-05-01T14:23:25+00:00
Don't see any of these in the GUI code.

## adrelanos | 2020-05-01T14:30:44+00:00
Right...

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

## selsta | 2020-05-01T14:31:48+00:00
Please report to monero repo. This is for GUI only.

## adrelanos | 2020-05-01T14:33:14+00:00
https://github.com/monero-project/monero/issues/6492

# Action History
- Created by: adrelanos | 2020-05-01T14:02:20+00:00
- Closed at: 2020-05-01T14:33:15+00:00
