---
title: 'Windows build broken by #3170'
source_url: https://github.com/monero-project/monero/issues/3296
author: iDunk5400
assignees: []
labels: []
created_at: '2018-02-19T21:13:05+00:00'
updated_at: '2018-03-22T06:33:32+00:00'
type: issue
status: closed
closed_at: '2018-03-05T22:48:36+00:00'
---

# Original Description
Since #3170 was merged, building in MSYS2 fails like this:
[https://build.getmonero.org/builders/monero-static-win64/builds/3757/steps/compile/logs/stdio](https://build.getmonero.org/builders/monero-static-win64/builds/3757/steps/compile/logs/stdio)

I managed to make it build by substituting `command_line::has_arg` with `!command_line::is_not_defaulted` [here](https://github.com/monero-project/monero/blob/master/src/daemonizer/windows_daemonizer.inl#L114), but I think it's better the author fix any code or template issues properly. (@mrwhythat)

# Discussion History
## stoffu | 2018-02-26T08:18:01+00:00
#3318 

## iDunk5400 | 2018-02-26T10:06:15+00:00
#3318 does fix the build failure. Thanks.

## moneromooo-monero | 2018-03-05T22:34:09+00:00
+resolved

## rodentrabies | 2018-03-22T06:33:32+00:00
@stoffy, thanks for fixing this for me. Sorry I couldn't respond in time, as I don't have any Windows machines at hand.

# Action History
- Created by: iDunk5400 | 2018-02-19T21:13:05+00:00
- Closed at: 2018-03-05T22:48:36+00:00
