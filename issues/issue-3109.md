---
title: 'Failed to import outputs: Transaction extra has unsupported format at index
  17'
source_url: https://github.com/monero-project/monero/issues/3109
author: bullno1
assignees: []
labels: []
created_at: '2018-01-13T07:19:52+00:00'
updated_at: '2018-01-13T11:32:24+00:00'
type: issue
status: closed
closed_at: '2018-01-13T11:32:24+00:00'
---

# Original Description
I could not import outputs using monero-cli 0.11.1.

First I export outputs from a monero-cli connected to an online and synced monerod: `export_outputs outputs`.

Then I move that `outputs` file to the offline machine, start monero-wallet-cli and do: `import_outputs outputs`

All I get is:

> Failed to import outputs: Transaction extra has unsupported format at index 17

So I tried to `rescan_bc` on the hot wallet and the outputs still can't be imported. Now both the hot and cold wallet are showing different balances because outputs can't be imported and I believe my wallet is unusable now that outputs aren't properly tracked in the hot/cold wallet. I have already tried to export key images and importing to hot wallet anyway in case that error is just a warning but the balances shown still differ.

Monero version: 0.11.1.0 for Linux 64bit.

OS of monerod: ArchLinux

OS of monero-wallet-cli: Fedora-25 guest inside QubesOS 3.2.

I am willing to provide viewkey if needed.

# Discussion History
## bullno1 | 2018-01-13T07:51:30+00:00
I dig through the code base and found the problem here:

https://github.com/monero-project/monero/blob/master/src/wallet/wallet2.cpp#L8643

The loop will break for a single invalid extra field in output. If I understood this correctly an invalid extra field which can totally be set by a sender can render my wallet unusable? Is it safe to just warn instead of throwing on this? How important are extra field? I tried looking up here https://github.com/monero-project/monero/blob/master/src/cryptonote_basic/tx_extra.h#L186 but the names are totally cryptic (mysterious_minergate)

## moneromooo-monero | 2018-01-13T11:24:41+00:00
Fixed in https://github.com/monero-project/monero/pull/3065

+resolved

# Action History
- Created by: bullno1 | 2018-01-13T07:19:52+00:00
- Closed at: 2018-01-13T11:32:24+00:00
