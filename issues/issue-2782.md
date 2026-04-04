---
title: Ledger / Trezor restore ignores restore height.
source_url: https://github.com/monero-project/monero-gui/issues/2782
author: selsta
assignees: []
labels:
- bug
created_at: '2020-02-25T20:12:12+00:00'
updated_at: '2020-02-26T19:51:27+00:00'
type: issue
status: closed
closed_at: '2020-02-26T19:51:27+00:00'
---

# Original Description
Any value entered here gets ignored, the current estimated blockchain height gets used.

<img width="1026" alt="Screenshot 2020-02-25 at 21 10 17" src="https://user-images.githubusercontent.com/7697454/75283454-3a106f80-5813-11ea-949f-9164789d3303.png">

Changing the restore height in Settings -> Info -> Wallet creation height works.

Introduced somewhere between v0.15.0.2 and v0.15.0.3.

Reported here: https://www.reddit.com/r/Monero/comments/f6kokz/mnemonic_seed_changed_itself/fi7bte3/


# Discussion History
## selsta | 2020-02-25T20:54:15+00:00
Possibly introduced in https://github.com/monero-project/monero-gui/pull/2590

## rating89us | 2020-02-25T23:00:19+00:00
I'm not sure if #2463 is somehow related.

# Action History
- Created by: selsta | 2020-02-25T20:12:12+00:00
- Closed at: 2020-02-26T19:51:27+00:00
