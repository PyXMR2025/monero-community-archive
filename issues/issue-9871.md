---
title: Build error on FreeBSD 14.2-RELEASE
source_url: https://github.com/monero-project/monero/issues/9871
author: christosmarg
assignees: []
labels: []
created_at: '2025-03-26T15:12:16+00:00'
updated_at: '2025-03-27T17:47:22+00:00'
type: issue
status: closed
closed_at: '2025-03-27T17:47:21+00:00'
---

# Original Description
This FreeBSD port has been broken for a while already [1]. The build fails with boost-1.85+. I am using boost 1.87:
```
$ pkg info | grep boost
boost-libs-1.87.0_1            Free portable C++ libraries (without Boost.Python)
```

Below is a sample of the errors thrown:

```
1 error generated.
[  6% 20/213] /usr/bin/c++ -DAUTO_INITIALIZE_EASYLOGGINGPP -DBLOCKCHAIN_DB=DB_LMDB -DBOOST_ASIO_ENABLE_SEQUENTIAL_STRAND_ALLOCATION -DDEFAULT_DB_TYPE=\"lmdb\" -DHAVE_EXPLICIT_BZERO -DHAVE_MEMSET_S -DHAVE_READLINE -DHAVE_STRPTIME -DPER_BLOCK_CHECKPOINT -I/usr/ports/net-p2p/monero-cli/work/monero-0.18.3.4/external/rapidjson/include -I/usr/ports/net-p2p/monero-cli/work/monero-0.18.3.4/external/easylogging++ -I/usr/ports/net-p2p/monero-cli/work/monero-0.18.3.4/src -I/usr/ports/net-p2p/monero-cli/work/monero-0.18.3.4/contrib/epee/include -I/usr/ports/net-p2p/monero-cli/work/monero-0.18.3.4/external -I/usr/ports/net-p2p/monero-cli/work/monero-0.18.3.4/external/supercop/include -I/usr/ports/net-p2p/monero-cli/work/.build/generated_include -I/usr/ports/net-p2p/monero-cli/work/.build/translations -I/usr/ports/net-p2p/monero-cli/work/monero-0.18.3.4/external/db_drivers/liblmdb -isystem /usr/local/include -O2 -pipe -D_WANT_SEMUN -fstack-protector-strong -fno-strict-aliasing -pthread -maes  -fno-strict-aliasing -D_GNU_SOURCE   -Wall -Wextra -Wpointer-arith -Wundef -Wvla -Wwrite-strings -Wno-error=extra -Wno-error=deprecated-declarations -Wno-unused-parameter -Wno-error=unused-variable -Wno-error=undef -Wno-error=uninitialized -Wno-reorder -Wno-missing-field-initializers -fPIC  -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -fcf-protection=full -fstack-clash-protection -Werror=switch -Werror=return-type -fno-strict-aliasing -ftemplate-depth=900 -DNDEBUG -Ofast  -std=c++14 -MD -MT contrib/epee/src/CMakeFiles/obj_epee.dir/connection_basic.cpp.o -MF contrib/epee/src/CMakeFiles/obj_epee.dir/connection_basic.cpp.o.d -o contrib/epee/src/CMakeFiles/obj_epee.dir/connection_basic.cpp.o -c /usr/ports/net-p2p/monero-cli/work/monero-0.18.3.4/contrib/epee/src/connection_basic.cpp
FAILED: contrib/epee/src/CMakeFiles/obj_epee.dir/connection_basic.cpp.o
/usr/bin/c++ -DAUTO_INITIALIZE_EASYLOGGINGPP -DBLOCKCHAIN_DB=DB_LMDB -DBOOST_ASIO_ENABLE_SEQUENTIAL_STRAND_ALLOCATION -DDEFAULT_DB_TYPE=\"lmdb\" -DHAVE_EXPLICIT_BZERO -DHAVE_MEMSET_S -DHAVE_READLINE -DHAVE_STRPTIME -DPER_BLOCK_CHECKPOINT -I/usr/ports/net-p2p/monero-cli/work/monero-0.18.3.4/external/rapidjson/include -I/usr/ports/net-p2p/monero-cli/work/monero-0.18.3.4/external/easylogging++ -I/usr/ports/net-p2p/monero-cli/work/monero-0.18.3.4/src -I/usr/ports/net-p2p/monero-cli/work/monero-0.18.3.4/contrib/epee/include -I/usr/ports/net-p2p/monero-cli/work/monero-0.18.3.4/external -I/usr/ports/net-p2p/monero-cli/work/monero-0.18.3.4/external/supercop/include -I/usr/ports/net-p2p/monero-cli/work/.build/generated_include -I/usr/ports/net-p2p/monero-cli/work/.build/translations -I/usr/ports/net-p2p/monero-cli/work/monero-0.18.3.4/external/db_drivers/liblmdb -isystem /usr/local/include -O2 -pipe -D_WANT_SEMUN -fstack-protector-strong -fno-strict-aliasing -pthread -maes  -fno-strict-aliasing -D_GNU_SOURCE   -Wall -Wextra -Wpointer-arith -Wundef -Wvla -Wwrite-strings -Wno-error=extra -Wno-error=deprecated-declarations -Wno-unused-parameter -Wno-error=unused-variable -Wno-error=undef -Wno-error=uninitialized -Wno-reorder -Wno-missing-field-initializers -fPIC  -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -fcf-protection=full -fstack-clash-protection -Werror=switch -Werror=return-type -fno-strict-aliasing -ftemplate-depth=900 -DNDEBUG -Ofast  -std=c++14 -MD -MT contrib/epee/src/CMakeFiles/obj_epee.dir/connection_basic.cpp.o -MF contrib/epee/src/CMakeFiles/obj_epee.dir/connection_basic.cpp.o.d -o contrib/epee/src/CMakeFiles/obj_epee.dir/connection_basic.cpp.o -c /usr/ports/net-p2p/monero-cli/work/monero-0.18.3.4/contrib/epee/src/connection_basic.cpp
In file included from /usr/ports/net-p2p/monero-cli/work/monero-0.18.3.4/contrib/epee/src/connection_basic.cpp:35:
In file included from /usr/ports/net-p2p/monero-cli/work/monero-0.18.3.4/contrib/epee/include/net/connection_basic.hpp:53:
/usr/ports/net-p2p/monero-cli/work/monero-0.18.3.4/contrib/epee/include/net/net_utils_base.h:33:10: fatal error: 'boost/asio/io_service.hpp' file not found
   33 | #include <boost/asio/io_service.hpp>
      |          ^~~~~~~~~~~~~~~~~~~~~~~~~~~
```

[1] https://cgit.freebsd.org/ports/commit/?id=3da4573eecd73a44684a43970822cac66177a70c

# Discussion History
## vtnerd | 2025-03-26T15:25:37+00:00
The release branch has this fixed, but an official release has not yet been tagged. This should be happening Friday, but check #9758 for updates.

## christosmarg | 2025-03-26T15:27:19+00:00
That's great. Thank you!

## selsta | 2025-03-27T17:47:21+00:00
Closing as this is already fixed in the codebase.

# Action History
- Created by: christosmarg | 2025-03-26T15:12:16+00:00
- Closed at: 2025-03-27T17:47:21+00:00
