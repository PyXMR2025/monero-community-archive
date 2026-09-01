---
title: '[Collaboration] Post-quantum signatures in a UTXO PoW chain — seeking review
  / co-author'
source_url: https://github.com/monero-project/research-lab/issues/163
author: ricardocbernardi
assignees: []
labels: []
created_at: '2026-09-01T23:26:19+00:00'
updated_at: '2026-09-01T23:26:19+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi MRL,

I run BrainX, an experimental UTXO + PoW chain (devnet, no economic value). I'm scoping a research contribution on integrating post-quantum signatures (ML-DSA / SLH-DSA, FIPS 204/205) into a Bitcoin-style PoW chain: PQ-aware addresses, UTXO-set migration without a trusted party, and witness/DoS limits derived from benchmarks. Not new crypto — the work is the integration, the economics and the migration.

Already built: a reference implementation (JavaScript = consensus, Rust parity in progress), an SLH-DSA-SHA2-128s wallet, real-GPU proof-of-work evidence, and a DoS benchmark harness (SLH-DSA-128s witness ~10.6 KB, verification ~2.2 ms median).

Looking for: anyone willing to review the approach, or a researcher interested in co-authoring the security analysis / whitepaper. This community understands PoW and applied crypto better than anyone.

A 2-page proposal and a technical report are ready to share. Happy to discuss here.

Thanks — Ricardo

# Discussion History
# Action History
- Created by: ricardocbernardi | 2026-09-01T23:26:19+00:00
