---
title: '"monero-wallet-gui.exe" not showing correct current status of connection with
  remote node'
source_url: https://github.com/monero-project/monero-gui/issues/2352
author: greatalazar
assignees: []
labels: []
created_at: '2019-08-16T10:27:05+00:00'
updated_at: '2019-08-19T10:09:01+00:00'
type: issue
status: closed
closed_at: '2019-08-19T10:09:01+00:00'
---

# Original Description
While Monero GUI shows disconnected but it connected to a node.
While Monero GUI shows synchronizing but there is no connection from "monero-wallet-gui.exe"

Just a tip, the status label is too vague too tell what the hell is going on

Tools Used:
_TCPView_ (www.sysinternals.com)
_CurrPorts_ (www.nirsoft.net)

# Discussion History
## ghost | 2019-08-16T19:51:20+00:00
> While Monero GUI shows synchronizing but there is no connection from "monero-wallet-gui.exe"

**IMO** "monerod.exe" is doing the network communication - not "monero-wallet-gui.exe". Therefore, this could be ok. 
 
> Just a tip, the status label is too vague too tell what the hell is going on

You're right. #2304 is trying to improve this.

## greatalazar | 2019-08-19T07:15:59+00:00
If you are using remote node, "monerod.exe" doesn't even need to start so connections are made from "monero-wallet-gui.exe"

## ghost | 2019-08-19T09:50:59+00:00
You are right, the wording is wrong as pointed out in #2304 number 4. You may consider closing this issue.

## greatalazar | 2019-08-19T10:09:00+00:00
#2304 is much detailed issue so I'm closing this one

# Action History
- Created by: greatalazar | 2019-08-16T10:27:05+00:00
- Closed at: 2019-08-19T10:09:01+00:00
