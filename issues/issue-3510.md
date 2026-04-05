---
title: add cpu algo xelishhashv2 to xmrig
source_url: https://github.com/xmrig/xmrig/issues/3510
author: sfhdfshdfh
assignees: []
labels: []
created_at: '2024-07-11T07:26:59+00:00'
updated_at: '2024-07-11T12:56:48+00:00'
type: issue
status: closed
closed_at: '2024-07-11T12:56:48+00:00'
---

# Original Description
please add xelishhashv2 algo to xmrig since it became cpu friendly now and pools like herominers have it. 
it should also utilize avx512 instruction of cpu if available.
and you might wanna add salvium in randomx coins but silently since it may or may not survive out there.
thank you.

# Discussion History
## SChernykh | 2024-07-11T08:15:39+00:00
Xelis project had a questionable launch: https://bitcointalk.org/index.php?topic=5493934.msg63992605#msg63992605
and they hardforked to a new algorithm less than 3 months after it launched.

I'm afraid that if I invest time and effort into implementing and optimizing it, it will all go down the drain pretty quickly - one way or another. Either they will hardfork to a new algorithm again, or the price will dump to near 0, or they rug pull...

As for Salvium - they use normal rx/0, and as soon as there are pools for it, XMRig will be able to mine it without modification.

# Action History
- Created by: sfhdfshdfh | 2024-07-11T07:26:59+00:00
- Closed at: 2024-07-11T12:56:48+00:00
