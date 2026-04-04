---
title: ZMQ Crash
source_url: https://github.com/monero-project/monero/issues/8911
author: SnAFKe
assignees: []
labels:
- pending review
created_at: '2023-06-19T13:54:11+00:00'
updated_at: '2025-12-28T23:33:24+00:00'
type: issue
status: closed
closed_at: '2025-12-28T23:33:24+00:00'
---

# Original Description
I'm unable to fix this issue and not sure there are any real solution for this issue because got me crazy.

I tried everything possible solution i find here.

- Close port to public and only access specify IP (remote node)
- Run as local
- I apply vtnerd patch
- I apply BotoX patch
- I don't think this solve this issue but i active Hugepages

I still i got random "Unable to send ZMQ/Pub - ZMQ server destroyed" error.

I'm running v0.18.2.2 release from official binary or building from source in ARM64 system with 12GB RAM 

# Discussion History
## selsta | 2023-06-19T14:01:51+00:00
Can you also share your config?

## SnAFKe | 2023-06-19T14:15:50+00:00
```monerod --rpc-bind-ip 172.16.20.3 --zmq-rpc-bind-ip 172.16.20.3 --zmq-pub=tcp://172.16.20.3:18083 --detach --confirm-external-bind --restricted-rpc --rpc-login user:pass --prune-blockchain --block-notify '/bin/bash /home/monero/block_notify.sh' --enable-dns-blocklist```

## B15Hi | 2023-11-12T15:27:49+00:00
try taking out "=" in "--zmq-pub=tcp://172.16.20.3:18083"

## selsta | 2025-12-28T23:33:21+00:00
This has been resolved in recent versions.

# Action History
- Created by: SnAFKe | 2023-06-19T13:54:11+00:00
- Closed at: 2025-12-28T23:33:24+00:00
