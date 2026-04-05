---
title: XMRIG Connection Reset on Launch after "use argon2 implementation default"
source_url: https://github.com/xmrig/xmrig/issues/3344
author: Lukescott78
assignees: []
labels: []
created_at: '2023-10-17T05:54:09+00:00'
updated_at: '2025-06-18T22:19:41+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:19:41+00:00'
---

# Original Description
**Describe the bug**
When launching XMRIG script it starts up and just freezes on CPU "use argon2 implementation default". Console will stay like this for multiple hours and only stops by cancelling the operation. 

**To Reproduce**
Any time I launch the XMRIG 

**Expected behavior**
For XMRIG to run properly. 

**Required data**
![broken](https://github.com/xmrig/xmrig/assets/55175950/dfa440ae-1ce1-4150-abad-d0fe24652b04)



**Additional context**
Add any other context about the problem here.


# Discussion History
## SChernykh | 2023-10-17T07:02:07+00:00
I don't know how you managed to have Raspberry Pi Linux console and `C:\WINDOWS\system32>` on the same screenshot, but you should probably compile xmrig for RPi using advanced build instructions: https://xmrig.com/docs/miner/build/ubuntu

## SChernykh | 2023-10-17T07:04:10+00:00
`client_loop` message is not coming from XMRig, it doesn't have this message anywhere in its code. It's probably your ssh client's (?) disconnect message. Make sure RPi has good enough cooling and doesn't overheat.

# Action History
- Created by: Lukescott78 | 2023-10-17T05:54:09+00:00
- Closed at: 2025-06-18T22:19:41+00:00
