---
title: 'xmrig not mining on ghostrider algo error threads self test failed : Ubuntu
  24.04 version'
source_url: https://github.com/xmrig/xmrig/issues/3617
author: KHPak2023
assignees: []
labels:
- bug
created_at: '2025-01-14T11:35:34+00:00'
updated_at: '2025-06-28T10:28:20+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I am running my own pool; ghostrider is also workable on this pool. Tried to mine RHEX coin, tested all ubuntu related versions with same error. 
xmrig-6.22.2-jammy-x64.tar.gz 
xmrig-6.22.2-noble-x64.tar.gz 
xmrig-6.22.2-linux-static-x64.tar.gz 
![image](https://github.com/user-attachments/assets/07875c85-5700-4053-8a11-230c4b2de5dd)

Any suggestion and help shall be highly appreciated. Thanks


# Discussion History
## SChernykh | 2025-01-14T17:57:05+00:00
Unfortunately this is a GCC compiler bug for software AES versions of the algorithm (your CPU doesn't support hardware AES). You could try to build XMRig with clang compiler.

# Action History
- Created by: KHPak2023 | 2025-01-14T11:35:34+00:00
