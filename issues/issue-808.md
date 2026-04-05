---
title: 10% slowdown on Ryzen CPU at "rewrite memory allocation" commit (its a bit
  after 2.6.0-beta2)
source_url: https://github.com/xmrig/xmrig/issues/808
author: greynolds890
assignees: []
labels:
- bug
created_at: '2018-10-17T11:47:37+00:00'
updated_at: '2019-11-14T08:19:21+00:00'
type: issue
status: closed
closed_at: '2019-11-14T08:19:21+00:00'
---

# Original Description
I run xmrig on Ryzen7 2700 CPU.
Linux, 8 threads, one thread per core, of course.
gcc 8.1.1.
2.5.2 used to give me ~295h/s.
Now I upgrade to 2.8.1 (for imminent monero v8 support) and suddenly I get  only 550h/s.

I narrowed it down to these commits. If I "git reset --hard" to this commit:

commit 8716f362f893cd7a40c3000d6c1ef23bdb7b7208
Author: XMRig <support@xmrig.com>
Date:   Sun Apr 15 11:36:48 2018 +0700
    Fixed HW AES detection.

commit 9125b6c2512bb5539424894c766ef178ded93fbd
Author: XMRig <support@xmrig.com>
Date:   Sun Apr 15 11:08:47 2018 +0700
    Rewrite memory allocation.

I'm getting 550 h/s. If I reset to the previous one:

commit 4b71b7aa29e6ff89e20e8679625f4599edf75b40
Author: XMRig <support@xmrig.com>
Date:   Sat Apr 14 22:14:57 2018 +0700
    Added class MultiWorker and remove classes SingleWorker and DoubleWorker.

and then re-apply "Fixed HW AES detection" on top (as it's an obvious fix for an obvious goof in "Cpu::hasAES() ? AES_SOFT : AES_SOFT"), I get 590h/s.

The difference may be related to hugepages stopping being contiguous: pmap for 590h/s process shows just one hugepage mapping:

...
d4600000   18432K rw-p  /anon_hugepage
...

whereas after "Rewrite memory allocation" patch pmap shows separate single hugepages:

...
dbc00000    2048K rw-p  /anon_hugepage
dbe00000    2048K rw-p  /anon_hugepage
dc000000     132K rw-p    [ anon ]
...
e8021000   65404K ---p    [ anon ]
ec1ec000      44K r-xp  /usr/lib64/libnss_files-2.27.9000.so
ec1f7000    2044K ---p  /usr/lib64/libnss_files-2.27.9000.so
ec3f6000       4K r--p  /usr/lib64/libnss_files-2.27.9000.so
ec3f7000       4K rw-p  /usr/lib64/libnss_files-2.27.9000.so
ec3f8000      24K rw-p    [ anon ]
...
ecc00000    8192K rw-p    [ anon ]
ed400000    2048K rw-p  /anon_hugepage
ed7ff000       4K ---p    [ anon ]
ed800000    8192K rw-p    [ anon ]
ee000000    2048K rw-p  /anon_hugepage
ee3ff000       4K ---p    [ anon ]
ee400000    8192K rw-p    [ anon ]
eec00000    2048K rw-p  /anon_hugepage
eeffe000       4K ---p    [ anon ]
...
f4100000    1024K rw-p    [ anon ]
f4200000    2048K rw-p  /anon_hugepage
f4400000    2048K rw-p  /anon_hugepage
...

Maybe Ryzen somehow benefits on hardware level when hugepages are contiguous, or discontiguous ones may get aliased and cause spurious TLB evictions?

# Discussion History
## 2010phenix | 2018-10-18T11:31:28+00:00
confirm... when i test C++ v8, on few CPU, too look that in auto mode not correct mixing threads... even L3 huge miner try start with 6-8 core on CPU 24 core

## xmrig | 2019-10-08T03:24:37+00:00
Ability to use use continuous memory block reverted back https://github.com/xmrig/xmrig/blob/evo/doc/CPU.md#memory-pool-since-v430 mostly for Windows and macOS, but I can't confirm performance difference on modern algorithms.
Thank you.

# Action History
- Created by: greynolds890 | 2018-10-17T11:47:37+00:00
- Closed at: 2019-11-14T08:19:21+00:00
