---
title: AMD Epyc msr mod
source_url: https://github.com/xmrig/xmrig/issues/1685
author: geriweb
assignees: []
labels: []
created_at: '2020-05-21T07:43:59+00:00'
updated_at: '2020-08-19T01:20:05+00:00'
type: issue
status: closed
closed_at: '2020-08-19T01:20:05+00:00'
---

# Original Description
The msr mod settings are not working on amd epyc.
Can you fix it in the next release please?
Thank you

# Discussion History
## SChernykh | 2020-05-21T07:47:59+00:00
The MSR mod works on all AMD Zen series CPUs, including EPYC. Make sure you run xmrig as admin (if using Windows) or as root (Linux). You also need to have `msrtools` installed on Linux.

## Unnameless | 2020-05-21T15:05:17+00:00
Is there any other way to avoid running xmrig as root on Linux but still get pages and most mods?

## SChernykh | 2020-05-21T15:23:33+00:00
Yes, run https://github.com/xmrig/xmrig/blob/master/scripts/randomx_boost.sh as root before starting xmrig

## Unnameless | 2020-05-21T15:26:03+00:00
> Yes, run https://github.com/xmrig/xmrig/blob/master/scripts/randomx_boost.sh as root before starting xmrig

Thanks! 

## geriweb | 2020-05-21T17:12:18+00:00
[2020-05-21 17:03:09.546]  msr  cannot read MSR 0xc0011020
[2020-05-21 17:03:09.546]  msr  cannot read MSR 0xc001102b
[2020-05-21 17:03:09.546]  msr  cannot set MSR 0xc0011020 to 0x00000000


## geriweb | 2020-05-21T17:14:31+00:00
root@localhost:~# cat /proc/cpuinfo
processor	: 0
vendor_id	: AuthenticAMD
cpu family	: 23
model		: 1
model name	: AMD EPYC 7501 32-Core Processor


## geriweb | 2020-05-21T17:15:37+00:00
There is no "AMD Ryzen" in the cpuinfo file...

## SChernykh | 2020-05-21T17:18:04+00:00
@geriweb Did you install `msrtools` and run xmrig as root? If you prefer the randomx_boost script, you can change `AMD Ryzen` to `EPYC` and it will work.

## geriweb | 2020-05-21T17:26:29+00:00
Yes I installed, but it is not working:
wrmsr: CPU 0 cannot set MSR 0xc001102b to 0x000000001808cc16
wrmsr: CPU 0 cannot set MSR 0xc0011020 to 0x0000000000000000
wrmsr: CPU 0 cannot set MSR 0xc0011021 to 0x0000000000000040

:(


## SChernykh | 2020-05-21T17:27:18+00:00
Are you running in a VM? It works only on physical CPU.

## geriweb | 2020-05-21T17:29:58+00:00
VM

## TimoC1982 | 2020-07-20T12:33:37+00:00
Hi, well is there a way to work that for virtual enviroments?


## SChernykh | 2020-07-21T07:14:08+00:00
@TimoC1982 No, it's impossible in a VM. Writing to MSR registers can be used to get full access to the physical machine, so it would be a security vulnerability if it could be done in a VM.

# Action History
- Created by: geriweb | 2020-05-21T07:43:59+00:00
- Closed at: 2020-08-19T01:20:05+00:00
