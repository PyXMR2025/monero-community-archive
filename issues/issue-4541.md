---
title: p2pool permission issues with /usr/bin/stats/
source_url: https://github.com/monero-project/monero-gui/issues/4541
author: AllergicMushroom
assignees: []
labels: []
created_at: '2025-12-09T21:00:08+00:00'
updated_at: '2025-12-20T18:02:20+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
When launching P2Pool via monero-gui, I'm getting the following errors:

```
P2Pool can't continue execution: panic at /usr/src/debug/p2pool/p2pool/src/p2pool_api.cpp:51
2025-12-09 20:57:58.2653 P2Pool API path /usr/bin/stats/ doesn't exist
2025-12-09 20:57:58.2653 Log stopped
```

I think this issue is very similar with #4108 . I've checked for recent issues with p2pool permission issues, but I don't see an open one with the same problem.

The versions are:
- monero-gui 0.18.4.3-release (Qt 5.15.18)
- p2pool 4.12

I've also tried adding `--data-dir ~/.p2pool`, but this doesn't seem to affect p2pool whatsoever. Note that this flag works when launching p2pool via terminal emulator.

Also, on a side note, I believe at some point we chould choose what pool to mine for? Has this setting disappeared from the GUI?

# Discussion History
## selsta | 2025-12-19T23:54:18+00:00
How did you install monero-gui, or did you compile it yourself?

> Also, on a side note, I believe at some point we chould choose what pool to mine for? Has this setting disappeared from the GUI?

No, P2Pool itself is the "pool".

## AllergicMushroom | 2025-12-20T08:24:43+00:00
I installed it with yay from the AUR.

## selsta | 2025-12-20T10:08:21+00:00
p2pool integration does not work well together with package managers unfortunately

See the discussion here https://github.com/monero-project/monero-gui/pull/3926

## AllergicMushroom | 2025-12-20T10:26:51+00:00
I don't understand why, even after reading #3926 .

My p2pool seems to launch, but its data directory is /usr/bin/, which is obviously bad.

I believe we should examine why `--data-dir ~/.p2pool` does not work.

## FabriLluvia | 2025-12-20T18:02:20+00:00
Maybe, meanwhile, you should use XMRig? You can choose pool or do solo-mining.
Wizard for configuration: https://xmrig.com/wizard

# Action History
- Created by: AllergicMushroom | 2025-12-09T21:00:08+00:00
