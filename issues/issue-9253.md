---
title: block-notify seems not working
source_url: https://github.com/monero-project/monero/issues/9253
author: SnAFKe
assignees: []
labels:
- question
- low priority
- discussion
created_at: '2024-03-15T02:33:02+00:00'
updated_at: '2024-03-22T02:56:22+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I'm using command line to start monero with --block-notify '/bin/bash /home/user/block_notify.sh'

I want to switch to monero config file but with block-notify seems not working

```
block-notify='/bin/bash /home/user/notify.sh'
```

When i start monero in the logs show this.

```
ffff858c4010	WARNING	notify	src/common/notify.cpp:55	A notification spec contains a quote or backslash: note that these are handled verbatim, which may not be the intent
ffff858c4010	ERROR	notify	src/common/notify.cpp:57	File not found: '/bin/bash
ffff858c4010	ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:651	Failed to parse block notify spec: File not found: '/bin/bash
```

**Edit: Seems error is gone if i remove quote (not sure if will work). Now is not necessary to add quote or i miss something.**

What can I do to run a script when block found via config file ?

Thanks

# Discussion History
## moneromooo-monero | 2024-03-15T08:42:54+00:00
This file is boost format.
https://www.boost.org/doc/libs/1_84_0/doc/html/program_options/overview.html#id-1.3.30.5.10
Unfortunately, the documentation doesn't specify how quoting is handled, but https://github.com/boostorg/program_options/blob/develop/src/config_file.cpp, lines 103-119, suggests that no quoting is done (unless there is a post process step somewhere).
Monero could perform some interpretation, but that opens the usual can of worms. So removing the quote *should* work.

# Action History
- Created by: SnAFKe | 2024-03-15T02:33:02+00:00
