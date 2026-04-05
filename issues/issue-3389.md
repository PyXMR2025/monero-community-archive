---
title: 'ZEPH: Low hashrate after pool reconnection'
source_url: https://github.com/xmrig/xmrig/issues/3389
author: amoiseev
assignees: []
labels: []
created_at: '2023-12-25T09:52:24+00:00'
updated_at: '2025-06-18T22:25:40+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:25:40+00:00'
---

# Original Description
Sometimes with CPU mining ZEPH on Windows, hashrate drops to near-zero:

```
[2023-12-25 12:01:49.928]  miner    speed 10s/60s/15m 1139.8 1159.0 1162.2 H/s max 1216.8 H/s
[2023-12-25 12:02:15.636]  net      new job from zeph.kryptex.network:7777 diff 400015 algo rx/0 height 149313
[2023-12-25 12:02:51.163]  miner    speed 10s/60s/15m 1081.4 1101.2 1158.8 H/s max 1216.8 H/s
[2023-12-25 12:03:11.402]  net      new job from zeph.kryptex.network:7777 diff 400015 algo rx/0 height 149314
[2023-12-25 12:03:39.989]  net      new job from zeph.kryptex.network:7777 diff 400015 algo rx/0 height 149315
[2023-12-25 12:03:45.053]  net      new job from zeph.kryptex.network:7777 diff 400015 algo rx/0 height 149316
[2023-12-25 12:03:52.438]  miner    speed 10s/60s/15m 1155.7 1146.9 1156.7 H/s max 1216.8 H/s
[2023-12-25 12:04:40.332]  net      new job from zeph.kryptex.network:7777 diff 400015 algo rx/0 height 149317
[2023-12-25 12:04:53.656]  miner    speed 10s/60s/15m 1184.4 1144.4 1154.7 H/s max 1216.8 H/s
[2023-12-25 12:05:16.164]  net      new job from zeph.kryptex.network:7777 diff 400015 algo rx/0 height 149318
[2023-12-25 12:05:54.918]  miner    speed 10s/60s/15m 1127.0 1162.5 1154.6 H/s max 1216.8 H/s
[2023-12-25 12:06:56.180]  miner    speed 10s/60s/15m 735.8 917.3 1137.2 H/s max 1216.8 H/s
[2023-12-25 12:07:57.432]  miner    speed 10s/60s/15m 750.9 742.1 1109.6 H/s max 1216.8 H/s
[2023-12-25 12:08:44.719]  net      stratum+tcp://zeph.kryptex.network:7777 read error: "end of file"
[2023-12-25 12:08:44.720]  net      no active pools, stop mining
[2023-12-25 12:08:49.872]  net      use pool zeph.kryptex.network:7777  142.132.131.238
[2023-12-25 12:08:49.872]  net      new job from zeph.kryptex.network:7777 diff 400015 algo rx/0 height 149318
[2023-12-25 12:08:58.709]  miner    speed 10s/60s/15m 1.65 591.0 1069.8 H/s max 1216.8 H/s
[2023-12-25 12:09:59.994]  miner    speed 10s/60s/15m 2.16 2.14 989.9 H/s max 1216.8 H/s
[2023-12-25 12:11:01.263]  miner    speed 10s/60s/15m 2.47 2.29 911.3 H/s max 1216.8 H/s
[2023-12-25 12:12:02.514]  miner    speed 10s/60s/15m 2.06 2.18 835.9 H/s max 1216.8 H/s
[2023-12-25 12:13:03.792]  miner    speed 10s/60s/15m 2.27 2.19 755.6 H/s max 1216.8 H/s
[2023-12-25 12:14:05.057]  miner    speed 10s/60s/15m 2.06 2.26 675.5 H/s max 1216.8 H/s
[2023-12-25 12:15:06.266]  miner    speed 10s/60s/15m 2.59 2.28 597.3 H/s max 1216.8 H/s
[2023-12-25 12:15:46.223]  net      new job from zeph.kryptex.network:7777 diff 400015 algo rx/0 height 149319
[2023-12-25 12:16:07.434]  miner    speed 10s/60s/15m 2.16 2.28 518.6 H/s max 1216.8 H/s
[2023-12-25 12:17:08.686]  miner    speed 10s/60s/15m 2.48 2.33 441.8 H/s max 1216.8 H/s
[2023-12-25 12:18:09.951]  miner    speed 10s/60s/15m 2.16 2.18 366.0 H/s max 1216.8 H/s
[2023-12-25 12:19:11.223]  miner    speed 10s/60s/15m 1.96 2.19 288.2 H/s max 1216.8 H/s
[2023-12-25 12:20:12.452]  miner    speed 10s/60s/15m 2.27 2.24 209.5 H/s max 1216.8 H/s
[2023-12-25 12:20:29.480]  net      new job from zeph.kryptex.network:7777 diff 400015 algo rx/0 height 149320
[2023-12-25 12:21:13.731]  miner    speed 10s/60s/15m 2.27 2.24 134.1 H/s max 1216.8 H/s
[2023-12-25 12:22:15.010]  miner    speed 10s/60s/15m 2.06 2.18 77.43 H/s max 1216.8 H/s
[2023-12-25 12:23:16.291]  miner    speed 10s/60s/15m 2.37 2.26 26.50 H/s max 1216.8 H/s
[2023-12-25 12:24:17.518]  miner    speed 10s/60s/15m 1.96 2.13 2.22 H/s max 1216.8 H/s
[2023-12-25 12:24:40.570]  net      new job from zeph.kryptex.network:7777 diff 400015 algo rx/0 height 149321
[2023-12-25 12:25:18.763]  miner    speed 10s/60s/15m 2.17 2.19 2.22 H/s max 1216.8 H/s
[2023-12-25 12:25:33.500]  net      new job from zeph.kryptex.network:7777 diff 400015 algo rx/0 height 149322
[2023-12-25 12:26:07.511]  net      new job from zeph.kryptex.network:7777 diff 400015 algo rx/0 height 149323
[2023-12-25 12:26:22.351]  miner    speed 10s/60s/15m 2.16 2.44 2.24 H/s max 1216.8 H/s
[2023-12-25 12:27:17.791]  net      new job from zeph.kryptex.network:7777 diff 400015 algo rx/0 height 149324
[2023-12-25 12:27:34.196]  miner    speed 10s/60s/15m 2.86 2.62 2.27 H/s max 1216.8 H/s
[2023-12-25 12:27:54.631]  net      new job from zeph.kryptex.network:7777 diff 400015 algo rx/0 height 149325
[2023-12-25 12:28:55.328]  miner    speed 10s/60s/15m 2.27 2.33 2.29 H/s max 1216.8 H/s
[2023-12-25 12:29:56.560]  miner    speed 10s/60s/15m 2.06 2.23 2.29 H/s max 1216.8 H/s
[2023-12-25 12:30:57.799]  miner    speed 10s/60s/15m 2.37 2.41 2.30 H/s max 1216.8 H/s
[2023-12-25 12:31:07.331]  net      new job from zeph.kryptex.network:7777 diff 400015 algo rx/0 height 149326
[2023-12-25 12:31:34.592]  net      new job from zeph.kryptex.network:7777 diff 400015 algo rx/0 height 149327
[2023-12-25 12:31:46.172]  net      new job from zeph.kryptex.network:7777 diff 400015 algo rx/0 height 149328
```

# Discussion History
## SChernykh | 2023-12-25T14:13:23+00:00
It can be Windows running some unwanted background tasks, read https://www.reddit.com/r/MoneroMining/comments/f18825/windows_10_tuning_guide_for_randomx_mining/
Turn off `Memory Compression` and `RunFullMemoryDiagnostic`

# Action History
- Created by: amoiseev | 2023-12-25T09:52:24+00:00
- Closed at: 2025-06-18T22:25:40+00:00
