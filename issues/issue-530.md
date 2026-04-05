---
title: Wrong thread detection on E7400
source_url: https://github.com/xmrig/xmrig/issues/530
author: snipeTR
assignees: []
labels: []
created_at: '2018-04-09T15:18:11+00:00'
updated_at: '2019-08-02T12:51:54+00:00'
type: issue
status: closed
closed_at: '2019-08-02T12:51:54+00:00'
---

# Original Description
Hello There,

I was using v2.4.3 to mine XMR and v2.43 was detecting thead count right which is 2 threads for **Intel E7400** CPU. After I upgrade miner to 2.5.2 or 2.6 thread detection does not detects the thead count correctly. It sets the thead count to **1** but it should be **2**. You can see the screenshots between versions with same conig file below. 

PS: Thead count setted to null or "all" wont affects the result.

Thanks in advance

v2.4.3
![image](https://user-images.githubusercontent.com/31975916/38506269-0ba713e2-3c22-11e8-9ecc-ce6c28fb45cf.png)
v2.5.2
![image](https://user-images.githubusercontent.com/31975916/38506286-11235628-3c22-11e8-91e9-cbab86c0bcd1.png)
v2.6
![image](https://user-images.githubusercontent.com/31975916/38506292-14e51c10-3c22-11e8-82a2-1ce2b015aa75.png)


# Discussion History
## NmxMilk | 2018-04-10T08:26:37+00:00
The newer version are reporting 3MB cache while older version was reporting 6MB.
The rule is each thread needs 2MB of cache for optimal performance.
https://ark.intel.com/fr/products/36500/Intel-Core2-Duo-Processor-E7400-3M-Cache-2_80-GHz-1066-MHz-FSB?q=Intel%20E7400
report 3MB cache only !
BTW, you can override the value xmrig uses with the -t option. (or in config file).
Your proc does not have aes and should give you poor performance. 
I guess that should be around 30 H/S. Maybe with 2 threads you get a bit more ~40 H/S but that will not double your hashrate (unefficient).





## snipeTR | 2018-04-11T08:28:17+00:00
Ok, I understand that detail and realized why its using 1 thread on my machine. However is it possible to force it to maximum thread even it is unefficient? I need this feature because I have lots of machines with different specs and I want to use maximum thread on each machine with same config without concerning with its cpu or thread count etc. Is it possible to create that feature with actual versions or future versions.

## NmxMilk | 2018-04-11T14:15:43+00:00
As i have said previously:
you can override the value xmrig uses with the -t option. (or in config file).

## marcel1974 | 2018-04-14T05:40:18+00:00
I also have the same problem... I have 60 miners all with different config files. I wget the new  xmrig and config.json from my proxy....that is until the next mining disaster "cryptonight-heavy" crash /disaster

# Action History
- Created by: snipeTR | 2018-04-09T15:18:11+00:00
- Closed at: 2019-08-02T12:51:54+00:00
