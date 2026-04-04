---
title: Please fix clang warnings
source_url: https://github.com/monero-project/monero/issues/3134
author: yurivict
assignees: []
labels:
- invalid
created_at: '2018-01-16T01:14:18+00:00'
updated_at: '2018-01-16T10:40:33+00:00'
type: issue
status: closed
closed_at: '2018-01-16T10:40:33+00:00'
---

# Original Description
```
/usr/ports/net-p2p/libmonero/work/monero-0.11.1.0/src/cryptonote_protocol/block_queue.cpp:208:44: warning: suggest braces around initialization of subobject [-Wmissing-braces]
  static const boost::uuids::uuid uuid0 = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
                                           ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                           {                                          }
1 warning generated.
```

# Discussion History
## moneromooo-monero | 2018-01-16T10:30:14+00:00
It was fixed long ago. You're using some old code.

+invalid

## yurivict | 2018-01-16T10:35:37+00:00
I am using the latest release ```0.11.1.0```.

# Action History
- Created by: yurivict | 2018-01-16T01:14:18+00:00
- Closed at: 2018-01-16T10:40:33+00:00
