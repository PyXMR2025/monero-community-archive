---
title: Returning MSR to Default value
source_url: https://github.com/xmrig/xmrig/issues/1419
author: cmlau
assignees: []
labels:
- enhancement
created_at: '2019-12-15T10:29:02+00:00'
updated_at: '2019-12-21T19:18:39+00:00'
type: issue
status: closed
closed_at: '2019-12-21T19:18:39+00:00'
---

# Original Description
Will the MSR setting return to default value after xmrig is stopped in Windows OS?? If not, any way to do this without rebooting Windows?

For Linux, can I just use "modprobe -r msr" to return to default value  or do I need to set another value other than "6" (i.e. wrmsr -a 0x1a4 _X_) to return it to default ?

Thanks.

# Discussion History
## xmrig | 2019-12-15T10:49:41+00:00
It not implemented right now, for revert to default values need save it first and apply them back on exit.
Module is just interface to MSR registers, you need set another value to revert it back, read current value by `sudo rdmsr 0x1a4` usually it `0` or `3` and write it back `sudo wrmsr -a 0x1a4 0`.

Please note for Ryzen value of 4 registers changed https://github.com/xmrig/xmrig/blob/master/scripts/randomx_boost.sh

## xmrig | 2019-12-17T11:43:00+00:00
Implemented in dev branch, the miner will restore initial values on exit by default, it controlled by new option `rdmsr`.
In case If something bad happen, eg the miner crashed, you still need to reboot to restore default values.
Thank you.

## j1warren | 2019-12-17T22:22:24+00:00
would be nice to have this in script, too
save original values in file via rdmsr, and have an option to restore them

## xmrig | 2019-12-21T19:18:39+00:00
https://github.com/xmrig/xmrig/releases/tag/v5.4.0

# Action History
- Created by: cmlau | 2019-12-15T10:29:02+00:00
- Closed at: 2019-12-21T19:18:39+00:00
