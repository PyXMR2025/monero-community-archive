---
title: Trezor Safe 3 launch
source_url: https://github.com/monero-project/monero-gui/issues/4227
author: Hannsek
assignees: []
labels: []
created_at: '2023-10-12T10:47:04+00:00'
updated_at: '2024-01-18T23:19:04+00:00'
type: issue
status: closed
closed_at: '2024-01-18T23:19:04+00:00'
---

# Original Description
Hello,

New Trezor Safe 3 was launched. Please try it with the [emulator](https://github.com/trezor/trezor-user-env/). And give us a feedback if you find any bugs. 

Cheers.

# Discussion History
## plowsof | 2023-10-13T00:39:43+00:00
trezor suite detects the emulated trezor (and im able to allow the connection for it to 'check' the device and for it to tell me its not geniune etc). 

when trying to get the monero-gui to create a hardware wallet (is this intended to work?):

```
E No device found
E No matching Trezor device found. Device specifier: ""
E Device connect failed
```


## Hannsek | 2023-10-13T04:45:57+00:00
What transport type does Monero GUI use?

## ZhenyaPav | 2023-12-18T17:40:38+00:00
Just received my Trezor Safe 3. Monero GUI does not detect it when creating, not when opening a wallet created with Feather

EDIT: the issue is only with the Arch Linux package. The official build from getmonero works fine.

# Action History
- Created by: Hannsek | 2023-10-12T10:47:04+00:00
- Closed at: 2024-01-18T23:19:04+00:00
