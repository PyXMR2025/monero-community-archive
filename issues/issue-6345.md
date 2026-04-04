---
title: fails to build from source with new gtest
source_url: https://github.com/monero-project/monero/issues/6345
author: xnox
assignees: []
labels: []
created_at: '2020-02-18T22:54:49+00:00'
updated_at: '2020-04-04T17:50:37+00:00'
type: issue
status: closed
closed_at: '2020-04-04T17:50:37+00:00'
---

# Original Description
```
In file included from /usr/include/gtest/gtest.h:62,
                 from /<<PKGBUILDDIR>>/tests/unit_tests/hmac_keccak.cpp:29:
/<<PKGBUILDDIR>>/tests/unit_tests/hmac_keccak.cpp:126:1: error: static assertion failed: test_name must not be empty
  126 | TEST(keccak_hmac, )
```

I guess that test needs a name, rather than empty.

# Discussion History
# Action History
- Created by: xnox | 2020-02-18T22:54:49+00:00
- Closed at: 2020-04-04T17:50:37+00:00
