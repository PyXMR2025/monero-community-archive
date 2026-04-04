---
title: '''error.h'' file not found with <angled> include; use "quotes" instead'
source_url: https://github.com/monero-project/monero/issues/5296
author: mariodian
assignees: []
labels: []
created_at: '2019-03-15T12:31:24+00:00'
updated_at: '2019-03-16T22:25:12+00:00'
type: issue
status: closed
closed_at: '2019-03-16T22:25:12+00:00'
---

# Original Description
Hey! Trying to build the master on Mac (for Trezor support) and it gives me the following error:

```
Building CXX object src/common/CMakeFiles/obj_common.dir/timings.cc.o
/Users/mariodian/Source/Monero/monero/src/common/timings.cc:2:10: error: 'error.h' file not found with <angled> include; use "quotes" instead
#include <error.h>
         ^~~~~~~~~
         "error.h"
1 error generated.
make[3]: *** [src/common/CMakeFiles/obj_common.dir/timings.cc.o] Error 1
make[2]: *** [src/common/CMakeFiles/obj_common.dir/all] Error 2
make[1]: *** [all] Error 2
make: *** [release-all] Error 2
```

When I change `#include <error.h>` to `#include "error.h"` in `src/common/CMakeFiles/obj_common.dir/timings.cc.` it compiles without errors.

I've been having this issue for quite some time now (can't be more specific sorry). 

Running MacOS 10.14.3 with Xcode 10.1

# Discussion History
## moneromooo-monero | 2019-03-15T12:54:41+00:00
It's not the right file though, you want #5249.

## mariodian | 2019-03-15T13:32:18+00:00
Oh I see. Thanks! 

## moneromooo-monero | 2019-03-16T22:18:40+00:00
+resolved

# Action History
- Created by: mariodian | 2019-03-15T12:31:24+00:00
- Closed at: 2019-03-16T22:25:12+00:00
