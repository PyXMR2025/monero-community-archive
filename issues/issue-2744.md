---
title: unit tests - unbound.supported_algorithms - dnskey_algo_id_is_supported(5)
  - false
source_url: https://github.com/monero-project/monero/issues/2744
author: danrmiller
assignees: []
labels:
- tests
created_at: '2017-11-01T18:18:17+00:00'
updated_at: '2017-12-26T15:56:23+00:00'
type: issue
status: closed
closed_at: '2017-12-26T15:56:23+00:00'
---

# Original Description
@moneromooo-monero has helped me look into this before. At first glance it looks like openssl has no SHA256 support, but it seems there is something else going on.

If moo gets some time I can make sure you have access to a testing box, but windows isn't the easiest to work with.

Using mingw-w64-x86_64-openssl-1.0.2.k-1 

https://build.getmonero.org/builders/monero-static-win64/builds/2579/steps/test/logs/LastTest

```
[----------] 1 test from unbound
[ RUN      ] unbound.supported_algorithms
C:/msys64/home/vagrant/slave/monero-static-win64/build/tests/unit_tests/unbound.cpp:46: Failure
Value of: dnskey_algo_id_is_supported(5)
  Actual: false
Expected: true
[  FAILED  ] unbound.supported_algorithms (0 ms)
[----------] 1 test from unbound (0 ms total)
```





# Discussion History
## danrmiller | 2017-11-01T18:23:00+00:00
+tests

## moneromooo-monero | 2017-12-23T16:36:09+00:00
Better late than never...

https://github.com/monero-project/monero/pull/2996

## moneromooo-monero | 2017-12-26T15:55:58+00:00
+resolved

# Action History
- Created by: danrmiller | 2017-11-01T18:18:17+00:00
- Closed at: 2017-12-26T15:56:23+00:00
