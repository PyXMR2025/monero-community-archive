---
title: Cannot connect to daemon
source_url: https://github.com/monero-project/monero-gui/issues/848
author: ckellingc
assignees: []
labels:
- resolved
created_at: '2017-09-03T01:54:25+00:00'
updated_at: '2017-12-13T11:54:15+00:00'
type: issue
status: closed
closed_at: '2017-12-13T11:54:15+00:00'
---

# Original Description

2017-09-02 20:51:52.842	33508	INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
2017-09-02 20:51:53.845	33508	ERROR	msgwriter	src/common/scoped_message_writer.h:94	Error: Couldn't connect to daemon
Error: Couldn't connect to daemon

Port is opened, needing advice.

# Discussion History
## dEBRUYNE-1 | 2017-10-27T13:49:33+00:00
Can you try v0.11.1.0?

## dEBRUYNE-1 | 2017-12-13T11:19:09+00:00
If the issue is strictly related to the daemon, please open an issue on monero-project/monero. 

+resolved

# Action History
- Created by: ckellingc | 2017-09-03T01:54:25+00:00
- Closed at: 2017-12-13T11:54:15+00:00
