---
title: 'Tests: node_server.bind_same_p2p_port failing with 10% probability'
source_url: https://github.com/monero-project/monero/issues/7645
author: mj-xmr
assignees: []
labels: []
created_at: '2021-04-04T20:06:52+00:00'
updated_at: '2021-04-06T17:25:09+00:00'
type: issue
status: closed
closed_at: '2021-04-06T17:25:09+00:00'
---

# Original Description
In my recent scheduled runs, the Unit Test `node_server.bind_same_p2p_port` was failing with 10% probability. Below are the logs:

```
[----------] 1 test from node_server
[ RUN      ] node_server.bind_same_p2p_port
/home/runner/work/monero/monero/tests/unit_tests/node_server.cpp:307: Failure
Value of: init(node, port)
  Actual: false
Expected: true
[  FAILED  ] node_server.bind_same_p2p_port (25 ms)
```

The test can be considered unstable for now. I will soon run more in-depth tests to learn what the real cause is.

# Discussion History
## moneromooo-monero | 2021-04-05T11:34:35+00:00
Anything interesting with log level 2 (or even 3) ?

## mj-xmr | 2021-04-05T15:53:32+00:00
> Anything interesting with log level 2 (or even 3) ?

We checked with `wfaressuissia` but found nothing interesting.

# Action History
- Created by: mj-xmr | 2021-04-04T20:06:52+00:00
- Closed at: 2021-04-06T17:25:09+00:00
