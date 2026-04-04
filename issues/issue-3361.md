---
title: cmake -DBUILD_SHARED_LIBS=1 . fails on master
source_url: https://github.com/monero-project/monero/issues/3361
author: sammy007
assignees: []
labels: []
created_at: '2018-03-06T14:37:45+00:00'
updated_at: '2018-03-16T13:10:25+00:00'
type: issue
status: closed
closed_at: '2018-03-16T13:10:25+00:00'
---

# Original Description
My pool used to link with dynamically compiled monero...

```
cmake -DBUILD_SHARED_LIBS=1 . && make
```

... in order to avoid code copy paste and fragmentation, now it's impossible to build monero this way. Is it intention or broken by mistake?

```
Doxygen: graphviz not found - graphs disabled
-- Could NOT find Doxygen (missing:  DOXYGEN_EXECUTABLE)
-- Performing Test HAVE_C11
-- Performing Test HAVE_C11 - Success
-- Configuring done
CMake Error: The inter-target dependency graph contains the following strongly connected component (cycle):
  "common" of type SHARED_LIBRARY
    depends on "cncrypto" (weak)
    depends on "device" (weak)
    depends on "ringct" (weak)
    depends on "cryptonote_basic" (weak)
    depends on "checkpoints" (weak)
  "cncrypto" of type SHARED_LIBRARY
    depends on "device" (weak)
    depends on "ringct" (weak)
    depends on "common" (weak)
    depends on "cryptonote_basic" (weak)
    depends on "checkpoints" (weak)
  "ringct" of type SHARED_LIBRARY
    depends on "common" (weak)
    depends on "cncrypto" (weak)
    depends on "device" (weak)
    depends on "cryptonote_basic" (weak)
    depends on "checkpoints" (weak)
  "checkpoints" of type SHARED_LIBRARY
    depends on "common" (weak)
    depends on "cncrypto" (weak)
    depends on "device" (weak)
    depends on "ringct" (weak)
    depends on "cryptonote_basic" (weak)
  "cryptonote_basic" of type SHARED_LIBRARY
    depends on "common" (weak)
    depends on "cncrypto" (weak)
    depends on "device" (weak)
    depends on "ringct" (weak)
    depends on "checkpoints" (weak)
  "device" of type SHARED_LIBRARY
    depends on "cncrypto" (weak)
    depends on "ringct" (weak)
    depends on "common" (weak)
    depends on "cryptonote_basic" (weak)
    depends on "checkpoints" (weak)
At least one of these targets is not a STATIC_LIBRARY.  Cyclic dependencies are allowed only among static libraries.
-- Build files have been written to: /home/build/src/monero
```

# Discussion History
## moneromooo-monero | 2018-03-06T15:05:00+00:00
Probably fixed in 3350

# Action History
- Created by: sammy007 | 2018-03-06T14:37:45+00:00
- Closed at: 2018-03-16T13:10:25+00:00
