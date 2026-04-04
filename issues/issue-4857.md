---
title: Monerod stuck when syncing blockchain
source_url: https://github.com/monero-project/monero/issues/4857
author: Jasonhcwong
assignees: []
labels: []
created_at: '2018-11-16T00:08:33+00:00'
updated_at: '2018-11-29T09:39:15+00:00'
type: issue
status: closed
closed_at: '2018-11-29T09:39:15+00:00'
---

# Original Description
Monerod stuck when syncing blockchain, happened multiple times at different block height.

Arch: arm64
OS: Armbian 5.65, tried both Debian Stretch and Ubuntu Bionic, both get stuck
Version: 13.04, tried official binary files and self compiled, both get stuck
SBC: Rock64
CPU: Rockchip 3328
Blockchain Storage media: tried HDD, SSD and sdcard, all get stuck

Symptom:
Monerod get stuck at random block height. When getting stuck, monerod is still using 100% CPU out of 400% (4 cores), iostat shows that monerod keep writing data to storage at 4096 KB/s. Both dmesg and kernel log did not show anything strange. Run commands "monerod sync_info" and "monerod status" wait for a long time and then failed.


Error message:
```
jason@rock64:~$ monero-v0.13.0.4/monerod --config-file=/etc/monerod.conf sync_info
2018-11-15 23:56:46,753 INFO  [default] Page size: 4096
Error: Unsuccessful -- json_rpc_request: 
```

Log: (set_log 4 after getting stuck): https://pastebin.com/Qwwyy2m5

# Discussion History
## moneromooo-monero | 2018-11-16T00:15:59+00:00
Also post an all thread stack trace:
gdb/path/to/monerod \`pidof monerod\`
thread apply all bt


## Jasonhcwong | 2018-11-16T10:55:00+00:00
Here is the stack trace: https://pastebin.com/8d3CZJ28

## Jasonhcwong | 2018-11-19T18:04:04+00:00
The stack trace is strange. 
The stack of thread 12 is corrupted.
`
Thread 12 (Thread 0x7f9d5ff1d0 (LWP 27961)):
#0  0x00000055948ae930 in (anonymous namespace)::compare_hash32(MDB_val const*, MDB_val const*) ()
Backtrace stopped: previous frame identical to this frame (corrupt stack?)
`

I tried to debug by myself.
One of the thread in monerod is using 100% CPU.
I find out the thread ID with top command and attach gdb to the thread.
The thread is corrupted and is in the same function compare_hash32() as above stack trace above.
Any ideas ?

## moneromooo-monero | 2018-11-19T21:16:59+00:00
That looks like lmdb looking for records.

## Jasonhcwong | 2018-11-29T09:39:15+00:00
#4906 seems fixed this issue.

# Action History
- Created by: Jasonhcwong | 2018-11-16T00:08:33+00:00
- Closed at: 2018-11-29T09:39:15+00:00
