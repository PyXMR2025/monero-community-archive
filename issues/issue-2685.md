---
title: 'failed to generate a new wallet: Cannot get a device address'
source_url: https://github.com/monero-project/monero-gui/issues/2685
author: got3nks
assignees: []
labels: []
created_at: '2019-12-25T18:06:19+00:00'
updated_at: '2019-12-25T21:31:10+00:00'
type: issue
status: closed
closed_at: '2019-12-25T21:31:10+00:00'
---

# Original Description
I'm trying to setup a Trezor with Monero-Wallet-GUI on MacOS but get this error when creating a new wallet:

`failed to generate a new wallet: Cannot get a device address`

I can't find the log path to check more details. The Trezor is working fine in Chrome browser with latest bridge driver installed.

# Discussion History
## got3nks | 2019-12-25T18:11:47+00:00
I think I've found the reason. Monero-Wallet-GUI supports Trezor T only.

Is there any wat to use Monero with an older Trezor One?

## dEBRUYNE-1 | 2019-12-25T20:39:19+00:00
There is currently no Monero support for the older Trezor One. 

# Action History
- Created by: got3nks | 2019-12-25T18:06:19+00:00
- Closed at: 2019-12-25T21:31:10+00:00
