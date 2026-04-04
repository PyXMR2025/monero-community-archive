---
title: Bus 10 error - does someone want to look at DB
source_url: https://github.com/monero-project/monero/issues/3046
author: jwm1969
assignees: []
labels: []
created_at: '2018-01-02T16:56:52+00:00'
updated_at: '2021-08-13T06:44:36+00:00'
type: issue
status: closed
closed_at: '2021-08-13T06:44:36+00:00'
---

# Original Description
My lmdb/data.mdb got corrupt around last block (is my assumption based on error), was wondering if someone wanted the DB before I deleted it.  I was able to recover by doing an export / import versus a slow re-sync

FYI:  export reported Bus 10 error around last block but export/import still worked for recovery.

commands performed:

blockchain-export 
renamed ~/.bitmonero/lmdb/ directory. 
monero-blockchain-import --verify 0 --database lmdb#nosync

# Discussion History
## moneromooo-monero | 2018-01-03T10:35:45+00:00
Did your computer/OS crash before you got this corruption ?

Good thinking about the export/import :)

## jwm1969 | 2018-01-03T13:40:20+00:00
I think my Macbook Pro either crashed or the battery ran out because when i plugged it in it required a cold start...leaning towards abrupt shutdown for sure.

## selsta | 2021-08-13T06:44:36+00:00
Closing, issue doesn't seem relevant anymore.

# Action History
- Created by: jwm1969 | 2018-01-02T16:56:52+00:00
- Closed at: 2021-08-13T06:44:36+00:00
