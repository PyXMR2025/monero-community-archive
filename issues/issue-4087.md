---
title: 'Monero GUI no longer working after Tails 5.8 upgrade '
source_url: https://github.com/monero-project/monero-gui/issues/4087
author: psoidon
assignees: []
labels: []
created_at: '2022-12-21T12:24:39+00:00'
updated_at: '2023-02-27T22:58:46+00:00'
type: issue
status: closed
closed_at: '2023-02-27T22:58:45+00:00'
---

# Original Description
Monero GUI was working prior to Tails upgrade.
After upgrade it no longer starts, I believe this is an issue due to Weyland change in Tails 5.8
Unable to access wallet :-( 

# Discussion History
## nahuhh | 2022-12-21T12:33:27+00:00
https://gitlab.tails.boum.org/tails/tails/-/issues/19326

## tobtoht | 2022-12-21T12:44:30+00:00
Workaround:

Open `monero-wallet-gui.AppImage` in a text editor and change it to:

    QT_QPA_PLATFORM=xcb ./monero-wallet-gui

Save the file and run it like normal.


## psoidon | 2022-12-22T09:49:20+00:00
Awesome, that worked, many thanks.

## ghost | 2022-12-29T22:19:48+00:00
@tobtoht 
Awesome, is that all that would be needed for apps in general to support Wayland or would `QT_QPA_PLATFORM=wayland;xcb` be more suited *(not just for xmr wallets but any AppImages in Tails)*?

## selsta | 2023-02-27T22:58:45+00:00
This should be fixed on Tails side.

# Action History
- Created by: psoidon | 2022-12-21T12:24:39+00:00
- Closed at: 2023-02-27T22:58:45+00:00
