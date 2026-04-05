---
title: Fail work two physical cpu.
source_url: https://github.com/xmrig/xmrig/issues/2266
author: Alienz69
assignees: []
labels: []
created_at: '2021-04-14T16:04:55+00:00'
updated_at: '2022-04-03T14:50:50+00:00'
type: issue
status: closed
closed_at: '2022-04-03T14:50:50+00:00'
---

# Original Description

[topology.txt](https://github.com/xmrig/xmrig/files/6312140/topology.txt)
**Describe the bug**
Xmrig 6.11.2 does not take advantage of the two physical cpu.

**To Reproduce**
With the Xmrig active it gives an approximate CPU calculation is 3200 h/s

**Expected behavior**
The approximate total of h/s with both CPUs should be 7000.

**Required data**
 - OS: Ubuntu Focal
 - CPU: 2x Intel Xeon E5-2650 V2.
 - RAm: 16 GB DDr3.
 - Motherboard: Asus Z9PR-D12

**Additional context**
I request support to correctly configure the config.json file so that the Xmrig software takes advantage of the two physical CPUs. Attached topology.xml and capture of the xmrig working.

[topology.txt](https://github.com/xmrig/xmrig/files/6312148/topology.txt)

![xmrig_6](https://user-images.githubusercontent.com/82528321/114742301-9b4a1980-9d19-11eb-870d-438b469c2cb9.png)





# Discussion History
## SChernykh | 2021-04-14T16:54:48+00:00
You are running 32 threads on a system where 16 threads is optimal, also huge pages and MSR mod don't work. Your config.json is just wrong. It's better to regenerate the config using https://xmrig.com/wizard and run xmrig as root.

## xmrig | 2021-04-14T17:06:10+00:00
In addition, `can't bind memory` means your second CPU likely doesn't have physical memory connected to this CPU all memory connected to the first CPU. Correct memory configuration is important for RandomX.
Thank you.

## Alienz69 | 2021-04-14T20:43:49+00:00
**Upgrade**

Changes made:
- I checked the motherboard manual and reconfigured the memory modules (4x4Gb DDR3). The result is that it does not indicate can't bind memory problems.

- I restored the config.json from the wizard.

-check the following post https://github.com/xmrig/xmrig/issues/2201
and increase the pages to 5210.

Results: the h/s of a cpu increased to 6463 h/s, but the xmrig has not yet been able to take advantage of the second physical CPU.


:(
I attach images the use CPU from ubuntu, the config.json file and lscpu.


![lscpu](https://user-images.githubusercontent.com/82528321/114776326-58e80300-9d40-11eb-9fad-ac499777b497.png)
![user_cpu](https://user-images.githubusercontent.com/82528321/114776338-5dacb700-9d40-11eb-9dc2-eb652b416958.png)
![xmring61](https://user-images.githubusercontent.com/82528321/114776351-62716b00-9d40-11eb-81c0-57917597153e.png)


## SChernykh | 2021-04-14T22:59:06+00:00
Both CPUs are working now. CPUs 16-31 are second virtual cores of 2 physical CPUs, they don't need to be used. You have good hashrate already: https://xmrig.com/benchmark?cpu=Intel%28R%29+Xeon%28R%29+CPU+E5-2650+v2+%40+2.60GHz
Now you only need to enable MSR mod (run xmrig as root or run https://github.com/xmrig/xmrig/blob/master/scripts/randomx_boost.sh as root before xmrig).

# Action History
- Created by: Alienz69 | 2021-04-14T16:04:55+00:00
- Closed at: 2022-04-03T14:50:50+00:00
