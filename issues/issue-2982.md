---
title: dont run cmd parameter
source_url: https://github.com/xmrig/xmrig/issues/2982
author: snipeTR
assignees: []
labels: []
created_at: '2022-03-21T07:22:49+00:00'
updated_at: '2022-03-21T09:27:46+00:00'
type: issue
status: closed
closed_at: '2022-03-21T09:22:40+00:00'
---

# Original Description
input:

> -DWITH_TLS=OFF
-DWITH_ASM=OFF
-DWITH_OPENCL=OFF
-DWITH_CUDA=OFF
-DWITH_NVML=OFF
-DWITH_ADL=OFF
-DWITH_BENCHMARK=OFF
-DWITH_CN_LITE=OFF
-DWITH_CN_HEAVY=OFF
-DWITH_CN_PICO=OFF
-DWITH_CN_FEMTO=OFF
-DWITH_RANDOMX=OFF
-DWITH_ARGON2=OFF
-DWITH_KAWPOW=OFF
-DWITH_GHOSTRIDER=OFF

cmake .. -G "Unix Makefiles" -DXMRIG_DEPS=c:/xmrig-deps/gcc/x86 -DWITH_TLS=OFF -DWITH_ASM=OFF -DWITH_OPENCL=OFF -DWITH_CUDA=OFF -DWITH_NVML=OFF -DWITH_ADL=OFF -DWITH_BENCHMARK=OFF -DWITH_CN_LITE=OFF -DWITH_CN_HEAVY=OFF -DWITH_CN_PICO=OFF -DWITH_CN_FEMTO=OFF -DWITH_RANDOMX=OFF -DWITH_ARGON2=OFF -DWITH_KAWPOW=OFF -DWITH_GHOSTRIDER=OFF
make 

output:

>https://pastebin.com/8dKFv0YW

![image](https://user-images.githubusercontent.com/31975916/159218577-565609bb-14c7-4eb4-877d-1fa4af3392f6.png)


# Discussion History
## SChernykh | 2022-03-21T09:05:53+00:00
astrobwt/v2 requires TLS

## snipeTR | 2022-03-21T09:27:46+00:00
Can a warning message be added to the cmake script? For "-DWITH_TLS=OFF".

# Action History
- Created by: snipeTR | 2022-03-21T07:22:49+00:00
- Closed at: 2022-03-21T09:22:40+00:00
