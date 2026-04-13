---
title: Confusing error log
source_url: https://github.com/seraphis-migration/monero/issues/315
author: j-berman
assignees: []
labels: []
created_at: '2026-04-13T01:52:02+00:00'
updated_at: '2026-04-13T01:52:02+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
When debugging using logs, I've gotten tripped up a couple times from [this error log](https://github.com/seraphis-migration/monero/blob/11a40647c839bc7bb772b77d57bed1185cf341f3/src/carrot_impl/address_device_hierarchies.cpp#L68-L69), uncertain if that's the cause of whatever bug I'm running into or not.

That can error for a legacy wallet every time because of [this](https://github.com/seraphis-migration/monero/blob/11a40647c839bc7bb772b77d57bed1185cf341f3/src/carrot_impl/address_utils.cpp#L88-L101).

Would be nice to not log that error in this instance.

I also think we (myself included) should probably aim to avoid exceptions for expected errors, and go with boolean returns instead (exceptions can break the program when not careful to manage them properly).

# Discussion History
# Action History
- Created by: j-berman | 2026-04-13T01:52:02+00:00
