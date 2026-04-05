---
title: Hash speed drops
source_url: https://github.com/xmrig/xmrig/issues/2480
author: Valtsuh
assignees: []
labels: []
created_at: '2021-07-09T13:56:31+00:00'
updated_at: '2021-07-11T19:12:10+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hello, I'm not really sure to as to where to post, but my hash speed seems to just drop overtime, eventually going all the way down to under 1h/s (from 400 ish / thread (laptop), max. roughly 1200 with 3-4 threads). 

Any help?

# Discussion History
## SChernykh | 2021-07-09T13:59:09+00:00
https://xmrig.com/docs/miner/randomx-stability-troubleshooting-guide

## Valtsuh | 2021-07-09T14:37:43+00:00
> https://xmrig.com/docs/miner/randomx-stability-troubleshooting-guide

> The only known workaround for this is to unpin threads from cores

After just opening the config file for the miners, 

>was changed, reloading configuration

Although the config file was only opened (maybe a quick tweak?), opening the file isn't exactly modifying the file, anyway, the speed does seem to bump up, maybe the miner isn't refreshing itself as it should, certainly would seem like it?
![detox xmrig speed](https://user-images.githubusercontent.com/77432892/125094267-ca371800-e0db-11eb-8f96-2c1e08cd3503.jpg)

I tried quick unpinning, pinning, but just refreshing the config seemed to work the most. I'll try again once I notice the speed dropping (if drops) down to near 0.

## SChernykh | 2021-07-09T14:40:02+00:00
You didn't read the full guide, better workaround is to turn off memory compression and RunFullMemoryDiagnostic tasks.

## Valtsuh | 2021-07-09T15:06:17+00:00
Yeah I don't know if doing that made any difference, the speed just seems wavy, doesn't seem to stabilize at all.

i7-8565U Gen 8
>GenuineIntel Family 6 Model 142 Stepping 12
>Socket 1356 FCBGA
>Kaby Lake-U/Y
>North: Intel ID3E34 0C
>South: Intel Coffee Lake-U/Y PCH 30

>16GB DDR4

Note: My own application could be interfering with the hashing, maybe something to do with thread switching?
>https://github.com/Valtsuh/Detox

## Valtsuh | 2021-07-09T19:29:47+00:00
Been running a few hours now, hashrate very low, with the above mentioned advice. 

## Shai0Hulud | 2021-07-11T11:29:45+00:00
It's a laptop? I would guess that Overheat protection kicks in. 

And depending on electricity costs, not sure if it's really worth it with a hashrate like this

## Valtsuh | 2021-07-11T19:11:50+00:00
> It's a laptop? I would guess that Overheat protection kicks in. 
> 
> And depending on electricity costs, not sure if it's really worth it with a hashrate like this

I'm not too worried 'bout electricity costs, thought about getting an ant. If I can get to withdrawing the coins i'm fine with it. 400(BTT) limit at unmineable. GAS running aswell, seems a lot for just one coin. Considering the site bases on rewarding as they mention "mining". Not sure if the reward rate increases or decreases with hashrate, seems constant.

# Action History
- Created by: Valtsuh | 2021-07-09T13:56:31+00:00
