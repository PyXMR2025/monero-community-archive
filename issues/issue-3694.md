---
title: Possibly memory leak in slow-hash.c on Windows
source_url: https://github.com/monero-project/monero/issues/3694
author: aivve
assignees: []
labels: []
created_at: '2018-04-24T09:31:38+00:00'
updated_at: '2018-05-27T09:56:51+00:00'
type: issue
status: closed
closed_at: '2018-05-27T09:56:51+00:00'
---

# Original Description
Please review, memory leak is possible here:
https://github.com/monero-project/monero/blob/8fdf645397654956b74d6ddcd79f94bfa7bf2c5f/src/crypto/slow-hash.c#L527

The correct expression suggested: `VirtualFree(hp_state, 0, MEM_RELEASE);`

It was reported by @mgurgev here: https://github.com/seredat/karbowanec/issues/41, his proposal fixes memory leak.

He refers to: https://msdn.microsoft.com/en-us/library/windows/desktop/aa366892(v=vs.85).aspx




# Discussion History
## hyc | 2018-04-24T12:54:23+00:00
Looks like you're right, according to the M$ docs.

## moneromooo-monero | 2018-05-27T09:50:43+00:00
+resolved

# Action History
- Created by: aivve | 2018-04-24T09:31:38+00:00
- Closed at: 2018-05-27T09:56:51+00:00
