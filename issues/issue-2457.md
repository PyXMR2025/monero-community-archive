---
title: Unable to run xmrig after compiling from source.
source_url: https://github.com/xmrig/xmrig/issues/2457
author: Joe23232
assignees: []
labels:
- question
created_at: '2021-06-26T11:04:47+00:00'
updated_at: '2021-06-28T12:23:41+00:00'
type: issue
status: closed
closed_at: '2021-06-28T12:23:41+00:00'
---

# Original Description
Hi, after compiling `xmrig` from source, When I tried to run it via powershell (for Windows) I get the following errors:

```cmd
[2021-06-26 21:02:15.908] unable to open "C:\Users\joe\Desktop\building\xmrig\build\config.json".
[2021-06-26 21:02:15.909] unable to open "C:\Users\joe\.xmrig.json".
[2021-06-26 21:02:15.909] unable to open "C:\Users\joe\.config\xmrig.json".
[2021-06-26 21:02:15.909] no valid configuration found, try https://xmrig.com/wizard
```

I am not too sure how to solve this? Do I have to run something else?

# Discussion History
## Spudz76 | 2021-06-26T14:18:56+00:00
Make a base config with the [config generator](https://xmrig.com/wizard)

## Joe23232 | 2021-06-27T02:41:46+00:00
I see thanks

## Joe23232 | 2021-06-27T05:11:53+00:00
![image](https://user-images.githubusercontent.com/34926497/123533576-eb058200-d759-11eb-8fbd-d802a75d3eed.png)

WHat would be the most recommended one to use?

@Spudz76 

# Action History
- Created by: Joe23232 | 2021-06-26T11:04:47+00:00
- Closed at: 2021-06-28T12:23:41+00:00
