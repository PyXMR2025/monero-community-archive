---
title: make command fails after a while amount of time
source_url: https://github.com/monero-project/monero/issues/7835
author: S1700
assignees: []
labels: []
created_at: '2021-08-06T10:15:30+00:00'
updated_at: '2021-08-06T21:04:04+00:00'
type: issue
status: closed
closed_at: '2021-08-06T21:04:04+00:00'
---

# Original Description
So when i ran the make command it works for the first 1 minute or 2 but then after a bit it gets stuck on this and then fails:
```
[  7%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/abstract_http_client.cpp.o
[  7%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/http_auth.cpp.o
c++: fatal error: Killed signal terminated program cc1plus
compilation terminated.
make[3]: *** [contrib/epee/src/CMakeFiles/epee.dir/build.make:134: contrib/epee/src/CMakeFiles/epee.dir/http_auth.cpp.o] Error 1
make[3]: Leaving directory '/root/monero-pool/monero/build/Linux/release-v0.17/release'
make[2]: *** [CMakeFiles/Makefile2:1643: contrib/epee/src/CMakeFiles/epee.dir/all] Error 2
make[2]: Leaving directory '/root/monero-pool/monero/build/Linux/release-v0.17/release'
make[1]: *** [Makefile:160: all] Error 2
make[1]: Leaving directory '/root/monero-pool/monero/build/Linux/release-v0.17/release'
make: *** [Makefile:103: release-all] Error 2
root@rkfaucets:~/monero-pool/monero#
```


# Discussion History
## selsta | 2021-08-06T18:42:58+00:00
It means you are out of RAM..

## S1700 | 2021-08-06T21:04:04+00:00
ah okay ill try to kill some background processes. thanks

# Action History
- Created by: S1700 | 2021-08-06T10:15:30+00:00
- Closed at: 2021-08-06T21:04:04+00:00
