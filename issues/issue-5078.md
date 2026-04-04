---
title: Use <boost/integer/integer_log2.hpp> instead
source_url: https://github.com/monero-project/monero/issues/5078
author: moneroexamples
assignees: []
labels: []
created_at: '2019-01-17T04:19:54+00:00'
updated_at: '2019-05-20T21:45:30+00:00'
type: issue
status: closed
closed_at: '2019-01-17T05:01:00+00:00'
---

# Original Description
After a batch of most recent PRs, lots of warnings appears on arch linux:

```
/usr/include/boost/predef/detail/endian_compat.h:11:161: note: #pragma message: The use of BOOST_*_ENDIAN and BOOST_BYTE_ORDER is deprecated. Please include <boost/predef/other/endian.h> and use BOOST_ENDIAN_*_BYTE instead
 #pragma message("The use of BOOST_*_ENDIAN and BOOST_BYTE_ORDER is deprecated. Please include <boost/predef/other/endian.h> and use BOOST_ENDIAN_*_BYTE instead")
```

```
/usr/include/boost/pending/integer_log2.hpp:7:59: note: #pragma message: This header is deprecated. Use <boost/integer/integer_log2.hpp> instead.
 BOOST_HEADER_DEPRECATED("<boost/integer/integer_log2.hpp>");
```

For now I don't know if its Monero's fault or Arch's, so I just leave it here for other to view. 


# Discussion History
## moneroexamples | 2019-01-17T05:00:59+00:00
Seems to be boost issue. So closing for now.

## Geremia | 2019-05-20T21:45:29+00:00
@moneroexamples I replaced `#include <boost/archive/portable_binary_oarchive.hpp>
` with `include <boost/predef/other/endian.h>` in `src/p2p/net_peerlist.cpp`, and it compiled for me (Boost 0.70).

# Action History
- Created by: moneroexamples | 2019-01-17T04:19:54+00:00
- Closed at: 2019-01-17T05:01:00+00:00
