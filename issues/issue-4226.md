---
title: Unit test fails
source_url: https://github.com/monero-project/monero/issues/4226
author: D4nte
assignees: []
labels:
- duplicate
created_at: '2018-08-05T11:07:38+00:00'
updated_at: '2018-09-11T09:32:56+00:00'
type: issue
status: closed
closed_at: '2018-09-11T09:32:56+00:00'
---

# Original Description
Hi,

When running `make release-test` the unit test fails. v0.12.3.0 from git. 
On Ubuntu 18.04 LTS, compiled locally. No special flags passed. All dev dependencies installed via apt.

```
$ uname -a
Linux nuc 4.15.0-29-generic #31-Ubuntu SMP Tue Jul 17 15:39:52 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux
```

```
The following tests FAILED:
          4 - unit_tests (Failed)
Errors while running CTest
Makefile:85: recipe for target 'test' failed
make[1]: *** [test] Error 8
```

Let me know what info you need.

[release_test.txt](https://github.com/monero-project/monero/files/2260248/release_test.txt)


# Discussion History
## moneromooo-monero | 2018-08-05T15:11:05+00:00
Run manually and see which one(s) fail(s). If it's just the DNS one, you can ignore it.

## radfish | 2018-08-05T20:58:37+00:00
Also see PR #4165 regarding ringdb unit test failing.
Also, if you're running on an NFS share, Serialization.portability_wallet will also fail.

## D4nte | 2018-08-05T23:55:20+00:00
No NFS share. It is indeed the DNS ones:
```
[  FAILED  ] 3 tests, listed below:
[  FAILED  ] AddressFromURL.Failure
[  FAILED  ] DNSResolver.DNSSECSuccess
[  FAILED  ] DNSResolver.DNSSECFailure
```

## radfish | 2018-08-11T21:19:37+00:00
Can be closed as duplicate of #2172

## moneromooo-monero | 2018-09-11T09:18:05+00:00
+duplicate

# Action History
- Created by: D4nte | 2018-08-05T11:07:38+00:00
- Closed at: 2018-09-11T09:32:56+00:00
