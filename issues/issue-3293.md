---
title: KawPow failed to initialize DAG
source_url: https://github.com/xmrig/xmrig/issues/3293
author: Autonetic
assignees: []
labels: []
created_at: '2023-07-03T10:01:25+00:00'
updated_at: '2025-06-18T22:46:48+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:46:48+00:00'
---

# Original Description
**XMRig - KawPow failed to initialize DAG**
Cant seem to get this stupid gt 630m to mine anything at all, but it looked like it almost wanted to do something with xmrig and kawpow, however it accepts a job, gets the gpu ready and then sends an error and mines with n/a hash rate

**error message:**
[2023-07-03 19:30:12.940]  nvidia   KawPow failed to initialize DAG: <kawpow_prepare>:86 "no kernel image is available for execution on the device"

**Expected behavior**
A clear and concise description of what you expected to happen.

**Required data**
 - Screenshot bellow
 - Config file or command line (without wallets):
`cd %~dp0
xmrig.exe --no-cpu --cuda -a kawpow -o neox.2miners.com:4040 -u wallet.rig0 -p x
pause
`
 - OS: Windows 10
 - GPU - nVidia GT630m 2gb


![kawpowissue1](https://github.com/xmrig/xmrig/assets/117817490/8b126e9f-0f8e-49be-b32b-29e552510ec5)


# Discussion History
## SChernykh | 2023-07-03T10:39:37+00:00
It doesn't have enough RAM to mine KawPow. I think you need at least 4 GB GPU for this.

## Spudz76 | 2023-07-05T04:04:31+00:00
Also Arch21 requires CUDA8.0 maximum, and is not available in the release builds because those are so old, so you have to compile it.  Then it might work with stuff that doesn't need 4GB+

## Spudz76 | 2023-07-05T04:07:39+00:00
Oh and even if it had 32GB, Kawpow (and RandomX) don't work with less than CUDA 9.0 because of missing features.

## heliosgnosis | 2023-07-27T00:32:21+00:00
It is the open CL being too low of a version, with mining a 4gb GTX 730 around about is the age of gpu that "could work" been down this road with every gpu to pass through my hands and the new forks from kawpow are always the reason ppl think but no it is the CL version and age so compatible with the gpu that is usually always the prob of this one and those similar.

# Action History
- Created by: Autonetic | 2023-07-03T10:01:25+00:00
- Closed at: 2025-06-18T22:46:48+00:00
