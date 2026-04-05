---
title: RTM mining on Linux static build 5.16.1 crashes - "Segmentation fault"
source_url: https://github.com/xmrig/xmrig/issues/2762
author: Pavlogal
assignees: []
labels: []
created_at: '2021-11-30T08:00:18+00:00'
updated_at: '2021-11-30T08:50:03+00:00'
type: issue
status: closed
closed_at: '2021-11-30T08:12:19+00:00'
---

# Original Description
Running Ubuntu 21.10 and Linux 5.15.5 kernel (so far had no issues with a this recent release)

Downloaded Linux static build 6.16.1 to get VAES optimizations for Zen 3. It failed every single time I tried to mine RTM with a message "Segmentation fault". XMR mining worked flawlessly though.

Switched from static to regular Linux build and now both RTM and XMR mining is working without issues. I don't know if static build has a bug or I'm missing something (probably this)

# Discussion History
## Pavlogal | 2021-11-30T08:12:19+00:00
saw that this is a duplicate issue, closing it myself so others don't have to

## SChernykh | 2021-11-30T08:50:03+00:00
> Switched from static to regular Linux build and now both RTM and XMR mining is working without issues

Regular Linux build doesn't have VAES because it's compiled with a very old GCC version. This bug is already fixed in the dev branch, next release will have the fix.

# Action History
- Created by: Pavlogal | 2021-11-30T08:00:18+00:00
- Closed at: 2021-11-30T08:12:19+00:00
