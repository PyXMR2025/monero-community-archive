---
title: credits
source_url: https://github.com/xmrig/xmrig/issues/211
author: xxlxxlxxl
assignees: []
labels: []
created_at: '2017-11-20T22:19:22+00:00'
updated_at: '2017-11-27T00:08:09+00:00'
type: issue
status: closed
closed_at: '2017-11-27T00:08:09+00:00'
---

# Original Description
{
"algo": "cryptonight",
"av": 0,
"background": false,
"colors": true,
"cpu-affinity": null,
"cpu-priority": null,
"donate-level": 5,
"log-file": null,
"max-cpu-usage": 1000000,
"print-time": 60,
"retries": 5,
"retry-pause": 5,
"safe": false,
"syslog": false,
"threads": null,
"pools": [
{
"url": "pool.minemonero.pro:5555",
"user": "wallet adress*",
"pass": "x",
"keepalive": true,
"nicehash": false
}
]
}

i make config like this is it ok?

and after how much hours payment are credited in my wallet?

# Discussion History
## xmrig | 2017-11-21T10:54:56+00:00
Check answers in #160 issue.
Thank you.

## xxlxxlxxl | 2017-11-21T10:57:17+00:00
I want to know if the i put the wallet correctly?

## xmrig | 2017-11-21T11:00:17+00:00
`"user": "wallet adress*",`
Yep.

## xxlxxlxxl | 2017-11-21T11:02:03+00:00
Also please last question, how do i check my total mining balance and limit of mining to withdraw?

## xmrig | 2017-11-21T11:09:23+00:00
So If you use pool.minemonero.pro open https://monero.hashvault.pro/en/#!/dashboard and enter your wallet address in `Track Live Stats` block. Withdraw limit is 0.3 XMR.

## xxlxxlxxl | 2017-11-21T16:20:26+00:00
Total Due
0.0057123778 XMR

this is total mining till now
correct?

## xmrig | 2017-11-21T16:48:50+00:00
Yep

## xxlxxlxxl | 2017-11-21T23:37:24+00:00
@xmrig , please i want to know
maxcpu usage = 75
is this maximum usage of cpu
or 50% usage?

## xmrig | 2017-11-27T00:07:06+00:00
Your CPU usage limited by L3 cache.

# Action History
- Created by: xxlxxlxxl | 2017-11-20T22:19:22+00:00
- Closed at: 2017-11-27T00:08:09+00:00
