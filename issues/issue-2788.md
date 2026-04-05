---
title: hello i have a problem with cmake on raspberry pi 4 8GB.
source_url: https://github.com/xmrig/xmrig/issues/2788
author: razvanwir
assignees: []
labels:
- bug
- arm
created_at: '2021-12-04T07:35:21+00:00'
updated_at: '2025-06-16T20:25:40+00:00'
type: issue
status: closed
closed_at: '2025-06-16T20:25:40+00:00'
---

# Original Description
In file included from /home/pi/xmrig/src/crypto/ghostrider/ghostrider.cpp:57:
/home/pi/xmrig/src/crypto/ghostrider/../../crypto/cn/sse2neon.h:122:2: error: #error "Unsupported target. Must be either ARMv7-A+NEON or ARMv8-A."
  122 | #error "Unsupported target. Must be either ARMv7-A+NEON or ARMv8-A."
      |  ^~~~~
In file included from /home/pi/xmrig/src/crypto/ghostrider/ghostrider.cpp:57:
/home/pi/xmrig/src/crypto/ghostrider/../../crypto/cn/sse2neon.h:7594:9: warning: ‘#pragma GCC pop_options’ without a corresponding ‘#pragma GCC push_options’ [-Wpragmas]
 7594 | #pragma GCC pop_options
      |         ^~~
make[2]: *** [src/crypto/ghostrider/CMakeFiles/ghostrider.dir/build.make:290: src/crypto/ghostrider/CMakeFiles/ghostrider.dir/ghostrider.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:240: src/crypto/ghostrider/CMakeFiles/ghostrider.dir/all] Error 2
make: *** [Makefile:103: all] Error 2


# Discussion History
## razvanwir | 2021-12-04T10:56:56+00:00
please help. 

## Spudz76 | 2021-12-04T17:23:19+00:00
Usually these problems (on ARM-v8) are related to something being 32-bit.  Ensure your Pi OS is full 64-bit (kernel, compiler, etc).

If it's actually a 32-bit Pi (ARM-v7) then the opposite.

Sometimes forcing it with `-DARM_TARGET=8` (or if it's a 7, `7`) helps.

## Spudz76 | 2021-12-04T17:48:21+00:00
Noticed you said Pi4 which is of course `8`

## razvanwir | 2021-12-04T17:56:53+00:00
is the exactly the same error.

## razvanwir | 2021-12-04T17:57:09+00:00
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
CPU max MHz:         1800.0000
CPU min MHz:         600.0000
BogoMIPS:            108.00
Flags:               half thumb fastmult vfp edsp neon vfpv3 tls vfpv4 idiva idi
                     vt vfpd32 lpae evtstrm crc32


## razvanwir | 2021-12-04T17:59:14+00:00
![image](https://user-images.githubusercontent.com/39533194/144719689-bec3a92d-702c-479c-bd03-a078ddd594f0.png)


## razvanwir | 2021-12-04T18:04:01+00:00
I do not know what to do . I tried all the options. I've been trying for 1 day.


## Spudz76 | 2021-12-04T18:31:40+00:00
You have Rasbian with 32-bit kernel apparently.

You need full 64-bit everything, find either the beta Raspbian 64 or install normal Debian 64 for ARM

See here for [slightly more explanation](https://raspberrypi.stackexchange.com/questions/101215/why-raspberry-pi-4b-claims-that-its-processor-is-armv7l-when-in-official-specif)

## Spudz76 | 2021-12-04T18:33:29+00:00
This seems to be a [valid how-to-64-your-pi type article](https://pimylifeup.com/raspberry-pi-64-bit/)

## razvanwir | 2021-12-05T07:58:35+00:00
ok. i will try to install a debian . 

## razvanwir | 2021-12-05T15:02:20+00:00
when i tryed i see  
![image](https://user-images.githubusercontent.com/39533194/144752015-4d1e7b7d-d9f6-46b2-b14a-7020e6dbf087.png)

after 4 tryed.


## razvanwir | 2021-12-06T11:33:39+00:00
Rezolved ! and miner works.

## kazmek | 2021-12-07T00:23:51+00:00
I had that same issue getting the Pi4 to work. It has to do with running the 32 bit OS. It fails and throws errors even when you specify to compile for ARM 7. The best bet is to flash with a new image 64 bit image.
I prefer to use the light versions and go CLI. You can find the images here https://downloads.raspberrypi.org/

`sudo apt-get update && sudo apt-get upgrade -y`
`sudo rpi-update` to ensure you have the latest firmware too.

You can find all the commands you need inside the wiki for the rest of the install using 
`sudo git clone https://github.com/xmrig`


## bastifpv | 2021-12-07T15:13:26+00:00
i have the same problem, upgrading to 64 bit didn't fix it

## Spudz76 | 2021-12-07T18:32:52+00:00
Make sure it's full full full 64-bit everything version, not just stupid 64-bit kernel with 32-bit userspace.

## kazmek | 2021-12-08T01:50:40+00:00
@Basti2502 run this command from the CLI to be sure you have the 64 bit OS.

`uname -m`
You should see a printout like this. You are looking for the v8+ at the end of the OS version and aarch64.
Linux devicename 5.10.82-**v8+** #1493 SMP PREEMPT Wed Dec 1 11:40:12 GMT 2021 **aarch64** GNU/Linux
Another helpful command is `lscpu`. This is good for checking processor info.
If you need to update to a 64 bit OS, I suggest using the rpiOS-lite version located here <https://downloads.raspberrypi.org/raspios_arm64/images/raspios_arm64-2021-11-08/>

Post edit here. If you updated to a 64 bit OS, make sure you installed 64 bit dependencies. That can cause issues if you are trying to compile with 32 bit.
Here is a command to check `sudo apt list git build-essential* cmake libuv1-dev* libssl-dev* libhw
loc-dev* -i`
You should see the 64 bit versions listed. If you see a 32, remove it and install the 64.

## benthetechguy | 2022-01-26T00:08:20+00:00
Original issue is fixed in #2898

# Action History
- Created by: razvanwir | 2021-12-04T07:35:21+00:00
- Closed at: 2025-06-16T20:25:40+00:00
