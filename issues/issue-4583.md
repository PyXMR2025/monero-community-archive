---
title: Make daemon start timeout configurable
source_url: https://github.com/monero-project/monero-gui/issues/4583
author: ab-c-d
assignees: []
labels: []
created_at: '2026-04-29T09:33:47+00:00'
updated_at: '2026-04-29T12:09:40+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
https://github.com/monero-project/monero-gui/blob/1216e07c471fa2a7c46582dfcbe1070a211303ee/src/daemon/DaemonManager.cpp#L48

Why make it hard-coded? The daemon takes 16 minutes to start on my external SSD.

# Discussion History
## selsta | 2026-04-29T10:20:06+00:00
That sounds like a bug, even if you are not synced it should not take more than 5-10 seconds.

## ab-c-d | 2026-04-29T11:59:28+00:00
What bug? Here is the log I got:
```
2026-04-29 09:13:31.337 I Monero 'Fluorine Fermi' (v0.18.4.4-release)
2026-04-29 09:13:31.337 I Initializing cryptonote protocol...
2026-04-29 09:13:31.337 I Cryptonote protocol initialized OK
2026-04-29 09:13:31.337 I Initializing core...
2026-04-29 09:13:31.339 I Loading blockchain from folder D:\bitmonero\lmdb ...
2026-04-29 09:29:02.467 I Loading checkpoints
2026-04-29 09:29:02.481 I Core initialized OK
2026-04-29 09:29:02.481 I Initializing p2p server...
```

## nahuhh | 2026-04-29T12:09:28+00:00
Run with log lvl 2

`--log-level 2`

# Action History
- Created by: ab-c-d | 2026-04-29T09:33:47+00:00
