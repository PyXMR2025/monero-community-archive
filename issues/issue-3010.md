---
title: Why i don't have any acceptions?
source_url: https://github.com/xmrig/xmrig/issues/3010
author: qqiumax
assignees: []
labels: []
created_at: '2022-04-07T06:57:54+00:00'
updated_at: '2022-04-09T05:08:28+00:00'
type: issue
status: closed
closed_at: '2022-04-09T05:08:28+00:00'
---

# Original Description
![image](https://user-images.githubusercontent.com/102963434/162138628-d64c3b70-e852-4f56-887e-71df01ed1d5f.png)
I am at us-west-minexmr.com pool


# Discussion History
## Lonnegan | 2022-04-07T14:30:25+00:00
You have a very low hashrate and obviously the pool doesn't send jobs with a difficulty of less than 50,000. That still is way too much. Consider to mine something else which is better suited for your hardware or find a pool, where you manually can set the diff to around 5,000 or so.

## qqiumax | 2022-04-08T03:12:22+00:00
ok which pool do you recommend?

## Lonnegan | 2022-04-08T05:29:58+00:00
If you want to stay at Monero regardless of your low hashrate, I'd go to hashcity.org which starts at diff 1000 when you connect to port 3100, so you don't even need to use a fixed diff. Besides it is a PPS pool, so you get bucks for every result you return, regardless if the pool finds a block at that moment or not. So it's not so important that you return results regulary to get a part of the reward of the last block found (PROP pool) or to stay within the PPLNS window to get a fraction of the reward.

## qqiumax | 2022-04-08T07:50:01+00:00
But since i have to bypass china's firewall,i have to use ports 443,i cant connect to others
what shall i do?


## Lonnegan | 2022-04-08T08:03:12+00:00
You can try hashvault.pro. They for sure listen to port 443 (SSL) and as far as I can remember they adjust the diff automatically so that your miner can return a result every 30-60 seconds. I don't know if they do it so low that this is possible with just 200 H/s, but it's worth trying.
But: it's not a PPS pool. You only get paid if the pool finds a block. Keep that in mind when it'll take hours to see pending balance.

## qqiumax | 2022-04-09T05:08:28+00:00
ok thx

# Action History
- Created by: qqiumax | 2022-04-07T06:57:54+00:00
- Closed at: 2022-04-09T05:08:28+00:00
