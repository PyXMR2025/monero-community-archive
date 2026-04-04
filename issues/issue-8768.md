---
title: Issue with connecting to multiple local nodes after v18.2.0
source_url: https://github.com/monero-project/monero/issues/8768
author: suggalla
assignees: []
labels: []
created_at: '2023-03-07T20:16:47+00:00'
updated_at: '2023-03-08T21:44:32+00:00'
type: issue
status: closed
closed_at: '2023-03-08T21:44:31+00:00'
---

# Original Description
Seeing the following error when configuring multiple local nodes to connect: `CONNECTION FROM 127.0.0.1 REFUSED, too many connections from the same address`. I also have the following flag configured: `--allow-local-ip`. This worked prior to this version.

# Discussion History
## selsta | 2023-03-08T05:11:58+00:00
Which version did you use previously?
Did you set `--max-connections-per-ip` ?


## suggalla | 2023-03-08T14:20:21+00:00
Let me try setting that. Previously I used `v0.18.1.2`

## selsta | 2023-03-08T19:33:10+00:00
I can't think of any change between v0.18.1.2 and v0.18.2.0 that would cause this.

I'd need detailed steps to reproduce this myself if the max-connections flag doesn't help.

## suggalla | 2023-03-08T21:44:31+00:00
That seems to have resolved it. Thanks! 

# Action History
- Created by: suggalla | 2023-03-07T20:16:47+00:00
- Closed at: 2023-03-08T21:44:31+00:00
