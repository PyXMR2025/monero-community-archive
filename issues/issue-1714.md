---
title: Low hashrate with AMD FX 6350
source_url: https://github.com/xmrig/xmrig/issues/1714
author: Vivilatulipe
assignees: []
labels: []
created_at: '2020-06-06T13:27:25+00:00'
updated_at: '2020-06-06T18:52:42+00:00'
type: issue
status: closed
closed_at: '2020-06-06T18:52:42+00:00'
---

# Original Description
Hi everybody,

I just tried XMRig yesterday, and i saw something unusual...
I used an Amd fx 6350 -6 Core and 8 Go RAM on XMRig 5.11.2 on W7 and it shows me:
![15914495504172682017118707771512](https://user-images.githubusercontent.com/26848402/83945164-2197f400-a809-11ea-8ce1-becce92aafb5.jpg)

Is that possible to have to have that max hashrate??

I did not put any spécial parameters on the configuration file, i used the xmrig config for cpu miner on web.

Thanks for help.

Vivilatulipe 

PS: Sorry for english 


# Discussion History
## downystreet | 2020-06-06T15:20:22+00:00
I've noticed that on some AMD processors, when you start mining and the config.json file gets prefilled, it's not set at the optimal setting. Open your config.json file and go to "cpu": . Below this you will see the different algorithms listed out. Go to "rx": . I noticed on a 4 core AMD processor I was using it was prefilled with [-1,-1] which was not the optimal config because it was only using 2 cores instead of 4 and giving me a lower hashrate. With your particular processor you will need to manually enter this into the file where the "rx" is "rx": [0, 1, 2, 3, 4, 5]. This is the setting for using all six cores of your processor. You can adjust accordingly by removing a number to use less cores.

Update: Looking at your hash rate, that might be the max for an fx 6350 processor but I'm not 100% sure. That's an older processor, so while it has 6 cores it only has 8MB of L3 cache which is important for randomX mining. So check out the config.json file. If it looks like what I said with "rx": [0, 1, 2, 3, 4, 5] then you are running at the max settings.

## Vivilatulipe | 2020-06-06T16:37:06+00:00
Thanks! That's working perfectly!

![15914612636282610577163013753772](https://user-images.githubusercontent.com/26848402/83949495-6bda9e80-a824-11ea-8726-c435f55ab48f.jpg)

With ram clock adjustments,  i think it will increase a lil bit more.
Thx.

# Action History
- Created by: Vivilatulipe | 2020-06-06T13:27:25+00:00
- Closed at: 2020-06-06T18:52:42+00:00
