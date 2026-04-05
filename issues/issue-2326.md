---
title: './xmrig:  /lib/x86_64-linux-gnu/libm.so.6: version `GLIBC_2.29'' not found'
source_url: https://github.com/xmrig/xmrig/issues/2326
author: 03lenio
assignees: []
labels: []
created_at: '2021-04-28T23:55:07+00:00'
updated_at: '2023-07-12T23:33:00+00:00'
type: issue
status: closed
closed_at: '2021-04-29T12:55:03+00:00'
---

# Original Description
Compiling works, tested on an Ubuntu x64 VM, executing in the same VM still works, then when the program is executed on another laptop I get the error ./xmrig:  /lib/x86_64-linux-gnu/libm.so.6: version `GLIBC_2.29' not found


**To Reproduce**
Compile on an Ubuntu VM, start the compiled file on another physical linux device.

**Expected behavior**
Miner starts mining.




# Discussion History
## SChernykh | 2021-04-29T08:22:45+00:00
I don't know what you really expect... If you compiled it with newer GLIBC and tried to run on a system with older GLIBC, of course it won't run. Compile it again on that system.

## 03lenio | 2021-04-29T12:55:03+00:00
> I don't know what you really expect... If you compiled it with newer GLIBC and tried to run on a system with older GLIBC, of course it won't run. Compile it again on that system.

Yes, excuse me, I was a bit too tired when I opened this issue. I identified the issue on my own and my project works now

# Action History
- Created by: 03lenio | 2021-04-28T23:55:07+00:00
- Closed at: 2021-04-29T12:55:03+00:00
