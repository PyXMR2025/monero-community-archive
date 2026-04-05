---
title: 'Windows fix: do not fail on `git clone` if repo already exists'
source_url: https://github.com/MrCyjaneK/monero_c/pull/1
author: sneurlax
assignees: []
labels: []
created_at: '2024-04-12T16:52:28+00:00'
updated_at: '2024-04-12T17:03:24+00:00'
type: pull_request
status: merged
closed_at: '2024-04-12T17:03:24+00:00'
merged_at: '2024-04-12T17:03:24+00:00'
---

# Original Description
build_single.sh will fail on Windows (WSL2) due to `git clone` if we already did a `git submodule update --init --recursive`.  These script changes attempt to check whether the folder already exists, and if it does, attempts to checkout the appropriate branch/tag/commit.

# Discussion History
# Action History
- Created by: sneurlax | 2024-04-12T16:52:28+00:00
- Merged at: 2024-04-12T17:03:24+00:00
