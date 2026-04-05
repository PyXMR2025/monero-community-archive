---
title: GR, 100% cpu usage sometimes
source_url: https://github.com/xmrig/xmrig/issues/2766
author: miningmeister
assignees: []
labels: []
created_at: '2021-12-01T10:17:11+00:00'
updated_at: '2021-12-01T12:41:10+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi
e2630 sometimes have 100% cpu load from all cores and crazy hashrate 1000-3000h, but cfg configured use 15 threads. I think normal hashrate for this cpu is 700-900.
 xmrig 6.16.1 ghostrider

<a href="https://fastpic.org/view/116/2021/1201/149309d8e15930f7cd4e53b0c61b99ce.jpg.html" target="_blank"><img src="https://i116.fastpic.org/thumb/2021/1201/ce/149309d8e15930f7cd4e53b0c61b99ce.jpeg" border="0"></a>
<a href="https://fastpic.org/view/116/2021/1201/3d1e4f2bae31c0c87e70b972af0e22c7.jpg.html" target="_blank"><img src="https://i116.fastpic.org/thumb/2021/1201/c7/3d1e4f2bae31c0c87e70b972af0e22c7.jpeg" border="0"></a>

# Discussion History
## miningmeister | 2021-12-01T10:38:41+00:00
upd
I think it happens then I run task manager and look cpu usage, then i close TM and after some time cpu load comeback to~80% and hashrate<900
<a href="https://fastpic.org/view/116/2021/1201/acf95fe5eb7109166319c39c9c6ad320.jpg.html" target="_blank"><img src="https://i116.fastpic.org/thumb/2021/1201/20/acf95fe5eb7109166319c39c9c6ad320.jpeg" border="0"></a>

## miningmeister | 2021-12-01T11:43:57+00:00
upd
walked away for a few minutes and hash rate increased without launch TM
<a href="https://fastpic.org/view/116/2021/1201/0818cf74f4c51bc0a6cf52388aed100c.jpg.html" target="_blank"><img src="https://i116.fastpic.org/thumb/2021/1201/0c/0818cf74f4c51bc0a6cf52388aed100c.jpeg" border="0"></a>

## miningmeister | 2021-12-01T12:41:10+00:00
On the cpuminer-gr github page written that  "the hash rate is very volatile and changes almost always with each block". Ok (500-3000 h/s), but what about 100% load and all cores?

# Action History
- Created by: miningmeister | 2021-12-01T10:17:11+00:00
