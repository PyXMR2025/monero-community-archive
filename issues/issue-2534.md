---
title: FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
source_url: https://github.com/xmrig/xmrig/issues/2534
author: marqanton
assignees: []
labels: []
created_at: '2021-08-12T13:33:46+00:00'
updated_at: '2021-08-13T19:00:24+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I am getting the below message when running xmrig on a dell computer. I am trying to mine ZCH. Please find the output below.

I am running it with root.

[root@master xmrig-6.13.1]# ./xmrig
 * ABOUT        XMRig/6.13.1 gcc/5.4.0
 * LIBS         libuv/1.41.0 OpenSSL/1.1.1k hwloc/2.4.1
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel(R) Core(TM) i5-8500T CPU @ 2.10GHz (1) 64-bit AES
                L2:1.5 MB L3:9.0 MB 6C/6T NUMA:1
 * MEMORY       4.1/7.5 GB (54%)
                DIMM1: 8 GB DDR4 @ 2666 MHz HMA81GS6JJR8N-VK
                DIMM2: <empty>
 * MOTHERBOARD  Dell Inc. - 03KWTV
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      rx.unmineable.com:3333 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2021-08-12 09:26:47.232]  net      use pool rx.unmineable.com:3333  139.59.164.251
[2021-08-12 09:26:47.232]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2425479
[2021-08-12 09:26:47.232]  cpu      use argon2 implementation AVX2
[2021-08-12 09:26:47.243]  msr      cannot set MSR 0x000001a4 to 0x000000000000000f
[2021-08-12 09:26:47.243]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
[2021-08-12 09:26:47.243]  randomx  init dataset algo rx/0 (6 threads) seed 9c34f003984b0df9...
[2021-08-12 09:26:47.671]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (428 ms)
[2021-08-12 09:26:52.350]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2425480
[2021-08-12 09:26:52.436]  signal   Ctrl+C received, exiting
[2021-08-12 09:26:52.471]  msr      cannot set MSR 0x000001a4 to 0x0000000000000000
[2021-08-12 09:26:52.471]  msr      failed to restore initial state (34 ms)
^C
[root@master xmrig-6.13.1]#


# Discussion History
## Spudz76 | 2021-08-12T18:27:18+00:00
May not be available for writes.  If booting with UEFI then Secure Boot must be disabled (or MSR writes permanently locked).  Might need to override the msr module option `allow_writes` if it exists.

Smells like RedHat of some sort?

## marqanton | 2021-08-12T22:14:43+00:00
Thanks, It is CentOS. Let me try turning off secure boot. I will let you know.

## marqanton | 2021-08-12T22:32:13+00:00
It looks good now. Thanks for your help.

## Spudz76 | 2021-08-13T18:08:50+00:00
Good, that might be the first time it actually was because of Secure Boot, glad it was that easy.

## marqanton | 2021-08-13T19:00:24+00:00
Thanks

On Fri, Aug 13, 2021 at 2:09 PM Tony Butler ***@***.***>
wrote:

> Good, that might be the first time it actually was because of Secure Boot,
> glad it was that easy.
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/2534#issuecomment-898634320>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AMF46MHH77ZQ6ROJJAWS3CLT4VNTZANCNFSM5CBG3L7A>
> .
> Triage notifications on the go with GitHub Mobile for iOS
> <https://apps.apple.com/app/apple-store/id1477376905?ct=notification-email&mt=8&pt=524675>
> or Android
> <https://play.google.com/store/apps/details?id=com.github.android&utm_campaign=notification-email>
> .
>


# Action History
- Created by: marqanton | 2021-08-12T13:33:46+00:00
