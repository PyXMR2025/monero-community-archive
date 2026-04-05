---
title: 3970x hashrate only 14kh/s
source_url: https://github.com/xmrig/xmrig/issues/2399
author: Lianghao93
assignees: []
labels: []
created_at: '2021-05-21T02:56:47+00:00'
updated_at: '2021-05-31T07:41:12+00:00'
type: issue
status: closed
closed_at: '2021-05-31T07:41:12+00:00'
---

# Original Description
I use two CPU (3950x and 3970x) to mine XMR
hashrate of 3950x is stable, always around 14kh/s
but two days ago hashrate of 3970x drop from 26kh/s to 14kh/s
I didn't change any setting

![49 235 112 100_7002 - 远程桌面连接 2021_5_21 10_50_54 (2)](https://user-images.githubusercontent.com/32161863/119075322-2c9c6200-ba23-11eb-9171-50caed325d3a.png)

# Discussion History
## SChernykh | 2021-05-21T06:28:58+00:00
@LianghaoLi-Hust Your RAM is installed in wrong slots, you're not running in 4-channel mode. Check your motherboard manual and install in correct slots.

## Lianghao93 | 2021-05-31T06:16:01+00:00
> @LianghaoLi-Hust Your RAM is installed in wrong slots, you're not running in 4-channel mode. Check your motherboard manual and install in correct slots.

Thanks

## Spudz76 | 2021-05-31T06:55:19+00:00
Make sure Memory Compression task and Memory Disagnostics task are all disabled, or it will run randomly sometimes and fight the hashrate (due to clogging memory bus).

Along with other wasteful background junk.

# Action History
- Created by: Lianghao93 | 2021-05-21T02:56:47+00:00
- Closed at: 2021-05-31T07:41:12+00:00
