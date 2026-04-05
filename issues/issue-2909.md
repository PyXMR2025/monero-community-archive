---
title: start.cmd - auto close initial cmd window after calling xmrig as it is useless
  to stay open
source_url: https://github.com/xmrig/xmrig/issues/2909
author: blackgis
assignees: []
labels: []
created_at: '2022-01-29T16:15:13+00:00'
updated_at: '2023-09-02T08:06:29+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Could the start.cmd file improved to not have open the initial cmd window:

Full replacement:

`SET current_path=%~dp0
start /d "%current_path:~0,-1%" xmrig.exe`

# Discussion History
## geekwilliams | 2023-09-02T08:06:03+00:00
Not sure what the start.cmd file is you're using.  There isn't one included in the repo.  You can specify the "background": true option in the config.json file to keep a window from popping up when when you start the xmrig executable

See documentation here: https://xmrig.com/docs/miner/config/misc

# Action History
- Created by: blackgis | 2022-01-29T16:15:13+00:00
