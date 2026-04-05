---
title: Not shown health status for all GPU card, just zeroes.
source_url: https://github.com/xmrig/xmrig/issues/2066
author: minzak
assignees: []
labels:
- bug
created_at: '2021-01-28T13:17:43+00:00'
updated_at: '2021-04-12T14:18:49+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:18:49+00:00'
---

# Original Description
I use RVM for mining on 10 GPU,
And health status, not show detail for all cards, but when I use in a parallel way to check it - all is fine.

```
[2021-01-28 15:10:16.306]  opencl   #0 03:00.0  94W 55C 1904RPM 1080/2040MHz
[2021-01-28 15:10:16.306]  opencl   #1 07:00.0  93W 56C 1963RPM 1080/2040MHz
[2021-01-28 15:10:16.307]  opencl   #2 09:00.0  92W 54C 1923RPM 1100/2080MHz
[2021-01-28 15:10:16.307]  opencl   #3 0a:00.0  95W 53C 1913RPM 1100/2080MHz
[2021-01-28 15:10:16.307]  opencl   #4 0b:00.0  93W 53C 1937RPM 1100/2080MHz
[2021-01-28 15:10:16.307]  opencl   #5 0c:00.0  94W 52C 1950RPM 1100/2080MHz
[2021-01-28 15:10:16.307]  opencl   #6 0d:00.0   0W  0C    0RPM 0/0MHz
[2021-01-28 15:10:16.307]  opencl   #7 0e:00.0   0W  0C    0RPM 0/0MHz
[2021-01-28 15:10:16.307]  opencl   #8 0f:00.0   0W  0C    0RPM 0/0MHz
[2021-01-28 15:10:16.307]  opencl   #9 10:00.0   0W  0C    0RPM 0/0MHz
```
![Screenshot_20210128_145917](https://user-images.githubusercontent.com/12154217/106143297-41ef3700-617b-11eb-9aac-bf809ea092b7.png)

Both method is worked for getting GPU details:

`cat /sys/kernel/debug/dri/*/amdgpu_pm_info | grep -i Temperature | cat -n`
and 
```
/opt/ohgodatool -i 1 --show-temp
/opt/ohgodatool -i 2 --show-temp
...
/opt/ohgodatool -i 9 --show-temp
/opt/ohgodatool -i 10 --show-temp
```

And at the start all was fine:
```
 * ADL          press e for health report
 * OPENCL       #0 AMD Accelerated Parallel Processing/OpenCL 2.1 AMD-APP (3143.9)
 * OPENCL GPU   #0 03:00.0 Radeon RX 580 Series (Ellesmere) 1411 MHz cu:36 mem:3839/4090 MB
 * OPENCL GPU   #1 07:00.0 Radeon RX 580 Series (Ellesmere) 1411 MHz cu:36 mem:3839/4090 MB
 * OPENCL GPU   #2 09:00.0 Radeon RX 580 Series (Ellesmere) 1411 MHz cu:36 mem:3839/4090 MB
 * OPENCL GPU   #3 0a:00.0 Radeon RX 580 Series (Ellesmere) 1411 MHz cu:36 mem:3839/4090 MB
 * OPENCL GPU   #4 0b:00.0 Radeon RX 580 Series (Ellesmere) 1411 MHz cu:36 mem:3839/4090 MB
 * OPENCL GPU   #5 0c:00.0 Radeon RX 580 Series (Ellesmere) 1411 MHz cu:36 mem:3839/4090 MB
 * OPENCL GPU   #6 0d:00.0 Radeon RX 580 Series (Ellesmere) 1411 MHz cu:36 mem:3839/4090 MB
 * OPENCL GPU   #7 0e:00.0 Radeon RX 580 Series (Ellesmere) 1411 MHz cu:36 mem:3839/4090 MB
 * OPENCL GPU   #8 0f:00.0 Radeon RX 580 Series (Ellesmere) 1430 MHz cu:36 mem:7935/8186 MB
 * OPENCL GPU   #9 10:00.0 Radeon RX 580 Series (Ellesmere) 1430 MHz cu:36 mem:7935/8186 MB
[2021-01-28 14:51:58.938]  net      use pool stratum.ravenminer.com:3838  3.122.71.171
[2021-01-28 14:51:58.970]  net      new job from stratum.ravenminer.com:3838 diff 431M algo kawpow height 1601891
[2021-01-28 14:51:58.970]  opencl   use profile  kawpow  (10 threads) scratchpad 32 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 | 03:00.0 |   9437184 |   256 |   2770 | Radeon RX 580 Series (Ellesmere)
|  1 |   1 | 07:00.0 |   9437184 |   256 |   2770 | Radeon RX 580 Series (Ellesmere)
|  2 |   2 | 09:00.0 |   9437184 |   256 |   2770 | Radeon RX 580 Series (Ellesmere)
|  3 |   3 | 0a:00.0 |   9437184 |   256 |   2770 | Radeon RX 580 Series (Ellesmere)
|  4 |   4 | 0b:00.0 |   9437184 |   256 |   2770 | Radeon RX 580 Series (Ellesmere)
|  5 |   5 | 0c:00.0 |   9437184 |   256 |   2770 | Radeon RX 580 Series (Ellesmere)
|  6 |   6 | 0d:00.0 |   9437184 |   256 |   2770 | Radeon RX 580 Series (Ellesmere)
|  7 |   7 | 0e:00.0 |   9437184 |   256 |   2770 | Radeon RX 580 Series (Ellesmere)
|  8 |   8 | 0f:00.0 |   9437184 |   256 |   2770 | Radeon RX 580 Series (Ellesmere)
|  9 |   9 | 10:00.0 |   9437184 |   256 |   2770 | Radeon RX 580 Series (Ellesmere)
[2021-01-28 14:51:59.149]  opencl   GPU #9 compiling...
[2021-01-28 14:51:59.322]  opencl   GPU #9 compilation completed (173 ms)
[2021-01-28 14:52:00.022]  opencl   READY threads 10/10 (1051 ms)
[2021-01-28 14:52:00.335]  opencl   KawPow program for period 533963 compiled (314ms)
```

What is wrong?

# Discussion History
## xmrig | 2021-01-28T14:02:12+00:00
Reading code located here https://github.com/xmrig/xmrig/blob/master/src/backend/opencl/wrappers/AdlLib_linux.cpp

Can you please check content of:
* `/sys/bus/pci/drivers/amdgpu/0000:0d:00.0/hwmon/*`
* `/sys/bus/pci/drivers/amdgpu/0000:0e:00.0/hwmon/*`
* `/sys/bus/pci/drivers/amdgpu/0000:0f:00.0/hwmon/*`
* `/sys/bus/pci/drivers/amdgpu/0000:10:00.0/hwmon/*`

## minzak | 2021-01-28T17:48:36+00:00
Hm, very strange.
All fine and worked:
```
cat /sys/bus/pci/drivers/amdgpu/*/hwmon/*/freq1_input
echo
cat /sys/bus/pci/drivers/amdgpu/*/hwmon/*/power1_average
echo
cat /sys/bus/pci/drivers/amdgpu/*/hwmon/*/fan1_input
```
and result is:
```

1016320000
995080000
1025860000
1001350000
970090000
990790000
999510000
1028060000
983940000
1014220000

120036000
118056000
119201000
118228000
118112000
117254000
119160000
121126000
119057000
118206000

2110
2175
2136
2105
2140
2140
1999
2208
2082
1744
```

Also all needed dirs and filer are present and readable:

```
root@ferma /sys/bus/pci/drivers/amdgpu/0000:10:00.0/hwmon/hwmon13 # ls -la
total 0
drwxr-xr-x 3 root root    0 Jan 28  2021 .
drwxr-xr-x 3 root root    0 Jan 28  2021 ..
lrwxrwxrwx 1 root root    0 Jan 28 19:37 device -> ../../../0000:10:00.0
-rw-r--r-- 1 root root 4096 Jan 28 19:37 fan1_enable
-r--r--r-- 1 root root 4096 Jan 28 19:37 fan1_input
-r--r--r-- 1 root root 4096 Jan 28 19:37 fan1_max
-r--r--r-- 1 root root 4096 Jan 28 19:37 fan1_min
-rw-r--r-- 1 root root 4096 Jan 28 19:37 fan1_target
-r--r--r-- 1 root root 4096 Jan 28 19:37 freq1_input
-r--r--r-- 1 root root 4096 Jan 28 19:37 freq1_label
-r--r--r-- 1 root root 4096 Jan 28 19:37 freq2_input
-r--r--r-- 1 root root 4096 Jan 28 19:37 freq2_label
-r--r--r-- 1 root root 4096 Jan 28 19:25 in0_input
-r--r--r-- 1 root root 4096 Jan 28 19:25 in0_label
-r--r--r-- 1 root root 4096 Jan 28 19:24 name
drwxr-xr-x 2 root root    0 Jan 28 19:37 power
-r--r--r-- 1 root root 4096 Jan 28 19:24 power1_average
-rw-r--r-- 1 root root 4096 Jan 28 19:25 power1_cap
-r--r--r-- 1 root root 4096 Jan 28 19:37 power1_cap_max
-r--r--r-- 1 root root 4096 Jan 28 19:37 power1_cap_min
-rw-r--r-- 1 root root 4096 Jan 28 19:26 pwm1
-rw-r--r-- 1 root root 4096 Jan 28 19:26 pwm1_enable
-r--r--r-- 1 root root 4096 Jan 28 19:24 pwm1_max
-r--r--r-- 1 root root 4096 Jan 28 19:25 pwm1_min
lrwxrwxrwx 1 root root    0 Jan 28 19:37 subsystem -> ../../../../../../class/hwmon
-r--r--r-- 1 root root 4096 Jan 28 19:25 temp1_crit
-r--r--r-- 1 root root 4096 Jan 28 19:37 temp1_crit_hyst
-r--r--r-- 1 root root 4096 Jan 28 19:23 temp1_input
-r--r--r-- 1 root root 4096 Jan 28 19:25 temp1_label
-rw-r--r-- 1 root root 4096 Jan 28  2021 uevent

```

## minzak | 2021-01-28T17:54:41+00:00
Hm, how about use lower reads, but from files - cat /sys/kernel/debug/dri/*/amdgpu_pm_info
here is all info, except fan

```
Clock Gating Flags Mask: 0x3fbcf
        Graphics Medium Grain Clock Gating: On
        Graphics Medium Grain memory Light Sleep: On
        Graphics Coarse Grain Clock Gating: On
        Graphics Coarse Grain memory Light Sleep: On
        Graphics Coarse Grain Tree Shader Clock Gating: Off
        Graphics Coarse Grain Tree Shader Light Sleep: Off
        Graphics Command Processor Light Sleep: On
        Graphics Run List Controller Light Sleep: On
        Graphics 3D Coarse Grain Clock Gating: Off
        Graphics 3D Coarse Grain memory Light Sleep: Off
        Memory Controller Light Sleep: On
        Memory Controller Medium Grain Clock Gating: On
        System Direct Memory Access Light Sleep: Off
        System Direct Memory Access Medium Grain Clock Gating: On
        Bus Interface Medium Grain Clock Gating: Off
        Bus Interface Light Sleep: On
        Unified Video Decoder Medium Grain Clock Gating: On
        Video Compression Engine Medium Grain Clock Gating: On
        Host Data Path Light Sleep: On
        Host Data Path Medium Grain Clock Gating: On
        Digital Right Management Medium Grain Clock Gating: Off
        Digital Right Management Light Sleep: Off
        Rom Medium Grain Clock Gating: On
        Data Fabric Medium Grain Clock Gating: Off
        Address Translation Hub Medium Grain Clock Gating: Off
        Address Translation Hub Light Sleep: Off

GFX Clocks and Power:
        2000 MHz (MCLK)
        984 MHz (SCLK)
        600 MHz (PSTATE_SCLK)
        1000 MHz (PSTATE_MCLK)
        1018 mV (VDDGFX)
        118.129 W (average GPU)

GPU Temperature: 60 C
GPU Load: 100 %
MEM Load: 85 %

UVD: Enabled

VCE: Enabled
```
Also many other tools can read HW data like amdcovc, ohgodatool

I also use this way:
```
for card in {1..10}; do
echo "Card $card:";
#cat /sys/kernel/debug/dri/$card/amdgpu_pm_info | grep -i " ("
cat /sys/kernel/debug/dri/$card/amdgpu_pm_info | sed -n -e 27,36p -e 38,39p
done
```

## xmrig | 2021-01-28T18:30:16+00:00
Fixed in dev branch, it quick fix, but solves the issue, later will be implemented proper fix.
Thank you.

# Action History
- Created by: minzak | 2021-01-28T13:17:43+00:00
- Closed at: 2021-04-12T14:18:49+00:00
