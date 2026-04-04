---
title: Multisig wallets are not backwards compatible
source_url: https://github.com/monero-project/monero/issues/8541
author: tmoravec
assignees: []
labels: []
created_at: '2022-08-30T13:45:26+00:00'
updated_at: '2024-01-03T05:02:14+00:00'
type: issue
status: closed
closed_at: '2024-01-03T05:02:14+00:00'
---

# Original Description
As far as I can tell, this means funds in multisig wallets are inaccessible.

Steps to reproduce:

1. Create multisig wallets in `v0.17.3.2` software. I tried with 2/3 but that's presumably irrelevant.
2. Open the wallets in `v0.18.1.0`.
3. Run `set enable-multisig-experimental 1`.
4. Run `export_multisig_info msiginfo.bin`.
5. Observe error: `Error: This multisig wallet is not yet finalized`.

If I have any funds in a multisig wallet created with prior versions of the software, the funds are inaccessible. There's a backup way: export the multisig seed and import it in a new wallet created with new software. But that doesn't work either: https://github.com/monero-project/monero/issues/8537

# Discussion History
## UkoeHB | 2022-09-08T18:49:22+00:00
Need this PR: https://github.com/monero-project/monero/pull/8329

## selsta | 2024-01-03T05:02:14+00:00
Should be solved with #8329 merged.

# Action History
- Created by: tmoravec | 2022-08-30T13:45:26+00:00
- Closed at: 2024-01-03T05:02:14+00:00
