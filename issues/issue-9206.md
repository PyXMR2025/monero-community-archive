---
title: data-dir option for MacOS
source_url: https://github.com/monero-project/monero/issues/9206
author: duhanov
assignees: []
labels:
- question
- low priority
- mac
- more info needed
created_at: '2024-02-26T08:59:00+00:00'
updated_at: '2025-12-19T14:59:35+00:00'
type: issue
status: closed
closed_at: '2025-12-19T14:59:35+00:00'
---

# Original Description
Please, activate data-dir option in Gui-Wallet for MacOS 🙏

# Discussion History
## selsta | 2024-02-26T10:55:28+00:00
You can set the blockchain location in `Settings -> Node` which in turn sets the --data-dir flag.

## duhanov | 2024-02-27T04:38:32+00:00
It would be great if it were possible to specify via the console like this:
/Applications/monero-wallet-gui.app/Contents/MacOS/monero-wallet-gui --data-dir=/Volumes/mydisk/Monero/

but now this is not possible (
Unknown option 'data-dir'.

## selsta | 2024-02-27T14:09:38+00:00
Yes, `--data-dir` is a monerod flag and not a monero-wallet-gui flag. Is there a good reason why this should be added to GUI?

## duhanov | 2024-02-29T00:47:59+00:00
I would not like my wallet settings and location to be visible. The ideal option is for the client itself and settings to be stored on an external drive. My solution: store the launch script on an external drive indicating the path to the wallet, for this I need --data-dir parameter

## selsta | 2024-02-29T00:49:07+00:00
Did you try to use the monero-gui portable mode?

## duhanov | 2024-02-29T00:51:13+00:00
> Did you try to use the monero-gui portable mode?

its possible on mac os? how to?the settings will not be saved on the main drive?

## selsta | 2024-02-29T12:33:36+00:00
Put monero-gui on your external drive and start it. Click on "Change wallet mode" in the main menu, and then select the "portable mode" flag. Afterwards all settings will be stored in the same location as the monero-gui program itself.

# Action History
- Created by: duhanov | 2024-02-26T08:59:00+00:00
- Closed at: 2025-12-19T14:59:35+00:00
