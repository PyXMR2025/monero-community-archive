---
title: GUI faults on starting
source_url: https://github.com/monero-project/monero-gui/issues/973
author: Razaekel
assignees: []
labels: []
created_at: '2017-11-26T16:26:25+00:00'
updated_at: '2017-12-03T16:56:47+00:00'
type: issue
status: closed
closed_at: '2017-12-03T16:56:47+00:00'
---

# Original Description
Win10 64-bit
GUI Version 0.11.1.0

Attempting to start the GUI results in the computer working a little bit, then stopping, and doesn't open the GUI. Log file only has the log initialization line. No other errors or issues displayed.

Exploring Windows Event Viewer shows an error message recorded by windows.

`Faulting application name: monero-wallet-gui.exe, version: 0.0.0.0
Faulting module name: Qt5Core.dll, version: 5.7.0.0
Exception code: 0xc0000005
Fault offset: 0x00000000001aed78`

# Discussion History
# Action History
- Created by: Razaekel | 2017-11-26T16:26:25+00:00
- Closed at: 2017-12-03T16:56:47+00:00
