---
title: Custom API output
source_url: https://github.com/xmrig/xmrig/issues/3415
author: dexmar
assignees: []
labels:
- question
created_at: '2024-02-01T04:31:20+00:00'
updated_at: '2024-02-21T20:39:49+00:00'
type: issue
status: closed
closed_at: '2024-02-21T20:39:48+00:00'
---

# Original Description
A question, not a bug:


Is there a method to inject custom data into the xmrig api output? I want to add CoreFreq CPU temps so that the API will output the data. I could repurpose a field in the config.json and switch off auto restart but am hopeful there is another way.

Thanks!


# Discussion History
## geekwilliams | 2024-02-01T07:15:22+00:00
There's no built-in way to do this. You'll need to recompile your own version of xmrig with the changes you'd like 

# Action History
- Created by: dexmar | 2024-02-01T04:31:20+00:00
- Closed at: 2024-02-21T20:39:48+00:00
