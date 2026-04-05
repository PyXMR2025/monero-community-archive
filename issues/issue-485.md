---
title: Systemd service - SIGTERM received, exiting
source_url: https://github.com/xmrig/xmrig/issues/485
author: DrStein99
assignees: []
labels: []
created_at: '2018-03-30T02:08:17+00:00'
updated_at: '2018-07-03T18:48:30+00:00'
type: issue
status: closed
closed_at: '2018-07-03T18:48:30+00:00'
---

# Original Description
I try setup xmrig as a system service, like the rest of my applications.  Unfortunately, I fail to get this to work.

`[2018-03-28 21:20:05] SIGTERM received, exiting`

Here is my service:

```
[Unit]
Description=xmrig miner
After=network.target

[Service]
Type=simple
GuessMainPID=no
ExecStart=/usr/src/xmrig25/build/xmrig -B -c /usr/src/xmrig25/build/config.json 
#Restart=on-failure
User=drstein99
LimitMEMLOCK=infinity

[Install]
WantedBy=multi-user.target

```

Does anyone have advice on what I am doing wrong?  

# Discussion History
## L1LjSHX | 2018-03-30T16:17:05+00:00
remove -B option

## DrStein99 | 2018-03-30T16:52:04+00:00
Ok.  I replace

`ExecStart=/usr/src/xmrig25/build/xmrig -B -c /usr/src/xmrig25/build/config.json`

with

`ExecStart=/usr/src/xmrig25/build/xmrig -c /usr/src/xmrig25/build/config.json`

Same issue - no change in the result.


# Action History
- Created by: DrStein99 | 2018-03-30T02:08:17+00:00
- Closed at: 2018-07-03T18:48:30+00:00
