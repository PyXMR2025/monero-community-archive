---
title: 'monero-0.18.1.2/src/common/threadpool.h:96:10: error: ‘deque’ in namespace
  ‘std’ does not name a template type'
source_url: https://github.com/monero-project/monero/issues/8695
author: l29ah
assignees: []
labels: []
created_at: '2023-01-01T16:36:48+00:00'
updated_at: '2023-01-11T17:13:10+00:00'
type: issue
status: closed
closed_at: '2023-01-11T17:13:10+00:00'
---

# Original Description
gcc (Gentoo Hardened 12.2.1_p20221224 p7) 12.2.1 20221224
```
FAILED: src/common/CMakeFiles/obj_common.dir/threadpool.cpp.o 
/usr/bin/ccache /usr/lib/ccache/bin/x86_64-pc-linux-gnu-g++ -DAUTO_INITIALIZE_EASYLOGGINGPP -DBLOCKCHAIN_DB=DB_LMDB -DBOOST_ASIO_ENABLE_SEQUENTIAL_STRAND_ALLOCATION -DDEFAULT_DB_TYPE=\"lmdb\" -DHAVE_EXPLICIT_BZERO -DHAVE_HIDAPI -DHAVE_READLINE -DHAVE_STRPTIME -DPER_BLOCK_CHECKPOINT -I/var/tmp/portage/net-p2p/monero-0.18.1.2/work/monero-0.18.1.2/external/rapidjson/include -I/var/tmp/portage/net-p2p/monero-0.18.1.2/work/monero-0.18.1.2/external/easylogging++ -I/var/tmp/portage/net-p2p/monero-0.18.1.2/work/monero-0.18.1.2/src -I/var/tmp/portage/net-p2p/monero-0.18.1.2/work/monero-0.18.1.2/contrib/epee/include -I/var/tmp/portage/net-p2p/monero-0.18.1.2/work/monero-0.18.1.2/external -I/var/tmp/portage/net-p2p/monero-0.18.1.2/work/monero-0.18.1.2_build/generated_include -I/var/tmp/portage/net-p2p/monero-0.18.1.2/work/monero-0.18.1.2_build/translations -I/var/tmp/portage/net-p2p/monero-0.18.1.2/work/monero-0.18.1.2/external/db_drivers/liblmdb -I/usr/include/hidapi  -O2 -pipe -march=native -ftree-vectorize -malign-data=cacheline -mtls-dialect=gnu2 -pthread -maes -march=native -fno-strict-aliasing -D_GNU_SOURCE   -Wall -Wextra -Wpointer-arith -Wundef -Wvla -Wwrite-strings -Wno-error=extra -Wno-error=deprecated-declarations -Wno-unused-parameter -Wno-error=unused-variable -Wno-error=undef -Wno-error=uninitialized -Wlogical-op -Wno-error=maybe-uninitialized -Wno-error=cpp -Wno-reorder -Wno-missing-field-initializers -fPIC  -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -fcf-protection=full -fstack-clash-protection -Werror=switch -Werror=return-type -fno-strict-aliasing -ftemplate-depth=900 -std=c++14 -MD -MT src/common/CMakeFiles/obj_common.dir/threadpool.cpp.o -MF src/common/CMakeFiles/obj_common.dir/threadpool.cpp.o.d -o src/common/CMakeFiles/obj_common.dir/threadpool.cpp.o -c /var/tmp/portage/net-p2p/monero-0.18.1.2/work/monero-0.18.1.2/src/common/threadpool.cpp
In file included from /var/tmp/portage/net-p2p/monero-0.18.1.2/work/monero-0.18.1.2/src/common/threadpool.cpp:29:
/var/tmp/portage/net-p2p/monero-0.18.1.2/work/monero-0.18.1.2/src/common/threadpool.h:96:10: error: ‘deque’ in namespace ‘std’ does not name a template type
   96 |     std::deque<entry> queue;
      |          ^~~~~
/var/tmp/portage/net-p2p/monero-0.18.1.2/work/monero-0.18.1.2/src/common/threadpool.h:33:1: note: ‘std::deque’ is defined in header ‘<deque>’; did you forget to ‘#include <deque>’?
   32 | #include <boost/thread/thread.hpp>
  +++ |+#include <deque>
   33 | #include <cstddef>
/var/tmp/portage/net-p2p/monero-0.18.1.2/work/monero-0.18.1.2/src/common/threadpool.cpp: In member function ‘void tools::threadpool::submit(waiter*, std::function<void()>, bool)’:
/var/tmp/portage/net-p2p/monero-0.18.1.2/work/monero-0.18.1.2/src/common/threadpool.cpp:88:36: error: ‘queue’ was not declared in this scope; did you mean ‘sigqueue’?
   88 |   if (!leaf && ((active == max && !queue.empty()) || depth > 0)) {
      |                                    ^~~~~
      |                                    sigqueue
/var/tmp/portage/net-p2p/monero-0.18.1.2/work/monero-0.18.1.2/src/common/threadpool.cpp: In member function ‘void tools::threadpool::run(bool)’:
/var/tmp/portage/net-p2p/monero-0.18.1.2/work/monero-0.18.1.2/src/common/threadpool.cpp:155:11: error: ‘queue’ was not declared in this scope; did you mean ‘sigqueue’?
  155 |     while(queue.empty() && running)
      |           ^~~~~
      |           sigqueue
/var/tmp/portage/net-p2p/monero-0.18.1.2/work/monero-0.18.1.2/src/common/threadpool.cpp:164:19: error: ‘queue’ was not declared in this scope; did you mean ‘sigqueue’?
  164 |     e = std::move(queue.front());
      |                   ^~~~~
      |                   sigqueue
```

# Discussion History
## SChernykh | 2023-01-01T16:52:05+00:00
https://github.com/monero-project/monero/pull/8682

# Action History
- Created by: l29ah | 2023-01-01T16:36:48+00:00
- Closed at: 2023-01-11T17:13:10+00:00
