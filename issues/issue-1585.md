---
title: WITH_HTTP=OFF cmake option fails to link
source_url: https://github.com/xmrig/xmrig/issues/1585
author: turtleminor13
assignees: []
labels:
- bug
created_at: '2020-03-07T22:16:59+00:00'
updated_at: '2020-03-08T08:17:23+00:00'
type: issue
status: closed
closed_at: '2020-03-08T08:17:23+00:00'
---

# Original Description
**Describe the bug**
Using cmake option WITH_HTTP=OFF fails to link with undefined reference errors

**To Reproduce**
xmrig v5.8.2 on ubuntu with gcc 8.3, link fails 

![image](https://user-images.githubusercontent.com/49797136/76153235-28825f80-607e-11ea-9372-4a23a9fd6317.png)

![image](https://user-images.githubusercontent.com/49797136/76153211-e35e2d80-607d-11ea-88d4-05188be2b836.png)


# Discussion History
## xmrig | 2020-03-08T08:17:23+00:00
Fixed https://github.com/xmrig/xmrig/releases/tag/v5.9.0

# Action History
- Created by: turtleminor13 | 2020-03-07T22:16:59+00:00
- Closed at: 2020-03-08T08:17:23+00:00
