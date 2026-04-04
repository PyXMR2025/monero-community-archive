---
title: Warn When Adjusting KDF Rounds
source_url: https://github.com/monero-project/monero-gui/issues/4076
author: russoj88
assignees: []
labels: []
created_at: '2022-12-01T06:56:15+00:00'
updated_at: '2022-12-01T16:52:42+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
After creating a wallet, if the number of KDF rounds is changed, the wallet password becomes invalid.

If this is the expected behavior, I think there should be a warning when changing it. A tooltip when the password is invalid may help too.

Originally from Reddit: https://www.reddit.com/r/monerosupport/comments/z7mjh5/comment/iyb9b50/?utm_source=share&utm_medium=web2x&context=3

# Discussion History
## selsta | 2022-12-01T11:26:31+00:00
> Adjusting KDF Rounds Invalidates Current Password

That's intended behaviour.

Maybe you can change the issue title to something like "warn when adjusting KDF Rounds"

## russoj88 | 2022-12-01T16:09:09+00:00
Done.

Does it make sense to set the KDF rounds per seed instead of GUI-wide?

## selsta | 2022-12-01T16:52:27+00:00
Does not work unfortunately, to save something inside the wallet cache you first have to decrypt it, which requires the amount of KDF rounds.

# Action History
- Created by: russoj88 | 2022-12-01T06:56:15+00:00
