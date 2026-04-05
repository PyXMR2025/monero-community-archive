---
title: Block downloader shuts down due to inner service error
source_url: https://github.com/Cuprate/cuprate/issues/431
author: hinto-janai
assignees: []
labels:
- C-bug
created_at: '2025-04-08T21:40:45+00:00'
updated_at: '2025-04-08T21:41:04+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
## Environment
- OS: Linux x64
- Cuprate: v0.0.1

## Bug
The block downloader stop signal:

https://github.com/Cuprate/cuprate/blob/3ef6a96d0470c08f5cec8b0a8ac4186964335ee1/binaries/cuprated/src/blockchain/syncer.rs#L80-L81

gets triggered upon inner service errors.

## Log
Snippet from around 2025-04-08 20:52, IPs are `REDACTED`.

```
DEBUG net{zone="ClearNet"}:connection{addr=REDACTED}: Sending message: [new fluffy block] to peer
DEBUG net{zone="ClearNet"}:connection{addr=REDACTED}: waiting for peer/client request.
DEBUG net{zone="ClearNet"}:connection{addr=REDACTED}: waiting for peer/client request.
DEBUG net{zone="ClearNet"}:connection{addr=REDACTED}: waiting for peer/client request.
DEBUG net{zone="ClearNet"}:connection{addr=REDACTED}: waiting for peer/client request.
DEBUG net{zone="ClearNet"}:connection{addr=REDACTED}: One or more key images in batch already spent.
DEBUG net{zone="ClearNet"}:connection{addr=REDACTED}: Connection task shutting down: inner service error: Transaction error: Key-image is already spent.
DEBUG net{zone="ClearNet"}:connection{addr=REDACTED}: Sending message: [new fluffy block] to peer
DEBUG net{zone="ClearNet"}:connection{addr=REDACTED}: waiting for peer/client request.
 INFO syncer: Received stop signal, stopping block downloader
DEBUG net{zone="ClearNet"}:connection{addr=REDACTED}: connection guard has shutdown, shutting down connection.
DEBUG net{zone="ClearNet"}:connection{addr=REDACTED}: Connection task shutting down: The connection was closed.
DEBUG timeout_monitor{addr=REDACTED}: Closing timeout monitor, connection disconnected.
DEBUG timeout_monitor{addr=REDACTED}: Closing timeout monitor, connection disconnected.
DEBUG net{zone="ClearNet"}:handle_free_permit: Permit available, making outbound connection.
DEBUG net{zone="ClearNet"}:handle_free_permit: Banning peer: REDACTED, for: 604800s
DEBUG net{zone="ClearNet"}:handle_free_permit: service.ready=true processing request
DEBUG net{zone="ClearNet"}:handle_free_permit:AddressBook: Retrieving random white peer
DEBUG net{zone="ClearNet"}:handle_free_permit:connect_to_outbound_peer: Connecting to peer: REDACTED
DEBUG net{zone="ClearNet"}:handle_free_permit: Permit available, making outbound connection.
DEBUG net{zone="ClearNet"}:handle_free_permit: service.ready=true processing request
DEBUG net{zone="ClearNet"}:handle_free_permit:AddressBook: Retrieving random gray peer
DEBUG net{zone="ClearNet"}:handle_free_permit:connect_to_outbound_peer: Connecting to peer: REDACTED
DEBUG net{zone="ClearNet"}:connection{addr=REDACTED}: Received peer message, command: TimedSync
DEBUG net{zone="ClearNet"}:connection{addr=REDACTED}: waiting for peer/client request.
DEBUG timeout_monitor{addr=REDACTED}:timed_sync: Received timed sync response, incoming peer list len: 0
DEBUG timeout_monitor{addr=REDACTED}: service.ready=true processing request
DEBUG timeout_monitor{addr=REDACTED}:AddressBook: Received new peer list, length: 0
DEBUG timeout_monitor{addr=REDACTED}:timed_sync: Sending timed sync to peer
DEBUG net{zone="ClearNet"}:connection{addr=REDACTED}: handling client request, id: TimedSync
DEBUG net{zone="ClearNet"}:connection{addr=REDACTED}: Sending message: [timed sync] to peer
DEBUG net{zone="ClearNet"}:connection{addr=REDACTED}: waiting for peer response.
```

Problematic line seems to be:
```
DEBUG net{zone="ClearNet"}:connection{addr=REDACTED}: Connection task shutting down: inner service error: Transaction error: Key-image is already spent.
```

# Discussion History
# Action History
- Created by: hinto-janai | 2025-04-08T21:40:45+00:00
