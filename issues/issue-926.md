---
title: static build of tests fails with `undefined reference to __wrap___cxa_throw`
source_url: https://github.com/monero-project/monero/issues/926
author: radfish
assignees: []
labels: []
created_at: '2016-07-23T19:01:52+00:00'
updated_at: '2016-07-28T02:38:28+00:00'
type: issue
status: closed
closed_at: '2016-07-28T02:38:28+00:00'
---

# Original Description
Debian Jessie x86_64 _without_ libunwind-dev and libunwind8 (otherwise fails due to #907). Same on Arch Linux 32-bit and 64-bit, too.
[build.log.txt](https://github.com/monero-project/bitmonero/files/379937/build.log.txt)

```
cmake -DCMAKE_BUILD_TYPE=Release -DSTATIC=ON -DBUILD_TESTS=ON .. 2>&1 | tee -a build.log
```

```
/tmp/cc8lNtqY.ltrans12.ltrans.o: In function `boost::exception_detail::clone_impl<boost::exception_detail::error_info_injector<boost::thread_resource_error> >::rethrow() const [clone .lto_priv.41]':
cc8lNtqY.ltrans12.o:(.text+0x4e): undefined reference to `__wrap___cxa_throw'
```

Build succeeds with `BUILD_TESTS=OFF`


# Discussion History
## radfish | 2016-07-28T02:38:28+00:00
Fixed by #933


# Action History
- Created by: radfish | 2016-07-23T19:01:52+00:00
- Closed at: 2016-07-28T02:38:28+00:00
