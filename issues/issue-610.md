---
title: xmrig 2.6.1 stopped to build on ARMv7
source_url: https://github.com/xmrig/xmrig/issues/610
author: Zenitur
assignees: []
labels:
- bug
created_at: '2018-05-06T19:02:22+00:00'
updated_at: '2018-05-06T19:44:51+00:00'
type: issue
status: closed
closed_at: '2018-05-06T19:44:51+00:00'
---

# Original Description
```
[ 54%] Building CXX object CMakeFiles/xmrig.dir/src/workers/CpuThread.cpp.o
In file included from /home/pi/altcoins/xmr-stak/xmrig-2.6.1/src/workers/CpuThread.cpp:33:0:
/home/pi/altcoins/xmr-stak/xmrig-2.6.1/src/crypto/CryptoNight_arm.h:39:29: фатальная ошибка: crypto/c_keccak.h: Нет такого файла или каталога
 #include "crypto/c_keccak.h"
                             ^
компиляция прервана.
```

Hovewer 2.5.3 successfully builds.

# Discussion History
## xmrig | 2018-05-06T19:14:49+00:00
Already fixed in master branch.
Thank you.

## xmrig | 2018-05-06T19:44:51+00:00
Fixed in v2.6.2.

# Action History
- Created by: Zenitur | 2018-05-06T19:02:22+00:00
- Closed at: 2018-05-06T19:44:51+00:00
