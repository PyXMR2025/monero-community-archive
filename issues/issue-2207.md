---
title: Contradictory statements on daemon synchronization
source_url: https://github.com/monero-project/monero-gui/issues/2207
author: ghost
assignees: []
labels: []
created_at: '2019-06-10T14:21:51+00:00'
updated_at: '2019-08-30T18:36:05+00:00'
type: issue
status: closed
closed_at: '2019-08-30T18:35:47+00:00'
---

# Original Description
![monero1](https://user-images.githubusercontent.com/46682965/59201785-76277580-8b9b-11e9-99d2-701809b7ec25.jpg)

Edit: MAYBE the screenshot was a result of me not having pressed "Export View Key" on my Ledger Nano S. Not sure if I missed that. Edit2: This theory is WRONG.

# Discussion History
## dEBRUYNE-1 | 2019-06-11T06:23:01+00:00
>Edit: MAYBE the screenshot was a result of me not having pressed "Export View Key" on my Ledger Nano S. Not sure if I missed that.

Can you try to reproduce this behavior? 

## ghost | 2019-06-11T08:23:37+00:00
1.) My theory that it has something to do with me not having pressed "Export View Key" is WRONG.
2.) I didn't manage to reproduce the behavior WITH MY STANDARD WALLET because everything happens too fast now since it's up to date.
3.) I DID manage to reproduce the behavior with creating a new wallet (from hardware). Directly after creating the new wallet everything was fine: It was working on the "Wallet blocks remaining: 12345" and no message "Waiting on daemon synchronization to finish" was shown. Nice. But now I closed the GUI and opened it again: Then we have the situation shown in the screenshot.

## ghost | 2019-08-30T18:35:47+00:00
I close this because I think this is just a small symptom of the real issue #2304. Also, because I can't reproduce it.

# Action History
- Created by: ghost | 2019-06-10T14:21:51+00:00
- Closed at: 2019-08-30T18:35:47+00:00
