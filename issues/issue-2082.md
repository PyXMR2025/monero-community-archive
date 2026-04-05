---
title: Miner can't continue with the tests
source_url: https://github.com/xmrig/xmrig/issues/2082
author: nadal28
assignees: []
labels:
- invalid
created_at: '2021-02-04T09:30:37+00:00'
updated_at: '2021-02-04T09:40:47+00:00'
type: issue
status: closed
closed_at: '2021-02-04T09:40:47+00:00'
---

# Original Description
**Describe the bug**
I have win7 and all controllers updated, gtx 660 and i5 750, after a fresh install the miner starts with the test, when the gpu test is kawpow it just stops testing because it throws an error
**To Reproduce**
Download https://github.com/MoneroOcean/xmrig/releases/download/v6.8.1-mo2/xmrig-v6.8.1-mo2-win64.zip and extracted,  same for https://github.com/xmrig/xmrig-cuda/releases/download/v6.5.0/xmrig-cuda-6.5.0-cuda9_1-win64.zip
All the files in the same folder. Edit config.json to enable cuda and add my monero wallet.
Open xmrig.exe as adminstrator and the calibration starts, it tests several profiles until reach kawpow, then the error comes and the miner doesn't do anything more

**Expected behavior**
The tests continues and the miner can finally mine

**Required data**
 - Miner log as text or screenshot: https://i.imgur.com/ImklSMz.png
 - Config file or command line (without wallets): open xmrig.exe as adminstrator, no parameters
 - OS: [e.g. Windows] Windows 7 professional 64 bits
 - For GPU related issues: information about GPUs and driver version.: Nvidia gtx 660. Controller 391.35

**Additional context**
Add any other context about the problem here.


# Discussion History
## SChernykh | 2021-02-04T09:36:11+00:00
MoneroOcean version is not the official release, you're asking in the wrong place. Official release doesn't have this functionality.

# Action History
- Created by: nadal28 | 2021-02-04T09:30:37+00:00
- Closed at: 2021-02-04T09:40:47+00:00
