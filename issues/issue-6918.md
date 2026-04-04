---
title: 'Error starting server: Failed to bind IPv4 (set to required)'
source_url: https://github.com/monero-project/monero/issues/6918
author: lh1008
assignees: []
labels: []
created_at: '2020-10-18T18:23:25+00:00'
updated_at: '2021-11-14T03:19:48+00:00'
type: issue
status: closed
closed_at: '2020-10-18T18:28:38+00:00'
---

# Original Description
Hello everyone,

I did what's suggested in https://www.reddit.com/r/Monero/comments/jdh5to/psa_a_bug_has_caused_some_nodes_to_get_stuck_on/ 

    git clone --recursive -b release-v0.17 https://github.com/monero-project/monero

    make

but I get the following error:

```
2020-10-18 18:18:33.947	I Monero 'Oxygen Orion' (v0.17.1.1-76cc82c29)
2020-10-18 18:18:33.947	I Initializing cryptonote protocol...
2020-10-18 18:18:33.947	I Cryptonote protocol initialized OK
2020-10-18 18:18:33.947	I Initializing core...
2020-10-18 18:18:33.947	I Loading blockchain from folder /home/siddha/.bitmonero/lmdb ...
2020-10-18 18:18:34.025	I Loading checkpoints
2020-10-18 18:18:34.026	I Core initialized OK
2020-10-18 18:18:34.026	I Initializing p2p server...
2020-10-18 18:18:34.036	F Error starting server: Failed to bind IPv4 (set to required)
2020-10-18 18:18:34.038	I Deinitializing core...
2020-10-18 18:18:34.044	I Stopping cryptonote protocol...
2020-10-18 18:18:34.044	I Cryptonote protocol stopped successfully
2020-10-18 18:18:34.044	E Exception in main! Failed to initialize p2p server.
```

# Discussion History
## lh1008 | 2020-10-18T18:28:38+00:00
Closing this issue, I had past version 0.17.0.1 running. Thank you for your support.

## sdzc | 2021-11-14T03:19:48+00:00
How to solve it

# Action History
- Created by: lh1008 | 2020-10-18T18:23:25+00:00
- Closed at: 2020-10-18T18:28:38+00:00
