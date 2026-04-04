---
title: Wallet corruption while storing
source_url: https://github.com/monero-project/monero/issues/9332
author: MrCyjaneK
assignees: []
labels:
- bug
- wallet
created_at: '2024-05-15T15:40:31+00:00'
updated_at: '2025-07-23T19:35:17+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Steps to reproduce:

1. restore a wallet
2. start a refresh
3. while syncing call store() method
4. wallet should crash, if it didn't repeat step 3

expected results: 
- wallet not crashing and wallet cache getting updated or
- wallet not crashing and store method being ignored or
- wallet crashing and cache file not getting corrupted


With the help of tobtoht I was able to figure a way around this bug by using the following patch:

https://git.mrcyjanek.net/mrcyjanek/monero_c/src/branch/rewrite-wip/patches/monero/0011-store-crash-fix.patch

it depends on the LOCK_REFRESH macro from background sync pr (https://github.com/monero-project/monero/pull/8617/files#diff-fcae134993cca2b6f1e887a60638f226ab00165e30bd4d326c17f0a58e11871fR57-R68)

also note that the issue exist in forked version of monero, with couple of patches applied, that's the reason behind this report being an issue and not a PR. If the patch looks about right I'll make this a PR

NOTE: technically you can still cause crash with this fix, when you try to modify the wallet state while storing.

# Discussion History
## binarybaron | 2025-07-23T19:19:03+00:00
Was this ever fixed upstream?

## x64x2 | 2025-07-23T19:35:17+00:00
> Was this ever fixed upstream?

it wasn't on the priority list.

# Action History
- Created by: MrCyjaneK | 2024-05-15T15:40:31+00:00
