---
title: Failed to start WinRing0 driver error 183
source_url: https://github.com/xmrig/xmrig/issues/2508
author: geosimsimma
assignees: []
labels: []
created_at: '2021-08-03T19:41:22+00:00'
updated_at: '2021-08-04T12:59:01+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Starting XMrig 6.13.1 as admin I get the error message:

Failed to start WinRin0 driver, error 183.

No VM. I tried starting it from the cmd prompt as admin and get the same issue. 

![image](https://user-images.githubusercontent.com/55563569/128075929-189a9492-b276-4f2d-8edf-e922b84131a9.png)



# Discussion History
## SChernykh | 2021-08-03T20:02:21+00:00
You are running some other software that uses WinRing0.sys. It can be hardware monitor, RGB control utility etc. Try to stop or restart it. If it doesn't help, reinstall it.

## geosimsimma | 2021-08-04T12:59:01+00:00
Maybe it is aquasuite from aquacomputer? I'll try to reinstall it

# Action History
- Created by: geosimsimma | 2021-08-03T19:41:22+00:00
