---
title: hashrate different to xmr-stak
source_url: https://github.com/xmrig/xmrig/issues/495
author: lowprofileusername
assignees: []
labels: []
created_at: '2018-04-04T04:10:17+00:00'
updated_at: '2018-11-05T13:18:40+00:00'
type: issue
status: closed
closed_at: '2018-11-05T13:18:40+00:00'
---

# Original Description
Same machine. using xmrig I get around 300 hashrate, but using xmr-stak double the hashrate which around 600. 

default xmrig using 10 threads xmr-stak using 20 threads. but if I change thread to 20 with xmrig. xmrig hashrate will result lower.

 * VERSIONS:     XMRig/2.6.0-beta1 libuv/1.19.2 MSVC/2017
 * HUGE PAGES:   available, enabled
 * CPU:          Intel(R) Xeon(R) CPU E7-4809 v3 @ 2.00GHz (1) x64 AES-NI
 * CPU L2/L3:    2.0 MB/20.0 MB

what else should I post here?

Thanks.

# Discussion History
## Meyer01 | 2018-04-04T10:56:34+00:00
In which timeframe did you make measuremens? I think you need to mine using xmrig for 1-2 hours and then mine by xmr-stak for 1-2 hours. And then compare the average hashrate.

## lowprofileusername | 2018-04-04T13:12:25+00:00
tried mine using xmrig for 1 hr. same result.

Thanks for the product anyway

## ghost | 2018-04-04T13:37:15+00:00
For just one E7 4809 V3 (8c16t 2Ghz) with 20M L3 cache, 300H/s is the correct result. Did you get 2 of E7 4809 V3 in use? Perhaps the xmrig did not recognize your second CPU I think.

## lowprofileusername | 2018-04-04T14:05:50+00:00
yes. you are right. cpu-z detect 2 sockets installed

Windows Taskmgr shows mine L3 cache 40.0 MB instead of 20.0MB

## farmer-1 | 2018-04-04T16:46:35+00:00
use:
start /node 0 xmrig.exe blablablabla 
and after this another:
start /node 1 xmrig.exe blablablabla 

The second start session should bind at the second processor, can you confirm this?

# Action History
- Created by: lowprofileusername | 2018-04-04T04:10:17+00:00
- Closed at: 2018-11-05T13:18:40+00:00
