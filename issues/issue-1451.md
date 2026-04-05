---
title: Broken CN/PICO algorithm
source_url: https://github.com/xmrig/xmrig/issues/1451
author: mtl1979
assignees: []
labels:
- duplicate
created_at: '2019-12-21T03:44:56+00:00'
updated_at: '2019-12-21T20:28:40+00:00'
type: issue
status: closed
closed_at: '2019-12-21T20:02:05+00:00'
---

# Original Description
**Describe the bug**
AES mask for CN_PICO is hardcoded as 0x1FFF0, when it can be either 0x1FFF0 or 0x3FFF0

**To Reproduce**
Try mining Talleo, which uses CryptoNight Ultra Variant 2

**Expected behavior**
No rejected shares

**Required data**
pool.talleo.org:8888
TA4yACzMYuFYq7V6xVAWYHeS39jQ8w4mKRowpY6NskGuS1rZpjcWuCpdeCypwUCJrK9mGqVW9o1pY2EG3HW7BZkR2YRcc4YNa

**Additional context**
CN_PICO_0 is CryptoNight Ultra Lite Variant 2, which is not same as CryptoNight Turtle/Ultra/Pico Variant 2 defined in original TurtleCoin multi-hashing library.
To support real CryptoNight Turtle/Ultra/Pico Variant 2 (CN_PICO_2?), the AES mask can't be patched in assembler code just by choosing base algorithm.


# Discussion History
## xmrig | 2019-12-21T20:02:05+00:00
Duplicate #1399

## mtl1979 | 2019-12-21T20:28:39+00:00
Not quite duplicate, more like prerequisite... Can't really make pull request as it would break support for existing coins... The whole Pico/Ultra/Turtle ambiguous naming scheme happened with xmr-stak too, but their algorithm code was smarter, so required only minor adjustment...

# Action History
- Created by: mtl1979 | 2019-12-21T03:44:56+00:00
- Closed at: 2019-12-21T20:02:05+00:00
