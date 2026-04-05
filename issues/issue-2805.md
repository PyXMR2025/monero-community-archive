---
title: Cant run it trough systemd
source_url: https://github.com/xmrig/xmrig/issues/2805
author: samsagaz
assignees: []
labels: []
created_at: '2021-12-10T15:07:17+00:00'
updated_at: '2021-12-10T20:10:03+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**
When try to start xmrig trough systemd dont works

**To Reproduce**
Compiled the src, and run it from console works. but when run it trough systemd (to autostart on boot) dont

Someone know why this happend? SOmeone have some working version of systemd script?

# Discussion History
## Spudz76 | 2021-12-10T20:09:05+00:00
Put this in `/lib/systemd/system/xmrig.service` and put your xmrig in `/opt/xmrig/` or mass replace the path if you want to put it somewhere improper :)

```
[Unit]
Description=xmrig
After=network-online.target systemd-modules-load.service
Wants=network-online.target systemd-modules-load.service
AssertFileNotEmpty=/opt/xmrig/config.json

[Service]
Type=simple
User=root
Group=root
Restart=always
KillSignal=SIGINT
LimitMEMLOCK=8G
WorkingDirectory=/opt/xmrig
SyslogIdentifier=xmrig
TimeoutStartSec=30s
TimeoutStopSec=15s
ExecStart=/opt/xmrig/xmrig

[Install]
WantedBy=multi-user.target
```

`systemctl daemon-reload ; systemctl enable xmrig ; systemctl restart xmrig`

# Action History
- Created by: samsagaz | 2021-12-10T15:07:17+00:00
