---
title: Very low hashrate on 96 core / 192 thread processor.
source_url: https://github.com/xmrig/xmrig/issues/3659
author: nmateo
assignees: []
labels: []
created_at: '2025-05-21T17:00:25+00:00'
updated_at: '2025-05-22T07:18:10+00:00'
type: issue
status: closed
closed_at: '2025-05-22T07:18:08+00:00'
---

# Original Description
**Describe the bug**
Very low hash count.
My processor (9K84) is not an standard Epyc processor, but it's basically the standard 9654, just with a bit higher tdp, but maybe that can affect the fact that xmrig is not working properly.

**To Reproduce**
9K84 processor, install debian 12, wget xmrig latest, sudo ./xmrig.

**Expected behavior**
I know I have only 2 ram slot populated and my motherboard should have 12, but even with only 2 i except more hashrate, on a slower zen1 i with 2 dimm also slower, I get more hash than 6000. And this machine is 96 core / 192 threads. 

**Required data**
 - XMRig version: 
  https://github.com/xmrig/xmrig/releases/download/v6.22.2/xmrig-6.22.2-linux-static-x64.tar.gz

 - Miner log as text or screenshot:
 
![Image](https://github.com/user-attachments/assets/84388db7-f90b-4116-95a9-60fc43feedd3)

 - Original config not modified.
 - OS: Fresh debian 12 install


**Additional context**



# Discussion History
## SChernykh | 2025-05-21T19:57:36+00:00
This CPU has 12 memory channels, and you need 12 memory sticks for the best performance. You have only two installed.

## nmateo | 2025-05-22T07:18:08+00:00
Okay thank you.

# Action History
- Created by: nmateo | 2025-05-21T17:00:25+00:00
- Closed at: 2025-05-22T07:18:08+00:00
