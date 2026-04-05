---
title: 'Bug: consensus failure while validating block''s n tree layers or tree root'
source_url: https://github.com/seraphis-migration/monero/issues/102
author: jeffro256
assignees: []
labels: []
created_at: '2025-09-09T18:51:48+00:00'
updated_at: '2025-09-11T21:11:16+00:00'
type: issue
status: closed
closed_at: '2025-09-11T21:11:16+00:00'
---

# Original Description
## Issue

On a local testnet, during block sync, block validation fails with error: 

```
Block with id: <BLOCKID> used incorrect FCMP++ n tree layers or tree root
```

The other daemon is running honestly and doesn't perceive this to be the case. One of them is wrong and a netsplit is caused.

## Reproducing

1. Run a local testnet as described in https://github.com/seraphis-migration/monero/issues/47
2. Mine up to height 2956
3. Restart one daemon and attempt to re-sync from other
4. Aforementioned error occurs

The restarted daemon gets stuck at height 1700 (before the very first v17 / FCMP++ block).

# Discussion History
## j-berman | 2025-09-11T01:30:07+00:00
I'm pretty confident this was caused by merging #93, since it modified hash to point (and generators) used for FCMP++, which would break compatibility across daemons running old and new code. I can repro by trying to sync a daemon using latest code, pointing to a daemon running old code. And I can sync pointing to a daemon running old code by reverting that PR.

If definitely the case, I figure the optimal solution would be to scrap chains running the old code, and use the latest going forward.

## j-berman | 2025-09-11T17:57:23+00:00
Confirmed #93 caused this, and the solution is to scrap old and run new.

_______

@kayabaNerve also pointed out the exact spots which caused the break to tree building before FCMP++/Carrot outputs entered the tree:

BEFORE: https://github.com/j-berman/fcmp-plus-plus/blob/2b17c6cfdbdb6711004c5b37eb4fbd37d11332c4/networks/monero/ringct/fcmp%2B%2B/src/lib.rs#L122

AFTER: https://github.com/monero-oxide/monero-oxide/blob/b76cb2b75fae56f233d7bc267f381c4de0d4b1cb/monero-oxide/generators/src/lib.rs#L184

`hash_grow` uses the helios/selene generators here:

https://github.com/seraphis-migration/monero/blob/64190feb26151e186b86c27bcd7c08e2ca09db6b/src/fcmp_pp/fcmp_pp_rust/src/lib.rs#L272

https://github.com/seraphis-migration/monero/blob/64190feb26151e186b86c27bcd7c08e2ca09db6b/src/fcmp_pp/fcmp_pp_rust/src/lib.rs#L303

## jeffro256 | 2025-09-11T21:10:45+00:00
I think that this might have been it, since I saved the `monerod` directories. 

## jeffro256 | 2025-09-11T21:11:16+00:00
I am having trouble reproducing now, so I'm going to close this as resolved unless it comes up again. 

# Action History
- Created by: jeffro256 | 2025-09-09T18:51:48+00:00
- Closed at: 2025-09-11T21:11:16+00:00
