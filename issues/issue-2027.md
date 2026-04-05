---
title: 'Mining Monero on raspi 4 '
source_url: https://github.com/xmrig/xmrig/issues/2027
author: Noisk8
assignees: []
labels:
- bug
created_at: '2021-01-07T05:06:48+00:00'
updated_at: '2022-02-01T17:59:05+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:25:03+00:00'
---

# Original Description
Hello, I'm new in the world of mining, I'm mining monero via terminal on my computer linux 64 and everything is going well, recently bought a raspi 4, but I do not know how to put to roll the script ./xmrig appears to me that the binary is not compatible, I imagine that is by the architecture of the raspi is arm, I would like to know if anyone knows how is the way to mine monero in raspi 4 with xmrig, thank you very much for your attention 



# Discussion History
## SChernykh | 2021-01-07T08:36:29+00:00
You need to build it from source: https://xmrig.com/docs/miner/build

## Noisk8 | 2021-01-07T20:50:12+00:00
Hi, good afternoon, I just compiled the binary and when I launch the script I get this message 

Illegal instruction (core dumped)

Can anyone tell me why this is?

Thank you very much for your time and support 

## SChernykh | 2021-01-07T20:57:09+00:00
Try to disable AES - `"hw-aes": false,` in config.json

## Noisk8 | 2021-01-08T08:16:25+00:00
Thank you very much !!!!!! is already running...

I don't want to remain in the ignorance of making a line change, can you explain us what happens in the script when we make that change from false to null?

