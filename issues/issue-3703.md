---
title: Benchmark rejected and is valid.
source_url: https://github.com/xmrig/xmrig/issues/3703
author: jekv2
assignees: []
labels: []
created_at: '2025-09-03T10:52:04+00:00'
updated_at: '2025-09-03T13:02:50+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I submitted a benchmark for a AMD 9950x and even though the first 3 I am in first place but my latest highest got rejected moments ago but still is valid and stable and is actually first first place.

https://xmrig.com/benchmark/ZJH88

https://xmrig.com/benchmark?cpu=AMD+Ryzen+9+9950X+16-Core+Processor

<img width="979" height="512" alt="Image" src="https://github.com/user-attachments/assets/20344894-f572-4d87-83b9-9cf5aade53a4" />
<img width="975" height="987" alt="Image" src="https://github.com/user-attachments/assets/ef1e1e74-d997-4c85-9d70-3be77c44261f" />

# Discussion History
## SChernykh | 2025-09-03T10:58:27+00:00
Did you verify it by running
```
xmrig --bench=10M --seed=5eebbbc70b9190fad012e9fe675feb51e00c944f268e21c802e9327a86f4bab5 --hash=2AC832F48DBF2254
```
On another PC?

## SChernykh | 2025-09-03T11:02:12+00:00
If you get `accepted` from a mining pool, it doesn't mean that it's fully stable. You can get 1 invalid hash out of 10 million, and it will result in a rejected benchmark, but you will still get all `accepted` from a pool (except for maybe 1 in 10 million).

## xmrig | 2025-09-03T13:02:50+00:00
Correct hash sum for this benchmark is `CD9DB3D2B50393AD`, not `2AC832F48DBF2254`, so it was rejected correctly.
Also, pools may not validate all shares; they might use some trust-based optimization to skip validation of some shares.
Thank you.

# Action History
- Created by: jekv2 | 2025-09-03T10:52:04+00:00
