---
title: '''W Unable to send transaction(s), no available connections'' at startup '
source_url: https://github.com/monero-project/monero/issues/7200
author: unamefailed
assignees: []
labels: []
created_at: '2020-12-27T07:30:12+00:00'
updated_at: '2023-05-29T01:51:24+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
```
2020-12-27 07:15:43.162	I **********************************************************************
2020-12-27 07:15:43.162	I The daemon will start synchronizing with the network. This may take a long time to complete.
2020-12-27 07:15:43.162	I 
2020-12-27 07:15:43.162	I You can set the level of process detailization through "set_log <level|categories>" command,
2020-12-27 07:15:43.162	I where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).
2020-12-27 07:15:43.162	I 
2020-12-27 07:15:43.162	I Use the "help" command to see the list of available commands.
2020-12-27 07:15:43.162	I Use "help <command>" to see a command's documentation.
2020-12-27 07:15:43.162	I **********************************************************************
2020-12-27 07:15:43.187	W Unable to send transaction(s), no available connections
```


It could be confusing.


# Discussion History
## selsta | 2021-01-08T05:46:48+00:00
@vtnerd AFAIK this issue was introduced with #7021, it is only a warning message but it seems confusing.

## scramblr | 2023-05-29T01:51:24+00:00
Yeah just a little confusing. 

# Action History
- Created by: unamefailed | 2020-12-27T07:30:12+00:00
