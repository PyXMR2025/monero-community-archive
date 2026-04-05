---
title: can't utilize the all cores on Intel(R) Xeon(R) 6986P-C
source_url: https://github.com/xmrig/xmrig/issues/3670
author: tingyuloulala
assignees: []
labels:
- bug
- randomx
created_at: '2025-06-17T07:44:32+00:00'
updated_at: '2025-06-28T10:23:29+00:00'
type: issue
status: closed
closed_at: '2025-06-28T10:23:29+00:00'
---

# Original Description
**Describe the bug**
here i have a vps with a cpu of Intel(R) Xeon(R) 6986P-C. lscpu shows that it has 240 cores.  but only 120 cores working when mining and with the hashrate 60k. When I manually set the thread count to 240, CPU utilization reached 100%, but the hashrate dropped to 33k.

![Image](https://github.com/user-attachments/assets/b7a2bcb5-2d22-4ae4-9ece-f59a9b6b926d)

![Image](https://github.com/user-attachments/assets/75e2d128-ae4c-4b90-8240-d2cd586e1c18)

![Image](https://github.com/user-attachments/assets/521fa991-8bf8-413b-8615-5d4c4216a20e)

<img width="974" alt="Image" src="https://github.com/user-attachments/assets/b16567bf-1100-481d-98e0-8abf4a84d74d" />

# Discussion History
## SChernykh | 2025-06-17T08:29:19+00:00
That is a very weird virtualized system. 3 NUMA nodes, but 1 CPU? XMRig assigns threads based on L2 and L3 cache availability for each core, so if it didn't create more threads automatically, and you can't reach better hashrate with more threads, then there is a good reason to use only 120 threads.

Can you run `./xmrig --export-topology` and attach the generated XML file here?

## SChernykh | 2025-06-17T08:38:57+00:00
It's probably this CPU: https://www.techpowerup.com/cpu-specs/xeon-6980p.c3862

128 physical cores, each core has 2 MB L2 cache (perfect for RandomX). When you use more than 120 threads, it starts to use slower L3 cache instead of L2, this is why you get lower hashrate.

3 NUMA nodes are probably used because it has 12 memory channels (4 channels per NUMA node for faster access to the corresponding physical RAM sticks).

If you ran XMRig on the physical CPU, you would get best hashrate with 128 threads, but since you only have access to 120 physical cores, you get best results with 120 threads.

## tingyuloulala | 2025-06-17T08:42:00+00:00
[topology.txt](https://github.com/user-attachments/files/20771551/topology.txt)

## xmrig | 2025-06-17T09:56:55+00:00
Automatic configuration may not work well in a virtual environment, as the real physical topology is hidden, and other virtual machines may consume the L3 cache. Thanks for the topology. I could reproduce the creation of 120 threads. ~~According to the topology, the L3 cache is inclusive, and its size doesn't meet the requirements of L2 (256KB) and L3 (2MB). We can't sum these sizes on this CPU.~~

You can't use the `--threads` option if you have more than one NUMA node, as it prevents threads from binding to the correct node. The correct way to try to use all 240 threads is to replace `"rx"` profile in `"cpu"` section to:
```
"rx": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239],
```

## tingyuloulala | 2025-06-17T10:39:07+00:00
> Automatic configuration may not work well in a virtual environment, as the real physical topology is hidden, and other virtual machines may consume the L3 cache. Thanks for the topology. I could reproduce the creation of 120 threads. According to the topology, the L3 cache is inclusive, and its size doesn't meet the requirements of L2 (256KB) and L3 (2MB). We can't sum these sizes on this CPU.
> 
> You can't use the `--threads` option if you have more than one NUMA node, as it prevents threads from binding to the correct node. The correct way to try to use all 240 threads is to replace `"rx"` profile in `"cpu"` section to:
> 
> ```
> "rx": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239],
> ```

thanks for your reply.  I modified the config.json file according to your instructions, and after running xmrig, I found that what you said was completely correct. All cores are working, and the hashrate has increased to 84k. I want to ask another question: is there a way to achieve this without using the json file?

![Image](https://github.com/user-attachments/assets/06877a53-f4af-475c-8728-389a1538b97d)

## xmrig | 2025-06-17T11:08:24+00:00
I mark this issue as a bug. The auto-config needs to be tuned for cases where nearly all required cache is available.
Thank you,

# Action History
- Created by: tingyuloulala | 2025-06-17T07:44:32+00:00
- Closed at: 2025-06-28T10:23:29+00:00