## xmrig | 2021-01-08T08:31:13+00:00
`false` disable hardware AES (raspberry pi doesn't support it), `true` enable it.
`null` or other invalid value or missing option, means auto detect, seems there is a bug and miner detects hardware AES, but it is not supported.
Please provide details about the Linux distribution you use and output of `lscpu`.
Thank you.


## coffeeroaster | 2021-01-10T22:40:13+00:00
Having the same problem.  I set `"hw-aes": false,` in config.json and still getting illegal instruction.  lscpu output: 
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

## SChernykh | 2021-01-10T22:44:37+00:00
Try this: https://github.com/xmrig/xmrig/issues/1567#issuecomment-757501022
It should work on RPi 4.

## coffeeroaster | 2021-01-10T23:26:49+00:00
Thanks. removing the build directory and disabling AES did the trick. I also recompiled the kernel with HUGE page support. Getting  96H/S.
Edit: removing the build directory and re-running cmake.

## coffeeroaster | 2021-01-11T23:31:29+00:00
Still happening randomly to me with with the same error. Any other ideas?
```
[New Thread 0x7ff1db61c0 (LWP 6132)]
[New Thread 0x7ff25b71c0 (LWP 6133)]
[New Thread 0x7ff2db81c0 (LWP 6134)]
[2021-01-11 18:34:50.810]  cpu      READY threads 4/4 (4) huge pages 0% 0/4 memory 8192 KB (4 ms)

Thread 59 "xmrig" received signal SIGILL, Illegal instruction.
[Switching to Thread 0x7ff15b51c0 (LWP 6131)]
0x0000007ff01af000 in ?? ()
(gdb) 
```

## coffeeroaster | 2021-01-12T19:34:45+00:00
ok I think I finally resolved the issue on my end. I built it with the following:
```
cmake .. -DCMAKE_BUILD_TYPE=Release -DWITH_OPENCL=OFF -DWITH_CUDA=OFF -DXMRIG_DEPS=scripts/deps -DWITH_SSE4_1=OFF
```
Note: I think the culprit in this case was `SSE4_1`. So far so good.

## Noisk8 | 2021-01-12T20:19:29+00:00
@coffeeroaster  you can shareme the jason.confug file plis to compare with mi file....

## Noisk8 | 2021-01-12T20:21:59+00:00
@xmrig  hi dude,  i still have the same problem Illegal instruction (core dumped)


my lshw output is 

   description: Computer
    product: Raspberry Pi 4 Model B Rev 1.4
    serial: 10000000352b271f
    width: 64 bits
    capabilities: smp cp15_barrier setend swp tagged_addr_disabled
  *-core
       description: Motherboard
       physical id: 0
     *-cpu:0
          description: CPU
          product: cpu
          physical id: 1
          bus info: cpu@0
          size: 1500MHz
          capacity: 1500MHz
          capabilities: fp asimd evtstrm crc32 cpuid cpufreq
     *-cpu:1
          description: CPU
          product: cpu
          physical id: 2
          bus info: cpu@1
          size: 1500MHz
          capacity: 1500MHz
          capabilities: fp asimd evtstrm crc32 cpuid cpufreq
     *-cpu:2
          description: CPU
          product: cpu
          physical id: 3
          bus info: cpu@2
          size: 1500MHz
          capacity: 1500MHz
          capabilities: fp asimd evtstrm crc32 cpuid cpufreq
     *-cpu:3
          description: CPU
          product: cpu
          physical id: 4
          bus info: cpu@3
          size: 1500MHz
          capacity: 1500MHz
          capabilities: fp asimd evtstrm crc32 cpuid cpufreq
     *-memory
          description: System memory
          physical id: 5
          size: 7759MiB
     *-pci
          description: PCI bridge
          product: Broadcom Inc. and subsidiaries
          vendor: Broadcom Inc. and subsidiaries
          physical id: 0
          bus info: pci@0000:00:00.0
          version: 10
          width: 32 bits
          clock: 33MHz
          capabilities: pci normal_decode bus_master cap_list
          configuration: driver=pcieport
          resources: irq:41 memory:600000000-6000fffff
        *-usb
             description: USB controller
             product: VL805 USB 3.0 Host Controller
             vendor: VIA Technologies, Inc.
             physical id: 0
             bus info: pci@0000:01:00.0
             version: 01
             width: 64 bits
             clock: 33MHz
             capabilities: xhci bus_master cap_list
             configuration: driver=xhci_hcd latency=0
             resources: irq:42 memory:600000000-600000fff
  *-network:0
       description: Ethernet interface
       physical id: 1
       logical name: eth0
       serial: dc:a6:32:c4:3f:91
       capacity: 1Gbit/s
       capabilities: ethernet physical tp mii 10bt 10bt-fd 100bt 100bt-fd 1000bt 1000bt-fd autonegotiation
       configuration: autonegotiation=on broadcast=yes driver=bcmgenet driverversion=5.8.0-1011-raspi link=no multicast=yes port=MII
  *-network:1
       description: Wireless interface
       physical id: 2
       logical name: wlan0
       serial: dc:a6:32:c4:3f:92
       capabilities: ethernet physical wireless
       configuration: broadcast=yes driver=brcmfmac driverversion=7.45.206 firmware=01-88ee44ea ip=192.168.0.109 multicast=yes wireless=IEEE 802.11


my SO is 

Ubuntu 20.10 \n \l

very thanks to u time !!!




## coffeeroaster | 2021-01-12T20:25:47+00:00
1.) did set "hw-aes" to false in src/config.json?
2.) How did you build ?

## Noisk8 | 2021-01-12T22:16:05+00:00

1) yes i pu false en hs-aes


2)
sudo apt update
sudo apt install git build-essential cmake libuv1-dev libssl-dev libhwloc-dev
git clone https://github.com/xmrig/xmrig.git
cd xmrig
mkdir build
cd build
[here use u recomendation] cmake .. -DCMAKE_BUILD_TYPE=Release -DWITH_OPENCL=OFF -DWITH_CUDA=OFF -DXMRIG_DEPS=scripts/deps -DWITH_SSE4_1=OFF
make

and to  play with this line 

./xmrig -a cryptonight -o stratum+tcp://xmr.pool.minergate.com:45700 -u my@mail.com -p x+







## Noisk8 | 2021-01-15T00:42:46+00:00
well, I tell you that the raspberry was mining a couple of hours with the change of the file jason.config

