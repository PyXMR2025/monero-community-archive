---
title: Mine just when i inactive
source_url: https://github.com/xmrig/xmrig/issues/760
author: LearnMiner
assignees: []
labels:
- wontfix
created_at: '2018-09-22T13:30:51+00:00'
updated_at: '2018-11-05T14:18:20+00:00'
type: issue
status: closed
closed_at: '2018-11-05T14:18:20+00:00'
---

# Original Description
How can start mining just when i inactive ?

# Discussion History
## ghost | 2018-09-24T01:49:03+00:00
By scheduled tasks.
Cmd:
`schtasks /create /tn "<app>" /tr <what> /sc onidle /i <time>`
If it is does work, create task manually.


## LearnMiner | 2018-09-26T12:46:15+00:00
thanks but have 1 ask..

/tr <what> idk what i need write there

## ghost | 2018-09-29T14:46:30+00:00
<what> - command or path to file.
Example: schtasks /create /tn "Miner" /tr "C:\miner.exe" /sc onidle /i 10

## LearnMiner | 2018-09-30T13:54:31+00:00
ok is working good, this have startup or i need open always?


## ghost | 2018-10-08T02:47:06+00:00
Have startup. Please close issues.

# Action History
- Created by: LearnMiner | 2018-09-22T13:30:51+00:00
- Closed at: 2018-11-05T14:18:20+00:00
