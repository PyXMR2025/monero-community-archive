---
title: Can this be compiled for Android?
source_url: https://github.com/xmrig/xmrig/issues/2525
author: Joe23232
assignees: []
labels: []
created_at: '2021-08-09T13:09:58+00:00'
updated_at: '2026-02-05T13:27:58+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Can this be compiled for Android?

# Discussion History
## ReperakDev | 2021-08-09T15:46:32+00:00
It definitely can, as long as you use a Linux environment such as [Termux](https://termux.com/).

## Spudz76 | 2021-08-09T16:58:54+00:00
Yes.  I've never gotten it to work, personally, but I also don't have any Android devices with 64-bit and/or enough cache, and I was trying to build it "the right way" with the Android SDK cross-compiling on a real computer.

## Joe23232 | 2021-08-09T22:44:34+00:00
@ReperakPro @Spudz76 Hey guys, so would it compile for ARM architectures though since most Android phones are ARM?

## ReperakDev | 2021-08-09T23:08:49+00:00
Yes, XMRig has ARM support.

## Spudz76 | 2021-08-10T03:06:59+00:00
There are two flavors of ARM, ARMv7 and ARMv8 where v8 is of course better (64-bit).

## Joe23232 | 2021-08-10T03:52:32+00:00
If I compiled it on ARM, would it work on ARMv8 on Android but not vice versa?

## ReperakDev | 2021-08-10T21:29:45+00:00
If your Android device is 64-bit, then XMRig will automatically compile for ARMv8, which is the only 64-bit ARM specification to my knowledge, meaning that it won't work with anything less than ARMv7 (32-bit)

## Joe23232 | 2021-08-10T23:15:30+00:00
Sorry I am a little confused here, how can xmrig automatically compile for ARMv8? Unless if I compiled xmrig for Android and then it has machine code for ARMv7 and ARMv8?

## ReperakDev | 2021-08-11T03:01:09+00:00
CMake takes care of it.

## Joe23232 | 2021-08-11T03:28:11+00:00
Ok thanks

## Spudz76 | 2021-08-12T06:23:18+00:00
Detection code is in [cmake/cpu.cmake starting at line 11](https://github.com/xmrig/xmrig/blob/master/cmake/cpu.cmake#L11)

Occasionally it makes incorrect detection but that may only be when the Termux stuff isn't set up quite right.  It can be forced with `-DARM_TARGET=7` or `-DARM_TARGET=8` which if given will skip ARM autodetection.

## Joe23232 | 2021-08-12T07:43:30+00:00
Why wouldn't I just compile it on Windows and target it for Android?

On Thu, Aug 12, 2021 at 4:23 PM Tony Butler ***@***.***>
wrote:

> Detection code is in cmake/cpu.cmake starting at line 11
> <https://github.com/xmrig/xmrig/blob/master/cmake/cpu.cmake#L11>
>
> Occasionally it makes incorrect detection but that may only be when the
> Termux stuff isn't set up quite right. It can be forced with
> -DARM_TARGET=7 or -DARM_TARGET=8 which if given will skip ARM
> autodetection.
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/2525#issuecomment-897380969>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AIKO7IJWKR5T4EM3YMTBXVLT4NSGDANCNFSM5BZ7TH6A>
> .
> Triage notifications on the go with GitHub Mobile for iOS
> <https://apps.apple.com/app/apple-store/id1477376905?ct=notification-email&mt=8&pt=524675>
> or Android
> <https://play.google.com/store/apps/details?id=com.github.android&utm_campaign=notification-email>
> .
>


## Spudz76 | 2021-08-12T18:13:30+00:00
I haven't gotten that "proper" method of building Android stuff, to work yet.  Partially because that detection code uses `CMAKE_SYSTEM_PROCESSOR` which is the compiling computer's CPU not the cross-target CPU.

## Joe23232 | 2021-08-13T02:29:38+00:00
Ah right, thanks mate then.

## mymirai-nikki | 2026-02-05T11:17:52+00:00
what target I should use for the following device?
```
$  adb shell
A37:/ # uname -a
Linux localhost 3.10.108-Nebula-g089c1872808-dirty #1 SMP PREEMPT Thu Jan 18 11:34:32 IST 2024 armv8l
A37:/ # cat /proc/cpuinfo
processor       : 0
Features        : half thumb fastmult vfp edsp neon vfpv3 tls vfpv4 idiva idivt evtstrm
CPU implementer : 0x41
CPU architecture: 8
CPU variant     : 0x0
CPU part        : 0xd03
CPU revision    : 0

processor       : 1
Features        : half thumb fastmult vfp edsp neon vfpv3 tls vfpv4 idiva idivt evtstrm
CPU implementer : 0x41
CPU architecture: 8
CPU variant     : 0x0
CPU part        : 0xd03
CPU revision    : 0

processor       : 2
Features        : half thumb fastmult vfp edsp neon vfpv3 tls vfpv4 idiva idivt evtstrm
CPU implementer : 0x41
CPU architecture: 8
CPU variant     : 0x0
CPU part        : 0xd03
CPU revision    : 0

processor       : 3
Features        : half thumb fastmult vfp edsp neon vfpv3 tls vfpv4 idiva idivt evtstrm
CPU implementer : 0x41
CPU architecture: 8
CPU variant     : 0x0
CPU part        : 0xd03
CPU revision    : 0

wp half thumb fastmult vfp edsp neon vfpv3 tlsi vfpv4 idiva idivt
A37:/ # getconf LONG_BIT
32
A37:/ # getprop ro.product.cpu.abi
armeabi-v7a
A37:/ # getprop ro.product.cpu.abilist
armeabi-v7a,armeabi
A37:/ # getprop ro.build.version.sdk
32
```

## mymirai-nikki | 2026-02-05T11:20:42+00:00
I can't find pre-built binary for android arm on the github release page or https://download.xmrig.com/xmrig/6.25.0/753859caea40cd645eacb9049cf94a8104d63f43/

## mymirai-nikki | 2026-02-05T13:17:55+00:00
with the help of AI, I successfully cross-compiled it to Android! If anyone is interested, check this out: https://gist.github.com/mymirai-nikki/62d0cd6bc7f10463eff7364056a168bf

```
|    CPU # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |       -1 |    0.11 |    0.15 |    0.18 |
|        1 |       -1 |    0.21 |    0.15 |    0.18 |
|        2 |       -1 |    0.11 |    0.15 |    0.18 |
|        3 |       -1 |    0.11 |    0.15 |    0.18 |
|        - |        - |    0.53 |    0.60 |    0.70 |
[2026-02-05 20:24:32.035]  miner    speed 10s/60s/15m 0.53 0.60 0.70 H/s max 0.84 H/s
 - CONNECTION
 * pool address     192.168.18.201:3333 (192.168.18.201)
 * algorithm        rx/0
 * difficulty       1000
 * ping time        106ms
 * connection time  1610s
 - RESULTS
 * accepted         2 (100.0%)
 * pool-side hashes 2000 avg 1000
 * difficulty       1000
 * avg result time  805.6s
 - TOP 10
  # | DIFFICULTY | EFFORT % |
  1 |      15571 |    12.84 |
  2 |       1992 |   100.40 |
```
Although after seeing the hashrate, I don't think it's a good idea to mine on a low-spec Android phone, lol.

# Action History
- Created by: Joe23232 | 2021-08-09T13:09:58+00:00
