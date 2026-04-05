---
title: Hashrate Randomsfx going Down
source_url: https://github.com/xmrig/xmrig/issues/1621
author: jgonzis
assignees: []
labels:
- stability
created_at: '2020-03-27T09:40:06+00:00'
updated_at: '2020-08-31T05:47:23+00:00'
type: issue
status: closed
closed_at: '2020-08-31T05:47:22+00:00'
---

# Original Description
**Describe the bug**
The miner is working properly, but the hashrate goes down.

**To Reproduce**
I cannot answer that, because it happens… I only found that if I forces pushing the h hashrate, it comes back.

It is going from 1600 to 3200 double when I push the h other automatic with time and also goes from 3200 to 1600 without any reason.

**Expected behavior**
The hashrate should maintence stable… 

**Required data**
It is a Ryzen 7 2700 with Windows 10. Using         "rx": [3, 5, 7, 9, 11, 13, 15], I use in the other cores 0,2,4,6,8,10,12 other miner Verushash miner. 


**Additional context**
![RandomSFX](https://user-images.githubusercontent.com/38668405/77742410-b8308380-7016-11ea-9264-417322ade458.jpg)
![RandomSFX2](https://user-images.githubusercontent.com/38668405/77742413-b8c91a00-7016-11ea-9216-54e849b61da2.jpg)




# Discussion History
## Lonnegan | 2020-03-28T23:17:41+00:00
> It is a Ryzen 7 2700 with Windows 10. Using "rx": [3, 5, 7, 9, 11, 13, 15], I use in the other cores 0,2,4,6,8,10,12 other miner Verushash miner.
> 
You know that Ryzen 7 only has 8 "real" cores? It has 16 logical cores due to SMT, which means, that SMT pretends the software, the CPU had 16 cores, but in reality the two logical cores of each real core have to share resources. This technique is implemented to realize higher utilization of the compute units.

But: if you run two different miners at the same time, one on the odd the other on the even logical cores, it is normal, that the hashrates will vary heavily. Sometimes the miner on the odd logical cores will get more of the real resources, sometimes the miner on the even logical cores will.

## jgonzis | 2020-03-28T23:47:38+00:00
I will prove it and say you the results. Normally goes perfect using the logic for XmRig. It was only strange that pushing the h for hashrate automaticly return the normal results. With this solution I know I lose 20% of hash rate for Randomsfx, from 4200 to 3400, but I got lot more than the lost. I suppose it is complicated to make this dual miner automaticky...

## xmrig | 2020-08-31T05:47:22+00:00
https://xmrig.com/docs/miner/randomx-stability-troubleshooting-guide

# Action History
- Created by: jgonzis | 2020-03-27T09:40:06+00:00
- Closed at: 2020-08-31T05:47:22+00:00
