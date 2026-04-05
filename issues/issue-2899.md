---
title: ARMv7l not supported
source_url: https://github.com/xmrig/xmrig/issues/2899
author: royjrm
assignees: []
labels:
- bug
- arm
created_at: '2022-01-25T21:06:15+00:00'
updated_at: '2025-06-16T20:26:50+00:00'
type: issue
status: closed
closed_at: '2025-06-16T20:26:49+00:00'
---

# Original Description
**Describe the bug**
At the moment of building an error related with the ARM version is raised.

**To Reproduce**

- Clone repo
- Go to repo folder and create a build folder
- Use cmake command `cmake ..`
- Use make command `make`

**Expected behavior**
Application should be compiled and built.

**Required data**
![image](https://user-images.githubusercontent.com/36004884/151059657-28c89186-0ef5-4075-92b9-d8251f040bf7.png)

**Additional context**
Add any other context about the problem here.


# Discussion History
## SChernykh | 2022-01-25T21:27:14+00:00
It was fixed in https://github.com/xmrig/xmrig/pull/2898

# Action History
- Created by: royjrm | 2022-01-25T21:06:15+00:00
- Closed at: 2025-06-16T20:26:49+00:00
