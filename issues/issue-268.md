---
title: Hashrate question
source_url: https://github.com/xmrig/xmrig/issues/268
author: ghost
assignees: []
labels: []
created_at: '2017-12-16T18:12:10+00:00'
updated_at: '2018-03-14T23:39:27+00:00'
type: issue
status: closed
closed_at: '2018-03-14T23:39:27+00:00'
---

# Original Description
Why may hashrate is not constantly at max ? 

speed 2.5s/60s/15m 109.6 132.6 129.3 H/s max: 161.6 H/s

# Discussion History
## ghost | 2017-12-16T20:44:16+00:00
I noticed this too, my hashrate is half of what I was getting previously back in March.

## xmrig | 2017-12-17T04:27:56+00:00
CPU hashrate highly depends of other cache intensive running apps. Video playback, browsing web, background updates, etc.
Thank you.

## ghost | 2017-12-17T10:33:04+00:00
@darthyvader  @xmrig  Thanks for your reply,
But I only use the computer for that this is really strange, I'll investigate on this

## ghost | 2017-12-17T19:01:13+00:00
that sounds  good my hashrate is just half of what it was on July same hw
same settings. bytecoin miner works as expected though. 1-1.2kh vs 400h/s
xmrig 28 threads

On Dec 17, 2017 4:33 AM, "BenBenz" <notifications@github.com> wrote:

> @darthyvader <https://github.com/darthyvader> @xmrig
> <https://github.com/xmrig> Thanks for your reply,
> But I only use the computer for that this is really strange, I'll
> investigate on this
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/268#issuecomment-352245917>, or mute
> the thread
> <https://github.com/notifications/unsubscribe-auth/Ag7-RZ4A_9gKBkYG16r291eXcT1I7pIqks5tBO3jgaJpZM4REaWv>
> .
>


## QwertyJack | 2017-12-18T09:22:38+00:00
You can setup a static difficulty, which will helps making the hashrate stable.

## Sgordon123 | 2017-12-20T12:47:02+00:00
Chechk PowerSave Settings  on your computer....

# Action History
- Created by: ghost | 2017-12-16T18:12:10+00:00
- Closed at: 2018-03-14T23:39:27+00:00
