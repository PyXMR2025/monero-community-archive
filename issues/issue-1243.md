---
title: '[RFC] Expected behaviour of set-default-mixin'
source_url: https://github.com/monero-project/monero/issues/1243
author: ghost
assignees: []
labels: []
created_at: '2016-10-22T12:18:45+00:00'
updated_at: '2017-10-03T10:54:22+00:00'
type: issue
status: closed
closed_at: '2017-10-03T10:54:22+00:00'
---

# Original Description
My thoughts:

In HF 3 (currently) - default is 4 but minimum allowed is 2. In HF 4 these will both be 4

Someone typing `set` in the console will see the value that has actually been set as their default, and not `0` defining `default`

If a wallet has a mixin value below the minimum allowed, their wallet will be forced to upgrade to the minimum allowed value of 2, rising to 4 after HF 4.


# Discussion History
## luigi1111 | 2016-11-01T16:51:56+00:00
Related to #1206. Will leave both open for now.


## moneromooo-monero | 2017-10-03T10:49:24+00:00
+resolved

# Action History
- Created by: ghost | 2016-10-22T12:18:45+00:00
- Closed at: 2017-10-03T10:54:22+00:00
