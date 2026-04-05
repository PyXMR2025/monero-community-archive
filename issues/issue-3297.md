---
title: Low hashrate on dual xeon 2686 v4
source_url: https://github.com/xmrig/xmrig/issues/3297
author: lacau
assignees: []
labels: []
created_at: '2023-07-12T15:54:23+00:00'
updated_at: '2023-07-12T19:19:02+00:00'
type: issue
status: closed
closed_at: '2023-07-12T19:17:41+00:00'
---

# Original Description
**Describe the bug**
OS: hiveos (5.15.0-hiveos #110)

Hello!
Since i have 2x xeon 2686v4 L2(18 x 256 KB) and L3(45Mb), i should be able to run 36 threads(cores) at max hashrate, witch by my tests is around 460H/s per core... However, when i use xmrig default config, 36 threads are started (thats right), but hash rate total is 8261 H/s witch is around 230 H/s per thread.
So my thought is that xmrig was recruiting 36 threads from one cpu only, witch would be 18 physical cores + 18 HT.
Then i use lscpu, and find out that its splitted like this:
NUMA node0 CPU(s): 0-17,36-53
NUMA node1 CPU(s): 18-35,54-71

**To Reproduce**
#### Test 01 - Default config:
![Screenshot from 2023-07-12 11-00-04](https://github.com/xmrig/xmrig/assets/12762984/100ad498-584a-4b03-b26f-2ba13fe229e0)
![Screenshot from 2023-07-12 11-15-32](https://github.com/xmrig/xmrig/assets/12762984/197f8c90-3516-4c30-af44-7f316965afd1)
![Screenshot from 2023-07-12 12-16-16](https://github.com/xmrig/xmrig/assets/12762984/7f41b6c0-852e-430e-a382-4629a2bfc65b)

#### Test 02 - Set affinity to use 18 cores from CPU 0:
"rx/xdag": [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17] - this gives me 4244 H/s witch is odd, since every core can do about 460 H/s, so expected hasrate is around 8000 H/s
![Screenshot from 2023-07-12 12-19-40](https://github.com/xmrig/xmrig/assets/12762984/c7ae7cdd-933f-4496-be16-642dc7bf6fa3)
![Screenshot from 2023-07-12 12-23-02](https://github.com/xmrig/xmrig/assets/12762984/e45715fd-9e84-409a-93b2-d836664866db)
![Screenshot from 2023-07-12 12-25-19](https://github.com/xmrig/xmrig/assets/12762984/abdea382-9af3-4d6f-8ba4-06391ccdec0a)

#### Test 03 - Set affinity to use 36 cores (theoretically 18 from each CPU, based on lscpu output)
"rx/xdag": [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35] - this gives me 8160 H/s witch is odd, since every core can do about 460 H/s, so expected hasrate is around 16000 H/s
![Screenshot from 2023-07-12 12-31-46](https://github.com/xmrig/xmrig/assets/12762984/9ed3b084-ce84-4b63-a69d-f739efd2f672)
![Screenshot from 2023-07-12 12-33-55](https://github.com/xmrig/xmrig/assets/12762984/871b011a-25e0-470c-bc0b-c4503e0b400c)
![Screenshot from 2023-07-12 12-34-31](https://github.com/xmrig/xmrig/assets/12762984/d3ca8009-324c-45dc-b3fe-7b1c27967cd5)

#### Test 04 - I did a lot of other tests playing with affinity, and this is the max hashrate that i archieved using 24 cores (theoretically 12 from each CPU)
"rx/xdag": [0,1,2,3,4,5,6,7,18,19,20,21,50,51,52,53,64,65,66,67,68,69,70,71] - this gives me 10420 H/s witch is acceptable, since every core is doing about 430 H/s
If i keep scaling cores using same strategy, hash rate starts to drop.
![Screenshot from 2023-07-12 12-44-07](https://github.com/xmrig/xmrig/assets/12762984/82a0fcac-e17e-4f10-83ab-7e52eaef2c24)
![Screenshot from 2023-07-12 12-45-14](https://github.com/xmrig/xmrig/assets/12762984/ed198482-7d57-4509-b107-ee43964acec4)
![Screenshot from 2023-07-12 12-49-44](https://github.com/xmrig/xmrig/assets/12762984/432e0a5a-1ead-484a-bd85-62ae00234eea)

Any directions to get close of what is expected (16000 H/s) ?


# Discussion History
## SChernykh | 2023-07-12T16:36:59+00:00
XMRig doesn't support rx/xdag. You should ask whoever made this modified version.
But from what I can see, you probably need more memory sticks to fill all memory channels. You're probably limited by RAM speed.

## lacau | 2023-07-12T19:17:41+00:00
> 



> XMRig doesn't support rx/xdag. You should ask whoever made this modified version.
> But from what I can see, you probably need more memory sticks to fill all memory channels. You're probably limited by RAM speed.

Okay, thank you for your answer. I will fill all memory channels and do more tests.

# Action History
- Created by: lacau | 2023-07-12T15:54:23+00:00
- Closed at: 2023-07-12T19:17:41+00:00
