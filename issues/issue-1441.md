---
title: 'Miner halts with "cpu: stopped" in the log'
source_url: https://github.com/xmrig/xmrig/issues/1441
author: peepay
assignees: []
labels: []
created_at: '2019-12-18T08:57:00+00:00'
updated_at: '2021-04-12T15:08:19+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:08:19+00:00'
---

# Original Description
**Describe the bug**
Ever since upgrading to version 5, the msvc miner hangs after a day or two. The process xmrig.exe is still running in the task manager, but no mining is being done, the last log entry says "cpu: stopped" and it can't be closed by Ctrl+C, I need to manually kill the process in the task manager. When I run it again, it will again run for a day or two and the same situation repeats. The system is responsive, it does not freeze.

**To Reproduce**
Keep xmrig.exe running for a day or two, it will hang.

**Expected behavior**
The miner should not hang, it should work indefinitely.

**Required data**
 - the only log entry that is out of the ordinary is "cpu: stopped"
 - OS: Windows 10 1903
 - Intel i7-7700 3.6GHz; Intel HD Graphics 630
 - default config file, only changes are:
   - opencl - enabled - true
   - opencl - platform - intel
   - donate level - 1
   - pool url and user


# Discussion History
## dedizones | 2019-12-18T14:59:05+00:00
try in config.json

> "yield": true,

>  "opencl": {
>         "enabled": false,

https://github.com/xmrig/xmrig/blob/master/src/config.json

on the other hand you put opencl in true but on an intel card?

opencl = AMD
cuda = NVIDIA

## peepay | 2019-12-18T15:28:23+00:00
I may try the yield option - but based on what I read about it in the documentation, shouldn't it rather be set to false?

As for the OpenCL, it is an integrated card and according to https://en.wikipedia.org/wiki/Intel_Graphics_Technology#Capabilities it has OpenCL support. Also when xmrig starts, the gpu name is shown in green, with the text "Intel (R) OpenCL / OpenCL 2.1" above it. Should I configure it differently? (Now that I think of it, it is true I only get confirmed jobs from the CPU, but I thought that was just a thing of the output, now that one miner can mine on both CPU and GPU.)

## dedizones | 2019-12-19T07:23:51+00:00
If take charge to see, you launch xmrig and after 5 minutes you press "H" to display the hashrate.

the option on false according to what I read will make it more efficient but less stable, I had CPU crashes since I put on true it is very stable.

# Action History
- Created by: peepay | 2019-12-18T08:57:00+00:00
- Closed at: 2021-04-12T15:08:19+00:00
