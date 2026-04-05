---
title: Error mining cn/gpu on GTX 1080ti
source_url: https://github.com/xmrig/xmrig/issues/1402
author: UselessGuru
assignees: []
labels: []
created_at: '2019-12-10T14:44:15+00:00'
updated_at: '2020-01-13T09:33:44+00:00'
type: issue
status: closed
closed_at: '2019-12-10T15:10:33+00:00'
---

# Original Description
Version 5.11

Hardware Nvidia GTX 1080Ti, driver version 441.12

Command line:

`XmrigCryptonight-v5.1.1\xmrig.exe --algo=cn/gpu --http-host=127.0.0.1 --http-port=4002 --api-worker-id=Blackbox --url=stratum+tcp://cryptonight_gpu.mine.zergpool.com:4445 --user=******************** --pass=ID=*********,c=BTC --donate-level 1 --cuda-bfactor-hint=8 --no-cpu --no-nvml --cuda --cuda-loader=xmrig-cuda.dll --cuda-devices 0`

**Error thread #0 failed with error <cryptonight_core_gpu_hash_gpu>:846 "too many resources requested for launch"**

Same config with works well on a Nvidia 1060 6GB


# Discussion History
## xmrig | 2019-12-10T15:10:33+00:00
If you interesting to this algorithm use xmr-stak instead.
Thank you.

## UselessGuru | 2019-12-10T15:37:35+00:00
@xmrig 

But why is GTX 1060 6GB working then?

## zonalimitatore | 2020-01-13T09:33:43+00:00
same with 750ti

# Action History
- Created by: UselessGuru | 2019-12-10T14:44:15+00:00
- Closed at: 2019-12-10T15:10:33+00:00
