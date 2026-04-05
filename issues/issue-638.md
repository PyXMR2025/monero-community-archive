---
title: '2.6.2:  supportxmr.com:3333: low difficulty share'
source_url: https://github.com/xmrig/xmrig/issues/638
author: tkalfaoglu
assignees: []
labels: []
created_at: '2018-05-19T07:44:54+00:00'
updated_at: '2018-05-19T07:52:05+00:00'
type: issue
status: closed
closed_at: '2018-05-19T07:52:04+00:00'
---

# Original Description
With 2.6.2 and cn-heavy, I'm getting low difficulty share errors:

rejected (0/3) diff 4999 "Low Difficulty share" (254ms)

Windows 8.1.. 
in config:  av:0 , huge-pages: true, variant:0 

# Discussion History
## xmrig | 2018-05-19T07:49:10+00:00
For Monero algorithm should be `cn` not `cn-heavy` and variant is `1`. https://github.com/xmrig/xmrig/blob/master/doc/ALGORITHMS.md
Thank you.

## tkalfaoglu | 2018-05-19T07:52:04+00:00
great help thank you.. The machine instantly became unresponsive after the changes.. Now I know it's working correctly! :)


# Action History
- Created by: tkalfaoglu | 2018-05-19T07:44:54+00:00
- Closed at: 2018-05-19T07:52:04+00:00
