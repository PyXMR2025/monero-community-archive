---
title: Port numbers for `cuprated`
source_url: https://github.com/Cuprate/cuprate/issues/269
author: hinto-janai
assignees: []
labels:
- C-discussion
created_at: '2024-09-05T01:15:53+00:00'
updated_at: '2025-08-05T18:50:17+00:00'
type: issue
status: closed
closed_at: '2025-08-05T18:50:17+00:00'
---

# Original Description
## What
Which port numbers will `cuprated` use by default?

## The standard
`monerod` uses the following ports as convention/defaults:

| Port  | Purpose |
|-------|---------|
| [18080](https://github.com/monero-project/monero/blob/a1dc85c5373a30f14aaf7dcfdd95f5a7375d3623/src/cryptonote_config.h#L226) | P2P traffic
| [18081](https://github.com/monero-project/monero/blob/a1dc85c5373a30f14aaf7dcfdd95f5a7375d3623/src/cryptonote_config.h#L227) | Non-restricted RPC
| [18082](https://github.com/monero-project/monero/blob/a1dc85c5373a30f14aaf7dcfdd95f5a7375d3623/src/cryptonote_config.h#L228) (but sometimes on 18083) | ZMQ
| 18083 (convention) | Anonymity network
| 18089 (convention) | Restricted RPC

[2808* is used for for testnet](https://github.com/monero-project/monero/blob/a1dc85c5373a30f14aaf7dcfdd95f5a7375d3623/src/cryptonote_config.h#L269), [3808* is used for stagenet](https://github.com/monero-project/monero/blob/a1dc85c5373a30f14aaf7dcfdd95f5a7375d3623/src/cryptonote_config.h#L284).

## Considerations
- 4808* is tempting but may clash with `monerod` in the future
- [Should be above 1024](https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers)
- Should not be a common test port, i.e. 8000, 8080, 7777
- Should not be a port used by another common program, i.e. 9001, 8333

# Discussion History
## hinto-janai | 2025-03-06T17:07:55+00:00
As of https://github.com/Cuprate/cuprate/commit/2dc258e4c8388efcef78ed4f6cae19cf59520f64, the only ports opened are P2P, which defaults to 0, which eventually picks a random available port. One of the cons of using the same ports is testing `monerod` <-> `cuprated` is slightly more cumbersome, current CI would fail. Running both `monerod` and `cuprated` on the same machine would also fail by default.

This can be settled after `v0.0.1`.

## Boog900 | 2025-03-06T21:46:01+00:00
ah randomly selecting a port was not supposed to happen, setting `0` should disable the inbound listener, seems like I missed that check though.

## hinto-janai | 2025-08-05T18:50:17+00:00
https://github.com/monero-project/meta/issues/1246#issuecomment-3156226055

> the port numbers for the existing interfaces will be the same

# Action History
- Created by: hinto-janai | 2024-09-05T01:15:53+00:00
- Closed at: 2025-08-05T18:50:17+00:00
