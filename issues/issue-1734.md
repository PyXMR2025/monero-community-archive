---
title: 'request: set_log default; show_log (display current log levels)'
source_url: https://github.com/monero-project/monero/issues/1734
author: voidzero
assignees: []
labels: []
created_at: '2017-02-15T03:35:28+00:00'
updated_at: '2017-10-02T19:54:23+00:00'
type: issue
status: closed
closed_at: '2017-10-02T19:54:23+00:00'
---

# Original Description
Upon startup, monerod shows the current loglevel:

`New log categories: *:WARNING,net*:FATAL,global:INFO,verify:FATAL,stacktrace:INFO`

If possible, it would be nice if we could restore this setting by use of `set_log default`.

Additionally, I'd like to request a `show_log` command that prints the current loglevel to the screen. Example:

<pre>show_log
Current log level: *:WARNING,net*:FATAL,global:INFO,verify:FATAL,stacktrace:INFO</pre>

This allows to see what the current log level is without changing it.

# Discussion History
## moneromooo-monero | 2017-02-15T09:46:49+00:00
Default is 0, which maps to what you are seeing.
I might add some more helpers though.

## voidzero | 2017-02-15T19:32:58+00:00
Ah yes. I missed the obvious. Glad to hear about maybe adding helpers.

## moneromooo-monero | 2017-09-22T17:09:29+00:00
https://github.com/monero-project/monero/pull/2512

## moneromooo-monero | 2017-10-02T19:29:40+00:00
+resolved

# Action History
- Created by: voidzero | 2017-02-15T03:35:28+00:00
- Closed at: 2017-10-02T19:54:23+00:00
