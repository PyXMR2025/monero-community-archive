---
title: 'Ledger Nanox : handle locked device gracefully'
source_url: https://github.com/monero-project/monero-gui/issues/3507
author: jonathancross
assignees: []
labels: []
created_at: '2021-05-26T11:12:27+00:00'
updated_at: '2021-05-26T11:50:03+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Error message from "Please enter wallet password for: [wallet name]" screen:
> Couldn't open wallet: Wrong Device Status: 0x6e00 (SW_CLA_NOT_SUPPORTED), EXPECTED 0x9000 (SW_OK), MASK 0xffff

Monero app version: `1.7.6` (latest Firmware)

Related: #2762

![2021-05-26_nanox_locked_error_gui](https://user-images.githubusercontent.com/5115470/119649756-48d54000-be23-11eb-8d2b-0cbb366779d9.png)

Ideally we would just ask the user to unlock the device using their PIN and ensure the Monero app is open.

# Discussion History
## rating89us | 2021-05-26T11:50:03+00:00
> just ask the user to unlock the device using their PIN and ensure the Monero app is open.

I think this is a nice solution. I'll work on this.

# Action History
- Created by: jonathancross | 2021-05-26T11:12:27+00:00
