---
title: XMRig server certificate verification failure
source_url: https://github.com/xmrig/xmrig/issues/2980
author: kamadom
assignees: []
labels: []
created_at: '2022-03-20T16:11:14+00:00'
updated_at: '2022-04-03T17:06:14+00:00'
type: issue
status: closed
closed_at: '2022-04-03T06:39:36+00:00'
---

# Original Description
**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
git clone https://github.com/xmrig/xmrig.git

Cloning into 'xmrig'...

fatal: unable to access 'https://github.com/xmrig/xmrig.git/': server certificate verification failed. CAfile: none CRLfile: none

**Expected behavior**
After cloning the XMRig repository from GITHUB, be able to install xmrig from source using cmake 

**Required data**
 - Miner log as text or screenshot (Not Applicable)
 - Config file or command line (without wallets) "git clone https://github.com/xmrig/xmrig.git"
 - OS: [e.g. Windows] "Both Ubuntu 20.04 and ARMv8 return same result"
 - For GPU related issues: information about GPUs and driver version. (Not Applicable)

**Additional context**
"Anyone have a workaround for the XMRig server certificate verification failure?"


# Discussion History
## Spudz76 | 2022-03-20T16:34:33+00:00
Works fine from here, was just renewed on the 14th.

## snipeTR | 2022-03-20T22:28:14+00:00
Check date, time or timezone

## kamadom | 2022-04-03T17:06:14+00:00
Thanks for the reply.  During that period, I found there was a problem with
my WAN feed, specifically the NTP service, that caused other issues due to
time synchronization problems.  That is fixed now.

Charles


On Sun, Mar 20, 2022 at 9:34 AM Tony Butler ***@***.***>
wrote:

> Works fine from here, was just renewed on the 14th.
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/2980#issuecomment-1073286830>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AHLSIFSPS65VQVBIA3R4EHTVA5HSHANCNFSM5RFWLRCA>
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
- Created by: kamadom | 2022-03-20T16:11:14+00:00
- Closed at: 2022-04-03T06:39:36+00:00
