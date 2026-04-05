---
title: Low hashrate on win32  xmrig
source_url: https://github.com/xmrig/xmrig/issues/846
author: jiaxu2000
assignees: []
labels: []
created_at: '2018-10-25T07:54:44+00:00'
updated_at: '2019-03-17T16:32:48+00:00'
type: issue
status: closed
closed_at: '2019-03-17T16:32:48+00:00'
---

# Original Description
I found that the 2.8.x version of the win32 program is a lot slower.
I did an interesting test
Same computer , windows 7 64 bit , intel i7 2600k CPU 
delete config.json file

xmrig.exe -o stratum+tcp://pool.supportxmr.com:5555 -u ****************************** -p x 

xmrig-2.8.3-gcc-win32.zip  speed 10s/60s/15m 54.0 51.8 n/a H/s max 54.7 H/s
xmrig-2.8.3-gcc-win64.zip speed 10s/60s/15m 103.1 n/a n/a H/s max 107.5 H/s

I used the options av=1/2/3/4/5, hw-aes, asm=none/intel/auto, etc., but the speed of win32 is not optimized.

I understand that the new CN2 algo will slow down, but the 32-bit xmrig program on the G4560, G4400, i5 6500 and other CPUs is 100%-300% slower than before, while the 64-bit xmrig is only 30%-50% slower than before 

I don't expect win32 to be as fast as win64, but win32 is much slower than before.



# Discussion History
## jiaxu2000 | 2018-10-26T05:22:31+00:00
different win32 and win64

win32

 * ABOUT        XMRig/2.8.3 gcc/7.2.0
 * LIBS         libuv/1.15.0 OpenSSL/1.1.1 microhttpd/0.9.58
 * HUGE PAGES   available
 * CPU          Intel(R) Core(TM) i7-2600K CPU @ 3.40GHz (1) -x64 AES
 * CPU L2/L3    1.0 MB/8.0 MB
 * THREADS      4, cryptonight, donate=5%
 * POOL #1      ************** variant auto
 * COMMANDS     hashrate, pause, resume
[2018-10-26 13:09:06] use pool **********************
[2018-10-26 13:09:06] new job from ********************* diff 12000 algo cn/2
[2018-10-26 13:09:06] READY (CPU) threads 4(4) huge pages 4/4 100% memory 8.0 MB


win64

 * ABOUT        XMRig/2.8.3 gcc/8.2.0
 * LIBS         libuv/1.23.1 OpenSSL/1.1.1 microhttpd/0.9.59
 * HUGE PAGES   available
 * CPU          Intel(R) Core(TM) i7-2600K CPU @ 3.40GHz (1) x64 AES
 * CPU L2/L3    1.0 MB/8.0 MB
 * THREADS      4, cryptonight, donate=5%
 * ASSEMBLY     auto:intel-----------------------------------------------------different 
 * POOL #1      ************* variant auto
 * COMMANDS     hashrate, pause, resume
[2018-10-26 13:14:38] use pool ******************
[2018-10-26 13:14:38] new job from ******************* diff 12000 algo cn/2
[2018-10-26 13:14:38] READY (CPU) threads 4(4) huge pages 4/4 100% memory 8.0 MB

Win64 has one more line than win32
 * ASSEMBLY     auto:intel


different config.json file

win32：
…………………………
…………………………
"threads": [
        {
            "low_power_mode": 1,
            "affine_to_cpu": false,
        },
        {
            "low_power_mode": 1,
            "affine_to_cpu": false,
        },
        {
            "low_power_mode": 1,
            "affine_to_cpu": false,
        },
        {
            "low_power_mode": 1,
            "affine_to_cpu": false,
        }
    ],
………………
………………



win64：
…………………………
…………………………
"asm": true,
…………………………
…………………………

"threads": [
        {
            "low_power_mode": 1,
            "affine_to_cpu": false,
            "asm": true
        },
        {
            "low_power_mode": 1,
            "affine_to_cpu": false,
            "asm": true
        },
        {
            "low_power_mode": 1,
            "affine_to_cpu": false,
            "asm": true
        },
        {
            "low_power_mode": 1,
            "affine_to_cpu": false,
            "asm": true
        }
    ],

I copied the win64 config.json file to win32, win32 still can't correctly identify the CPU.

## jiaxu2000 | 2018-10-26T07:39:53+00:00
I use av=3 parameter in win64, forcing soft AES, the speed is exactly the same as win32.

From this it can be concluded that win32 cannot use the Hardware AES function.

I hope fix in next versions

## xmrig | 2018-10-27T10:13:03+00:00
1. Assembly only available for 64 bit (av 1 and av2), it not available for 32 bit builds at all.
2. Hardware AES supported by 32 bit builds, but not all registers available and some 64 bit instructions emulated, it always slower.

## sailei00 | 2018-10-28T03:02:41+00:00
I found that too,and is there any way to make it as fast as before?

## jiaxu2000 | 2018-11-01T05:57:34+00:00
> 1. Assembly only available for 64 bit (av 1 and av2), it not available for 32 bit builds at all.
> 2. Hardware AES supported by 32 bit builds, but not all registers available and some 64 bit instructions emulated, it always slower.

I read the source code of xmrig carefully.
in cmake/asm.cmake file

if (WITH_ASM AND NOT XMRIG_ARM AND CMAKE_SIZEOF_VOID_P EQUAL 8)
    set(XMRIG_ASM_LIBRARY "xmrig-asm")
    ...........................................
    .............................................
else()
    set(XMRIG_ASM_SOURCES "")
    set(XMRIG_ASM_LIBRARY "")
    add_definitions(/DXMRIG_NO_ASM)
endif()

From the condition of CMAKE_SIZEOF_VOID_P EQUAL 8, it is easy to see that win32 does not get any optimization, win64 and win32 are not treated the same, I guess win32 will not use any Hard AES instructions.

Win32 has been tagged with -D XMRIG_NO_ASM, so no acceleration is used at all.

There are a lot of judgment conditions in the source code for # ifndef XMRIG_NO_ASM


## xmrig | 2018-11-05T15:02:52+00:00
`ASM` not equal `AES`.

## 123456789vgkeine | 2018-11-15T21:43:15+00:00
very bad that no x32

## postubsla | 2018-11-16T00:41:17+00:00
for me it is also inconvenient that there is no x32, I ask to make x32

## hantokokume | 2019-01-01T06:45:58+00:00
What is your benefit that there is no x32 very very sorry that you do not want to do x32

## 123456789vgkeine | 2019-01-01T07:24:16+00:00
> What is your benefit that there is no x32 very very sorry that you do not want to do x32

Lazy campaign

## yarigoyaosu | 2019-01-01T23:08:14+00:00
> `ASM` not equal `AES`.

nonsense that no x32? why didn't you do MSVC 32 bit

## DeadManWalkingTO | 2019-03-17T14:46:37+00:00
I think this issue can be closed.
Thank you!

# Action History
- Created by: jiaxu2000 | 2018-10-25T07:54:44+00:00
- Closed at: 2019-03-17T16:32:48+00:00
