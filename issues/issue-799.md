---
title: MSVC2015 x32 compile error
source_url: https://github.com/xmrig/xmrig/issues/799
author: FusixGit
assignees: []
labels: []
created_at: '2018-10-15T08:22:18+00:00'
updated_at: '2018-10-15T10:29:06+00:00'
type: issue
status: closed
closed_at: '2018-10-15T10:29:06+00:00'
---

# Original Description
Hello. I'm trying to compile a project under x32 and this error appears:
`CryptoNight_x86.h(450): error C2719: "cx": formal parameter with "16" won't be aligned`
When compiling 64 everything goes well. How can I fix this?
xmrig 2.8.1

# Discussion History
## FusixGit | 2018-10-15T09:35:15+00:00
On MSVC2017, the compilation of both versions of the project is successful. It appears that the problem only appears on MSVC2015 (or earlier)

## FusixGit | 2018-10-15T10:29:00+00:00
Issue resolved by adding __vectorcall call convention to the definition of the function

# Action History
- Created by: FusixGit | 2018-10-15T08:22:18+00:00
- Closed at: 2018-10-15T10:29:06+00:00
