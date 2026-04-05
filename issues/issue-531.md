---
title: Better fast sync
source_url: https://github.com/Cuprate/cuprate/issues/531
author: Boog900
assignees: []
labels:
- A-p2p
- A-storage
- C-proposal
- E-hard
- A-binaries
created_at: '2025-08-23T14:46:40+00:00'
updated_at: '2025-10-01T18:49:38+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
## What
We could improve fast sync with a better block downloader & filling the DB in stages. 

## Why
More speed 🚀 

## Where

P2P block downloader, blockchain database, cuprated.

## How

- [ ] Block downloader: allow the user to specify if you want the blocks returned in order (for fast sync we don't need them in order)
- [ ] Database: Allow writing blocks out of order, some data needs previous blocks so once fast sync is done we need to fill in the parts of the DB that we couldn't fill in while syncing 
- [ ] Cuprated: For fast sync write blocks to DB in any order, when done fast syncing call the function on the DB that fills in the missing data.



# Discussion History
## SyntheticBird45 | 2025-08-23T19:57:50+00:00
<img width="483" height="620" alt="Image" src="https://github.com/user-attachments/assets/56a6556e-4437-4625-b550-365f2f26e4a8" />

## hinto-janai | 2025-10-01T18:43:40+00:00
IMO (fast-)sync is already more than fast enough, is the implementation time and added complexity for this worth it?

## Boog900 | 2025-10-01T18:49:38+00:00
this should get syncing to like 30 mins on 1 Gbps internet, I do think it is worth it but it isn't a priority atm 

# Action History
- Created by: Boog900 | 2025-08-23T14:46:40+00:00
