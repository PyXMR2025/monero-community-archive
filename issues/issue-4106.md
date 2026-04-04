---
title: Offset is larger than total outputs when creating viewwallet for stagenet wallet
source_url: https://github.com/monero-project/monero-gui/issues/4106
author: elibroftw
assignees: []
labels: []
created_at: '2023-01-20T01:48:06+00:00'
updated_at: '2023-01-20T03:09:41+00:00'
type: issue
status: closed
closed_at: '2023-01-20T03:09:28+00:00'
---

# Original Description
To reproduce create a stagenet wallet, and click create view wallet.

![image](https://user-images.githubusercontent.com/21298211/213600529-94d25159-7962-458e-93d8-84058968b624.png)

Creating a view wallet a second time results in this error.

![image](https://user-images.githubusercontent.com/21298211/213600558-852fb94b-5dad-4786-9750-9520bcb9cada.png)


# Discussion History
## selsta | 2023-01-20T03:09:28+00:00
Solved by https://github.com/monero-project/monero/pull/8616, will be included in the next release.

# Action History
- Created by: elibroftw | 2023-01-20T01:48:06+00:00
- Closed at: 2023-01-20T03:09:28+00:00
