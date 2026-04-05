---
title: Vega64 Reports Hashes / Second of 200K on RandomX
source_url: https://github.com/xmrig/xmrig/issues/1788
author: StrikeAttack
assignees: []
labels: []
created_at: '2020-07-23T10:27:42+00:00'
updated_at: '2020-07-24T21:26:01+00:00'
type: issue
status: closed
closed_at: '2020-07-24T21:26:01+00:00'
---

# Original Description
**Describe the bug**
When using XMRIG 6.3.0 and AMD Radeon Drivers 20.7.2 (Latest as of 7/23/2020), XMRIG reports an aggregate hashrate of close to 200K hashes per second across all GPU cores.

**To Reproduce**
Enable OpenCL and mine RandomX on a Vega64.

**Expected behavior**
Hashes are expected to be around 1K hashes/sec.

**Required data**
 - Miner log as text or screenshot
 - Config fil
<img width="684" alt="2020723 xmrig 200K HashRate" src="https://user-images.githubusercontent.com/45234252/88276747-30e1dc80-cca5-11ea-9f8b-95a2e2480d0d.png">
e or command line (without wallets)
 - OS: Windows 10
 - For GPU related issues: information about GPUs and driver version.

**Additional context**
Add any other context about the problem here.


# Discussion History
## SChernykh | 2020-07-23T20:29:26+00:00
Can you try older driver versions? I think the latest AMD driver broke something again, I'll check it tomorrow.

## SChernykh | 2020-07-24T17:50:22+00:00
I've installed 20.7.2 driver on my PC with Vega 64 and it can mine as usual. Can you try to clear xmrig OpenCL cache in `AppData\Local\xmrig`?

## StrikeAttack | 2020-07-24T21:26:01+00:00
Ah, yes. That does resolve the issue. I would venture that it was the drivers as well. After recompiling what was in the OpenCL cache, there is no longer a problem. I must say that the error'ed hashrate is much more exciting! Almost don't want to fix it.
<img width="674" alt="20200724 XMRIG Repair" src="https://user-images.githubusercontent.com/45234252/88436561-25d49c80-cdca-11ea-8783-568154f0e8b6.png">


# Action History
- Created by: StrikeAttack | 2020-07-23T10:27:42+00:00
- Closed at: 2020-07-24T21:26:01+00:00
