---
title: Issues running on dual socket system
source_url: https://github.com/xmrig/xmrig/issues/177
author: Tualua
assignees: []
labels:
- NUMA
created_at: '2017-10-26T15:58:22+00:00'
updated_at: '2019-08-02T12:38:00+00:00'
type: issue
status: closed
closed_at: '2019-08-02T12:38:00+00:00'
---

# Original Description
Hi! First of all, thanks for your great job!

Just downloaded you miner to try to replace stak. I have noticed that performance is lower than stak.
I have 2-node Quanta Windmill with 2*E5-2650v1 on each node.
Nodes are running Windows 7

stak node gives about 790H/s on 10 threads for each CPU (8 for physical cores, 2 for virtual cores, total of 20)
Tried XMRig ang got interesting results.
First, I tried 20 threads with mask 0x555F555F. It gave me around 745 H/s, but CPU was load only for 56% (stak loads came CPU for 62%) and only 18 cores was fully loaded. I checked threads performance over API and found that 2-3 threads with performance significantly lower - about 13-17 H/s , while other are 35-43 H/s. Using stak all 20 threads are 36-42 H/s

I started to google and found issues with NUMA and tried to run 2 instances of XMRig (start /node 0 and start /node 1)
Again I got almost same results. 19 cores with full load and 390+370=760 H/s

`start /node 0 xmrig_msvc.exe --url=de02.supportxmr.com:7777 --user=xxx --pass=x --threads=10 --av=1 --keepalive --retries=5 --retry-pause=5 --cpu-affinity=0x555F --donate-level=1 --print-time=10 --api-port=63418`

`start /node 1 xmrig_msvc.exe --url=de02.supportxmr.com:7777 --user=xxx --pass=x --threads=10 --av=1 --keepalive --retries=5 --retry-pause=5 --cpu-affinity=0x555F0000 --donate-level=1 --print-time=10 --api-port=63419
`
![xmrig](https://user-images.githubusercontent.com/32481693/32063256-459351f6-baa9-11e7-97da-f4d43aea83b8.PNG)

Am I doing something wrong? 

# Discussion History
## xmrig | 2017-10-26T16:48:32+00:00
stak currently has much better NUMA nodes support, see related issues: #86.
Also looks like need different mask, cpu numbers for second CPU/node core numbers can be not sequential. Can please show `cpu_threads_conf` from stak config.
Thank you.

## Tualua | 2017-10-27T01:11:17+00:00
Thanks, could you advise me proper mask?

stak threads:
"cpu_thread_num" : 20,
"cpu_threads_conf" :
[
   { "low_power_mode" : false, "no_prefetch" : true, "affine_to_cpu" : 0 },
   { "low_power_mode" : false, "no_prefetch" : true, "affine_to_cpu" : 1 },
   { "low_power_mode" : false, "no_prefetch" : true, "affine_to_cpu" : 2 },
   { "low_power_mode" : false, "no_prefetch" : true, "affine_to_cpu" : 3 },
   { "low_power_mode" : false, "no_prefetch" : true, "affine_to_cpu" : 4 },
   { "low_power_mode" : false, "no_prefetch" : true, "affine_to_cpu" : 6 },
   { "low_power_mode" : false, "no_prefetch" : true, "affine_to_cpu" : 8 },
   { "low_power_mode" : false, "no_prefetch" : true, "affine_to_cpu" : 10 },
   { "low_power_mode" : false, "no_prefetch" : true, "affine_to_cpu" : 12 },
   { "low_power_mode" : false, "no_prefetch" : true, "affine_to_cpu" : 14 },

   { "low_power_mode" : false, "no_prefetch" : true, "affine_to_cpu" : 16 },
   { "low_power_mode" : false, "no_prefetch" : true, "affine_to_cpu" : 17 },
   { "low_power_mode" : false, "no_prefetch" : true, "affine_to_cpu" : 18 },
   { "low_power_mode" : false, "no_prefetch" : true, "affine_to_cpu" : 19 },
   { "low_power_mode" : false, "no_prefetch" : true, "affine_to_cpu" : 20 },
   { "low_power_mode" : false, "no_prefetch" : true, "affine_to_cpu" : 22 },
   { "low_power_mode" : false, "no_prefetch" : true, "affine_to_cpu" : 24 },
   { "low_power_mode" : false, "no_prefetch" : true, "affine_to_cpu" : 26 },
   { "low_power_mode" : false, "no_prefetch" : true, "affine_to_cpu" : 28 },
   { "low_power_mode" : false, "no_prefetch" : true, "affine_to_cpu" : 30 },

![stak20171027](https://user-images.githubusercontent.com/32481693/32083698-2fa550ee-baf7-11e7-8721-f44e2d917d92.PNG)



## Tualua | 2017-10-27T01:19:51+00:00
Hmm. Checked again 3 minutes ago. Now 20 cores working

![xmrig20171027](https://user-images.githubusercontent.com/32481693/32083792-f415cc38-baf7-11e7-9b1d-0a2c5e08f6df.PNG)

![xmrig_cpuload](https://user-images.githubusercontent.com/32481693/32083796-fad772b0-baf7-11e7-93d8-4332014badd7.PNG)



## xmrig | 2017-10-27T09:40:47+00:00
Mask looks good, at least it equal to stak config.

## xmrig | 2019-07-29T02:19:31+00:00
If this issue still actual, please check v2.99.2-beta release #1077.
Thank you.

# Action History
- Created by: Tualua | 2017-10-26T15:58:22+00:00
- Closed at: 2019-08-02T12:38:00+00:00
