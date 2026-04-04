---
title: Ledger not detected on Windows v0.12.1 GUI
source_url: https://github.com/monero-project/monero-gui/issues/1435
author: philkode
assignees: []
labels:
- resolved
created_at: '2018-05-31T09:15:05+00:00'
updated_at: '2018-06-01T11:45:22+00:00'
type: issue
status: closed
closed_at: '2018-06-01T11:45:22+00:00'
---

# Original Description
Just built v0.12.1 GUI from source on Windows and can't open an existing, known working ledger wallet file. The Ledger wallet file was created on v0.12.1 CLI on the same machine.

The error given by the GUI is:
`Couldn't open wallet: device not found: Ledger`

This is the same error that v0.12.0 CLI gave on Windows when it couldn't connect to the smartcard service at all. If it can interface with that then it gives a more detailed error message.

Update: the compilation-time error given is:
`Could NOT find PCSC (missing: PCSC_INCLUDE_DIR)`

# Discussion History
## dEBRUYNE-1 | 2018-06-01T11:40:12+00:00
This is resolved with https://github.com/monero-project/monero/pull/3886

+resolved

# Action History
- Created by: philkode | 2018-05-31T09:15:05+00:00
- Closed at: 2018-06-01T11:45:22+00:00
