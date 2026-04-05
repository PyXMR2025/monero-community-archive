---
title: Low hashrate on Epyc 7v12 on GhostRider
source_url: https://github.com/xmrig/xmrig/issues/3256
author: arpadboda
assignees: []
labels: []
created_at: '2023-04-19T11:56:23+00:00'
updated_at: '2025-06-18T22:47:36+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:47:36+00:00'
---

# Original Description
I have an Epyc 7v12 cpu with 256MB L3 cache and 64C.

The CPU boosts up to 3.2 GHz on all core, but the hashrate is only around 8.8 Kh/s. 
This is only 30% above the Epyc 7452, which is half of this processor (32C, 128MB L3, around the same clocks).

I would expect the hashrate to be around double of the hashrate of the 7452, so around 13Kh/s

Attached some screenshots. Is there any log or detail or data I can help you with?


<img width="1065" alt="Screenshot 2023-04-19 at 13 46 05" src="https://user-images.githubusercontent.com/43749426/233067378-f5f55e2f-cd9d-4bd2-b80a-c4e368f1b734.png">
<img width="1124" alt="Screenshot 2023-04-19 at 13 49 05" src="https://user-images.githubusercontent.com/43749426/233067402-6664fb25-1af2-4497-9756-d281d9cc6a4a.png">


# Discussion History
## SChernykh | 2023-04-19T12:03:44+00:00
GhostRider hashrate changes a lot between rounds, you need to compare the same rounds on both CPUs.

## arpadboda | 2023-04-19T12:05:22+00:00
@SChernykh : I did, what you see here is a 24h average. As you can see it's a pretty long run with 32500 accepted shares. 

## NVMDSTEVil | 2023-04-25T07:45:48+00:00
only single stick of ram is your problem likely.  Try with 4 or 8.

# Action History
- Created by: arpadboda | 2023-04-19T11:56:23+00:00
- Closed at: 2025-06-18T22:47:36+00:00
