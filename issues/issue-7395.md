---
title: Code styling and indentation
source_url: https://github.com/monero-project/monero/issues/7395
author: stnby
assignees: []
labels: []
created_at: '2021-02-22T15:54:14+00:00'
updated_at: '2022-02-19T18:53:40+00:00'
type: issue
status: closed
closed_at: '2022-02-19T18:53:40+00:00'
---

# Original Description
I honestly do not know why and how someone allowed this to happen but the code base is literally so uneven that I have seen enough random indentation (*2 spaces seriously, functions in the same source file having multiple different styles?*).

I think enforcing [Linux kernel coding stye](https://www.kernel.org/doc/html/latest/process/coding-style.html) or some alternative as the code is C++ after all. I think this would greatly increase codes readability.

# Discussion History
## moneromooo-monero | 2021-02-23T12:54:03+00:00
No reindent spam please.

## xanoni | 2021-08-16T03:48:15+00:00
Some projects care, others don't. Seems this project doesn't ;-)

Off topic, but I think tickets should be closed faster. I see a lot of very outdated or irrelevant tickets.

## selsta | 2022-02-19T18:53:40+00:00
Monero forked from a project that already had messy indentation and we didn't want to auto format the whole project as it spams the git history.

# Action History
- Created by: stnby | 2021-02-22T15:54:14+00:00
- Closed at: 2022-02-19T18:53:40+00:00
