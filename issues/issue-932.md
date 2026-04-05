---
title: 'version 2.12.0: cn-pico hashrate drop'
source_url: https://github.com/xmrig/xmrig/issues/932
author: yyfong0918
assignees: []
labels:
- bug
created_at: '2019-02-14T04:54:16+00:00'
updated_at: '2019-02-22T10:25:15+00:00'
type: issue
status: closed
closed_at: '2019-02-22T10:25:15+00:00'
---

# Original Description
2.11.0 (cn-pico): >6K
[2019-02-14 12:47:25] speed 10s/60s/15m 6016.7 6017.1 n/a H/s max 6020.0 H/s

2.12.0 (cn-pico): <4K
[2019-02-14 12:48:57] speed 10s/60s/15m 3885.9 n/a n/a H/s max 3887.6 H/s

# Discussion History
## asylum119 | 2019-02-14T15:41:08+00:00
Just upgraded and can confirm approx 50% drop in hash rate on Ryzen threadripper using cryptonight-turtle with all settings the same prior to upgrading.

Changing --algo to cn-pico/trtl gave the expected hash rate if loading directly via command but dropped again if using --background.

Using --asm Ryzen fixed the hash rate when using --background and --algo cn-pico/trtl so I'm happy there. Just a bit confused.

What I found strange was originally I was unable to use --algo cn-pico/trtl to get the expected hash rate when the algo went live, things swapped around now for some reason. 

Are CPU algos now being cached ? reason for asking is I had a similar issue with xmrig-amd when GPU caching was first implemented so needed to use --no-caching for a few releases. Otherwise swapping algo alieses to rectify hash rate drops doesn't make much sense to me at all.



## uejji | 2019-02-14T16:22:33+00:00
Not as drastic, but I've noticed about 20% hashrate decrease on cn-pico/trtl on Westmere (built from source on Ubuntu).

## xmrig | 2019-02-19T04:28:14+00:00
Fixed in dev branch. ASM code was not used for this algorithm due copy-paste error.
Thank you.

## xmrig | 2019-02-22T10:25:15+00:00
v2.13.0 released.

# Action History
- Created by: yyfong0918 | 2019-02-14T04:54:16+00:00
- Closed at: 2019-02-22T10:25:15+00:00
