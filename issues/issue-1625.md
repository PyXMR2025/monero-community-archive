---
title: How can I change which core to mine?
source_url: https://github.com/xmrig/xmrig/issues/1625
author: IAMPARKSANG
assignees: []
labels:
- question
created_at: '2020-03-29T05:09:12+00:00'
updated_at: '2020-08-29T04:55:36+00:00'
type: issue
status: closed
closed_at: '2020-08-29T04:55:31+00:00'
---

# Original Description
![image](https://user-images.githubusercontent.com/48522014/77840794-2a939600-71c6-11ea-8582-7d498abfea01.png)

I am mining with 5 cores, and other one core is doing web surfing or else with .  I've set my cpu to use only 5 cores for mining and I am worried about cpu0,1,2,3,4 working too much. 
How can I choose which core to work? I want 1,2,3,4,5 to mine and cpu0 to do other things 

# Discussion History
## setuidroot | 2020-03-29T19:24:02+00:00
You'd do this by setting the CPU thread affinity... it's easier just to show you.  Can you post your current config.json file?

If you do so, I will modify it to set affinity to the CPU threads you want it to mine on.

Otherwise, just read here about thread affinity: https://github.com/xmrig/xmrig/blob/dev/doc/CPU.md

Keep in mind that Windows does some funny stuff with threads so you may have to affine to all odd or all even cores to get the outcome you want.

# Action History
- Created by: IAMPARKSANG | 2020-03-29T05:09:12+00:00
- Closed at: 2020-08-29T04:55:31+00:00
