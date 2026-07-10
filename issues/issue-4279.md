---
title: '[GNU/Linux] launches Konqueror'
source_url: https://github.com/monero-project/monero-gui/issues/4279
author: dchmelik
assignees: []
labels: []
created_at: '2024-02-26T04:33:42+00:00'
updated_at: '2026-07-10T07:45:11+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
On GNU/Linux monero-gui, if you have Konqueror/KDE installed, running monero-gui first launches Konqueror file_manager/web_browser, which monero-gui shouldn't do.

# Discussion History
## selsta | 2026-07-09T00:24:45+00:00
I don't know why this happens, we don't have any file manager / web browser specific code. Is this still an issue?

## dchmelik | 2026-07-10T07:44:41+00:00
It was certain situations, like maybe when launched from GUI menu, which I don't currently have monero-gui in (after upgrade and when XFCE hid 'other' menu intermittently) and monero-gui is no longer asking me if it should be added to that menu.

# Action History
- Created by: dchmelik | 2024-02-26T04:33:42+00:00
