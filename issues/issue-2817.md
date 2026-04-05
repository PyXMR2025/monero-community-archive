---
title: cl_build_program_failure when calling clbuild program
source_url: https://github.com/xmrig/xmrig/issues/2817
author: Tetsu13
assignees: []
labels: []
created_at: '2021-12-16T16:52:05+00:00'
updated_at: '2021-12-24T15:36:03+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
i tried to mine using my GPU (radeon rx 550 that is) and this happen, i'm doing this on linux. CPU mining is fine btw, what should i do?
i'm new in this game, if you want any more info just tell me, i don't know what to attach other than this screenshot.
![image](https://user-images.githubusercontent.com/95771535/146414186-6f6ee669-d817-4c75-af5f-8089bae74a45.png)


# Discussion History
## Spudz76 | 2021-12-16T17:05:45+00:00
Probably newer than 21.40 is broken, I personally don't go beyond 20.40.

## Tetsu13 | 2021-12-17T01:16:34+00:00
i'm using arch linux and it's currently unsupported by radeon, i'll maybe use my gpu to mine anything else


## Spudz76 | 2021-12-17T02:56:36+00:00
"Unsupported" is relative.  It works fine I'm sure.

## Deep0310 | 2021-12-17T04:40:33+00:00
heii dog animals stop message to me woiii😠

Pada tanggal Jum, 17 Des 2021 09.57, Tony Butler ***@***.***>
menulis:

> "Unsupported" is relative. It works fine I'm sure.
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/2817#issuecomment-996394991>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AU22PXUKT4Q2XFNPJZ7KAWTURKRIJANCNFSM5KGZOBJA>
> .
> Triage notifications on the go with GitHub Mobile for iOS
> <https://apps.apple.com/app/apple-store/id1477376905?ct=notification-email&mt=8&pt=524675>
> or Android
> <https://play.google.com/store/apps/details?id=com.github.android&referrer=utm_campaign%3Dnotification-email%26utm_medium%3Demail%26utm_source%3Dgithub>.
>
> You are receiving this because you are subscribed to this thread.Message
> ID: ***@***.***>
>


## ghost | 2021-12-24T15:35:02+00:00
Did you try the gcn_asm tweak?

Example:
`"opencl": { "enabled":true, "loader":"Your_Path_Here", "adl":true, "cache":false, "platform":"AMD", "rx": [{ "intensity":<<See what is best for you>>, "worksize":<<See what is best for you>>, "gcn_asm":false, "index":0}, { "intensity":<<See what is best for you>>, "worksize":<<See what is best for you>>, "gcn_asm":false, "index":1} ]}`

# Action History
- Created by: Tetsu13 | 2021-12-16T16:52:05+00:00
