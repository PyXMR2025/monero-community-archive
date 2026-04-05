---
title: FCMP++ DB Migration
source_url: https://github.com/seraphis-migration/monero/issues/115
author: vtnerd
assignees: []
labels: []
created_at: '2025-09-27T18:27:05+00:00'
updated_at: '2025-09-29T17:19:41+00:00'
type: issue
status: closed
closed_at: '2025-09-29T17:19:41+00:00'
---

# Original Description
I was looking at the DB migration code for FCMP++, and I think I've found an oversight.

The fcmp++ migration appears to assume that the "output id" field in "output amounts" table is globally unique. The id field is unique per amount, but not globally. The DB insertion code doesn't catch this issue because the last blocked lock will likely differ for each conflict.

Whether there are problems in the tree from this assumption, I'm not sure. I posted this issue because the code comments seem to lean in the direction of a misunderstanding of how the output ids were generated.

# Discussion History
## j-berman | 2025-09-28T16:54:56+00:00
It's using the globally unique output ID, not the other "global output ID" tethered to amounts from the output amounts table. Note here how these globally unique output ID's are generated without consideration for output amount, and strictly based on how many outputs are in the table: https://github.com/monero-project/monero/blob/b591866fcfed400bc89631686655aa769ec5f2dd/src/blockchain_db/lmdb/db_lmdb.cpp#L1060 

The fact that there is another "global output ID" is a pretty annoying source of confusion, see this convo: https://github.com/seraphis-migration/monero/pull/62#discussion_r2230016815

EDIT: `amount_index` is unique per amount, `output_id` is globally unique


## j-berman | 2025-09-29T16:40:15+00:00
~~Btw, the migration should fail if `output_id` wasn't unique, because `MDB_NODUPDATA` would cause the db insertion to fail IIRC. Have tested the migration successfully.~~

EDIT: nevermind:

> The DB insertion code doesn't catch this issue because the last blocked lock will likely differ for each conflict.

Valid point. In any case, the `output_id` should be globally unique.

## vtnerd | 2025-09-29T17:19:41+00:00
This value must be internal to `monerod` as I can't recall it ever being exposed.

# Action History
- Created by: vtnerd | 2025-09-27T18:27:05+00:00
- Closed at: 2025-09-29T17:19:41+00:00
