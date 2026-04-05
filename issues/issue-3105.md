---
title: '[suggestion] PID files'
source_url: https://github.com/xmrig/xmrig/issues/3105
author: JacksonChen666
assignees: []
labels: []
created_at: '2022-08-07T22:59:26+00:00'
updated_at: '2025-06-18T22:53:34+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:53:34+00:00'
---

# Original Description
given that PR #2616 makes literally no sense (like, those 2 commits aren't even related to the PR or the creator) and a PID file option still isn't present (or found anywhere), i'm making this issue for the suggestion of PID files. it should be a file is written to a specific place (maybe provided in the command line arguments) containing the PID for xmrig.

# Discussion History
## snipeTR | 2022-08-07T23:43:37+00:00
https://stackoverflow.com/questions/9486960/how-to-get-pid-of-process-just-started-from-within-a-batch-file

## JacksonChen666 | 2022-08-08T10:59:23+00:00
i don't use windows. i'm asking for the feature for use in openrc and running xmrig in the background.


## snipeTR | 2022-08-08T15:24:38+00:00
https://gist.github.com/jirutka/5cf0e731dbc39a3a6fff0c6e1a2c2510

## Spudz76 | 2022-08-08T15:29:25+00:00
All init systems track PIDs of the things they launched without any support of the apps themselves.  There is no need for this useless feature.

# Action History
- Created by: JacksonChen666 | 2022-08-07T22:59:26+00:00
- Closed at: 2025-06-18T22:53:34+00:00
