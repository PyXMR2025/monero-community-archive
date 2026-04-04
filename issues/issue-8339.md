---
title: Can't create viewwallet on testnet
source_url: https://github.com/monero-project/monero/issues/8339
author: ghost
assignees: []
labels: []
created_at: '2022-05-17T12:59:31+00:00'
updated_at: '2022-05-17T13:11:22+00:00'
type: issue
status: closed
closed_at: '2022-05-17T13:11:22+00:00'
---

# Original Description
**Terminal:**

```
debian@vps:~/monero/build/Linux/master/release/bin$ ./monero-wallet-cli --generate-from-view-key viewwallet --log-level 2
This is the command line monero wallet. It needs to connect to a monero
daemon to work correctly.
WARNING: Do not reuse your Monero keys on another fork, UNLESS this fork has key reuse mitigations built in. Doing so will harm your privacy.

Monero 'Oxygen Orion' (v0.17.0.0-8349cfe4a)
Logging to ./monero-wallet-cli.log
Standard address: 9wog1AwLTJRKCMgs7ZbCZGVJa26eve3ZU4hpxTBYxpp8LGUMiioB1shjS5aibER2AvY8bpDRiNRw929FMpxmeeuy9vQnRH6
Error: failed to parse address
debian@vps:~/monero/build/Linux/master/release/bin$ 
```

**Monero-wallet-cli.log:**

https://paste.debian.net/1241153/

Says it needs to connect to a monero daemon to work correctly, but the daemon is running. Creating wallets and sending tx work fine. But creating view wallets does not work.

# Discussion History
# Action History
- Created by: ghost | 2022-05-17T12:59:31+00:00
- Closed at: 2022-05-17T13:11:22+00:00
