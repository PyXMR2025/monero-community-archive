---
title: Monero-GUI throws error::needs_rescan
source_url: https://github.com/seraphis-migration/monero/issues/129
author: ComputeryPony
assignees: []
labels: []
created_at: '2025-10-01T23:27:06+00:00'
updated_at: '2025-12-09T18:08:40+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
While getting ready for the alpha hardfork I noticed that creating a new wallet in the GUI seems to work at first, but after closing the GUI the wallet no longer loads.
Instead I get:
```
E m_blockchain.size() != 1 || m_tree_cache.n_synced_blocks() != 0. THROW EXCEPTION: error::needs_rescan
```
repeated every 10 seconds in the console and the GUI shows `Synchronizing Wallet` in the bottom left.
The GUI is pointed at my own node, which is marked as trusted.

I am building the `monero-gui` from source from upstream commit `1de4a65f90685561bc317d55ad2cfca3277992a1` with it's CMakeFile.txt updated to 0.19.0.0 and the `monero` submodule is from this repo on the `fcmp++-alpha-stressnet` branch with commit `3f4864ce389be85c2a9bce28d1072f8c24f75f27`. I did remember to set the GUI to testnet. :)

# Discussion History
## j-berman | 2025-10-01T23:53:24+00:00
Repro'd, working on it

## j-berman | 2025-10-02T00:30:25+00:00
In the meantime, you should be able to manually set a new restore height in Settings->Info to be able to use the wallet

## ComputeryPony | 2025-10-02T00:45:25+00:00
> In the meantime, you should be able to manually set a new restore height in Settings->Info to be able to use the wallet

Gotcha, thanks for the quick response!

## j-berman | 2025-10-02T01:43:58+00:00
#131 should fix it

## ComputeryPony | 2025-10-02T01:51:15+00:00
> [#131](https://github.com/seraphis-migration/monero/pull/131) should fix it

Yup, that fixed it. Thanks!

## j-berman | 2025-12-09T18:08:40+00:00
Keeping this open for now. Ideally there is a better solution in place that makes sure new wallets use the daemon's chain height as the initial restore height

# Action History
- Created by: ComputeryPony | 2025-10-01T23:27:06+00:00
