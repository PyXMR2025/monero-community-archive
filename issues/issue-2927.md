---
title: adding priority node with authentication not allowed
source_url: https://github.com/monero-project/monero/issues/2927
author: razorman8669
assignees: []
labels: []
created_at: '2017-12-15T06:31:53+00:00'
updated_at: '2017-12-17T18:26:20+00:00'
type: issue
status: closed
closed_at: '2017-12-17T18:26:20+00:00'
---

# Original Description
I'm trying to add a priority node upon launching the monero daemon like so:
```./monerod --add-priority-node un:pw@111.222.333.444:18089```  however, this results in the daemon quiting upon startup with the log message ```Failed to parse address from string: un:pw@111.222.333.444:18089```

is this just something unsupported?

# Discussion History
## moneromooo-monero | 2017-12-15T09:40:33+00:00
Indeed. Use a tunnel if you want to do anything like this.

## razorman8669 | 2017-12-17T18:26:20+00:00
I had it all wrong..  I was trying to add a priority node via the RPC port and not the P2P port.  Once I opened the P2P port I was able to connect just fine.  no need for authentication

# Action History
- Created by: razorman8669 | 2017-12-15T06:31:53+00:00
- Closed at: 2017-12-17T18:26:20+00:00
