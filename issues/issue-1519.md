---
title: '[CriticalЕrror / Fraud] Transaction amount invalid'
source_url: https://github.com/monero-project/monero-gui/issues/1519
author: candro
assignees: []
labels:
- resolved
created_at: '2018-07-24T09:27:09+00:00'
updated_at: '2018-07-27T08:09:23+00:00'
type: issue
status: closed
closed_at: '2018-07-27T08:09:23+00:00'
---

# Original Description
Attention, in the latest version (0.12.2.0) Monero Gui for Windows has a critical error that allows an attacker to deceive you. Briefly, in the transaction history shows the amount of 20XMR, and in fact, 10XMR has arrived.

The balance is increased by 10, if you do a transaction check, then it also writes 10, but in the history the transaction has a value of 20.

# Discussion History
## dEBRUYNE-1 | 2018-07-24T12:37:56+00:00
This issue is resolved in GUI v0.12.3.0, which should be out soon. 

## dEBRUYNE-1 | 2018-07-27T08:03:56+00:00
+resolved

# Action History
- Created by: candro | 2018-07-24T09:27:09+00:00
- Closed at: 2018-07-27T08:09:23+00:00
