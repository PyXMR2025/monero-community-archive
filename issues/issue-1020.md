---
title: Error compiling xmrig on FreeBSD
source_url: https://github.com/xmrig/xmrig/issues/1020
author: codeorcode
assignees: []
labels: []
created_at: '2019-05-08T12:44:38+00:00'
updated_at: '2019-08-02T11:51:21+00:00'
type: issue
status: closed
closed_at: '2019-08-02T11:51:21+00:00'
---

# Original Description
Hi, I get this error when I try to compile xmrig on FreeBSD.

I've tried using gcc6 and gcc7.

Any idea how to solve this?

(I've posted this in xmrig-proxy, it should be posted here, please delete the post from there.)


```
CMakeFiles/xmrig.dir/src/workers/Workers.cpp.o: In function `Workers::onTick(uv_timer_s*)':
Workers.cpp:(.text+0x42): undefined reference to `__atomic_load_8'
Workers.cpp:(.text+0x6b): undefined reference to `__atomic_load_8'
CMakeFiles/xmrig.dir/src/workers/Workers.cpp.o: In function `Workers::setEnabled(bool)':
Workers.cpp:(.text+0x607): undefined reference to `__atomic_fetch_add_8'
CMakeFiles/xmrig.dir/src/workers/Workers.cpp.o: In function `Workers::setJob(xmrig::Job const&, bool)':
Workers.cpp:(.text+0x8e0): undefined reference to `__atomic_fetch_add_8'
CMakeFiles/xmrig.dir/src/workers/Workers.cpp.o: In function `Workers::stop()':
Workers.cpp:(.text+0x971): undefined reference to `__atomic_store_8'
CMakeFiles/xmrig.dir/src/workers/Workers.cpp.o: In function `Workers::start(xmrig::Controller*)':
Workers.cpp:(.text+0x1806): undefined reference to `__atomic_store_8'
CMakeFiles/xmrig.dir/src/net/Network.cpp.o: In function `xmrig::Network::onPause(xmrig::IStrategy*)':
Network.cpp:(.text+0x4c9): undefined reference to `__atomic_fetch_add_8'
CMakeFiles/xmrig.dir/src/workers/MultiWorker.cpp.o: In function `Worker::timestamp() const':
MultiWorker.cpp:(.text._ZNK6Worker9timestampEv[_ZNK6Worker9timestampEv]+0xe): undefined reference to `__atomic_load_8'
CMakeFiles/xmrig.dir/src/workers/MultiWorker.cpp.o: In function `Worker::hashCount() const':
MultiWorker.cpp:(.text._ZNK6Worker9hashCountEv[_ZNK6Worker9hashCountEv]+0xe): undefined reference to `__atomic_load_8'
CMakeFiles/xmrig.dir/src/workers/MultiWorker.cpp.o: In function `MultiWorker<1u>::consumeJob()':
MultiWorker.cpp:(.text._ZN11MultiWorkerILj1EE10consumeJobEv[_ZN11MultiWorkerILj1EE10consumeJobEv]+0x27): undefined reference to `__atomic_load_8'
CMakeFiles/xmrig.dir/src/workers/MultiWorker.cpp.o: In function `MultiWorker<1u>::start()':
MultiWorker.cpp:(.text._ZN11MultiWorkerILj1EE5startEv[_ZN11MultiWorkerILj1EE5startEv]+0x2b): undefined reference to `__atomic_load_8'
MultiWorker.cpp:(.text._ZN11MultiWorkerILj1EE5startEv[_ZN11MultiWorkerILj1EE5startEv]+0x300): undefined reference to `__atomic_load_8'
CMakeFiles/xmrig.dir/src/workers/MultiWorker.cpp.o:MultiWorker.cpp:(.text._ZN11MultiWorkerILj1EE5startEv[_ZN11MultiWorkerILj1EE5startEv]+0x3ab): more undefined references to `__atomic_load_8' follow
CMakeFiles/xmrig.dir/src/workers/Worker.cpp.o: In function `Worker::storeStats()':
Worker.cpp:(.text+0x1b6): undefined reference to `__atomic_store_8'
Worker.cpp:(.text+0x1c8): undefined reference to `__atomic_store_8'
collect2: error: ld returned 1 exit status
```

# Discussion History
## lisergey | 2019-05-08T16:10:21+00:00
use  `portmaster net-p2p/xmrig/`
or `pkg install xmrig`
It wonderfully compiles with clang onboard

## codeorcode | 2019-05-08T18:32:29+00:00
Thank you for your reply. In the end I've compiled this version from github with clang and it worked ok.
Too bad that this new cryptonight/r is that slow on CPU (I got 54 hs/s on a 6 core amd 6300). Not worth mining on it anymore.

# Action History
- Created by: codeorcode | 2019-05-08T12:44:38+00:00
- Closed at: 2019-08-02T11:51:21+00:00
