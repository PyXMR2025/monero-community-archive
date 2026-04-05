---
title: Windows console colors don't work
source_url: https://github.com/xmrig/xmrig/issues/1057
author: Spudz76
assignees: []
labels:
- bug
- review later
created_at: '2019-07-09T20:25:55+00:00'
updated_at: '2021-04-18T06:20:25+00:00'
type: issue
status: closed
closed_at: '2021-04-18T06:20:25+00:00'
---

# Original Description
They do work if you use `--config` mode and edit the current running config file to turn color back on...

...which led to patches ignoring any tty_init return values on Windows (which makes color work normally)...

PR #1055 and PR #1056 

# Discussion History
## Spudz76 | 2019-07-09T20:28:30+00:00
See Also: [xmrig-nvidia issue #196](https://github.com/xmrig/xmrig-nvidia/issues/196)

## xmrig | 2021-04-12T16:00:22+00:00
Is this issue still actual?
Thank you.

## Spudz76 | 2021-04-15T22:58:27+00:00
I still run this patch on my builds, will try without it and see if the problem still exists.  Win7 may have something to do with it (probably works fine either way with Win10) and I run inside the normal good old cmd.exe shell (not powershell or etc).

## Spudz76 | 2021-04-18T06:20:25+00:00
Must have been upstream bug in an older version of libuv, it works properly without this now.  Closing...

# Action History
- Created by: Spudz76 | 2019-07-09T20:25:55+00:00
- Closed at: 2021-04-18T06:20:25+00:00
