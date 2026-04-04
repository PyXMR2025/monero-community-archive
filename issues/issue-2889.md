---
title: Checkpoint Validation Failed
source_url: https://github.com/monero-project/monero/issues/2889
author: heroes1412
assignees: []
labels:
- invalid
created_at: '2017-12-07T02:23:28+00:00'
updated_at: '2018-02-11T11:04:48+00:00'
type: issue
status: closed
closed_at: '2017-12-07T08:48:27+00:00'
---

# Original Description
i want to create a custom chain, but get the error? how can i fix this?

# Discussion History
## moneromooo-monero | 2017-12-07T08:41:35+00:00
This is a bug tracker, not a help desk.

+invalid


## UsFantom | 2018-02-11T11:04:48+00:00
in checkpoints.cpp, 
function: check_block

insert "return true;" in the first line.

# Action History
- Created by: heroes1412 | 2017-12-07T02:23:28+00:00
- Closed at: 2017-12-07T08:48:27+00:00
