---
title: Improve syncer startup
source_url: https://github.com/Cuprate/cuprate/issues/532
author: Boog900
assignees: []
labels:
- A-p2p
- C-optimization
- C-proposal
- E-medium
- A-binaries
created_at: '2025-08-23T14:52:57+00:00'
updated_at: '2026-03-15T19:44:49+00:00'
type: issue
status: closed
closed_at: '2026-03-15T19:44:49+00:00'
---

# Original Description

## What
Currently we check every 30s if we are synced, this was a hacky way of doing it which was never meant to stick. Instead we should have a way of telling the syncer if we are behind. 

## Why
Qubic recently caused a lot of re orgs, most of these blocks were passed around by syncing not through block notifications, needing to wait an extra 30s to sync blocks is a lot of wasted time for anyone who uses cuprated to mine. 

## Where
Syncer, p2p.

## How
A channel to wake the syncer if we are behind? 


# Discussion History
# Action History
- Created by: Boog900 | 2025-08-23T14:52:57+00:00
- Closed at: 2026-03-15T19:44:49+00:00
