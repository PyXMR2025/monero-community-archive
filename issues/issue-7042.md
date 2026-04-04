---
title: Can't export key images - always 164 bytes file
source_url: https://github.com/monero-project/monero/issues/7042
author: KarboDuck
assignees: []
labels: []
created_at: '2020-11-24T16:19:40+00:00'
updated_at: '2020-11-25T08:48:44+00:00'
type: issue
status: closed
closed_at: '2020-11-24T20:52:12+00:00'
---

# Original Description
I'm trying to export key images. But I always get a file with size just of 164 bytes.

Importing this file on view wallet does nothing - balance is not updated.

Tried that using three different wallets with some balance on them on:

1. Laptop #1: Ubuntu 20.10, gui wallet 0.17.1.4

2. Laptop #2: 
* Windows 10, gui wallet 0.17.1.4, cli 0.17.1.3, cli 0.17.11
* Ubuntu 20.10 from live usb, gui wallet 0.17.1.4

# Discussion History
## moneromooo-monero | 2020-11-24T16:38:00+00:00
The wallet exports what it's not exported before. Add "all" to export all, like this:

export_key_images all somefilename

## KarboDuck | 2020-11-24T16:43:12+00:00
Thanks. Seems it worked.

Is there way to use this in gui wallet?

## dEBRUYNE-1 | 2020-11-24T20:48:16+00:00
@KarboDuck - Perhaps you can close this issue (as there isn't really an issue with `monero-wallet-cli`) and open a new one on the GUI repository?

https://github.com/monero-project/monero-gui/issues/new

## KarboDuck | 2020-11-25T08:48:44+00:00
https://github.com/monero-project/monero-gui/issues/3246

# Action History
- Created by: KarboDuck | 2020-11-24T16:19:40+00:00
- Closed at: 2020-11-24T20:52:12+00:00
