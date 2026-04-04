---
title: Default monerod configuration speedup
source_url: https://github.com/monero-project/monero/issues/9275
author: S5NC
assignees: []
labels:
- question
created_at: '2024-04-02T10:16:37+00:00'
updated_at: '2026-01-25T22:59:02+00:00'
type: issue
status: closed
closed_at: '2025-01-17T14:06:02+00:00'
---

# Original Description
Why are the default monerod configurations very low?
Download is limited to 8 MiB/s, upload is limited to 2 MiB/s, and the maximum number of peers to download from (in) is limited to 12.

Could we increase the default limits to 1024 MiB/s download, 1024 MiB/s upload, 512 in_peers, and 512 out_peers?
Torrenting software typically don't have artificial transfer speed limits and they manage fine. We should too.

./monerod --help shows
```
  --out-peers arg (=-1)                 set max number of out peers
  --in-peers arg (=-1)                  set max number of in peers
  --tos-flag arg (=-1)                  set TOS flag
  --limit-rate-up arg (=2048)           set limit-rate-up [kB/s]
  --limit-rate-down arg (=8192)         set limit-rate-down [kB/s]
  --limit-rate arg (=-1)                set limit-rate [kB/s]
```

These limits are all what is by default, except the `--out-peers arg (=-1)`, which is actually 12. Maybe this was changed, or perhaps 12 is a fallback value from an incorrect configuration. If you pass `-1` as any of the arguments, it doesn't set it to unlimited but retains the default (which may be a fallback).

Maybe you would also want to increase the default maximum number of connections per ip from 1 to 32 or remove the restriction completely, as this impacts users with shared ips (same network, large business, VPN, cloud provider) when there are a large number of monero users on the same network.

# Discussion History
## selsta | 2024-04-02T14:22:05+00:00
Increasing the number of out peers has an impact on privacy and network topology. We won't do any changes to it without corresponding research.

The bandwidth limits could be increased but as far as I know even during the recent spam attack the limit wasn't reached.

> Maybe you would also want to increase the default maximum number of connections per ip from 1 to 32 or remove the restriction completely

This makes it easier to sybil attack the network.

## S5NC | 2026-01-25T22:59:02+00:00
Increased 4x by #9770

# Action History
- Created by: S5NC | 2024-04-02T10:16:37+00:00
- Closed at: 2025-01-17T14:06:02+00:00
