---
title: Add Mod question/request
source_url: https://github.com/xmrig/xmrig/issues/411
author: Zelecktor
assignees: []
labels: []
created_at: '2018-02-22T23:51:33+00:00'
updated_at: '2018-02-26T02:39:41+00:00'
type: issue
status: closed
closed_at: '2018-02-26T02:39:41+00:00'
---

# Original Description
Something interesting is that i found a mod to manage and monitoring miners/workers with an easy configuration server.

See this proyect
https://github.com/Bendr0id/xmrigCC

The only bad is that it uses two .exes files and have unnesesary addons. I would like have separates things. The mining software for one side (just only the original xmrig.exe) and the server exe (or file for linux) in another side.

# Discussion History
## MarQuisKnox | 2018-02-24T08:22:28+00:00
xmrigCC already has an independent binaries for the client & server. I don't understand your question.

## Zelecktor | 2018-02-24T22:11:43+00:00
To explain in simple words, it has 3 files, daemon (client), miner and server.
Server is independant. (its ok)

The miner is dependant of daemon (client), without daemon, the miner doesnt run. In summary both files (two .exe files on windows) must be together. On this case daemon is responsible to interact (send/receive) server orders.
My question is if it is possible to make only one file (client+miner) that can interact with the server but also mine. Just imagine xmrig running and monitoring with the CC server.

## MarQuisKnox | 2018-02-25T06:34:49+00:00
Better to ask in the XMRigCC project, since it is a fork & not directly compatible w/ the original XMRig:  https://github.com/Bendr0id/xmrigCC/issues/new

Also, maybe there's a good reason why this design was implemented. 

Simply ask on the XMRigCC issue tracker. 
@Bendr0id normally responds promptly.

# Action History
- Created by: Zelecktor | 2018-02-22T23:51:33+00:00
- Closed at: 2018-02-26T02:39:41+00:00
