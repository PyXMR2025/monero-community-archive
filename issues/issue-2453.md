---
title: start-gui.sh and start-tails.appimage not shipped with v0.15.0.1 release archive
source_url: https://github.com/monero-project/monero-gui/issues/2453
author: tobtoht
assignees: []
labels: []
created_at: '2019-11-23T16:53:50+00:00'
updated_at: '2019-12-08T14:25:02+00:00'
type: issue
status: closed
closed_at: '2019-12-08T14:25:02+00:00'
---

# Original Description
No description

# Discussion History
## selsta | 2019-11-23T17:16:17+00:00
We don’t use the linuxdeploy helper script anymore, that’s why they are missing.

Do you know the point of `start-gui.sh` and `start-tails.appimage`? Do we need both?

## tobtoht | 2019-11-23T17:21:52+00:00
`start-gui.sh` is unnecessary.
`start-tails.appimage` was added for Tails users to start the wallet without needing to open the terminal and cd to the right directory. It depended on `start-gui.sh`, but can be changed to launch `monero-wallet-gui` directly, I suppose.

## xiphon | 2019-11-27T11:14:09+00:00
`start-tails.AppImage` will be included in v0.15.0.2 point release

# Action History
- Created by: tobtoht | 2019-11-23T16:53:50+00:00
- Closed at: 2019-12-08T14:25:02+00:00
