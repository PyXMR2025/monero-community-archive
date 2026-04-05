---
title: CMake with Visual Studio 2022
source_url: https://github.com/xmrig/xmrig/issues/2816
author: kimpurcell
assignees: []
labels: []
created_at: '2021-12-16T10:54:54+00:00'
updated_at: '2021-12-16T11:03:39+00:00'
type: issue
status: closed
closed_at: '2021-12-16T11:03:38+00:00'
---

# Original Description
Can't seem to build this with VS 2022.

Referring to the xmrig docs here: https://xmrig.com/docs/miner/build/windows

How do I specify cmake?
I tried 

`cmake .. -G "Visual Studio 17 2022" -A x64 -DXMRIG_DEPS=c:\xmrig-deps\msvc2019\x64`

and I get the error  

`CMake Error: Could not create named generator Visual Studio 17 2022`




# Discussion History
## kimpurcell | 2021-12-16T11:03:38+00:00
Nevermind, just needed to update CMake. 🙄

# Action History
- Created by: kimpurcell | 2021-12-16T10:54:54+00:00
- Closed at: 2021-12-16T11:03:38+00:00
