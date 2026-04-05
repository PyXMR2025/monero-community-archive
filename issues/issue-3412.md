---
title: connect error
source_url: https://github.com/xmrig/xmrig/issues/3412
author: nameOnStone
assignees: []
labels: []
created_at: '2024-01-28T06:31:26+00:00'
updated_at: '2025-06-18T22:17:33+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:17:33+00:00'
---

# Original Description
```
D:\software\xmrig-6.21.0>xmrig.exe -o sg-zephyr.miningocean.org:5432 -u ZEPHsB2zVpb3gW6mjPSYGEfziQ3Rk4GBn14K1XZkBU9ibpHERPXvdWEQoqnP9Vedvo4gnPYSsg9iLJMJZEXzCKBnYTHtwz4utNj -p test -a rx/0 -k --donate-level 1 --tls
 * ABOUT        XMRig/6.21.0 gcc/11.2.0 (built for Windows x86-64, 64 bit)
 * LIBS         libuv/1.44.2 OpenSSL/1.1.1s hwloc/2.9.0
 * HUGE PAGES   unavailable
 * 1GB PAGES    unavailable
 * CPU          12th Gen Intel(R) Core(TM) i5-12450H (1) 64-bit AES VM
                L2:7.0 MB L3:12.0 MB 8C/12T NUMA:1
 * MEMORY       8.4/15.7 GB (53%)
                Controller0-ChannelA: 2 GB LPDDR5 @ 5200 MHz K3LKBKB@BM-MGCP
                Controller0-ChannelB: 2 GB LPDDR5 @ 5200 MHz K3LKBKB@BM-MGCP
                Controller0-ChannelC: 2 GB LPDDR5 @ 5200 MHz K3LKBKB@BM-MGCP
                Controller0-ChannelD: 2 GB LPDDR5 @ 5200 MHz K3LKBKB@BM-MGCP
                Controller1-ChannelA: 2 GB LPDDR5 @ 5200 MHz K3LKBKB@BM-MGCP
                Controller1-ChannelB: 2 GB LPDDR5 @ 5200 MHz K3LKBKB@BM-MGCP
                Controller1-ChannelC: 2 GB LPDDR5 @ 5200 MHz K3LKBKB@BM-MGCP
                Controller1-ChannelD: 2 GB LPDDR5 @ 5200 MHz K3LKBKB@BM-MGCP
 * MOTHERBOARD  TIMI - Redmi Book Pro 14 2022
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      sg-zephyr.miningocean.org:5432 algo rx/0
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2024-01-28 14:28:36.545]  net      sg-zephyr.miningocean.org:5432 51.79.157.201 connect error: "operation canceled"

```

I don't know why it does not work?


# Discussion History
## geekwilliams | 2024-01-28T07:38:53+00:00
Please remove --tls and try again

## nameOnStone | 2024-01-28T11:09:38+00:00
> Please remove --tls and try again

thanks, I tried, but It didn't work, still same problem

## geekwilliams | 2024-01-28T16:54:00+00:00
["Operation cancelled" indicates that xmrig was not able to connect to the pool within 20 seconds.](https://github.com/xmrig/xmrig/issues/1746#issuecomment-648739897)You may need to check your network connections, or try a different port on the pool. Alternatively, try mining to a different pool and see if you can access it. 

I read [here](https://www.reddit.com/r/MoneroMining/comments/lko4zj/connect_error_operation_canceled_help/) that this can be caused by your ISP blocking the domain, which you may be able to get past by using a vpn. 

Edit: When I first looked at this issue, there was a problem with the pool; the website wasn't loading, and when opening the mining address in a browser the connection dropped.  Now everything appears to be working normally.  If you can navigate to [https://sg-zephyr.miningocean.org:5432](https://sg-zephyr.miningocean.org:5432) in a browser on the same machine and the text "Mining server Online" appears, everything should work. 

## Uncle-Yuanl | 2024-04-03T11:07:32+00:00
use --proxy if you use vpn like clash

## Dijkstarlin | 2024-07-05T16:13:38+00:00
> use --proxy if you use vpn like clash

do you mean the system proxy?

## Uncle-Yuanl | 2024-07-10T07:05:52+00:00
> > use --proxy if you use vpn like clash
> 
> do you mean the system proxy?

First set system proxy then use --proxy in command line args.

# Action History
- Created by: nameOnStone | 2024-01-28T06:31:26+00:00
- Closed at: 2025-06-18T22:17:33+00:00
