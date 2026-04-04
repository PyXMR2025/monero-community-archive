---
title: Can't drag wallet window during password prompt
source_url: https://github.com/monero-project/monero-gui/issues/2063
author: Thunderosa
assignees: []
labels: []
created_at: '2019-04-10T19:02:02+00:00'
updated_at: '2019-04-25T18:06:14+00:00'
type: issue
status: closed
closed_at: '2019-04-25T18:06:13+00:00'
---

# Original Description
The wallet keeps getting better, good job. I noticed on Windows 10 using v0.14.0.0 that whenever the password prompt is up the wallet window can't be moved.  I noticed it during a screen resolution change. I was able to key in the password and then move the window, but it occurred to me that there might be edge cases where that wouldn't be the case.

# Discussion History
## sanderfoobar | 2019-04-10T19:48:33+00:00
I actually noticed this last night. Will be fixed in #2060

https://github.com/monero-project/monero-gui/blob/5dbcd714eae8bfd6e900adde6910789e5cce6613/components/PasswordDialog.qml#L65

Thanks!

## mmbyday | 2019-04-11T20:54:43+00:00
Also happens on InputDialog.qml when setting a new restore height or jumping to a page on the transactions. Fix sent to #2060 :)

# Action History
- Created by: Thunderosa | 2019-04-10T19:02:02+00:00
- Closed at: 2019-04-25T18:06:13+00:00
