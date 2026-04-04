---
title: Create DB Format Migration System
source_url: https://github.com/monero-project/monero/issues/663
author: fluffypony
assignees: []
labels:
- enhancement
created_at: '2016-02-14T17:26:16+00:00'
updated_at: '2016-07-07T20:03:35+00:00'
type: issue
status: closed
closed_at: '2016-07-07T20:03:35+00:00'
---

# Original Description
**_Assigned To:**_ Currently unassigned, although @hyc has indicated interest in it

**_Notes:**_

See dev meeting logs from 2016-02-14


# Discussion History
## hyc | 2016-02-14T17:38:05+00:00
1) should provide individual migration steps: v0 to v1, v1 to v2, v2 to v3, etc.
2) should support incremental state, resumable from interruptions
   just migrate in batches, and record a migrated_height with each batch

3) chain all the steps: so migrating from v0 to v3 invokes v0 - v1, v1-v2, v2-v3 on each block, don't do multiple passes across the entire DB for each version bump.


## hyc | 2016-04-08T02:37:04+00:00
A migration function to convert from v0 to v1 is now available for testing in https://github.com/LMDB/bitmonero/commit/c14f9efd52084cee21ff9072c3a903eb33635b1d

It can be safely interrupted and resumed without any problem.


## hyc | 2016-04-09T11:52:23+00:00
The current migration function performs quite poorly. Importing an 874830 block blockchain.raw file on 5400rpm HDD using v0.9.4 took 1:12:21 (over 1 hour), migrating it using the current migrate function took nearly 3 hours. Simply exporting the DB back to a .raw file took 26 minutes, and running blockchain_import from the perf branch took only 4 minutes. Full details here https://gist.github.com/hyc/913420265895e7fcc20473264324d05c

So, we definitely should not proceed with the current migration function. Time for round 2...


## fluffypony | 2016-07-07T20:03:35+00:00
Done and fixed


# Action History
- Created by: fluffypony | 2016-02-14T17:26:16+00:00
- Closed at: 2016-07-07T20:03:35+00:00
