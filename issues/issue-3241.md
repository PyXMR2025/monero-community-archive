---
title: Portable mode .cache traces
source_url: https://github.com/monero-project/monero-gui/issues/3241
author: selsta
assignees: []
labels: []
created_at: '2020-11-17T18:59:47+00:00'
updated_at: '2020-12-09T14:41:13+00:00'
type: issue
status: closed
closed_at: '2020-12-09T14:41:13+00:00'
---

# Original Description
Hello Monero devs!
Portable mode is working fine but on Ubuntu, every time I open the portable wallet, "monero-project" directory is created with files in the ".cache" directory. A file "monero-gui.desktop" is also created in ".local/share/applications".
These directories and files should be created on the same directory as the portable configuration file, so absolutely zero traces of Monero wallet are left on the computer hard disk.

_Originally posted by @skaiaswiss in https://github.com/monero-project/monero-gui/issues/3026#issuecomment-728239765_

# Discussion History
## selsta | 2020-11-17T19:00:02+00:00
Opening as new issue so that it does not get lost in a closed PR.

## xiphon | 2020-12-09T14:41:13+00:00
Closed via https://github.com/monero-project/monero-gui/pull/3245, https://github.com/monero-project/monero-gui/pull/3251, https://github.com/monero-project/monero-gui/pull/3260, https://github.com/monero-project/monero-gui/pull/3262

# Action History
- Created by: selsta | 2020-11-17T18:59:47+00:00
- Closed at: 2020-12-09T14:41:13+00:00
