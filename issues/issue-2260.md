---
title: Lots of warnings on OS X build now.
source_url: https://github.com/monero-project/monero/issues/2260
author: jtgrassie
assignees: []
labels: []
created_at: '2017-08-07T17:03:08+00:00'
updated_at: '2017-08-15T20:12:14+00:00'
type: issue
status: closed
closed_at: '2017-08-15T20:12:14+00:00'
---

# Original Description
```
src/cryptonote_basic/cryptonote_basic_impl.h:72:17: warning: function 'return_first_address' is not needed and will not be
      emitted [-Wunneeded-internal-declaration]```

# Discussion History
## jtgrassie | 2017-08-07T17:04:57+00:00
Introduced by commit cb0b559

## moneromooo-monero | 2017-08-07T18:14:40+00:00
Does it go away if you make that function inline ?

## jtgrassie | 2017-08-07T18:28:53+00:00
Yes that fixes it.

+edit

Get's rid of the warning anyway. Not aware of any consequences though.

## moneromooo-monero | 2017-08-07T20:51:54+00:00
None expected.

## moneromooo-monero | 2017-08-07T23:35:44+00:00
Fixed in https://github.com/monero-project/monero/pull/2264

## moneromooo-monero | 2017-08-15T20:11:52+00:00
+resolved

# Action History
- Created by: jtgrassie | 2017-08-07T17:03:08+00:00
- Closed at: 2017-08-15T20:12:14+00:00
