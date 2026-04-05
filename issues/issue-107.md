---
title: Errors
source_url: https://github.com/xmrig/xmrig/issues/107
author: RomNiko
assignees: []
labels: []
created_at: '2017-09-12T16:45:19+00:00'
updated_at: '2017-10-02T11:55:25+00:00'
type: issue
status: closed
closed_at: '2017-10-02T11:55:25+00:00'
---

# Original Description
1. In config.json in this file, I can not set the value of a variable log-file. Program does not start.
2. max-cpu-usage I think the percentage is somehow strange. at a value of 75% gives 100% load of real processor cores http://take.ms/jWKH0


# Discussion History
## xmrig | 2017-09-12T16:56:31+00:00
Log file option required string contains log filename
```json
"log-file": "xmrig.log",
```

`max-cpu-usage` limiting maximum **visible** CPU usage, in your case it limited by L3 cache (8 / 2 = 4 threads) it's about 50% and on your screenshot it 49% it's ok.

# Action History
- Created by: RomNiko | 2017-09-12T16:45:19+00:00
- Closed at: 2017-10-02T11:55:25+00:00
