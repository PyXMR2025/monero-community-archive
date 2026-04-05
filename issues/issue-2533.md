---
title: how to limit the manning on the processor to 25 percent?
source_url: https://github.com/xmrig/xmrig/issues/2533
author: sidex84
assignees: []
labels: []
created_at: '2021-08-12T05:17:45+00:00'
updated_at: '2021-08-17T23:28:28+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior.

**Expected behavior**
A clear and concise description of what you expected to happen.

**Required data**
 - Miner log as text or screenshot
 - Config file or command line (without wallets)
 - OS: [e.g. Windows]
 - For GPU related issues: information about GPUs and driver version.

**Additional context**
Add any other context about the problem here.


# Discussion History
## freakovision | 2021-08-14T10:48:16+00:00
`--cpu-max-threads-hint=25` or specify number of logical process using `--threads=N`



## sidex84 | 2021-08-15T08:56:30+00:00
Will the --max-cpu-usage 25 parameter work?

## freakovision | 2021-08-17T19:28:50+00:00
I believe it's deprecated.

## Spudz76 | 2021-08-17T23:27:16+00:00
It works but only if you don't have any thread-definitions in the config.json

Everything is a hint and if there is already a definition, there is no need for the hints, because initial config is not executed.

Also using`-t` or `--threads` only makes a `"*"` definition which means every algo will run that many threads (zero automatic sizing) which is not ideal either.

# Action History
- Created by: sidex84 | 2021-08-12T05:17:45+00:00
