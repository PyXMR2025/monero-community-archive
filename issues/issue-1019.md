---
title: Memory Leak for Mac (maybe windows)
source_url: https://github.com/monero-project/monero-gui/issues/1019
author: am517
assignees: []
labels:
- bug
- resolved
created_at: '2017-12-13T11:57:21+00:00'
updated_at: '2018-11-18T14:18:32+00:00'
type: issue
status: closed
closed_at: '2018-11-18T14:18:32+00:00'
---

# Original Description
monero-wallet-gui for Mac uses the full amount of available memory within 48 hours. Attached is a picture after about 24 hours:

Process Name | Memory | Compressed Memory | Threads | Ports |
monero-wallet-gui | 59.46 GB | 57.98 GB | 16 | 277 |  
monerod | 139.4 MB | 42.5 MB | 15 | 36

![memory](https://user-images.githubusercontent.com/6310271/33937687-b42120a8-e047-11e7-92b5-ab2e02650d77.jpg)

It's a clean install last week:

- GUI version: v0.11.1.0
- Embedded Monero version: v0.11.1.0-2-gc328163
- OS X 10.13
- block chain has been synced for days (fresh install last week)

This is my first issue - If info is missing please let me know and I'll update it.

# Discussion History
## medusadigital | 2017-12-13T12:13:17+00:00
+bug 

## erciccione | 2018-11-18T14:16:35+00:00
Closing since it's related to an old version. Please reopen if leak stil exists.

+resolved

# Action History
- Created by: am517 | 2017-12-13T11:57:21+00:00
- Closed at: 2018-11-18T14:18:32+00:00
