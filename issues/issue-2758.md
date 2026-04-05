---
title: Cache Value Displayed under VMware is Incorrect
source_url: https://github.com/xmrig/xmrig/issues/2758
author: x86txt
assignees: []
labels:
- question
created_at: '2021-11-30T01:29:44+00:00'
updated_at: '2021-12-19T15:12:44+00:00'
type: issue
status: closed
closed_at: '2021-12-19T15:12:43+00:00'
---

# Original Description
When running XMRig under VMware ESXi, the cache value displayed is incorrect. My (Zen 2) Epyc 7302p reports 256MB of L3 and my 5700G reports 32MB - both are 2x what is actually on the chip. It doesn't seem to affect performance and appears to merely be a cosmetic bug, but I thought I'd report it for completeness.

![7302p](https://user-images.githubusercontent.com/34278354/143969076-c716bcfd-4ca9-4848-92b8-4d7335f7b8d9.png)

![5700G](https://user-images.githubusercontent.com/34278354/143968788-4f1b0219-f210-4dca-a826-2554c39a571b.png)




# Discussion History
## xmrig | 2021-12-19T15:12:43+00:00
This is how VMware reports CPU topology and this may affect performance since auto configuration may use more threads than actually optimal which is not issue for recent AMD CPUs since they have enough cache anyway.
Thank you.

# Action History
- Created by: x86txt | 2021-11-30T01:29:44+00:00
- Closed at: 2021-12-19T15:12:43+00:00
