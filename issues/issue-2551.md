---
title: use HTTP API Program Exit
source_url: https://github.com/xmrig/xmrig/issues/2551
author: Zy143L
assignees: []
labels: []
created_at: '2021-08-22T03:08:42+00:00'
updated_at: '2021-08-23T16:58:55+00:00'
type: issue
status: closed
closed_at: '2021-08-23T16:58:55+00:00'
---

# Original Description
![image](https://user-images.githubusercontent.com/21352718/130340540-759396ac-2637-4cc7-99b7-946ab153abed.png)
![image](https://user-images.githubusercontent.com/21352718/130340547-f6c28fed-9b35-4d4e-8a88-d9de42f70f95.png)
## The program exits abnormally after clicking apply

# Discussion History
## xmrig | 2021-08-23T13:20:11+00:00
Please show your config and new config if you make changes and not just click the button.
Thank you.


## Zy143L | 2021-08-23T13:22:08+00:00
Click apply and xmrig exits with no change in config.json

## xmrig | 2021-08-23T13:36:32+00:00
Already did it and all works fine, so need more details to reproduce this bug.
Thank you.


## Zy143L | 2021-08-23T13:39:43+00:00
I changed `src\base\kernel\Base.cpp` # 140
        chain.addFile(Process::location(Process::DataLocation, "config.json"));
Change to
     chain.addFile(Process::location(Process::DataLocation, "config.dat"));

## Zy143L | 2021-08-23T16:58:55+00:00
Problem Resolution

# Action History
- Created by: Zy143L | 2021-08-22T03:08:42+00:00
- Closed at: 2021-08-23T16:58:55+00:00
