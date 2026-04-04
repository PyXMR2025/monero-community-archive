---
title: adding entry to address book edits description of anther entry
source_url: https://github.com/monero-project/monero/issues/8218
author: Arimfexendrapus
assignees: []
labels: []
created_at: '2022-03-14T17:02:12+00:00'
updated_at: '2022-03-16T08:08:03+00:00'
type: issue
status: closed
closed_at: '2022-03-16T08:08:02+00:00'
---

# Original Description
Adding an entry to the address book in Monero GUI version 0.17.3.1 will result in not only an entry being added, but it will also cause the description of the bottom entry in the address book to change to the description of the newly added entry.

# Discussion History
## reemuru | 2022-03-15T06:03:08+00:00
@Arimfexendrapus I was able to duplicate this in monero-wallet-gui but not the cli so this issue should probably be [here](https://github.com/monero-project/monero-gui/issues). Looks like address book index 0 is getting overwritten on new add. Will take a look later.

![duplicate-8218](https://user-images.githubusercontent.com/13033037/158316492-176f13be-dbc2-47cb-88c5-19bed783015e.png)


## selsta | 2022-03-16T08:08:02+00:00
Wrong repo

# Action History
- Created by: Arimfexendrapus | 2022-03-14T17:02:12+00:00
- Closed at: 2022-03-16T08:08:02+00:00
