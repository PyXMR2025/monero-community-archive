---
title: Error while compiling arm
source_url: https://github.com/xmrig/xmrig/issues/468
author: JonyTester
assignees: []
labels:
- arm
created_at: '2018-03-21T09:17:23+00:00'
updated_at: '2019-02-16T01:08:29+00:00'
type: issue
status: closed
closed_at: '2018-04-12T12:10:43+00:00'
---

# Original Description
Hi, only for fun I´m trying to compile your ARM branch for my Android but I have this error.. 

After executing cmake . -DWITH_HTTPD=OFF && make VERBOSE=1

I get this: 

usr/lib/clang/5.0.1/include/x86intrin.h:27:
/data/data/com.termux/files/usr/lib/clang/5.0.1/include/ia32intrin.h:48:10: error: use of undeclared identifier '__builtin_ia32_readeflags_u32'
  return __builtin_ia32_readeflags_u32();

Note: I´m not cross-compiling I´m compiling in the device using a termux terminal.

any clue of what is going on?

thanks in advance

# Discussion History
## JonyTester | 2018-04-12T12:10:43+00:00
Error fixed with the last update :-)

## hozachief | 2019-02-16T01:08:28+00:00
I have a similar issue. I have an error that reads, "Use of undeclared identifier '__builtin_ia32_readeflags_u32'". @JonyTester would you mind elaborating how you solved this error?

# Action History
- Created by: JonyTester | 2018-03-21T09:17:23+00:00
- Closed at: 2018-04-12T12:10:43+00:00
