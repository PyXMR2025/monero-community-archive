---
title: API feature request
source_url: https://github.com/xmrig/xmrig/issues/2845
author: toxicroadkill
assignees: []
labels: []
created_at: '2021-12-30T02:06:43+00:00'
updated_at: '2021-12-30T02:42:16+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
could the following from the "/1/dmi" api be added to the "/2/summary" api

 "smbios": "?",
   "system": {
        "vendor": "?",
        "product": "?"
    },
    "board": {
        "vendor": "?",
        "product": "?"
    },

this would make things more logical since the summary reveals memory/etc already, why not have it identify the system, and board / etc, having the info in one place makes sense, should be a trivial matter to do, the main advantage would be for users with a **lot** of machines to keep the inventory of them/performance comparisons easier.

# Discussion History
## Spudz76 | 2021-12-30T02:28:30+00:00
Just query both and collate the info yourself.

DMI can be disabled and then it complicates what shows up in the summary rather than simply making the `dmi` endpoint nonexistent.

Also at some point the summary is no longer a summary if it shows literally every detail, right?

## toxicroadkill | 2021-12-30T02:42:15+00:00
is there a **complete** doc for the api calls for xmrig, a lot of them "page not finished", like json_rpg, and the like, a lot of missing information

summary i would assume, would be a summary, the /2/summary endpoint already says how much memory, what would be the harm on adding 3 more return params
if they were not available, return a empty string.

would save effort and aggravation calling 2 seperate endpoints

or make one "/2/detail", which does show everything, that probably would be a really good solution

> On Dec 29, 2021, at 8:28 PM, Tony Butler ***@***.***> wrote:
> 
> 
> Just query both and collate the info yourself.
> 
> DMI can be disabled and then it complicates what shows up in the summary rather than simply making the dmi endpoint nonexistent.
> 
> Also at some point the summary is no longer a summary if it shows literally every detail, right?
> 
> —
> Reply to this email directly, view it on GitHub <https://github.com/xmrig/xmrig/issues/2845#issuecomment-1002846087>, or unsubscribe <https://github.com/notifications/unsubscribe-auth/ASD5O3537IEWKVMB2HQCPKDUTO7VTANCNFSM5K65LVIA>.
> Triage notifications on the go with GitHub Mobile for iOS <https://apps.apple.com/app/apple-store/id1477376905?ct=notification-email&mt=8&pt=524675> or Android <https://play.google.com/store/apps/details?id=com.github.android&referrer=utm_campaign%3Dnotification-email%26utm_medium%3Demail%26utm_source%3Dgithub>. 
> You are receiving this because you authored the thread.
> 



# Action History
- Created by: toxicroadkill | 2021-12-30T02:06:43+00:00
