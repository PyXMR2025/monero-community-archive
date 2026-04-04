---
title: 'Dark theme: Settings: If using a remote node, the ''Log level'' section is
  redundant and shouldn''t be visible'
source_url: https://github.com/monero-project/monero-gui/issues/1257
author: tficharmers
assignees: []
labels:
- enhancement
- invalid
created_at: '2018-04-04T11:51:24+00:00'
updated_at: '2018-04-05T20:01:15+00:00'
type: issue
status: closed
closed_at: '2018-04-05T20:01:15+00:00'
---

# Original Description
If using a remote node, the 'Log level' section is redundant and shouldn't be visible.

# Discussion History
## sanderfoobar | 2018-04-04T12:08:34+00:00
+enhancement

## sanderfoobar | 2018-04-05T10:28:40+00:00
Log Level section actually implies to the GUI log, not the daemon log.

The daemon log is under `Settings->Manage Daemon->Show Status` which is hidden when using a remote node.

Argument could be made to communicate this more clearly to the user.

## sanderfoobar | 2018-04-05T10:43:44+00:00
+invalid

## tficharmers | 2018-04-05T12:00:45+00:00
> Argument could be made to communicate this more clearly to the user.

Agreed. I'll look into that.


# Action History
- Created by: tficharmers | 2018-04-04T11:51:24+00:00
- Closed at: 2018-04-05T20:01:15+00:00
