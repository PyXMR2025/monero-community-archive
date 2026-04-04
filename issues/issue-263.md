---
title: Cmake should check for proper bdb version
source_url: https://github.com/monero-project/monero/issues/263
author: arnuschky
assignees: []
labels: []
created_at: '2015-04-12T15:05:52+00:00'
updated_at: '2016-01-25T18:03:02+00:00'
type: issue
status: closed
closed_at: '2016-01-25T18:03:02+00:00'
---

# Original Description
Not sure which one is required. See #262 


# Discussion History
## molecular | 2015-05-16T05:06:14+00:00
Running into this with gentoo. bdb-4.8.30 is latest stable in gentoo.

I'm guessing at least bdb 5.x is required


## fluffypony | 2016-01-25T18:03:02+00:00
Closing this, we've also moved BDB to optional (LMDB is the default for 32-bit and for ARM now)


# Action History
- Created by: arnuschky | 2015-04-12T15:05:52+00:00
- Closed at: 2016-01-25T18:03:02+00:00
