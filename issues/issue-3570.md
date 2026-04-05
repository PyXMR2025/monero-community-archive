---
title: 'xmrig algo ghostrider : compiled version 6.22.1 failed to start threads error'
source_url: https://github.com/xmrig/xmrig/issues/3570
author: KHPak2023
assignees: []
labels: []
created_at: '2024-10-23T10:25:05+00:00'
updated_at: '2025-06-18T22:04:19+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:04:19+00:00'
---

# Original Description
I am using compiled xmrig version 6.22.1 on algo ghostrider getting error

self test failed. failed to start threads error
![image](https://github.com/user-attachments/assets/42cb2991-f1eb-4ec5-aaee-437951a7060a)

However, on pre-compiled downloaded xmrig copy it runs but resulting 
Rejected low difficulty shares

![image](https://github.com/user-attachments/assets/d2106c0d-0fe8-49a2-973f-2ac2f0a0de42)


Any advise please




# Discussion History
## SChernykh | 2024-10-23T11:24:27+00:00
Did it work with 6.22.0? If so, you can revert to it for now, while it's being fixed.

## SChernykh | 2024-10-23T11:31:51+00:00
Can you also check a different pool?
```
xmrig.exe -o eu.flockpool.com:4444 -u YOUR_RAPTOREUM_WALLET -a ghostrider
```

I can't reproduce it with `xmrig-6.22.1-gcc-win64.zip` and `xmrig-6.22.1-msvc-win64.zip`

## KHPak2023 | 2024-10-24T05:24:52+00:00
> Did it work with 6.22.0? If so, you can revert to it for now, while it's being fixed.

![image](https://github.com/user-attachments/assets/be5135f7-2f5e-4b86-86d9-c7de30f837d9)

Benchmark test with algo ghostrider also failed on 6.22 and 6.22.1.

![image](https://github.com/user-attachments/assets/fb5e3bdb-78b0-4900-b4ee-b9f246a1de74)

Bencgmark test successful on 6.20

## KHPak2023 | 2024-10-24T05:30:45+00:00
> Can you also check a different pool?
> 
> ```
> xmrig.exe -o eu.flockpool.com:4444 -u YOUR_RAPTOREUM_WALLET -a ghostrider
> ```
> 
> I can't reproduce it with `xmrig-6.22.1-gcc-win64.zip` and `xmrig-6.22.1-msvc-win64.zip`

same error on flockpool.com

![image](https://github.com/user-attachments/assets/45df06eb-f619-4443-88f1-cd3846f8d20f)

I think, xmrig is allergic to ghostrider


## SChernykh | 2024-10-24T06:21:05+00:00
Can you try msvc-compiled version, not gcc? `xmrig-6.22.1-msvc-win64.zip`

## KHPak2023 | 2024-10-24T06:45:43+00:00
> Can you try msvc-compiled version, not gcc? `xmrig-6.22.1-msvc-win64.zip`

Yes it worked with 6.22.1 msvc version
![image](https://github.com/user-attachments/assets/232db578-e8b2-4fac-9d21-03cdcf818808)

Thanks a lot for your time and help


# Action History
- Created by: KHPak2023 | 2024-10-23T10:25:05+00:00
- Closed at: 2025-06-18T22:04:19+00:00
