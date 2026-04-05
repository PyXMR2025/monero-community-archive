---
title: '[solved] cannot build on FreeBSD 10'
source_url: https://github.com/xmrig/xmrig/issues/839
author: codeorcode
assignees: []
labels:
- bug
created_at: '2018-10-23T15:07:49+00:00'
updated_at: '2018-11-05T06:55:43+00:00'
type: issue
status: closed
closed_at: '2018-11-05T06:55:43+00:00'
---

# Original Description
When I run:

```
cmake .. -DCMAKE_C_COMPILER=gcc6 -DCMAKE_CXX_COMPILER=g++6
make
```

I got:

```
Linking CXX executable xmrig
/usr/local/bin/ld: cannot find -ldl
collect2: error: ld returned 1 exit status
*** Error code 1
```

xmrig-.2.6 compiled ok.

I've also tried:

`cmake .. -DCMAKE_C_COMPILER=gcc6 -DCMAKE_CXX_COMPILER=g++6 -DCMAKE_EXE_LINKER_FLAGS=-L/usr/local/lib -DCMAKE_SHARED_LINKER_FLAGS=-L/usr/local/lib`

gcc is version: gcc6-6.4.0_3

Any hint?

**Update:** I've managed to compile by removing **-ldl** from _./build/CMakeFiles/xmrig.dir/link.txt_


# Discussion History
## xmrig | 2018-10-24T02:57:17+00:00
Please check this commit https://github.com/xmrig/xmrig/commit/acd042c23454c2be617cbdf4d1b562b7c542a2c1 in dev branch, it should solve this issue.
Thank you.

# Action History
- Created by: codeorcode | 2018-10-23T15:07:49+00:00
- Closed at: 2018-11-05T06:55:43+00:00
