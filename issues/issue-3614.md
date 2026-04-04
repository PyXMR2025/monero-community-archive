---
title: Funds of 0.11 wallet are not showing in 0.12 wallet
source_url: https://github.com/monero-project/monero/issues/3614
author: Zettt
assignees: []
labels: []
created_at: '2018-04-12T08:24:51+00:00'
updated_at: '2021-08-13T04:18:00+00:00'
type: issue
status: closed
closed_at: '2021-08-13T04:18:00+00:00'
---

# Original Description
After upgrading to the 0.12 chain, my funds were not showing anymore in my wallet. I had an issue upgrading directly to the 0.12 chain and I now have a `.unportable` file in my 0.11 wallet directory. I recreated the wallet from its seed to check whether the funds would show up eventually, but they didn't. Upgrading the chain – only running 0.12 `monerod` – I also had some issues apparently. So I deleted the entire blockchain itself, downloaded the raw blockchain again, and reimported it using the CLI tool. The funds still not show up, and I'm a little clueless, at to what I can still try. Thanks for your help!

# Discussion History
## moneromooo-monero | 2018-04-12T09:50:11+00:00
Type "set" and check the value of refresh-from-block-height. If it's after the first tx for that wallet, set it to earlier (or even 0), then rescan_bc.

## selsta | 2021-08-13T04:18:00+00:00
Closing as no reply from the issue creator and no longer relevant.

# Action History
- Created by: Zettt | 2018-04-12T08:24:51+00:00
- Closed at: 2021-08-13T04:18:00+00:00
