---
title: mingw compilation error
source_url: https://github.com/xmrig/xmrig/issues/825
author: limidame
assignees: []
labels:
- question
created_at: '2018-10-19T23:25:52+00:00'
updated_at: '2018-11-05T06:56:33+00:00'
type: issue
status: closed
closed_at: '2018-11-05T06:56:33+00:00'
---

# Original Description
Got this error while compile latest xmrig

```
./workers/CpuThread.cpp: In static member function 'static xmrig::CpuThread* xmrig::CpuThread::createFromAV(size_t, xmrig::Algo, xmrig::AlgoVariant, int64_t, int, xmrig::Assembly)':
./workers/CpuThread.cpp:293:109: error: invalid new-expression of abstract class type 'xmrig::CpuThread'
     return new CpuThread(index, algorithm, av, multiway(av), cpuId, priority, isSoftAES(av), false, assembly);
                                                                                                             ^
In file included from ./workers/CpuThread.cpp:32:0:
./workers/CpuThread.h:38:7: note:   because the following virtual functions are pure within 'xmrig::CpuThread':
 class CpuThread : public IThread
          ^~~~~~~~~
In file included from ./workers/CpuThread.h:29:0,
                 from ./workers/CpuThread.cpp:32:
./interfaces/IThread.h:65:30: note: 	virtual rapidjson::Value xmrig::IThread::toAPI(rapidjson::Document&) const
     virtual rapidjson::Value toAPI(rapidjson::Document &doc) const = 0;
                              ^~~~~
./workers/CpuThread.cpp: In static member function 'static xmrig::CpuThread* xmrig::CpuThread::createFromData(size_t, xmrig::Algo, const xmrig::CpuThread::Data&, int, bool)':
./workers/CpuThread.cpp:311:138: error: invalid new-expression of abstract class type 'xmrig::CpuThread'
     return new CpuThread(index, algorithm, static_cast<AlgoVariant>(av), multiway, data.affinity, priority, softAES, false, data.assembly);
                                                                                                                                          ^
```

Help me please.

# Discussion History
## xmrig | 2018-10-20T04:46:34+00:00
Are you modify the source? Please provide all possible information.
Thank you.

## sailei00 | 2018-11-01T14:06:32+00:00
#858 
i got a similar error

# Action History
- Created by: limidame | 2018-10-19T23:25:52+00:00
- Closed at: 2018-11-05T06:56:33+00:00
