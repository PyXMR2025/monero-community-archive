---
title: failure to get the difficulty (as a number) from the pool
source_url: https://github.com/xmrig/xmrig/issues/2737
author: sfhdfshdfh
assignees: []
labels:
- bug
created_at: '2021-11-28T09:37:05+00:00'
updated_at: '2021-11-28T13:31:54+00:00'
type: issue
status: closed
closed_at: '2021-11-28T13:31:54+00:00'
---

# Original Description
**Describe the bug**
when choosing high difficulty port from the pool i get this error. 
raptoreumemporium.com:3256 **invalid mining.set_difficulty notification: difficulty is not a number**
ports for Small miners | 3008 work fine.
also when i don't specify the algo gr, xmrig doesn't recognize the job as ghostrider(doesn't even connect to the pool), and it doesn't switch to my second pool, it just keeps waiting doing nothing. 
![xmrig error](https://user-images.githubusercontent.com/17777550/143757643-7d9c5d7a-7c4a-4690-8f4d-97bc85d7736f.png)

**To Reproduce**
gcc and msvc windows 8.1 x64
xmrig.exe -o raptoreumemporium.com:3256 -u WALLET_ADDRESS -a gr -p x
also port 3032 gets this difficulty not a number error. 

**Expected behavior**
1- xmrig should get the difficulty as a decimal number and if it fails to do so automatically switch to alternative mining pool set by user. 
2- also xmrig should detect the algo automatically. 
3- i suggest you add support to multiport format like this POOL:PORT1.PORT2.PORT3 -u WALLET (comma or dot separated ports)
xmrig.exe -o raptoreumemporium.com:3256.3008 -u wallet
4- also while xmrig it is running from commandline, (only if commandline hasn't specified any threads and affinity settings) let xmrig read affinity & thread count settings from json file next to it(if the json exists) and ignore other stuff from json. 

# Discussion History
## SChernykh | 2021-11-28T11:13:52+00:00
Fixed it in #2738. Next release will have this fix.

# Action History
- Created by: sfhdfshdfh | 2021-11-28T09:37:05+00:00
- Closed at: 2021-11-28T13:31:54+00:00
