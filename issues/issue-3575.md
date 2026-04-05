---
title: Why do xmrig phone home so often.
source_url: https://github.com/xmrig/xmrig/issues/3575
author: db00t
assignees: []
labels: []
created_at: '2024-10-30T18:00:45+00:00'
updated_at: '2025-06-16T19:32:37+00:00'
type: issue
status: closed
closed_at: '2025-06-16T19:32:37+00:00'
---

# Original Description
Every 10. second xmrig tries to phone home to donate.v2.xmrig.com or donate.ssl.xmrig.com.
Why isn't there an option to turn off this kind of behaviour.

# Discussion History
## geekwilliams | 2024-10-30T18:34:02+00:00
There is.  In donate.h change kDefaultDonateLevel and kMinimumDonateLevel to 0.  

If you modify donate.h please consider making a one-off donation instead to support the development of xmrig.  Details are in the comments within donate.h

# Action History
- Created by: db00t | 2024-10-30T18:00:45+00:00
- Closed at: 2025-06-16T19:32:37+00:00
