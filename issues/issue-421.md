---
title: Opening multiple instances
source_url: https://github.com/monero-project/monero-gui/issues/421
author: MoroccanMalinois
assignees: []
labels:
- bug
- resolved
created_at: '2017-01-20T01:41:05+00:00'
updated_at: '2018-11-11T16:18:24+00:00'
type: issue
status: closed
closed_at: '2018-11-11T16:18:24+00:00'
---

# Original Description
The GUI does not prevent from opening multple instances with the same wallet


# Discussion History
## fresheneesz | 2017-05-24T04:54:12+00:00
And why would it? I'm currently doing that to test. If you don't want more than one instance, why are you running the executable more than once?

## MoroccanMalinois | 2017-05-24T14:35:31+00:00
    And why would it?

Because it is likely that someone opening the same wallet twice is doing it by mistake.

    why are you running the executable more than once?

To open different wallets
 

## fresheneesz | 2017-05-24T19:39:00+00:00
If you open a second instance by mistake the close it ffs. I would imagine the more likely scenario is that you meant to do it. 

"To open different wallets"
And how do you expect to open 2 different wallets at once without allowing multiple instances?

Until tabs gets implemented https://github.com/monero-project/monero-core/issues/394 opening multiple instances shouldn't be prevented.

## MoroccanMalinois | 2017-05-24T22:26:04+00:00
    If you open a second instance by mistake the close it **ffs**.

Thank you so much @fresheneesz. I never thought about it. You saved my day !

    And how do you expect to open 2 different wallets at once without allowing multiple instances?

... multple instances **with the same wallet**

## dEBRUYNE-1 | 2017-08-09T14:26:56+00:00
This might be a bug as it could cause issues with the wallet cache.

+bug

## xiphon | 2018-11-11T15:43:15+00:00
The issue has been fixed at some point. The current release 13.0.4 correctly handles the case, preventing you from opening the same wallet file multiple times.

## dEBRUYNE-1 | 2018-11-11T16:00:17+00:00
+resolved

# Action History
- Created by: MoroccanMalinois | 2017-01-20T01:41:05+00:00
- Closed at: 2018-11-11T16:18:24+00:00
