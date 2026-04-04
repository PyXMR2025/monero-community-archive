---
title: make failed on centos7(call to non-constexpr function)
source_url: https://github.com/monero-project/monero/issues/6400
author: liuxh-go
assignees: []
labels: []
created_at: '2020-03-24T01:55:08+00:00'
updated_at: '2022-04-08T16:42:19+00:00'
type: issue
status: closed
closed_at: '2022-04-08T16:42:19+00:00'
---

# Original Description
this is print:
```bash
...
[ 36%] Building CXX object external/randomx/CMakeFiles/randomx.dir/src/instruction.cpp.o
[ 36%] Building CXX object external/randomx/CMakeFiles/randomx.dir/src/randomx.cpp.o
/data/wanthings_projects/xmr/monero/external/randomx/src/randomx.cpp: 在函数‘randomx_cache* randomx_alloc_cache(randomx_flags)’中:
/data/wanthings_projects/xmr/monero/external/randomx/src/randomx.cpp:97:27: 错误：call to non-constexpr function ‘randomx_flags operator|(randomx_flags, randomx_flags)’
     case RANDOMX_FLAG_JIT | RANDOMX_FLAG_LARGE_PAGES:
                           ^
/data/wanthings_projects/xmr/monero/external/randomx/src/randomx.cpp:97:27: 错误：call to non-constexpr function ‘randomx_flags operator|(randomx_flags, randomx_flags)’
/data/wanthings_projects/xmr/monero/external/randomx/src/randomx.cpp: 在函数‘randomx_vm* randomx_create_vm(randomx_flags, randomx_cache*, randomx_dataset*)’中:
/data/wanthings_projects/xmr/monero/external/randomx/src/randomx.cpp:219:32: 错误：call to non-constexpr function ‘randomx_flags operator|(randomx_flags, randomx_flags)’
...
```

my gcc version is 4.8.5, code branch is release-v0.15.

How can i solve this?

# Discussion History
## selsta | 2020-03-24T02:15:26+00:00
Can you upgrade gcc to version 7?

## liuxh-go | 2020-03-24T03:42:14+00:00
I upgraded the gcc version to 7.5.0 and still report this error . @selsta 

## sumogr | 2020-03-24T06:41:51+00:00
Its a gcc bug like @selsta said @wshhz https://gcc.gnu.org/bugzilla/show_bug.cgi?id=86678
Update gcc by installing dev-toolset9 package and type `gcc --version` to see if its properly installed

## selsta | 2022-04-08T16:42:19+00:00
See @sumogr comment. Also we had no other reports about this -> closing.

# Action History
- Created by: liuxh-go | 2020-03-24T01:55:08+00:00
- Closed at: 2022-04-08T16:42:19+00:00
