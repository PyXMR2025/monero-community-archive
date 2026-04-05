---
title: Node opens connections only to close them without sending any data
source_url: https://github.com/seraphis-migration/monero/issues/276
author: ComputeryPony
assignees: []
labels: []
created_at: '2025-12-28T06:01:43+00:00'
updated_at: '2026-01-01T22:30:43+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I happen to be doing a pcap of my node when starting it up and noticed that I saw it establish a TCP connection to a node, only for it to wait 10 seconds without sending a handshake and then proceed to close the connection.
I checked the pcap and found other connections where monerod did this however, in those cases the remote side happened to close the connection much quicker making it harder to notice. I only happened to notice this instance since it happened to be the first connection made and it didn't try to connect to another node till after it had closed the first connection, resulting in about an 18 second delay at startup.

Running on commit: a3f5c7a28688d5a548749fed55b404f37e70e402

# Discussion History
# Action History
- Created by: ComputeryPony | 2025-12-28T06:01:43+00:00
