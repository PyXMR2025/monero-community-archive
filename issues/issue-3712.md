---
title: error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
source_url: https://github.com/xmrig/xmrig/issues/3712
author: minerminer1950
assignees: []
labels: []
created_at: '2025-09-24T03:26:28+00:00'
updated_at: '2025-09-26T02:09:09+00:00'
type: issue
status: closed
closed_at: '2025-09-26T02:09:09+00:00'
---

# Original Description
**Describe the bug**
I need to confirm if this was fixed on the latest version. 
[2025-09-24 10:48:48.390]  opencl   error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
[2025-09-24 10:48:48.392]  opencl   thread #0 failed with error CL_INVALID_PROGRAM
[2025-09-24 10:48:48.404]  opencl   thread #0 self-test failed
[2025-09-24 10:48:48.408]  opencl   disabled (failed to start threads)

**To Reproduce**
Run  .\xmrig.exe -o 127.0.0.1:3333 --opencl

**Expected behavior**
opencl will create one thread for mining

**Required data**
 - XMRig version
    - 6.24.0
 - Miner log as text or screenshot
<img width="859" height="732" alt="Image" src="https://github.com/user-attachments/assets/8d507983-c206-4a8c-a15b-ea21287f0045" />
 - Config file or command line (without wallets)
 .\xmrig.exe -o 127.0.0.1:3333 --opencl
 - OS: Windows 10
 - For GPU related issues: information about GPUs and driver version.
AMD Athlon 200GE Vega 3 driver version 25.8.1

**Additional context**
Add any other context about the problem here.


# Discussion History
## SChernykh | 2025-09-24T07:29:07+00:00
It's not supported anymore because mining RandomX on GPU is too slow. Especially integrated GPU - even if it works, you will only get lower overall hashrate. If you really want to try OpenCL RandomX mining, it will work with Adrenaline drivers from late 2019-early 2020, but don't expect more than a couple hundred h/s from the integrated GPU.

## minerminer1950 | 2025-09-26T02:09:09+00:00
Thanks for confirming. I am closing this issue.

# Action History
- Created by: minerminer1950 | 2025-09-24T03:26:28+00:00
- Closed at: 2025-09-26T02:09:09+00:00
