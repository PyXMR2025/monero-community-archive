---
title: XMRIG Ghostrider GR on 9600x only uses 6 threads
source_url: https://github.com/xmrig/xmrig/issues/3615
author: NisRah
assignees: []
labels: []
created_at: '2025-01-09T16:52:04+00:00'
updated_at: '2025-06-18T22:02:33+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:02:33+00:00'
---

# Original Description
**Describe the bug**
HI, have a b650 and amd r5 9600x with 64gb 6400mhz cl32 ram, running xmrig with ghostrider algorthm
it should be using autoconfig for gr, it only runs with half the threads, i.e 6 threads. unable to get it to run all 12 threads

**To Reproduce**
xmrig.exe --url stratum-eu.rplant.xyz:17056 --user Myadd.mymachine --pass x --algo ghostrider randomx-1gb-pages --cpu-no-yield



**Expected behavior**
Would like it to use all 12 threads and not just 6 threads, attemtpting to use config.json doesnt work either

**Required data**
 - XMRig version 6.22.2
    - Either the exact link to a release you downloaded from https://github.com/xmrig/xmrig/releases
    - Or the exact command lines that you used to build XMRig
 - Miner log as text or screenshot
 - Config file or command line (without wallets)
 - OS: [e.g. Windows]
 - For GPU related issues: information about GPUs and driver version.

**Additional con
[xmrig-log-25-Jan-09_14-54.txt](https://github.com/user-attachments/files/18364623/xmrig-log-25-Jan-09_14-54.txt)
text**
Add any other context about the problem here.
if you can please also supply me with a config.json for further testing, ive tried that as well but xmrig did not accept the json i created

# Discussion History
## NisRah | 2025-01-09T16:53:02+00:00
using win11 pro

## SChernykh | 2025-01-09T17:44:44+00:00
XMRig runs 2 threads per 1 "reported" thread for Ghostrider. You should see higher than 50% usage when mining Ghostrider.

## NisRah | 2025-01-10T15:45:24+00:00
thank you, is 1gb pages capable of working in win11 pro? been struggling to enable it


## SChernykh | 2025-01-10T15:47:53+00:00
No, 1gb pages are only available on Linux. But from what I know, Windows 10/11 use 1gb pages transparently in the background, so you don't need to enable them.

## NisRah | 2025-01-11T19:54:49+00:00
thank you all so much so far....
okay, the expected has rate for 9600x is 4000kh, im only getting 2000 kh, half that, any advice?>

## SChernykh | 2025-01-12T08:05:17+00:00
GhostRider doesn't have a fixed hashrate, it depends a lot on the selection of 3 algorithms for each cycle.

## NisRah | 2025-01-22T14:06:14+00:00
yesh thats true, thank you, the average hashrate im getting is 2000 kh to 2300 kh, the expected hashrate on average for the 9600 is about 4000kh?

## SChernykh | 2025-01-22T15:57:31+00:00
Where did you find this "4000" number? But in any case, you should check that nothing else is using CPU when you're mining.

## NisRah | 2025-02-17T11:54:22+00:00
optimal setting, 80 w(entire machine wow, prob 55w cpu) 5195 hz and 1.125v giving out 2405.8 h/s average, think thats it for this cpu, ill look at adding a 9950x next to test 

# Action History
- Created by: NisRah | 2025-01-09T16:52:04+00:00
- Closed at: 2025-06-18T22:02:33+00:00
