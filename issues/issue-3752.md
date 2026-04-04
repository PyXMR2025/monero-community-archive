---
title: Couldn't Start Mining
source_url: https://github.com/monero-project/monero-gui/issues/3752
author: osakibill
assignees: []
labels: []
created_at: '2021-11-25T23:58:20+00:00'
updated_at: '2021-11-27T16:25:00+00:00'
type: issue
status: closed
closed_at: '2021-11-26T17:58:28+00:00'
---

# Original Description
Just installed monero-gui on windows 10. 

Wallet and Daemon are synchronized.

When I try to mine, I get a pop up error box that says " couldn't start mining"

Version is:
>>> version
[25/11/2021 23:52] 2021-11-25 23:52:05.789 I Monero 'Oxygen Orion' (v0.17.2.3-release) 
Error: The daemon software version is not available.
>>> update check
[25/11/2021 23:53] 2021-11-25 23:52:40.528 I Monero 'Oxygen Orion' (v0.17.2.3-release) 
No update available

Any ideas on what going on,,, or what I did wrong? :-/


# Discussion History
## osakibill | 2021-11-26T17:58:28+00:00
I am closing this issue until I know more about this. Just think I set it up incorrectly.

Thanks
Osakibill

## selsta | 2021-11-26T18:05:28+00:00
Could it be anti virus related?

## osakibill | 2021-11-26T18:28:58+00:00
Probably not. I did exclude the directories from my antivirus and I had no
error messages.

I think I did not have a connection to a node (?) or still trying to
download the chain.

So till I know about this I pulled my newbe issue. :-)


On Fri, Nov 26, 2021 at 6:05 PM selsta ***@***.***> wrote:

> Could it be anti virus related?
>
> —
> You are receiving this because you modified the open/close state.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero-gui/issues/3752#issuecomment-980238734>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AWVHJ5ESEE2LJ2KTWRCC22TUN7D7FANCNFSM5IZP5H5A>
> .
> Triage notifications on the go with GitHub Mobile for iOS
> <https://apps.apple.com/app/apple-store/id1477376905?ct=notification-email&mt=8&pt=524675>
> or Android
> <https://play.google.com/store/apps/details?id=com.github.android&referrer=utm_campaign%3Dnotification-email%26utm_medium%3Demail%26utm_source%3Dgithub>.
>
>


## selsta | 2021-11-27T16:25:00+00:00
Yes, mining is not possible if you are still syncing / don't have to full blockchain.

# Action History
- Created by: osakibill | 2021-11-25T23:58:20+00:00
- Closed at: 2021-11-26T17:58:28+00:00
