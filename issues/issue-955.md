---
title: How to config(2.13)
source_url: https://github.com/xmrig/xmrig/issues/955
author: smzwsz
assignees: []
labels:
- question
created_at: '2019-02-27T12:40:07+00:00'
updated_at: '2019-03-07T05:27:27+00:00'
type: issue
status: closed
closed_at: '2019-03-07T05:27:27+00:00'
---

# Original Description
Just set as:
"algo": "cn/r"
"variant": -1

same as xmrig-proxy?

# Discussion History
## xmrig | 2019-03-02T06:26:26+00:00
* `"algo": "cn"`, but miner/proxy also understand `"cn/r"`.
* `"variant"` `-1` for auto detect or `"r"`.

If connect miner to the proxy, variant option in miner config doesn't matter.
Thank you.

## smzwsz | 2019-03-02T10:04:01+00:00
Thank u.
BY the way?  I used proxy,miner config must use:
"nicehash": false,
"keepalive": false,
I find "true" may take  a mistake

## xmrig | 2019-03-02T11:03:27+00:00
`"true"` it's string value and it not valid for these options, it expected Boolean value, just `true`.

## smzwsz | 2019-03-02T12:53:15+00:00
like as this :"nicehash": true,？
It seems not very useful

## xmrig | 2019-03-02T16:06:50+00:00
Okay, then:

1. Show full miner output including configs
2. Show config file, wallets can be omitted.

## smzwsz | 2019-03-07T05:27:18+00:00
Sorry。
I have got it wrong,and solved it.

# Action History
- Created by: smzwsz | 2019-02-27T12:40:07+00:00
- Closed at: 2019-03-07T05:27:27+00:00
