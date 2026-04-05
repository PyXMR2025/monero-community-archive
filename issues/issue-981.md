---
title: Double algorithm variations has no effect on Cryptonight/R
source_url: https://github.com/xmrig/xmrig/issues/981
author: Ronnier33
assignees: []
labels: []
created_at: '2019-03-11T00:21:33+00:00'
updated_at: '2019-08-02T11:58:55+00:00'
type: issue
status: closed
closed_at: '2019-08-02T11:58:55+00:00'
---

# Original Description
when use av=2 option, the hashrate is no difference than av=1. though it worked fine on v8. has this feature be nuked by the new algorithm?

# Discussion History
## slavab73 | 2019-03-12T10:32:03+00:00
...and triplehash drop down to 15 h/s (from 80 h/s - 1 thread, av=0, core i5, 6mb cache). someone knows the reason?

## slavab73 | 2019-03-12T11:27:18+00:00
xmrstack fixed this bug in 2.10.1 release 13 hours ago. 
https://github.com/fireice-uk/xmr-stak/pull/2309

## xmrig | 2019-03-12T11:53:10+00:00
Double hash now much slower that before, thanks to `cn/r`, it new sad reality, in additional triple and more hash mode lacks ASM acceleration.

@slavab73 xmr-stak bug was never exists in xmrig.
Thank you.

## slavab73 | 2019-03-12T12:04:30+00:00
@xmrig 
xmrstack 
- get 124h/s in low_power_mode=true (1 thread)
- get   75h/s in low_power_mode=false (1 thread)
so...

## xmrig | 2019-03-12T12:20:21+00:00
Okay my quick test, low_power_mode=false, 1 thread, i7-7700, Ubuntu 18.04:
xmr-stak 2.10.0 = ~78 h/s
xmr-stak 2.10.1 = **~97 h/s**
xmrig 2.14.1 = **~97 h/s**
xmrig 2.13.0 = **~97 h/s**

So? nothing to fix.

## slavab73 | 2019-03-12T12:24:55+00:00
@xmrig very sorry! my mistake!! wrong config for xmrstack! :(
best regards...

# Action History
- Created by: Ronnier33 | 2019-03-11T00:21:33+00:00
- Closed at: 2019-08-02T11:58:55+00:00
