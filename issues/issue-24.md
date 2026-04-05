---
title: Make failed on OSX
source_url: https://github.com/xmrig/xmrig/issues/24
author: kurakin-oleksandr
assignees: []
labels: []
created_at: '2017-07-03T07:55:44+00:00'
updated_at: '2017-07-03T09:16:51+00:00'
type: issue
status: closed
closed_at: '2017-07-03T09:16:51+00:00'
---

# Original Description
I got this error on 2.0.0 version:
```
[ 35%] Building CXX object CMakeFiles/xmrig.dir/src/Cpu_mac.cpp.o
/Users/kurakin/www/ethereum/xmrig/src/Cpu_mac.cpp:43:11: error: out-of-line definition of 'setAffinity' does not match any declaration in 'Cpu'
void Cpu::setAffinity(int id, unsigned long mask)

```

# Discussion History
## xmrig | 2017-07-03T08:04:58+00:00
Please check again, probably I fix OS X support. Nowhere to check by self now.

## kurakin-oleksandr | 2017-07-03T09:16:39+00:00
Yes, it works now

# Action History
- Created by: kurakin-oleksandr | 2017-07-03T07:55:44+00:00
- Closed at: 2017-07-03T09:16:51+00:00
