---
title: Illegal instruction
source_url: https://github.com/monero-project/monero/issues/6719
author: abyssal0
assignees: []
labels: []
created_at: '2020-07-22T01:58:16+00:00'
updated_at: '2020-07-22T03:47:44+00:00'
type: issue
status: closed
closed_at: '2020-07-22T03:47:44+00:00'
---

# Original Description
on Ubuntu 18.04.4 LTS

`cd monero`
`git checkout release-v0.16`
`make`

These operations were successful.
Run Monero with ./monerod failed

`./build/Linux/release-v0.16/release/bin/monerod`
`Illegal instruction`

What happened? What should I do?

# Discussion History
## abyssal0 | 2020-07-22T03:47:44+00:00
I deleted it and reinstalled it.Problem solved.

# Action History
- Created by: abyssal0 | 2020-07-22T01:58:16+00:00
- Closed at: 2020-07-22T03:47:44+00:00
