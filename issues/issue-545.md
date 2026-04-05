---
title: Fluctuation in hashrate
source_url: https://github.com/xmrig/xmrig/issues/545
author: septuig
assignees: []
labels:
- NUMA
created_at: '2018-04-12T13:41:38+00:00'
updated_at: '2019-08-02T13:57:34+00:00'
type: issue
status: closed
closed_at: '2019-08-02T13:57:34+00:00'
---

# Original Description
CPU: Intel(R) Xeon(R) CPU E5-2680 v2 @ 2.80GHz (2) x64 AES-NI
CPU L2/L3: 10.0 MB/50.0 MB
I am mining Monero with CN7, but fluctuation in hashrate is large, from 500 to 1.3k at different time. How to config  "config.json" correctly?  Now all items are default , thank you.

"cpu-affinity": null,
"cpu-priority": null, 

# Discussion History
## lisergey | 2018-04-12T13:52:33+00:00
@septuig, your CPU has 10 cores, 20 threads each. 
try
"threads": 24,
if this would increase and stabilize hashrate, then I would count affinity mask for this threads number to make it even better.

## septuig | 2018-04-12T14:06:42+00:00
Ok, I will try, fyi, now default "threads" is 25. thank you.

## lisergey | 2018-04-12T14:17:53+00:00
25 threads is more then your CPUs are capable without overlapping in L3 cache.
each CPU should run 12 threads x 2MB L3 cache = 24 MB, to be the most effective.

## lisergey | 2018-04-12T14:31:18+00:00
I recommend to try
```
"av": 2,
"threads": 12,
"cpu-affiinity": "0xAAA00AAA00",
```
Also, this affinity might me slightly better or worse.
`"cpu-affiinity": "0x5550055500",`


## septuig | 2018-04-14T12:46:43+00:00
"av": 2,
"threads": 12,
"cpu-affiinity": "0xAAA00AAA00",
 
The above setting is workable, the hashrate is obviously improved and stable. 
 "cpu-affiinity": "0x5550055500" is worse than "0xAAA00AAA00" 
Thank you very much

Another question,  how to config the "config.json" to improve the mining of SUMO with CN H by the same CPU E5-2680v2 x2. Now the config is default as below, hashrate is about 400-500h:
"av": 1,
"threads": 12,
"cpu-affiinity": null,

Thank you in advance.


## lisergey | 2018-04-14T14:06:03+00:00
for Sumokoin, it takes 4MB of L3 cache per thread to maximize performance.
thus same affiinity with twice less threads:
```
"algo": "cryptonight-heavy",
"av": 1,
"threads": 12,
"cpu-affiinity": "0xAAA00AAA00",
```

I wonder what gives most rate for MoneroV7, 12 threads with av=2 or 24 threads with av=1?
for `"av": 1` affinity would be
`"cpu-affiinity": "0xFAAAAFAAAA",`

## septuig | 2018-04-15T01:42:26+00:00
Tested.

"av": 1,"threads": 24,"cpu-affiinity": "0xFAAAAFAAAA", is better than "av": 2,"threads": 12,"cpu-affiinity": "0xAAA00AAA00", for me.

Thank you so much

## chimchi | 2018-09-21T06:49:49+00:00
What is the meaning of "cpu-affiinity": "0xFAAAAFAAAA".

Thanks in advance.

## septuig | 2018-10-28T09:31:48+00:00
Afer upgraded to CN v8, the fluctuation in hashrate occurs again, the hash range is from 900+ to 1100+, can you please help fix this problem, thanks in advance. 

## xmrig | 2019-08-02T13:57:34+00:00
#1077 

# Action History
- Created by: septuig | 2018-04-12T13:41:38+00:00
- Closed at: 2019-08-02T13:57:34+00:00
