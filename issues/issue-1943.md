---
title: source code
source_url: https://github.com/xmrig/xmrig/issues/1943
author: wong-fi-hung
assignees: []
labels: []
created_at: '2020-11-11T18:18:20+00:00'
updated_at: '2021-04-12T14:35:11+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:35:11+00:00'
---

# Original Description
Why the source code can't be compiled on armv8 (Android)...?
What's wrong...?

# Discussion History
## SChernykh | 2020-11-12T08:34:21+00:00
What error do you get?

## AlexanderIreland | 2020-11-13T01:14:55+00:00
For arm8 systems I've generally had some success with the following cmake options:

`-DCMAKE_SYSTEM_PROCESSOR=arm -DWITH_RANDOMX=OFF -DARM_TARGET=8`

I haven't tried to run a build on arm7 or arm8 in the last 15-20 days or so with randomx on, but for the life of me I wasn't able to get it to work on arm7 or 8 target systems previously.

Hope this helps! - Alexander

## wong-fi-hung | 2020-11-13T06:15:16+00:00
my be add option conmand --xmrig-mode=light to run xmrig on arm v7 or arm v8 (Android) with small memories under 4 gb.
But, xmrig's work in fast mode on 5 to 8 gb ram memories.

# Action History
- Created by: wong-fi-hung | 2020-11-11T18:18:20+00:00
- Closed at: 2021-04-12T14:35:11+00:00
