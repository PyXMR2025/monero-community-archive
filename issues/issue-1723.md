---
title: compile error xmrig 5.11.2 dev 4.1
source_url: https://github.com/xmrig/xmrig/issues/1723
author: snipeTR
assignees: []
labels: []
created_at: '2020-06-08T17:11:50+00:00'
updated_at: '2020-06-10T10:30:52+00:00'
type: issue
status: closed
closed_at: '2020-06-10T10:30:52+00:00'
---

# Original Description
i dont pass %73
![image](https://user-images.githubusercontent.com/31975916/84060064-3d93c500-a9c4-11ea-911b-8f26e364237d.png)


# Discussion History
## xmrig | 2020-06-08T18:22:59+00:00
Don't use path with spaces and special characters or remove this line https://github.com/xmrig/xmrig/blob/master/CMakeLists.txt#L135.
Thank you.

## snipeTR | 2020-06-08T18:39:02+00:00
u'r rock

## snipeTR | 2020-06-08T19:21:59+00:00
x86 compile complate but not run xmrig.exe 
no error. no log. no dry run. yes --help. yes "no config error". but not run command.

# Action History
- Created by: snipeTR | 2020-06-08T17:11:50+00:00
- Closed at: 2020-06-10T10:30:52+00:00
