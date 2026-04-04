---
title: daemon can send duplicate transactions, causing disconnects
source_url: https://github.com/monero-project/monero/issues/9335
author: selsta
assignees:
- '0xFFFC0000'
labels:
- bug
- daemon
created_at: '2024-05-20T16:24:22+00:00'
updated_at: '2025-12-29T01:24:17+00:00'
type: issue
status: closed
closed_at: '2025-12-29T01:24:17+00:00'
---

# Original Description
Since #8916 peers that send duplicate transactions gets dropped. This usually isn't an issue, but when running a daemon with `--max-txpool-weight` it's possible that duplicate transactions can get into the fluff queue.

Quoting @Boog900 from https://github.com/monero-project/monero/issues/9317#issuecomment-2106216570

> If you receive a tx, add it to your fluff queue, drop the tx from the txpool, then receive it again, it is added to the fluff queue a second time. When the fluff timer fires we would then broadcast a message with the same tx twice causing the peer to disconnect.

Relevant code:

https://github.com/monero-project/monero/blob/c8214782fb2a769c57382a999eaf099691c836e7/src/cryptonote_protocol/levin_notify.cpp#L203-L207

# Discussion History
# Action History
- Created by: selsta | 2024-05-20T16:24:22+00:00
- Closed at: 2025-12-29T01:24:17+00:00
