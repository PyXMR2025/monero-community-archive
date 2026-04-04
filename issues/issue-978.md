---
title: Cannot Connect to Daemon
source_url: https://github.com/monero-project/monero-gui/issues/978
author: alexbellotta
assignees: []
labels:
- resolved
created_at: '2017-11-29T15:36:44+00:00'
updated_at: '2018-11-18T15:00:35+00:00'
type: issue
status: closed
closed_at: '2018-11-18T15:00:35+00:00'
---

# Original Description
Height: 81998/1453682 (5.6%) on mainnet, not mining, net hash 4.88 MH/s, v1, up to date, 6(out)+0(in) connections, uptime 0d 2h 6m 20s

2017-11-29 15:32:31.322	11060	ERROR	net.http	contrib/epee/include/net/http_client.h:444	Unexpected recv fail
Error: Couldn't connect to daemon: 127.0.0.1:18081


# Discussion History
## dEBRUYNE-1 | 2017-12-01T11:48:43+00:00
Which operating system are you using?

## alexbellotta | 2017-12-01T11:52:14+00:00

Windows 10
--
Inviato da Libero Mail per Android Venerdì, 01 Dicembre 2017, 00:48PM +01:00 da dEBRUYNE-1  notifications@github.com :

>Which operating system are you using?
>—
>You are receiving this because you authored the thread.
>Reply to this email directly,  view it on GitHub , or  mute the thread .


## jordangunderson | 2017-12-20T11:42:20+00:00
I'm wondering whether this isn't a duplicate issue of #890.

## dEBRUYNE-1 | 2017-12-20T12:19:21+00:00
@alex34qw Apologies for the late response. Can you try this guide? https://monero.stackexchange.com/questions/6825/i-am-using-the-gui-and-my-daemon-doesnt-start-anymore

@jordangunderson: Yes. I'll close once alex34qw answers. 

## erciccione | 2018-11-18T14:12:58+00:00
duplicate and related to old version

+resolved

# Action History
- Created by: alexbellotta | 2017-11-29T15:36:44+00:00
- Closed at: 2018-11-18T15:00:35+00:00