"hw-aes" to false 

but stopped again with the error Illegal instruction (core dumped)


this is the ubuntu i have installed 

https://ubuntu.com/download/raspberry-pi/thank-you?version=20.10&architecture=desktop-arm64+raspi

someone can explain to me why that mistake 


## coffeeroaster | 2021-01-15T00:56:27+00:00
I also ran into the same problem again. There appears to be some bug with the makefile. A hacky work around I used was to do the following:
```
--- a/cmake/cpu.cmake
+++ b/cmake/cpu.cmake
@@ -28,14 +28,7 @@ if (ARM_TARGET AND ARM_TARGET GREATER 6)
         set(XMRIG_ARMv8 ON)
         add_definitions(/DXMRIG_ARMv8)
 
-        CHECK_CXX_COMPILER_FLAG(-march=armv8-a+crypto XMRIG_ARM_CRYPTO)
-
-        if (XMRIG_ARM_CRYPTO)
-            add_definitions(/DXMRIG_ARM_CRYPTO)
-            set(ARM8_CXX_FLAGS "-march=armv8-a+crypto")
-        else()
-            set(ARM8_CXX_FLAGS "-march=armv8-a")
-        endif()
+        set(ARM8_CXX_FLAGS "-march=armv8-a")
     elseif (ARM_TARGET EQUAL 7)
```
You can double check the `march` flag is correct (march=armv8-a)  with `make VERBOSE=1`
Note: I still get the illegal instruction sometimes, but it mostly works..

## Noisk8 | 2021-01-18T14:39:33+00:00
@coffeeroaster  sorry what is this file ?

## Spudz76 | 2021-01-18T20:21:03+00:00
@Noisk8 hmm I'm going out on a limb here, but probably `cmake/cpu.cmake` considering unified diffs always have filenames at the top

