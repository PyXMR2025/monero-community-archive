---
title: '[SUGGESTION] Add support for dinamically chage which threads are working'
source_url: https://github.com/xmrig/xmrig/issues/2109
author: ghost
assignees: []
labels: []
created_at: '2021-02-17T10:23:12+00:00'
updated_at: '2021-02-23T17:27:56+00:00'
type: issue
status: closed
closed_at: '2021-02-23T17:27:56+00:00'
---

# Original Description
As in title, I think using same threads/cores all the time would damage CPU/s faster than changing dinamically them.

My original idea was based on changing it every tot time, but then I have thinkd it would be better to change on every new work, in order to maintain threads occupied for the time needed on complete a work.

Do you think this could be a good idea?

# Discussion History
## Spudz76 | 2021-02-18T21:31:43+00:00
Silicon does not wear from usage.

If anything, moving the hot spot (active cores) around the die would damage it faster than constant heat in the same place due to thermal cycling.

# Action History
- Created by: ghost | 2021-02-17T10:23:12+00:00
- Closed at: 2021-02-23T17:27:56+00:00
