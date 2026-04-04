---
title: Mac build failed
source_url: https://github.com/monero-project/monero/issues/49
author: sammy007
assignees: []
labels: []
created_at: '2014-06-20T04:44:59+00:00'
updated_at: '2014-06-20T07:30:27+00:00'
type: issue
status: closed
closed_at: '2014-06-20T07:30:27+00:00'
---

# Original Description
Hi, after latest changes from @NoodleDoodleNoodleDoodleNoodleDoodleNoo I can't build monero on osx.

```
[ 37%] Building CXX object src/CMakeFiles/cryptonote_core.dir/cryptonote_core/checkpoints.cpp.o
[ 38%] Building C object src/CMakeFiles/crypto.dir/crypto/slow-hash.c.o
/tmp/bitmonero-OhJz/src/crypto/slow-hash.c:308:35: error: use of undeclared identifier 'MAP_ANONYMOUS'
                    MAP_PRIVATE | MAP_ANONYMOUS | MAP_HUGETLB, 0, 0);
                                  ^
/tmp/bitmonero-OhJz/src/crypto/slow-hash.c:308:51: error: use of undeclared identifier 'MAP_HUGETLB'
                    MAP_PRIVATE | MAP_ANONYMOUS | MAP_HUGETLB, 0, 0);
                                                  ^
2 errors generated.
make[3]: *** [src/CMakeFiles/crypto.dir/crypto/slow-hash.c.o] Error 1
make[2]: *** [src/CMakeFiles/crypto.dir/all] Error 2
make[2]: *** Waiting for unfinished jobs....
```

https://github.com/sammy007/homebrew-cryptonight/issues/3


# Discussion History
## sammy007 | 2014-06-20T07:30:27+00:00
Fixed.


# Action History
- Created by: sammy007 | 2014-06-20T04:44:59+00:00
- Closed at: 2014-06-20T07:30:27+00:00
