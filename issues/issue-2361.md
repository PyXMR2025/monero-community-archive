---
title: 'When I use -f config.json paramter that error occur '
source_url: https://github.com/xmrig/xmrig/issues/2361
author: Zhiyuancheng
assignees: []
labels: []
created_at: '2021-05-10T01:41:01+00:00'
updated_at: '2021-05-11T16:21:52+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
./xmrig -f config.json -B
error infor:
```
rx.unmineable.com:3333 error: "Double check your TRX address, it seems to be invalid!" , code: -1
read error: "end of file."
```

when switch command : ./xmrig , the error is seams too. 

how to use config.json file instead of use others parameter in command?


# Discussion History
## gkroon | 2021-05-11T16:21:39+00:00
Try `./xmrig --config=/path/to/config.json`

Also, have a look at the docs: https://xmrig.com/docs/miner

Or, `./xmrig --help`

# Action History
- Created by: Zhiyuancheng | 2021-05-10T01:41:01+00:00
