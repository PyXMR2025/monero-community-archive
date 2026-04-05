---
title: hi, there have some bug
source_url: https://github.com/xmrig/xmrig/issues/31
author: local139
assignees: []
labels: []
created_at: '2017-07-08T03:06:14+00:00'
updated_at: '2023-05-19T21:24:16+00:00'
type: issue
status: closed
closed_at: '2017-07-11T16:09:53+00:00'
---

# Original Description
i turn it to 0.8, because i find some bug from 2.0
it (2.0) is show mining and show hash , but at pool site, hash is 0, and earn also is 0.
when i begin mining use 2.0, it is will be hash=0(POOL site) and always is 0 after 2-3 minutes
for example:
begin mining....
2.0 hash is 100h/s , pool hash 100h/s
after 2-3 minutes, 2.0 hash is 100h/s , pool hash 0h/s 
now, always 2.0 hash is 100h/s , pool hash 0h/s , also earn =0

but 0.8have no this problem or bug, 0.8 and 0.8.2 work fine.
i do not know why, hope this bug can be fix when you have free time. dude
 my english is not good, please don't mind


# Discussion History
## local139 | 2017-07-08T03:06:47+00:00
ubuntu16.10  use VPS server
pool :  monero.crypto-pool.fr   and minexmr.com
0.8.2 is ok, 2.0 not work

## xmrig | 2017-07-08T05:13:38+00:00
In version 2 hashrate reports just for information, by default every 60 seconds. If share accepted you should see green message with that, like `accepted (1/0) diff 10000 (138 ms)` only after that pool show you hashrate (very estimated).

What diff you use? You should use minimum possibility diff (12000 or 10000 on these pools) but also 10000 to high for 100 H/s, so it can take minutes to see accepted message, depends on luck.
Thank you.

## local139 | 2017-07-08T06:28:02+00:00
yes, but pool site show 0, earn is not add (earn 0).
0.8.2 no problem, i do not know why 2.0 not work.
my 2.0 use gcc 5.4 (ubuntu default 5.4)


## xmrig | 2017-07-08T06:40:50+00:00
1. You see accepted messages?
2. What exactly command line you use (except wallet address).

## local139 | 2017-07-08T10:53:14+00:00
yes, accept, but all those 2 pool (monero.crypto-pool.fr and minexmr.com),  hash =0
./xmrig -o pool address -u wallet --av=2
very simple and work with old version,  2.0 not work except first 2-3 minutes.

## local139 | 2017-07-08T10:55:17+00:00
and i am use this config ,if anything wrong  , please tell me ：
cmake .. -DCMAKE_BUILD_TYPE=Release -DUV_LIBRARY=/usr/lib/x86_64-linux-gnu/libuv.a
make

## local139 | 2017-07-08T10:58:06+00:00
when i use -DUV_LIBRARY=/usr/lib/x86_64-linux-gnu/libuv.a  , after type " make" there have many whilte letters, i am do not know what's that. but when i use old version it is no this problem.

## xmrig | 2017-07-08T12:12:04+00:00
I run
`./xmrig -o pool.minexmr.com:4444 -u 48edfHu7V9Z84YzzMa6fUueoELZ9ZRXq9VetWzYGzKt52XU5xvqgzYnDK9URnRoJMk1j8nLwEVsaSWJ4fhdUyZijBGUicoD --av 2`

`Last Share Submitted` updated imitatively.
`Hash Rate` and `Total Hashes Submitted` after some time.

If you see accepted message this mean only one thing, pool successfully accept your share.
Stats on pool side can be delayed, because of heavy load (over 20 MH/s each pool).

## local139 | 2017-07-08T12:20:07+00:00
thanks

## howtopay | 2023-05-19T21:24:15+00:00
when your looking online for error message's because your too lazy to make a issue

# Action History
- Created by: local139 | 2017-07-08T03:06:14+00:00
- Closed at: 2017-07-11T16:09:53+00:00
