---
title: xmrig 6.16
source_url: https://github.com/xmrig/xmrig/issues/2724
author: Macacul
assignees: []
labels: []
created_at: '2021-11-26T20:58:56+00:00'
updated_at: '2021-12-19T15:37:32+00:00'
type: issue
status: closed
closed_at: '2021-12-19T15:37:32+00:00'
---

# Original Description
**Describe the bug**
on my system start at 16k - 17k but in few minutes drop to 9k, or sometiome to 600 h/s. this is the behavior on version 6.15 too.
for example, with xmrig 6.10 this don't happend.

**To Reproduce**
i only let them run.

**Expected behavior**
what i expect is to stay at same  rate all the tiem (16k to 17k)

**Required data**

 - Config file or command line (without wallets):xmrig.exe -o xmr-eu1.nanopool.org:14433 -u wallet.worker/e-mail--tls --coin monero --cpu-priority 0
 - win 10 pro last updets 



# Discussion History
## SChernykh | 2021-11-26T21:04:26+00:00
https://xmrig.com/docs/miner/randomx-stability-troubleshooting-guide
> Other causes of low hashrate can be Windows background tasks running, especially memory compression and RunFullMemoryDiagnostic task. You can check [Windows 10 tuning guide ](https://www.reddit.com/r/MoneroMining/comments/f18825/windows_10_tuning_guide_for_randomx_mining/) to find out how to turn them off.

## Macacul | 2021-11-26T21:33:32+00:00
are off. is strange why in 6.10 this don't happend

## Lonnegan | 2021-11-27T13:58:55+00:00
CPU priority 0 is one of the reasons why it happens. Since Windows 10 version 1903 Microsoft has changed the process scheduler,  a known issue long before version 6.16 or 6.10. See:
https://github.com/xmrig/xmrig/issues/1506#issuecomment-593678237
With 1809 and older I never had thoses problems.

You can fix it, when you don't reduce the process priority and let the scheduler choose the right cores, so don't set fixed cores in the config, but instead set -1 so that the scheduler can deside.

Interestingly it is not the case with every CPU model. AMD FX-8300 (Vishera), Ryzen 5 1600, 2700 (Pinnacle Ridge) and 3700X (Matisse) are affected as well as Intel Core i5 11400 (Rocket Lake), but Ryzen 3 2200G isn't, despite of priority 0 and fixed cores.

I gave up to dive even deeper. I've understood the reason and how I can fix it for myself. Everything other is wasted time. But when 6.10 works fine for you, just use it :)

## Macacul | 2021-11-27T14:56:31+00:00
Thanks for answering. I use cpu priority ) only for version newest than 6.10 because all those version affect other mining programs.  Version 6.10 has same cmd without  cpu priority. 
Thanks again.

# Action History
- Created by: Macacul | 2021-11-26T20:58:56+00:00
- Closed at: 2021-12-19T15:37:32+00:00
