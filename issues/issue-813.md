---
title: Critical bug with Minergate pool and variant 2
source_url: https://github.com/xmrig/xmrig/issues/813
author: d3c0d3d
assignees: []
labels:
- bug
created_at: '2018-10-18T15:41:00+00:00'
updated_at: '2018-10-19T04:04:22+00:00'
type: issue
status: closed
closed_at: '2018-10-19T04:04:22+00:00'
---

# Original Description
![image](https://user-images.githubusercontent.com/29043805/47166454-9d5ec900-d2d2-11e8-8735-450979dcf8ff.png)

The miner is not respecting variant 2 causing rejection!

# Discussion History
## snipeTR | 2018-10-18T17:06:16+00:00
Algo cn/2 try please

## dimkers | 2018-10-18T17:15:02+00:00
./xmrig -a cryptonight-lite
or
./xmrig -a cryptonight-heavy

```
unable to open /home/dimkers/xmrig/build/config.json: no such file or directory
No valid configuration found. Exiting.
```

if ./xmrig -a cn/2
http://dl3.joxi.net/drive/2018/10/18/0025/3522/1678786/86/6c3fd65d9d.jpg



## berezinevgeniy | 2018-10-18T17:32:12+00:00
> if ./xmrig -a cn/2

not working -( still cn/1

## dimkers | 2018-10-18T17:34:12+00:00
> not working -( still cn/1

Do you mean on pool?

## berezinevgeniy | 2018-10-18T17:37:58+00:00
new job from xmr.pool.minergate.com:45700 diff 1063 algo cn/1
try algo "cn/2", try "variant":2 but all new job has algo cn/1.
on original minergate gui software all working fine. 

## berezinevgeniy | 2018-10-18T18:06:49+00:00
any suggestions?

## dimkers | 2018-10-18T18:12:50+00:00
I haven't.

## berezinevgeniy | 2018-10-18T18:40:35+00:00
* POOL #1      stratum+tcp://xmr.pool.minergate.com:45700 variant 1
why variant 1 has been choosen. variant:2 set at config. 

## dimkers | 2018-10-18T18:42:50+00:00
can you try on other pool(not minergate)?

## berezinevgeniy | 2018-10-18T18:52:38+00:00
* POOL #1      spool.minexmr.com:4444 variant 2
f..ck. Whats wrong with minergate ? -(

## berezinevgeniy | 2018-10-18T18:53:16+00:00
problem with detection of connection`s variant maybe?

## d3c0d3d | 2018-10-18T19:33:02+00:00
https://github.com/xmrig/xmrig/blob/master/src/common/net/Pool.cpp#L352

The bug is in this line, just change to Variant_2 and recompile the code!

## dimkers | 2018-10-18T20:43:25+00:00
YES!
change in code 
`m_algorithm.setVariant(m_port == 45700 ? VARIANT_1 : VARIANT_0);`
to
`m_algorithm.setVariant(m_port == 45700 ? VARIANT_2 : VARIANT_0);`
recompil and miner work!
http://joxi.ru/Y2LMN8YT9D6B9A

Thanks!

## damcko8888 | 2018-10-19T01:49:17+00:00
You can try with IP address instead domain name (xmr.pool.minergate.com).

https://minergate.com/blog/critical-bug-found-in-the-xmrig-miner/


## xmrig | 2018-10-19T02:23:13+00:00
I will make new releases as soon as possible, right now I can't, unexpected power outage in my location. As temporary solution use IP address instead of domain name as mentioned above.
Thank you.

## xmrig | 2018-10-19T02:44:54+00:00
@0xc0d32 I merge your PRs, as quick emergency fix it ok.
Thank you.

## xmrig | 2018-10-19T02:51:11+00:00
Good news electricity is come back.

## xmrig | 2018-10-19T03:59:24+00:00
Done
https://github.com/xmrig/xmrig/releases/tag/v2.8.3
https://github.com/xmrig/xmrig-amd/releases/tag/v2.8.3
https://github.com/xmrig/xmrig-nvidia/releases/tag/v2.8.3

## d3c0d3d | 2018-10-19T04:04:22+00:00
Thank you! Thanks for the speed hehehe, I'll close this issue!

# Action History
- Created by: d3c0d3d | 2018-10-18T15:41:00+00:00
- Closed at: 2018-10-19T04:04:22+00:00
