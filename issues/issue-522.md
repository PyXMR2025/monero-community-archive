---
title: 'Integrated address: not working for size=64'
source_url: https://github.com/monero-project/monero-gui/issues/522
author: voidzero
assignees: []
labels: []
created_at: '2017-03-03T01:18:22+00:00'
updated_at: '2017-03-05T22:00:16+00:00'
type: issue
status: closed
closed_at: '2017-03-05T22:00:16+00:00'
---

# Original Description
The Payment ID field says "16 or 64 hexadecimal characters", but when I create a random hash using `openssl rand -hex 32` and paste it, the Integrated Address field says "Invalid payment ID". It only works for 16 chars.

As an aside - the integrated field has no max length atm. Probably doesn't matter much but hey, since we're squashing bugs anyway, can't hurt to add it.

# Discussion History
## Jaqueeee | 2017-03-03T17:21:35+00:00
@voidzero integrated addresses only works with short payment id. Updated the description in #530

## voidzero | 2017-03-05T22:00:16+00:00
Ahh. Perfect. Thank you. Guess this can be closed then.

# Action History
- Created by: voidzero | 2017-03-03T01:18:22+00:00
- Closed at: 2017-03-05T22:00:16+00:00
