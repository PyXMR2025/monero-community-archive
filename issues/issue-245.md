---
title: Lookup table for calculating amount commitments
source_url: https://github.com/Cuprate/cuprate/issues/245
author: Boog900
assignees:
- SyntheticBird45
labels:
- A-storage
- C-proposal
- E-easy
- I-perf
- P-medium
- E-help-wanted
created_at: '2024-08-06T01:19:31+00:00'
updated_at: '2024-10-24T21:10:34+00:00'
type: issue
status: closed
closed_at: '2024-10-24T21:10:34+00:00'
---

# Original Description
## What

When retrieving pre-RCT outputs from the DB we need to calculate an amount commitment for use in RCT rings, this is currently done manually:

https://github.com/Cuprate/cuprate/blob/27767690ca7d7c5b44172a857581f08c728a740d/storage/blockchain/src/ops/output.rs#L158-L160

Also when adding V2 miner txs:

https://github.com/Cuprate/cuprate/blob/27767690ca7d7c5b44172a857581f08c728a740d/storage/blockchain/src/ops/tx.rs#L123-L129

This issue is for creating a lookup table for common amounts (the validly decomposed amounts).

## Why

Calculating commitments is slower than using a look up table.

## How

I did this in our test sync branch:

https://github.com/Cuprate/cuprate/blob/1eaf32bee956b66591f1537201c16969d5ec8696/helper/src/commitment.rs#L55-L62

However performance tests should be conducted to see if the slow path (line 60) is actually faster than our current method 


# Discussion History
## willco-1 | 2024-09-06T19:59:41+00:00
I'd like to take a shot at this if that's okay

## Boog900 | 2024-09-06T21:05:21+00:00
We currently have someone working on this sorry, #178 is slightly larger but currently has no one working on it, if that interests you?


## willco-1 | 2024-09-06T23:23:31+00:00
I’d probably need a little help on this one but feel free to assign it to me and i’ll take a shot at it! cheers. On Sep 6, 2024, at 17:05, Boog900 ***@***.***> wrote:﻿
We currently have someone working on this sorry, #178 is slightly larger but currently has no one working on it, if that interests you?

—Reply to this email directly, view it on GitHub, or unsubscribe.You are receiving this because you commented.Message ID: ***@***.***>

## Boog900 | 2024-09-07T13:46:14+00:00
Nice, you will have to comment on the issue for me to assign it. You are welcome to join our matrix server: https://matrix.to/#/#cuprate:monero.social, out of the 4 tasks listed in #178  `Persist banned peers` would _probably_ be the easiest to start on.

# Action History
- Created by: Boog900 | 2024-08-06T01:19:31+00:00
- Closed at: 2024-10-24T21:10:34+00:00
