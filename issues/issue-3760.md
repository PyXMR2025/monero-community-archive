---
title: '[ 96%] Linking CXX executable unit_tests error'
source_url: https://github.com/monero-project/monero/issues/3760
author: nicebbs
assignees: []
labels:
- invalid
created_at: '2018-05-06T11:27:49+00:00'
updated_at: '2018-08-19T07:50:21+00:00'
type: issue
status: closed
closed_at: '2018-05-16T23:40:53+00:00'
---

# Original Description
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/5/../../../../lib/libgtest.a(gtest-all.cc.o): relocation R_X86_64_32 against `.rodata' can not be used when making a shared object; recompile with -fPIC
/usr/lib/gcc/x86_64-linux-gnu/5/../../../../lib/libgtest.a: 无法添加符号: 错误的值
collect2: error: ld returned 1 exit status
tests/unit_tests/CMakeFiles/unit_tests.dir/build.make:1206: recipe for target 'tests/unit_tests/unit_tests' failed
make[3]: *** [tests/unit_tests/unit_tests] Error 1

# Discussion History
## dEBRUYNE-1 | 2018-05-06T11:39:20+00:00
Your logs are fairly explanatory:

>recompile with -fPIC
 



## moneromooo-monero | 2018-05-16T23:33:36+00:00
For libgtest, you can also uninstall the system one, monero can use its internal one (which it builds with -fPIC).

+invalid

## calidion | 2018-08-19T07:32:06+00:00
@moneromooo-monero 
any detailed steps?

how to use the internal one?

I followed the instuctions on the readme file, but can not get through this

# Action History
- Created by: nicebbs | 2018-05-06T11:27:49+00:00
- Closed at: 2018-05-16T23:40:53+00:00
