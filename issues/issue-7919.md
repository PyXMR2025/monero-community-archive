---
title: '[UX] Monero GUI — failed TX always showing first if sorting by block height?'
source_url: https://github.com/monero-project/monero/issues/7919
author: xanoni
assignees: []
labels: []
created_at: '2021-09-05T21:29:50+00:00'
updated_at: '2021-09-05T21:36:48+00:00'
type: issue
status: closed
closed_at: '2021-09-05T21:36:48+00:00'
---

# Original Description
Hi there, I have a TX that failed more than a month ago, but in the GUI it is always shown first when I sort by `Blockheight`. Given people sort by blockheight to see the most recent TX, wouldn't it make sense to not show failed pending TX first?

Screenshot:

![x](https://user-images.githubusercontent.com/77220130/132141923-9fa7c0cb-fab4-4602-8e70-58b7c47ee85d.png)

My workaround has been to sort by `Date` instead.

# Discussion History
## xanoni | 2021-09-05T21:36:48+00:00
Forgot that there's a separate repo for the GUI, reopened ticket here: https://github.com/monero-project/monero-gui/issues/3691

# Action History
- Created by: xanoni | 2021-09-05T21:29:50+00:00
- Closed at: 2021-09-05T21:36:48+00:00
