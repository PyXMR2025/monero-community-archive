---
title: msys64 build error.
source_url: https://github.com/xmrig/xmrig/issues/1764
author: snipeTR
assignees: []
labels: []
created_at: '2020-07-04T14:37:59+00:00'
updated_at: '2020-07-04T18:14:45+00:00'
type: issue
status: closed
closed_at: '2020-07-04T18:14:45+00:00'
---

# Original Description
mkdir build
cd build
cmake .. -G "Unix Makefiles" -DXMRIG_DEPS=c:/xmrig-deps/gcc/x86
make
i dont change source code.

![image](https://user-images.githubusercontent.com/31975916/86514500-56549680-be1b-11ea-9d8e-5f59973e8733.png)
![image](https://user-images.githubusercontent.com/31975916/86514747-949e8580-be1c-11ea-97ae-8007087a7a9f.png)
![image](https://user-images.githubusercontent.com/31975916/86514780-f363ff00-be1c-11ea-91a3-c49fedcfca49.png)
![image](https://user-images.githubusercontent.com/31975916/86514788-01198480-be1d-11ea-9032-4539ecabcc12.png)


# Discussion History
## xmrig | 2020-07-04T15:20:17+00:00
If you try build 64 bit version, remove all generated cmake files and use `-DXMRIG_DEPS=c:/xmrig-deps/gcc/x64`

Otherwise use `mingw32.exe` shell instead of `mingw64.exe`.
Thank you.

## snipeTR | 2020-07-04T18:14:43+00:00
ohhh shit!! again u'r rock

# Action History
- Created by: snipeTR | 2020-07-04T14:37:59+00:00
- Closed at: 2020-07-04T18:14:45+00:00
