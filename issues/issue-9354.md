---
title: Scan_tx stucks on newer versions
source_url: https://github.com/monero-project/monero/issues/9354
author: ghost
assignees: []
labels:
- wallet
created_at: '2024-06-06T10:40:00+00:00'
updated_at: '2025-01-18T02:34:31+00:00'
type: issue
status: closed
closed_at: '2025-01-18T02:34:31+00:00'
---

# Original Description
It seems because of [this](https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/wallet/wallet2.cpp#L1925-L1927) todo, Scan_tx gets stuck when trying to scan transactions before syncing wallet.

It is related to woodser/monero-ts#212.

# Discussion History
## woodser | 2024-06-06T13:35:31+00:00
Essentially the issue is that calling `scan_tx` also calls `refresh` which syncs the entire blockchain starting from the tx height.

So this issue is requesting to scan the minimum necessary.

## ghost | 2024-06-06T15:50:46+00:00
@0xFFFC0000 Excuse me, but Is this considered a "question"? because literally `scan_tx` takes 10 (or more) minutes to run.

## 0xFFFC0000 | 2024-06-06T16:16:39+00:00
@sharifzadesina thank you for reporting this. We will take a look into this. 

1. This happened after specific updates? 
2. Have you tried on other systems with other configurations too, and problem was still present?


In the meantime it appears to me @woodser has explained the actual reason. 

## selsta | 2024-06-06T16:23:53+00:00
Issue got introduced here: https://github.com/monero-project/monero/pull/8566

## j-berman | 2024-06-06T17:41:29+00:00
The expected behavior:

- user restores a wallet using current chain height as restore height
- user calls `scan_tx` with an earlier tx
- `scan_tx` returns immediately

The problem: [`scan_tx` calls `refresh()`](https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/wallet/wallet2.cpp#L1925-L1927), which can take a long time to complete even if the wallet's restore height is set to the current height.

This needs confirmation (repro with the RPC and observe the logs), but I believe refresh is slow to complete even when setting restore height to current height because it's taking a while to get all block hashes from the chain starting from genesis.

Assuming this is the general issue (long-running refresh in scan_tx), the simplest fix for this is probably to remove the call to refresh in `scan_tx`, which means the wallet won't have the latest chain state upon completion of `scan_tx`. This is probably ok and expected.

The more involved fix is to refactor `fast_refresh` and scanning to not need all block hashes from the chain, and to only need hashes starting from the wallet's restore height. The Seraphis lib does this refactoring already, which we're in the process of migrating toward, so I would lean towards the simpler fix for now.

## ghost | 2024-06-06T18:16:36+00:00
@j-berman Exactly, Thank you.

Even when I set restore height to a higher value, it takes too long to finish.

## ghost | 2024-06-26T15:50:20+00:00
Bump! any update on this?

## j-berman | 2024-06-26T15:56:38+00:00
Will fix by end of this week

## ghost | 2024-06-26T17:28:17+00:00
@j-berman Thank you, I wish I could help, I just don't know C++, 

# Action History
- Created by: ghost | 2024-06-06T10:40:00+00:00
- Closed at: 2025-01-18T02:34:31+00:00
