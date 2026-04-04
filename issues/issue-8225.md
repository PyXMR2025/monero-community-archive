---
title: high log level causes high memory usage during IBD / fresh sync
source_url: https://github.com/monero-project/monero/issues/8225
author: Gingeropolous
assignees: []
labels: []
created_at: '2022-03-24T20:15:57+00:00'
updated_at: '2023-08-26T17:03:48+00:00'
type: issue
status: closed
closed_at: '2023-08-26T17:03:48+00:00'
---

# Original Description
reproduce on 2 different machines with log level 3 and 4 using v0.17.3.0 (and v0.17.2.3 and v0.17.0.0) .

16 gb RAM on both machines. SSD,5900x ryzen. 

monerod would sync but eventually get killed by the OOM killer. 

high memory issue doesn't appear with default log level (0)

# Discussion History
## Gingeropolous | 2023-08-26T17:03:48+00:00
i think this ended up being OOM on the screen application.

look at me im productive closing my own issues

# Action History
- Created by: Gingeropolous | 2022-03-24T20:15:57+00:00
- Closed at: 2023-08-26T17:03:48+00:00
