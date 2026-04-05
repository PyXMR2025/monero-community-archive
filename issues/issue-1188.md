---
title: XMRig crash when mining RandomXL (rx/loki) on ubuntu 14.04
source_url: https://github.com/xmrig/xmrig/issues/1188
author: dragelecpc
assignees: []
labels: []
created_at: '2019-09-22T06:18:36+00:00'
updated_at: '2021-07-20T09:06:21+00:00'
type: issue
status: closed
closed_at: '2019-09-25T09:27:13+00:00'
---

# Original Description
Hi, I'm using xmrig (lastest release) to mine Loki on ubuntu 14.04. But the xmrig process killed after some minute. Do anyone have the same problem with me? And how can i fix it?
Thanks

# Discussion History
## xmrig | 2019-09-22T13:04:50+00:00
Please provide little more information:
1. How you build the miner, this Ubuntu version has no libuv1-dev at least.
2. Hardware information.

Better if you can obtain backtrace of crash using `gdb`.
Thank you.

## dragelecpc | 2019-09-22T14:08:09+00:00
Hi, i used the Binary releases: https://github.com/xmrig/xmrig/releases
try v3.1.3, v3.1.2, v4.0 but all of them crashed after run a minute without any error (just show killed).
Do i need to install any required lib or package?

## xmrig | 2019-09-22T14:32:16+00:00
Check the logs `/var/log/syslog` likely process killed by OOM killer.
Thank you.

## dragelecpc | 2019-09-22T14:43:29+00:00
![failed](https://user-images.githubusercontent.com/39180136/65389583-f73cfe00-dd81-11e9-895f-97c9d313ced0.jpg)
Can you help to check it

## xmrig | 2019-09-22T15:06:48+00:00
How much RAM do you have? `free -h` output, and is it virtual machine?

Disable NUMA support, it should fix the crash https://github.com/xmrig/xmrig/blob/master/src/config.json#L19 but if this is virtual machine autoconfig might wrong.

## dragelecpc | 2019-09-23T03:18:46+00:00
Hi, i disabled NUMA and now the xmrig mining is working now, thank you so much

## oozmark8535 | 2021-02-16T13:20:42+00:00
Sir how to disable the numa i using virtual but i dont know how to edit please help thanks

## wayae222 | 2021-03-29T11:52:35+00:00
how to disable NUMA?

## SChernykh | 2021-03-29T12:16:41+00:00
In config.json: https://github.com/xmrig/xmrig/blob/master/doc/CPU.md#numa

## Xyanc | 2021-07-20T09:06:14+00:00
> Merhaba, NUMA'yı devre dışı bıraktım ve şimdi xmrig madenciliği çalışıyor, çok teşekkür ederim

How did you disable NUMA?

## Xyanc | 2021-07-20T09:06:21+00:00
> Ne kadar RAM'in var? `free -h`çıktı ve sanal makine mi?
> 
> NUMA desteğini devre dışı bırakın, kilitlenmeyi düzeltmelidir https://github.com/xmrig/xmrig/blob/master/src/config.json#L19 ancak bu sanal makine ise otomatik yapılandırma yanlış olabilir.

How did you disable NUMA?

# Action History
- Created by: dragelecpc | 2019-09-22T06:18:36+00:00
- Closed at: 2019-09-25T09:27:13+00:00
