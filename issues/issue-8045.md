---
title: Monero wallet RPC callback on incoming transaction
source_url: https://github.com/monero-project/monero/issues/8045
author: ob45
assignees: []
labels: []
created_at: '2021-11-05T14:46:30+00:00'
updated_at: '2022-02-18T23:32:17+00:00'
type: issue
status: closed
closed_at: '2022-02-18T23:32:17+00:00'
---

# Original Description
Hello

Is there a way to get notified about an incoming transaction?
I'm currently working on a node.js application and I'd like to validate transactions in an automated way. (mainly checking if the incoming transaction has the right amount of XMR etc.)



# Discussion History
## selsta | 2021-11-05T18:21:31+00:00
```
  --tx-notify arg                       Run a program for each new incoming 
                                        transaction, '%s' will be replaced by 
                                        the transaction hash
```

There is also ZMQ but that's more advanced: https://github.com/monero-project/monero/blob/master/docs/ZMQ.md

# Action History
- Created by: ob45 | 2021-11-05T14:46:30+00:00
- Closed at: 2022-02-18T23:32:17+00:00
