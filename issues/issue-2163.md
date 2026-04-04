---
title: Background mining options not accepted
source_url: https://github.com/monero-project/monero/issues/2163
author: alejandorr
assignees: []
labels: []
created_at: '2017-07-10T11:33:11+00:00'
updated_at: '2017-08-07T15:48:48+00:00'
type: issue
status: closed
closed_at: '2017-07-26T13:33:08+00:00'
---

# Original Description
Two symptoms, not sure if the root problem is the same:

1) Issuing e.g. --bg-mining-idle-threshold 80 in the command line says that the value is not valid for the option.

2) Starting bg mining from the daemon console works (once the threshold is reached), but when requested from the command line, the idle threshold is never reported, and bg mining never actually starts.

Both tested in 0.10.3.1 and HEAD, ubuntu 16.04 x64

# Discussion History
## moneromooo-monero | 2017-07-12T10:24:25+00:00
https://github.com/monero-project/monero/pull/2169 fixes the first. It might fix the second, but I'm not sure what you did exactly, so if it doesn't, detail your steps.

## alejandorr | 2017-07-26T13:33:08+00:00
Confirming that options are now accepted, thanks. Still, bg mining is not working from command line, but I will open a separate issue that clarifies the problem.

# Action History
- Created by: alejandorr | 2017-07-10T11:33:11+00:00
- Closed at: 2017-07-26T13:33:08+00:00
