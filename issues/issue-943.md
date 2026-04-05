---
title: Startup message not consitant on xmrig
source_url: https://github.com/xmrig/xmrig/issues/943
author: lhirlimann
assignees: []
labels: []
created_at: '2019-02-22T21:32:06+00:00'
updated_at: '2019-08-02T12:02:00+00:00'
type: issue
status: closed
closed_at: '2019-08-02T12:02:00+00:00'
---

# Original Description
 * CPU          ARMv8 (1) x64 -AES -AVX2

ARMV8 should be enough :)

# Discussion History
## xmrig | 2019-02-23T02:31:16+00:00
Actually you are right `x64` and `AVX2` can be removed, but AES is still useful information, in your case CPU lacks hardware AES support.
Thank you.

## lhirlimann | 2019-02-23T10:40:01+00:00
can you point me where that part of the code lies so I can do patch/PR ?

# Action History
- Created by: lhirlimann | 2019-02-22T21:32:06+00:00
- Closed at: 2019-08-02T12:02:00+00:00
