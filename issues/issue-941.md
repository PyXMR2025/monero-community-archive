---
title: 'out_peers command in daemon returns error: unsuccessful '
source_url: https://github.com/monero-project/monero/issues/941
author: Gingeropolous
assignees: []
labels: []
created_at: '2016-07-31T00:07:48+00:00'
updated_at: '2017-10-15T18:12:20+00:00'
type: issue
status: closed
closed_at: '2017-10-15T18:12:20+00:00'
---

# Original Description
```
out_peers 10
2016-Jul-30 20:07:11.233075 Error: Unsuccessful
Error: Unsuccessful
out_peers 20
2016-Jul-30 20:07:14.697942 Error: Unsuccessful
Error: Unsuccessful
```

on both release and recent head (well, ringct testnet that I had up)


# Discussion History
## jedigras | 2016-09-08T01:02:29+00:00
Confirmed still gives an error.


## moneromooo-monero | 2017-10-02T19:33:25+00:00
It's just been gutted long ago, and nobody replaced it.


## moneromooo-monero | 2017-10-06T07:41:32+00:00
https://github.com/monero-project/monero/pull/2587

## moneromooo-monero | 2017-10-15T17:58:48+00:00
+resolved

# Action History
- Created by: Gingeropolous | 2016-07-31T00:07:48+00:00
- Closed at: 2017-10-15T18:12:20+00:00
