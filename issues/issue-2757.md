---
title: Build failed with WITH_OPENCL option disabled (v6.16.1)
source_url: https://github.com/xmrig/xmrig/issues/2757
author: timk74
assignees: []
labels: []
created_at: '2021-11-30T00:48:43+00:00'
updated_at: '2021-11-30T02:05:04+00:00'
type: issue
status: closed
closed_at: '2021-11-30T02:04:45+00:00'
---

# Original Description
**To Reproduce**
```
cmake .. -G "Visual Studio 16 2019" -A "x64" -DXMRIG_DEPS="..\xmrig-deps\msvc2019\x64" -DWITH_OPENCL=OFF
cmake --build . --config Release
```
![error](https://user-images.githubusercontent.com/43396824/143965293-45971ef4-7aa7-4328-ac29-1e48a0974c7d.png)


# Discussion History
## Spudz76 | 2021-11-30T01:06:15+00:00
I just compiled fine under MSVC `19.29.30137.0` (include path version `14.29.30133`) with `-DWITH_OPENCL=OFF`

Unsure how to revert to older `14.24.28314` to attempt to reproduce.  But if you can update from the Visual Studio Installer, it will work due to updated includes.

## timk74 | 2021-11-30T02:04:45+00:00
> But if you can update from the Visual Studio Installer, it will work due to updated includes.

Thanks, the latest updates helps.


# Action History
- Created by: timk74 | 2021-11-30T00:48:43+00:00
- Closed at: 2021-11-30T02:04:45+00:00
