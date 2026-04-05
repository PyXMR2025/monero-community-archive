---
title: Termux support not available or removed.
source_url: https://github.com/xmrig/xmrig/issues/2079
author: Surajkumarsaw1
assignees: []
labels: []
created_at: '2021-02-03T17:51:26+00:00'
updated_at: '2021-02-12T12:52:29+00:00'
type: issue
status: closed
closed_at: '2021-02-12T12:52:28+00:00'
---

# Original Description
[ 76%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/VirtualMemory_unix.cpp.o
/data/data/com.termux/files/home/xmrig/src/crypto/common/VirtualMemory_unix.cpp:153:124: error: use of undeclared identifier 'hugePagesFlag'
        mem = mmap(0, align(size), PROT_READ | PROT_WRITE | SECURE_PROT_EXEC, MAP_PRIVATE | MAP_ANONYMOUS | MAP_POPULATE | hugePagesFlag(hugePageSize()), -1, 0);


     ^
/data/data/com.termux/files/home/xmrig/src/crypto/common/VirtualMemory_unix.cpp:173:114: error: use of undeclared identifier 'hugePagesFlag'
    void *mem = mmap(0, size, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS | MAP_HUGETLB | MAP_POPULATE | hugePagesFlag(hugePageSize()), 0, 0);

                                                      ^
2 errors generated.

# Discussion History
## SChernykh | 2021-02-03T17:59:46+00:00
Can you try https://github.com/xmrig/xmrig/pull/2080 ?

## SChernykh | 2021-02-03T18:07:43+00:00
I've just checked and #2080 fixed it for me.

## Surajkumarsaw1 | 2021-02-03T18:18:54+00:00
No it gives same error.

## SChernykh | 2021-02-04T09:11:12+00:00
I repeat - I had the same compile error in Termux and it fixed the error. Try the latest dev branch now.

## Surajkumarsaw1 | 2021-02-06T17:45:19+00:00
I have xmrig build for termux arm aarch64 in my [repository xmrig](https://github.com/Surajkumarsaw1/xmrig.git)

## diminDDL | 2021-02-09T22:53:17+00:00
As @SChernykh said I just copied the new VirtualMemory_unix.cpp file in to my failed build and tried again. After that it finished without a problem.

## xmrig | 2021-02-12T12:52:28+00:00
https://github.com/xmrig/xmrig/releases/tag/v6.8.2

# Action History
- Created by: Surajkumarsaw1 | 2021-02-03T17:51:26+00:00
- Closed at: 2021-02-12T12:52:28+00:00
