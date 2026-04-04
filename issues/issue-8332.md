---
title: Tweaks for building on M1 Mac with Homebrew
source_url: https://github.com/monero-project/monero/issues/8332
author: hyc
assignees: []
labels: []
created_at: '2022-05-15T17:51:45+00:00'
updated_at: '2022-05-29T15:28:48+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
The libunbound.a static library in homebrew depends on two other libraries.

[dif.txt](https://github.com/monero-project/monero/files/8695602/dif.txt)

I haven't made this into a PR because I'd prefer to see a more generalized solution than this hack. But at least it works and builds to completion.

# Discussion History
# Action History
- Created by: hyc | 2022-05-15T17:51:45+00:00
