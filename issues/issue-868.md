---
title: E5 2680V2 mining error
source_url: https://github.com/xmrig/xmrig/issues/868
author: netmebtc
assignees: []
labels:
- question
created_at: '2018-11-04T02:35:40+00:00'
updated_at: '2019-08-02T12:05:52+00:00'
type: issue
status: closed
closed_at: '2019-08-02T12:05:52+00:00'
---

# Original Description
E52680V2 win7 xmrig 2.8.3
xmrig-proxy 2.8.1
Mining algo cn_v8

 when mining , often error, then  stop xmrig , start xmrig again, still cannot mining.  only restart the E52680V2 ,then it is working, what is the problem ?

![image](https://user-images.githubusercontent.com/32667839/47959363-ffcaff80-e01c-11e8-960c-0e86452c7a2c.png)


# Discussion History
## snipeTR | 2018-11-04T19:33:02+00:00
192.168.0.252 proxy?
İnfo the proxy

## xmrig | 2018-11-05T06:49:42+00:00
Network issue, but no other issues, connection recovered, mining too.
Thank you.

## netmebtc | 2018-11-05T07:14:39+00:00
> Network issue, but no other issues, connection recovered, mining too.
> Thank you.

No,no.
When connection recovered , the rig cannot mining, restart xmrig, cannot mining,  only restart rig power,then can mining

![image](https://user-images.githubusercontent.com/32667839/47986021-65e77d80-e116-11e8-9b56-f89bae7bd7c5.png)

![image](https://user-images.githubusercontent.com/32667839/47986072-94fdef00-e116-11e8-871c-556475974779.png)


## netmebtc | 2018-11-05T08:20:12+00:00



> 192.168.0.252 proxy?
> İnfo the proxy

It  is xmrig-proxy 2.8.1

## netmebtc | 2018-11-06T03:18:51+00:00
Hi, this is not a question,It is realy a issue

## xmrig | 2018-11-06T05:51:51+00:00
Missed your second screenshot, looks really strange, please provide all possible details, especially about network.

It's plain wired local network or something more complicated eg VPN. Also I confusing with 3 different IP address on your screenshot `192.168.0.252`, `192.168.1.250`, `192.168.88.250`.

Is there any firewall (local or network) or AV blocking traffic?

## netmebtc | 2018-11-06T06:05:51+00:00
This problem occurs in three farms, all of which are the same issue. After the problem occurs, CPU rigs must restart the power supply before they can continue to mine.   There is no firewall.
If rigs connect to the pool directly, the problem  also happen.

## xmrig | 2018-11-06T06:20:15+00:00
Okay let's start investigate it from direct connection to pool.
You from China (I guess it from your screenshots)?, so your pool located in Singapore (if it one of major pools) in this case there is already big firewall on the way.

Try use SSL/TLS to hide your traffic:
1. `"tls": true` in config.
2. SSL port on your pool.

One thing strange, if it miner issue, just simple miner restart should help.

# Action History
- Created by: netmebtc | 2018-11-04T02:35:40+00:00
- Closed at: 2019-08-02T12:05:52+00:00
