---
title: MSVC 2015 LINK Error
source_url: https://github.com/xmrig/xmrig/issues/380
author: hgs81
assignees: []
labels: []
created_at: '2018-02-02T13:44:03+00:00'
updated_at: '2018-11-05T07:10:57+00:00'
type: issue
status: closed
closed_at: '2018-11-05T07:10:57+00:00'
---

# Original Description
Please help me fix this error during MSVC 2015 compilation.
I am using latest xmrig-deps binaries, and using cmake-3.8.1-win64-x64.
```
...
3>  Api.obj : MSIL .netmodule or module compiled with /GL found; restarting link with /LTCG; add /LTCG to the link command line to improve linker performance
3>LINK : fatal error C1047: The object or library file 'xmrig.dir\Release\Api.obj' was created with an older compiler than other objects; rebuild old objects and libraries
3>LINK : fatal error LNK1257: code generation failed
```

# Discussion History
## RansomFuck | 2018-02-12T22:35:11+00:00
Build -> Clear *project-name*

## hgs81 | 2018-02-12T22:36:57+00:00
I tried but same error occurs.

## enwillyado | 2018-02-18T20:32:42+00:00
Check the VS project in https://github.com/enwillyado/xmrig/.

# Action History
- Created by: hgs81 | 2018-02-02T13:44:03+00:00
- Closed at: 2018-11-05T07:10:57+00:00
