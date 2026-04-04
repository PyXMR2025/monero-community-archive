---
title: node thinks its syncing so it won't allow new peer to connect, but node is
  reporting 100%
source_url: https://github.com/monero-project/monero/issues/5836
author: Gingeropolous
assignees: []
labels: []
created_at: '2019-08-21T01:53:45+00:00'
updated_at: '2019-08-21T13:52:59+00:00'
type: issue
status: closed
closed_at: '2019-08-21T13:52:58+00:00'
---

# Original Description
```2019-08-21 01:45:39.407 D  connection type P2P 192.168.1.38:28080 <--> 192.168.1.194:46462 (via 192.168.1.194:46462)
2019-08-21 01:45:39.411 D [192.168.1.194:46462 INC] LEVIN_PACKET_RECEIVED. [len=293, flags1, r?=1, cmd = 1001, v=1
2019-08-21 01:45:39.411 D block <48ca7cd3c8de5b6a4d53d2861fbdaedca141553559f9be9520068053cda8430b> found in main chain
2019-08-21 01:45:39.411 I [192.168.1.194:46462 INC] peer is not ahead of us and we're syncing, disconnecting
2019-08-21 01:45:39.411 W [192.168.1.194:46462 INC] COMMAND_HANDSHAKE came, but process_payload_sync_data returned false, dropping connection.
2019-08-21 01:45:39.412 I [192.168.1.194:46462 INC] [0] state: closed in state before_handshake
2019-08-21 01:45:39.412 I [192.168.1.194:46462 78d0ebbf-2aae-4653-be33-1151cc2c3811 INC] CLOSE CONNECTION
2019-08-21 01:45:39.412 D Destructing connection #198 to 192.168.1.194
2019-08-21 01:45:39.427 D handle_accept
```

on master with  5549 and 5813

# Discussion History
## xiphon | 2019-08-21T02:06:18+00:00
#5815 

## Gingeropolous | 2019-08-21T13:52:58+00:00
yep, resolved. thanks. 

# Action History
- Created by: Gingeropolous | 2019-08-21T01:53:45+00:00
- Closed at: 2019-08-21T13:52:58+00:00
