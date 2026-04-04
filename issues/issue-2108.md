---
title: GUI Will Not Quit Upon Exit, Daemon Does (Latest Master on OS X)
source_url: https://github.com/monero-project/monero-gui/issues/2108
author: breadsax
assignees: []
labels:
- duplicate
created_at: '2019-04-24T02:10:21+00:00'
updated_at: '2019-04-24T12:09:38+00:00'
type: issue
status: closed
closed_at: '2019-04-24T12:09:38+00:00'
---

# Original Description
I compiled from Master just now on Mac OS X High Sierra and the build went well. When I exit the GUI from any method it prompts to stop the daemon as expected, the daemon stops normally, but the GUI remains running. It will close only with a Force Quit.

# Discussion History
## sanderfoobar | 2019-04-24T03:46:18+00:00
What Qt version are you using?

## sanderfoobar | 2019-04-24T03:47:39+00:00
Possible duplicate of #2033

## breadsax | 2019-04-24T04:00:01+00:00
brew install qt5. Does seem to be a duplicate issue across OSs. Mac OS X is also native host and not on a VM

## selsta | 2019-04-24T11:57:47+00:00
`brew install qt5` installs Qt 5.12.2.

#2033

+duplicate

# Action History
- Created by: breadsax | 2019-04-24T02:10:21+00:00
- Closed at: 2019-04-24T12:09:38+00:00
