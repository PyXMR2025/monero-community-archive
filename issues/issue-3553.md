---
title: 'Question: View screen'
source_url: https://github.com/xmrig/xmrig/issues/3553
author: AngryDragonflyStudios
assignees: []
labels: []
created_at: '2024-09-16T15:13:06+00:00'
updated_at: '2024-09-16T16:21:10+00:00'
type: issue
status: closed
closed_at: '2024-09-16T16:21:10+00:00'
---

# Original Description
I'm running Linux, and i been trying to google to find the answer, but i have xmrig running in background, is there a command that i can run when i SSH in to view the console for the running pid process so i can monitor the progress again after running overnight?

# Discussion History
## geekwilliams | 2024-09-16T16:11:12+00:00
Why not run xmrig in the foreground, but use a [screen](https://en.wikipedia.org/wiki/GNU_Screen) window to keep an eye on it?  You can detach and reattach to the screen session, even through ssh.   

Another option would be to have xmrig output to a log file, which you can then monitor with tail. [See documentation here.](https://xmrig.com/docs/miner/command-line-options#logging). If you are using config.json, find the line "log-file": null, and change it's value.  

# Action History
- Created by: AngryDragonflyStudios | 2024-09-16T15:13:06+00:00
- Closed at: 2024-09-16T16:21:10+00:00
