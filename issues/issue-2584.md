---
title: 'Suggestion: warning/reminder if paused for too long'
source_url: https://github.com/xmrig/xmrig/issues/2584
author: Kelvets
assignees: []
labels: []
created_at: '2021-09-17T02:52:34+00:00'
updated_at: '2025-06-16T20:53:57+00:00'
type: issue
status: closed
closed_at: '2025-06-16T20:53:57+00:00'
---

# Original Description
It happens embarrasingly frequently that I pause XMRig in order to go play a game and only realize I forgot to unpause it a day or so later, having wasted all that potential mining time. It would be very neat if XMRig could be configured to flash in the taskbar if it has been paused for an user-defined amount of hours.

# Discussion History
## Spudz76 | 2021-09-17T13:30:09+00:00
xmrig is a console app and has no control over its own taskbar appearance.

Forget to unpause a couple more times, and you'll never forget again. :)

## Fyrhus | 2021-09-17T13:35:31+00:00
I have been in a similar situation. My solution is to never pause manually but let XMRig pause automatically on user activity.

## Kelvets | 2021-09-18T14:17:29+00:00
@Fyrhus that won't do, wouldn't it pause with ANY user activity? I only
want it to pause when gaming; XMRig running when I'm doing anything else is
fine. It would need to detect applications that use a lot of CPU and only
pause with those, not simply e.g. when it detects mouse movement.

On Fri, Sep 17, 2021, 10:35 Fyrhus ***@***.***> wrote:

> I have been in a similar situation. My solution is to never pause manually
> but let XMRig pause automatically on user activity.
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/2584#issuecomment-921802510>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AA473EKIOZ4625B6WVKMIYTUCM725ANCNFSM5EGBLD7A>
> .
> Triage notifications on the go with GitHub Mobile for iOS
> <https://apps.apple.com/app/apple-store/id1477376905?ct=notification-email&mt=8&pt=524675>
> or Android
> <https://play.google.com/store/apps/details?id=com.github.android&referrer=utm_campaign%3Dnotification-email%26utm_medium%3Demail%26utm_source%3Dgithub>.
>
>


## Spudz76 | 2021-09-18T16:54:00+00:00
What I love is that it still switches algos while paused, which uses CPU for init of the algo, and has gotten me killed in games before.  It would be super neat if it also ignored pool messages while paused.

And yes that feature pauses on any activity, the same Windows function a screensaver uses.

And wouldn't having a timeout just unpause during the game if you happened to still be playing for longer than the unpause delay?

I still think this is user error and you could quite easily build a reflex to always unpause, like I did forever, it became just a part of quitting the game just like pausing before launch is automatic reflex (do you ever forget to pause it before games? or is that automatic reflex... same thing on the exit/unpause procedure it should just become automatic)

## Kelvets | 2021-09-18T19:10:13+00:00
@Tony I've been using XMRig for months and the reflex still hasn't kicked
in. And yes, I forget to pause it before opening games often, but that's
easy to notice because the game gets laggy. Forgetting to turn it back on
after the game finishes is very hard to notice.

Em sáb., 18 de set. de 2021 às 13:54, Tony Butler ***@***.***>
escreveu:

> What I love is that it still switches algos while paused, which uses CPU
> for init of the algo, and has gotten me killed in games before. It would be
> super neat if it also ignored pool messages while paused.
>
> And yes that feature pauses on any activity, the same Windows function a
> screensaver uses.
>
> And wouldn't having a timeout just unpause during the game if you happened
> to still be playing for longer than the unpause delay?
>
> I still think this is user error and you could quite easily build a reflex
> to always unpause, like I did forever, it became just a part of quitting
> the game just like pausing before launch is automatic reflex (do you ever
> forget to pause it before games? or is that automatic reflex... same thing
> on the exit/unpause procedure it should just become automatic)
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/2584#issuecomment-922339094>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AA473EPFLP3WKN4YCK2432LUCS73HANCNFSM5EGBLD7A>
> .
> Triage notifications on the go with GitHub Mobile for iOS
> <https://apps.apple.com/app/apple-store/id1477376905?ct=notification-email&mt=8&pt=524675>
> or Android
> <https://play.google.com/store/apps/details?id=com.github.android&referrer=utm_campaign%3Dnotification-email%26utm_medium%3Demail%26utm_source%3Dgithub>.
>
>


-- 
Érico


## SChernykh | 2021-09-20T15:31:16+00:00
https://github.com/xmrig/xmrig/pull/2594

# Action History
- Created by: Kelvets | 2021-09-17T02:52:34+00:00
- Closed at: 2025-06-16T20:53:57+00:00
