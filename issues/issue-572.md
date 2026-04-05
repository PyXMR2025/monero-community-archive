---
title: Cuprate reorg failed
source_url: https://github.com/Cuprate/cuprate/issues/572
author: Boog900
assignees: []
labels:
- C-bug
- P-critical
created_at: '2025-12-18T20:50:31+00:00'
updated_at: '2025-12-19T18:22:38+00:00'
type: issue
status: closed
closed_at: '2025-12-19T18:22:38+00:00'
---

# Original Description
While running Cuprate my node first reorged successfully then the original chain overtook the chain we reorged to but cuprate failed to reorg back.

# Discussion History
## Boog900 | 2025-12-18T20:51:31+00:00
This was on the wip branch, but I don't _think_ I changed anything that would cause this scenario to happen.

## hinto-janai | 2025-12-18T22:18:34+00:00
Did not seem to happen for my `cuprated v0.0.8` running since release, latest block is on the correct chain `3568489` -> `961e945b9e4ee2f42af7f9128cfa97cafd6c458225fbae46c57326857fce88a4`.

## Boog900 | 2025-12-19T18:22:38+00:00
Ah I accidentally removed the update for the common ancestor in the alt chains database, added a test for this so it can't happen again  

# Action History
- Created by: Boog900 | 2025-12-18T20:50:31+00:00
- Closed at: 2025-12-19T18:22:38+00:00
