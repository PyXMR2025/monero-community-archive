---
title: Remove dead links
source_url: https://github.com/monero-project/monero-docs/issues/109
author: jermanuts
assignees: []
labels: []
created_at: '2024-12-19T13:08:49+00:00'
updated_at: '2026-07-26T23:22:56+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
link https://www.monerooutreach.org/stories/RandomX.html on https://docs.getmonero.org/proof-of-work/random-x/

link [CryptoNote Standard](https://cryptonote.org/cns/cns008.txt) on https://docs.getmonero.org/proof-of-work/cryptonight/#step-1-scratchpad-initialization

# Discussion History
## nahuhh | 2024-12-19T13:40:01+00:00
randomx will be fixed here https://github.com/monero-project/monero-docs/pull/47

## monerostar | 2026-07-26T23:22:55+00:00
Opened a partial fix: https://github.com/monero-project/monero-docs/pull/367

- **CNS008 / cryptonote.org** — still dead from here; PR points both CryptoNight references at the preserved laanwj gist mirror of `cns008.txt`.
- **Monero Outreach RandomX** — returns HTTP 200 again from this host today, so I left `random-x.md` alone. Broader RandomX page work remains in #47 as noted earlier.

# Action History
- Created by: jermanuts | 2024-12-19T13:08:49+00:00
