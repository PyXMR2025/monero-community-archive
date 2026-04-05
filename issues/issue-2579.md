---
title: 'log rotate compatibility : no new log file created after rotating log.'
source_url: https://github.com/xmrig/xmrig/issues/2579
author: ZwaZo22
assignees: []
labels: []
created_at: '2021-09-14T22:37:05+00:00'
updated_at: '2021-09-16T18:24:13+00:00'
type: issue
status: closed
closed_at: '2021-09-16T18:24:13+00:00'
---

# Original Description
**Describe the bug**

When using logrotate on the XMrig log, a new empty log file is not created, leaving XMrig without log output when ran in background.

**To Reproduce**

Run logrotate against XMrig log file.

**Expected behavior**

A new empty xyz.log file should be created to continue the logging.

**Required data**

relevant lines in config.json : 

 "background": true,
 "log-file": "/home/xmr/xmrig/xmrig.log",

logrotate configuration file for XMrig in /etc/logrotate.d/ : 

/home/xmr/xmrig/*.log
{
    rotate 7
    daily
    missingok
    delaycompress
    nocreate
}

 - OS: [e.g. Windows]
Ubuntu 20.04 server

 - For GPU related issues: information about GPUs and driver version.
N/A

**Additional context**
Add any other context about the problem here.
headless server


# Discussion History
## SChernykh | 2021-09-14T22:54:32+00:00
Did you try to remove `nocreate` from logrotate config?

## ZwaZo22 | 2021-09-16T18:24:13+00:00
It works without the `nocreate` option. Thanks !

# Action History
- Created by: ZwaZo22 | 2021-09-14T22:37:05+00:00
- Closed at: 2021-09-16T18:24:13+00:00
