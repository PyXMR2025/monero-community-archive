---
title: Failed to load OpenCL runtime this is not bug && unofficial issue
source_url: https://github.com/xmrig/xmrig/issues/1978
author: Saikatsaha1996
assignees: []
labels: []
created_at: '2020-12-15T05:22:34+00:00'
updated_at: '2020-12-21T10:25:32+00:00'
type: issue
status: closed
closed_at: '2020-12-16T08:19:33+00:00'
---

# Original Description
**Describe the bug**
Not bug

**To Reproduce**
Steps to reproduce the behavior.

**Expected behavior**
A clear and concise description of what you expected to happen.

**Required data**
 - Miner log as text or screenshot
 - Config file or command line (without wallets)
 - OS: [e.g. Windows]
 - For GPU related issues: information about GPUs and driver version.

**Additional context**
Add any other context about the problem here.
![Screenshot_20201214-184632](https://user-images.githubusercontent.com/72664192/102174306-2548b980-3ec3-11eb-839a-123fedd54562.png)
![Screenshot_20201215-104718](https://user-images.githubusercontent.com/72664192/102174315-2843aa00-3ec3-11eb-8887-655e30635b36.png)
![Screenshot_20201214-195733](https://user-images.githubusercontent.com/72664192/102174316-28dc4080-3ec3-11eb-9239-94dcf3465b89.png)

Android mobile
Android 10
Ram 6gb
Gpu Qualcomm Adreno TM 514
In my device already available OpenCL 2.0
But i face problem with failed to load OpenCL runtime
This is testing purposes only
Please help me
How can i solve it?
![Screenshot_20201214-182224](https://user-images.githubusercontent.com/72664192/102182573-81ffa080-3ed2-11eb-8daf-53f06898c867.png)


# Discussion History
## Saikatsaha1996 | 2020-12-15T07:08:19+00:00
No one available for help 😑

## FrankHB | 2020-12-21T10:25:32+00:00
The default library name `libOpenCL.so` is hard-coded in `xmrig::OclLib::defaultLoader`. Seems a different name?


# Action History
- Created by: Saikatsaha1996 | 2020-12-15T05:22:34+00:00
- Closed at: 2020-12-16T08:19:33+00:00
