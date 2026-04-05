---
title: 'Assertion failed: 0, file src/win/stream.c, line 85'
source_url: https://github.com/xmrig/xmrig/issues/2376
author: tla2k12
assignees: []
labels: []
created_at: '2021-05-14T20:53:28+00:00'
updated_at: '2021-05-14T21:03:34+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**
Start xmrig with:
~/xmrig/build/xmrig.exe -o pool.minexmr.com:443 -u yy -k --tls --rig-id xx
returns:
Assertion failed: 0, file src/win/stream.c, line 85

**To Reproduce**
Every time started.

**Expected behavior**
No error, xmrig to continue running.

**Required data**
As above. Weirdly (well not really as this perhaps looks like a streams library error?) adding a "--log-file=<path>" option allows xmrig to start normally and output to the stdout and log file.
Command line as above.
Windows 10 Home 20H2
No GPU mining

**Additional context**
Adding a "--log-file=<path>" option allows xmrig to start normally.
Previous versions worked fine and this appeared to break after a Windows update.
Built under msys2 with gcc 10.3.0
Tried updating msys, msys dependencies, gcc, git, cmake -> no change
Tried rebuilding using latest master branch head -> no change

# ~/xmrig/build/xmrig.exe --version
XMRig 6.12.1
 built on May 14 2021 with GCC 10.3.0
 features: 64-bit AES

libuv/1.41.0
OpenSSL/1.1.1j
hwloc/2.4.1

# Discussion History
## SChernykh | 2021-05-14T21:03:34+00:00
Don't start xmrig under msys, start it under regular Windows command line.

# Action History
- Created by: tla2k12 | 2021-05-14T20:53:28+00:00
