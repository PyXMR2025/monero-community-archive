---
title: 'History: received transactions don''t display fee'
source_url: https://github.com/monero-project/monero-gui/issues/3124
author: rating89us
assignees: []
labels: []
created_at: '2020-09-30T12:33:23+00:00'
updated_at: '2021-02-16T02:46:35+00:00'
type: issue
status: closed
closed_at: '2021-02-16T02:46:35+00:00'
---

# Original Description
transaction fee information could be recovered from the blockchain

# Discussion History
## xiphon | 2020-10-04T22:34:34+00:00
I doubt a recipient needs such information. Could you provide a use case?

## rating89us | 2020-10-04T22:41:54+00:00
Someone from your family sends you a transaction paying a high fee ("Fastest (x200 fee)" option in GUI).
Then you warn this person "Hey, I saw that you used the fastest fee option. You don't need to use this fee level the next time".

Also, transaction fee is a public information, there is no reason to hide it in GUI.

## xiphon | 2020-10-04T22:48:25+00:00
Providing tx fee information to a recipient will require some (most probably significant) efforts. The use case you mentioned doesn't seem to be worth it.

# Action History
- Created by: rating89us | 2020-09-30T12:33:23+00:00
- Closed at: 2021-02-16T02:46:35+00:00
