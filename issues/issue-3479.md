---
title: How to make XMRIG rest for x time every x time?
source_url: https://github.com/xmrig/xmrig/issues/3479
author: Carlese33
assignees: []
labels: []
created_at: '2024-05-15T09:03:16+00:00'
updated_at: '2025-06-18T22:14:26+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:14:26+00:00'
---

# Original Description
This may be a silly question, and I'm sorry if it's already been answered somewhere. I've tried searching everywhere and haven't found a way to do it. 

I would like to know if there is a way to make XMRIG work at intervals in order to allow my computer to rest from time to time. I know that with pause-on-active I can make the computer rest when I am actively using it, but there are times when I spend a lot of time away from home and I would like to make the miner pause, for example, every 30 minutes for 5 minutes so that the temperature keeps regulated. 

Is this possible?

Thank you so much!

# Discussion History
## SChernykh | 2024-05-15T09:10:47+00:00
This is the quickest way to wear your PC components. Thermal cycling from hot to cold and back is the worst for electronics. The best is the stable temperature conditions - stable 100% load. Assuming that your cooling is good enough and nothing overheats, of course.

## Carlese33 | 2024-05-15T09:47:01+00:00
> This is the quickest way to wear your PC components. Thermal cycling from hot to cold and back is the worst for electronics. The best is the stable temperature conditions - stable 100% load. Assuming that your cooling is good enough and nothing overheats, of course.

Hey SCernykh. Thank you very much for your answer, I did not know that and I today learned something, so thanks! 

Anyways, just for curiosity (and in case I eventually spend days outside home): so there's not a way to do it? 

## geekwilliams | 2024-05-16T02:26:27+00:00
If you must, your better off implementing this yourself with windows task manager or cron or some script that handles it all for you. You could also use the xmrig http api to make calls via some script keeping track of time to tell xmrig to pause/continue etc. But as stated previously, it's not really a good idea if you're doing it to prolong the life of your rig. 

## Carlese33 | 2024-05-18T10:50:21+00:00
Okay, then I guess I will better try to use lower threads and keep it 24/7. My problem was that I sometimes spend days outside home, and never know when I will be back, but using 1 thread for example should allow me to be outside with zero worries. 

Thanks!! 

## geekwilliams | 2024-05-19T06:41:33+00:00
Using the same config you can set things to run at like 75% say, instead of max. Modern processors have the ability to throttle if there are thermal issues

Sent from my iSlippers


On May 18, 2024, at 4:50 AM, Carlese33 ***@***.***> wrote:

﻿

Okay, then I guess I will better try to use lower threads and keep it 24/7. My problem was that I sometimes spend days outside home, and never know when I will be back, but using 1 thread for example should allow me to be outside with zero worries.

Thanks!!

—
Reply to this email directly, view it on GitHub<https://github.com/xmrig/xmrig/issues/3479#issuecomment-2118776312>, or unsubscribe<https://github.com/notifications/unsubscribe-auth/AG7SNTLCTP27X67V5RSKKZTZC4XAFAVCNFSM6AAAAABHXXECT2VHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZDCMJYG43TMMZRGI>.
You are receiving this because you commented.Message ID: ***@***.***>


# Action History
- Created by: Carlese33 | 2024-05-15T09:03:16+00:00
- Closed at: 2025-06-18T22:14:26+00:00
