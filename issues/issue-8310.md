---
title: Update hardforks.cpp
source_url: https://github.com/monero-project/monero/issues/8310
author: lubomr
assignees: []
labels: []
created_at: '2022-05-03T12:20:30+00:00'
updated_at: '2022-07-19T15:54:39+00:00'
type: issue
status: closed
closed_at: '2022-07-19T15:54:39+00:00'
---

# Original Description
Since the network upgrade is set for 16th July 2022, real values can be added to hardforks.cpp. 

AC: Update 
```
  { 15, 8000000, 0, 1608223241 }, // temp so tests test with these consensus rules
  { 16, 8000001, 0, 1608223242 }, // temp so tests test with these consensus rules
```
with real values.

# Discussion History
## selsta | 2022-07-19T15:54:39+00:00
Resolved in v0.18.0.0

# Action History
- Created by: lubomr | 2022-05-03T12:20:30+00:00
- Closed at: 2022-07-19T15:54:39+00:00
