---
title: request for more log info on i2p connections by default
source_url: https://github.com/monero-project/monero/issues/6640
author: MoneroArbo
assignees: []
labels: []
created_at: '2020-06-11T11:36:52+00:00'
updated_at: '2022-07-20T23:01:33+00:00'
type: issue
status: closed
closed_at: '2022-07-20T23:01:33+00:00'
---

# Original Description
Here is a [bitmonero.log](https://github.com/monero-project/monero/files/4764401/bitmonero.log.txt) snippet from this morning. 

Viewing this log, it is impossible for me to tell when I actually have an outbound i2p connection I can send transactions over. If there were log entries saying when outbound i2p connections go from 0 to >0, it would be really helpful.

I suppose if #6631 and #6590 were fixed this would be less of an issue, but I still think it would in general be good to report when the state that caused a warning has ended.

**edit:** Okay so apparently you can call for example 'print cn' on a detached daemon by running 'monerod print_cn'. Gonna refrain from closing this because it still seems maybe good to report when a state that causes a warning ends?

But like, not a big deal. Feel free to close.

# Discussion History
## selsta | 2022-07-20T23:01:33+00:00
Closing this, both issues you linked should be resolved in v0.18.0.0.

# Action History
- Created by: MoneroArbo | 2020-06-11T11:36:52+00:00
- Closed at: 2022-07-20T23:01:33+00:00
