---
title: '`monerod` OOM after synced'
source_url: https://github.com/seraphis-migration/monero/issues/202
author: j-berman
assignees: []
labels: []
created_at: '2025-10-29T20:11:04+00:00'
updated_at: '2025-11-04T20:25:54+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
We've had a number of reports of OOM's after a daemon is synced.

@nahuhh raised that this was mainly observed during periods where the tx pool was large.

@boog900 raised suspicion this may be due to the inefficient tx relay relaying every tx to all connections, which tx relay v2 would help on.

Running with ASAN hasn't found any significant leaks.

# Discussion History
## j-berman | 2025-11-03T02:10:12+00:00
Using valgrind (which was a bit painful to set up with monerod, I'm going to share instructions on how to set it up for the future), I found that verifying 128-input proofs is taking ~1.2gb of RAM at peak. Running monerod with valgrind for a while, verification of high input txs seems to be a significant cause of high RAM usage. @kayabaNerve cut that down to 790mb with [this change](https://github.com/monero-oxide/monero-oxide/pull/39/commits/96eae33ed42c50b3ec8d1ca969c95c6e4d13a29f).

The investigation continues. I'll continue with identifying areas in verification using a lot of RAM. I will also look deeper into threaded batch verification as another plausible cause of OOM's. Presumably it would be ... split batch verification of potentially multiple 128-in txs across all threads and clearly that would eat up a lot of RAM. @kayabaNerve has suggested limiting each active verifying thread to 128 inputs max.

The reason I am/was not completely sold on tx relay being the only cause of high memory usage is because @SNeedlewoods reported OOM's with only 1 peer.

Good news that there doesn't seem to be any significant leaks in the FFI, #39 appears to have been effective.

## kayabaNerve | 2025-11-03T09:39:05+00:00
> has suggested limiting each active verifying thread to 128 inputs max.

'limiting all verifying threads to 128 inputs simultaneously at max'. 256 would also work, yet an unbounded n * 128 as the theoretical limit seems problematic.

Alternatively, use a threadpool for all proofs of < = 16 inputs and only kick large proofs to their own thread. This also increases the odds large proofs end up on a thread with other large proofs, as needed for their CRSs to batch.

## j-berman | 2025-11-04T20:03:11+00:00
@SNeedlewoods reported that running [this code](https://github.com/j-berman/monero/commits/fcmp%2B%2B-limit-verify-mem-usage/) is preventing OOM's during sync on their machine with 2 threads and 8GB of RAM, but that sync is roughly 2-3x slower (ballpark observation, could be that blocks are larger/smaller). That perf hit doesn't seem too unexpected considering the limit of max 128 inputs per active verifying batch, and the machine only has 2 threads. We could theoertically tune the batch verifier further to allow larger batches when a machine has <8 threads. I'll also look into the memory footprint when batch verifying 2x 128-ins to see how 256 holds up.

Of note, that code is also currently platform dependent on systems which support the `mallopt` syscall, which is mostly Linux platforms.

Also of note, I do still see continuously growing memory usage that does not get reclaimed (`top` indicates `monerod`'s resident memory grew from 1.95mb to 2.3gb overnight and it's not shrinking, and that's even with a smaller pool).

Continuing.

## kayabaNerve | 2025-11-04T20:25:54+00:00
As one note, `mallopt` was added due to aggravating the present allocator. If `mallopt` tames the current allocator, we don't need a cross-platform `mallopt` unless we're also aggravating allocators who don't respect `mallopt`.

It's still incredibly stupid that memory is growing without any leaks being detected, if we trust there aren't leaks. I'll leave that question alone for now however.

# Action History
- Created by: j-berman | 2025-10-29T20:11:04+00:00
