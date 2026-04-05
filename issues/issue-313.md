---
title: Split out the context cache from the consensus crate
source_url: https://github.com/Cuprate/cuprate/issues/313
author: Boog900
assignees:
- SyntheticBird45
labels:
- C-proposal
- E-hard
created_at: '2024-10-14T15:31:31+00:00'
updated_at: '2024-10-23T00:05:02+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
## What
The context cache is the service in `cuprate-consensus` that caches data from the database, this issue is for splitting it into a separate crate. 

## Why

We should pass in the data needed to verify a tx/block we shouldn't hold the context service in the verifiers. Splitting it into a separate crate makes this clearer.



# Discussion History
## hinto-janai | 2024-10-22T18:34:48+00:00
@Boog900 @SyntheticBird45 is this closed by #318?

## SyntheticBird45 | 2024-10-22T18:55:41+00:00
@hinto-janai As far as I understand it, there is a still second part to be achieved regarding the **Why** section

## Boog900 | 2024-10-23T00:05:01+00:00
The crate should be completed separated, `cuprate-consensus` shouldn't depend on the context crate 

# Action History
- Created by: Boog900 | 2024-10-14T15:31:31+00:00
