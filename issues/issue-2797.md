---
title: Instance Terminated
source_url: https://github.com/xmrig/xmrig/issues/2797
author: 21CreativeMedia
assignees: []
labels: []
created_at: '2021-12-06T13:35:35+00:00'
updated_at: '2021-12-07T09:02:58+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Im Using xmrig-6.16.2-linux-static-x64.tar.gz
After Runing ./xmrig.sh the instance instantly terminated
Currently Using Xeon Platinum 8380 ICE LAKE
Problem was completely gone while using xmrig-6.16.2-linux-x64.tar.gz
Any Help?

# Discussion History
## Lonnegan | 2021-12-06T22:57:16+00:00
You have an Ice-Lake based CPU mit VAES support? The static version of the xmrig binaries are using the VAES instructions, the dynamic one doesn't. So there must be still something wrong, hence there were fixes regarding VAES in the latest release.

What did you want to mine? RandomX? GhostRider?

## 21CreativeMedia | 2021-12-07T07:58:50+00:00
Yes im trying to mine RTM on FlockPool with GhostRider algo. i've read VAES optimizations not supported by xmrig-6.16.2-linux-x64.tar.gz due old compiler, so im using xmrig-6.16.2-linux-static-x64.tar.gz instead. 
but it failed to run on my system,  

been tried on Ryzen 9 5950X and its seem working fine, so  i think there was a problem with Ice Lake Microarch or smth?

## Lonnegan | 2021-12-07T09:02:58+00:00
> been tried on Ryzen 9 5950X and its seem working fine, so i think there was a problem with Ice Lake Microarch or smth?

Well, the devs of xmrig have a Ryzen 5 5600X as their personal computer, so bugs or errors are immediately obvious. They don't have an Ice-Lake system as far as I know, so it's untested there. Perhaps you can help them to find the glitch in the code in combination with Ice Lake :-)

# Action History
- Created by: 21CreativeMedia | 2021-12-06T13:35:35+00:00
