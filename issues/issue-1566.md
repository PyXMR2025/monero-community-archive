---
title: Trouble with s775 and huge pages 11/100%
source_url: https://github.com/xmrig/xmrig/issues/1566
author: ValoWaking
assignees: []
labels:
- question
created_at: '2020-02-23T13:09:53+00:00'
updated_at: '2020-08-28T16:41:07+00:00'
type: issue
status: closed
closed_at: '2020-08-28T16:41:07+00:00'
---

# Original Description
Hi, i have trouble with s775 and huge pages 11/100%
I have 4gb RAM and "huge pages permission granted" but huge pages loaded less than 10%
any fix?

forgot, cpu - q6600, possible use 4 threads

# Discussion History
## xmrig | 2020-02-23T23:08:27+00:00
https://xmrig.com/docs/miner/hugepages 

> Please note on Windows no way to reserve huge pages for future use and the miner still can fail to allocate all required huge pages, because other applications use memory, if you got less than 100% of huge pages best option is reboot.

Also please check https://www.reddit.com/r/MoneroMining/comments/f18825/windows_10_tuning_guide_for_randomx_mining/

## ValoWaking | 2020-02-23T23:29:01+00:00
That PC has win7x64. I also try start miner after reboot - and have same result. Also i try run miner with Admin rights. Usage memory after run windows is 700MB, totally i have 3300MB free memory.

## Spudz76 | 2020-02-24T22:31:05+00:00
4GB is tight, you may have to boot with most startup garbage disabled (virus scanners, etc, wasting memory before you can launch miner).

## ValoWaking | 2020-02-24T22:46:57+00:00
i didn't have any garbage virus scanners, etc. After Windows load i have 3.3GB free memory. Miner needs 2.3GB

## Spudz76 | 2020-02-24T22:53:45+00:00
Yes but, you want 2.3GB of hugepages.  One app loading at startup could allocate even one small page in the middle of that 2.3GB and then you get no hugepages.  Has to be contiguous memory.  Startup apps don't need to be large just allocating before miner has a chance to reserve.

## ValoWaking | 2020-02-24T23:28:15+00:00
I do cleaned my autostart from all and disable some unneeded windows services, it's no fix. Maybe try to install some linux distro and try "1GB linux huge pages"?

## Spudz76 | 2020-03-21T22:45:24+00:00
That probably won't work either, you have to reserve 3*1GB pages (with kernel args so it's done before userspace starts) which means entire system has to fit in 1GB remaining.  You don't get to use the leftover part of the third GB then (blowing 3GB for 2.3 usage, lose 700MB).  But it could work with normal 2MB hugepages but still maybe not.

4GB is really really really tight like probably not enough.

# Action History
- Created by: ValoWaking | 2020-02-23T13:09:53+00:00
- Closed at: 2020-08-28T16:41:07+00:00
