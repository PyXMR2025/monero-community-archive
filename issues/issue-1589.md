---
title: 'Script killed '
source_url: https://github.com/xmrig/xmrig/issues/1589
author: jhankz03
assignees: []
labels:
- question
created_at: '2020-03-09T10:15:48+00:00'
updated_at: '2020-08-28T16:40:45+00:00'
type: issue
status: closed
closed_at: '2020-08-28T16:40:45+00:00'
---

# Original Description

![Screenshot_20200309-171508](https://user-images.githubusercontent.com/61969060/76203667-9b7c0980-6229-11ea-9c8c-bac037f4fc0d.png)



# Discussion History
## SChernykh | 2020-03-09T13:30:21+00:00
It says `Memory 2.6/2.6 GB (98%)` on startup. You don't have enough free memory, so Android kills XMRig when it tries to allocate 2 GB dataset.

## Spudz76 | 2020-03-21T21:25:08+00:00
You can't use RandomX based coins due to not enough memory, require 2336MB for dataset even before any scratchpads.

Other coins should work?

# Action History
- Created by: jhankz03 | 2020-03-09T10:15:48+00:00
- Closed at: 2020-08-28T16:40:45+00:00
