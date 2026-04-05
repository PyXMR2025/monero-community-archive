---
title: Wrong detect AES
source_url: https://github.com/xmrig/xmrig/issues/10
author: 2010phenix
assignees: []
labels: []
created_at: '2017-06-01T11:00:11+00:00'
updated_at: '2018-10-10T22:14:14+00:00'
type: issue
status: closed
closed_at: '2018-10-10T22:14:14+00:00'
---

# Original Description
First of all, Thx for your hard work with miner.

Second, found issue with wrong detecting AES-NI in CPU

Am using before other miner [source](https://github.com/JayDDee/cpuminer-opt)
no any problem with detect AES and good H\s [screen](https://prnt.sc/fem1k9)
xmrig wrong detecting AES CPU [screen](https://prnt.sc/fem1tz)

Not always have much free time, but ready if need some test or etc...


# Discussion History
## xmrig | 2017-06-01T11:32:02+00:00
You can force use AES-NI if add command line options `--av=1` or `--av=2` it disable all checks, so if app not crash after that AES-NI available.

CPU-Z in your screens also show AES not available, for example http://i.imgur.com/pAwwWgP.png

You can check version 0.6.0 https://github.com/xmrig/xmrig/releases/tag/v0.6.0
It uses different method to detect AES-NI

Thank you.

## xmrig | 2017-06-01T11:44:49+00:00
For 2 threads and 8 MB L3 better choice `--av=2`.

## 2010phenix | 2017-06-01T13:00:50+00:00
thx for suggestion....
Yes I know that not show AES in CPU-Z, but algo strange used for block AES optimization....

checking (not miner auto detect) but by hands add in config.... not detect but give some more H\s

--av2: give same result from 1 post
--av1:  better but not detect AES [screen](https://prnt.sc/feni61)
v 0.6.0: not detect at all [screen](https://prnt.sc/fenjs7)



## xmrig | 2017-06-01T13:26:59+00:00
If miner works with `--av=1` it's mean AES-NI supported and used (but strange --av=2 in your case should give better hashrate, for version 0.8.0+).

I looked again at the screenshots and saw that L2/L3 cache size also not detected. Please download and run cpuid_tool.exe from https://github.com/anrieff/libcpuid/releases

Then check report.txt if cache size not detected and/or aes, create issue there https://github.com/anrieff/libcpuid/issues

Or I can do it if you attach raw.txt and report.txt

## 2010phenix | 2017-06-01T20:23:22+00:00
cashe is 8MB and correct detect with cpuid_tool...

> CPUID is present
> CPU Info:
> ------------------
>   vendor_str : `GenuineIntel'
>   vendor id  : 0
>   brand_str  : `Intel(R) Xeon(R) CPU E3-1220 V2 @ 3.10GHz'
>   family     : 6 (06h)
>   model      : 10 (0Ah)
>   stepping   : 9 (09h)
>   ext_family : 6 (06h)
>   ext_model  : 58 (3Ah)
>   num_cores  : 8
>   num_logical: 8
>   tot_logical: 4
>   L1 D cache : 32 KB
>   L1 I cache : 32 KB
>   L2 cache   : 256 KB
>   L3 cache   : 8192 KB
>   L4 cache   : -1 KB
>   L1D assoc. : 8-way
>   L2 assoc.  : 8-way
>   L3 assoc.  : 16-way
>   L4 assoc.  : -1-way
>   L1D line sz: 64 bytes
>   L2 line sz : 64 bytes
>   L3 line sz : 64 bytes
>   L4 line sz : -1 bytes
>   SSE units  : 128 bits (non-authoritative)
>   code name  : `Ivy Bridge (Xeon)'
>   features   : fpu vme de pse tsc msr pae mce cx8 apic mtrr sep pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ss ht pni ssse3 cx16 sse4_1 sse4_2 syscall xd popcnt xsave osxsave avx lm lahf_lm
> 

if more specific this dedicated server work like VM, and maybe problem that xmrig not detect this things or not correct detect?

## xmrig | 2017-06-02T16:50:03+00:00
Virtual CPU this is a good explanation of why AES-NI detection does not work, and also `--av=2` slower.
I will add warning message, to suggest manually enable AES-NI algo variation.
Thank you.


## 2010phenix | 2017-06-03T16:45:29+00:00
maybe look on source(link in first post), that miner am using before... his algo-detect over VM and give Hashrate like simple computer with AES.

and thanks to you and your work.


## mercenaruss | 2018-01-20T14:09:03+00:00
@2010phenix you solve the problem?
I have the same one but on physical CPU not virtual,have lots of server and nowhere is working AES-NI 

# Action History
- Created by: 2010phenix | 2017-06-01T11:00:11+00:00
- Closed at: 2018-10-10T22:14:14+00:00
