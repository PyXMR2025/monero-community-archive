---
title: 'Compile for android '
source_url: https://github.com/xmrig/xmrig/issues/11
author: 0xAliNik
assignees: []
labels:
- enhancement
- arm
created_at: '2017-06-03T13:27:08+00:00'
updated_at: '2019-08-02T12:42:03+00:00'
type: issue
status: closed
closed_at: '2019-08-02T12:42:03+00:00'
---

# Original Description
Hi,
Is It possible to compile xmrig for android ?

Thanks a lot.

# Discussion History
## 0xAliNik | 2017-06-06T13:57:54+00:00
Any idea !?

## xmrig | 2017-06-06T16:03:01+00:00
No it not possible at this moment. Mining part heavy optimized for x86 SSE2 and AES-NI instructions. No ARM CPUs supported.

For curiosity what user interface should be? Some android interface + native part in APK file or something else, because now only console interface available.

## tsudmi | 2017-10-10T18:50:47+00:00
Is there in plans to support ARM CPUs or are there any updates on running the miner on Android?

## tsudmi | 2017-10-11T18:42:12+00:00
@xmrig ?

## xmrig | 2017-10-11T19:39:43+00:00
Plans https://github.com/xmrig/xmrig/issues/106 I added ARM to the list.
ARM would be nice, but it not scheduled at this moment.
Thank you.

## JuniorJPDJ | 2017-11-29T02:02:09+00:00
I successfully run it in Linux Deploy app on android, If someone here is able to compile it with android sdk, please, show me how :<

## talobin | 2017-12-04T01:12:44+00:00
@xmrig with this commit
https://github.com/xmrig/xmrig/commit/aa4f8b6fa78eb8331b5927ba5315b926ac75ce9c
Can we now compile for Android?
Could you give us some instruction to cross-build for Android?
Thank you so much

## cmorsucci | 2017-12-29T08:51:09+00:00
Need instruction to compile for android.. pls

## bs3vcenk | 2018-01-04T15:58:58+00:00
Closed the repo -- check out NanoBytes' Picaxe on the Play Store if you want to mine using your phone.

## cmorsucci | 2018-01-04T16:37:12+00:00
Thank you ! Could you provide the list of commands you launched in Termux to get this compiled version?

## bs3vcenk | 2018-01-04T17:29:31+00:00
> Could you provide the list of commands you launched in Termux to get this compiled version?

This version was compiled with the same commands above, but it's just a packaged in a .deb file (created using `termux-create-package`) with the binary inside.

## H3avyus3r | 2018-01-11T03:26:26+00:00
+1 32-bit, Appreciated!

## Holmgrenstefan | 2018-01-18T13:29:11+00:00
Works om Huawei p9plus not Sony Experia m2 as it is armv71

## bs3vcenk | 2018-01-19T15:27:45+00:00
Just to let you all know, someone made a reddit post with both the 32 and 64-bit versions [here](https://www.reddit.com/r/MoneroMining/comments/7qcu93/mining_on_android_64_bit_or_32_bitxmrig/).

## H3avyus3r | 2018-01-19T16:22:44+00:00
Thanks so much for that update!

On Jan 19, 2018 9:27 AM, "b3" <notifications@github.com> wrote:

> Just to let you all know, someone made a reddit post with both the 32 and
> 64-bit versions here
> <https://www.reddit.com/r/MoneroMining/comments/7qcu93/mining_on_android_64_bit_or_32_bitxmrig/>
> .
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/11#issuecomment-358997518>, or mute
> the thread
> <https://github.com/notifications/unsubscribe-auth/AeEdwtxMryE21cGAISBrzALmejKVWoJKks5tMLR1gaJpZM4NvFYy>
> .
>


## Patometro06 | 2018-03-08T02:50:44+00:00
Thanks a lot! I can run this fork on a Swissmobility Zeit 403 Black 32 bits ARM MTK6580M Quad Core 1.3 Ghz with 512 MB of RAM, all run on Android 5.1 .
[ * w * ]/')

Update: Confirmed, i can compile this fork on 32 bit ARM android device on Termux.

i have a second Z403 but with different 32 bit ARM processor a SC7731C quad core 1.3 Ghz processor.

and after compile and run in both devices all works at 100%.

NOTE: Only you can install Termux 0.60 on Android 5.0 +, on Android 4.2+ you can't install it.

# Action History
- Created by: 0xAliNik | 2017-06-03T13:27:08+00:00
- Closed at: 2019-08-02T12:42:03+00:00
