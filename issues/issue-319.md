---
title: xmrig and W10 multitasking
source_url: https://github.com/xmrig/xmrig/issues/319
author: cirlama
assignees: []
labels: []
created_at: '2018-01-05T12:44:40+00:00'
updated_at: '2018-11-05T07:08:21+00:00'
type: issue
status: closed
closed_at: '2018-11-05T07:08:21+00:00'
---

# Original Description
Hi,
I am mining ETH/PASC on Claymore's dual Ethereum miner V10.2 on 3 windows 10 PC (R9 380, RX-480 and RX-580) and in the same time I use the Intel I5 or I7 to mine XMR (monero or similar) with your xmrig and the CPU mining pays the electricity...
This morning, 2 out of my 3 PC did upgrade Windows 10 to the latest patch for spectre issue (I guess it is KB4056892), and my ETH/PASC combined mining went down to 0 on those 2 PCs.

Same behavior after PC restart, so I stopped XMR mining (XMRIG), and ETH/PASC combined mining went back to normal...

No more time to investigate (need to go to work).

Hope we will find a better solution and thanks for your work

(it's for info and u can close the issue if u want)

Edit: it's working when using one thread less than before (4 to 3 on i7 and 3 to 2 on i5, hashrate slightly reduced)

# Discussion History
# Action History
- Created by: cirlama | 2018-01-05T12:44:40+00:00
- Closed at: 2018-11-05T07:08:21+00:00
