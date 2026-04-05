---
title: XMRIG ram issues
source_url: https://github.com/xmrig/xmrig/issues/2690
author: revdeluxe
assignees: []
labels: []
created_at: '2021-11-13T06:14:54+00:00'
updated_at: '2021-11-14T16:41:11+00:00'
type: issue
status: closed
closed_at: '2021-11-14T16:41:11+00:00'
---

# Original Description
Basically I was mining the whole night and when i check my computer, it hang i think that went on for 5 hours

when i didn't my bench it's fine no problem but when i started mining XMRIG suddenly usses 2330MB of ram +256MB for unknown reasons

It should cleared my ram when i CTRL+C but takes to long to do so.
restarting might have broke it?

Mining Log - *Good thing i still have 10% of my ram left* i wont be able to use randomX though
![Screenshot from 2021-11-13 14-05-52](https://user-images.githubusercontent.com/38414584/141608187-b8f7497e-e538-4200-a3d5-e7f80e0df4ff.png)
here are the pics.
![Screenshot from 2021-11-13 14-05-11](https://user-images.githubusercontent.com/38414584/141608205-5b6f492e-046f-4076-91d7-9b3b605871ca.png)
im kinda anxious running xmrig again. so yeah.
_*SEND HELP*_

**EDIT**
when i relaunch xmrig it's kinda fast...
from 60H/s it became 170H/s
although it made my computer useless on other tasks like
Watching Youtube, facebook/messenger, videocalls

I wanted to allocate and de-allocate RandomX freely

Im Using Kali Linux 9

└─$ cat /proc/cpuinfo               
processor	: 0
vendor_id	: GenuineIntel
cpu family	: 6
model		: 76
model name	: Intel(R) Celeron(R) CPU  N3060  @ 1.60GHz
stepping	: 4
microcode	: 0x411
cpu MHz		: 1200.686
cache size	: 1024 KB
physical id	: 0
siblings	: 2
core id		: 0
cpu cores	: 2
apicid		: 0
initial apicid	: 0
fpu		: yes
fpu_exception	: yes
cpuid level	: 11
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology tsc_reliable nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 cx16 xtpr pdcm sse4_1 sse4_2 movbe popcnt tsc_deadline_timer aes rdrand lahf_lm 3dnowprefetch epb pti ibrs ibpb stibp tpr_shadow vnmi flexpriority ept vpid tsc_adjust smep erms dtherm ida arat md_clear
vmx flags	: vnmi preemption_timer invvpid ept_x_only flexpriority tsc_offset vtpr mtf vapic ept vpid unrestricted_guest
bugs		: cpu_meltdown spectre_v1 spectre_v2 mds msbds_only
bogomips	: 3200.00
clflush size	: 64
cache_alignment	: 64
address sizes	: 36 bits physical, 48 bits virtual
power management:

processor	: 1
vendor_id	: GenuineIntel
cpu family	: 6
model		: 76
model name	: Intel(R) Celeron(R) CPU  N3060  @ 1.60GHz
stepping	: 4
microcode	: 0x411
cpu MHz		: 1499.781
cache size	: 1024 KB
physical id	: 0
siblings	: 2
core id		: 2
cpu cores	: 2
apicid		: 4
initial apicid	: 4
fpu		: yes
fpu_exception	: yes
cpuid level	: 11
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology tsc_reliable nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 cx16 xtpr pdcm sse4_1 sse4_2 movbe popcnt tsc_deadline_timer aes rdrand lahf_lm 3dnowprefetch epb pti ibrs ibpb stibp tpr_shadow vnmi flexpriority ept vpid tsc_adjust smep erms dtherm ida arat md_clear
vmx flags	: vnmi preemption_timer invvpid ept_x_only flexpriority tsc_offset vtpr mtf vapic ept vpid unrestricted_guest
bugs		: cpu_meltdown spectre_v1 spectre_v2 mds msbds_only
bogomips	: 3200.00
clflush size	: 64
cache_alignment	: 64
address sizes	: 36 bits physical, 48 bits virtual
power management:



# Discussion History
## revdeluxe | 2021-11-14T16:41:11+00:00
Alternative Fix: FORMAT/CHANGE OS `Kali` to `Linux Mint`

my case is software not hardware...
also i tried removing HUGEPAGE but still didn't work...

Feel free to leave a comment if someone have this issue

# Action History
- Created by: revdeluxe | 2021-11-13T06:14:54+00:00
- Closed at: 2021-11-14T16:41:11+00:00
