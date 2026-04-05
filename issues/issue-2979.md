---
title: Clang-13 error
source_url: https://github.com/xmrig/xmrig/issues/2979
author: Novjack
assignees: []
labels:
- arm
created_at: '2022-03-20T08:16:11+00:00'
updated_at: '2022-04-03T07:50:28+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**clang-13 shows warning**
During executing "make" too many errors emitted
![20220320_160508](https://user-images.githubusercontent.com/101918064/159153985-8ac3d8f4-f78c-4f4b-9d1e-c4731365ba08.jpg)
![20220320_160522](https://user-images.githubusercontent.com/101918064/159153987-b8b83865-e686-4308-ab22-4976a2d0fd2a.jpg)
![20220320_160555](https://user-images.githubusercontent.com/101918064/159153991-9e6e0096-92aa-4485-a756-e180627dfa01.jpg)



# Discussion History
## Spudz76 | 2022-03-20T16:37:20+00:00
How did you set compiler(s)?

Should be like:
```
CC=/usr/bin/clang-13 CXX=/usr/bin/clang++-13 cmake ..
```

## Novjack | 2022-03-20T23:28:26+00:00
Hi,
Thanks for the response and I am not a programmer and I'm just following
the instruction step by step. So far my mobile phone working good for the
first time attempt but in my android tv box i did the same procedure but
and executing make does error shows.
Can you please share the link procedure for Android tv box. Thanks

Br
Novem

On Mon, Mar 21, 2022, 12:37 AM Tony Butler, ***@***.***>
wrote:

> How did you set compiler(s)?
>
> Should be like:
>
> CC=/usr/bin/clang-13 CXX=/usr/bin/clang++-13 cmake ..
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/2979#issuecomment-1073287256>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AYJSK4HSZVZTCZIDHC6HQ3TVA5H4VANCNFSM5RFFQ25Q>
> .
> Triage notifications on the go with GitHub Mobile for iOS
> <https://apps.apple.com/app/apple-store/id1477376905?ct=notification-email&mt=8&pt=524675>
> or Android
> <https://play.google.com/store/apps/details?id=com.github.android&referrer=utm_campaign%3Dnotification-email%26utm_medium%3Demail%26utm_source%3Dgithub>.
>
> You are receiving this because you authored the thread.Message ID:
> ***@***.***>
>


# Action History
- Created by: Novjack | 2022-03-20T08:16:11+00:00
