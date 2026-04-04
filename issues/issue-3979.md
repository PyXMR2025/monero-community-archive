---
title: Submodules not being initialized for Apple M1 CPUs
source_url: https://github.com/monero-project/monero-gui/issues/3979
author: ghost
assignees: []
labels: []
created_at: '2022-07-21T16:57:38+00:00'
updated_at: '2022-07-21T16:59:45+00:00'
type: issue
status: closed
closed_at: '2022-07-21T16:59:30+00:00'
---

# Original Description
If I `git clone --recursive https://github.com/monero-project/monero-gui.git` it works fine.

But if I omit the `--recursive` flag and instead run `git submodule init && git submodule update` in the main directory after simply cloning the repo (non-recursively) it only pulls in two of the submodules (external/quirc and monero), and not the entire set.

Is this a real issue or should I close this?

# Discussion History
## selsta | 2022-07-21T16:59:30+00:00
It's just how git works. You can use

```
git submodule update --init --recursive
```

to do everything in one command.

## ghost | 2022-07-21T16:59:45+00:00
Ok good to know

# Action History
- Created by: ghost | 2022-07-21T16:57:38+00:00
- Closed at: 2022-07-21T16:59:30+00:00
