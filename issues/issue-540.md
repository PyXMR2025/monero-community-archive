---
title: Hide certain data in logs
source_url: https://github.com/Cuprate/cuprate/issues/540
author: Boog900
assignees: []
labels:
- C-request
created_at: '2025-08-29T17:39:33+00:00'
updated_at: '2025-08-29T19:13:22+00:00'
type: issue
status: open
closed_at: null
---

# Original Description

## Feature
Hide certain data from the log file, like stem tx hashes or onion addresses, with an option to show these details. 

## Why
To prevent the log file from being a target.

## Additional context
arti has a crate for this: https://docs.rs/safelog/latest/safelog/index.html

and some guideline for arti: https://tpo.pages.torproject.net/core/arti/contributing/for-developers/logging/


# Discussion History
## SyntheticBird45 | 2025-08-29T18:23:07+00:00
Interesting. May this behavior be gated behind a release cfg? Or will this be opt-in + flag/config line to disable

## Boog900 | 2025-08-29T19:13:22+00:00
making it opt in would be bad as most wont, it would be opt-out by config/command line yes 

# Action History
- Created by: Boog900 | 2025-08-29T17:39:33+00:00
