---
title: About the default CPU usage of 50%
source_url: https://github.com/xmrig/xmrig/issues/3044
author: ttsite
assignees: []
labels: []
created_at: '2022-05-07T13:19:35+00:00'
updated_at: '2025-06-28T10:37:23+00:00'
type: issue
status: closed
closed_at: '2025-06-28T10:37:23+00:00'
---

# Original Description
If I want to make the CPU of any new machine occupy 50% by default, do I need to set it in config.json
![50](https://user-images.githubusercontent.com/43260559/167256146-634b59fe-f0ba-4660-b577-d41e19dd213e.png)
 file is changed to this or what kind of in the figure. Please help thank you

# Discussion History
## snipeTR | 2022-05-07T15:00:17+00:00
Run cmd and type
Start "" /low cmd x:\somedirectory\xmrig.exe
you will not slow down any other application.

## ttsite | 2022-05-07T15:42:43+00:00



> Run cmd and type Start "" /low cmd x:\somedirectory\xmrig.exe you will not slow down any other application.

config.json I want to add it to this configuration file. How can I fill in the default occupation of 50%

## Spudz76 | 2022-05-07T17:30:39+00:00
You would delete that line from the config.json and if there are already algorithm thread profiles in the config.json delete those too, and then use `./xmrig --cpu-max-threads-hint=50` so the option applies (it doesn't work from inside the config.json, config.json always wins over commandline options, and it doesn't run thread-config unless there are no profiles).

Or just hand-edit the existing thread profiles to drop some threads.

## ttsite | 2022-05-08T03:11:13+00:00
> You would delete that line from the config.json and if there are already algorithm thread profiles in the config.json delete those too, and then use `./xmrig --cpu-max-threads-hint=50` so the option applies (it doesn't work from inside the config.json, config.json always wins over commandline options, and it doesn't run thread-config unless there are no profiles).
> 
> Or just hand-edit the existing thread profiles to drop some threads.

Add     "max-cpu-usage": 75,  config.json  Is this option available now?

# Action History
- Created by: ttsite | 2022-05-07T13:19:35+00:00
- Closed at: 2025-06-28T10:37:23+00:00
