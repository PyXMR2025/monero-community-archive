---
title: --config option is weird.
source_url: https://github.com/xmrig/xmrig/issues/679
author: baryluk
assignees: []
labels: []
created_at: '2018-06-06T21:17:07+00:00'
updated_at: '2018-06-07T00:31:34+00:00'
type: issue
status: closed
closed_at: '2018-06-07T00:31:34+00:00'
---

# Original Description
```text
$ ls -lh
total 990K
-rw-r--r-- 1 baryluk baryluk 2.3K Jun  6 23:11 config-electroneum.json
-rw-r--r-- 1 baryluk baryluk 2.6K Jun  6 22:56 config-monero.json
-rw-r--r-- 1 baryluk baryluk  810 Jun  6 21:13 config-original.json
-rwxr-xr-x 1 baryluk baryluk 1.9M May  6 21:30 xmrig
$

$ strace -e trace=openat ./xmrig -c config-electroneum.json 
openat(AT_FDCWD, "/etc/ld.so.preload", O_RDONLY|O_CLOEXEC) = 3
openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libpthread.so.0", O_RDONLY|O_CLOEXEC) = 3
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/librt.so.1", O_RDONLY|O_CLOEXEC) = 3
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
openat(AT_FDCWD, "/sys/devices/system/cpu/online", O_RDONLY|O_CLOEXEC) = 3
openat(AT_FDCWD, "config-electroneum.json", O_RDONLY|O_CLOEXEC) = 9
openat(AT_FDCWD, "/home/baryluk/Linux/xmrig/xmrig-2.6.2/config.json", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
unable to open /home/baryluk/Linux/xmrig/xmrig-2.6.2/config.json: no such file or directory
No valid configuration found. Exiting.
+++ exited with 2 +++
```

xmrig-2.6.2

Why it is still trying to open config.json, with an absolute path ? I did provide all options in config-electroneum.json 

# Discussion History
## baryluk | 2018-06-06T21:20:57+00:00
So, I think this is because `xmrig` had problem parsing my `config-electroneum.json` file, and fallback to try use `config.json`. That is wrong. It should report the problem instead.

There was no JSON syntax error (configured by manually parsing file in Chrome console), but I specified pool url that xmrig couldn't parse (`stratum+ssl://xyz.cc:13433`).


## xmrig | 2018-06-07T00:31:33+00:00
Merge this issue with #680

# Action History
- Created by: baryluk | 2018-06-06T21:17:07+00:00
- Closed at: 2018-06-07T00:31:34+00:00
