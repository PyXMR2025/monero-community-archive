---
title: MSR not available after cmake options
source_url: https://github.com/xmrig/xmrig/issues/2767
author: ShazAu
assignees: []
labels:
- question
created_at: '2021-12-01T11:38:59+00:00'
updated_at: '2021-12-19T15:13:14+00:00'
type: issue
status: closed
closed_at: '2021-12-19T15:13:14+00:00'
---

# Original Description
**Describe the bug**
When using cmake options to remove unused algorithms and features for RTM mining, MSR is no longer listed during miner startup

**To Reproduce**
Building in windows using MSYS2
CMAKE Command line:
"c:\Program Files\CMake\bin\cmake.exe" .. -G "Unix Makefiles" -DXMRIG_DEPS=c:/xmrig-deps/gcc/x64 -DWITH_RANDOMX=OFF -DWITH_ARGON2=OFF -DWITH_ASTROBWT=OFF -DWITH_KAWPOW=OFF -DWITH_OPENCL=OFF -DWITH_CUDA=OFF -DWITH_PROFILING=OFF

**Expected behavior**
I expected the custom cmake would disable the following algorithms: randomx, argon2, astrobwt and kawpow
I expected the custom cmake would disable OpenCL, Cuda, Dev Profiling
I expected all other functions such as MSR would stay intact.


**Required data**
 - Miner log as text or screenshot: sorry don't have one, runs as per normal but there no line about MSR during miner startup.
 - Config file or command line (without wallets):
 - cd %~dp0
xmrig.exe -a gr -o asia.flockpool.com:5555 --tls -u WALLET -p x
pause
 - OS: [e.g. Windows]: Win10

**Additional context**
I thought the miner might be slightly faster if I compiled it with less algorithms and features enabled.

PC Specs:  Win10(20H2), Ryzen 5 3600, MSI B450 Mortar Max, 16GB (2x8) 3600Mhz, Noctua UH12S


# Discussion History
## SChernykh | 2021-12-01T12:07:05+00:00
MSR requires RandomX to work.

## ShazAu | 2021-12-01T20:47:01+00:00
> MSR requires RandomX to work.

Thanks, I'll give this a go!

## ShazAu | 2021-12-03T07:14:45+00:00
MSR is now working after enabling RandomX.  I changed the Cmake command to:
"c:\Program Files\CMake\bin\cmake.exe" .. -G "Unix Makefiles" -DXMRIG_DEPS=c:/xmrig-deps/gcc/x64 -DWITH_ASTROBWT=OFF -DWITH_KAWPOW=OFF -DWITH_OPENCL=OFF -DWITH_CUDA=OFF -DWITH_PROFILING=OFF -DWITH_BENCHMARK=OFF

Please let me know if there is any further optimisations I can perform.

# Action History
- Created by: ShazAu | 2021-12-01T11:38:59+00:00
- Closed at: 2021-12-19T15:13:14+00:00
