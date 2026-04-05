---
title: Unsupported target. Must be either ARMv7-A+NEON or ARMv8-A.
source_url: https://github.com/xmrig/xmrig/issues/2348
author: royheuer
assignees: []
labels:
- bug
- arm
created_at: '2021-05-06T12:04:48+00:00'
updated_at: '2025-06-16T18:48:36+00:00'
type: issue
status: closed
closed_at: '2025-06-16T18:48:36+00:00'
---

# Original Description
I followed the guide on how to build on a Raspberry Pi 4.

https://github.com/pragathoys/build_xmrig_for_armv7

I ran:

cmake .. -DARM_TARGET=7
make

I get the output:

In file included from /home/pi/Mining/xmrig/src/crypto/cn/soft_aes.h:31,
                 from /home/pi/Mining/xmrig/src/crypto/cn/CryptoNight_arm.h:35,
                 from /home/pi/Mining/xmrig/src/crypto/cn/CnHash.cpp:35:
/home/pi/Mining/xmrig/src/crypto/cn/sse2neon.h:122:2: error: #error "Unsupported target. Must be either ARMv7-A+NEON or ARMv8-A."
 #error "Unsupported target. Must be either ARMv7-A+NEON or ARMv8-A."
  ^~~~~


# Discussion History
## royheuer | 2021-05-06T12:07:13+00:00
pi@raspberrypi:~/Mining/xmrig/build $ lscpu
Architecture:        armv7l
Byte Order:          Little Endian
CPU(s):              4
On-line CPU(s) list: 0-3
Thread(s) per core:  1
Core(s) per socket:  4
Socket(s):           1
Vendor ID:           ARM
Model:               3
Model name:          Cortex-A72
Stepping:            r0p3
CPU max MHz:         1500.0000
CPU min MHz:         600.0000
BogoMIPS:            108.00
Flags:               half thumb fastmult vfp edsp neon vfpv3 tls vfpv4 idiva idivt vfpd32 lpae evtstrm crc32


## Skilowi | 2021-05-06T13:50:17+00:00
Aint Raspi 4B aarch64? 

pi@RPivonSkilowi:~ $ lscpu
Architecture:        aarch64
Byte Order:          Little Endian
CPU(s):              4
On-line CPU(s) list: 0-3
Thread(s) per core:  1
Core(s) per socket:  4
Socket(s):           1
Vendor ID:           ARM
Model:               3
Model name:          Cortex-A72
Stepping:            r0p3
CPU max MHz:         2000,0000
CPU min MHz:         600,0000
BogoMIPS:            108.00
Flags:               fp asimd evtstrm crc32 cpuid


I dont see here aarch64 architecture
![2021-05-06-154951_447x150_scrot](https://user-images.githubusercontent.com/76708049/117309474-bcb6a500-ae82-11eb-85a7-ff95cc14e5ae.png)


## SChernykh | 2021-05-06T13:54:30+00:00
RPi 4B is ARMv8-A architecture (64-bit). You need to have 64-bit OS and compiler, and performance will be much better.

## Skilowi | 2021-05-06T13:58:29+00:00
i have putted in config.txt arm_64bit=1 so raspiOS is running on 64bits kernel (in beta :/) and cmake is 3.16.3 (GNU Make 4.2.1)

When compiling it crashes at 82% and throws many errors

## Skilowi | 2021-05-06T15:41:37+00:00
damn.
![](https://cdn.discordapp.com/attachments/810866716942925844/839889295300231178/2021-05-06-173929_545x30_scrot.png)


## foomip | 2021-08-22T14:20:54+00:00
I am getting the same error on my Raspberry PI 4.

lscpu output
```
Architecture:        aarch64
Byte Order:          Little Endian
CPU(s):              4
On-line CPU(s) list: 0-3
Thread(s) per core:  1
Core(s) per socket:  4
Socket(s):           1
Vendor ID:           ARM
Model:               3
Model name:          Cortex-A72
Stepping:            r0p3
CPU max MHz:         1500.0000
CPU min MHz:         600.0000
BogoMIPS:            108.00
Flags:               fp asimd evtstrm crc32 cpuid
```

## kwsp | 2021-10-09T22:07:01+00:00
After installing the 64bit kernel on your raspberry pi, you need to run `ds64-shell` to activate a shell inside the 64bit OS. You'll have to install all the dependencies again but compiling from there should work.

## benthetechguy | 2022-01-26T00:12:12+00:00
fixed in #2898

# Action History
- Created by: royheuer | 2021-05-06T12:04:48+00:00
- Closed at: 2025-06-16T18:48:36+00:00
