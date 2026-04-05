---
title: RandomX on x86?
source_url: https://github.com/xmrig/xmrig/issues/1289
author: passnet
assignees: []
labels: []
created_at: '2019-11-15T09:08:22+00:00'
updated_at: '2021-04-12T15:29:01+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:29:01+00:00'
---

# Original Description
Trying to build xmrig 5.0.0 on msys-mingw32 I get the following warning:

```
xmrig-5.0.0/src/crypto/rx/RxDataset.cpp: In member function 'void xmrig::RxDataset::setRaw(const void*)':
xmrig-5.0.0/src/crypto/rx/RxDataset.cpp:154:11: warning: 'void* memcpy(void*, const void*, size_t)' specified bound 2181038080 exceeds maximum object size 2147483647 [-Wstringop-overflow=]
  154 |     memcpy(randomx_get_dataset_memory(m_dataset), raw, maxSize());
      |     ~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

```

Not sure what it means but seems like it can cause mem overflow on 32-bit systems.

`gcc.exe (Rev2, Built by MSYS2 project) 9.2.0`

# Discussion History
## passnet | 2019-11-15T09:37:31+00:00
It still works with slow mode:
```
[2019-11-15 12:36:32.150]  rx   failed to allocate RandomX dataset, switching to slow mode (4 ms)
[2019-11-15 12:36:34.259]  rx   dataset ready (2109 ms)
```

If the warning can be safely ignored then probably that is not an issue.

## xmrig | 2019-11-15T10:04:13+00:00
I didn't deep look why allocation of a dataset does not work on 32 bit systems as it not too much useful for mining anyway, at least linker flag added `-Wl,--large-address-aware`.

`RxDataset.cpp:154:11: warning` this code works on NUMA machines for copy initialized dataset to other nodes.
Thank you.

# Action History
- Created by: passnet | 2019-11-15T09:08:22+00:00
- Closed at: 2021-04-12T15:29:01+00:00
