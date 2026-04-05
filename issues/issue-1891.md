---
title: cannot set MSR 0x000001a4 to 0x0000000f
source_url: https://github.com/xmrig/xmrig/issues/1891
author: dangfuyidabai
assignees: []
labels: []
created_at: '2020-10-13T11:11:44+00:00'
updated_at: '2023-08-05T13:02:47+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:46:35+00:00'
---

# Original Description
When I ran the command, xmrig starts mining. But I am receiving that message with yellow line.

cannot set MSR 0x000001a4 to 0x0000000f


MSR Tools has been automatically installed.  I put in all necessary wrmrs combinations for  CPU from randomx_boost.

# Discussion History
## dangfuyidabai | 2020-10-13T11:16:14+00:00

![20201013191535](https://user-images.githubusercontent.com/52128945/95853768-8a2f4880-0d88-11eb-8396-cc4472cf0056.jpg)



## dangfuyidabai | 2020-10-13T11:23:45+00:00
![20201013192309](https://user-images.githubusercontent.com/52128945/95854469-9667d580-0d89-11eb-9cf1-2bc400c4431a.jpg)


## Saikatsaha1996 | 2020-10-13T11:35:37+00:00
Run xmrig 6.3.5 exe..
Don't start run application


## Saikatsaha1996 | 2020-10-13T11:38:32+00:00
> When I ran the command, xmrig starts mining. But I am receiving that message with yellow line.
> 
> cannot set MSR 0x000001a4 to 0x0000000f
> 
> 
> MSR Tools has been automatically installed.  I put in all necessary wrmrs combinations for  CPU from randomx_boost.

Don't start run command
Just start xmrig .exe

## dangfuyidabai | 2020-10-13T11:39:45+00:00
> > When I ran the command, xmrig starts mining. But I am receiving that message with yellow line.
> > cannot set MSR 0x000001a4 to 0x0000000f
> > MSR Tools has been automatically installed.  I put in all necessary wrmrs combinations for  CPU from randomx_boost.
> 
> Don't start run command
> Just start xmrig .exe

Under linux system

## Saikatsaha1996 | 2020-10-13T11:41:54+00:00
> > > When I ran the command, xmrig starts mining. But I am receiving that message with yellow line.
> > > cannot set MSR 0x000001a4 to 0x0000000f
> > > MSR Tools has been automatically installed.  I put in all necessary wrmrs combinations for  CPU from randomx_boost.
> > 
> > Don't start run command
> > Just start xmrig .exe
> 
> Under linux system

Give me all files screen shot..

## mesche | 2020-10-19T13:48:26+00:00
Unfortunately I get the same error with Version v6.4.0 on Intel Xeon

Result of `cat /proc/cpuinfo | grep "Intel"`

> vendor_id	: GenuineIntel
> model name	: Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz
> ...

## SChernykh | 2020-10-19T13:52:38+00:00
MSR requires root/administrator privileges. Run as `sudo ./xmrig`

## mesche | 2020-10-19T14:43:23+00:00
@SChernykh yes! But this is not the cause of the problem, because XMRig runs as root.

Result of `sudo wrmsr -a 0x1a4 0xf`
> wrmsr: CPU 0 cannot set MSR 0x000001a4 to 0x000000000000000f

The simple shell-script  "randomx_boost.sh" does not work for me.



## SChernykh | 2020-10-19T14:46:53+00:00
@mesche It also must be a dedicated server, not a VM. MSR mod works only on the real hardware.

## ShineSmile | 2020-11-11T06:59:07+00:00
```
➜  ~ sudo wrmsr -a 0x1a4 0xf
wrmsr: pwrite: Operation not permitted
```

I solved it by disabling Security Boot in BIOS.
https://xmrig.com/docs/miner/randomx-optimization-guide/msr
https://stackoverflow.com/questions/44362796/wrmsr-operation-not-permitted-exception

## dnandz | 2021-01-05T16:17:24+00:00

![Screenshot from 2021-01-05 23-23-05](https://user-images.githubusercontent.com/26770640/103671168-22665380-4fad-11eb-8942-8e30b280a25e.png)
i am using ubuntu 18.04
in config.json
`"randomx": {
        "init": -1,
        "init-avx2": -1,
        "mode": "auto",
        "1gb-pages": true,
        "rdmsr": true,
        "wrmsr": "-a 0x1a4 0xf",
        "cache_qos": false,
        "numa": true,
        "scratchpad_prefetch_mode": 1
    },
`then save the text
go to terminal type sudo ./xmrig parameter 
xmrig need root permit to run config.json
sorry my english
![Screenshot from 2021-01-05 23-25-27](https://user-images.githubusercontent.com/26770640/103671320-56417900-4fad-11eb-94fd-4e90db293251.png)



## Shahnewaz1996 | 2021-02-09T19:23:05+00:00
Just a tip for people facing the same error on Windows: You need to disable "Memory Integrity" in Windows Security settings.
Windows Security -> Device Security -> Core isolation settings -> Turn Memory integrity off -> Restart.

I figured this out after the script from this [Reddit guide from u/sech1](https://www.reddit.com/r/MoneroMining/comments/e9tuvd/randomx_boost_guide_for_ryzen_on_windows_9100_hs/) output "no such msr" for all registers.

My setup works with Secure Boot enabled.

## ghost | 2021-02-09T21:29:23+00:00
The dev branch should have fixed this problem

## Avnsx | 2021-02-25T05:25:22+00:00
Same thing for me too

## SChernykh | 2021-02-25T07:22:56+00:00
@Avnsx Did you read the messages and try the listed solutions?

## Avnsx | 2021-02-26T18:43:39+00:00
> @Avnsx Did you read the messages and try the listed solutions?

Yes didn't work for me at all, but I guess it's because I'm running on a VM @SChernykh  is there maybe any kind of bypass or anything for that

## Koesters | 2021-03-02T04:17:29+00:00
on some Atom prefetch is not accessible and seemingly  N3050 too. Safe boot is disabled and all run as sudo.

see;
https://stackoverflow.com/questions/36608310/how-to-disable-prefetcher-in-atom-n270-processor

sudo ./boost.sh 

Detected Intel
wrmsr: CPU 0 cannot set MSR 0x000001a4 to 0x000000000000000f
MSR register values for Intel applied
sudo lsmod | grep msr
msr                    16384  0

cat /proc/cpuinfo
processor	: 0
vendor_id	: GenuineIntel
cpu family	: 6
model		: 76
model name	: Intel(R) Celeron(R) CPU  N3050  @ 1.60GHz
stepping	: 3
microcode	: 0x368
cpu MHz		: 950.625
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
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 cx16 xtpr pdcm sse4_1 sse4_2 movbe popcnt tsc_deadline_timer aes rdrand lahf_lm 3dnowprefetch epb ibrs ibpb stibp kaiser tpr_shadow vnmi flexpriority ept vpid tsc_adjust smep erms dtherm ida arat md_clear
bugs		: cpu_meltdown spectre_v1 spectre_v2 mds msbds_only
bogomips	: 3199.87
clflush size	: 64
cache_alignment	: 64
address sizes	: 36 bits physical, 48 bits virtual
power management:

processor	: 1
vendor_id	: GenuineIntel
cpu family	: 6
model		: 76
model name	: Intel(R) Celeron(R) CPU  N3050  @ 1.60GHz
stepping	: 3
microcode	: 0x368
cpu MHz		: 1370.937
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
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 cx16 xtpr pdcm sse4_1 sse4_2 movbe popcnt tsc_deadline_timer aes rdrand lahf_lm 3dnowprefetch epb ibrs ibpb stibp kaiser tpr_shadow vnmi flexpriority ept vpid tsc_adjust smep erms dtherm ida arat md_clear
bugs		: cpu_meltdown spectre_v1 spectre_v2 mds msbds_only
bogomips	: 3199.87
clflush size	: 64
cache_alignment	: 64
address sizes	: 36 bits physical, 48 bits virtual
power management:
`
This is just for info.


## revdeluxe | 2021-11-12T18:14:33+00:00
> on some Atom prefetch is not accessible and seemingly N3050 too. Safe boot is disabled and all run as sudo.
> 
> see; https://stackoverflow.com/questions/36608310/how-to-disable-prefetcher-in-atom-n270-processor
> 
> sudo ./boost.sh
> 
> Detected Intel wrmsr: CPU 0 cannot set MSR 0x000001a4 to 0x000000000000000f MSR register values for Intel applied sudo lsmod | grep msr msr 16384 0
> 
> cat /proc/cpuinfo processor : 0 vendor_id : GenuineIntel cpu family : 6 model : 76 model name : Intel(R) Celeron(R) CPU N3050 @ 1.60GHz stepping : 3 microcode : 0x368 cpu MHz : 950.625 cache size : 1024 KB physical id : 0 siblings : 2 core id : 0 cpu cores : 2 apicid : 0 initial apicid : 0 fpu : yes fpu_exception : yes cpuid level : 11 wp : yes flags : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 cx16 xtpr pdcm sse4_1 sse4_2 movbe popcnt tsc_deadline_timer aes rdrand lahf_lm 3dnowprefetch epb ibrs ibpb stibp kaiser tpr_shadow vnmi flexpriority ept vpid tsc_adjust smep erms dtherm ida arat md_clear bugs : cpu_meltdown spectre_v1 spectre_v2 mds msbds_only bogomips : 3199.87 clflush size : 64 cache_alignment : 64 address sizes : 36 bits physical, 48 bits virtual power management:
> 
> processor : 1 vendor_id : GenuineIntel cpu family : 6 model : 76 model name : Intel(R) Celeron(R) CPU N3050 @ 1.60GHz stepping : 3 microcode : 0x368 cpu MHz : 1370.937 cache size : 1024 KB physical id : 0 siblings : 2 core id : 2 cpu cores : 2 apicid : 4 initial apicid : 4 fpu : yes fpu_exception : yes cpuid level : 11 wp : yes flags : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 cx16 xtpr pdcm sse4_1 sse4_2 movbe popcnt tsc_deadline_timer aes rdrand lahf_lm 3dnowprefetch epb ibrs ibpb stibp kaiser tpr_shadow vnmi flexpriority ept vpid tsc_adjust smep erms dtherm ida arat md_clear bugs : cpu_meltdown spectre_v1 spectre_v2 mds msbds_only bogomips : 3199.87 clflush size : 64 cache_alignment : 64 address sizes : 36 bits physical, 48 bits virtual power management: ` This is just for info.

IDK why i find this funny 
what a coincidence
`processor	: 0
vendor_id	: GenuineIntel
cpu family	: 6
model		: 76
model name	: Intel(R) Celeron(R) CPU  N3060  @ 1.60GHz
stepping	: 4
microcode	: 0x411
cpu MHz		: 1146.036
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
cpu MHz		: 480.000
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
`



## GVCrypto | 2022-11-24T17:04:04+00:00
> Just a tip for people facing the same error on Windows: You need to disable "Memory Integrity" in Windows Security settings. Windows Security -> Device Security -> Core isolation settings -> Turn Memory integrity off -> Restart.
> 
> I figured this out after the script from this [Reddit guide from u/sech1](https://www.reddit.com/r/MoneroMining/comments/e9tuvd/randomx_boost_guide_for_ryzen_on_windows_9100_hs/) output "no such msr" for all registers.
> 
> My setup works with Secure Boot enabled.

correct 

## Tronixxx88 | 2023-07-16T16:07:11+00:00
> > > > Cuando ejecuta el comando, xmrig comienza un minar. Pero estoy recibiendo ese mensaje con línea amarilla. 
> > > > no se puede configurar MSR 0x000001a4 a 0x0000000f 
> > > > MSR Tools se instaló automáticamente. Utilice todas las combinaciones de wrmrs necesarias para la CPU de randomx_boost.
> > > 
> > > 
> > > No iniciar el comando de ejecución 
> > > Simplemente iniciar xmrig .exe
> > 
> > 
> > sistema bajo linux
> 
> Dame todos los archivos captura de pantalla ..

Puedes ayudarme un poco?

## srujan-singh | 2023-07-28T14:05:11+00:00
> 
> ![20201013191535](https://user-images.githubusercontent.com/52128945/95853768-8a2f4880-0d88-11eb-8396-cc4472cf0056.jpg)
> 
> 
I too faced the exact same problem in my windows 11 laptop, just follow the below mentioned steps: 

If using windows just turn off Memory integrity. You can do it by

1. Win + s --> search for Windows Security.

2. On the Windows Security Home page, Click on Device security.

3. Under Core isolaton, you'll find Memory integrity --> toggle that to Off.

4. Restart your computer and start mining, this'll fix the problem.

## dustybookshelf | 2023-08-05T11:33:54+00:00
Thanks I have with this value and working Preset has been set successfully,

wrmsr:"-a 0xc001102b 0x2000cc14"  and or leave it the value wrmsr: true,

![image](https://github.com/xmrig/xmrig/assets/34599947/81fec7fd-5f99-489d-92e7-38e929797c7f)

![image](https://github.com/xmrig/xmrig/assets/34599947/8558959f-8730-4d29-bf2c-2e40998724e3)

![image](https://github.com/xmrig/xmrig/assets/34599947/8d961401-a0df-4749-a2e3-83627082059a)
![image](https://github.com/xmrig/xmrig/assets/34599947/855dc69a-3c9f-4c8e-9c16-0e01d7548b88)
Clicking xmrig.exe properties and check RunThis Program as administrator so the next step is restarting your computer and run your xmrrig.exe

for donatioan XMR :  85uL3HjUmn5K2hNFWygtaggEGDnQVeyQjVNeLdtBQbdhefPce3jdsvVZtYVhRmD1gfWtY21MrKzxhXT4R2qKp5u2HmAJYDE

Happy Mining :)




# Action History
- Created by: dangfuyidabai | 2020-10-13T11:11:44+00:00
- Closed at: 2021-04-12T14:46:35+00:00
