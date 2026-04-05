---
title: Why there is asm for vs 2015 separately
source_url: https://github.com/xmrig/xmrig/issues/997
author: adevelopcr
assignees: []
labels:
- question
created_at: '2019-03-19T11:07:01+00:00'
updated_at: '2019-04-01T06:09:53+00:00'
type: issue
status: closed
closed_at: '2019-04-01T06:09:53+00:00'
---

# Original Description
In asm.cmake vs 2017 has its asm code in crypto/asm/win64 dir while vs 2015 has its asm code in the crypto/asm dir
Is there any difference between them

# Discussion History
## xmrig | 2019-04-01T06:09:53+00:00
`movq` -> `movd`, you can use any tool to compare files.
Thank you.

# Action History
- Created by: adevelopcr | 2019-03-19T11:07:01+00:00
- Closed at: 2019-04-01T06:09:53+00:00
