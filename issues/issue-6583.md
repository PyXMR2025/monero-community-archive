---
title: Exception while synchronizing database
source_url: https://github.com/monero-project/monero/issues/6583
author: burghof
assignees: []
labels: []
created_at: '2020-05-23T07:43:47+00:00'
updated_at: '2020-05-30T17:21:39+00:00'
type: issue
status: closed
closed_at: '2020-05-30T17:21:39+00:00'
---

# Original Description
[bitmonero.log](https://github.com/monero-project/monero/files/4671366/bitmonero.log)
System:    Host: odroid Kernel: 4.9.219-72 aarch64 bits: 32 Console: tty 0
           Distro: Ubuntu 18.04.4 LTS
Machine:   No /sys/class/dmi; using dmidecode: no smbios data. Old system?
CPU:       6 core  (-MCP-)  (ARM)
           clock speeds: max: 1896 MHz 1: 1000 MHz 2: 1000 MHz 3: 1000 MHz
           4: 1000 MHz 5: 1000 MHz 6: 1000 MHz
Graphics:  Card: Failed to Detect Video Card!
           Display Server: N/A drivers: fbdev (unloaded: modesetting)
           tty size: 80x24 Advanced Data: N/A out of X
Audio:     Card AML-AUGESOUND driver: AML-AUGESOUND
           Sound: Advanced Linux Sound Architecture v: k4.9.219-72
Network:   Card: Failed to Detect Network Card!
Drives:    HDD Total Size: NA (-)
           ID-1: /dev/mmcblk1 model: N/A size: 127.9GB
Partition: ID-1: / size: 117G used: 14G (12%) fs: ext4 dev: /dev/mmcblk1p2
Sensors:   None detected - is lm-sensors installed and configured?
Info:      Processes: 171 Uptime: 28 min Memory: 261.8/3712.2MB
           Init: systemd runlevel: 5 Client: Shell (bash) inxi: 2.3.56

# Discussion History
## moneromooo-monero | 2020-05-23T11:01:48+00:00
That looks like some networking error, but the first monerod looks like it might have hanged. If it's still running, you can get an all thread stack trace?

gdb /path/to/monerod \`pidof monerod\`
thread apply all bt

And paste the (multi page) output here.

## burghof | 2020-05-24T07:14:33+00:00
It's difficult to debug because the terminal session aborts, when the error occurs. I restricted the process to a single processor core, and now it seems to work.

## moneromooo-monero | 2020-05-24T11:13:01+00:00
Do you have really strict system resource limits ? A system error could well be "resource unavailable" or the like, and would fit well with "the terminal session aborts".

## burghof | 2020-05-30T14:51:38+00:00
Seems stable now, but I am still seeing a lot of exceptions.
[bitmonero.log.zip](https://github.com/monero-project/monero/files/4705814/bitmonero.log.zip)



## moneromooo-monero | 2020-05-30T15:14:57+00:00
Wrong log I think.

## burghof | 2020-05-30T15:21:05+00:00
It may be a bit long, but if you scroll to the end of the file you will see many exceptions of this type:
2020-05-30 14:46:56.555	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::runtime_error
2020-05-30 14:46:56.555	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2020-05-30 14:46:56.563	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0xf8) [0x55581b8b60]:__cxa_throw+0xf8) [0x55581b8b60]
2020-05-30 14:46:56.563	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2]  0x70) [0x55582f03d0]:_Z21allocLargePagesMemorym+0x70) [0x55582f03d0]
2020-05-30 14:46:56.563	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3]  0x44) [0x55582eabe4]:_ZN7randomx6VmBaseINS_18LargePageAllocatorELb0EE8allocateEv+0x44) [0x55582eabe4]
2020-05-30 14:46:56.563	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4]  0x114) [0x55582e853c]:_create_vm+0x114) [0x55582e853c]
2020-05-30 14:46:56.563	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5]  0x3a0) [0x5558187278]:_slow_hash+0x3a0) [0x5558187278]
2020-05-30 14:46:56.563	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	


## moneromooo-monero | 2020-05-30T17:13:20+00:00
Those are expected. What is the actual problem ?

## burghof | 2020-05-30T17:21:39+00:00
If they are expected, then no problem on my side.

# Action History
- Created by: burghof | 2020-05-23T07:43:47+00:00
- Closed at: 2020-05-30T17:21:39+00:00
