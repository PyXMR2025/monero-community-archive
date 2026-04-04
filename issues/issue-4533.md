---
title: Ledger Nano X OS v & GUI sending error
source_url: https://github.com/monero-project/monero-gui/issues/4533
author: dan-is-not-the-man
assignees: []
labels: []
created_at: '2025-11-22T22:37:18+00:00'
updated_at: '2025-11-24T19:45:30+00:00'
type: issue
status: closed
closed_at: '2025-11-24T18:24:32+00:00'
---

# Original Description
I get an error when trying to send ,please see image.

Gui wallet - 18.4.3 & 18.4.4
ledger version - Ledger Nano X OS version 2.6.0

fyi feather wallet worked

<img width="1182" height="552" alt="Image" src="https://github.com/user-attachments/assets/ab12b84f-ab4c-414a-bc45-cf5ffe633987" />

# Discussion History
## selsta | 2025-11-23T00:05:00+00:00
Which OS are you using?

## dan-is-not-the-man | 2025-11-23T03:43:50+00:00
> Which OS are you using?

Linux - openSUSE Leap 15.6

## tobtoht | 2025-11-23T10:34:34+00:00
Try this build from CI: https://github.com/monero-project/monero-gui/actions/runs/19602370976?pr=4534

## dan-is-not-the-man | 2025-11-24T06:08:26+00:00
> Try this build from CI: https://github.com/monero-project/monero-gui/actions/runs/19602370976?pr=4534

Yeah worked

## tobtoht | 2025-11-24T19:34:36+00:00
This error message is shown when you attempt to construct a transaction after the Ledger Monero app was closed and reopened for any reason.

With the latest Ledger firmware it seems to automatically close the Monero app _some of the time_ when it is locked due to inactivity. 

It is unclear whether bumping hidapi changes anything. With hidapi 0.15.0, I haven't been able to reproduce the Monero app closing on its own, whereas with 0.13.1 it has happened sporadically at least thrice.

If you encounter this error, the workaround is to simply close the wallet in the GUI and reopen it.

# Action History
- Created by: dan-is-not-the-man | 2025-11-22T22:37:18+00:00
- Closed at: 2025-11-24T18:24:32+00:00