![image](https://user-images.githubusercontent.com/2391234/104959683-faed8e80-598f-11eb-9beb-abe8151fa422.png)


## coffeeroaster | 2021-01-18T20:29:09+00:00
correct. cmake/cpu.cmake

## Noisk8 | 2021-01-18T23:14:17+00:00
This is my cpu.make, its wrong ?

if (NOT CMAKE_SYSTEM_PROCESSOR)
    message(WARNING "CMAKE_SYSTEM_PROCESSOR not defined")
endif()

if (CMAKE_SYSTEM_PROCESSOR MATCHES "^(x86_64|AMD64)$" AND CMAKE_SIZEOF_VOID_P EQUAL 8)
    add_definitions(/DRAPIDJSON_SSE2)
else()
    set(WITH_SSE4_1 OFF)
endif()

if (NOT ARM_TARGET)
    if (CMAKE_SYSTEM_PROCESSOR MATCHES "^(aarch64|arm64|armv8-a)$")
        set(ARM_TARGET 8)
    elseif (CMAKE_SYSTEM_PROCESSOR MATCHES "^(armv7|armv7f|armv7s|armv7k|armv7-a|armv7l)$")
        set(ARM_TARGET 7)
    endif()
endif()

if (ARM_TARGET AND ARM_TARGET GREATER 6)
    set(XMRIG_ARM     ON)
    add_definitions(/DXMRIG_ARM)

    message(STATUS "Use ARM_TARGET=${ARM_TARGET} (${CMAKE_SYSTEM_PROCESSOR})")

    include(CheckCXXCompilerFlag)

    if (ARM_TARGET EQUAL 8)
        set(XMRIG_ARMv8 ON)
        add_definitions(/DXMRIG_ARMv8)

        CHECK_CXX_COMPILER_FLAG(-march=armv8-a+crypto XMRIG_ARM_CRYPTO)

        if (XMRIG_ARM_CRYPTO)
            add_definitions(/DXMRIG_ARM_CRYPTO)
            set(ARM8_CXX_FLAGS "-march=armv8-a+crypto")
        else()
            set(ARM8_CXX_FLAGS "-march=armv8-a")
        endif()
    elseif (ARM_TARGET EQUAL 7)
        set(XMRIG_ARMv7 ON)
        add_definitions(/DXMRIG_ARMv7)
    endif()
endif()

if (WITH_SSE4_1)
    add_definitions(/DXMRIG_FEATURE_SSE4_1)
endif()


note: the miner sometime run, but it stops too much with the error of illegal instruction :( 

## gms2009 | 2021-01-20T10:26:44+00:00
About what hashrate the pi can get?

## Noisk8 | 2021-01-21T16:20:57+00:00
Greetings I have the raspi 4 with 8 ram, I usually get a hast rate of 80 to 100, but sometimes I get up to 280-300. withou overclock...

here is the balance that the pool gives 


Total Hash Rate: (24h) 29.75 H/s (12h) 1.99 H/s (1h) 28.20 H/s (10m) 200.00 H/s

note: the balance is from two raspberries

## FPS-Lightning | 2021-01-29T21:17:43+00:00
@Noisk8 broken any ground? from my experience, I had a working version of xmrig on my raspberry pi 4 4gb on the 64-bit OS. I can't seem to get back to that version. What would you recommend that I try, because the suggestions so far have not made any difference to me.

## Noisk8 | 2021-02-01T20:41:02+00:00
80 MHS


El mié, 20 ene 2021 a las 5:27, gms2009 (<notifications@github.com>)
escribió:

> About what hashrate the pi can get?
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/2027#issuecomment-763503591>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AEHDR4AE4ERRPB3PHCDWWBDS22VXLANCNFSM4VYOZZQA>
> .
>


## FPS-Lightning | 2021-02-01T21:36:01+00:00
> 80 MHS El mié, 20 ene 2021 a las 5:27, gms2009 (<notifications@github.com>) escribió:
> […](#)
> About what hashrate the pi can get? — You are receiving this because you were mentioned. Reply to this email directly, view it on GitHub <[#2027 (comment)](https://github.com/xmrig/xmrig/issues/2027#issuecomment-763503591)>, or unsubscribe <https://github.com/notifications/unsubscribe-auth/AEHDR4AE4ERRPB3PHCDWWBDS22VXLANCNFSM4VYOZZQA> .

Also, this all depends on the currency you mine. Personally, due to the low processor cache size on the pi, I went with ArQMA due to it's lower scratchpad size. I push nearly 1kh/s on that currency.
Also, I personally made some ground on this topic myself about the pi not working at all. I will link to my findings somewhere in this thread.

## FPS-Lightning | 2021-02-01T21:38:45+00:00
Hello all, after having this same issue with the "Illegal Instruction" bug, I came to an alternative solution. I am a dev at one of the mining pools and I have a writeup on our wiki [here](https://github.com/GNTLMiningPools/Mining-Support/wiki/Mining-on-Raspberry-Pi) which basically uses older versions of xmrig which I have verified to not contain this issue. By following the guide I have written it should be a fairly easy process to get your pi up and mining.

## SChernykh | 2021-02-01T21:58:37+00:00
Illegal instruction crash is fixed in the dev branch, see #2077 

## FPS-Lightning | 2021-02-01T22:03:20+00:00
> Illegal instruction crash is fixed in the dev branch, see #2077

Oh okay, cool. Is there any real reason to run the newest version though? Like are there significant optimizations that I'm missing out on in 6.3.4/6.3.5?

## SChernykh | 2021-02-01T22:04:40+00:00
There are more new features, Apple M1 support. No significant optimizations for ARM though, except better huge pages support: https://github.com/xmrig/xmrig/pull/2076

## Grantrocks | 2021-12-02T13:25:17+00:00
You can mine on  a raspberry pi too
https://cryptoandpi.cf/blog/posts/mining-on-raspi-in-2022

# Action History
- Created by: Noisk8 | 2021-01-07T05:06:48+00:00
- Closed at: 2021-04-12T14:25:03+00:00
