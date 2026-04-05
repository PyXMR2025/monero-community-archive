---
title: How to put pool information inside xmrig when compile in v6.12
source_url: https://github.com/xmrig/xmrig/issues/2365
author: xJuniorProgrammer
assignees: []
labels: []
created_at: '2021-05-10T08:08:00+00:00'
updated_at: '2021-05-13T20:32:20+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hello
How to put necessary parameters(like pool & wallet info and ...) inside xmrig, and remove config.json requirement in last version 6.12.1 , when build?
I dont want to show wallet & pool info in task manager in command line column for xmrig process.
Thanks.

# Discussion History
## gamethrower | 2021-05-10T16:21:59+00:00
I don't think there is a way other than modifying the code and compiling it yourself.

## Spudz76 | 2021-05-10T17:47:04+00:00
The feature is documented where it was added:
https://github.com/xmrig/xmrig/issues/957#issuecomment-468890667

## xJuniorProgrammer | 2021-05-13T20:32:20+00:00
Hello,
I want force to use embedded config even if config.json is exist, i checked #1152 (comment) , but it's not worked.

# Action History
- Created by: xJuniorProgrammer | 2021-05-10T08:08:00+00:00
