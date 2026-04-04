---
title: Inactivity lock seems too strict
source_url: https://github.com/monero-project/monero/issues/6043
author: SomaticFanatic
assignees: []
labels: []
created_at: '2019-10-27T17:56:48+00:00'
updated_at: '2019-11-01T21:44:25+00:00'
type: issue
status: closed
closed_at: '2019-11-01T21:44:25+00:00'
---

# Original Description
I can't even finish reading the list of commands inside the help command without my CLI wallet locking me out with the cow due to inactivity. Can we make the lock time a little less strict, or better yet, have an option to turn it off completely in the "set" command?

# Discussion History
## moneromooo-monero | 2019-10-27T19:49:05+00:00
It's a minute and a half by default. That seems fairly long. Is yours shorter ? You can disable it by setting the timeout to 0 in the settings.

## SomaticFanatic | 2019-10-29T16:40:15+00:00
90 seconds seems too strict to me. I suppose this is a subjective measurement. But I would prefer it be closer to 3 minutes by default.

## ndorf | 2019-10-29T17:16:30+00:00
I also found the 90 second timeout annoying, but I think it's an appropriate default nonetheless. The default should err on the side of safety, and it's only a minor inconvenience to type `set inactivity-timeout 180` or even 0 if you want it completely off.

Perhaps the lock message should include a short blurb like "You can configure this locking behavior, type `help set` for more info?"

## moneromooo-monero | 2019-10-29T17:49:05+00:00
Good idea.

https://github.com/monero-project/monero/pull/6058

## SomaticFanatic | 2019-11-01T00:15:32+00:00
`inactivity-timeout` is not listed in the `help set` menu

## moneromooo-monero | 2019-11-01T15:43:53+00:00
https://github.com/monero-project/monero/pull/6076

# Action History
- Created by: SomaticFanatic | 2019-10-27T17:56:48+00:00
- Closed at: 2019-11-01T21:44:25+00:00
