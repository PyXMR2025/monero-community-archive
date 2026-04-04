---
title: Could not connect to daemon
source_url: https://github.com/monero-project/monero/issues/2673
author: lukaisailovic
assignees: []
labels: []
created_at: '2017-10-17T18:23:42+00:00'
updated_at: '2017-10-17T18:53:26+00:00'
type: issue
status: closed
closed_at: '2017-10-17T18:53:26+00:00'
---

# Original Description
I'm starting daemon in testnet mode (sync is finished) and now I'm trying to connect to it but I get this error:
```Failed to connect to localhost port 18082: Connection refused```
is there any other option or setting I should have specified in order to get it to work ? (i've tried to connect to ```http://127.0.0.1:18082/json_rpc``` and ```http://localhost:18082/json_rpc```). Whatever I do daemon refuses my connection.

# Discussion History
## lukaisailovic | 2017-10-17T18:53:25+00:00
SOLUTION: Testnet port is **28081**

# Action History
- Created by: lukaisailovic | 2017-10-17T18:23:42+00:00
- Closed at: 2017-10-17T18:53:26+00:00
